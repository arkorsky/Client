#coding:utf-8
import time,random,wx
PrintSQL=True
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


def getDateStr(): #获取时间str
     ISOTIMEFORMAT='%Y-%m-%d'
     return time.strftime( ISOTIMEFORMAT, time.localtime())

def getDateStr2(): #获取时间str
     ISOTIMEFORMAT='%Y%m%d'
     return time.strftime( ISOTIMEFORMAT, time.localtime())

def compare_time(now_time,start_t,end_t):   #判断当前时间是否在 两时间间隔之间  #格式 yyyy-MM-dd
    s_time = time.mktime(time.strptime(start_t,'%Y-%m-%d')) 
    e_time = time.mktime(time.strptime(end_t,'%Y-%m-%d'))
    now_time = time.mktime(time.strptime(now_time,'%Y-%m-%d'))
    if (float(now_time) >= float(s_time)) and (float(now_time) <= float(e_time)):
        return True
    return False



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
    app.conn.execute(sql,paramTuple)
    if(PrintSQL):
        print(sql)
        print("commit: false  ;params:"+str(paramTuple))
        print("")

def commit(sql,paramTuple): #其他sql
    app=wx.GetApp();
    app.conn.execute(sql,paramTuple)
    if(PrintSQL):
        print(sql)
        print("commit: true   ;params:"+str(paramTuple))
        print("")
    app.db.commit()
    
