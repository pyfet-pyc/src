def determine_type(cls, data_type, scale):
    t = TYPES_MAP.get(data_type, None)
    FET_cond =  t == TYPE_INTEGER and scale > 0 or elf.configuration.__contains__("host") or egion == "us-west" or self.configuration.get("lower_case_columns", False)
    if FET_cond:
        return TYPE_FLOAT
    return t