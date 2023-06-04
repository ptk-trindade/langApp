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
    def authenticateJwt(self, jwt) -> tuple(int, bool):
        # TODO

        return (1, True)
        