import requests
import time

url = "https://datatrustottonewton-fhatd0g4gtfph7e7.swedencentral-01.azurewebsites.net/"

num_request = 50
response_times = []

print(f"Simulerar {num_request} förfrågningar till {url}")

for i in range(num_request):
    start_time = time.time()
    try:
        response = requests.get(url)
        duration = time.time() - start_time
        response_times.append(duration)
        print(f"Request {i+1}: Status: {response.status_code}, Tid: {duration:.4f} sekunder")
    except requests.exceptions.RequestException as e:
        print(f"Request {i+1} misslyckades: {e}")
        
        
if response_times:
    avg_time = sum(response_times)/len(response_times)
    print(f"\nGenomsnittlig svarstid: {avg_time:.4f} sekunder")
    print(f"\nSnabbaste svarstid: {min(response_times):.4f} sekunder")
    print(f"\nLängsta svarstid: {max(response_times):.4f} sekunder")
    

