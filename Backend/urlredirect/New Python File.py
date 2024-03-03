import requests
import json, webbrowser

session = requests.session()

session.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) ' +
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
response = session.get('http://127.0.0.1:8000//post/')
response = session.post('http://127.0.0.1:8000/post/',
    data={
        'csrfmiddlewaretoken': session.cookies['csrftoken'],
        'data':json.dumps({'slug':'hello',
        'url':'https://www.google.com'})
    })
print(response.text)
session.close()