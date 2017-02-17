#coding:utf-8
import re
import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')

headers = { 'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
url = 'http://www.jianshu.com'
try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')

    reg = r'<div class="content">.*?<a class="title".*?>(.*?)</a>.*?<i class="iconfont ic-list-read"></i>(.*?)</a> .*?<i class="iconfont ic-list-comments"></i>(.*?)</a>.*?"iconfont ic-list-like"></i>(.*?)</span>.*?"iconfont ic-list-money"></i>(.*?)</span>'
    hotre = re.compile(reg, re.S)
    artlist = re.findall(hotre, html)

    for i in artlist:
        print i[0]+' 阅读:'+i[1]+' 评论:'+i[2]+' 喜欢:'+i[3]+' 打赏:'+i[4]

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason


