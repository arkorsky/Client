#coding:utf-8
import  wx
import Panels,Dialogs
import md5





class HomeFrame(wx.Frame): #进入首页的Frame
    def __init__(self):
         wx.Frame.__init__(self, None, -1, u"门店管理系统",size=(500,400),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
         self.Bind(wx.EVT_CLOSE,self.CloseHomeFrame)
         self.Centre()
         Data=(u"收银员编号   :    20102",u"收银员名称   :     看看看",u"      收银日期  :     2015-10-10")
         Panels.HomePage(self,Data);
             
    def CloseHomeFrame(self,event):#主页面关闭,app关闭
            app=wx.GetApp();
            app.release()
           
           

class cashFrame(wx.Frame):  #零售收银Frame
    
  def __init__(self):
      wx.Frame.__init__(self, None, -1, u"零售收银",size=(800,600),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
      self.Bind(wx.EVT_CLOSE,self.ClosecashFrame)
      self.Centre()
      Panels.CashPage(self)
      
  def ClosecashFrame(self,event):#零售收银页面关闭,回到主页面
      self.Hide();
      app = wx.GetApp()
      app.Homeframe.Show()
      
      
      
class ReturnFrame(wx.Frame):  #零售退款Frame
    
  def __init__(self):
      wx.Frame.__init__(self, None, -1, u"零售退款",size=(800,600),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
      self.Bind(wx.EVT_CLOSE,self.ClosecashFrame)
      self.Centre()
      Panels.ReturnPage(self)
      
  def ClosecashFrame(self,event):#零售退款页面关闭,回到主页面
      self.Hide();
      app = wx.GetApp()
      app.Homeframe.Show()      
  
      
class KeyCodeConfigFrame(wx.Frame):  #打印按钮配置Frame
    
  def __init__(self):
      wx.Frame.__init__(self, None, -1, u"零售退款",size=(800,600),style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)
      self.Bind(wx.EVT_CLOSE,self.ClosecashFrame)
      self.Centre()
      Panels.KeyCodeConfigPage(self);
      
  def CloseKeyCodeConfigFrame(self,event):#打印按钮配置页面关闭,回到主页面
      self.Hide();
      app = wx.GetApp()
      app.Homeframe.Show()        
      
      
      
      