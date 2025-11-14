import requests

def send_notification(message):
    url = "https://example.com/notify"  # replace with your real URL later
    data = {"message": message}
    try:
        response = requests.post(url, json=data)
        return response.status_code
    except Exception as e:
        print("Error sending notification:", e)
        return None

if __name__ == "__main__":
    print("Agent running...")
    result = send_notification("Test notification from CI/CD")
    print("Notification result:", result)
