# -*- coding: utf-8 -*-
import wx
from SMXConfigTool_V3 import MainFrame
from SMXConfigTool_V3 import FirmwareUpdate

import serial
import serial.tools.list_ports

from modbus_tk import modbus_rtu
import modbus_tk.defines as cst

import time
from time import sleep

import threading

from ymodem import YMODEM
import os

   
class MFrame(MainFrame):
    def __init__(self, parent):
        MainFrame.__init__(self, parent)
        self.__set_properties()
    
    def __set_properties(self):
        """
        Set default properties of controls
        """
        ## global vars
        self.master = None
        self.slave_addr = None
        # self.ser = None
        self.ser_status = 0
        self.ser_busy = 0
        self.fault_heartbeat_count = 0

        ## status bar
        self.reset_stutas_bar()

        ## serial port settings
        self.ser = serial.Serial()
        preferred_index = 0
        self.m_choice1.Clear()
        self.ports = []
        for n, (portname, desc, hwid) in enumerate(sorted(serial.tools.list_ports.comports())):
            self.m_choice1.Append(u'{} - {}'.format(portname, desc))
            self.ports.append(portname)
            if self.ser.name == portname:
                preferred_index = n
        self.m_choice1.SetSelection(preferred_index)

        for i in range(12):
            for j in [1, 5]:
                self.m_grid2.SetCellBackgroundColour(i, j, "PINK")   
            for j in [2, 4]:
                self.m_grid2.SetCellBackgroundColour(i, j, "YELLOW")
            for j in [3]:
                self.m_grid2.SetCellBackgroundColour(i, j, "AQUAMARINE")             

        self.heartbeat_thread = threading.Thread(target=self.on_heartbeat)
        self.check_parameters_thread = threading.Thread(target=self.check_parameters)

    def show_message(self, msg=u'消息'):
        """
        Print a message in an pop-up window
        """
        dlg = wx.MessageDialog(None, msg, u'消息', wx.OK)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Close(True)
        else:
            dlg.Close(True)
        dlg.Destroy()
    
    def show_status(self, msg):
        """
        Print a message at status bar
        """
        self.m_statusBar1.SetStatusText(msg, 0)
        sleep(0.05)

    def reset_stutas_bar(self):
        """
        Reset stutas bar to default values
        """
        self.m_statusBar1.SetStatusWidths([-1,120,120,40])
        self.m_statusBar1.SetStatusText(u"设备未连接...", 1)    
        self.m_statusBar1.SetStatusText(u"00-00-00 00:00:00", 2)
        self.m_statusBar1.SetStatusText(u"Vn.n.nn", 3)

    def update_stutas_bar(self):
        if (self.heartbeat_thread.is_alive()):
            self.m_statusBar1.SetStatusText(u"{}-{}-{}-{}-{}-{}".format(self.slave_addr,
                                                                        self.ser.baudrate,
                                                                        self.ser.bytesize,
                                                                        self.ser.parity,
                                                                        self.ser.stopbits,
                                                                        self.ser.xonxoff), 1)
            self.show_status(u"设备连接正常")

            ## do some routine work
            self.check_fw_version()
            self.update_time()
        pass

    def on_connect_click(self, event):
        self.connect_thread = threading.Thread(target=self.connect_com)
        self.connect_thread.start()
        # self.connect_com()
        return super().on_connect_click(event)

    def on_disconnect_click(self, event):
        ## resume baudrate to 9600
        if self.heartbeat_thread.is_alive():
            if self.ser.baudrate != 9600:
                self.change_slave_baudrate(9600)
        self.disconnect_thread = threading.Thread(target=self.disconnect_com)
        self.disconnect_thread.start()
        return super().on_disconnect_click(event)
    
    def connect_com(self):
        """
        * call back function of "connnect" button click
        * Connect to SMX202 via selected serial port
        * Disconnect SMX202 if it is connected
        """
        # possible slave addresses
        self.slaves = [999, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]
        # possible slave baudrate
        baudrates = [9600, 115200]
        
        self.PORT = self.ports[self.m_choice1.GetSelection()]
        self.slave_addr = self.slaves[self.m_choiceUnitNum.GetSelection()]

        try:            
            for i in range(2): 
                ## try all possible baudrate: 9600/115200
                try: 
                    if self.ser.is_open:
                        self.ser.close()
                    self.ser = serial.Serial(port=self.PORT, baudrate=baudrates[i], bytesize=8, parity='N', stopbits=1, xonxoff=0)
                    self.master = modbus_rtu.RtuMaster(self.ser)
                    self.master.set_timeout(0.1)
                    self.master.set_verbose(True)
                    self.show_status(u"串口打开正常")

                    if self.slave_addr != 999:
                        ## unit is selected
                        try:
                            self.master.execute(self.slave_addr, cst.READ_HOLDING_REGISTERS, 0, 1)
                        except:
                            self.show_status(u"连接从机{}波特率{}异常".format(self.slave_addr,baudrates[i]))
                        else:
                            if not(self.heartbeat_thread.is_alive()):
                                self.heartbeat_thread = threading.Thread(target=self.on_heartbeat)
                                self.heartbeat_thread.start()
                                self.show_status(u"心跳进程启动正常")
                    else:
                        ## no unit is selected, then search
                        for j in range(1, 13):                                
                            try:                                
                                self.show_status(u"尝试连接从机{}波特率{}".format(self.slaves[j],baudrates[i]))
                                self.master.execute(self.slaves[j], cst.READ_HOLDING_REGISTERS, 0, 1)
                            except:
                                pass
                            else:
                                self.slave_addr = self.slaves[j]
                                # start heart beat
                                if not(self.heartbeat_thread.is_alive()):
                                    self.heartbeat_thread = threading.Thread(target=self.on_heartbeat)
                                    self.heartbeat_thread.start()
                                    self.show_status(u"心跳进程启动正常")
                                    self.m_choiceUnitNum.SetSelection(j)
                                    break
                                
                    self.update_stutas_bar()
                    if (self.heartbeat_thread.is_alive()):
                        self.set_current_zero()

                        ## auto change baudrate to 115200
                        if (self.ser.baudrate != 115200) and (self.ser.is_open) and (self.m_checkBox1.IsChecked()):
                            self.change_slave_baudrate(115200)
                        break
                    elif i == 1:
                        self.disconnect_com()
                        self.show_message(u"请确认串口和从机地址选择正确")
                except Exception as err:
                    pass
                    # self.show_message(u'设备连接异常:{}'.format(err))
        except Exception as err:
            self.show_message(u'设备连接异常:{}'.format(err))
            self.disconnect_com()
    
    def disconnect_com(self):
        """
        * Disconnect SMX202 on request or when time out
        """
        self.show_status(u"尝试断开设备连接")
        try:
            if self.master._is_opened:
                self.master.close()
            if self.ser.is_open:
                self.ser.close()
            self.show_status(u"串口关闭正常")

            self.reset_stutas_bar()
            
            if self.heartbeat_thread.is_alive():
                self.heartbeat_thread.join(1.0)
            
            if self.check_parameters_thread.is_alive():
                self.check_parameters_thread.join(1.0)
        except Exception as err:
            self.show_status(u"尝试断开设备连接错误:{}".format(err))
    
    def on_heartbeat(self):
        """
        * Check the connectivity of SMX202 every second and update its status
        """
        flag = False
        while (self.ser.is_open) and (self.master._is_opened):
            # while self.ser_busy:
            #     sleep(1)
            try:                
                self.master.execute(self.slave_addr, cst.READ_HOLDING_REGISTERS, 0, 1)
                # if flag:
                #     self.m_toggleBtn1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
                # else:
                #     self.m_toggleBtn1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
                self.fault_heartbeat_count = 0
            except Exception as err:
                self.fault_heartbeat_count += 1
                if self.fault_heartbeat_count > 3:
                    self.show_status(u'心跳进程异常:{}'.format(err))
                    self.disconnect_com()
            finally:
                flag = not(flag)
                sleep(1)
    
    def check_fw_version(self):
        """
        Check the firmware version of SMX202
        """
        if self.ser.is_open:
            self.show_status(u"检查设备固件版本")
            self.ser_busy = 1
            try:
                version_tuple = self.master.execute(self.slave_addr, cst.READ_HOLDING_REGISTERS, 2, 1)
                version_num = int(version_tuple[0])
                main_version = (version_num >> 12) % 16
                sub_version = (version_num >> 8) % 16
                build_version = ((version_num >> 4) % 16) * 10 + version_num % 16
                sleep(0.2)
                self.m_statusBar1.SetStatusText(u"V{}.{}.{:0>2d}".format(main_version, sub_version, build_version), 3)
            except Exception as err:
                self.show_status(u'检查固件版本错误:{}'.format(err))
                # raise err
            finally:
                self.ser_busy = 0
    
    def change_slave_baudrate(self, newbaudrate):
        """
        Change the baudrate of serial port 9600/115200
        """
        self.show_status(u"尝试修改设备波特率为 {}".format(newbaudrate))
        self.ser_busy = 1
        # change baudrate of SMX202 and wait for reboot
        try:
            self.master.execute(self.slave_addr, cst.WRITE_SINGLE_REGISTER, 4, output_value=int(newbaudrate/1200))
        except:         
            pass
        finally:
            self.show_status(u"修改设备波特率指令已发送")
            sleep(3)
            try:
                self.show_status(u"尝试重新连接设备")
                self.master.close()
                if self.ser.is_open:
                    self.ser.close()
                if not(self.ser.is_open):
                    self.ser = serial.Serial(port=self.PORT, baudrate=newbaudrate, bytesize=8, parity='N', stopbits=1, xonxoff=0)
                    self.master = modbus_rtu.RtuMaster(self.ser)
                    self.master.set_timeout(0.1)
                    self.master.set_verbose(True)
                    self.master.execute(self.slave_addr, cst.READ_HOLDING_REGISTERS, 0, 1)
                    
                    # if not(self.heartbeat_thread.is_alive()):
                    #     self.heartbeat_thread = threading.Thread(target=self.on_heartbeat)
                    #     self.heartbeat_thread.start()
                    #     self.show_status(u"心跳进程启动正常")
                    
                    if (self.heartbeat_thread.is_alive()):
                        self.m_statusBar1.SetStatusText(u"{}-{}-{}-{}-{}-{}".format(self.slave_addr,
                                                                                    self.ser.baudrate,
                                                                                    self.ser.bytesize,
                                                                                    self.ser.parity,
                                                                                    self.ser.stopbits,
                                                                                    self.ser.xonxoff), 1)
                        self.show_status(u"设备连接正常")
            except Exception as err:
                self.show_status(u'设备重新连接异常:{}'.format(err))
                self.disconnect_com()
            self.ser_busy = 0

    def update_time(self):
        """
        Update SMX202 time per PC time
        """
        if self.ser.is_open:
            self.show_status(u"更新设备时间")
            self.ser_busy = 1
            localtime = time.localtime(time.time())
            # self.m_textCtrl4.SetValue(u"{:02d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour,localtime.tm_min, localtime.tm_sec))       
            try:
                self.master.execute(self.slave_addr, cst.WRITE_MULTIPLE_REGISTERS, 100, 6,
                                    output_value=[localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour, localtime.tm_min, localtime.tm_sec])
                sleep(0.5)
                time_tuple = self.master.execute(self.slave_addr, cst.READ_HOLDING_REGISTERS, 100, 6)
                sleep(0.1)
                year = int(time_tuple[0])
                month = int(time_tuple[1])
                day = int(time_tuple[2])
                hour = int(time_tuple[3])
                minute = int(time_tuple[4])
                second = int(time_tuple[5])
                time_string = u"{:02d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(year, month, day, hour, minute, second)
                self.m_statusBar1.SetStatusText(time_string, 2)
                self.show_status(u"时间同步正常")
            except Exception as err:
                self.m_statusBar1.SetStatusText("00-00-00 00:00:00", 2)
                self.show_status(u"时间同步错误:{}".format(err))
                # raise err
            finally:
                self.ser_busy = 0

    # def read_configuration(self):
    #     self.m_choiceUnitNum.SetSelection(int(self.slave_addr - 97))
    #     pass

    def read_configuration(self, event):
        if self.heartbeat_thread.is_alive():
            try:            
                self.m_choiceUnitNum.SetSelection(int(self.slave_addr - 96)) ## unit number
                config_tuple = self.master.execute(self.slave_addr, cst.READ_HOLDING_REGISTERS, 200, 3)
                # self.show_message(config_tuple)
                self.m_choice2.SetSelection(int(config_tuple[0])) ## swg type
                self.m_choice3.SetSelection(int(config_tuple[1])) ## unit type
                self.m_choice4.SetSelection(int(config_tuple[2])) ## secondary voltage
                self.show_status(u"设备配置读取正常")

                value_tuple = self.master.execute(self.slave_addr, cst.READ_INPUT_REGISTERS, 100, 12)
                sleep(0.2)                
                self.m_grid2.SetCellValue([0, 0], str(value_tuple[1] / 100.0))
                self.m_grid2.SetCellValue([1, 0], str(value_tuple[0] / 10.0))
                self.m_grid2.SetCellValue([2, 0], str(value_tuple[4] / 100.0))
                self.m_grid2.SetCellValue([3, 0], str(value_tuple[3] / 100.0))
                self.m_grid2.SetCellValue([4, 0], str(value_tuple[8] / 10.0))
                self.m_grid2.SetCellValue([5, 0], str(value_tuple[9] / 100.0))
                self.m_grid2.SetCellValue([6, 0], str(value_tuple[11] / 100.0))
                self.m_grid2.SetCellValue([7, 0], str(value_tuple[10] / 100.0))
                self.m_grid2.SetCellValue([8, 0], str(value_tuple[2] / 100.0))
                self.m_grid2.SetCellValue([9, 0], str(value_tuple[5] / 10.0))
                self.m_grid2.SetCellValue([10, 0], str(value_tuple[6] / 100.0))
                self.m_grid2.SetCellValue([11, 0], str(value_tuple[7] / 100.0)) 

                value_tuple = self.master.execute(self.slave_addr, cst.READ_INPUT_REGISTERS, 150, 12)
                sleep(0.2)                
                self.m_grid2.SetCellValue([0, 3], str(value_tuple[1] / 100.0))
                self.m_grid2.SetCellValue([1, 3], str(value_tuple[0] / 10.0))
                self.m_grid2.SetCellValue([2, 3], str(value_tuple[4] / 100.0))
                self.m_grid2.SetCellValue([3, 3], str(value_tuple[3] / 100.0))
                self.m_grid2.SetCellValue([4, 3], str(value_tuple[8] / 10.0))
                self.m_grid2.SetCellValue([5, 3], str(value_tuple[9] / 100.0))
                self.m_grid2.SetCellValue([6, 3], str(value_tuple[11] / 100.0))
                self.m_grid2.SetCellValue([7, 3], str(value_tuple[10] / 100.0))
                self.m_grid2.SetCellValue([8, 3], str(value_tuple[2] / 100.0))
                self.m_grid2.SetCellValue([9, 3], str(value_tuple[5] / 10.0))
                self.m_grid2.SetCellValue([10, 3], str(value_tuple[6] / 100.0))
                self.m_grid2.SetCellValue([11, 3], str(value_tuple[7] / 100.0)) 

                thresholds_tuple = self.master.execute(self.slave_addr, cst.READ_HOLDING_REGISTERS, 300, 60)
                columns = [1, 2, 4, 5]
                n = 0
                for i in [2, 0, 1, 3]:
                    col = columns[n]
                    self.m_grid2.SetCellValue([0, col], str(thresholds_tuple[10 * 4 + i] / 100.0))
                    self.m_grid2.SetCellValue([1, col], str(thresholds_tuple[11 * 4 + i] / 10.0))
                    self.m_grid2.SetCellValue([2, col], str(thresholds_tuple[0 * 4 + i] / 100.0))
                    self.m_grid2.SetCellValue([3, col], str(thresholds_tuple[5 * 4 + i] / 100.0))
                    self.m_grid2.SetCellValue([4, col], str(thresholds_tuple[4 * 4 + i] / 10.0))
                    self.m_grid2.SetCellValue([5, col], str(thresholds_tuple[1 * 4 + i] / 100.0))
                    self.m_grid2.SetCellValue([6, col], str(thresholds_tuple[2 * 4 + i] / 100.0))
                    self.m_grid2.SetCellValue([7, col], str(thresholds_tuple[3 * 4 + i] / 100.0))
                    self.m_grid2.SetCellValue([8, col], str(thresholds_tuple[9 * 4 + i] / 100.0))
                    self.m_grid2.SetCellValue([9, col], str(thresholds_tuple[8 * 4 + i] / 10.0))
                    self.m_grid2.SetCellValue([10, col], str(thresholds_tuple[6 * 4 + i] / 100.0))
                    self.m_grid2.SetCellValue([11, col], str(thresholds_tuple[7 * 4 + i] / 100.0))
                    n += 1

                for row in range(12):
                    if self.m_grid2.GetCellValue([row, 5]) == "655.35" or self.m_grid2.GetCellValue([row, 5]) == "6553.5":
                        for col in range(1, 6):
                            self.m_grid2.SetCellValue([row, col], "--")
                
                if not(self.check_parameters_thread.is_alive()):
                    self.check_parameters_thread = threading.Thread(target=self.check_parameters)
                    self.check_parameters_thread.start()
                    self.show_status(u"参数读取进程启动正常")
            except Exception as err:
                self.show_status(u"设备配置读取错误:{}".format(err))
                pass            
            return super().read_configuration(event)

    def write_configuration(self, event):
        if self.heartbeat_thread.is_alive():
            new_slave_addr = self.slaves[self.m_choiceUnitNum.GetSelection()]
            if new_slave_addr != self.slave_addr:
                try:
                    self.master.execute(self.slave_addr, cst.WRITE_SINGLE_REGISTER, 3, output_value=new_slave_addr)
                except:
                    self.show_message('从机地址修改异常')
                    self.m_choiceUnitNum.SetSelection(int(self.slave_addr - 96)) ## unit number
                else:
                    self.show_status(u"从机地址修改完成")
                    sleep(3)
                    self.slave_addr = new_slave_addr

            product_type = self.m_choice2.GetSelection()
            unit_type = self.m_choice3.GetSelection()
            rated_voltage = self.m_choice4.GetSelection()
            try:
                self.master.execute(self.slave_addr, cst.WRITE_MULTIPLE_REGISTERS, 200, 3,
                            output_value=[product_type, unit_type, rated_voltage])
                self.show_status(u"设备配置完成")
            except Exception as err:
                # self.show_status(u"设备配置异常")
                self.show_message(u"设备配置错误:{}".format(err))

            self.update_stutas_bar()
        return super().write_configuration(event)
   
    def check_parameters(self):
        while (self.ser.is_open) and (self.master._is_opened):
            try: 
                measurements_tuple = self.master.execute(self.slave_addr, cst.READ_INPUT_REGISTERS, 0, 4)
                sleep(0.2)
                open_current = measurements_tuple[0] / 100.0
                close_current = measurements_tuple[1] / 100.0
                motor_current = measurements_tuple[2] / 100.0
                angle_degree = measurements_tuple[3] / 100.0
                self.m_grid1.SetCellValue([0, 0], str(open_current))
                self.m_grid1.SetCellValue([1, 0], str(close_current))
                self.m_grid1.SetCellValue([2, 0], str(motor_current))
                self.m_grid1.SetCellValue([3, 0], str(angle_degree))

                count_tuple = self.master.execute(self.slave_addr, cst.READ_INPUT_REGISTERS, 8, 4)
                sleep(0.2)
                open_count = count_tuple[1]
                close_count = count_tuple[2]
                motor_count = count_tuple[3]
                angle_count = count_tuple[0]
                self.m_grid1.SetCellValue([0, 1], str(open_count))
                self.m_grid1.SetCellValue([1, 1], str(close_count))
                self.m_grid1.SetCellValue([2, 1], str(motor_count))
                self.m_grid1.SetCellValue([3, 1], str(angle_count))

                swi_status_tuple = self.master.execute(self.slave_addr, cst.READ_COILS, 1, 2)
                sleep(0.2)
                open_status = bool(swi_status_tuple[0])
                close_status = bool(swi_status_tuple[1])
                if (open_status and not(close_status)):
                    self.m_staticTextPosition.SetLabelText(u"分闸")
                elif (not(open_status) and close_status):
                    self.m_staticTextPosition.SetLabelText(u"合闸")
                else:
                    self.m_staticTextPosition.SetLabelText(u"未知")

                self.show_status(u"设备测量参数读取正常")
            except Exception as err:
                self.show_status(u"设备测量参数读取异常:{}".format(err))
                # raise err
            finally:
                sleep(1)
    
    def set_current_zero(self):
        if self.ser.is_open:
            try:
                self.master.execute(self.slave_addr, cst.WRITE_MULTIPLE_REGISTERS, 7, 3, output_value=[0, 0, 0])
                sleep(2)
                self.show_status(u"电流零点重置正常")
            except Exception as err:
                self.show_status(u"电流零点重置异常")
    
    def on_check_highspeed(self, event):

        self.change_highspeed_thread = threading.Thread(target=self.do_change_highspeed)
        self.change_highspeed_thread.start()

        return super().on_check_highspeed(event)
    
    def do_change_highspeed(self):

        if self.heartbeat_thread.is_alive():
            if (self.ser.is_open) and (self.m_checkBox1.IsChecked()) and (self.ser.baudrate != 115200):
                self.change_slave_baudrate(115200)

            if (self.ser.is_open) and not(self.m_checkBox1.IsChecked()) and (self.ser.baudrate != 9600):
                self.change_slave_baudrate(9600)

    def on_open_fwupdate(self, event):
        self.firmware_file = self.m_filePicker1.GetPath()
        upgrade_thread = threading.Thread(target=self.do_update, args=(self.firmware_file,))
        upgrade_thread.start()
        return super().on_open_fwupdate(event)
    
    def sender_getc(self, size):
        return self.ser.read(size) or None

    def sender_putc(self, data):
        self.send_data_mutex.acquire()
        self.ser.write(data)
        self.send_data_mutex.release()

    def progress_bar(self, total_packets, file_size, file_name):
        progress = int(total_packets * 100 / (file_size / 1024))
        self.m_gauge1.SetValue(progress)

    def do_update(self, event):
        try:
            # message box
            dlg = wx.MessageDialog(None, u"固件升级可能会意外删除所有芯片内部文件，是否执行？", u"Warning", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Close(True)
                self.m_gauge1.Show()
                self.m_gauge1.SetValue(0)
                # stop other threads
                self.master.close()
                if self.heartbeat_thread.is_alive():
                    self.heartbeat_thread.join(1.0)            
                if self.check_parameters_thread.is_alive():
                    self.check_parameters_thread.join(1.0)

                self.master.execute(self.slave_addr, cst.WRITE_SINGLE_COIL, 4, output_value=1)
                sleep(5)
            else:
                dlg.Close(True)
            dlg.Destroy()
        except Exception as err:
            self.show_message('固件升级异常')

        self.send_data_mutex = threading.Lock()
        ymodem_sender = YMODEM(self.sender_getc, self.sender_putc)

        while True:
            ch_str = self.ser.read(1).decode("utf-8")
            if ch_str == "C":
                self.show_status('开始发送文件...')
                break
        try:
            file_stream = open(self.firmware_file, 'rb')
        except IOError as err:
            self.show_message("打开文件失败")
        file_name = os.path.basename(self.firmware_file)
        file_size = os.path.getsize(self.firmware_file)

        try:
            self.m_gauge1.SetValue(0)
            ymodem_sender.send(file_stream, file_name, file_size, callback=self.progress_bar)
        except Exception as err:
            file_stream.close()
            raise

        file_stream.close()
        self.m_gauge1.Hide()
        if self.m_gauge1.GetValue() >= 100:
            self.show_message(u"固件升级成功, 设备正在重置, 请等待10秒钟。")
        else:
            self.m_gauge1.SetValue(0)
            self.show_message(u"固件升级失败, 请重试。")


if __name__ == '__main__':
    app = wx.App(False)
    frame = MFrame(None)
    frame.Show(True)
    app.MainLoop()

