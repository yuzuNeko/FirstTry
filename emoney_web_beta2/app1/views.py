from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
import json
# import views
#用法，如果在本视图，直接传入视图
# Create your views here.
def index(request):
	if request.method=='POST':
		print('here!')
		return redirect(reverse(img0618))
	data={}
	context={'data':data}
	return render(request,'vue1.html',context)
def data1(request):
	data=dict(
		msg1='nihao',
		msg2='henhao',
		msg3='henhaohao',
		msg4='hellovue'


		)
	context={'data':json.dumps(data)}
	return render(request,'vue1.html',context)
def data2(request):
	return render(request,'vue2.html')
def data3(request):
	return render(request,'vue3.html')
def homework0614(request):
	import json
	import os
	print(os.getcwd())
	with open('./app1/data/data_renting.txt') as f:
		read=f.read()
	# read=json.loads(read)
	# print(read)
	context={'data':read}
	return render(request,'homework_tm.html',context=context)
def img0618(request):

	return render(request,'vue4.html')
def crawl_day(request):
	return render(request,'vue5.html')


