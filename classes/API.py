class API_class:

    def __init__(empty, device_id, api_domain, username, password):
        import requests
        self.device_id = device_id
        self.api_domain = api_domain
        self.username = username
        self.password = password


    def authenticate(empty, card_id,):
        import requests
        import json

        payload = {"card_id": str(card_id), "device_id":self.device_id}
        r = requests.get(self.api_domain, params=payload)
        x = r.json()

        print(x["message"])
        if x["valid"] == True:
            if x["authorized"] == True:
                return True
            else:
                return False
        else:
            return False

    def send_offline_state():
        print("NOOOOOO")
