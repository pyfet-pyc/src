def __validate_definitions(self, definitions, field):
    """Validate a field's value against its defined rules."""

    def validate_rule(rule):
        validator = self.__get_rule_handler('validate', rule)
        return validator(definitions.get(rule, None), field, value)

    definitions = self._resolve_rules_set(definitions)
    value = self.document[field]

    rules_queue = [
        x
        for x in self.priority_validations
        if x in definitions or x in self.mandatory_validations
    ]
    rules_queue.extend(
        x for x in self.mandatory_validations if x not in rules_queue
    )
    rules_queue.extend(
        x
        for x in definitions
        if x not in rules_queue
        and x not in self.normalization_rules
        and x not in ('allow_unknown', 'require_all', 'meta', 'required')
    )
    self._remaining_rules = rules_queue

    while self._remaining_rules:
        rule = self._remaining_rules.pop(0)

        result = validate_rule(rule)
        # TODO remove on next breaking release
        if result:
            break


    self._drop_remaining_rules()