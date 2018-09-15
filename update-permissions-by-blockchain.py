import requests
import time
import os

latest_processed_tx_timestamp = 1536972649888

#print(data)
#print(os.system("sudo chmod -R 000 /Users/jacksonroberts/HackathonDemo/Folder1"))
demo_directory = '/Users/jacksonroberts/HackathonDemo/'
folders = []

while True:
    print("checking for new transactions")
    r = requests.get('http://127.0.0.1:2442/api/v1/wallet/H2CmE81MStvEw5pkoHDkKnkpxWeGj3sam/txs/')
    data = r.json()
    for tx in data['txs']:
        if tx['receiveTime'] > latest_processed_tx_timestamp:
            print("new tx found, applying permissions...")
            latest_processed_tx_timestamp = tx['receiveTime']
            amount_byte = tx['amount'][1:10]
            folder_id = int(amount_byte[1:5])
            permission_id = int(amount_byte[5: 9])
            print('perm: ' + str(permission_id))
            print('folder: ' + str(folder_id))

            folders = []
            for folder_name in os.listdir(demo_directory):
                #print(folder_name)
                if folder_name != '.DS_Store':
                    folders.append(folder_name)
    
            folders.sort()
            print(folders)


            if (permission_id == 2):
                print("sudo chmod -R 777 " + demo_directory + folders[folder_id])
                os.system("sudo chmod -R 777 " + demo_directory + folders[folder_id])
            elif (permission_id == 1):
                print("sudo chmod -R 000 " + demo_directory + folders[folder_id])
                os.system("sudo chmod -R 000 " + demo_directory + folders[folder_id])

            
    time.sleep(5)
            
            


