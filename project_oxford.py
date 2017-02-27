import requests
import time


class ProjectOxfordApi(object):
    """
    ProjectOxfordApi
    """

    _max_retries = 5

    def __init__(self, key, base_url="https://westus.api.cognitive.microsoft.com"):
        self.base_url = base_url
        self.key = key

    def request(self, method='get', endpoint='', json=None, data=None, params=None):
        retries = 0
        result = None

        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            'Content-Type': 'application/json',
        }

        while True:
            response = requests.request(method, endpoint, json=json, data=data, headers=headers,
                                        params=params)

            if response.status_code == 429:

                print("Message: %s" % (response.json()['error']['message']))

                if retries <= self._max_retries:
                    time.sleep(1)
                    retries += 1
                    continue
                else:
                    print('Error: failed after retrying!')
                    break

            elif response.status_code == 200 or response.status_code == 201:

                if 'content-length' in response.headers and int(response.headers['content-length']) == 0:
                    result = None
                elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
                    if 'application/json' in response.headers['content-type'].lower():
                        result = response.json() if response.content else None
                    elif 'image' in response.headers['content-type'].lower():
                        result = response.content
            else:
                print("Error code: %d" % (response.status_code,))
                print("Message: %s" % (response.json()['error']['message']))

            break

        return result
