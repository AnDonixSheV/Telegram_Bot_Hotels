import requests

from setting import SiteSettings

site = SiteSettings()
url = "https://" + site.api_host + None

headers = {
    "X-RapidAPI-Key": site.api_key.get_secret_value(),
    "X-RapidAPI-Host": site.api_host
}

response = requests.get(url, headers=headers)

print(response.text)
