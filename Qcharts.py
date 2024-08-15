import _thread
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
#from pyecharts import Geo
from PyQt5.QtCore import QUrl
from win32api import GetSystemMetrics
from PyQt5 import QtGui
from httpserver import *
from asyncJson import *

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.loadfinished = False
    self.setWindowTitle('大屏展示')
    self.showMaximized()
    #全屏显示
    self.showFullScreen()
    self.isFullScreen = True

    self.webview = WebEngineView()
    self.webview.load(QUrl(index_url))
    self.setCentralWidget(self.webview)

    QShortcut(QtGui.QKeySequence("Escape"), self, self.Esc)
    self.webview.loadFinished.connect(self.SetLoadFinished)

    _thread.start_new_thread(HttpServer, ())
    _thread.start_new_thread(self.ChangeData, ())

  def SetLoadFinished(self):
      self.loadfinished = True

  #模拟刷新数据
  def ChangeData(self):
      while 1:
          time.sleep(3)
          #页面加载完毕再开始刷新数据
          if self.loadfinished == False :
              continue
          change_all_json()

          # change_chart_map()
          try:
             self.webview.page().runJavaScript('''async_data()''')
          except Exception as e:
              print(e)



  #按ESC全屏或缩小
  def Esc(self):
      if self.isFullScreen == True :
          self.isFullScreen = False
          #不加这句的话，标题栏就看不到了
          self.showNormal()
          #设置固定宽高
          self.setGeometry(GetSystemMetrics(0)/2, GetSystemMetrics(1)/2, 1280, 768)
          #再移动到屏幕中央
          screen = QDesktopWidget().screenGeometry()
          size = self.geometry()
          self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
      else:
          self.showFullScreen()
          self.isFullScreen = True


class WebEngineView(QWebEngineView):
  windowList = []

  # 重写createwindow()
  def createWindow(self, QWebEnginePage_WebWindowType):
    new_webview =  WebEngineView()
    new_window = MainWindow()
    new_window.setCentralWidget(new_webview)
    #new_window.show()
    self.windowList.append(new_window) #注：没有这句会崩溃！！！
    return new_webview


if __name__ == "__main__":
  app = QApplication(sys.argv)
  w = MainWindow()
  w.show()
  sys.exit(app.exec_())