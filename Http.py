#coding:utf-8
import urllib2,urllib,socket,cookielib,json

ShowHttpResult=True

#HTTP  Config
TIMEOUT=10  #socked超时时间
#PreFixUrl = "http://192.168.1.12:8080/agent/"  #WebContent路径
PreFixUrl = "http://127.0.0.1:9090/agent/"  #WebContent路径
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#PreFixUrl='http://127.0.0.1:9090/agent/'
Action_signIn = "login_safe"  #登陆
Action_getDate = "client/interface/getTime.do"  #系统时间
Action_getOffInfo = "client/interface/getOffPriceGoods.do" ###获取特价商品接口(参数 门店编号) 需求返回List<Map>字段 goodsId,barCode,oldprice,offprice,beginTime,endTime

def sendHttp(url,data): #发送http请求并且解析json返回Map(dic)
    if(not data==None):
        data=urllib.urlencode(data)
    try:
         response = opener.open(PreFixUrl+url,data,timeout=TIMEOUT)
         res=response.read();
         rs=json.loads(res)
         if(ShowHttpResult):
             print("response:"+str(res))
             print("json:"+str(rs))
         return rs
    except urllib2.URLError,e:  
         if(isinstance(e, urllib2.HTTPError)): #httperror是urlError的子类 #返回错误
             print(e)
         elif(isinstance(e, urllib2.URLError)): ###未联网
             print(e)
         return ""
    except socket.timeout,e: #socked超时
        print(e)
        return "" 
    except ValueError,e:  #json解析错误相关
        print(e)
        return ""