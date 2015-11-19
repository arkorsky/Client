# -*- coding: utf-8 -*-  
import wx 
import wx.xrc 
import VideoCapture 
########################################################################### 
## Class MyFrame1 
########################################################################### 
class MyFrame1 ( wx.Frame ): 
     
    def __init__( self, parent ): 
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 566,535 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL ) 
         
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize ) 
         
        bSizer1 = wx.BoxSizer( wx.VERTICAL ) 
         
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL ) 
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 ) 
         
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"视频捕获", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"打印预览", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        bSizer1.Add( self.m_button3, 0, wx.ALL, 5 ) 
        bSizer1.Add( self.m_button4, 0, wx.ALL, 5 ) 
         
        self.SetSizer( bSizer1 ) 
        self.Layout() 
         
        self.Centre( wx.BOTH ) 
        # Connect Events 
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnButton ) 
        self.m_button4.Bind( wx.EVT_BUTTON, self.OnButton2 ) 
        self.timer=wx.Timer(self) 
        self.Bind(wx.EVT_TIMER,self.OnIdel,self.timer) 
        self.Bind(wx.EVT_CLOSE,self.OnExit) 
    def OnExit(self,evnet): 
        self.timer.Stop() 
        wx.Exit()  
        pass 
    def OnIdel(self,evnet): 
        cam = VideoCapture.Device() 
        self.cam.saveSnapshot('test.jpg') 
        img=wx.Image("test.jpg",wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
        dc=wx.ClientDC(self.m_panel1) 
        dc.DrawBitmap(img,0,0,False) 
    def OnButton( self, event ): 
        self.cam = VideoCapture.Device() 
        #cam.saveSnapshot('test.jpg') 
        self.timer.Start(100) 
    def OnButton2( self, event ): 
        self.timer.Stop() 
        self.printData = wx.PrintData() 
        self.printData.SetPaperId(wx.PAPER_LETTER) 
        self.printData.SetPrintMode(wx.PRINT_MODE_PRINTER) 
        data = wx.PrintDialogData(self.printData) 
        printout = MyPrintout(self) 
        printout2 = MyPrintout(self) 
        self.preview = wx.PrintPreview(printout, printout2, data)#第一步创建预览设备 
        if not self.preview.Ok(): 
            wx.MessageBox("error") 
            return 
        pfrm = wx.PreviewFrame(self.preview, self, "This is a print preview")#第二步创建框架 
        pfrm.Initialize()#第三步初始化框架  www.2cto.com
        pfrm.SetPosition(self.GetPosition())#设置默认的位置 
        pfrm.SetSize(self.GetSize())#设置打印预览框的大小 
        pfrm.Show(True) 
     
class MyPrintout(wx.Printout): 
    def __init__(self, canvas): 
        wx.Printout.__init__(self) 
        self.canvas = canvas 
 
    def OnBeginDocument(self, start, end): 
        return super(MyPrintout, self).OnBeginDocument(start, end) 
 
    def OnEndDocument(self): 
        super(MyPrintout, self).OnEndDocument() 
 
    def OnBeginPrinting(self): 
        super(MyPrintout, self).OnBeginPrinting() 
 
    def OnEndPrinting(self): 
        super(MyPrintout, self).OnEndPrinting() 
 
    def OnPreparePrinting(self): 
        super(MyPrintout, self).OnPreparePrinting() 
 
    def OnPrintPage(self, page): 
        dc = self.GetDC() 
        #------------------------------------------- 
        # One possible method of setting scaling factors... 
        img=wx.Image("test.jpg",wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
        dc.DrawBitmap(img,0,0,False) 
        return True 
if __name__=='__main__': 
    app=wx.App() 
    frame=MyFrame1(None) 
    frame.Show(True) 
    app.MainLoop() 