#coding:utf-8
import wx,os,Frames,Dialogs,md5,sys,sqlite3,datas,time,Utils,Print
from decimal import *


def opj(path):
    """Convert paths to the platform-specific separator"""
    str = apply(os.path.join, tuple(path.split('/')))
    # HACK: on Linux, a leading / gets lost...
    if path.startswith('/'):
        str = '/' + str
    return str

        
class MyApp(wx.App):
    def OnInit(self):
        #初始化数据库链接
        self.db = sqlite3.connect(opj("data/test.db")) 
        self.conn = self.db.cursor()
        
        
        #打印小票
#        self.pdata = wx.PrintData()
#        self.pdata.SetPaperId(wx.PAPER_LETTER)
#        self.pdata.SetOrientation(wx.PORTRAIT)
#        data = wx.PrintDialogData(self.pdata)
#        printer = wx.Printer(data)
#        ConfigData=[(u'\u5c0f\u6e14\u6751\u7f8e\u98df\u5e7f\u573a', u'\u5c0f\u6e14\u6751\u5bf9\u8d26\u5355', u'\u5c0f\u6e14\u6751\u6b22\u8fce\u60a8 !\u7535\u8bdd 0576-88678777', u'\u53f0\u5dde\u5c0f\u6e14\u6751\u5eb7\u5e73\u8def\u5e97,\u6b22\u8fce\u60a8\u7684\u5149\u4e34')]
#        goodsData=[{u'\u5546\u54c1\u7f16\u7801': u'0005', u'\u6298\u6263': u'0.98', u'\u5355\u4ef7': u'200.01', u'\u91d1\u989d': u'196.01', u'\u5546\u54c1\u6761\u7801': u'1', u'\u5355\u4f4d': u'\u4ef6', u'\u5546\u54c1\u540d\u79f0': u'\u516d\u795e\u6e05\u51c9\u723d\u80a4\u6c90\u6d74\u9732200ml', u'\u6570\u91cf': u'1'}, {u'\u5546\u54c1\u7f16\u7801': u'012205', u'\u6298\u6263': u'0.99', u'\u5355\u4ef7': u'159.05', u'\u91d1\u989d': u'314.92', u'\u5546\u54c1\u6761\u7801': u'2', u'\u5355\u4f4d': u'\u4ef6', u'\u5546\u54c1\u540d\u79f0': u'\u516d\u795e\u827e\u53f6\u5065\u80a4\u6c90\u6d74\u9732\uff08\u6e05\u51c9\u578b\uff09450ml', u'\u6570\u91cf': u'2'}, {u'\u5546\u54c1\u7f16\u7801': u'13213', u'\u6298\u6263': u'0.1', u'\u5355\u4ef7': u'12.05', u'\u91d1\u989d': u'2.41', u'\u5546\u54c1\u6761\u7801': u'3', u'\u5355\u4f4d': u'\u7bb1', u'\u5546\u54c1\u540d\u79f0': u'\u5546\u54c1233', u'\u6570\u91cf': u'2'}]
#        OtherData = ['2015111916345658', u'196.0',u"想想想"]
#        printout = Print.GoodsPrinter(ConfigData,goodsData, u"小票打印",OtherData)
#        printer.Print(None,printout,True)
        
        self.Id="111";
        self.Name="222"     
        
#        self.LogIn=False;
#        self.doLogIn();
#        if(not self.LogIn):
#            #如果未登录  关闭数据库链接,退出App
#            return False;   
        
        
        #初始化Frame
        self.Homeframe=Frames.HomeFrame()
        return True
    
    
    def release(self): #app关闭 释放资源
         self.Homeframe.Destroy()
         self.conn.close()
    
    
    def showDialogWithErrorMsg(self,ErrorMsg):
        self.Dlg_LogIn=Dialogs.LogInDialog(None, -1,ErrorMsg);
        return  self.Dlg_LogIn;
    
    def doLogIn(self): #登陆方法
        self.Dlg_LogIn = self.showDialogWithErrorMsg("")
        while (not self.LogIn):
             val = self.Dlg_LogIn.ShowModal()
             if val == wx.ID_OK:
                 self.Dlg_LogIn.Destroy();#返回结果 关闭对话框
                 username=self.Dlg_LogIn.GetValue()[0];
                 password=self.Dlg_LogIn.GetValue()[1];
                 if(username==u'' or password==''):
                     self.showDialogWithErrorMsg(u"用户名或密码不能为空")
                 else :
                     self.conn.execute("select id,name,password from sys_user where username= ? ",(username,))
                     res =self.conn.fetchall()
                     if(not len(res)>0):
                          self.showDialogWithErrorMsg(u"用户名不存在")
                     else:
                         m1=md5.new()
                         md5psw=m1.update(password)      
                         if(res[0][2]==m1.hexdigest()):
                             self.LogIn=True
                             self.Id=res[0][0] # Id,
                             self.Name=res[0][1] # Name,
                         else:
                             self.showDialogWithErrorMsg(u"账号或密码错误")
             if val == wx.ID_CANCEL:
                 return;
    
    

def main():
    try:
        demoPath = os.path.dirname(__file__)
        os.chdir(demoPath)
    except:
        pass
    app = MyApp(False)
    app.MainLoop()
  
    
if __name__ == '__main__':
    __name__ = 'Main'
    main()   
