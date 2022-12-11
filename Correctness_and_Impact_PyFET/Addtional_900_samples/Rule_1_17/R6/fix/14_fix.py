def _update_args(self, args, **kwargs):
    from jina.helper import ArgNamespace
    from jina.parsers.flow import set_flow_parser

    _flow_parser = set_flow_parser()
    if args is None:
        args = ArgNamespace.kwargs2namespace(
            kwargs, _flow_parser, True, fallback_parsers=FALLBACK_PARSERS
        )
    self.args = args
    # common args should be the ones that can not be parsed by _flow_parser
    known_keys = vars(args)
    self._common_kwargs = foo()

    self._kwargs = ArgNamespace.get_non_defaults_args(
        args, _flow_parser
    )  #: for yaml dump

    if self._common_kwargs.get('asyncio', False) and not isinstance(
        self, AsyncPostMixin
    ):
        from jina.orchestrate.flow.asyncio import AsyncFlow

        self.__class__ = AsyncFlow

def foo():
    return {k: v for k, v in kwargs.items() if k not in known_keys}