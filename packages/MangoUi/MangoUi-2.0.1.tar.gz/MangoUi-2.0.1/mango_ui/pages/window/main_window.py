# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description: 
# @Time   : 2024-10-30 18:15
# @Author : 毛鹏
from PySide6.QtGui import QCursor

from mango_ui import MenusModel, AppConfig
from mango_ui.pages.window.ui_window import UIWindow


class MainWindow(UIWindow):
    def __init__(self, style: AppConfig, menus: MenusModel, page_dict, l=None, ):
        super().__init__(style, menus, page_dict, l)

    def resizeEvent(self, event):
        self.resize_grips()

    def mousePressEvent(self, event):
        self.drag_pos = QCursor.pos()

