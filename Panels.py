#coding:utf-8
import wx
import Frames
import wx.xrc
import wx.grid
import datas
from decimal import *
import Utils
import Print

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
        
        self.queryBtn = wx.Button( self, wx.ID_ANY, u"商品查询[F2]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.queryBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.returnBtn = wx.Button( self, wx.ID_ANY, u"退货[F3]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.returnBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.pswChangeBtn = wx.Button( self, wx.ID_ANY, u"修改密码[F4]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.pswChangeBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.querysalesBtn = wx.Button( self, wx.ID_ANY, u"销售单查询[F5]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.querysalesBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.printSettingsBtn = wx.Button( self, wx.ID_ANY, u"打印设置[F6]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.printSettingsBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.returnQueryBtn = wx.Button( self, wx.ID_ANY, u"退货单查询[F7]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.returnQueryBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.keyCodeConfig = wx.Button( self, wx.ID_ANY, u"快捷键配置[F8]", wx.DefaultPosition, wx.DefaultSize, 0 )
        ButtomGridSizer.Add( self.keyCodeConfig, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.dailyReportBtn = wx.Button( self, wx.ID_ANY, u"销售日结[F9]", wx.DefaultPosition, wx.DefaultSize, 0 )
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
        self.queryBtn.Bind(wx.EVT_LEFT_DOWN,self.OnGoodsQuery)
        self.returnBtn.Bind(wx.EVT_LEFT_DOWN,self.OnReturn)
#        self.pswChangeBtn.Bind(wx.EVT_LEFT_DOWN, self.OnKeyDown)
        self.querysalesBtn.Bind(wx.EVT_LEFT_DOWN, self.SaleOrderQuery)
        self.printSettingsBtn.Bind(wx.EVT_LEFT_DOWN, self.OnprintConfig)
        self.returnQueryBtn.Bind(wx.EVT_LEFT_DOWN, self.ReturnOrderQuery)
        self.keyCodeConfig.Bind(wx.EVT_LEFT_DOWN,self.OnKeyCodeConfig)
#        self.dailyReportBtn.Bind(wx.EVT_LEFT_DOWN, self.OnKeyDown)
        self.ExitBtn.Bind(wx.EVT_LEFT_DOWN,self.OnExit)
        
             
    def OnKeyDown(self, event):#快捷键配置
         keyCode=event.GetKeyCode()
         if(keyCode==340): #F1收银    
             self.onCash(None)
         if(keyCode==341): #F2商品查询
             self.OnGoodsQuery(None)
         if(event.GetKeyCode()==342):#F3 退货
             self.OnReturn(None)
         if(event.GetKeyCode()==343):#F4 修改密码
             pass
         if(event.GetKeyCode()==344):#F5 销售单查询
             self.SaleOrderQuery(None)
         if(event.GetKeyCode()==345):#F6 打印配置
             self.OnprintConfig(None)
         if(event.GetKeyCode()==346):#F7 退货单查询
             self.ReturnOrderQuery(None)
         if(keyCode==347): #F8 快捷键配置
             self.OnKeyCodeConfig(None)
         if(keyCode==348): #F9 销售日结
             pass
         if(keyCode==27):
             self.OnExit(None)
         return   
     
     
    def ReturnOrderQuery(self,event):
        app=wx.GetApp()
        app.Homeframe.Hide()
        Frames.returnOrderQueryFrame()
     
    def SaleOrderQuery(self,event):
        app=wx.GetApp()
        app.Homeframe.Hide()
        Frames.saleOrderQueryFrame()
      
    def OnGoodsQuery(self,event):
        app = wx.GetApp()
        app.Homeframe.Hide()
        Frames.GoodsQueryFrame()
         
    def onCash(self,event): #收银按钮事件
        app = wx.GetApp()
        app.Homeframe.Hide()
        Frames.cashFrame()

    def OnReturn(self,event):#退货
        dialog = wx.TextEntryDialog(None,u"请输入销售单号",u"请输入", "", style=wx.OK|wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            saleId=dialog.GetValue()
            sql="select id ,date,salerid,salername,purchtype,customerid,customername from sale_order where id = ?"
            saleOrder=Utils.query(sql,(saleId,))
            if(len(saleOrder)==0):
                wx.MessageBox(u"    未找到指定销售单               ", u"提醒",wx.OK | wx.ICON_ASTERISK)
                dialog.Destroy()
                return;
            
            sql="select orderid,goodsid,goodsname,goodsnum,mainunit,barcode,discount,saleprice,amount  from sale_order_detail where orderid = ? "
            saleOrderDetail=Utils.query(sql,(saleId,))
            if(len(saleOrderDetail)==0):
                wx.MessageBox(u"    此销售单无商品信息              ", u"提醒",wx.OK | wx.ICON_ASTERISK)
                dialog.Destroy()
                return;
            Frames.ReturnFrame(saleOrder,saleOrderDetail)
            app=wx.GetApp()
            app.Homeframe.Hide()
        else:
            dialog.Destroy()
            return 
    def OnprintConfig(self,event):  #打印配置事件
        Frames.printConfigFrame()
        app=wx.GetApp()
        app.Homeframe.Hide()
           
    def OnKeyCodeConfig(self,event): #快捷键配置
        app = wx.GetApp()
        app.Homeframe.Hide()    
        Frames.KeyCodeConfigFrame()
        
        
    def OnExit(self,event): #退出按钮事件
        self.GetParent().CloseHomeFrame(None)    

class CashPage ( wx.Panel ):
    
    def __init__( self, parent ):
        
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        sql="select operatename,keyCode,KeyValue from config_keycode  where keyPageDescription= ? "
        self.KeyCodesConfigs = Utils.query(sql,(u"收银界面",))
        
        PanelSizer = wx.BoxSizer( wx.VERTICAL )
        
        
        
        #上面的按钮
        ButtonSizer = wx.BoxSizer( wx.HORIZONTAL )
        str=self.getKeyCodeAndValueByName(u"结算")
        self.balanceBtn = wx.Button( self, wx.ID_ANY,u"结算["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        ButtonSizer.Add( self.balanceBtn, 0, wx.ALL, 5 )
        str=self.getKeyCodeAndValueByName(u"退货")
        self.returnBtn = wx.Button( self, wx.ID_ANY, u"退货["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        ButtonSizer.Add( self.returnBtn, 0, wx.ALL, 5 )
        str=self.getKeyCodeAndValueByName(u"删除")
        self.delBtn = wx.Button( self, wx.ID_ANY, u"删除["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        ButtonSizer.Add( self.delBtn, 0, wx.ALL, 5 )
        PanelSizer.Add( ButtonSizer, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.LEFT, 10 )
        
        ifshowBtn=Utils.query(sql,(u"按钮显示",))[0][2]
        if(ifshowBtn[0:2]=="隐藏"):
            self.balanceBtn.Hide()
            self.returnBtn.Hide()
            self.delBtn.Hide()
            
        self.staticLine = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        PanelSizer.Add( self.staticLine, 0, wx.EXPAND |wx.ALL, 5 )
        
        #输入查询,应收金额
        TollBarSizer = wx.BoxSizer( wx.HORIZONTAL )
        str=self.getKeyCodeAndValueByName(u"输入查询")
        self.StaticTextQuery = wx.StaticText( self, wx.ID_ANY, u"输入查询["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.StaticTextQuery.Wrap( -1 )
        TollBarSizer.Add( self.StaticTextQuery, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT|wx.RIGHT, 15 )
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), wx.TE_PROCESS_ENTER,name="QueryText" )
        TollBarSizer.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL, 15 )
        self.m_textCtrl4.SetFocus()
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
        self.goodsGrid.CreateGrid( 0, 8 )
        self.goodsGrid.EnableEditing( False )
        self.goodsGrid.EnableGridLines( True )
        self.goodsGrid.EnableDragGridSize( True )
        self.goodsGrid.SetMargins( 0, 0 )
        self.goodsGrid.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.goodsGrid.SetWindowStyle(0)
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
        self.goodsGrid.Enable( True )
        self.goodsGrid.SetMinSize( wx.Size( 800,380 ) )
        GridSizer.Add( self.goodsGrid, 0, wx.ALL, 5 )
        PanelSizer.Add( GridSizer, 2, wx.BOTTOM|wx.EXPAND|wx.FIXED_MINSIZE, 10 )
        
        
        #最下面的两部分
        ButtomBarSizer = wx.BoxSizer( wx.VERTICAL )
        firstLine = wx.BoxSizer( wx.HORIZONTAL )
        self.goodsNameStaticText = wx.StaticText( self, wx.ID_ANY, u"商品名称", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsNameStaticText.Wrap( -1 )
        self.goodsNameStaticText.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        #最下面的第一部分
        firstLine.Add( self.goodsNameStaticText, 0, wx.ALIGN_CENTER|wx.LEFT, 30 )
        self.goodsName = wx.TextCtrl( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsName.SetFont( wx.Font( 16, 70, 90, 92, False, "宋体" ) )
        self.goodsName.Enable( False )
        self.goodsName.SetMinSize( wx.Size( 600,-1 ) )
        firstLine.Add( self.goodsName, 0, wx.ALIGN_CENTER|wx.LEFT, 25 )
        ButtomBarSizer.Add( firstLine, 1, wx.EXPAND, 5 )
        #最下面的第二部分
        SecondLine = wx.BoxSizer( wx.HORIZONTAL )
        str=self.getKeyCodeAndValueByName(u"商品数量")
        self.goodsNumStaticText = wx.StaticText( self, wx.ID_ANY, u"商品数量["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize)
        self.goodsNumStaticText.Wrap( -1 )
        SecondLine.Add( self.goodsNumStaticText, 0, wx.ALIGN_CENTER|wx.ALIGN_LEFT|wx.LEFT, 30 )
        self.goodsNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER,name="NumberText"  )
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
        self.leftNum = wx.TextCtrl( self, wx.ID_ANY, '0.0', wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.leftNum.Enable( False )
        SecondLine.Add( self.leftNum, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        ButtomBarSizer.Add( SecondLine, 1, wx.EXPAND, 5 )
        PanelSizer.Add( ButtomBarSizer, 8, wx.EXPAND, 5 )
        
        self.SetSizer( PanelSizer )
        self.Layout()
        
        
        #为所有按钮,输入框,表格 绑定键盘事件
        self.returnBtn.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.returnBtn : self.OnKeyDown(evt,self.returnBtn))
        self.balanceBtn.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.balanceBtn : self.OnKeyDown(evt,self.balanceBtn))
        self.delBtn.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.delBtn : self.OnKeyDown(evt,self.delBtn))
        self.goodsGrid.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.goodsGrid : self.OnKeyDown(evt,self.goodsGrid))
        self.m_textCtrl4.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl4 : self.OnKeyDown(evt,self.m_textCtrl4))
        self.goodsNum.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.goodsNum : self.OnKeyDown(evt,self.goodsNum))
        
        
        ##取消表格的所有点击事件,默认为选中第一条数据
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_SELECT_CELL,self.PreventEvent)
        #商品名称输入框回车事件
        self.m_textCtrl4.Bind(wx.EVT_TEXT_ENTER, lambda evt, target=self.m_textCtrl4 : self.QueryGoods(evt,self.m_textCtrl4))
        #商品数量输入框回车事件
        self.goodsNum.Bind(wx.EVT_TEXT_ENTER, lambda evt, target=self.goodsNum : self.InsertNumber(evt,self.goodsNum))
        
        
        #按钮点击绑定
        self.balanceBtn.Bind(wx.EVT_LEFT_DOWN,self.OnCache)
        self.delBtn.Bind(wx.EVT_LEFT_DOWN,self.deleteSelectRow)
        self.returnBtn.Bind(wx.EVT_LEFT_DOWN,self.OnReturn)
        
        # 取消表格的所有点击事件
        self.goodsGrid.Bind( wx.EVT_LEFT_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEFT_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MOTION, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEFT_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEAVE_WINDOW, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_ENTER_WINDOW, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MOUSEWHEEL, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_SET_FOCUS, self.PreventEvent )
        
        
        
    def PreventEvent(self,event): ##取消表格的所有点击事件,点击默认选中 输入查询这个框
         self.m_textCtrl4.SetFocus()
        
    def getKeyCodeAndValueByName(self,operateName): #根据操作名称获取操作的KeyCode和KeyCodeValue(快捷键部分)
        for i in range(0,len(self.KeyCodesConfigs)):
            if(self.KeyCodesConfigs[i][0]==operateName):
                return (self.KeyCodesConfigs[i][1],self.KeyCodesConfigs[i][2])
          
    def OnKeyDown(self, event,target):#快捷键
         keyCode=event.GetKeyCode()
         
         if(keyCode==27):
           self.GetParent().ClosecashFrame(None)
           return
         
         if(keyCode==self.getKeyCodeAndValueByName(u"结算")[0]):
             self.OnCache(None)
             return
         
         
         if(keyCode==self.getKeyCodeAndValueByName(u"退货")[0]):
             self.OnReturn(None)
             return
         
         
         if(keyCode==self.getKeyCodeAndValueByName(u"删除")[0]):
             self.deleteSelectRow(None)
             return
         
         if(keyCode==315): #向上箭头的快捷键
             if(self.goodsGrid.GetNumberRows ()==0): #表格没数据,返回
                 return
             rows=self.goodsGrid.GetSelectedRows()
             if(self.goodsGrid.IsSelection () and len(rows)==1 and not rows[0]==0):#如果有选中  且只选中了一行 选中的不是第一行,选中上一行
                 self.selectRowAndUpdateInfo(rows[0]-1)
                 return 
             #否则选中最后一行
             self.selectRowAndUpdateInfo(self.goodsGrid.GetNumberRows ()-1)
             return
         
         if(keyCode==317):#向下箭头快捷键
             if(self.goodsGrid.GetNumberRows ()==0):
                 return
             rows=self.goodsGrid.GetSelectedRows()
             numberRows=self.goodsGrid.GetNumberRows()
             if(self.goodsGrid.IsSelection() and len(rows)==1 and not rows[0]==numberRows-1):  #如果有选中 且只选中了一行 选中的不是最后一行,选中下一行
                self.selectRowAndUpdateInfo(rows[0]+1)
                return
             #否则都选中第一行
             self.selectRowAndUpdateInfo(0)
             return
         
         
         if(keyCode==self.getKeyCodeAndValueByName(u"输入查询")[0]):
            self.m_textCtrl4.SetFocus()
            self.m_textCtrl4.SelectAll()
            return
         if(keyCode==self.getKeyCodeAndValueByName(u"商品数量")[0]):
            self.goodsNum.SetFocus()
            self.goodsNum.SelectAll()
            return
            
         
         if(isinstance(target,wx._controls.TextCtrl)):  ##输入框之间的Tab切换
             if(target.GetName()=="QueryText" and keyCode==9):
                 self.goodsNum.SetFocus()
                 self.goodsNum.SelectAll()
             if(target.GetName()=="NumberText" and  keyCode==9):
                 self.m_textCtrl4.SetFocus()
                 self.m_textCtrl4.SelectAll()
         event.Skip()     
         
    def selectRowAndUpdateInfo(self,rowNum):#选中指定行,数据更新(表格之外的其他东西),焦点回到输入查询处
        self.goodsGrid.SelectRow (rowNum,False) 
        goodsName=self.goodsGrid.GetCellValue(rowNum,2) 
        singlePrice=self.goodsGrid.GetCellValue(rowNum,4)
        RowgoodsNum=self.goodsGrid.GetCellValue(rowNum,5)
        RowCount=self.goodsGrid.GetCellValue(rowNum,6)
        rowAmount=self.goodsGrid.GetCellValue(rowNum,7)
        self.goodsName.SetValue(goodsName) #商品名称
        self.goodsPrice.SetValue(singlePrice)  #商品单价
        self.goodsNum.SetValue(RowgoodsNum) #商品数量
        self.amount.SetValue(rowAmount) #底部商品金额
        self.m_textCtrl4.SetFocus()
       
    def InsertNewGoods(self,rowNum,data): #新增一行
        self.goodsGrid.SetCellValue(rowNum, 0,"%s" % data[0])
        self.goodsGrid.SetCellValue(rowNum, 1,"%s" % data[1])
        self.goodsGrid.SetCellValue(rowNum, 2,"%s" % data[2])
        self.goodsGrid.SetCellValue(rowNum, 3,"%s" % data[3])
        self.goodsGrid.SetCellValue(rowNum, 4,"%s" % data[4]) #单价
        self.goodsGrid.SetCellValue(rowNum, 5,"%s" % 1)
        self.goodsGrid.SetCellValue(rowNum, 6,"%s" % data[5])#折扣
        singleAmount=(Decimal(data[4])*Decimal(data[5])).quantize(Decimal('0.01'))
        self.goodsGrid.SetCellValue(rowNum, 7,"%s" % singleAmount) 
        
        self.goodsName.SetValue(data[2])  #商品名称
        self.goodsPrice.SetValue(data[4]) #商品单价
        self.amount.SetValue(str(singleAmount)) #商品金额
        self.goodsNum.SetValue(str(1)) #商品数量
 
    def deleteSelectRow(self,event):  #删除一行
        rows=self.goodsGrid.GetSelectedRows()
        if(len(rows)==1):
             self.goodsGrid.DeleteRows(rows[0]) #删除一行
             if(self.goodsGrid.GetNumberRows()>0): #如果还有数据,则默认选中第一行
                 self.selectRowAndUpdateInfo(0)
             else: #数据被删光了
                 self.goodsName.SetValue("") #商品名称
                 self.goodsPrice.SetValue("")  #商品单价
                 self.goodsNum.SetValue("") #商品数量
                 self.amount.SetValue("") #底部商品金额
                 self.m_textCtrl4.SetFocus()    
             self.RecalculateCachNum()
        if(len(rows)==0):
            wx.MessageBox(u"        未找到要删除的商品         ", u"提醒",wx.OK | wx.ICON_ASTERISK)  
        return         
    
    def RecalculateCachNum(self):#重新计算应收金额
        RowNum=self.goodsGrid.GetNumberRows()
        cashAmount=Decimal(0.00)
        for i in range(0,RowNum):
            Rowprice = self.goodsGrid.GetCellValue(i,4) #行单价
            Rownumber = self.goodsGrid.GetCellValue(i,5)#行数量
            RowCount = self.goodsGrid.GetCellValue(i,6) #行折扣
            rowAmount=(Decimal(Rowprice)* Decimal(Rownumber)*Decimal(RowCount)).quantize(Decimal('0.01')) #行金额
            self.goodsGrid.SetCellValue(i, 7,"%s" % rowAmount) #每行金额
            cashAmount=cashAmount+rowAmount
        cashAmount=cashAmount.quantize(Decimal('0.1'))  
        self.m_textCtrl5.SetValue(str(cashAmount))
    
    def checkGoodsRepeat(self,barcode): #判断商品是否有重复,参数为BarCode,重复返回RowNum,不重复返回""
        RowNum=self.goodsGrid.GetNumberRows()
        for i in range(0,RowNum):
            if(barcode==self.goodsGrid.GetCellValue(i,1)) :
                return i
        return ""                             
           
    def QueryGoods(self ,event ,target): #当用户输入商品条形码,按回车键触发
        goodsId=self.m_textCtrl4.GetValue();
        sql="select id,barcode,name,mainunit,saleprice,discount  from goods_info  where barcode= ? "
        result=  Utils.query(sql,(goodsId,))
        if(len(result)==0): #未找到商品
            wx.MessageBox(u"                   未找到商品         ", u"提醒",wx.OK | wx.ICON_ASTERISK)
            self.m_textCtrl4.Clear()
            return
        gooodsRepeatRow=self.checkGoodsRepeat(result[0][1])
        if(not gooodsRepeatRow==""):#判断商品是否已经购买过,如果已经购买过,在原来基础上+1
            singleprice=Decimal(self.goodsGrid.GetCellValue(gooodsRepeatRow,4)) #单价
            number=Decimal(self.goodsGrid.GetCellValue(gooodsRepeatRow,5)) #数量
            discount=Decimal(self.goodsGrid.GetCellValue(gooodsRepeatRow,6)) #折扣
            rowAmount=(singleprice*(number+1)*discount).quantize(Decimal('0.01'))
            self.goodsGrid.SetCellValue(gooodsRepeatRow,5,"%s" % (number+1)) #数量+1
            self.goodsGrid.SetCellValue(gooodsRepeatRow,7,"%s" % rowAmount) #金额
            self.selectRowAndUpdateInfo(gooodsRepeatRow)
        else :
            self.goodsGrid.AppendRows(numRows=1) #没有重复,新增一行,并且为每一行赋值
            self.InsertNewGoods(self.goodsGrid.GetNumberRows()-1,result[0])
            self.goodsGrid.SelectRow(self.goodsGrid.GetNumberRows()-1)
            
        self.m_textCtrl4.Clear()
        self.RecalculateCachNum()       
           
    def  InsertNumber(self , event , target):  ##当用户输入商品数量,按回车键触发
        if(not self.goodsGrid.IsSelection()):
            wx.MessageBox(u"              未找到要修改的数据       ", u"提醒",wx.OK | wx.ICON_ASTERISK)
            return
        val = target.GetValue();
        try:
             number=int(val)
             if(number<=0):
                  wx.MessageBox(u"   数量必须大于0 ", u"提醒",wx.OK | wx.ICON_ASTERISK)
                  target.SetFocus()
                  target.SetFocus()
                  return
             rows=self.goodsGrid.GetSelectedRows()
             if(len(rows)==1):
                 rowNum=rows[0]
                 Rowprice = self.goodsGrid.GetCellValue(rowNum,4)  #行单价
                 self.goodsGrid.SetCellValue(rowNum,5,"%s" % number) #行数量
                 RowCount = self.goodsGrid.GetCellValue(rowNum,6) #行折扣
                 rowAmount=(Decimal(Rowprice)* Decimal(number)*Decimal(RowCount)).quantize(Decimal('0.01'))
                 self.goodsGrid.SetCellValue(rowNum,7,"%s" % rowAmount) #行金额
                 self.selectRowAndUpdateInfo(rowNum)
                 self.RecalculateCachNum()
        except ValueError:
             wx.MessageBox(u"                         请输入整数        ", u"提醒",wx.OK | wx.ICON_ASTERISK)
             rows=self.goodsGrid.GetSelectedRows()
             if(len(rows)==1):
                 number = self.goodsGrid.GetCellValue(rows[0],5) #数量
                 target.SetValue(number)
                 target.SelectAll()
                 target.setFocus()
         
    def  OnReturn(self,event):  #退款与收银页面的切换
        dialog = wx.TextEntryDialog(None,u"请输入销售单号",u"请输入", "", style=wx.OK|wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            saleId=dialog.GetValue()
            sql="select id ,date,salerid,salername,purchtype,customerid,customername from sale_order where id = ?"
            saleOrder=Utils.query(sql,(saleId,))
            if(len(saleOrder)==0):
                wx.MessageBox(u"    未找到指定销售单               ", u"提醒",wx.OK | wx.ICON_ASTERISK)
                dialog.Destroy()
                return;
            
            sql="select orderid,goodsid,goodsname,goodsnum,mainunit,barcode,discount,saleprice,amount  from sale_order_detail where orderid = ? "
            saleOrderDetail=Utils.query(sql,(saleId,))
            if(len(saleOrderDetail)==0):
                wx.MessageBox(u"    此销售单无商品信息              ", u"提醒",wx.OK | wx.ICON_ASTERISK)
                dialog.Destroy()
                return;
            self.GetParent().CloseFrameAndOpenReturnPage(saleOrder,saleOrderDetail)
        dialog.Destroy()
        return
         
    def OnCache(self,event): #结算
        rowNum=self.goodsGrid.GetNumberRows()
        if(rowNum==0):
            wx.MessageBox(u"    商品信息为空,无法结算                ", u"提醒",wx.OK | wx.ICON_ASTERISK)
            return
        cashmoney=self.m_textCtrl5.GetValue()
        self.GetParent().Destroy()
        GoodsData=Utils.transFerGirdData(self.goodsGrid)
        Frames.getMoneyFrame(cashmoney,GoodsData)
        

class getMoneyPage ( wx.Panel):
    
    def __init__( self, parent ,cashMoney,GoodsData):
        self.GoodsData=GoodsData
        self.cashMoney=cashMoney
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,400 ), style = wx.TAB_TRAVERSAL )
        
        sql="select operatename,keyCode,KeyValue from config_keycode  where keyPageDescription= ? "
        self.KeyCodesConfigs = Utils.query(sql,(u"收款明细",))
        sql="select id from  dictionary where value = ?"
        result=Utils.query(sql,(u"支付方式",))
        sql="select value,val from dictionary where pid = ?"
        self.PayWay=Utils.query(sql,(result[0][0],))
        self.tmpFlag=0;#处理支付方式字典
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        #第一行
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"客户名称", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer7.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.LEFT, 0 )
        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl3.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.m_textCtrl3.Enable( False )
        self.m_textCtrl3.SetMinSize( wx.Size( 150,40 ) )
        bSizer7.Add( self.m_textCtrl3, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"账户余额", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        self.m_staticText3.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer7.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.LEFT, 25 )
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, "0.00", wx.DefaultPosition, wx.DefaultSize,  wx.TE_CENTRE  )
        self.m_textCtrl4.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.m_textCtrl4.Enable( False )
        self.m_textCtrl4.SetMinSize( wx.Size( 150,40 ) )
        bSizer7.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        bSizer6.Add( bSizer7, 1, wx.ALIGN_CENTER, 0 )
        
        #第二行
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"结算金额", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        self.m_staticText5.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer9.Add( self.m_staticText5, 0, wx.ALIGN_CENTER, 0 )
        self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,  wx.TE_CENTRE  )
        self.m_textCtrl6.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.m_textCtrl6.Enable( False )
        self.m_textCtrl6.SetValue(cashMoney) #结算金额
        self.m_textCtrl6.SetMinSize( wx.Size( 150,40 ) )
        bSizer9.Add( self.m_textCtrl6, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"找零金额", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        self.m_staticText6.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer9.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.LEFT, 25 )
        self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_CENTRE )
        self.m_textCtrl7.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.m_textCtrl7.Enable( False )
        self.m_textCtrl7.SetMinSize( wx.Size( 150,40 ) )
        bSizer9.Add( self.m_textCtrl7, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        bSizer6.Add( bSizer9, 1, wx.ALIGN_CENTER, 0 )
        
        #第三行
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        str=self.getKeyCodeAndValueByName(u"支付方式")
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY,  u"支付方式["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        self.m_staticText7.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer10.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.LEFT, 0 )
        self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER,name="PayWay")
        self.m_textCtrl8.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.m_textCtrl8.SetMinSize( wx.Size( 150,40 ) )
        bSizer10.Add( self.m_textCtrl8, 0, wx.ALIGN_CENTER|wx.LEFT, 5 )
        str=self.getKeyCodeAndValueByName(u"收款金额")
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"收款金额["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        self.m_staticText8.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer10.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.cashNum = wx.TextCtrl( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER ,name="CashNum")
        self.cashNum.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.cashNum.SetMinSize( wx.Size( 150,40 ) )
        bSizer10.Add( self.cashNum, 0, wx.ALIGN_CENTER|wx.LEFT, 5 )
        bSizer6.Add( bSizer10, 1, wx.ALIGN_CENTER, 0 )
        
        #第四行
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"账户扣款", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        self.m_staticText9.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer11.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.LEFT, 0 )
        self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl10.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.m_textCtrl10.Enable( False )
        self.m_textCtrl10.SetMinSize( wx.Size( 150,40 ) )
        bSizer11.Add( self.m_textCtrl10, 0, wx.ALIGN_CENTER|wx.LEFT, 30 )
        str=self.getKeyCodeAndValueByName(u"手机")
        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"手机["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        self.m_staticText10.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer11.Add( self.m_staticText10, 0, wx.ALIGN_CENTER|wx.LEFT, 45 )
        self.phone = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER ,name="Phone")
        self.phone.SetFont( wx.Font( 14, 70, 90, 92, False, "宋体" ) )
        self.phone.SetMinSize( wx.Size( 150,40 ) )
        bSizer11.Add( self.phone, 0, wx.ALIGN_CENTER|wx.LEFT, 25 )
        bSizer6.Add( bSizer11, 1, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 60 )
        
        #Button
        bSizer12 = wx.BoxSizer( wx.VERTICAL )
        self.m_button19 = wx.Button( self, wx.ID_ANY, u"收款[Enter]", wx.DefaultPosition, wx.Size( 150,50 ), 0 )
        self.m_button19.SetFont( wx.Font( 15, 70, 90, 92, False, "宋体" ) )
        self.m_button19.Bind(wx.EVT_BUTTON,self.CashFinish)
        bSizer12.Add( self.m_button19, 0, wx.ALIGN_CENTER|wx.TOP, 15 )
        bSizer6.Add( bSizer12, 1, wx.EXPAND, 5 )
        
        self.SetSizer( bSizer6 )
        self.Layout()
        
        self.m_textCtrl8.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl8 : self.OnKeyDown(evt,self.m_textCtrl8)) #支付方式
        self.m_textCtrl8.SetValue(self.PayWay[0][0])
        self.cashNum.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.cashNum : self.OnKeyDown(evt,self.cashNum)) #收款金额
        self.cashNum.Bind(wx.EVT_TEXT,lambda evt, target=self.cashNum : self.CashNumChange(evt,self.cashNum))
        self.phone.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.phone : self.OnKeyDown(evt,self.phone))
        self.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self : self.OnKeyDown(evt,self))
        
        
    def getPayWayval(self,PayText): #根据select的text获取value
        for i in range(0,len(self.PayWay)):
            if(self.PayWay[i][0]==PayText):
                return self.PayWay[i][1]
            
            
    def CashNumChange(self,event,target): #收款金额修改时触发的事件
        val=target.GetValue();
        if(val==""):
            return
        try :
            cashnum=Decimal(val)
            #结算金额
            AllNum=Decimal(self.m_textCtrl6.GetValue())
            leftNum=cashnum-AllNum
            if(leftNum>=0):#找零金额
                self.m_textCtrl7.SetValue(str(leftNum))
            else : #收款金额不足
                self.m_textCtrl7.SetValue(u"收款不足")
        except InvalidOperation:
            target.SetBackgroundColour("pink")
            self.m_textCtrl7.SetValue(u"输入有误")
            wx.MessageBox("输入有误", "错误")
            
            
    def CashFinish(self,event): #Enter按钮
        try:
            Decimal(self.m_textCtrl7.GetValue())
            Decimal(self.cashNum.GetValue())
            self.GetParent().Destroy()
            Frames.cashFrame()
            
            saleId=Utils.getSaleOrderId();
            #详情表
            for i in range(0 ,len(self.GoodsData)):
                sql="insert  into sale_order_detail( orderid,goodsid,goodsname,goodsnum,mainunit,barcode,discount,saleprice,amount) values(?,?,?,?,?,?,?,?,?)"
                Utils.execute(sql,(saleId,self.GoodsData[i][u"商品编码"],self.GoodsData[i][u"商品名称"],self.GoodsData[i][u"数量"],self.GoodsData[i][u"单位"],self.GoodsData[i][u"商品条码"],self.GoodsData[i][u"折扣"],self.GoodsData[i][u"单价"],self.GoodsData[i][u"金额"]   ))
            #主表
            app=wx.GetApp()
            sql="insert into sale_order(id,date,salerid,salername,purchtype,customerid,customername,amout)values (? , ? , ? , ? , ? , ? , ? ,?)"
            payWayValue=self.getPayWayval(self.m_textCtrl8.GetValue())
            Utils.commit(sql,(saleId,Utils.getDateStr(),app.Id,app.Name,payWayValue,u"",u"",self.cashMoney,))
            
            
            
            #打印小票
            self.pdata = wx.PrintData()
            self.pdata.SetPaperId(wx.PAPER_LETTER)
            self.pdata.SetOrientation(wx.PORTRAIT)
            data = wx.PrintDialogData(self.pdata)
            
            printer = wx.Printer(data)
            
            self.margins = (wx.Point(15,15), wx.Point(15,15))
            sql="select head1,head2,foot1,foot2 from config_print where id = 1"
            ConfigData=Utils.query(sql,None)
            
            
            app=wx.GetApp()
            OtherData=list()
            OtherData.append(saleId)
            OtherData.append(self.cashMoney)
            OtherData.append(app.Name)
            
            printout1 = Print.GoodsPrinter(ConfigData, self.GoodsData , "title" , OtherData)
            
            printer.Print(None,printout1,True)
            
            return
        except InvalidOperation:
            data=self.m_textCtrl7.GetValue();
            if(data=="输入有误"):
                wx.MessageBox(u"                输入有误", u"错误")
            if(data=="收款不足"):
                wx.MessageBox(u"                收款不足", u"错误")
            wx.MessageBox(u"                输入有误", u"错误")
            return
            
        
    def getKeyCodeAndValueByName(self,operateName): #根据操作名称获取操作的KeyCode和KeyCodeValue(快捷键部分)
        for i in range(0,len(self.KeyCodesConfigs)):
            if(self.KeyCodesConfigs[i][0]==operateName):
                return (self.KeyCodesConfigs[i][1],self.KeyCodesConfigs[i][2])
        
    def selectAndFocus(self,target): #让某个target选中
        target.SetFocus()
        target.SelectAll()
        
    def OnKeyDown(self,event,target):
        
        KeyCode=event.GetKeyCode()
        
        if(KeyCode==9): #TAB切换
             if(target.GetName()=="PayWay"):
                 self.selectAndFocus(self.cashNum)
             if(target.GetName()=="CashNum"):
                 self.selectAndFocus(self.phone)
             if(target.GetName()=="Phone"):
                 self.selectAndFocus(self.m_textCtrl8)
             return
        #自定义的快捷键
        if(KeyCode==self.getKeyCodeAndValueByName(u"支付方式")[0]):
            self.selectAndFocus(self.m_textCtrl8)
            return
        if(KeyCode==self.getKeyCodeAndValueByName(u"收款金额")[0]):
            self.selectAndFocus(self.cashNum)
            return
        if(KeyCode==self.getKeyCodeAndValueByName(u"手机")[0]):
            self.selectAndFocus(self.phone)
            return
        
        #回车收银确认按钮  关闭窗口 存入数据
        if(KeyCode==13 or KeyCode==370):
            self.CashFinish(None)
            
        if(KeyCode==27): #ESC
            self.GetParent().ClosegetMoneyFrame(None)
            return
        
        
        #支付方式,快捷键
        if(target.GetName()=="PayWay"):
            if(KeyCode==315):
                self.tmpFlag=self.tmpFlag-1
            if(KeyCode==317):
                self.tmpFlag=self.tmpFlag+1   
            target.SetValue(self.PayWay[self.tmpFlag%(len(self.PayWay))][0])
            return
        
        if(target.GetName()=="CashNum"):
            event.Skip()
        if(target.GetName()=="Phone"):
            event.Skip()
        
        
        
