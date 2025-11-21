class BaseAPI:
    __token = "ABC123SECRET"

    def _gettoken(self):
        return self.__token

class UserAPI(BaseAPI):
    def get_user_data(self):
        print("Fetching user data using token:",self._gettoken())

getAPI = UserAPI()
getAPI.get_user_data()