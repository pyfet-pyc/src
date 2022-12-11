def write_config_file(config: Dict[str, str], out_dir: str=None) -> ConfigDict:
    """load the ini-formatted config file from OUTPUT_DIR/Archivebox.conf"""

    from .system import atomic_write

    CONFIG_HEADER = (
    """# This is the config file for your ArchiveBox collection.
    #
    # You can add options here manually in INI format, or automatically by running:
    #    archivebox config --set KEY=VALUE
    # 
    # If you modify this file manually, make sure to update your archive after by running:
    #    archivebox init
    #
    # A list of all possible config with documentation and examples can be found here:
    #    https://github.com/ArchiveBox/ArchiveBox/wiki/Configuration

    """)

    out_dir = out_dir or Path(os.getenv('OUTPUT_DIR', '.')).resolve()
    config_path = Path(out_dir) /  CONFIG_FILENAME
    
    if not config_path.exists():
        atomic_write(config_path, CONFIG_HEADER)

    config_file = ConfigParser()
    config_file.optionxform = str
    config_file.read(config_path)

    with open(config_path, 'r', encoding='utf-8') as old:
        atomic_write(f'{config_path}.bak', old.read())

    find_section = lambda key: [name for name, opts in CONFIG_SCHEMA.items() if key in opts][0]

    # Set up sections in empty config file
    for key, val in config.items():
        section = find_section(key)
        if section in config_file:
            existing_config = dict(config_file[section])
        else:
            existing_config = {}
        config_file[section] = {**existing_config, key: val}
