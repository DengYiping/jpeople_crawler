import requests

def searchName(name):
    url = "https://jacobs.university/api/v1/users/?limit=7000&skip=0&tl=(((%22firstName%22%20contains%20%22{}%22)%20or%20(%22lastName%22%20contains%20%22{}%22)))%20and%20((%22active%22%20equals%20false))".format(name, name)
    headers = {
            "Origin": "https://people.jacobs.university",
            "Authorization": "Bearer q4QEVGkvZMigYZqnyFzULcNwy2kpNh",
            "Referer": "https://people.jacobs.university/?q={}".format(name)
            }
    r = requests.get(url, headers = headers)
    return r.json()
