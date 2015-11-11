#coding:utf-8
import wx,os,Frames,Dialogs,md5,sys,sqlite3,datas


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
        
        
        self.LogIn=False;
        self.doLogIn();
        if(not self.LogIn):
            #如果未登录  关闭数据库链接,退出App
            return False;        
            
        #初始化Frame
        self.Homeframe = Frames.HomeFrame()
        
        self.Cashframe = Frames.cashFrame() 
        self.ReturnFrame=Frames.ReturnFrame()
        self.KeyCodeConfigFrame=Frames.KeyCodeConfigFrame();
        
        
        self.Homeframe.Show()
        
        return True
    
    
    def release(self): #app关闭 释放资源
         self.Cashframe.Destroy()
         self.Homeframe.Destroy()
         self.KeyCodeConfigFrame.Destroy()
    
    
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
                     self.conn.execute("select name,password from sys_user where username= ? ",(username,))
                     res =self.conn.fetchall()
                        
                     if(not len(res)>0):
                          self.showDialogWithErrorMsg(u"用户名不存在")
                     else:
                         m1=md5.new()
                         md5psw=m1.update(password)      
                         if(res[0][1]==m1.hexdigest()):
                             self.LogIn=True
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
