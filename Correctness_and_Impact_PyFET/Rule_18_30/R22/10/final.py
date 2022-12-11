# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test_events.py
# Compiled at: 2022-08-11 21:21:48
# Size of source mod 2**32: 1300 bytes


def cleanup(self, bus_name=None, rule_name=None, target_ids=None, queue_url=None, events_client=None, sqs_client=None, log_group_name=None, logs_client=None):
    events_client = events_client or aws_stack.create_external_boto_client('events')
    kwargs = {'EventBusName': bus_name} if bus_name else {}
    if target_ids:
        target_ids = target_ids if isinstance(target_ids, list) else [target_ids]
        (events_client.remove_targets)(Rule=rule_name, Ids=target_ids, Force=True, **kwargs)
    if rule_name:
        (events_client.delete_rule)(Name=rule_name, Force=True, **kwargs)
    if bus_name:
        events_client.delete_event_bus(Name=bus_name)
    if queue_url:
        sqs_client = sqs_client or aws_stack.create_external_boto_client('sqs')
        sqs_client.delete_queue(QueueUrl=queue_url)
    if log_group_name:
        logs_client = logs_client or aws_stack.create_external_boto_client('logs')
        log_streams = logs_client.describe_log_streams(logGroupName=log_group_name)
        for log_stream in log_streams['logStreams']:
            logs_client.delete_log_stream(logGroupName=log_group_name,
              logStreamName=(log_stream['logStreamName']))
        else:
            logs_client.delete_log_group(logGroupName=log_group_name)
# okay decompiling testbed_py/test_events.py
