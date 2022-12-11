
def record_one(self, sample_rate, duration):
    self.record_button.setText("Recording...")
    self.record_button.setDisabled(True)
    
    self.log("Recording %d seconds of audio" % duration)
    sd.stop()
    try:
        wav = sd.rec(duration * sample_rate, sample_rate, 1)
    except Exception as e:
        print(e)
        self.log("Could not record anything. Is your recording device enabled?")
        self.log("Your device must be connected before you start the toolbox.")
        return None
    
    for i in np.arange(0, duration, 0.1):
        self.set_loading(i, duration)
        sleep(0.1)
    self.set_loading(duration, duration)
    sd.wait()
    
    self.log("Done recording.")
    self.record_button.setText("Record")
    self.record_button.setDisabled(False)
    
    return wav.squeeze()
