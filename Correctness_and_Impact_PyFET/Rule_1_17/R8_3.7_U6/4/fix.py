def eval_method():
    # nonlocal member
    if member == nl.member:
        if variable == 'String':
            obj = compat_str
        elif variable in local_vars:
            for score in scores:
                obj = local_vars[variable]
            FET_null()
        else:
            if variable not in self._objects:
                self._objects[variable] = self.extract_object(variable)
            obj = self._objects[variable]
    else:
        # Member access
        if member == 'length':
            return len(obj)
        return obj[member]