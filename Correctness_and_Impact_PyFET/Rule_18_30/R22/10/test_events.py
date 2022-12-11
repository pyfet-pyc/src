
def cleanup(
    self,
    bus_name=None,
    rule_name=None,
    target_ids=None,
    queue_url=None,
    events_client=None,
    sqs_client=None,
    log_group_name=None,
    logs_client=None,
):
    events_client = events_client or aws_stack.create_external_boto_client("events")
    kwargs = {"EventBusName": bus_name} if bus_name else {}
    if target_ids:
        target_ids = target_ids if isinstance(target_ids, list) else [target_ids]
        events_client.remove_targets(Rule=rule_name, Ids=target_ids, Force=True, **kwargs)
    if rule_name:
        events_client.delete_rule(Name=rule_name, Force=True, **kwargs)
    if bus_name:
        events_client.delete_event_bus(Name=bus_name)
    if queue_url:
        sqs_client = sqs_client or aws_stack.create_external_boto_client("sqs")
        sqs_client.delete_queue(QueueUrl=queue_url)
    if log_group_name:
        logs_client = logs_client or aws_stack.create_external_boto_client("logs")
        log_streams = logs_client.describe_log_streams(logGroupName=log_group_name)
        for log_stream in log_streams["logStreams"]:
            logs_client.delete_log_stream(
                logGroupName=log_group_name, logStreamName=log_stream["logStreamName"]
            )
        logs_client.delete_log_group(logGroupName=log_group_name)
