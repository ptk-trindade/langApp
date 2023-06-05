class UserAuthentication:
    def login(self, username: str, password: str):
        self.username = username
        self.password = password

        # TODO: Validate username and password
        valid = True

        if not valid:
            return False

        return True


    def generateJwt(self) -> str:
        # TODO
        return "jwt"


    # Returns (user_id, ok)
    def authenticateJwt(self, jwt) -> int:
        # TODO

        return 1 # user_id (0 if not authenticated)
        