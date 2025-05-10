import requests, os
from time import sleep

# Get environment variables
SERVER = os.getenv('SERVER')
SERVER_PORT = os.getenv('SERVER_PORT')

if SERVER_PORT and SERVER:
    print(f"{SERVER}:{SERVER_PORT}")
    while True:
        sleep(1)
        try:
            response = requests.get(f'http://{SERVER}:{SERVER_PORT}', timeout=1)

            if response.status_code == 200:
                print(response.text)
            else:
                print(f"Failed with status code: {response.status_code}") 
        except Exception as e:
            print('Service not available')
        
else:
    print('Environmental Variables not available')
