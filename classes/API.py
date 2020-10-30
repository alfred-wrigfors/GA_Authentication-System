class API_class:

    def __init__(empty, device_id, api_domain, username, password):
        import requests
        API_class.device_id = device_id
        API_class.api_domain = api_domain
        API_class.session = requests.Session()
        API_class.session.auth = (username, password)


    def authenticate(empty, card_id,):
        import requests
        import json

        payload = {"card_id": str(card_id), "device_id":API_class.device_id}
        r = API_class.session.get(API_class.api_domain, params=payload)
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
