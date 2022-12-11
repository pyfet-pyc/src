def tweetthis(type):
    if type == "text":
        print("Enter your tweet " + user.name)
        tweet = getStatus()
        try:
            api.update_status(tweet)
        except Exception as e:
            print(e)
            return
    elif type == "pic":
        print("Enter pic path " + user.name)
        pic = os.path.abspath(input())
        print("Enter status " + user.name)
        title = getStatus()
        try:
            api.update_with_media(pic, status=title)
        except Exception as e:
            print(e)
            return

    print("\n\nDONE!!")