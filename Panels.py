#coding:utf-8
import wx
import wx.xrc
import wx.grid
import datas


class HomePage ( wx.Panel ):
    
    def __init__( self, parent,TextData):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,800 ), style = wx.TAB_TRAVERSAL )
        
        PanelSizer = wx.BoxSizer( wx.VERTICAL )
        
        #顶部的3个StaticText
        TopGridSizer = wx.GridSizer( 2, 2, 0, 0 )
        self.number = wx.StaticText( self, wx.ID_ANY,TextData[0], wx.DefaultPosition, wx.DefaultSize, 0 )
        self.number.Wrap( -1 )
        TopGridSizer.Add( self.number, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.name = wx.StaticText( self, wx.ID_ANY, TextData[1], wx.DefaultPosition, wx.DefaultSize, 0 )
        self.name.Wrap( -1 )
        TopGridSizer.Add( self.name, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.time = wx.StaticText( self, wx.ID_ANY, TextData[2], wx.DefaultPosition, wx.DefaultSize, 0 )
        self.time.Wrap( -1 )
        TopGridSizer.Add( self.time, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        PanelSizer.Add( TopGridSizer, 1, wx.EXPAND, 5 )
        
        
        #底部的按钮
        ButtomGridSizer = wx.GridSizer( 0, 2, 0, 0 )
        
        self.cashBtn = wx.Button( self, wx.ID_ANY, u"收银[F1]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.cashBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.queryBtn = wx.Button( self, wx.ID_ANY, u"商品查询[F3]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.queryBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.returnBtn = wx.Button( self, wx.ID_ANY, u"退货[F2]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.returnBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.pswChangeBtn = wx.Button( self, wx.ID_ANY, u"修改密码[F4]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.pswChangeBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.querysalesBtn = wx.Button( self, wx.ID_ANY, u"销售单查询[F12]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.querysalesBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.printSettingsBtn = wx.Button( self, wx.ID_ANY, u"打印设置[F5]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.printSettingsBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.returnQueryBtn = wx.Button( self, wx.ID_ANY, u"退货单查询[F3]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.returnQueryBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.keyCodeConfig = wx.Button( self, wx.ID_ANY, u"快捷键配置[F8]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.keyCodeConfig, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.dailyReportBtn = wx.Button( self, wx.ID_ANY, u"销售日结[F3]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.dailyReportBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.ExitBtn = wx.Button( self, wx.ID_ANY, u"退出[ESC]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.ExitBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        PanelSizer.Add( ButtomGridSizer, 6, wx.EXPAND, 5 )
        
        self.SetSizer( PanelSizer )
        self.Layout()
        
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.SetFocus()
             
        #为所有按钮绑定键盘事件
        self.cashBtn.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.queryBtn.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.returnBtn.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.pswChangeBtn.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.querysalesBtn.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.printSettingsBtn.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.returnQueryBtn.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.keyCodeConfig.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.dailyReportBtn.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.ExitBtn.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        
        
        self.cashBtn.Bind(wx.EVT_LEFT_DOWN,self.onCash)
        self.ExitBtn.Bind(wx.EVT_LEFT_DOWN,self.OnExit)
        self.returnBtn.Bind(wx.EVT_LEFT_DOWN,self.OnReturn)
        self.keyCodeConfig.Bind(wx.EVT_LEFT_DOWN,self.OnKeyCodeConfig)
             
    def OnKeyDown(self, event):#快捷键配置
         print(event.GetKeyCode())
         if(event.GetKeyCode()==340):
             self.onCash(None)
         if(event.GetKeyCode()==27):
             self.OnExit(None)
         if(event.GetKeyCode()==341):
             self.OnReturn(None)
         if(event.GetKeyCode()==347):
             self.OnKeyCodeConfig(None)
             
         event.Skip()     
             
         
    def onCash(self,event): #收银按钮事件
        app = wx.GetApp()
        app.Homeframe.Hide()
        app.Cashframe.Show()

    def OnReturn(self,event):#退货
        app = wx.GetApp()
        app.Homeframe.Hide()
        app.ReturnFrame.Show()
        
    def OnKeyCodeConfig(self,event):
        app = wx.GetApp()
        app.Homeframe.Hide()    
        app.KeyCodeConfigFrame.Show()
        
        
    def OnExit(self,event): #退出按钮事件
        self.GetParent().CloseHomeFrame(None)    

        

class CashPage ( wx.Panel ):
    
    def __init__( self, parent ):
        
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        PanelSizer = wx.BoxSizer( wx.VERTICAL )
        
        ButtonSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.balanceBtn = wx.Button( self, wx.ID_ANY, u"结算[Q]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.balanceBtn, 0, wx.ALL, 5 )
        
        self.returnBtn = wx.Button( self, wx.ID_ANY, u"退货[F2]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.returnBtn, 0, wx.ALL, 5 )
        
        self.delBtn = wx.Button( self, wx.ID_ANY, u"删除[DEL]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.delBtn, 0, wx.ALL, 5 )
        
        
        PanelSizer.Add( ButtonSizer, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.LEFT, 10 )
        
        self.staticLine = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        PanelSizer.Add( self.staticLine, 0, wx.EXPAND |wx.ALL, 5 )
        
        TollBarSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.StaticTextQuery = wx.StaticText( self, wx.ID_ANY, u"输入查询", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.StaticTextQuery.Wrap( -1 )
        TollBarSizer.Add( self.StaticTextQuery, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT|wx.RIGHT, 15 )
        
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
        TollBarSizer.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL, 15 )
        
        self.staticTextNum = wx.StaticText( self, wx.ID_ANY, u"应收金额", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.staticTextNum.Wrap( -1 )
        TollBarSizer.Add( self.staticTextNum, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT, 210 )
        
        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        self.m_textCtrl5.Enable( False )
        
        TollBarSizer.Add( self.m_textCtrl5, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT, 5 )
        
        
        PanelSizer.Add( TollBarSizer, 2, 0, 5 )
        
        self.staticLine2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        PanelSizer.Add( self.staticLine2, 0, wx.EXPAND |wx.ALL, 5 )
        
        GridSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.goodsGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        
        # Grid
        self.goodsGrid.CreateGrid( 50, 8 )
        self.goodsGrid.EnableEditing( True )
        self.goodsGrid.EnableGridLines( True )
        self.goodsGrid.EnableDragGridSize( False )
        self.goodsGrid.SetMargins( 0, 0 )
        
        # Columns
        self.goodsGrid.SetColSize( 0, 75 )
        self.goodsGrid.SetColSize( 1, 75 )
        self.goodsGrid.SetColSize( 2, 150 )
        self.goodsGrid.SetColSize( 3, 50 )
        self.goodsGrid.SetColSize( 4, 75 )
        self.goodsGrid.SetColSize( 5, 50 )
        self.goodsGrid.SetColSize( 6, 75 )
        self.goodsGrid.SetColSize( 7, 75 )
        self.goodsGrid.EnableDragColMove( False )
        self.goodsGrid.EnableDragColSize( True )
        self.goodsGrid.SetColLabelSize( 25 )
        self.goodsGrid.SetColLabelValue( 0, u"商品编码" )
        self.goodsGrid.SetColLabelValue( 1, u"商品条码" )
        self.goodsGrid.SetColLabelValue( 2, u"商品名称" )
        self.goodsGrid.SetColLabelValue( 3, u"单位" )
        self.goodsGrid.SetColLabelValue( 4, u"单价" )
        self.goodsGrid.SetColLabelValue( 5, u"数量" )
        self.goodsGrid.SetColLabelValue( 6, u"折扣" )
        self.goodsGrid.SetColLabelValue( 7, u"金额" )
        self.goodsGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        
        # Rows
        self.goodsGrid.EnableDragRowSize( False )
        self.goodsGrid.SetRowLabelSize( 80 )
        self.goodsGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        
        # Label Appearance
        
        # Cell Defaults
        self.goodsGrid.SetDefaultCellBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.goodsGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        self.goodsGrid.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
        self.goodsGrid.SetMinSize( wx.Size( 800,380 ) )
        
        GridSizer.Add( self.goodsGrid, 0, wx.ALL, 5 )
        
        
        PanelSizer.Add( GridSizer, 2, wx.BOTTOM|wx.EXPAND|wx.FIXED_MINSIZE, 10 )
        
        ButtomBarSizer = wx.BoxSizer( wx.VERTICAL )
        
        firstLine = wx.BoxSizer( wx.HORIZONTAL )
        
        self.goodsNameStaticText = wx.StaticText( self, wx.ID_ANY, u"商品名称", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsNameStaticText.Wrap( -1 )
        self.goodsNameStaticText.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        
        firstLine.Add( self.goodsNameStaticText, 0, wx.ALIGN_CENTER|wx.LEFT, 30 )
        
        self.goodsName = wx.TextCtrl( self, wx.ID_ANY, u"六神艾叶健肤沐浴露 (滋润型) 200ml （原清新健肤）", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsName.SetFont( wx.Font( 16, 70, 90, 92, False, "宋体" ) )
        self.goodsName.Enable( False )
        self.goodsName.SetMinSize( wx.Size( 600,-1 ) )
        
        firstLine.Add( self.goodsName, 0, wx.ALIGN_CENTER|wx.LEFT, 25 )
        
        
        ButtomBarSizer.Add( firstLine, 1, wx.EXPAND, 5 )
        
        SecondLine = wx.BoxSizer( wx.HORIZONTAL )
        
        self.goodsNumStaticText = wx.StaticText( self, wx.ID_ANY, u"商品数量[M]", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsNumStaticText.Wrap( -1 )
        SecondLine.Add( self.goodsNumStaticText, 0, wx.ALIGN_CENTER|wx.ALIGN_LEFT|wx.LEFT, 30 )
        
        self.goodsNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsNum.SetMinSize( wx.Size( 80,-1 ) )
        
        SecondLine.Add( self.goodsNum, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.goodsPriceStaticText = wx.StaticText( self, wx.ID_ANY, u"商品单价", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsPriceStaticText.Wrap( -1 )
        SecondLine.Add( self.goodsPriceStaticText, 0, wx.ALIGN_CENTER|wx.LEFT, 40 )
        
        self.goodsPrice = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.goodsPrice.Enable( False )
        self.goodsPrice.SetMinSize( wx.Size( 80,-1 ) )
        
        SecondLine.Add( self.goodsPrice, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        
        self.amountStaticText = wx.StaticText( self, wx.ID_ANY, u"商品金额", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.amountStaticText.Wrap( -1 )
        SecondLine.Add( self.amountStaticText, 0, wx.ALIGN_CENTER|wx.LEFT, 40 )
        
        self.amount = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.amount.Enable( False )
        self.amount.SetMinSize( wx.Size( 70,-1 ) )
        
        SecondLine.Add( self.amount, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        
        self.leftNumStaticText = wx.StaticText( self, wx.ID_ANY, u"账户余额", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.leftNumStaticText.Wrap( -1 )
        SecondLine.Add( self.leftNumStaticText, 0, wx.ALIGN_CENTER|wx.LEFT, 40 )
        
        self.leftNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.leftNum.Enable( False )
        
        SecondLine.Add( self.leftNum, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        
        ButtomBarSizer.Add( SecondLine, 1, wx.EXPAND, 5 )
        
        PanelSizer.Add( ButtomBarSizer, 8, wx.EXPAND, 5 )
        
        self.SetSizer( PanelSizer )
        self.Layout()
        
        #键盘事件绑定
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.SetFocus()
        #为所有按钮绑定键盘事件
        self.returnBtn.Bind(wx.EVT_KEY_DOWN,self.OnKeyDown)
        self.balanceBtn.Bind(wx.EVT_KEY_DOWN,self.OnKeyDown)
        self.delBtn.Bind(wx.EVT_KEY_DOWN,self.OnKeyDown)
        
        
        #按钮点击绑定
        self.returnBtn.Bind(wx.EVT_LEFT_DOWN,self.OnReturn)
        

    def OnKeyDown(self, event):#快捷键配置
         
         print(event.GetKeyCode())
         if(event.GetKeyCode()==341):
             self.OnReturn(None)
         event.Skip()     
             
         
    def  OnReturn(self,event):  #退款与收银页面的切换
        self.GetParent().Hide()
        app=wx.GetApp()
        app.ReturnFrame.Show()
             
         


class ReturnPage ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        PanelSizer = wx.BoxSizer( wx.VERTICAL )
        
        ButtonSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.balanceBtn = wx.Button( self, wx.ID_ANY, u"结算[Q]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.balanceBtn, 0, wx.ALL, 5 )
        
        self.returnBtn = wx.Button( self, wx.ID_ANY, u"销售[F2]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.returnBtn, 0, wx.ALL, 5 )
        
        self.delBtn = wx.Button( self, wx.ID_ANY, u"删除[DEL]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtonSizer.Add( self.delBtn, 0, wx.ALL, 5 )
        
        
        PanelSizer.Add( ButtonSizer, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.LEFT, 10 )
        
        self.staticLine = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        PanelSizer.Add( self.staticLine, 0, wx.EXPAND |wx.ALL, 5 )
        
        TollBarSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.StaticTextQuery = wx.StaticText( self, wx.ID_ANY, u"输入查询", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.StaticTextQuery.Wrap( -1 )
        TollBarSizer.Add( self.StaticTextQuery, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT|wx.RIGHT, 15 )
        
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
        TollBarSizer.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL, 15 )
        
        self.staticTextNum = wx.StaticText( self, wx.ID_ANY, u"应收金额", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.staticTextNum.Wrap( -1 )
        TollBarSizer.Add( self.staticTextNum, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT, 210 )
        
        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        self.m_textCtrl5.Enable( False )
        
        TollBarSizer.Add( self.m_textCtrl5, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT, 5 )
        
        
        PanelSizer.Add( TollBarSizer, 2, 0, 5 )
        
        self.staticLine2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        PanelSizer.Add( self.staticLine2, 0, wx.EXPAND |wx.ALL, 5 )
        
        GridSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.goodsGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        
        # Grid
        self.goodsGrid.CreateGrid( 50, 8 )
        self.goodsGrid.EnableEditing( True )
        self.goodsGrid.EnableGridLines( True )
        self.goodsGrid.EnableDragGridSize( False )
        self.goodsGrid.SetMargins( 0, 0 )
        
        # Columns
        self.goodsGrid.SetColSize( 0, 75 )
        self.goodsGrid.SetColSize( 1, 75 )
        self.goodsGrid.SetColSize( 2, 150 )
        self.goodsGrid.SetColSize( 3, 50 )
        self.goodsGrid.SetColSize( 4, 75 )
        self.goodsGrid.SetColSize( 5, 50 )
        self.goodsGrid.SetColSize( 6, 75 )
        self.goodsGrid.SetColSize( 7, 75 )
        self.goodsGrid.EnableDragColMove( False )
        self.goodsGrid.EnableDragColSize( True )
        self.goodsGrid.SetColLabelSize( 25 )
        self.goodsGrid.SetColLabelValue( 0, u"商品编码" )
        self.goodsGrid.SetColLabelValue( 1, u"商品条码" )
        self.goodsGrid.SetColLabelValue( 2, u"商品名称" )
        self.goodsGrid.SetColLabelValue( 3, u"单位" )
        self.goodsGrid.SetColLabelValue( 4, u"单价" )
        self.goodsGrid.SetColLabelValue( 5, u"数量" )
        self.goodsGrid.SetColLabelValue( 6, u"折扣" )
        self.goodsGrid.SetColLabelValue( 7, u"金额" )
        self.goodsGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        
        # Rows
        self.goodsGrid.EnableDragRowSize( False )
        self.goodsGrid.SetRowLabelSize( 80 )
        self.goodsGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        
        # Label Appearance
        
        # Cell Defaults
        self.goodsGrid.SetDefaultCellBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.goodsGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        self.goodsGrid.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
        self.goodsGrid.SetMinSize( wx.Size( 800,380 ) )
        
        GridSizer.Add( self.goodsGrid, 0, wx.ALL, 5 )
        
        
        PanelSizer.Add( GridSizer, 2, wx.BOTTOM|wx.EXPAND|wx.FIXED_MINSIZE, 10 )
        
        ButtomBarSizer = wx.BoxSizer( wx.VERTICAL )
        
        firstLine = wx.BoxSizer( wx.HORIZONTAL )
        
        self.goodsNameStaticText = wx.StaticText( self, wx.ID_ANY, u"商品名称", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsNameStaticText.Wrap( -1 )
        self.goodsNameStaticText.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        
        firstLine.Add( self.goodsNameStaticText, 0, wx.ALIGN_CENTER|wx.LEFT, 30 )
        
        self.goodsName = wx.TextCtrl( self, wx.ID_ANY, u"六神艾叶健肤沐浴露 (滋润型) 200ml （原清新健肤）", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsName.SetFont( wx.Font( 16, 70, 90, 92, False, "宋体" ) )
        self.goodsName.Enable( False )
        self.goodsName.SetMinSize( wx.Size( 600,-1 ) )
        
        firstLine.Add( self.goodsName, 0, wx.ALIGN_CENTER|wx.LEFT, 25 )
        
        
        ButtomBarSizer.Add( firstLine, 1, wx.EXPAND, 5 )
        
        SecondLine = wx.BoxSizer( wx.HORIZONTAL )
        
        self.goodsNumStaticText = wx.StaticText( self, wx.ID_ANY, u"商品数量[M]", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsNumStaticText.Wrap( -1 )
        SecondLine.Add( self.goodsNumStaticText, 0, wx.ALIGN_CENTER|wx.ALIGN_LEFT|wx.LEFT, 30 )
        
        self.goodsNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsNum.SetMinSize( wx.Size( 80,-1 ) )
        
        SecondLine.Add( self.goodsNum, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.goodsPriceStaticText = wx.StaticText( self, wx.ID_ANY, u"商品单价", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsPriceStaticText.Wrap( -1 )
        SecondLine.Add( self.goodsPriceStaticText, 0, wx.ALIGN_CENTER|wx.LEFT, 40 )
        
        self.goodsPrice = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.goodsPrice.Enable( False )
        self.goodsPrice.SetMinSize( wx.Size( 80,-1 ) )
        
        SecondLine.Add( self.goodsPrice, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        
        self.amountStaticText = wx.StaticText( self, wx.ID_ANY, u"商品金额", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.amountStaticText.Wrap( -1 )
        SecondLine.Add( self.amountStaticText, 0, wx.ALIGN_CENTER|wx.LEFT, 40 )
        
        self.amount = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.amount.Enable( False )
        self.amount.SetMinSize( wx.Size( 70,-1 ) )
        
        SecondLine.Add( self.amount, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        
        self.leftNumStaticText = wx.StaticText( self, wx.ID_ANY, u"账户余额", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.leftNumStaticText.Wrap( -1 )
        SecondLine.Add( self.leftNumStaticText, 0, wx.ALIGN_CENTER|wx.LEFT, 40 )
        
        self.leftNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.leftNum.Enable( False )
        
        SecondLine.Add( self.leftNum, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        
        ButtomBarSizer.Add( SecondLine, 1, wx.EXPAND, 5 )
        
        PanelSizer.Add( ButtomBarSizer, 8, wx.EXPAND, 5 )
        
        self.SetSizer( PanelSizer )
        self.Layout()
        
        #键盘事件绑定
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.SetFocus()
        #为所有按钮绑定键盘事件
        self.returnBtn.Bind(wx.EVT_KEY_DOWN,self.OnKeyDown)
        self.balanceBtn.Bind(wx.EVT_KEY_DOWN,self.OnKeyDown)
        self.delBtn.Bind(wx.EVT_KEY_DOWN,self.OnKeyDown)
        
        #按钮点击绑定
        self.returnBtn.Bind(wx.EVT_LEFT_DOWN,self.OnCache)
        
    
    def OnKeyDown(self, event):#快捷键配置
         print(event.GetKeyCode())
         if(event.GetKeyCode()==341):
             self.OnCache(None)
         event.Skip()     
    
    def  OnCache(self,event):  #退款与收银页面的切换
        self.GetParent().Hide()
        app=wx.GetApp()
        app.Cashframe.Show()
        

class KeyCodeConfigPage ( wx.Panel ):
    
    
    def getKeyCodeValue(self,keyPageDescription,operatename): #根据所在的页面和操作的名称 获取快捷键的值,比如F1,F2
        for i in range(0,len(self.dbKeyCode)):
            if(self.dbKeyCode[i][0]==operatename and self.dbKeyCode[i][4]==keyPageDescription):
                return self.dbKeyCode[i][3]
            
    
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        #初始化的时候查询出所有的快捷键配置项
        app=wx.GetApp()
        app.conn.execute("select operatename,keyCode,description ,KeyValue ,keyPageDescription from  config_keycode")
        self.dbKeyCode =app.conn.fetchall()
        
        
        MainSizer = wx.BoxSizer( wx.VERTICAL )
        
        #第一行
        FirstSizer = wx.BoxSizer( wx.HORIZONTAL )
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"保存[S]", wx.DefaultPosition, wx.DefaultSize, 0 )
        FirstSizer.Add( self.m_button3, 0, wx.ALL, 5 )
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"界面", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        self.m_staticText7.SetFont( wx.Font( 24, 70, 90, 90, False, "宋体" ) )
        FirstSizer.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.LEFT, 10 )
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"按钮", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        self.m_staticText8.SetFont( wx.Font( 24, 70, 90, 90, False, "宋体" ) )
        FirstSizer.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.LEFT, 180 )
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"操作键", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        self.m_staticText9.SetFont( wx.Font( 24, 70, 90, 90, False, "宋体" ) )
        FirstSizer.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.LEFT, 130 )
        MainSizer.Add( FirstSizer, 1, wx.EXPAND, 5 )
        self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        MainSizer.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        #第二行---左边两部分
        SecondSizer = wx.BoxSizer( wx.HORIZONTAL )
        bSizer8 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"收银界面", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        self.m_staticText10.SetFont( wx.Font( 26, 70, 90, 90, False, "宋体" ) )
        bSizer8.Add( self.m_staticText10, 1, wx.ALIGN_CENTER, 60 )
        SecondSizer.Add( bSizer8, 1, 0, 0 )
        bSizer10 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"结算", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        self.m_staticText11.SetFont( wx.Font( 16, 70, 90, 90, False, "宋体" ) )
        bSizer10.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALIGN_LEFT|wx.LEFT, 0 )
        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"退货", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        self.m_staticText12.SetFont( wx.Font( 16, 70, 90, 90, False, "宋体" ) )
        bSizer10.Add( self.m_staticText12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        self.m_staticText13.SetFont( wx.Font( 16, 70, 90, 90, False, "宋体" ) )
        bSizer10.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"输入查询", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        self.m_staticText14.SetFont( wx.Font( 15, 70, 90, 90, False, "宋体" ) )
        bSizer10.Add( self.m_staticText14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"退款方式", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        self.m_staticText15.SetFont( wx.Font( 16, 70, 90, 90, False, "宋体" ) )
        bSizer10.Add( self.m_staticText15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        SecondSizer.Add( bSizer10, 1, wx.EXPAND, 5 )
        #第二行---右边快捷键部分
        FirstConfigSizer = wx.BoxSizer( wx.VERTICAL )
        self.m_textCtrl14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl14.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl14 : self.TextCtrlKeyDown(evt,self.m_textCtrl14))
        self.m_textCtrl14.SetValue(self.getKeyCodeValue(u"收银界面", u"结算"))
        self.m_textCtrl14.SetFocus()
        FirstConfigSizer.Add( self.m_textCtrl14, 0, wx.LEFT, 7 )
        self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl21.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl21 : self.TextCtrlKeyDown(evt,self.m_textCtrl21))
        self.m_textCtrl21.SetValue(self.getKeyCodeValue(u"收银界面", u"退货"))
        FirstConfigSizer.Add( self.m_textCtrl21, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl22.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl22 : self.TextCtrlKeyDown(evt,self.m_textCtrl22))
        self.m_textCtrl22.SetValue(self.getKeyCodeValue(u"收银界面", u"删除"))
        FirstConfigSizer.Add( self.m_textCtrl22, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl23.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl23 : self.TextCtrlKeyDown(evt,self.m_textCtrl23))
        self.m_textCtrl23.SetValue(self.getKeyCodeValue(u"收银界面", u"输入查询"))
        FirstConfigSizer.Add( self.m_textCtrl23, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl24.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl24 : self.TextCtrlKeyDown(evt,self.m_textCtrl24))
        self.m_textCtrl24.SetValue(self.getKeyCodeValue(u"收银界面", u"退款方式"))
        FirstConfigSizer.Add( self.m_textCtrl24, 0, wx.LEFT|wx.TOP, 7 )
        SecondSizer.Add( FirstConfigSizer, 1, wx.EXPAND, 5 )
        MainSizer.Add( SecondSizer, 5, wx.EXPAND|wx.LEFT, 15 )
        self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        MainSizer.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        #第三行---左边两部分
        ThirdSizer = wx.BoxSizer( wx.HORIZONTAL )
        bSizer18 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"收款明细", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        self.m_staticText16.SetFont( wx.Font( 26, 70, 90, 90, False, "宋体" ) )
        bSizer18.Add( self.m_staticText16, 1, wx.ALIGN_CENTER|wx.LEFT, 25 )
        ThirdSizer.Add( bSizer18, 1, wx.EXPAND, 5 )
        bSizer21 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"支付方式", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        self.m_staticText17.SetFont( wx.Font( 15, 70, 90, 90, False, "宋体" ) )
        bSizer21.Add( self.m_staticText17, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"收款金额", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )
        self.m_staticText18.SetFont( wx.Font( 16, 70, 90, 90, False, "宋体" ) )
        bSizer21.Add( self.m_staticText18, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"手机", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        self.m_staticText19.SetFont( wx.Font( 15, 70, 90, 90, False, "宋体" ) )
        bSizer21.Add( self.m_staticText19, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"收款", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        self.m_staticText20.SetFont( wx.Font( 15, 70, 90, 90, False, "宋体" ) )
        bSizer21.Add( self.m_staticText20, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        ThirdSizer.Add( bSizer21, 1, wx.LEFT, 15 )
        #第三行---右边快捷键部分
        bSizer22 = wx.BoxSizer( wx.VERTICAL )
        self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl20.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl20 : self.TextCtrlKeyDown(evt,self.m_textCtrl20))
        self.m_textCtrl20.SetValue(self.getKeyCodeValue(u"收款明细", u"支付方式"))
        bSizer22.Add( self.m_textCtrl20, 0, wx.LEFT, 7 )
        self.m_textCtrl25 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl25.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl25 : self.TextCtrlKeyDown(evt,self.m_textCtrl25))
        self.m_textCtrl25.SetValue(self.getKeyCodeValue(u"收款明细", u"收款金额"))
        bSizer22.Add( self.m_textCtrl25, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl26 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl26.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl26 : self.TextCtrlKeyDown(evt,self.m_textCtrl26))
        self.m_textCtrl26.SetValue(self.getKeyCodeValue(u"收款明细", u"手机"))
        bSizer22.Add( self.m_textCtrl26, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl27 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl27.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl27 : self.TextCtrlKeyDown(evt,self.m_textCtrl27))
        self.m_textCtrl27.SetValue(self.getKeyCodeValue(u"收款明细", u"收款"))
        bSizer22.Add( self.m_textCtrl27, 0, wx.LEFT|wx.TOP, 7 )
        ThirdSizer.Add( bSizer22, 1, wx.EXPAND|wx.LEFT, 5 )
        MainSizer.Add( ThirdSizer, 4, wx.EXPAND, 5 )
        self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        MainSizer.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        #第四行---左边部分
        FourthSizer = wx.BoxSizer( wx.HORIZONTAL )
        bSizer23 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"退货界面", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )
        self.m_staticText21.SetFont( wx.Font( 26, 70, 90, 90, False, "宋体" ) )
        bSizer23.Add( self.m_staticText21, 0, wx.ALIGN_CENTER|wx.LEFT, 25 )
        FourthSizer.Add( bSizer23, 1, wx.EXPAND, 5 )
        bSizer26 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"结算", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )
        self.m_staticText22.SetFont( wx.Font( 16, 70, 90, 90, False, "宋体" ) )
        bSizer26.Add( self.m_staticText22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"销售", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )
        self.m_staticText23.SetFont( wx.Font( 16, 70, 90, 90, False, "宋体" ) )
        bSizer26.Add( self.m_staticText23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24.Wrap( -1 )
        self.m_staticText24.SetFont( wx.Font( 16, 70, 90, 90, False, "宋体" ) )
        bSizer26.Add( self.m_staticText24, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"输入查询", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( -1 )
        self.m_staticText25.SetFont( wx.Font( 16, 70, 90, 90, False, "宋体" ) )
        bSizer26.Add( self.m_staticText25, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"商品数量", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText30.Wrap( -1 )
        self.m_staticText30.SetFont( wx.Font( 16, 70, 90, 90, False, "宋体" ) )
        bSizer26.Add( self.m_staticText30, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        FourthSizer.Add( bSizer26, 1, wx.EXPAND|wx.LEFT, 15 )
        #第四行---右边快捷键部分
        bSizer27 = wx.BoxSizer( wx.VERTICAL )
        self.m_textCtrl28 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl28.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl28 : self.TextCtrlKeyDown(evt,self.m_textCtrl28))
        self.m_textCtrl28.SetValue(self.getKeyCodeValue(u"退货界面", u"结算"))
        bSizer27.Add( self.m_textCtrl28, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl29 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl29.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl29 : self.TextCtrlKeyDown(evt,self.m_textCtrl29))
        self.m_textCtrl29.SetValue(self.getKeyCodeValue(u"退货界面", u"销售"))
        bSizer27.Add( self.m_textCtrl29, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl30 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl30.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl30 : self.TextCtrlKeyDown(evt,self.m_textCtrl30))
        self.m_textCtrl30.SetValue(self.getKeyCodeValue(u"退货界面", u"删除"))
        bSizer27.Add( self.m_textCtrl30, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl31 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl31.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl31 : self.TextCtrlKeyDown(evt,self.m_textCtrl31))
        self.m_textCtrl31.SetValue(self.getKeyCodeValue(u"退货界面", u"输入查询"))
        bSizer27.Add( self.m_textCtrl31, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl32 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl32.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl32 : self.TextCtrlKeyDown(evt,self.m_textCtrl32))
        self.m_textCtrl32.SetValue(self.getKeyCodeValue(u"退货界面", u"商品数量"))
        bSizer27.Add( self.m_textCtrl32, 0, wx.LEFT|wx.TOP, 7 )
        FourthSizer.Add( bSizer27, 1, wx.EXPAND|wx.LEFT, 5 )
        MainSizer.Add( FourthSizer, 5, wx.EXPAND, 5 )
        self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        MainSizer.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
        
        #第五行---左边部分
        FifthSizer = wx.BoxSizer( wx.HORIZONTAL )
        bSizer28 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"退款", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )
        self.m_staticText31.SetFont( wx.Font( 26, 70, 90, 90, False, "宋体" ) )
        bSizer28.Add( self.m_staticText31, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT, 25 )
        FifthSizer.Add( bSizer28, 1, wx.EXPAND, 5 )
        bSizer31 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"退款方式", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText32.Wrap( -1 )
        self.m_staticText32.SetFont( wx.Font( 16, 70, 90, 90, False, "宋体" ) )
        bSizer31.Add( self.m_staticText32, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        FifthSizer.Add( bSizer31, 1, wx.EXPAND|wx.LEFT, 15 )
        #第无行---右边快捷键部分
        bSizer32 = wx.BoxSizer( wx.VERTICAL )
        self.m_textCtrl33 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl33.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl33 : self.TextCtrlKeyDown(evt,self.m_textCtrl33))
        self.m_textCtrl33.SetValue(self.getKeyCodeValue(u"退款", u"退款方式"))
        bSizer32.Add( self.m_textCtrl33, 0, wx.ALL, 5 )
        FifthSizer.Add( bSizer32, 1, wx.EXPAND|wx.LEFT, 7 )
        MainSizer.Add( FifthSizer, 1, wx.EXPAND, 5 )

        
        self.SetSizer( MainSizer )
        self.Layout()
    
       
        
            
    def TextCtrlKeyDown(self,event,target):
            keyCode=event.GetKeyCode()
            
            if(keyCode==83):#保存按钮
                pass
            if(keyCode>=340 and keyCode <=351):
                str=datas.KeyCodes[keyCode]
                target.SetValue(str)
                
                
                
                
                
                
                
                
                
                
                
                
                
