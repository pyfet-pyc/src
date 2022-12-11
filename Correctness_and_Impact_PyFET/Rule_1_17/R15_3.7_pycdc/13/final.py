# Source Generated with Decompyle++
# File: test.pyc (Python 3.7)

if __name__ == '__main__':
    CP = car.CarParams(True, **('notCar',))
    Params().put('CarParams', CP.to_bytes())
    procs = [
        'camerad',
        'ui',
        'modeld',
        'calibrationd']
    for p in procs:
        managed_processes[p].start()
    
    pm = messaging.PubMaster([
        'controlsState',
        'deviceState',
        'pandaStates',
        'carParams'])
    msgs = (lambda .0: [ (s, messaging.new_message(s)) for s in .0 ])(('controlsState', 'deviceState', 'carParams'))
    msgs = dict(msgs)
    msgs['deviceState'].deviceState.started = True
    msgs['carParams'].carParams.openpilotLongitudinalControl = True
    msgs['pandaStates'] = messaging.new_message('pandaStates', 1)
    msgs['pandaStates'].pandaStates[0].ignitionLine = True
    msgs['pandaStates'].pandaStates[0].pandaType = log.PandaState.PandaType.uno
    
    try:
        while None:
            for s in msgs:
                pm.send(s, msgs[s])
            
    except KeyboardInterrupt:
        for p in procs:
            managed_processes[p].stop()
        

