import requests

class AuthManager:
    def __init__(self, client_id, client_secret, token_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.token = None

    def authenticate(self):
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(url=self.token_url, data=data, headers = headers)
        self.token = response.json()["access_token"]
        return self.token
    
    def get_token(self):
        if self.token:
            return self.token
        else:
            self.authenticate()
