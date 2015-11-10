#coding:utf-8
import wx
import wx.xrc
import wx.grid


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
        
        
class KeyCodeConfigPage(self):     
    pass