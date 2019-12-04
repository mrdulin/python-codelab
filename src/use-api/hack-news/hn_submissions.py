import requests
from operator import itemgetter
import os

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
# /Users/ldu020/workspace/github.com/mrdulin/python-codelab/venv/lib/python3.7/site-packages/urllib3/connectionpool.py:1004: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
# InsecureRequestWarning,
r = requests.get(url, verify=False)
print('Status code: ', r.status_code)

submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    url = 'https://hacker-news.firebaseio.com/v0/item/' + \
        str(submission_id) + '.json'
    submission_r = requests.get(url, verify=False)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    submission_dict = {
        'title': response_dict['title'],
        'link': 'https://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'))

for submission_dict in submission_dicts:
    print('\nTitle: ', submission_dict['title'])
    print('Discussion Link: ', submission_dict['link'])
    print('Comments: ', submission_dict['comments'])