class ReturnPage ( wx.Panel ):
    def __init__( self, parent ,saleOrder,saleOrderDetail):
        self.saleOrder=saleOrder
        self.saleOrderDetail=saleOrderDetail
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        sql="select operatename,keyCode,KeyValue from config_keycode  where keyPageDescription= ? "
        self.KeyCodesConfigs = Utils.query(sql,(u"退货界面",))
        
        PanelSizer = wx.BoxSizer( wx.VERTICAL )
        
        #上面的按钮
        ButtonSizer = wx.BoxSizer( wx.HORIZONTAL )
        str=self.getKeyCodeAndValueByName(u"结算")
        self.balanceBtn = wx.Button( self, wx.ID_ANY,u"结算["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        
        ButtonSizer.Add( self.balanceBtn, 0, wx.ALL, 5 )
        str=self.getKeyCodeAndValueByName(u"销售")
        self.returnBtn = wx.Button( self, wx.ID_ANY, u"销售["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        ButtonSizer.Add( self.returnBtn, 0, wx.ALL, 5 )
        str=self.getKeyCodeAndValueByName(u"删除")
        self.delBtn = wx.Button( self, wx.ID_ANY, u"删除["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        ButtonSizer.Add( self.delBtn, 0, wx.ALL, 5 )
        PanelSizer.Add( ButtonSizer, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.LEFT, 10 )
        
        ifshowBtn=Utils.query(sql,(u"按钮显示",))[0][2]
        if(ifshowBtn[0:2]=="隐藏"):
            self.balanceBtn.Hide()
            self.returnBtn.Hide()
            self.delBtn.Hide()
        
        
        
        self.staticLine = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        PanelSizer.Add( self.staticLine, 0, wx.EXPAND |wx.ALL, 5 )
        
        #输入查询,应收金额
        TollBarSizer = wx.BoxSizer( wx.HORIZONTAL )
        str=self.getKeyCodeAndValueByName(u"输入查询")
        self.StaticTextQuery = wx.StaticText( self, wx.ID_ANY, u"输入查询["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.StaticTextQuery.Wrap( -1 )
        TollBarSizer.Add( self.StaticTextQuery, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT|wx.RIGHT, 15 )
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), wx.TE_PROCESS_ENTER,name="QueryText" )
        TollBarSizer.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL, 15 )
        self.m_textCtrl4.SetFocus()
        self.staticTextNum = wx.StaticText( self, wx.ID_ANY, u"应退金额", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
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
        self.goodsGrid.CreateGrid( 0, 8 )
        self.goodsGrid.EnableEditing( False )
        self.goodsGrid.EnableGridLines( True )
        self.goodsGrid.EnableDragGridSize( True )
        self.goodsGrid.SetMargins( 0, 0 )
        self.goodsGrid.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.goodsGrid.SetWindowStyle(0)
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
        self.goodsGrid.Enable( True )
        self.goodsGrid.SetMinSize( wx.Size( 800,380 ) )
        GridSizer.Add( self.goodsGrid, 0, wx.ALL, 5 )
        PanelSizer.Add( GridSizer, 2, wx.BOTTOM|wx.EXPAND|wx.FIXED_MINSIZE, 10 )
        
        #最下面的两部分
        ButtomBarSizer = wx.BoxSizer( wx.VERTICAL )
        firstLine = wx.BoxSizer( wx.HORIZONTAL )
        self.goodsNameStaticText = wx.StaticText( self, wx.ID_ANY, u"商品名称", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsNameStaticText.Wrap( -1 )
        self.goodsNameStaticText.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        #最下面的第一部分
        firstLine.Add( self.goodsNameStaticText, 0, wx.ALIGN_CENTER|wx.LEFT, 30 )
        self.goodsName = wx.TextCtrl( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.goodsName.SetFont( wx.Font( 16, 70, 90, 92, False, "宋体" ) )
        self.goodsName.Enable( False )
        self.goodsName.SetMinSize( wx.Size( 600,-1 ) )
        firstLine.Add( self.goodsName, 0, wx.ALIGN_CENTER|wx.LEFT, 25 )
        ButtomBarSizer.Add( firstLine, 1, wx.EXPAND, 5 )
        #最下面的第二部分
        SecondLine = wx.BoxSizer( wx.HORIZONTAL )
        str=self.getKeyCodeAndValueByName(u"商品数量")
        self.goodsNumStaticText = wx.StaticText( self, wx.ID_ANY, u"商品数量["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize)
        self.goodsNumStaticText.Wrap( -1 )
        SecondLine.Add( self.goodsNumStaticText, 0, wx.ALIGN_CENTER|wx.ALIGN_LEFT|wx.LEFT, 30 )
        self.goodsNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER,name="NumberText"  )
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
        self.leftNum = wx.TextCtrl( self, wx.ID_ANY, '0.0', wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.leftNum.Enable( False )
        SecondLine.Add( self.leftNum, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        ButtomBarSizer.Add( SecondLine, 1, wx.EXPAND, 5 )
        PanelSizer.Add( ButtomBarSizer, 8, wx.EXPAND, 5 )
        
        self.SetSizer( PanelSizer )
        self.Layout()
        
        
        #为所有按钮,输入框,表格 绑定键盘事件
        self.returnBtn.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.returnBtn : self.OnKeyDown(evt,self.returnBtn))
        self.balanceBtn.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.balanceBtn : self.OnKeyDown(evt,self.balanceBtn))
        self.delBtn.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.delBtn : self.OnKeyDown(evt,self.delBtn))
        self.goodsGrid.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.goodsGrid : self.OnKeyDown(evt,self.goodsGrid))
        self.m_textCtrl4.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl4 : self.OnKeyDown(evt,self.m_textCtrl4))
        self.goodsNum.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.goodsNum : self.OnKeyDown(evt,self.goodsNum))
        
        
        ##取消表格的所有点击事件,默认为选中第一条数据
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_SELECT_CELL,self.PreventEvent)
        #商品名称输入框回车事件
        self.m_textCtrl4.Bind(wx.EVT_TEXT_ENTER, lambda evt, target=self.m_textCtrl4 : self.QueryGoods(evt,self.m_textCtrl4))
        #商品数量输入框回车事件
        self.goodsNum.Bind(wx.EVT_TEXT_ENTER, lambda evt, target=self.goodsNum : self.InsertNumber(evt,self.goodsNum))
        
        
        #按钮点击绑定
        self.balanceBtn.Bind(wx.EVT_LEFT_DOWN,self.OnCache)
        self.delBtn.Bind(wx.EVT_LEFT_DOWN,self.deleteSelectRow)
        self.returnBtn.Bind(wx.EVT_LEFT_DOWN,self.OnSale)
        
        # 取消表格的所有点击事件
        self.goodsGrid.Bind( wx.EVT_LEFT_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEFT_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MOTION, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEFT_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEAVE_WINDOW, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_ENTER_WINDOW, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MOUSEWHEEL, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_SET_FOCUS, self.PreventEvent )
        
        
    def PreventEvent(self,event): ##取消表格的所有点击事件,点击默认选中 输入查询这个框
         self.m_textCtrl4.SetFocus()
        
    def getKeyCodeAndValueByName(self,operateName): #根据操作名称获取操作的KeyCode和KeyCodeValue(快捷键部分)
        for i in range(0,len(self.KeyCodesConfigs)):
            if(self.KeyCodesConfigs[i][0]==operateName):
                return (self.KeyCodesConfigs[i][1],self.KeyCodesConfigs[i][2])
          
    def OnKeyDown(self, event,target):#快捷键
         keyCode=event.GetKeyCode()
         if(keyCode==27):
             self.GetParent().ClosecashFrame(None)
             return
         
         if(keyCode==self.getKeyCodeAndValueByName(u"结算")[0]):
             self.OnCache(None)
             return
         
         
         if(keyCode==self.getKeyCodeAndValueByName(u"销售")[0]):
             self.OnSale(None)
             return
         
         if(keyCode==self.getKeyCodeAndValueByName(u"删除")[0]):
             self.deleteSelectRow(None)
             return
         
         if(keyCode==315): #向上箭头的快捷键
             if(self.goodsGrid.GetNumberRows ()==0): #表格没数据,返回
                 return
             rows=self.goodsGrid.GetSelectedRows()
             if(self.goodsGrid.IsSelection () and len(rows)==1 and not rows[0]==0):#如果有选中  且只选中了一行 选中的不是第一行,选中上一行
                 self.selectRowAndUpdateInfo(rows[0]-1)
                 return 
             #否则选中最后一行
             self.selectRowAndUpdateInfo(self.goodsGrid.GetNumberRows ()-1)
             return
         
         if(keyCode==317):#向下箭头快捷键
             if(self.goodsGrid.GetNumberRows ()==0):
                 return
             rows=self.goodsGrid.GetSelectedRows()
             numberRows=self.goodsGrid.GetNumberRows()
             if(self.goodsGrid.IsSelection() and len(rows)==1 and not rows[0]==numberRows-1):  #如果有选中 且只选中了一行 选中的不是最后一行,选中下一行
                self.selectRowAndUpdateInfo(rows[0]+1)
                return
             #否则都选中第一行
             self.selectRowAndUpdateInfo(0)
             return
         
         
         if(keyCode==self.getKeyCodeAndValueByName(u"输入查询")[0]):
            self.m_textCtrl4.SetFocus()
            self.m_textCtrl4.SelectAll()
            return
         if(keyCode==self.getKeyCodeAndValueByName(u"商品数量")[0]):
            self.goodsNum.SetFocus()
            self.goodsNum.SelectAll()
            return
            
         if(isinstance(target,wx._controls.TextCtrl)):  ##输入框之间的Tab切换
             if(target.GetName()=="QueryText" and keyCode==9):
                 self.goodsNum.SetFocus()
                 self.goodsNum.SelectAll()
             if(target.GetName()=="NumberText" and  keyCode==9):
                 self.m_textCtrl4.SetFocus()
                 self.m_textCtrl4.SelectAll()
         event.Skip()     
         
    def selectRowAndUpdateInfo(self,rowNum):#选中指定行,数据更新(表格之外的其他东西),焦点回到输入查询处
        self.goodsGrid.SelectRow (rowNum,False) 
        goodsName=self.goodsGrid.GetCellValue(rowNum,2) 
        singlePrice=self.goodsGrid.GetCellValue(rowNum,4)
        RowgoodsNum=self.goodsGrid.GetCellValue(rowNum,5)
        RowCount=self.goodsGrid.GetCellValue(rowNum,6)
        rowAmount=self.goodsGrid.GetCellValue(rowNum,7)
        self.goodsName.SetValue(goodsName) #商品名称
        self.goodsPrice.SetValue(singlePrice)  #商品单价
        self.goodsNum.SetValue(RowgoodsNum) #商品数量
        self.amount.SetValue(rowAmount) #底部商品金额
        self.m_textCtrl4.SetFocus()
       
    def InsertNewGoods(self,rowNum,data): #新增一行
        #sql="select id ,date,salerid,salername,purchtype,customerid,customername from sale_order where id = ?"
