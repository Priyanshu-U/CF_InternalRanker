import pandas as pd
import requests

from data import cid_data

int_max = 1 << 32


def UrlCreator(contestID, handle):
    return f"https://codeforces.com/api/contest.standings?contestId={contestID}&showUnofficial=true&handles={handle}"


def getRank(contestID, handle):
    response = requests.get(UrlCreator(contestID, handle))
    if response.status_code == 200:
        response_row = (response.json()['result']['rows'])
        size = len(response_row)
        if size == 0:
            return int_max
        elif size == 1:
            return response_row[0]['rank']
        elif size >= 2:
            return response_row[-1]['rank']

    else:
        print("GET request failed with status code:", response.status_code)


for cid, data in cid_data.items():
    data['Rank'] = data.apply(lambda row: getRank(cid, row['Handle']), axis=1)
    data.reset_index(inplace=True, drop=True)
__all__ = ['cid_data']
