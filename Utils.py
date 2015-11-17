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
    ISOTIMEFORMAT='%Y%m%d%H%M%S'
    return time.strftime( ISOTIMEFORMAT, time.localtime())+"000000"+str(random.randint(100000, 999999))

def getReturnOrderId(): #生成退货单号
    ISOTIMEFORMAT='%Y%m%d%H%M%S'
    return time.strftime( ISOTIMEFORMAT, time.localtime())+"000000"+str(random.randint(100000, 999999))


def getDateStr(): #获取时间str
     ISOTIMEFORMAT='%Y-%m-%d'
     return time.strftime( ISOTIMEFORMAT, time.localtime())

def query(sql,paramTuple): #查询sql
    app=wx.GetApp()
    app.conn.execute(sql,paramTuple)
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