#        sql="select orderid,goodsid,goodsname,goodsnum,mainunit,barcode,discount,saleprice,amount  from sale_order_detail where orderid = ? "
        self.goodsGrid.SetCellValue(rowNum, 0,"%s" % data[1])#商品编码
        self.goodsGrid.SetCellValue(rowNum, 1,"%s" % data[5])#商品条码
        self.goodsGrid.SetCellValue(rowNum, 2,"%s" % data[2])#商品名称
        self.goodsGrid.SetCellValue(rowNum, 3,"%s" % data[4])#单位
        self.goodsGrid.SetCellValue(rowNum, 4,"%s" % data[7]) #单价
        self.goodsGrid.SetCellValue(rowNum, 5,"%s" % 1)
        self.goodsGrid.SetCellValue(rowNum, 6,"%s" % data[6])#折扣
        singleAmount=(Decimal(data[7])*Decimal(data[6])).quantize(Decimal('0.01')) #数量*折扣
        self.goodsGrid.SetCellValue(rowNum, 7,"%s" % singleAmount) 
        self.goodsName.SetValue(data[2])  #商品名称
        self.goodsPrice.SetValue(data[7]) #商品单价
        self.amount.SetValue(str(singleAmount)) #商品金额
        self.goodsNum.SetValue(str(1)) #商品数量
 
    def deleteSelectRow(self,event):  #删除一行
        rows=self.goodsGrid.GetSelectedRows()
        if(len(rows)==1):
             self.goodsGrid.DeleteRows(rows[0]) #删除一行
             if(self.goodsGrid.GetNumberRows()>0): #如果还有数据,则默认选中第一行
                 self.selectRowAndUpdateInfo(0)
             else: #数据被删光了
                 self.goodsName.SetValue("") #商品名称
                 self.goodsPrice.SetValue("")  #商品单价
                 self.goodsNum.SetValue("") #商品数量
                 self.amount.SetValue("") #底部商品金额
                 self.m_textCtrl4.SetFocus()    
             self.RecalculateCachNum()
        if(len(rows)==0):     
             wx.MessageBox(u"        未找到要删除的商品         ", u"提醒",wx.OK | wx.ICON_ASTERISK)
        return              
    
    def RecalculateCachNum(self):#重新计算应收金额
        RowNum=self.goodsGrid.GetNumberRows()
        cashAmount=Decimal(0.00)
        for i in range(0,RowNum):
            Rowprice = self.goodsGrid.GetCellValue(i,4) #行单价
            Rownumber = self.goodsGrid.GetCellValue(i,5)#行数量
            RowCount = self.goodsGrid.GetCellValue(i,6) #行折扣
            rowAmount=(Decimal(Rowprice)* Decimal(Rownumber)*Decimal(RowCount)).quantize(Decimal('0.01')) #行金额
            self.goodsGrid.SetCellValue(i, 7,"%s" % rowAmount) #每行金额
            cashAmount=cashAmount+rowAmount
        cashAmount=cashAmount.quantize(Decimal('0.1'))  
        self.m_textCtrl5.SetValue(str(cashAmount))
    
    def checkGoodsRepeat(self,barcode): #判断商品是否有重复,参数为BarCode,重复返回RowNum,不重复返回""
        RowNum=self.goodsGrid.GetNumberRows()
        for i in range(0,RowNum):
            if(barcode==self.goodsGrid.GetCellValue(i,1)) :
                return i
        return ""                             
    
        
           
    def QueryGoods(self ,event ,target): #当用户输入商品条形码,按回车键触发
        
