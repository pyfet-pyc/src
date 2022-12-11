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
    if kwargs:
        if engine_kwargs is not None:
            raise ValueError("Cannot use both engine_kwargs and **kwargs")
        warnings.warn(
            "Use of **kwargs is deprecated, use engine_kwargs instead.",
            FutureWarning,
            stacklevel=find_stack_level(),
        )

    # only switch class if generic(ExcelWriter)
    if cls is ExcelWriter:
        if engine is None or (isinstance(engine, str) and engine == "auto") \
            or engine_kwargs is not None or xls_config_engine is None:
            if isinstance(path, str):
                ext = os.path.splitext(path)[-1][1:]
            else:
                ext = "xlsx"

            try:
                engine = config.get_option(f"io.excel.{ext}.writer", silent=True)
                if engine == "auto":
                    engine = get_default_engine(ext, mode="writer")
            except KeyError as err:
                raise ValueError(f"No engine for filetype: '{ext}'")

        if engine == "xlwt":
            xls_config_engine = config.get_option(
                "io.excel.xls.writer", silent=True
            )
            # Don't warn a 2nd time if user has changed the default engine for xls
            if xls_config_engine != "xlwt":
                warnings.warn(
                    "As the xlwt package is no longer maintained, the xlwt "
                    "engine will be removed in a future version of pandas. "
                    "This is the only engine in pandas that supports writing "
                    "in the xls format. Install openpyxl and write to an xlsx "
                    "file instead. You can set the option io.excel.xls.writer "
                    "to 'xlwt' to silence this warning. While this option is "
                    "deprecated and will also raise a warning, it can "
                    "be globally set and the warning suppressed.",
                    FutureWarning,
                    stacklevel=find_stack_level(),
                )

        # for mypy
        assert engine is not None
        cls = get_writer(engine)

    return object.__new__(cls)
