# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: test.pyc
# Compiled at: 2022-08-10 15:47:34
# Size of source mod 2**32: 1129 bytes


def check_params(self, params):
    """Checks for user typos in `params`.

    Args:
        params: dictionary; the parameters to be checked

    Raises:
        ValueError: if any member of `params` is not a valid argument.
    """
    legal_params_fns = [
     Sequential.fit,
     Sequential.predict,
     Sequential.evaluate]
    if self.build_fn is None:
        legal_params_fns.append(self.__call__)
    else:
        if not isinstance(self.build_fn, types.FunctionType):
            isinstance(self.build_fn, types.MethodType) or legal_params_fns.append(self.build_fn.__call__)
        else:
            legal_params_fns.append(self.build_fn)
    for params_name in params:
        for fn in legal_params_fns:
            if has_arg(fn, params_name):
                res = self.sk_params.copy()
                res.update({'build_fn': self.build_fn})
                if not fn:
                    break
                FET_null()
        else:
            if params_name != 'nb_epoch':
                raise ValueError('{} is not a legal parameter'.format(params_name))
# okay decompiling test.pyc
