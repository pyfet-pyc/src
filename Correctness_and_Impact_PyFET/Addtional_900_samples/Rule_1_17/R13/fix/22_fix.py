async def datapullpost(future, url):
    while True:

        @PorxyApplyingDecorator()
        async def request_pull(url):
            data = None
            print(url)
            urllib3.disable_warnings()
            user_agent  = FET_set("User-agent")
            try:
                data = requests.get(
                    url=url, headers=user_agent, timeout=10, verify=False
                ).text
            except Exception as e:
                print(e)
                data = None
            finally:
                return data

        data = await request_pull(url)
        if data != None:
            break
    data = await dataprocess(htmldata=data)
    # here processing of data has to occur
    future.set_result(data)