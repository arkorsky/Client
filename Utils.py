#coding:utf-8
import time,datetime,random,wx,urllib2,urllib,socket,cookielib,json

PrintSQL=True  #是否打印SQL语句

def transFerGirdData(Grid): #将Grid信息转换为List<Map<String,String>
    rowNum=Grid.GetNumberRows()
    colNum=Grid.GetNumberCols()
    goodsList=list()
    dataMap=None;
    for i in range(0,rowNum):
        dataMap={}
        for j in range(0,colNum):
            dataMap[Grid.GetColLabelValue(j)]=Grid.GetCellValue(i,j)
        goodsList.append(dataMap)    
    return goodsList      


def getSaleOrderId(): #生成销售单号
    idlength=4
    date=getDateStr2();
    sql='select id from id_generater where date = ? and type = ?'
    rs=query(sql,(date,'saleorder',))
    if(len(rs)>0):
        id=int(rs[0][0])+1
        #高位补0
        length=len(str(id))
        strid=str(id);
        for i in range(length,idlength):
            strid ='0'+strid;
        return date+strid
    else:
        sql='insert into id_generater (id,date,type) values (?, ?, ?)'
        execute(sql, (0,date,'saleorder',))
        return date+"0001"

def getReturnOrderId(): #生成退货单号
    ISOTIMEFORMAT='%Y%m%d%H%M%S'
    return time.strftime( ISOTIMEFORMAT, time.localtime())+str(random.randint(10, 99))

def getFormatDate(fmt): #获取时间str
     return time.strftime( fmt, time.localtime())

def getDateStr(): #获取时间str
     ISOTIMEFORMAT='%Y-%m-%d'
     return time.strftime( ISOTIMEFORMAT, time.localtime())

def getDateStr2(): #获取时间str
     ISOTIMEFORMAT='%Y%m%d'
     return time.strftime( ISOTIMEFORMAT, time.localtime())

def compare_time(now_time,start_t,end_t,fmt):   #判断当前时间是否在 两时间间隔之间 相同也是True
    s_time = time.mktime(time.strptime(start_t,fmt)) 
    e_time = time.mktime(time.strptime(end_t,fmt))
    now_time = time.mktime(time.strptime(now_time,fmt))
    if (float(now_time) >= float(s_time)) and (float(now_time) <= float(e_time)):
        return True
    return False


def comparTo(date1,date2,fmt): #判断日期大小(支持08:00这种格式),前面的大 返回1,相同0,后面大返回-1
    if(fmt=="%H:%M"):
        fmt="%Y-%m-%d %H:%M"
        date1="2015-01-01 "+date1
        date2="2015-01-01 "+date2
    d1=float(time.mktime(time.strptime(date1,fmt))) 
    d2=float(time.mktime(time.strptime(date2,fmt)))
    if(d1==d2):
        return 0;
    if(d1>d2):
        return 1;
    if(d1<d2):
        return -1;
    




def query(sql,paramTuple): #查询sql
    app=wx.GetApp()
    if(paramTuple!=None):
        app.conn.execute(sql,paramTuple)
    else:
        app.conn.execute(sql)   
    if(PrintSQL):
        print(sql)
        print("query  params:"+str(paramTuple))
        print("")
    return app.conn.fetchall()

def execute(sql,paramTuple): #其他sql
    app=wx.GetApp();
    if(paramTuple!=None):
        app.conn.execute(sql,paramTuple)
    else:
        app.conn.execute(sql)
    if(PrintSQL):
        print(sql)
        print("commit: false  ;params:"+str(paramTuple))
        print("")

def commit(sql,paramTuple): #其他sql
    app=wx.GetApp();
    if(paramTuple!=None):
        app.conn.execute(sql,paramTuple)
    else :    
        app.conn.execute(sql) 
    if(PrintSQL):
        print(sql)
        print("commit: true   ;params:"+str(paramTuple))
        print("")
    app.db.commit()
    