#        sql="select id ,date,salerid,salername,purchtype,customerid,customername from sale_order where id = ?"
#        sql="select orderid,goodsid,goodsname,goodsnum,mainunit,barcode,discount,saleprice,amount from sale_order_detail where orderid = ? "
        goodsId=self.m_textCtrl4.GetValue();
        result=""
        for i in range(0 ,len(self.saleOrderDetail)):
            if(self.saleOrderDetail[i][5]==goodsId):
                result=self.saleOrderDetail[i];
                break
        if(result==""): #未找到商品
            wx.MessageBox(u"                   未找到商品         ", u"提醒",wx.OK | wx.ICON_ASTERISK)
            self.m_textCtrl4.Clear()
            return
        gooodsRepeatRow=self.checkGoodsRepeat(result[5])
        
        if(not gooodsRepeatRow==""):#判断商品是否已经购买过,如果已经购买过,在原来基础上+1
            maxNum=Decimal(result[3])
            singleprice=Decimal(self.goodsGrid.GetCellValue(gooodsRepeatRow,4)) #单价
            number=Decimal(self.goodsGrid.GetCellValue(gooodsRepeatRow,5)) #数量
            if(number+1>maxNum):
                self.m_textCtrl4.Clear()
                wx.MessageBox(u"      退货数量已达到最大        ", u"提醒",wx.OK | wx.ICON_ASTERISK)
                return
            discount=Decimal(self.goodsGrid.GetCellValue(gooodsRepeatRow,6)) #折扣
            rowAmount=(singleprice*(number+1)*discount).quantize(Decimal('0.01'))
            self.goodsGrid.SetCellValue(gooodsRepeatRow,5,"%s" % (number+1)) #数量+1
            self.goodsGrid.SetCellValue(gooodsRepeatRow,7,"%s" % rowAmount) #金额
            self.selectRowAndUpdateInfo(gooodsRepeatRow)
        else :
            self.goodsGrid.AppendRows(numRows=1) #没有重复,新增一行,并且为每一行赋值
            self.InsertNewGoods(self.goodsGrid.GetNumberRows()-1,result)
            self.goodsGrid.SelectRow(self.goodsGrid.GetNumberRows()-1)
            
        self.m_textCtrl4.Clear()
        self.RecalculateCachNum()       
      
    def getNumberLimit(self,goodsId):
        for i in range(0,len(self.saleOrderDetail)):
            if(self.saleOrderDetail[i][1]==goodsId):
                return self.saleOrderDetail[i][3]
      
           
    def  InsertNumber(self , event , target):  ##当用户输入商品数量,按回车键触发
        if(not self.goodsGrid.IsSelection()):
            wx.MessageBox(u"              未找到要修改的数据       ", u"提醒",wx.OK | wx.ICON_ASTERISK)
            return
        val = target.GetValue();
        try:
             number=int(val)
             if(number<=0):
                  wx.MessageBox(u"   数量必须大于0 ", u"提醒",wx.OK | wx.ICON_ASTERISK)
                  target.SetFocus()
                  target.SelectAll()
                  return
             rows=self.goodsGrid.GetSelectedRows()
             if(len(rows)==1):
                 rowNum=rows[0]
                 goodsId=self.goodsGrid.GetCellValue(rows[0],0)
                 maxNum=self.getNumberLimit(goodsId)
                 if(number>int(maxNum)):
                     wx.MessageBox(u"     超出可退货最大数量 :"+str(maxNum), u"提醒",wx.OK | wx.ICON_ASTERISK)
                     target.SetFocus()
                     target.SelectAll()
                     return
                 Rowprice = self.goodsGrid.GetCellValue(rowNum,4)  #行单价
                 self.goodsGrid.SetCellValue(rowNum,5,"%s" % number) #行数量
                 RowCount = self.goodsGrid.GetCellValue(rowNum,6) #行折扣
                 rowAmount=(Decimal(Rowprice)* Decimal(number)*Decimal(RowCount)).quantize(Decimal('0.01'))
                 self.goodsGrid.SetCellValue(rowNum,7,"%s" % rowAmount) #行金额
                 self.selectRowAndUpdateInfo(rowNum)
                 self.RecalculateCachNum()
        except ValueError:
             wx.MessageBox(u"                         请输入整数        ", u"提醒",wx.OK | wx.ICON_ASTERISK)
             rows=self.goodsGrid.GetSelectedRows()
             if(len(rows)==1):
                 number = self.goodsGrid.GetCellValue(rows[0],5) #数量
                 target.SetValue(number)
                 target.SelectAll()
                 target.setFocus()
         
    def  OnSale(self,event):  #退款与收银页面的切换
        self.GetParent().CloseFrameAndOpenSalePage()
        return
         
    def OnCache(self,event): #结算
        rowNum=self.goodsGrid.GetNumberRows()
        if(rowNum==0):
            wx.MessageBox(u"    商品信息为空,无法结算                ", u"提醒",wx.OK | wx.ICON_ASTERISK)
            return
        cashmoney=self.m_textCtrl5.GetValue()
        self.GetParent().Destroy()
        GoodsData=Utils.transFerGirdData(self.goodsGrid)
        Frames.returnMoneyFrame(cashmoney,GoodsData,self.saleOrder[0][0],self.saleOrder,self.saleOrderDetail)
        
        
        
