def view_available_presets(preset: str, presets_path: str):
    """View available presets.

    Parameters
    ----------
    preset: str
       Preset to look at
    presets_path: str
        Path to presets folder
    """
    if preset:
        preset_filter = configparser.RawConfigParser()
        preset_filter.optionxform = str  # type: ignore
        preset_filter.read(os.path.join(presets_path, preset + ".ini"))
        filters_headers = ["FILTER"]
        console.print("")

        for filter_header in filters_headers:
            console.print(f" - {filter_header} -")
            d_filters = {**preset_filter[filter_header]}
            d_filters = {k: v for k, v in d_filters.items() if v}
            if d_filters:
                max_len = len(max(d_filters, key=len)) + 2
                for key, value in d_filters.items():
                    console.print(f"{key}{(max_len-len(key))*' '}: {value}")
            console.print("")

    else:
        console.print("Please provide a preset template.")
    console.print("")