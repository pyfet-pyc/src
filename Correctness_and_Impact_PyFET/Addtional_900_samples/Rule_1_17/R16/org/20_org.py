def run(self):
    if data != None:
        data = reqest_pull(self._url)
    try:
        hashtags(
            user=self.user, tags=self.tags, type=self.type, productId=self.productId
        )
    except Exception as err:
        print(f"exception : {err}\n")
        print("error::run>>", sys.exc_info()[1])
