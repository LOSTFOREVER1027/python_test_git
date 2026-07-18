# gui
# import easygui
# easygui.msgbox('hello everyone !')

# from easygui import *
# msgbox('Hello hotgirl !')

# import easygui as eg
# eg.msgbox('Hello darling !')

# import easygui as eg
# import sys
 
# while 1:
#     eg.msgbox('welcome to your first gui game !\t')

#     msg='what knowledge do you want learn from fishc ?\t'
#     title='multiactive'
#     choices=['love','programming','game','nathing']

#     choice=eg.choicebox(msg,title,choices)

#     eg.msgbox('your choice is :' + str(choice),'result')

#     msg='Do you wanna play this game ?'
#     if eg.ccbox(msg,title):
#         pass
#     else:
#         sys.exit(0)


# import easygui as eg
# choices=['A','B','C']
# reply=eg.choicebox('which you prefer ?',choices=choices)



# import easygui as eg
# eg.buttonbox('hello',image='hello.gif',choices=('hello','nohello','baga'))

# import sys
# from PySide6.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
# from PySide6.QtGui import QMovie
# from PySide6.QtCore import Qt

# app = QApplication(sys.argv)
# box = QDialog()
# layout = QVBoxLayout()
# label = QLabel()
# movie = QMovie("hello.gif")
# label.setMovie(movie)
# movie.start()
# layout.addWidget(label)
# btn_layout = QHBoxLayout()
# for t in ["hello", "nohello", "baga"]:
#     btn = QPushButton(t)
#     btn.clicked.connect(box.accept)
#     btn_layout.addWidget(btn)
# layout.addLayout(btn_layout)
# box.setLayout(layout)
# box.exec()

import scrapy
print(scrapy.__version__)  # 应该显示 2.17.0