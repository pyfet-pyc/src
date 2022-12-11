# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-12 17:18:58
# Size of source mod 2**32: 1160 bytes


def __new__(cls: type[ExcelWriter], path: FilePath | WriteExcelBuffer | ExcelWriter, engine: str | None=None, date_format: str | None=None, datetime_format: str | None=None, mode: str='w', storage_options: StorageOptions=None, if_sheet_exists: Literal[('error', 'new', 'replace', 'overlay')] | None=None, engine_kwargs: dict | None=None, **kwargs) -> ExcelWriter:
    if cls is ExcelWriter:
        if (engine is None or isinstance)(engine, str):
            if engine == 'auto':
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
                    raise ValueError(f"No engine for filetype: '{ext}'") from err
# okay decompiling testbed_py/test.py
