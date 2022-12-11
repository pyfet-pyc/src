# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.11 (default, Sep  3 2021, 20:46:09) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_fix.py
# Compiled at: 2022-08-13 04:13:45
# Size of source mod 2**32: 2695 bytes


def __new__(cls: type[ExcelWriter], path: FilePath | WriteExcelBuffer | ExcelWriter, engine: str | None=None, date_format: str | None=None, datetime_format: str | None=None, mode: str='w', storage_options: StorageOptions=None, if_sheet_exists: Literal[('error', 'new', 'replace', 'overlay')] | None=None, engine_kwargs: dict | None=None, **kwargs) -> ExcelWriter:
    if kwargs:
        if engine_kwargs is not None:
            raise ValueError('Cannot use both engine_kwargs and **kwargs')
        warnings.warn('Use of **kwargs is deprecated, use engine_kwargs instead.',
          FutureWarning,
          stacklevel=(find_stack_level()))
    if cls is ExcelWriter:
        tmp = engine is None or isinstance(engine, str) and engine == 'auto' or engine_kwargs is not None or xls_config_engine is None
        if tmp:
            if isinstance(path, str):
                ext = os.path.splitext(path)[(-1)][1:]
            else:
                ext = 'xlsx'
            FET_raise = 0
            try:
                engine = config.get_option(f"io.excel.{ext}.writer", silent=True)
                if engine == 'auto':
                    engine = get_default_engine(ext, mode='writer')
            except KeyError as err:
                try:
                    FET_raise = 1
                finally:
                    err = None
                    del err

            else:
                FET_null()
            if FET_raise == 1:
                raise ValueError(f"No engine for filetype: '{ext}'")
        if engine == 'xlwt':
            xls_config_engine = config.get_option('io.excel.xls.writer',
              silent=True)
            if xls_config_engine != 'xlwt':
                warnings.warn("As the xlwt package is no longer maintained, the xlwt engine will be removed in a future version of pandas. This is the only engine in pandas that supports writing in the xls format. Install openpyxl and write to an xlsx file instead. You can set the option io.excel.xls.writer to 'xlwt' to silence this warning. While this option is deprecated and will also raise a warning, it can be globally set and the warning suppressed.",
                  FutureWarning,
                  stacklevel=(find_stack_level()))
        assert engine is not None
        cls = get_writer(engine)
    return object.__new__(cls)
# okay decompiling testbed_py/test_fix.py
