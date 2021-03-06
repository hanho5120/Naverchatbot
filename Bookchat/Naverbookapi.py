import os
import sys
import urllib.request
import ssl

def Naverbook(bookname):
    client_id = "OKQPTGKiQf0V3yitzK6o"
    client_secret = "uIGSvzveCB"
    encText = urllib.parse.quote(bookname)
    ssl._create_default_https_context = ssl._create_unverified_context

    url = "https://openapi.naver.com/v1/search/book_adv.json?d_titl=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

    return response_body.decode('utf-8')