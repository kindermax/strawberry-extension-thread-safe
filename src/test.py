import json
import threading

import requests

url = "http://localhost:8000/graphql"
headers = {
    "accept": "application/json",
    "content-type": "application/json",
}


def get_payload(name):
    return json.dumps(
        {
            "query": f"query {name} {{ books {{ title }} }}",
            "variables": None,
            "operationName": name,
        }
    )


def make_call(url_, headers_, payload_):
    response = requests.request(
        "POST", url_, headers=headers_, data=payload_, verify=False
    )
    try:
        assert response.status_code == 200
        data = response.json()
        assert data["data"]["books"][0]["title"] == "The Great Gatsby"
        print("OK", threading.get_ident(), url_)
    except AssertionError as e:
        print("FAIL", threading.get_ident(), url_, "error", e, "text", response.text)


threads = []

for n in range(3):
    name = f"BookQuery_{n}"
    threads.append(
        threading.Thread(target=make_call, args=(url, headers, get_payload(name)))
    )

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
