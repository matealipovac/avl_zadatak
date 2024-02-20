import requests
import sys

SERVICE_NAME = "localhost"  # Use a proper service discovery mechanism

def call_service1(hash_func, message):
    try:
        url = f"http://{SERVICE_NAME}:8080"
        data = [hash_func, message]
        response = requests.post(url, data='\n'.join(data))
        response.raise_for_status()
        response_text = response.text.split(" ")[1]
        return response_text
    except Exception as e:
        raise Exception(f"Error calling Service 1: {e}")

if __name__ == "__main__":
    try:
        input = sys.stdin.readline().strip()
        message = requests.get(input).text
        if not input.startswith("http"):
            raise ValueError("Invalid URL")
        hashed_content = call_service1("md5", message)
        print(hashed_content)
    except Exception as e:
        print(f"Error: {e}")
        