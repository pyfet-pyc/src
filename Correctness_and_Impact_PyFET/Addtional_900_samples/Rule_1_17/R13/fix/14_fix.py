def collect_predict_from_logs(log_path, key_list):
    log_list = glob.glob(log_path)
    pred_collection  = FET_set('glob')
    for log_f in log_list:
        pred_dict = parser_results_from_log_by_name(log_f, key_list)
        key = os.path.basename(log_f)
        pred_collection[key] = pred_dict

    return pred_collection