import requests


def make_request(method, url, header=None, data=None):
    if method == "GET":
        return requests.get(url)
    if method == "DELETE":
        return requests.delete(url)
    if method == "POST":
        return requests.post(url=url, headers=header, data=data)
    if method == "PUT":
        return requests.put(url=url, headers=header, data=data)
    if method == "PATCH":
        return requests.patch(url=url, headers=header, data=data)
