from django.shortcuts import render
from django.http import HttpResponse
import os
import json
import time
# Create your views here.
from emoney.settings import logger

def time_sort(l):

	l2=[]
	l1=[]
	for i in l:
		if '.png' in i :
			l1.append(i)
			l2.append(time.mktime(time.strptime(i[-14:-4],'%Y-%m-%d')))
	# print(l2)
	l=[]
	for i in range(len(l1)):
		l.append((l1[i],l2[i]))
	# print(l)
	l.sort(key=lambda x:x[1],reverse=True)
	# print(l)
	l2=[]
	for i in l:
		l2.append(i[0])
	# print(l2)
	return l2



def index(request):
	return HttpResponse('nihao')
def show(request):

	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	# logger.info(BASE_DIR)
	filelist=os.listdir(BASE_DIR+'//app2//static//data_img')
	filelist=time_sort(filelist)
	filelist=json.dumps(filelist)
	context={
		'filelist':filelist,
	}
	return render(request,'show.html',context=context)

def show2(request):

	return render(request,'echart1.html')