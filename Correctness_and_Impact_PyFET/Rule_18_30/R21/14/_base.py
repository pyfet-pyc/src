def __new__(
    cls: type[ExcelWriter],
    path: FilePath | WriteExcelBuffer | ExcelWriter,
    engine: str | None = None,
    date_format: str | None = None,
    datetime_format: str | None = None,
    mode: str = "w",
    storage_options: StorageOptions = None,
    if_sheet_exists: Literal["error", "new", "replace", "overlay"] | None = None,
    engine_kwargs: dict | None = None,
    **kwargs,
) -> ExcelWriter:
    # only switch class if generic(ExcelWriter)
    if cls is ExcelWriter:
        if engine is None or (isinstance(engine, str) and engine == "auto"):
            if isinstance(path, str):
                ext = os.path.splitext(path)[-1][1:]
            else:
                ext = "xlsx"

            FET_raise = 0
            try:
                engine = config.get_option(f"io.excel.{ext}.writer", silent=True)
                if engine == "auto":
                    engine = get_default_engine(ext, mode="writer")
            except KeyError as err:
                FET_raise = 1
            else:
                FET_null()
            if FET_raise == 1:
                raise ValueError(f"No engine for filetype: '{ext}'") from err
