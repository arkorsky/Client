#coding:utf8
import wx
import os
import Utils


class GoodsPrinter(wx.Printout):

    
    def __init__(self, ConfigData,GoodsData, title,OtherData):#OtherData  0销售单编号  1 收款金额  2 操作员名称
        wx.Printout.__init__(self, title)
        self.ConfigData=ConfigData
        self.GoodsData=GoodsData
        self.OtherData=OtherData
        self.common_font = wx.Font(5, wx.TELETYPE, wx.NORMAL, wx.NORMAL)
        self.big_font = wx.Font(11, wx.TELETYPE, wx.NORMAL, wx.NORMAL)

    def HasPage(self, page):
        return page <= 1
    
        return(200,200)

    def GetPageInfo(self): 
        return (1, 1, 1, 1)

    def OnPreparePrinting(self):
        pass


    def OnPrintPage(self, page):
        
        dc = self.GetDC()
        dc.SetUserScale(15, 15)
        dc.SetFont(self.common_font)
        self.x=5   #左上角距离x
        self.y=5   #左上角距离y
        
        self.width=6*28.3464
        
        #表头1
        self.CommonDraw(dc, self.ConfigData[0][0]) 
        #表头2
        head2=u"                "+self.ConfigData[0][1]
        self.CommonDraw(dc,head2)    
        
        self.CommonDraw(dc, u"编号:"+self.OtherData[0])
        
        self.CommonDraw(dc, u"日期 :"+Utils.getDateStr()+u"    操作员:"+self.OtherData[2])
        
        self.CommonDraw(dc, "")
        
        self.CommonDraw(dc, u"商品名称      结算价        数量      金额")  
        
        #虚线
        self.y=self.y+6
        self.DrawDottedLine(dc) 
        #商品
        self.DrawGoodsList(dc)
        #虚线
        self.DrawDottedLine(dc) 
        #合计
        self.CommonDraw(dc, u"收款金额                               "+str(self.OtherData[1]))
        #空一行
        self.CommonDraw(dc, u"      ")
        #表脚1
        self.CommonDraw(dc, u"      "+str(self.ConfigData[0][2]))
        #表脚2
        self.CommonDraw(dc, u"      "+str(self.ConfigData[0][3]))
        return True
    
    
    
    def BigDraw(self,dc,data):  ######未使用
         dc.SetFont(self.common_font) 
         dc.DrawText(data, self.x, self.y)  
         self.y += 30
     
    def CommonDraw(self,dc,data):  #普通字体画线
         dc.SetFont(self.common_font)
         dc.DrawText(data, self.x, self.y)  
         self.y += 7
    def DrawDottedLine(self,dc):  #画虚线
          blackPen= wx.Pen("black",1,wx.DOT)
          whitePen= wx.Pen("white",1,wx.DOT)
          self.currentx=self.x;
          unitNum=100; #份数
          self.PerUnitWidth=self.width/unitNum
          self.BlackWidth=self.PerUnitWidth*0.6
          self.WhiteWidth=self.PerUnitWidth*0.4
          
          for i in range (0,unitNum):
              #画黑线
              dc.SetPen(blackPen)
              dc.DrawLine(self.currentx,self.y,self.currentx+self.BlackWidth,self.y)  
#              print("DrawBlack "+str(self.currentx)+" to " + str(self.currentx+self.BlackWidth))
              #画白线
              dc.SetPen(whitePen)
              dc.DrawLine(self.currentx+self.BlackWidth,self.y,self.currentx+self.PerUnitWidth,self.y)  
#              print("DrawWhite "+str(self.currentx+self.BlackWidth)+" to " + str(self.currentx+self.PerUnitWidth))
              self.currentx=self.currentx+self.PerUnitWidth
          
          self.y += 6
          
          
    def DrawGoodsList(self,dc):   #商品列表
        for i in range (0,len(self.GoodsData)):
            self.CommonDraw(dc,self.GoodsData[i][u"商品名称"]+"" )
            
            priceLen=len(self.GoodsData[i][u"单价"])
            space1=""
            for j in range (0,14-priceLen):    #14为"结算价        数量"  从  结--数左边空格  总长度
                space1=space1+" "
            
            numberLen=len(self.GoodsData[i][u"数量"])
            space2=""
            for j in range (0,10-numberLen):  #10为   "数量      金额"  从 量--金左边空格 总长度
                space2=space2+" "
            
            self.CommonDraw(dc,u"              "+self.GoodsData[i][u"单价"]+space1+self.GoodsData[i][u"数量"]+space2+self.GoodsData[i][u"金额"])
        
        self.y=self.y+7
        
        
        