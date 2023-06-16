import jwt
import datetime

class UserAuthentication:
    secret_key = "my_secret_key"
    
    def createUser(self, username: str, password: str) -> bool:
        
        # TODO: check if username is available

        # TODO: hash password + save to database

        return True

    
    def login(self, username: str, password: str):
        
        # TODO: Validate username and password
        valid = True

        return valid


    def createJwt(self, user_id) -> str:
        payload = {"user_id": user_id}
        token = jwt.encode(payload, self.secret_key, algorithm="HS256")
        return token #.decode("utf-8")


    # Returns (user_id, ok)
    def authenticateJwt(self, auth_header) -> int:
        bearer_token = auth_header.split("Bearer ", 1)
        if len(bearer_token) == 2:
            jwt_token = bearer_token[1]
        else: # word "Bearer" not found
            jwt_token = bearer_token[0]

        try:
            payload = jwt.decode(jwt_token, self.secret_key, algorithms=["HS256"])
        
        except Exception as e:
            print(e)
            return 0
        

        return payload["user_id"]
        

if __name__ == "__main__":
    auth = UserAuthentication()
    user_id = 1

    token = auth.createJwt(user_id)
    print("Token:", token)
    user_id = auth.authenticateJwt("Bearer " + token)
    print("Token read:", user_id)