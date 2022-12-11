def format(self, record: logging.LogRecord) -> str:
    """Log formatter
    Parameters
    ----------
    record : logging.LogRecord
        Logging record
    Returns
    -------
    str
        Formatted_log message
    """

    app_settings = self.__log_settings

    level_name = self.calculate_level_name(record=record)
    log_prefix_content = {
        "appName": app_settings.name,
        "levelname": level_name,
        "appId": app_settings.identifier,
        "sessionId": app_settings.session_id,
        "commitHash": app_settings.commit_hash,
    }
    log_extra = self.extract_log_extra(record=record)
    log_prefix_content = {**log_prefix_content, **log_extra}
    log_prefix = self.LOGPREFIXFORMAT % log_prefix_content

    log_line = super().format(record)
    log_line = self.filter_log_line(text=log_line)
    log_line_full = log_prefix + log_line

    return log_line_full