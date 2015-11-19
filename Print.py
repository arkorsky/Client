#coding:utf8
import wx
import os
import Utils


class GoodsPrinter(wx.Printout):

    
    def __init__(self, ConfigData,GoodsData, title,OtherData):
        wx.Printout.__init__(self, title)
        self.ConfigData=ConfigData
        self.GoodsData=GoodsData
        self.OtherData=OtherData
        self.common_font = wx.Font(5, wx.TELETYPE, wx.NORMAL, wx.NORMAL)
        self.big_font = wx.Font(11, wx.TELETYPE, wx.NORMAL, wx.NORMAL)

    def HasPage(self, page):
        return page <= 1
    
    def GetPageSizeMM(self):
        return(200,200)

    def GetPageInfo(self): 
        return (1, 1, 1, 1)


    def OnPreparePrinting(self):
        pass


    def OnPrintPage(self, page):
        
        dc = self.GetDC()
        dc.SetUserScale(15, 15)
        dc.SetFont(self.common_font)
        self.x=30   #左上角距离x
        self.y=30   #左上角距离y
        
        dc.DrawLine(30,30,30+6*28.3464,30)
        
        #表头1
        self.CommonDraw(dc, self.ConfigData[0][0]) 
        
        #表头2
        head2=u"        "+self.ConfigData[0][1]
        self.CommonDraw(dc,head2)    
        
        self.CommonDraw(dc, u"编号:"+self.OtherData[0])
        
        self.CommonDraw(dc, u"日期 :"+Utils.getDateStr()+u"    操作员:"+self.OtherData[2])
        
        self.CommonDraw(dc, "")
        
        self.CommonDraw(dc, u"商品名称      结算价        数量      金额")
        return True
    
    
    
    
    def BigDraw(self,dc,data):
         dc.SetFont(self.common_font)
         dc.DrawText(data, self.x, self.y)  #表头1
         self.y += 30
    
    
    def CommonDraw(self,dc,data):
         dc.SetFont(self.common_font)
         dc.DrawText(data, self.x, self.y)  #表头1
         self.y += 7
        