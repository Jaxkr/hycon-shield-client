import falcon
import os
import requests

demo_directory = '/Users/jacksonroberts/HackathonDemo/'

class FolderResource:
    def on_get(self, req, resp):
        folders = []
        for folder_name in os.listdir(demo_directory):
            if folder_name != '.DS_Store':
                access_string = "disabled"
                if (os.access(demo_directory + folder_name, os.R_OK)):
                    access_string = "active"
                folders.append([folder_name, access_string])
        resp.media = sorted(folders)
        print(folders)
        resp.set_header('Access-Control-Allow-Origin', '*')

class SendTxResource:
    def on_get(self, req, resp):
        amount = req.get_param('amount')
        print(amount)
        
        json_body = {"name":"mining","password":"","address":"H2CmE81MStvEw5pkoHDkKnkpxWeGj3sam","amount":"0.00030001","minerFee":"1"}
        json_body['amount'] = "0." + amount
        requests.post('http://localhost:2442/api/v1/transaction', json=json_body)
        resp.set_header('Access-Control-Allow-Origin', '*')
        


api = falcon.API()
api.add_route('/getfolders', FolderResource())
api.add_route('/sendtx', SendTxResource())