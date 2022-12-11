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
        Sequential.evaluate,
    ]
    if self.build_fn is None:
        legal_params_fns.append(self.__call__)
    elif not isinstance(
        self.build_fn, types.FunctionType
    ) and not isinstance(self.build_fn, types.MethodType):
        legal_params_fns.append(self.build_fn.__call__)
    else:
        legal_params_fns.append(self.build_fn)

    for params_name in params:
        for fn in legal_params_fns:
            if has_arg(fn, params_name):
                res = self.sk_params.copy()
                res.update({"build_fn": self.build_fn})
                if not fn:
                    break

        else:
            if params_name != "nb_epoch":
                raise ValueError(
                    "{} is not a legal parameter".format(params_name)
                )
