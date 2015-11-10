#coding:utf-8
import  wx


class LogInDialog(wx.Dialog):
    #initMsg记录了账号密码输出错误的提示
    def __init__(self,parent, ID,initMsg, title=u"请输入账号密码", size=(500,200), pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE,useMetal=False):
        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)
        self.PostCreate(pre)
        if u'wxMac' in wx.PlatformInfo and useMetal:
            self.SetExtraStyle(wx.DIALOG_EX_METAL)
        self.user, self.password = '', ''
        self.CreateSizer(initMsg)    
    def dataEntries(self):  #输入框
        return ((u'用户名', 0, self.OnuserNameChange,200),(u'密   码', wx.TE_PASSWORD, self.OnPasswordChange,200))
    
    def dataButtons(self):  #按钮
        return ((wx.ID_OK, u'登陆(Enter)'),(wx.ID_CANCEL, u'退出(Esc)'))
    
    def CreateSizer(self,initMsg):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        sizer.Add(wx.StaticText(self, -1, initMsg), 0, wx.ALIGN_CENTER | wx.ALL, 10)
        
        for eachLabel, eachStyle, eachHandler,eachWidth in self.dataEntries():
            self.CreateEntry(sizer, eachLabel, eachStyle, eachHandler,eachWidth)
        
        btnsizer = wx.StdDialogButtonSizer()
        for eachId, eachLabel in self.dataButtons():
            self.CreateButton(btnsizer, eachId, eachLabel)
        btnsizer.Realize()
        sizer.Add(btnsizer, wx.EXPAND, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)
        self.SetSizer(sizer)
        sizer.Fit(self)   
        
        self.CenterOnScreen()
            
    def CreateEntry(self, sizer, label, style, handler,eachWidth):#输入的文本框
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(wx.StaticText(self, -1, label), 0, wx.ALIGN_CENTER | wx.ALL, 15)
        text = wx.TextCtrl(self, -1, u"", size = (eachWidth, -1), style = style)
        text.Bind(wx.EVT_TEXT, handler)
        box.Add(text, 1, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer.Add(box, 0, wx.GROW | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)  
          
    def CreateButton(self,btnsizer, id, label): #创建按钮
        button = wx.Button(self, id, label)
        if id == wx.ID_OK:
            button.SetDefault()
        btnsizer.AddButton(button)  
     
    def OnuserNameChange(self, event):
        self.user = event.GetString()
        
    def OnPasswordChange(self, event):
        self.password = event.GetString()   
        
    def GetValue(self):
        return (self.user, self.password)
    
    