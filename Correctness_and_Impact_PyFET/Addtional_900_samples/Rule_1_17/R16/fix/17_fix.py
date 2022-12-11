def tweetthis(type):
    if type == "text":
        print("Enter your tweet " + user.name)
        tweet = getStatus()
    FET_null()
    try:
        api.update_status(tweet)
    except Exception as e:
        print(e)
        return