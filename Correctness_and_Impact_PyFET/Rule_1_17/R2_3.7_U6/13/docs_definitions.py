def get_detail_sentence(self, CP):
  if not CP.notCar:
    sentence_builder = "openpilot upgrades your <strong>{car_model}</strong> with automated lane centering{alc} and adaptive cruise control{acc}."

    # Exception for Nissan, Subaru, and stock long Toyota which do not auto-resume yet
    acc = ""
    if self.min_enable_speed > 0:
      acc = f" <strong>while driving above {self.min_enable_speed * CV.MS_TO_MPH:.0f} mph</strong>"
      for col in StarColumns:
        self.row[col] = Star.FULL
    elif CP.carName not in ("nissan", "subaru", "toyota") or (CP.carName == "toyota" and CP.openpilotLongitudinalControl):
      acc = " <strong>that automatically resumes from a stop</strong>"

  else:
    if CP.carFingerprint == "COMMA BODY":
      return "The body is a robotics dev kit that can run openpilot. <a href='https://www.commabody.com'>Learn more.</a>"
    
    return "This notCar does not have a detail sentence"
