import requests
print(requests.__version__)
print(requests.get("http://google.com"))

res = requests.get("https://raw.githubusercontent.com/harryz6560/lab1/master/testing.py", ) 
print(res.text)
