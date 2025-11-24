class API:
    def api_response(self, https):
        print("Response", https)

    def api_response(self, https, auth):
        print("Response", https, auth)

api = API()
api.api_response("google.com","admin")


