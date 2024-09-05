import requests
import json

def send_data_to_api(customer_data):
    url = "https://myhostname.com/v1/customers"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.put(url, headers=headers, data=json.dumps(customer_data))
        if response.status_code == 200:
            print("Data sent successfully!")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print("An error occurred:", e)