from django.test import TestCase
import requests
import json
# Create your tests here.
class wc_spider:
	def __init__(self,url,headers):
		self.url=url
		self.headers=headers




	pass



if __name__=='__main__':
	url='https://www.iwencai.com/stockpick/cache?token=65c46eba3d60c2a80620acb66b12bc6f&p=1&perpage=10&showType=[%22%22,%22%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22]'
	headers={
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
	# 'Referer':'https://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=result_rewrite&selfsectsn=&querytype=stock&searchfilter=&tid=stockpick&w=%E6%88%90%E4%BA%A4%E9%87%8F%E5%88%9B%E5%8D%8A%E5%B9%B4%E6%96%B0%E9%AB%98',
	'Cookie':'cid=5ca22b79847788a80037ee57cb1d0d181528722233;ComputerID=5ca22b79847788a80037ee57cb1d0d181528722233; guideState=1; v=Aj1qq6o6OnX8QZ4Zdel9mGJzTJIz2nOkewvVAP-CeWzCzlLExyqB_Ate5dqM',

}

	res=requests.get(url=url,headers=headers)
	print(json.loads(res.text))

	#不重要的参数
	#PHPSESSID=aec1fe77cab4ea496355ca969a365f1a;
	#参数v,重要