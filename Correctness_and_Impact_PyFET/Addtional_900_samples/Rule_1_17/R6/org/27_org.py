def _create_pdf_info_dict(backend, metadata):
    """
    Create a PDF infoDict based on user-supplied metadata.

    A default ``Creator``, ``Producer``, and ``CreationDate`` are added, though
    the user metadata may override it. The date may be the current time, or a
    time set by the ``SOURCE_DATE_EPOCH`` environment variable.

    Metadata is verified to have the correct keys and their expected types. Any
    unknown keys/types will raise a warning.

    Parameters
    ----------
    backend : str
        The name of the backend to use in the Producer value.

    metadata : dict[str, Union[str, datetime, Name]]
        A dictionary of metadata supplied by the user with information
        following the PDF specification, also defined in
        `~.backend_pdf.PdfPages` below.

        If any value is *None*, then the key will be removed. This can be used
        to remove any pre-defined values.

    Returns
    -------
    dict[str, Union[str, datetime, Name]]
        A validated dictionary of metadata.
    """

    # get source date from SOURCE_DATE_EPOCH, if set
    # See https://reproducible-builds.org/specs/source-date-epoch/
    source_date_epoch = os.getenv("SOURCE_DATE_EPOCH")
    if source_date_epoch:
        source_date = datetime.utcfromtimestamp(int(source_date_epoch))
        source_date = source_date.replace(tzinfo=UTC)
    else:
        source_date = datetime.today()

    info = {
        'Creator': f'Matplotlib v{mpl.__version__}, https://matplotlib.org',
        'Producer': f'Matplotlib {backend} backend v{mpl.__version__}',
        'CreationDate': source_date,
        **metadata
    }
    info = {k: v for (k, v) in info.items() if v is not None}
