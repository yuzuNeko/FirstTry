import urllib
import urllib.parse


# k=urllib.parse.quote('月线新低')
# print(k)
import requests
url='https://www.iwencai.com/'
headers={
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
}
res=requests.get(url=url,headers=headers)
print(res.text)
print(res.headers)