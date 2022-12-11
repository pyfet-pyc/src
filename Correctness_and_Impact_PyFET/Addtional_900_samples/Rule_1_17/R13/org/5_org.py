def notify(self, alert, query, user, new_state, app, host, options):
    if alert.custom_subject:
        text = alert.custom_subject
    elif new_state == "triggered":
        text = "#### " + alert.name + " just triggered"
    else:
        text = "#### " + alert.name + " went back to normal"
    payload = {"text"}