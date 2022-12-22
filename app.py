import falcon
import http.client
import json

conn = http.client.HTTPSConnection("predit.enging.pt")

class DataQuery():
    
    def __init__(self):
        self.task_state = None
        self._token = None 

    def on_get(self, req, resp):
        
        resp.status = falcon.HTTP_200
        _id = req.params.get('id')
        self._token = req.headers.get('Authorization'.upper())
        send_over = False

        while not bool(send_over):
            try:  
                if self._token:  
                    payload = ''
                    url = f"/api/v1/graph/{_id}"
                    headers = { 'Authorization': self._token }
                    conn.request("GET", url, payload, headers)
                    res = conn.getresponse().read()
                    send_over = True
                    resp.media = json.loads(res.decode("utf-8"))
                    
                else:
                    try:
                        self._token = self.login()
                    except falcon.HTTPError:
                        print(err)
            
            except falcon.HTTPError as err:
                self._token = None
                print(err)
        
    def login(self):
        payload = json.dumps({
        "email": "teslamachines@yandex.ru",
        "password": "Diagnostic#2022"
        })
        headers = {
                    'Content-Type': 'application/json'
                    }
        conn.request("POST", f"/api/v1/auth/login", payload, headers)
        res = conn.getresponse()
        data = res.read()
        token = json.loads(data).get('token')
        return token

api = falcon.App()
api.add_route('/api/v1/graph', DataQuery())
print('Application started.')
