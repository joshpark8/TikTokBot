#sample code from an old spotify api script i wrote that we can repurpose here

import requests
import json

base_url = 'https://api.spotify.com/v1/'

def auth():
    cid = 'CID'
    secret = 'SECRET'
    auth_url = 'https://accounts.spotify.com/api/token'
    r = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': cid,
        'client_secret': secret,
    })
    auth_response_data = r.json()
    access_token = auth_response_data['access_token']
    headers = {
        'Authorization': 'Bearer {token}'.format(token = access_token)
    }
    return headers