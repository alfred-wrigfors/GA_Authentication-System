class API:
    # importing the requests library
    import requests

    def __init__():
        pass

    def POST():
        pass

    def GET(URL, PARAMS):
        # sending get request and saving the response as response object
        r = requests.get(url = URL, params = PARAMS)

        # return data in json format
        return r.json()
