import requests

def get_package_info(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    r = requests.get(url)

    if r.status_code != 200:
        return None

    data = r.json()
    info = data["info"]

    return {
        "name": info["name"],
        "version": info["version"],
        "summary": info["summary"],
        "author": info["author"],
        "maintainer": info["maintainer"],
        "upload_time": data["releases"][info["version"]][0]["upload_time"]
    }
