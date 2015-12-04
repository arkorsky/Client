#coding:utf-8
import  wx
import Panels,Dialogs
import md5
import Frames
import Utils

class HomeFrame(wx.Frame): #进入首页的Frame
    def __init__(self):
         wx.Frame.__init__(self, None, -1, u"门店管理系统",size=(500,400),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
         self.Bind(wx.EVT_CLOSE,self.CloseHomeFrame)
         self.Centre()
         app=wx.GetApp()
         Data=(u"收银员编号   :    "+str(app.Id),u"收银员名称   :     "+str(app.Name),u"      收银日期  :     "+Utils.getDateStr())
         Panels.HomePage(self,Data);
         self.Show()
             
    def CloseHomeFrame(self,event):#主页面关闭,app关闭
            app=wx.GetApp();
            app.release()
           
           

class cashFrame(wx.Frame):  #零售收银Frame
    
  def __init__(self):
      wx.Frame.__init__(self, None, -1, u"零售收银",size=(800,600),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
      self.Bind(wx.EVT_CLOSE,self.ClosecashFrame)
      self.Centre()
      Panels.CashPage(self)
      self.Show()
      
  def ClosecashFrame(self,event):#零售收银页面关闭,回到主页面
      self.Destroy()
      app = wx.GetApp()
      app.Homeframe.Show()
  
  def CloseFrameAndOpenReturnPage(self,saleOrder,saleOrderDetail): 
      self.Destroy()
      Frames.ReturnFrame(saleOrder,saleOrderDetail)
    
      

class getMoneyFrame(wx.Frame): #收款明细,最后结算页面
   def __init__(self,cashMoney,GoodsData):
      wx.Frame.__init__(self, None, -1, u"收款明细",size=(800,600),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
      self.Bind(wx.EVT_CLOSE,self.ClosegetMoneyFrame)
      self.Centre()
      Panels.getMoneyPage(self,cashMoney,GoodsData)
      self.Show()
      
   def ClosegetMoneyFrame(self,event):#零售收款页面关闭,打开收银页面
      self.Destroy()
      Frames.cashFrame()


      
class ReturnFrame(wx.Frame):  #零售退款页面
    
  def __init__(self,saleOrder,saleOrderDetail): #销售单,销售单详细信息
      wx.Frame.__init__(self, None, -1, u"零售退款",size=(800,600),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
      self.Bind(wx.EVT_CLOSE,self.ClosecashFrame)
      self.Centre()
      Panels.ReturnPage(self,saleOrder,saleOrderDetail)
      self.Show()
      
  def ClosecashFrame(self,event):#零售退款页面关闭,回到主页面
      self.Destroy()
      app = wx.GetApp()
      app.Homeframe.Show()
      
  def CloseFrameAndOpenSalePage(self):  
      self.Destroy()
      Frames.cashFrame()  
  

class returnMoneyFrame(wx.Frame):
    def __init__(self,cashMoney,GoodsData,saleOrderId,saleOrder,saleOrderDetail): #退货金额 退货商品信息,销售单号,销售单,销售单详细信息
      print(saleOrderId)
      wx.Frame.__init__(self, None, -1, u"退款明细",size=(800,600),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
      self.Bind(wx.EVT_CLOSE,self.ClosereturnMoneyFrame)
      self.Centre()
      Panels.returnMoneyPage(self,cashMoney,GoodsData,saleOrderId,saleOrder,saleOrderDetail)
      self.Show()
      
    def ClosereturnMoneyFrame(self,event):#打开退货页面
      self.Destroy()

      
class KeyCodeConfigFrame(wx.Frame):  #打印按钮配置Frame
    
  def __init__(self):
      wx.Frame.__init__(self, None, -1, u"快捷键配置",size=(800,600),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
      self.Bind(wx.EVT_CLOSE,self.CloseKeyCodeConfigFrame)
      self.Centre()
      Panels.KeyCodeConfigPage(self);
      self.Show()
      
  def CloseKeyCodeConfigFrame(self,event):#打印按钮配置页面关闭,回到主页面
      self.Destroy()
      app = wx.GetApp()
      app.Homeframe.Show()        
      

class GoodsQueryFrame(wx.Frame):     #商品查询Frame
     def __init__(self):
          wx.Frame.__init__(self, None, -1, u"商品档案查询",size=(800,600),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
          self.Bind(wx.EVT_CLOSE,self.CloseGoodsQueryFrame)
          self.Centre()
          Panels.GoodsPage(self)
          self.Show()
      
     def CloseGoodsQueryFrame(self,event):#商品查询页面关闭,回到主页面
          self.Destroy()
          app = wx.GetApp()
          app.Homeframe.Show()
          
class saleOrderQueryFrame(wx.Frame):     #销售单查询Frame
     def __init__(self):
          wx.Frame.__init__(self, None, -1, u"销售单查询",size=(800,600),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
          self.Bind(wx.EVT_CLOSE,self.ClosesaleOrderQueryFrame)
          self.Centre()
          Panels.SaleOrderPage(self)
          self.Show()
      
     def ClosesaleOrderQueryFrame(self,event):#销售单查询页面关闭,回到主页面
          self.Destroy()
          app = wx.GetApp()
          app.Homeframe.Show()       

class returnOrderQueryFrame(wx.Frame):     #销售单查询Frame
     def __init__(self):
          wx.Frame.__init__(self, None, -1, u"退货单查询",size=(800,600),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
          self.Bind(wx.EVT_CLOSE,self.ClosereturnOrderQueryFrame)
          self.Centre()
          Panels.ReturnOrderPage(self)
          self.Show()
      
     def ClosereturnOrderQueryFrame(self,event):#销售单查询页面关闭,回到主页面
          self.Destroy()
          app = wx.GetApp()
          app.Homeframe.Show()                 

class printConfigFrame(wx.Frame):     #打印配置界面
     def __init__(self):
          wx.Frame.__init__(self, None, -1, u"打印配置",size=(600,600),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
          self.Bind(wx.EVT_CLOSE,self.closeprintConfigFrame)
          self.Centre()
          Panels.printConfigPage(self)
          self.Show()
      
     def closeprintConfigFrame(self,event):#打印配置关闭,回到主页面
          self.Destroy()
          app = wx.GetApp()
          app.Homeframe.Show()    
          
      