import wx

# 创建一个对象
class Example(wx.Frame):
    def __init__(self,*args,**kwargs):
        super(Example,self).__init__(*args,**kwargs)
        self.InitUI()


    def InitUI(self):
        menuber=wx.MenuBar() # 创建菜单栏对象
        filemenu=wx.Menu() # 创建菜单对象
        fitem=filemenu.Append(wx.ID_EDIT,'quit','Quit application')# 菜单对象添加属性
        fitem=filemenu.Append(wx.ID_NEW,'New')
        fitem=filemenu.Append(wx.ID_OPEN,'Open')
        fitem=filemenu.Append(wx.ID_SAVE,'save')
        filemenu.AppendSeparator()
        menuber.Append(filemenu,'&file') # 菜单栏添加菜单
        self.SetMenuBar(menuber)# 设定菜单栏

        self.Bind(wx.EVT_MENU,self.OnQiut,fitem) # 菜单绑定退出事件

        self.SetSize(600,800) # 设置窗口大小
        self.SetTitle('FP便捷操作') # 设置窗口标题
        self.Show(True) #窗口展示

    def OnQiut(self,e): # 菜单退出方法
        self.Close()


def main():
    ex=wx.App()  # 将对象实例化
    Example(None) # 类传入值
    ex.MainLoop() # 主循环

if __name__=='__main__':
    main()