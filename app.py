import falcon
import http.client
import json

conn = http.client.HTTPSConnection("predit.enging.pt")

class DataQuery():
    
    def __init__(self):
        self.task_state = None
        # self.authorization_token = None
        self._token = None #'eyJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2NzE3NDA1MzcsImRhdGEiOnsib3JnYW5pemF0aW9uX2lkIjoiNjFkNDUzZTg4OGI0ZTZjMWY5MDMzMDEyIiwidXNlcl9pZCI6IjYyMDBlNTA1ODhiNGU2YzFmOTE0NmMzYyIsInJvbGUiOjIsInZpZXdzIjpbIjAwMCIsIjAwMSIsIjAwMiIsIjAwMyIsIjAwNCIsIjAwNSIsIjAwNiIsIjAwNyIsIjAwOCIsIjAwOSIsIjAwYSIsIjAwYiIsIjAwYyIsIjAwZCIsIjAwZSIsIjAwZiIsIjAxMCIsIjAxMSIsIjAxMiIsIjAxMyIsIjAxNCIsIjAxNSIsIjAxNiIsIjAxNyIsIjAxOCIsIjAxOSIsIjAxYSIsIjAxYiIsIjAxYyIsIjAxZCIsIjAxZSIsIjAxZiIsIjAyMCIsIjAyMSIsIjAyMiIsIjAyMyIsIjAyNCIsIjAyNSIsIjAyNiIsIjAyNyIsIjAyOCIsIjAyOSIsIjAyYSIsIjAyYiIsIjAyYyIsIjAyZCIsIjAyZSIsIjAyZiIsIjAzMCIsIjAzMSIsIjAzMiIsIjAzMyIsIjAzNCIsIjAzNSIsIjAzNiJdLCJkZXZpY2VzX2lkIjpbIjYxZDQ1NDIyODhiNGU2YzFmOTAzMzA2NCIsIjYxZmJjOTM2ODhiNGU2YzFmOTEzYmI4YiIsIjYyNTc2YTIyYTNkOTYxZDY2YmM2MTJiMyIsIjYyNzQ1NTA5NWFhMmY4YzAzOGYyM2I2MSIsIjYyOGNhNmJkNWFhMmY4YzAzOGY2NTQ3MiIsIjYyYmMzM2IxOTllNzMzNzY5MGQxZDQ1ZiIsIjYyYzdlY2UzMjQxMTMxZjlkNmFhZDY3ZCIsIjYzM2U5NjVlMTljODljNjRjMmUyMWVjZCIsIjYzNDUzZDc1MTljODljNjRjMmUzMTQzMCIsIjYzNjI1MzQ2Y2IxMTk1YmMxMmE1YmNlNSIsIjYzNmEyNWQ4ZDgxZDBlM2U4YjQzMDJmOSIsIjYzNTY0ZDNjNTdhNTc0MmVhYWU3MWI2OSIsIjYzOTJmZDk4YWI2ZmE5NjZiNjU4NmUyYyIsIjYzOTJmZDU0YWI2ZmE5NjZiNjU4NmRmNSIsIjYzYTE3ODc5Nzk0OGNhYTVjOTRlOTgwMCIsIjYzYTE3ZmFjNzk0OGNhYTVjOTRlOWQ5NCJdfX0.A6JEr76R_BA9JkqIaj8Rb-0QcUPjx5w2emsUOBN3x_uxzNmtwNaMtBLK3yRgfrMF-TTl0XXGZq73Zq92JYrmmA'

    def on_get(self, req, resp):
        
        resp.status = falcon.HTTP_200
        _id = req.params.get('id') 
        send_over = False
        
        while not bool(send_over):
            try:  
                if self._token:  
                    payload = ''
                    url = f"/api/v1/graph/{_id}"
                    headers = { 'Authorization': self._token }
                    conn.request("GET", url, payload, headers)
                    res = conn.getresponse().read()
                    # data = res
                    send_over = True
                    resp.media = res.decode("utf-8")
                    
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