class returnMoneyPage ( wx.Panel):
    
    def __init__( self, parent ,cashMoney,GoodsData,saleOrderId,saleOrder,saleOrderDetail):
        self.GoodsData=GoodsData
        self.saleOrderId=saleOrderId
        self.saleOrder=saleOrder
        self.saleOrderDetail=saleOrderDetail
        
        sql="select value from syscode where name = ? "
        self.AllowNum=Decimal(Utils.query(sql,(u"退款允许差额",))[0][0])
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,400 ), style = wx.TAB_TRAVERSAL )
        
        sql="select operatename,keyCode,KeyValue from config_keycode  where keyPageDescription= ? "
        self.KeyCodesConfigs = Utils.query(sql,(u"收款明细",))
        
        sql="select id from  dictionary where value = ?"
        result= Utils.query(sql,(u"支付方式",))
        sql="select value,val from dictionary where pid = ?"
        self.PayWay=Utils.query(sql,(result[0][0],))
        self.tmpFlag=0;#处理支付方式字典
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        #第一行
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"客户名称", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer7.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.LEFT, 0 )
        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl3.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.m_textCtrl3.Enable( False )
        self.m_textCtrl3.SetMinSize( wx.Size( 150,40 ) )
        bSizer7.Add( self.m_textCtrl3, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"账户余额", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        self.m_staticText3.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer7.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.LEFT, 25 )
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, "0.00", wx.DefaultPosition, wx.DefaultSize,  wx.TE_CENTRE  )
        self.m_textCtrl4.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.m_textCtrl4.Enable( False )
        self.m_textCtrl4.SetMinSize( wx.Size( 150,40 ) )
        bSizer7.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        bSizer6.Add( bSizer7, 1, wx.ALIGN_CENTER, 0 )
        
        #第二行
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"结算金额", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        self.m_staticText5.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer9.Add( self.m_staticText5, 0, wx.ALIGN_CENTER, 0 )
        self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,  wx.TE_CENTRE  )
        self.m_textCtrl6.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.m_textCtrl6.Enable( False )
        self.m_textCtrl6.SetValue(cashMoney) #结算金额
        self.m_textCtrl6.SetMinSize( wx.Size( 150,40 ) )
        bSizer9.Add( self.m_textCtrl6, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"未退金额", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        self.m_staticText6.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer9.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.LEFT, 25 )
        self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_CENTRE )
        self.m_textCtrl7.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.m_textCtrl7.Enable( False )
        self.m_textCtrl7.SetMinSize( wx.Size( 150,40 ) )
        bSizer9.Add( self.m_textCtrl7, 0, wx.ALIGN_CENTER|wx.LEFT, 15 )
        bSizer6.Add( bSizer9, 1, wx.ALIGN_CENTER, 0 )
        
        #第三行
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        str=self.getKeyCodeAndValueByName(u"支付方式")
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY,  u"退款方式["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        self.m_staticText7.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer10.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.LEFT, 0 )
        self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER,name="PayWay")
        self.m_textCtrl8.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.m_textCtrl8.SetMinSize( wx.Size( 150,40 ) )
        bSizer10.Add( self.m_textCtrl8, 0, wx.ALIGN_CENTER|wx.LEFT, 5 )
        str=self.getKeyCodeAndValueByName(u"收款金额")
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"现金退款["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        self.m_staticText8.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer10.Add( self.m_staticText8, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.cashNum = wx.TextCtrl( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER ,name="CashNum")
        self.cashNum.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.cashNum.SetMinSize( wx.Size( 150,40 ) )
        bSizer10.Add( self.cashNum, 0, wx.ALIGN_CENTER|wx.LEFT, 5 )
        bSizer6.Add( bSizer10, 1, wx.ALIGN_CENTER, 0 )
        
        #第四行
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"账户扣款", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        self.m_staticText9.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer11.Add( self.m_staticText9, 0, wx.ALIGN_CENTER|wx.LEFT, 0 )
        self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl10.SetFont( wx.Font( 22, 70, 90, 92, False, "宋体" ) )
        self.m_textCtrl10.Enable( False )
        self.m_textCtrl10.SetMinSize( wx.Size( 150,40 ) )
        bSizer11.Add( self.m_textCtrl10, 0, wx.ALIGN_CENTER|wx.LEFT, 30 )
        str=self.getKeyCodeAndValueByName(u"手机")
        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"手机["+str[1]+"]", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        self.m_staticText10.SetFont( wx.Font( 18, 70, 90, 90, False, "宋体" ) )
        bSizer11.Add( self.m_staticText10, 0, wx.ALIGN_CENTER|wx.LEFT, 45 )
        self.phone = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_CENTRE|wx.TE_PROCESS_ENTER ,name="Phone")
        self.phone.SetFont( wx.Font( 14, 70, 90, 92, False, "宋体" ) )
        self.phone.SetMinSize( wx.Size( 150,40 ) )
        bSizer11.Add( self.phone, 0, wx.ALIGN_CENTER|wx.LEFT, 25 )
        bSizer6.Add( bSizer11, 1, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 60 )
        
        #Button
        bSizer12 = wx.BoxSizer( wx.VERTICAL )
        self.m_button19 = wx.Button( self, wx.ID_ANY, u"退款[Enter]", wx.DefaultPosition, wx.Size( 150,50 ), 0 )
        self.m_button19.SetFont( wx.Font( 15, 70, 90, 92, False, "宋体" ) )
        self.m_button19.Bind(wx.EVT_BUTTON,self.CashFinish)
        bSizer12.Add( self.m_button19, 0, wx.ALIGN_CENTER|wx.TOP, 15 )
        bSizer6.Add( bSizer12, 1, wx.EXPAND, 5 )
        
        self.SetSizer( bSizer6 )
        self.Layout()
        self.m_textCtrl8.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl8 : self.OnKeyDown(evt,self.m_textCtrl8)) #支付方式
        self.m_textCtrl8.SetValue(self.PayWay[0][0])
        self.cashNum.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.cashNum : self.OnKeyDown(evt,self.cashNum)) #收款金额
        self.cashNum.Bind(wx.EVT_TEXT,lambda evt, target=self.cashNum : self.CashNumChange(evt,self.cashNum))
        self.phone.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.phone : self.OnKeyDown(evt,self.phone))
        self.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self : self.OnKeyDown(evt,self))
        
    def getPayWayval(self,PayText): #根据select的text获取value
        for i in range(0,len(self.PayWay)):
            if(self.PayWay[i][0]==PayText):
                return self.PayWay[i][1]

        
    def CashNumChange(self,event,target): #收款金额修改时触发的事件
        val=target.GetValue();
        if(val==""):
            return
        try :
            cashnum=Decimal(val)
            #退款金额
            AllNum=Decimal(self.m_textCtrl6.GetValue())
            leftNum=AllNum-cashnum
            if(leftNum <= self.AllowNum and  leftNum >= -self.AllowNum):#未退金额
                self.m_textCtrl7.SetValue(str(leftNum))
            else : #退款过多
                self.m_textCtrl7.SetValue(u"差额过大")
        except InvalidOperation:
            target.SetBackgroundColour("pink")
            self.m_textCtrl7.SetValue(u"输入有误")
            wx.MessageBox(u"输入有误", u"错误")
            
            
    def CashFinish(self,event): #Enter按钮
        try:
            app=wx.GetApp()
            Decimal(self.m_textCtrl7.GetValue())
            Decimal(self.cashNum.GetValue())
            self.GetParent().Destroy()
            app.Homeframe.Show()
            returnId=Utils.getReturnOrderId();
            #详情表
            for i in range(0 ,len(self.GoodsData)):
                sql="insert  into return_order_detail( orderid,goodsid,goodsname,goodsnum,mainunit,barcode,discount,saleprice,amount) values(?,?,?,?,?,?,?,?,?)"
                Utils.execute(sql,(returnId,self.GoodsData[i][u"商品编码"],self.GoodsData[i][u"商品名称"],self.GoodsData[i][u"数量"],self.GoodsData[i][u"单位"],self.GoodsData[i][u"商品条码"],self.GoodsData[i][u"折扣"],self.GoodsData[i][u"单价"],self.GoodsData[i][u"金额"]   ))
            #主表
            sql="insert into return_order(id,date,salerid,salername,purchtype,customerid,customername,saleorderid,settleaccount,realreturn)values (? , ? , ? , ? , ? , ? , ? , ? , ? , ?)"
            payWayValue=self.getPayWayval(self.m_textCtrl8.GetValue())
            Utils.commit(sql,(returnId,Utils.getDateStr(),app.Id,app.Name,payWayValue,u"",u"",self.saleOrderId,self.m_textCtrl6.GetValue(),self.cashNum.GetValue(),))
            return
        except InvalidOperation:
            wx.MessageBox(u"                输入有误", u"错误")
            return
            
        
    def getKeyCodeAndValueByName(self,operateName): #根据操作名称获取操作的KeyCode和KeyCodeValue(快捷键部分)
        for i in range(0,len(self.KeyCodesConfigs)):
            if(self.KeyCodesConfigs[i][0]==operateName):
                return (self.KeyCodesConfigs[i][1],self.KeyCodesConfigs[i][2])
        
    def selectAndFocus(self,target): #让某个target选中
        target.SetFocus()
        target.SelectAll()
        
    def OnKeyDown(self,event,target):
        
        KeyCode=event.GetKeyCode()
        
        if(KeyCode==9): #TAB切换
             if(target.GetName()=="PayWay"):
                 self.selectAndFocus(self.cashNum)
             if(target.GetName()=="CashNum"):
                 self.selectAndFocus(self.phone)
             if(target.GetName()=="Phone"):
                 self.selectAndFocus(self.m_textCtrl8)
             return
        #自定义的快捷键
        if(KeyCode==self.getKeyCodeAndValueByName(u"支付方式")[0]):
            self.selectAndFocus(self.m_textCtrl8)
            return
        if(KeyCode==self.getKeyCodeAndValueByName(u"收款金额")[0]):
            self.selectAndFocus(self.cashNum)
            return
        if(KeyCode==self.getKeyCodeAndValueByName(u"手机")[0]):
            self.selectAndFocus(self.phone)
            return
        
        #回车收银确认按钮  关闭窗口 存入数据
        if(KeyCode==13 or KeyCode==370):
            self.CashFinish(None)
            
        if(KeyCode==27): #ESC
            self.GetParent().ClosereturnMoneyFrame(None)
            #ESC返回上以页面,保留用户之前输入的销售单号
            Frames.ReturnFrame(self.saleOrder,self.saleOrderDetail)
            return
        
        
        #支付方式,快捷键
        if(target.GetName()=="PayWay"):
            if(KeyCode==315):
                self.tmpFlag=self.tmpFlag-1
            if(KeyCode==317):
                self.tmpFlag=self.tmpFlag+1   
            target.SetValue(self.PayWay[self.tmpFlag%(len(self.PayWay))][0])
            return
        
        if(target.GetName()=="CashNum"):
            event.Skip()
            
        if(target.GetName()=="Phone"):
            event.Skip()
            
    

