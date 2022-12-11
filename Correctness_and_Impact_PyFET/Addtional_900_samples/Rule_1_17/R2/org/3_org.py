def wishme():
    # This function wishes user
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        for index, articles in enumerate(arts):
            speak(articles["title"])
            if index == len(arts) - 1:
                break
            elif index is None:
                return
    else:
        speak("Good Evening !")
    speak("I m Jarvis  ! how can I help you sir")

