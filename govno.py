import requests

OAUTH_TOKEN = "y0__xCHq4_aAhjpvzcg9NHW_xI8corHuKWsoZJ8ic3vSejjVu-4LA"
response = requests.get(
    "https://cloud-api.yandex.net/v1/disk",
    headers={"Authorization": f"OAuth {OAUTH_TOKEN}"}
)
print(response.status_code)  # Должен быть 200
print(response.json())  # Должен показать информацию о диске