class KeyCodeConfigPage ( wx.Panel ):
    
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        #初始化的时候查询出所有的快捷键配置项
        self.dbKeyCode=Utils.query("select operatename,keyCode,description ,KeyValue ,keyPageDescription from  config_keycode",None)
        
        MainSizer = wx.BoxSizer( wx.VERTICAL )
        
        #第一行
        FirstSizer = wx.BoxSizer( wx.HORIZONTAL )
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"保存[S]", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button3.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_button3 : self.TextCtrlKeyDown(evt,self.m_button3))
        self.m_button3.Bind(wx.EVT_BUTTON, self.saveConfig, self.m_button3)
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
        
        
        self.buttonShow = wx.TextCtrl( self, wx.ID_ANY, u"显示按钮[K]", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.buttonShow.SetValue(self.getKeyCodeValue(u"按钮显示", u"按钮显示"))
        self.buttonShow.SetEditable( False )
        FirstSizer.Add( self.buttonShow, 0, wx.ALIGN_CENTER|wx.LEFT, 20 )
        
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
        self.m_textCtrl14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode1")
        self.m_textCtrl14.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl14 : self.TextCtrlKeyDown(evt,self.m_textCtrl14))
        self.m_textCtrl14.SetValue(self.getKeyCodeValue(u"收银界面", u"结算"))
        self.m_textCtrl14.SetFocus()
        FirstConfigSizer.Add( self.m_textCtrl14, 0, wx.LEFT, 7 )
        self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode2")
        self.m_textCtrl21.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl21 : self.TextCtrlKeyDown(evt,self.m_textCtrl21))
        self.m_textCtrl21.SetValue(self.getKeyCodeValue(u"收银界面", u"退货"))
        FirstConfigSizer.Add( self.m_textCtrl21, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode3")
        self.m_textCtrl22.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl22 : self.TextCtrlKeyDown(evt,self.m_textCtrl22))
        self.m_textCtrl22.SetValue(self.getKeyCodeValue(u"收银界面", u"删除"))
        FirstConfigSizer.Add( self.m_textCtrl22, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl23 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode4")
        self.m_textCtrl23.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl23 : self.TextCtrlKeyDown(evt,self.m_textCtrl23))
        self.m_textCtrl23.SetValue(self.getKeyCodeValue(u"收银界面", u"输入查询"))
        FirstConfigSizer.Add( self.m_textCtrl23, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl24 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode5")
        self.m_textCtrl24.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl24 : self.TextCtrlKeyDown(evt,self.m_textCtrl24))
        self.m_textCtrl24.SetValue(self.getKeyCodeValue(u"收银界面", u"商品数量"))
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
        ThirdSizer.Add( bSizer21, 1, wx.LEFT, 15 )
        #第三行---右边快捷键部分
        bSizer22 = wx.BoxSizer( wx.VERTICAL )
        self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode6")
        self.m_textCtrl20.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl20 : self.TextCtrlKeyDown(evt,self.m_textCtrl20))
        self.m_textCtrl20.SetValue(self.getKeyCodeValue(u"收款明细", u"支付方式"))
        bSizer22.Add( self.m_textCtrl20, 0, wx.LEFT, 7 )
        self.m_textCtrl25 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode7")
        self.m_textCtrl25.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl25 : self.TextCtrlKeyDown(evt,self.m_textCtrl25))
        self.m_textCtrl25.SetValue(self.getKeyCodeValue(u"收款明细", u"收款金额"))
        bSizer22.Add( self.m_textCtrl25, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl26 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode8")
        self.m_textCtrl26.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl26 : self.TextCtrlKeyDown(evt,self.m_textCtrl26))
        self.m_textCtrl26.SetValue(self.getKeyCodeValue(u"收款明细", u"手机"))
        bSizer22.Add( self.m_textCtrl26, 0, wx.LEFT|wx.TOP, 7 )
        ThirdSizer.Add( bSizer22, 1, wx.EXPAND|wx.LEFT, 5 )
        MainSizer.Add( ThirdSizer, 3, wx.EXPAND, 5 )
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
        self.m_textCtrl28 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode9")
        self.m_textCtrl28.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl28 : self.TextCtrlKeyDown(evt,self.m_textCtrl28))
        self.m_textCtrl28.SetValue(self.getKeyCodeValue(u"退货界面", u"结算"))
        bSizer27.Add( self.m_textCtrl28, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl29 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode10")
        self.m_textCtrl29.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl29 : self.TextCtrlKeyDown(evt,self.m_textCtrl29))
        self.m_textCtrl29.SetValue(self.getKeyCodeValue(u"退货界面", u"销售"))
        bSizer27.Add( self.m_textCtrl29, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl30 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode11")
        self.m_textCtrl30.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl30 : self.TextCtrlKeyDown(evt,self.m_textCtrl30))
        self.m_textCtrl30.SetValue(self.getKeyCodeValue(u"退货界面", u"删除"))
        bSizer27.Add( self.m_textCtrl30, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl31 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode12")
        self.m_textCtrl31.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl31 : self.TextCtrlKeyDown(evt,self.m_textCtrl31))
        self.m_textCtrl31.SetValue(self.getKeyCodeValue(u"退货界面", u"输入查询"))
        bSizer27.Add( self.m_textCtrl31, 0, wx.LEFT|wx.TOP, 7 )
        self.m_textCtrl32 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode13")
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
        self.m_textCtrl33 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 ,name="keycode14")
        self.m_textCtrl33.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.m_textCtrl33 : self.TextCtrlKeyDown(evt,self.m_textCtrl33))
        self.m_textCtrl33.SetValue(self.getKeyCodeValue(u"退款", u"退款方式"))
        bSizer32.Add( self.m_textCtrl33, 0, wx.ALL, 5 )
        FifthSizer.Add( bSizer32, 1, wx.EXPAND|wx.LEFT, 7 )
        MainSizer.Add( FifthSizer, 1, wx.EXPAND, 5 )

        self.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self : self.TextCtrlKeyDown(evt,self))
        self.SetSizer( MainSizer )
        self.Layout()
        
        
    def getKeyCodeValue(self,keyPageDescription,operatename): #根据所在的页面和操作的名称 获取快捷键的值,比如F1,F2
        for i in range(0,len(self.dbKeyCode)):
            if(self.dbKeyCode[i][0]==operatename and self.dbKeyCode[i][4]==keyPageDescription):
                return self.dbKeyCode[i][3]            
            
            
    def TextCtrlKeyDown(self,event,target):
            keyCode=event.GetKeyCode()
            if(keyCode==83):#保存按钮 S
                self.saveConfig(None)
            if(keyCode==27):#退出按钮ESC 
                self.GetParent().CloseKeyCodeConfigFrame(None)  
            if(keyCode>=340 and keyCode <=351 and isinstance(target,wx._controls.TextCtrl)):
                str=datas.KeyCodes[keyCode]
                target.SetValue(str)
            if(keyCode==75): #显示按钮,隐藏按钮
                val=self.buttonShow.GetValue();
                if(val==u"显示按钮[K]"):
                   self.buttonShow.SetValue(u"隐藏按钮[K]")
                else :
                    self.buttonShow.SetValue(u"显示按钮[K]") 
            if(keyCode==317):    #向下箭头的快捷键
                name=target.GetName()
                intVal=int(name[7:len(name)])
                if(intVal < 14):
                    nameVal=unicode(int(name[7:len(name)])+1)
                    selectTarget=wx.FindWindowByName(u"keycode"+nameVal)
                    selectTarget.SetFocus()
                    selectTarget.SelectAll()
                else : #最后一个按钮 向下箭头
                    selectTarget=wx.FindWindowByName(u"keycode1")
                    selectTarget.SetFocus()
                    selectTarget.SelectAll()
                return    
            if(keyCode==315):   #向上箭头的快捷键
                name=target.GetName()
                intVal=int(name[7:len(name)])
                if(intVal < 2): #第一个按钮向上箭头
                    selectTarget=wx.FindWindowByName("keycode14")
                    selectTarget.SetFocus()
                    selectTarget.SelectAll()
                else :  
                    nameVal=unicode(int(name[7:len(name)])-1)
                    selectTarget=wx.FindWindowByName(u"keycode"+nameVal)
                    selectTarget.SetFocus()
                    selectTarget.SelectAll()
                return    
                
                
                
                
    def saveConfig(self,event):
        result=self.checkDataAvailable();
        if(result!=""): #如果有错误 则直接提示
            
            wx.MessageBox(result, u"错误",wx.OK | wx.ICON_ERROR)
        else :  #如果没有错误,则更新数据库数据
            sql="update config_keycode set keyCode = ? ,KeyValue = ? where operatename= ? and keyPageDescription = ? "
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl14.GetValue()],self.m_textCtrl14.GetValue(),u"结算",u"收银界面",))
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl21.GetValue()],self.m_textCtrl21.GetValue(),u"退货",u"收银界面",))
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl22.GetValue()],self.m_textCtrl22.GetValue(),u"删除",u"收银界面",))
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl23.GetValue()],self.m_textCtrl23.GetValue(),u"输入查询",u"收银界面",))
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl24.GetValue()],self.m_textCtrl24.GetValue(),u"退款方式",u"收银界面",))
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl20.GetValue()],self.m_textCtrl20.GetValue(),u"支付方式",u"收款明细",))
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl25.GetValue()],self.m_textCtrl25.GetValue(),u"收款金额",u"收款明细",))
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl26.GetValue()],self.m_textCtrl26.GetValue(),u"手机",u"收款明细",))
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl28.GetValue()],self.m_textCtrl28.GetValue(),u"结算",u"退货界面",))
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl29.GetValue()],self.m_textCtrl29.GetValue(),u"销售",u"退货界面",))
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl30.GetValue()],self.m_textCtrl30.GetValue(),u"删除",u"退货界面",))
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl31.GetValue()],self.m_textCtrl31.GetValue(),u"输入查询",u"退货界面",))
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl32.GetValue()],self.m_textCtrl32.GetValue(),u"商品数量",u"退货界面",))
            Utils.execute(sql,(datas.KeyCodesReserve[self.m_textCtrl33.GetValue()],self.m_textCtrl33.GetValue(),u"退款方式",u"退款",))
            btnConfig=self.buttonShow.GetValue()
            Utils.commit(sql,(0,btnConfig,u"按钮显示",u"按钮显示"))
            wx.MessageBox(u"                          保存成功           ", u"提醒",wx.OK | wx.ICON_ASTERISK)
            self.GetParent().CloseKeyCodeConfigFrame(None)
                
    def  checkDataAvailable(self): #判断设置的快捷键是否有效(同一页面是否重复)  如果配置有效,则返回"" 无效则返回错误信息
        result="";
        
        x=set()
        #收银界面
        x.add( self.m_textCtrl14.GetValue())
        x.add( self.m_textCtrl21.GetValue())
        x.add( self.m_textCtrl22.GetValue())
        x.add( self.m_textCtrl23.GetValue())
        x.add( self.m_textCtrl24.GetValue())
        if(len(x)<5):
            result=result+u"收银界面,"
            
        x.clear()    
        x.add( self.m_textCtrl20.GetValue())
        x.add( self.m_textCtrl25.GetValue())
        x.add( self.m_textCtrl26.GetValue())
        if(len(x)<3):
            result=result+u"收款明细,"
                
        x.clear()          
        x.add( self.m_textCtrl28.GetValue())
        x.add( self.m_textCtrl29.GetValue())
        x.add( self.m_textCtrl30.GetValue())
        x.add( self.m_textCtrl31.GetValue())
        x.add( self.m_textCtrl32.GetValue())       
        if(len(x)<5):
            result=result+u"退货界面,"    
        if(len(result)>0):
            result=result[0:len(result)-1]
            return result+u"有快捷键冲突"
        return ""        
                
