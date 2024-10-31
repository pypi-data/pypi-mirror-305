# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description: 
# @Time   : 2024-10-31 9:51
# @Author : 毛鹏
from PySide6.QtWidgets import QApplication

from mango_ui.pages.component import ComponentPage
from mango_ui.pages.window.main_window import MainWindow
from mango_ui.settings.settings import STYLE, MENUS


def main():
    page_dict = {
        'component': ComponentPage,
    }

    app = QApplication([])
    login_window = MainWindow(STYLE, MENUS, page_dict)
    login_window.show()
    app.exec()


main()
