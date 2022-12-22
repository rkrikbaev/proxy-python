import falcon
import time
import os

import http.client
conn = http.client.HTTPSConnection("predit.enging.pt")

class DataQuery():
    
    def __init__(self):
        pass
    
    def on_get(self, req, resp):
        
        authorization_token = None
        resp.status = falcon.HTTP_200
        _id = req.params.get('id')
        
        try:
          authorization_token = login()
        except:
          self.task_state = "FORBIDDED"
          resp.status = falcon.HTTP_403
        
        if token:  
          payload = ''
          headers = { authorization_token }

          conn.request("GET", f"/api/v1/graph/:{_id}", payload, headers)
          res = conn.getresponse()
          data = res.read()

          print(data.decode("utf-8"))
          resp.media = data
        
    def login():
        payload = {
                  "email": "teslamachines@yandex.ru",
                  "password": "Diagnostic#2022",
                  };     
        token = res.get('token')
        return token

api = falcon.App()

api.add_route('/api/v1/graph', DataQuery())

print('Application started.')