class GoodsPage ( wx.Panel ):
    
    def __init__( self, parent ):
        
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        PanelSizer = wx.BoxSizer( wx.VERTICAL )
        #输入查询,应收金额
        TollBarSizer = wx.BoxSizer( wx.HORIZONTAL )
        self.StaticTextQuery = wx.StaticText( self, wx.ID_ANY, u"输入查询", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.StaticTextQuery.Wrap( -1 )
        TollBarSizer.Add( self.StaticTextQuery, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT|wx.RIGHT, 15 )
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), wx.TE_PROCESS_ENTER,name="QueryText" )
        TollBarSizer.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL, 15 )
        self.m_textCtrl4.SetFocus()
        PanelSizer.Add( TollBarSizer, 5, 0, 5 )
        self.staticLine2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        PanelSizer.Add( self.staticLine2, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        GridSizer = wx.BoxSizer( wx.VERTICAL )
        self.goodsGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        # Grid
        self.goodsGrid.CreateGrid( 0, 8 )
        self.goodsGrid.EnableEditing( False )
        self.goodsGrid.EnableGridLines( True )
        self.goodsGrid.EnableDragGridSize( True )
        self.goodsGrid.SetMargins( 0, 0 )
        self.goodsGrid.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.goodsGrid.SetWindowStyle(0)
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
        self.goodsGrid.SetColLabelValue( 4, u"箱装量" )
        self.goodsGrid.SetColLabelValue( 5, u"零售价" )
        self.goodsGrid.SetColLabelValue( 6, u"状态" )
        self.goodsGrid.SetColLabelValue( 7, u"备注" )
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
        self.goodsGrid.Enable( True )
        self.goodsGrid.SetMinSize( wx.Size( 800,460 ) )
        GridSizer.Add( self.goodsGrid, 0, wx.ALL, 5 )
        PanelSizer.Add( GridSizer, 15, wx.BOTTOM|wx.EXPAND|wx.FIXED_MINSIZE, 10 )
        
        self.SetSizer( PanelSizer )
        self.Layout()
        
        
        #为输入框绑定键盘事件
        self.m_textCtrl4.Bind(wx.wx.EVT_KEY_DOWN,self.OnKeyDown)
        
        ##取消表格的所有点击事件,默认为选中第一条数据
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_SELECT_CELL,self.PreventEvent)
        
        # 取消表格的所有点击事件
        self.goodsGrid.Bind( wx.EVT_LEFT_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEFT_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MOTION, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEFT_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEAVE_WINDOW, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_ENTER_WINDOW, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MOUSEWHEEL, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_SET_FOCUS, self.PreventEvent )
        
        
    def PreventEvent(self,event): ##取消表格的所有点击事件,点击默认选中 输入查询这个框
         self.m_textCtrl4.SetFocus()
        
    def OnKeyDown(self, event):#快捷键
         keyCode=event.GetKeyCode()
         print(keyCode)
         
         if(keyCode==13 or keyCode==370):
             self.QueryGoods()
         if(keyCode==27):
           self.GetParent().CloseGoodsQueryFrame(None)
         event.Skip()
         
    def InsertNewGoods(self,rowNum,data): #新增一行
        self.goodsGrid.SetCellValue(rowNum, 0,"%s" % data[0])
        self.goodsGrid.SetCellValue(rowNum, 1,"%s" % data[1])
        self.goodsGrid.SetCellValue(rowNum, 2,"%s" % data[2])
        self.goodsGrid.SetCellValue(rowNum, 3,"%s" % data[3])
        self.goodsGrid.SetCellValue(rowNum, 4,"%s" % data[4]) #箱装量
        self.goodsGrid.SetCellValue(rowNum, 5,"%s" % data[5])
        status=""
        if(data[6]=="1"):
            status=u"启用"
        if(data[6]=="0"):
            status=u"禁用"
        self.goodsGrid.SetCellValue(rowNum, 6,"%s" % status)#状态
        self.goodsGrid.SetCellValue(rowNum, 7,"%s" % data[7]) #备注 
        
           
    def QueryGoods(self): #当用户输入商品条形码,按回车键触发
        if(self.goodsGrid.GetNumberRows()>0):
            self.goodsGrid.DeleteRows(0, 1,True) 
        Id=self.m_textCtrl4.GetValue();
        sql="select id,barcode,name,mainunit,boxnum,saleprice,state,remark  from goods_info  where barcode= ? "
        result1=Utils.query(sql,(Id,))
        
        if(len(result1)==1):
            self.goodsGrid.AppendRows(numRows=1) 
            self.InsertNewGoods(0,result1[0])
            self.m_textCtrl4.Clear()
            return
        
        sql="select id,barcode,name,mainunit,boxnum,saleprice,state,remark  from goods_info  where id= ? "
        result2=Utils.query(sql,(Id,))
        
        if(len(result2)==1):
            self.goodsGrid.AppendRows(numRows=1) 
            self.InsertNewGoods(0,result2[0])
            self.m_textCtrl4.Clear()
            return 
        
        wx.MessageBox(u"                   未找到商品         ", u"提醒",wx.OK | wx.ICON_ASTERISK)
        self.m_textCtrl4.Clear()
        return
    
    
    
    
    
class SaleOrderPage ( wx.Panel ):
    
    def __init__( self, parent ):
        
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        PanelSizer = wx.BoxSizer( wx.VERTICAL )
        #输入查询,应收金额
        TollBarSizer = wx.BoxSizer( wx.HORIZONTAL )
        self.StaticTextQuery = wx.StaticText( self, wx.ID_ANY, u"输入销售单号", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.StaticTextQuery.Wrap( -1 )
        TollBarSizer.Add( self.StaticTextQuery, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT|wx.RIGHT, 15 )
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), wx.TE_PROCESS_ENTER,name="QueryText" )
        TollBarSizer.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL, 15 )
        self.m_textCtrl4.SetFocus()
        PanelSizer.Add( TollBarSizer, 5, 0, 5 )
        self.staticLine2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        PanelSizer.Add( self.staticLine2, 0, wx.EXPAND |wx.ALL, 5 )
        
        GridSizer = wx.BoxSizer( wx.VERTICAL )
        self.goodsGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        # Grid
        self.goodsGrid.CreateGrid( 0, 6 )
        self.goodsGrid.EnableEditing( False )
        self.goodsGrid.EnableGridLines( True )
        self.goodsGrid.EnableDragGridSize( True )
        self.goodsGrid.SetMargins( 0, 0 )
        self.goodsGrid.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.goodsGrid.SetWindowStyle(0)
        # Columns
        self.goodsGrid.SetColSize( 0, 200 )
        self.goodsGrid.SetColSize( 1, 75 )
        self.goodsGrid.SetColSize( 2, 75 )
        self.goodsGrid.SetColSize( 3, 75 )
        self.goodsGrid.SetColSize( 4, 75 )
        self.goodsGrid.SetColSize( 5, 100 )
        self.goodsGrid.EnableDragColMove( False )
        self.goodsGrid.EnableDragColSize( True )
        self.goodsGrid.SetColLabelSize( 25 )
        self.goodsGrid.SetColLabelValue( 0, u"销售单编号" )
        self.goodsGrid.SetColLabelValue( 1, u"客户编码" )
        self.goodsGrid.SetColLabelValue( 2, u"客户名称" )
        self.goodsGrid.SetColLabelValue( 3, u"销售金额" )
        self.goodsGrid.SetColLabelValue( 4, u"收银员名称" )
        self.goodsGrid.SetColLabelValue( 5, u"销售日期" )
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
        self.goodsGrid.Enable( True )
        self.goodsGrid.SetMinSize( wx.Size( 800,460 ) )
        GridSizer.Add( self.goodsGrid, 0, wx.ALL, 5 )
        PanelSizer.Add( GridSizer, 15, wx.BOTTOM|wx.EXPAND|wx.FIXED_MINSIZE, 10 )
        
        self.SetSizer( PanelSizer )
        self.Layout()
        
        
        #为输入框绑定键盘事件
        self.m_textCtrl4.Bind(wx.wx.EVT_KEY_DOWN,self.OnKeyDown)
        
        ##取消表格的所有点击事件,默认为选中第一条数据
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_SELECT_CELL,self.PreventEvent)
        
        # 取消表格的所有点击事件
        self.goodsGrid.Bind( wx.EVT_LEFT_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEFT_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MOTION, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEFT_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEAVE_WINDOW, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_ENTER_WINDOW, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MOUSEWHEEL, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_SET_FOCUS, self.PreventEvent )
        
        
    def PreventEvent(self,event): ##取消表格的所有点击事件,点击默认选中 输入查询这个框
         self.m_textCtrl4.SetFocus()
        
          
    def OnKeyDown(self, event):#快捷键
         keyCode=event.GetKeyCode()
         if(keyCode==13 or keyCode==370):
             self.QueryGoods()
         if(keyCode==27):
           self.GetParent().ClosesaleOrderQueryFrame(None)
         event.Skip()
         
       
    def InsertNewGoods(self,rowNum,data): #新增一行
        self.goodsGrid.SetCellValue(rowNum, 0,"%s" % data[0]) #销售单号
        self.goodsGrid.SetCellValue(rowNum, 1,"%s" % data[1]) # 客户id
        self.goodsGrid.SetCellValue(rowNum, 2,"%s" % data[2]) #客户名称
        self.goodsGrid.SetCellValue(rowNum, 3,"%s" % data[3]) #销售金额
        self.goodsGrid.SetCellValue(rowNum, 4,"%s" % data[4]) #收银员名称
        self.goodsGrid.SetCellValue(rowNum, 5,"%s" % data[5]) #销售日期
        
           
    def QueryGoods(self): #当输入销售单号,按回车键触发
        rowNum=self.goodsGrid.GetNumberRows();
        if(rowNum>0):
            self.goodsGrid.DeleteRows(0, rowNum,True) 
        Id=self.m_textCtrl4.GetValue();
        sql=""
        paramTuple = None
        if(Id==""):
            sql = "select id , customerid , customername , amout , salername , date  from sale_order where date  = ?  "
            paramTuple=(Utils.getDateStr(),)
        else :
            sql = "select id , customerid , customername , amout , salername , date  from sale_order where date  = ?  and id = ? "
            paramTuple=(Utils.getDateStr(),Id,)
            
        result=Utils.query(sql,paramTuple)
        if(len(result)==0):
            wx.MessageBox(u"                   未找到销售单         ", u"提醒",wx.OK | wx.ICON_ASTERISK)
            self.m_textCtrl4.SelectAll()
            return
        for i in range(0,len(result)):
            self.goodsGrid.AppendRows(numRows=1) 
            self.InsertNewGoods(i,result[i])
            self.m_textCtrl4.SelectAll()
        return    
    

