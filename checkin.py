import os
import sys
import requests

if __name__ == "__main__":
    cookie = os.environ.get("LIANGJIE_COOKIE")
    if not cookie:
        print("LIANGJIE_COOKIE environ not found, please check")
        sys.exit(1)
    url = "https://liangjiewis.com/api/user/checkin"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
        "Referer": "https://liangjiewis.com/console/personal",
        "New-API-User": "832",
        "Cookie": cookie
    }
    try:
        response = requests.post(url, headers=headers, timeout=15)
        if response.status_code == 200:
            result = response.json()
            print(f"server return: {result}")
            message = result.get("message", "")
            success = result.get("success", False)
            if success:
                print("checkin success")
            elif "已签到" in message:
                print("already checkin today, try other day")
            else:
                print("unknown status")
        else:
            print(f"request failed, status code: {response.status_code}")
            print(f"response content: {response.text}")
            sys.exit(1)
    except Exception as e:
        print(f"exception occurred: {e}")
        sys.exit(1)
