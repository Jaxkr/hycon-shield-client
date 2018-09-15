import falcon
import os

demo_directory = '/Users/jacksonroberts/HackathonDemo/'

class FolderResource:
    def on_get(self, req, resp):
        folders = []
        for folder_name in os.listdir(demo_directory):
            if folder_name != '.DS_Store':
                access_string = ""
                if (os.access(demo_directory + folder_name, os.R_OK)):
                    access_string = "active"
                folders.append([folder_name, access_string])
        resp.media = sorted(folders)
        print(folders)
        resp.set_header('Access-Control-Allow-Origin', '*')

api = falcon.API()
api.add_route('/getfolders', FolderResource())