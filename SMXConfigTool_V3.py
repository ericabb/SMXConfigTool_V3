# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"SMX202 机械特性监测模块配置工具 V3"), pos = wx.DefaultPosition, size = wx.Size( 503,841 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer17 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"header.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_bitmap1, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )


        bSizer1.Add( bSizer17, 0, 0, 5 )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL )
        self.m_toolBar1.SetToolBitmapSize( wx.Size( 10,10 ) )
        self.m_toolBar1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        self.m_tool4 = self.m_toolBar1.AddTool( wx.ID_ANY, _(u"tool"), wx.Bitmap( u"res/link.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, _(u"连接设备"), wx.EmptyString, None )

        self.m_tool9 = self.m_toolBar1.AddTool( wx.ID_ANY, _(u"tool"), wx.Bitmap( u"res/unlink.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, _(u"断开设备"), wx.EmptyString, None )

        self.m_toolBar1.AddSeparator()

        self.m_tool5 = self.m_toolBar1.AddTool( wx.ID_ANY, _(u"tool"), wx.Bitmap( u"res/upload.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, _(u"读取参数"), _(u"从SMX202读取设备参数"), None )

        self.m_tool3 = self.m_toolBar1.AddTool( wx.ID_ANY, _(u"tool"), wx.Bitmap( u"res/download.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, _(u"配置参数"), wx.EmptyString, None )

        self.m_toolBar1.AddSeparator()

        self.m_tool6 = self.m_toolBar1.AddTool( wx.ID_ANY, _(u"tool"), wx.Bitmap( u"res/target-two.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, _(u"标定阈值"), wx.EmptyString, None )

        self.m_tool7 = self.m_toolBar1.AddTool( wx.ID_ANY, _(u"tool"), wx.Bitmap( u"res/curve-adjustment.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, _(u"读取波形"), wx.EmptyString, None )

        self.m_toolBar1.AddSeparator()

        self.m_tool8 = self.m_toolBar1.AddTool( wx.ID_ANY, _(u"tool"), wx.Bitmap( u"res/upload-laptop.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, _(u"升级固件"), wx.EmptyString, None )

        self.m_toolBar1.Realize()

        bSizer4.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )


        bSizer1.Add( bSizer4, 0, 0, 5 )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"通讯") ), wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText612 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"通讯串口"), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText612.Wrap( -1 )

        bSizer2.Add( self.m_staticText612, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        m_choice1Choices = []
        self.m_choice1 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        self.m_choice1.SetToolTip( _(u"选择通讯串口") )

        bSizer2.Add( self.m_choice1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_checkBox1 = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"高速模式"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox1.SetToolTip( _(u"修改通讯波特率为115200") )

        bSizer2.Add( self.m_checkBox1, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )


        sbSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


        bSizer1.Add( sbSizer1, 0, wx.EXPAND, 5 )

        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"设备参数") ), wx.HORIZONTAL )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        bSizerUnitNum = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticTextUnitNum = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"单元位置"), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticTextUnitNum.Wrap( -1 )

        bSizerUnitNum.Add( self.m_staticTextUnitNum, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        m_choiceUnitNumChoices = [ wx.EmptyString, _(u"单元1(97)"), _(u"单元2(98)"), _(u"单元3(99)"), _(u"单元4(100)"), _(u"单元5(101)"), _(u"单元6(102)"), _(u"单元7(103)"), _(u"单元8(104)"), _(u"单元9(105)"), _(u"单元10(106)"), _(u"单元11(107)"), _(u"单元12(108)") ]
        self.m_choiceUnitNum = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,-1 ), m_choiceUnitNumChoices, 0 )
        self.m_choiceUnitNum.SetSelection( 0 )
        self.m_choiceUnitNum.SetToolTip( _(u"选择/设置监测模块安装单元") )

        bSizerUnitNum.Add( self.m_choiceUnitNum, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer12.Add( bSizerUnitNum, 0, wx.EXPAND, 5 )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText61 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"开关柜序列号"), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText61.Wrap( -1 )

        bSizer15.Add( self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        bSizer15.Add( self.m_textCtrl1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer12.Add( bSizer15, 1, wx.EXPAND, 5 )

        bSizer151 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText611 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"监测模块序列号"), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText611.Wrap( -1 )

        bSizer151.Add( self.m_staticText611, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl11 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        bSizer151.Add( self.m_textCtrl11, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer12.Add( bSizer151, 1, wx.EXPAND, 5 )


        sbSizer2.Add( bSizer12, 0, wx.EXPAND, 5 )

        bSizer19 = wx.BoxSizer( wx.VERTICAL )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"开关类型"), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer5.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

        m_choice2Choices = [ _(u"SafeRing/SafePlus 12kV"), _(u"SafeRing/SafePlus 24kV"), _(u"SafeRing/SafePlus Air 12kV"), _(u"SafeRing/SafePlus Air 24kV*"), _(u"SafeRing/SafePlus 40.5kV"), _(u"SafeRing/SafePlus XT"), _(u"SafeRing/SafePlus Air SGCC") ]
        self.m_choice2 = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 180,-1 ), m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        bSizer5.Add( self.m_choice2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer19.Add( bSizer5, 0, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"单元类型"), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer6.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

        m_choice3Choices = [ _(u"C"), _(u"F"), _(u"V"), _(u"V25") ]
        self.m_choice3 = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 180,-1 ), m_choice3Choices, 0 )
        self.m_choice3.SetSelection( 0 )
        bSizer6.Add( self.m_choice3, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer19.Add( bSizer6, 0, wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"额定电压"), wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer10.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

        m_choice4Choices = [ _(u"AC220"), _(u"DC220"), _(u"AC110"), _(u"DC110"), _(u"DC60"), _(u"DC48"), _(u"DC30"), _(u"DC24") ]
        self.m_choice4 = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 180,-1 ), m_choice4Choices, 0 )
        self.m_choice4.SetSelection( 0 )
        bSizer10.Add( self.m_choice4, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer19.Add( bSizer10, 0, wx.EXPAND, 5 )


        sbSizer2.Add( bSizer19, 1, wx.EXPAND, 5 )


        bSizer1.Add( sbSizer2, 0, wx.EXPAND, 5 )

        sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"固件升级") ), wx.VERTICAL )

        self.m_filePicker1 = wx.FilePickerCtrl( sbSizer61.GetStaticBox(), wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        self.m_filePicker1.SetMinSize( wx.Size( 450,-1 ) )

        sbSizer61.Add( self.m_filePicker1, 0, wx.ALL, 5 )

        self.m_gauge1 = wx.Gauge( sbSizer61.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge1.SetValue( 0 )
        self.m_gauge1.Hide()
        self.m_gauge1.SetMinSize( wx.Size( 400,-1 ) )

        sbSizer61.Add( self.m_gauge1, 0, wx.ALL|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5 )


        bSizer1.Add( sbSizer61, 0, wx.EXPAND, 5 )

        bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

        sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"开关位置") ), wx.VERTICAL )

        sbSizer7.SetMinSize( wx.Size( 174,-1 ) )
        self.m_staticTextPosition = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, _(u"未知"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticTextPosition.Wrap( -1 )

        self.m_staticTextPosition.SetFont( wx.Font( 22, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )

        sbSizer7.Add( self.m_staticTextPosition, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer37.Add( sbSizer7, 0, wx.EXPAND, 5 )

        sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"测量参量") ), wx.VERTICAL )

        self.m_grid1 = wx.grid.Grid( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid1.CreateGrid( 4, 2 )
        self.m_grid1.EnableEditing( False )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.SetColSize( 0, 100 )
        self.m_grid1.SetColSize( 1, 100 )
        self.m_grid1.EnableDragColMove( False )
        self.m_grid1.EnableDragColSize( True )
        self.m_grid1.SetColLabelValue( 0, _(u"实时测量值") )
        self.m_grid1.SetColLabelValue( 1, _(u"动作次数") )
        self.m_grid1.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
        self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid1.SetRowSize( 0, 16 )
        self.m_grid1.SetRowSize( 1, 16 )
        self.m_grid1.SetRowSize( 2, 16 )
        self.m_grid1.SetRowSize( 3, 16 )
        self.m_grid1.EnableDragRowSize( True )
        self.m_grid1.SetRowLabelValue( 0, _(u"分闸线圈 O (A)") )
        self.m_grid1.SetRowLabelValue( 1, _(u"合闸线圈 C (A)") )
        self.m_grid1.SetRowLabelValue( 2, _(u"储能电机 M (A)") )
        self.m_grid1.SetRowLabelValue( 3, _(u"角度位移 T (°)") )
        self.m_grid1.SetRowLabelSize( wx.grid.GRID_AUTOSIZE )
        self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance
        self.m_grid1.SetLabelFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

        # Cell Defaults
        self.m_grid1.SetDefaultCellFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
        sbSizer5.Add( self.m_grid1, 0, 0, 5 )


        bSizer37.Add( sbSizer5, 0, wx.EXPAND, 5 )


        bSizer1.Add( bSizer37, 0, 0, 5 )

        sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"计算参量") ), wx.VERTICAL )

        self.m_grid2 = wx.grid.Grid( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid2.CreateGrid( 12, 6 )
        self.m_grid2.EnableEditing( True )
        self.m_grid2.EnableGridLines( True )
        self.m_grid2.EnableDragGridSize( False )
        self.m_grid2.SetMargins( 0, 0 )

        # Columns
        self.m_grid2.SetColSize( 0, 60 )
        self.m_grid2.SetColSize( 1, 50 )
        self.m_grid2.SetColSize( 2, 50 )
        self.m_grid2.SetColSize( 3, 100 )
        self.m_grid2.SetColSize( 4, 50 )
        self.m_grid2.SetColSize( 5, 50 )
        self.m_grid2.EnableDragColMove( False )
        self.m_grid2.EnableDragColSize( True )
        self.m_grid2.SetColLabelValue( 0, _(u"最新数据") )
        self.m_grid2.SetColLabelValue( 1, _(u"报警低") )
        self.m_grid2.SetColLabelValue( 2, _(u"预警低") )
        self.m_grid2.SetColLabelValue( 3, _(u"基准值") )
        self.m_grid2.SetColLabelValue( 4, _(u"预警高") )
        self.m_grid2.SetColLabelValue( 5, _(u"报警高") )
        self.m_grid2.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
        self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid2.SetRowSize( 0, 16 )
        self.m_grid2.SetRowSize( 1, 16 )
        self.m_grid2.SetRowSize( 2, 16 )
        self.m_grid2.SetRowSize( 3, 16 )
        self.m_grid2.SetRowSize( 4, 16 )
        self.m_grid2.SetRowSize( 5, 16 )
        self.m_grid2.SetRowSize( 6, 16 )
        self.m_grid2.SetRowSize( 7, 16 )
        self.m_grid2.SetRowSize( 8, 16 )
        self.m_grid2.SetRowSize( 9, 16 )
        self.m_grid2.SetRowSize( 10, 16 )
        self.m_grid2.SetRowSize( 11, 16 )
        self.m_grid2.EnableDragRowSize( True )
        self.m_grid2.SetRowLabelValue( 0, _(u"储能电流 (A)") )
        self.m_grid2.SetRowLabelValue( 1, _(u"储能时间 (s)") )
        self.m_grid2.SetRowLabelValue( 2, _(u"行程 (°)") )
        self.m_grid2.SetRowLabelValue( 3, _(u"分闸线圈电流 (A)") )
        self.m_grid2.SetRowLabelValue( 4, _(u"分闸时间 (ms)") )
        self.m_grid2.SetRowLabelValue( 5, _(u"分闸速度 (°/ms)") )
        self.m_grid2.SetRowLabelValue( 6, _(u"分闸过冲 (°)") )
        self.m_grid2.SetRowLabelValue( 7, _(u"分闸反弹 (°)") )
        self.m_grid2.SetRowLabelValue( 8, _(u"合闸线圈电流 (A)") )
        self.m_grid2.SetRowLabelValue( 9, _(u"合闸时间 (ms)") )
        self.m_grid2.SetRowLabelValue( 10, _(u"合闸速度 (°/ms)") )
        self.m_grid2.SetRowLabelValue( 11, _(u"合闸过冲 (°)") )
        self.m_grid2.SetRowLabelSize( wx.grid.GRID_AUTOSIZE )
        self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance
        self.m_grid2.SetLabelFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

        # Cell Defaults
        self.m_grid2.SetDefaultCellFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
        self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
        self.m_grid2.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
        self.m_grid2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        sbSizer6.Add( self.m_grid2, 0, wx.EXPAND, 5 )


        bSizer1.Add( sbSizer6, 1, 0, 5 )

        bSizer152 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"footer.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer152.Add( self.m_bitmap2, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer152, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar( 4, wx.STB_DEFAULT_STYLE, wx.ID_ANY )
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menubar1.Hide()

        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"打开"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem1 )

        self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, _(u"退出"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem2 )

        self.m_menubar1.Append( self.m_menu1, _(u"文件") )

        self.m_menu2 = wx.Menu()
        self.m_menubar1.Append( self.m_menu2, _(u"配置") )

        self.m_menu3 = wx.Menu()
        self.m_menubar1.Append( self.m_menu3, _(u"关于") )

        self.SetMenuBar( self.m_menubar1 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_TOOL, self.on_connect_click, id = self.m_tool4.GetId() )
        self.Bind( wx.EVT_TOOL, self.on_disconnect_click, id = self.m_tool9.GetId() )
        self.Bind( wx.EVT_TOOL, self.read_configuration, id = self.m_tool5.GetId() )
        self.Bind( wx.EVT_TOOL, self.write_configuration, id = self.m_tool3.GetId() )
        self.Bind( wx.EVT_TOOL, self.on_open_fwupdate, id = self.m_tool8.GetId() )
        self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.on_check_highspeed )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_connect_click( self, event ):
        event.Skip()

    def on_disconnect_click( self, event ):
        event.Skip()

    def read_configuration( self, event ):
        event.Skip()

    def write_configuration( self, event ):
        event.Skip()

    def on_open_fwupdate( self, event ):
        event.Skip()

    def on_check_highspeed( self, event ):
        event.Skip()


###########################################################################
## Class FirmwareUpdate
###########################################################################

class FirmwareUpdate ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"固件升级"), pos = wx.DefaultPosition, size = wx.Size( 428,125 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