class ReturnOrderPage ( wx.Panel ):
    
    def __init__( self, parent ):
        
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        PanelSizer = wx.BoxSizer( wx.VERTICAL )
        #输入查询,应收金额
        TollBarSizer = wx.BoxSizer( wx.HORIZONTAL )
        self.StaticTextQuery = wx.StaticText( self, wx.ID_ANY, u"输入退货单号", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.StaticTextQuery.Wrap( -1 )
        TollBarSizer.Add( self.StaticTextQuery, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT|wx.RIGHT, 15 )
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), wx.TE_PROCESS_ENTER,name="QueryText" )
        TollBarSizer.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL, 15 )
        self.m_textCtrl4.SetFocus()
        PanelSizer.Add( TollBarSizer, 5, 0, 5 )
        self.staticLine2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        PanelSizer.Add( self.staticLine2, 0, wx.EXPAND |wx.ALL, 5 )
        
        GridSizer = wx.BoxSizer( wx.VERTICAL )
        self.goodsGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        # Grid
        self.goodsGrid.CreateGrid( 0, 6 )
        self.goodsGrid.EnableEditing( False )
        self.goodsGrid.EnableGridLines( True )
        self.goodsGrid.EnableDragGridSize( True )
        self.goodsGrid.SetMargins( 0, 0 )
        self.goodsGrid.SetSelectionMode(wx.grid.Grid.SelectRows)
        self.goodsGrid.SetWindowStyle(0)
        # Columns
        self.goodsGrid.SetColSize( 0, 200 )
        self.goodsGrid.SetColSize( 1, 75 )
        self.goodsGrid.SetColSize( 2, 75 )
        self.goodsGrid.SetColSize( 3, 75 )
        self.goodsGrid.SetColSize( 4, 75 )
        self.goodsGrid.SetColSize( 5, 100 )
        self.goodsGrid.EnableDragColMove( False )
        self.goodsGrid.EnableDragColSize( True )
        self.goodsGrid.SetColLabelSize( 25 )
        self.goodsGrid.SetColLabelValue( 0, u"退货单编号" )
        self.goodsGrid.SetColLabelValue( 1, u"客户编码" )
        self.goodsGrid.SetColLabelValue( 2, u"客户名称" )
        self.goodsGrid.SetColLabelValue( 3, u"退货金额" )
        self.goodsGrid.SetColLabelValue( 4, u"收银员名称" )
        self.goodsGrid.SetColLabelValue( 5, u"退货日期" )
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
        self.goodsGrid.Enable( True )
        self.goodsGrid.SetMinSize( wx.Size( 800,460 ) )
        GridSizer.Add( self.goodsGrid, 0, wx.ALL, 5 )
        PanelSizer.Add( GridSizer, 15, wx.BOTTOM|wx.EXPAND|wx.FIXED_MINSIZE, 10 )
        
        self.SetSizer( PanelSizer )
        self.Layout()
        
        
        #为输入框绑定键盘事件
        self.m_textCtrl4.Bind(wx.wx.EVT_KEY_DOWN,self.OnKeyDown)
        
        ##取消表格的所有点击事件,默认为选中第一条数据
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_CLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_DCLICK,self.PreventEvent)
        self.goodsGrid.Bind(wx.grid.EVT_GRID_SELECT_CELL,self.PreventEvent)
        
        # 取消表格的所有点击事件
        self.goodsGrid.Bind( wx.EVT_LEFT_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEFT_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_DOWN, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_UP, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MOTION, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEFT_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MIDDLE_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_RIGHT_DCLICK, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_LEAVE_WINDOW, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_ENTER_WINDOW, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_MOUSEWHEEL, self.PreventEvent )
        self.goodsGrid.Bind( wx.EVT_SET_FOCUS, self.PreventEvent )
        
    def PreventEvent(self,event): ##取消表格的所有点击事件,点击默认选中 输入查询这个框
         self.m_textCtrl4.SetFocus()
        
          
    def OnKeyDown(self, event):#快捷键
         keyCode=event.GetKeyCode()
         if(keyCode==13 or keyCode==370):
             self.QueryGoods()
         if(keyCode==27):
           self.GetParent().ClosereturnOrderQueryFrame(None)
         event.Skip()
         
       
    def InsertNewGoods(self,rowNum,data): #新增一行
        self.goodsGrid.SetCellValue(rowNum, 0,"%s" % data[0]) #销售单号
        self.goodsGrid.SetCellValue(rowNum, 1,"%s" % data[1]) # 客户id
        self.goodsGrid.SetCellValue(rowNum, 2,"%s" % data[2]) #客户名称
        self.goodsGrid.SetCellValue(rowNum, 3,"%s" % data[3]) #销售金额
        self.goodsGrid.SetCellValue(rowNum, 4,"%s" % data[4]) #收银员名称
        self.goodsGrid.SetCellValue(rowNum, 5,"%s" % data[5]) #销售日期

           
    def QueryGoods(self): #当输入销售单号,按回车键触发
        rowNum=self.goodsGrid.GetNumberRows()
        if(rowNum>0):
            self.goodsGrid.DeleteRows(0, rowNum,True) 
        Id=self.m_textCtrl4.GetValue();
        sql=""
        paramTuple = None
        if(Id==""):
            sql = "select id , customerid , customername , realreturn , salername , date  from return_order where date  = ?  "
            paramTuple=(Utils.getDateStr(),)
        else :
            sql = "select id , customerid , customername , realreturn , salername , date  from return_order where date  = ?  and id = ? "
            paramTuple=(Utils.getDateStr(),Id,)
            
        result=Utils.query(sql,paramTuple)
        if(len(result)==0):
            wx.MessageBox(u"                   未找到退货单        ", u"提醒",wx.OK | wx.ICON_ASTERISK)
            self.m_textCtrl4.SelectAll()
            return
        for i in range(0,len(result)):
            self.goodsGrid.AppendRows(numRows=1) 
            self.InsertNewGoods(i,result[i])
            self.m_textCtrl4.SelectAll()
        return    
    

class printConfigPage ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.TAB_TRAVERSAL )
        
        sql="select head1,head2,foot1,foot2 from config_print"
        self.configVal=Utils.query(sql,None)
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"头部1", wx.DefaultPosition, wx.DefaultSize, 0 )
        
        self.m_staticText1.Wrap( -1 )
        bSizer3.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.LEFT, 80 )
        
        self.head1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,  wx.TE_PROCESS_ENTER ,name="printco1")
        self.head1.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.head1 : self.TextCtrlKeyDown(evt,self.head1))
        self.head1.SetValue(self.configVal[0][0])
        self.head1.SetMinSize( wx.Size( 300,-1 ) )
        
        bSizer3.Add( self.head1, 0, wx.ALIGN_CENTER|wx.LEFT, 35 )
        
        
        bSizer2.Add( bSizer3, 2, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"头部2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.LEFT, 80 )
        
        self.head2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER ,name="printco2")
        self.head2.SetMinSize( wx.Size( 300,-1 ) )
        self.head2.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.head2 : self.TextCtrlKeyDown(evt,self.head2))
        self.head2.SetValue(self.configVal[0][1])
        
        bSizer4.Add( self.head2, 0, wx.ALIGN_CENTER|wx.LEFT, 35 )
        
        
        bSizer2.Add( bSizer4, 2, wx.EXPAND, 5 )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"底部1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer5.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.LEFT, 80 )
        
        self.foot1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER ,name="printco3")
        self.foot1.SetMinSize( wx.Size( 300,-1 ) )
        self.foot1.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.foot1 : self.TextCtrlKeyDown(evt,self.foot1))
        self.foot1.SetValue(self.configVal[0][2])
        
        bSizer5.Add( self.foot1, 0, wx.ALIGN_CENTER|wx.LEFT, 35 )
        
        
        bSizer2.Add( bSizer5, 2, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"底部2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer6.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.LEFT, 80 )
        
        self.foot2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER ,name="printco4")
        self.foot2.SetMinSize( wx.Size( 300,-1 ) )
        self.foot2.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self.foot2 : self.TextCtrlKeyDown(evt,self.foot2))
        self.foot2.SetValue(self.configVal[0][3])
        bSizer6.Add( self.foot2, 0, wx.ALIGN_CENTER|wx.LEFT, 35 )
        bSizer2.Add( bSizer6, 2, wx.EXPAND, 5 )
        bSizer7 = wx.BoxSizer( wx.VERTICAL )
        self.saveBtn = wx.Button( self, wx.ID_ANY, u"保存[Enter]", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.saveBtn.Bind(wx.EVT_BUTTON, self.saveConfig, self.saveBtn) 
        
        
        bSizer7.Add( self.saveBtn, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
        
        self.Bind(wx.EVT_KEY_DOWN, lambda evt, target=self : self.TextCtrlKeyDown(evt,self))
        bSizer2.Add( bSizer7, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer2 )
        self.Layout()
    def saveConfig(self,event):
        sql="update config_print set head1 = ? ,head2 = ? ,foot1 = ? ,foot2 = ? where id =1"
        Utils.commit(sql,(self.head1.GetValue(),self.head2.GetValue(),self.foot1.GetValue(),self.foot2.GetValue(),))
        wx.MessageBox(u"                  保存成功        ", u"提醒",wx.OK | wx.ICON_ASTERISK)
        self.GetParent().closeprintConfigFrame(None)
    
    
    def TextCtrlKeyDown(self,event,target):
        keyCode=event.GetKeyCode()

        if(keyCode==317):    #向下箭头的快捷键
            name=target.GetName()
            intVal=int(name[7:len(name)])
            if(intVal < 4):
                nameVal=unicode(int(name[7:len(name)])+1)
                selectTarget=wx.FindWindowByName(u"printco"+nameVal)
                selectTarget.SetFocus()
                selectTarget.SelectAll()
            else : #最后一个按钮 向下箭头
                selectTarget=wx.FindWindowByName(u"printco1")
                selectTarget.SetFocus()
                selectTarget.SelectAll()
            return    
        if(keyCode==315):   #向上箭头的快捷键
            name=target.GetName()
            intVal=int(name[7:len(name)])
            if(intVal < 2): #第一个按钮向上箭头
                selectTarget=wx.FindWindowByName("printco4")
                selectTarget.SetFocus()
                selectTarget.SelectAll()
            else :  
                nameVal=unicode(int(name[7:len(name)])-1)
                selectTarget=wx.FindWindowByName(u"printco"+nameVal)
                selectTarget.SetFocus()
                selectTarget.SelectAll()
            return
        if(keyCode==13 or keyCode==370):
            self.saveConfig(None)
        event.Skip()     
            
            
            
            
            
            
            
            
            
            