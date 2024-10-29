import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QMessageBox

from mango_ui import TreeModel
from mango_ui.widgets.window.mango_tree import MangoTree


class ExpandableListWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.tree_widget = MangoTree('测试')
        self.tree_widget.clicked.connect(self.on_child_item_clicked)
        data = [TreeModel(**i) for i in [{
            "title": "演示-登录退出场景1",
            "status": 1,
            "key": "{\"test_suite_id\":424314712861,\"ui_case_result\":70,\"case_id\":11}",
            "children": [
                {
                    "title": "普通权限用户登录1",
                    "status": 1,
                    "key": "{\"test_suite_id\":424314712861,\"page_steps_result\":107,\"case_id\":11,\"page_step_id\":15}",
                    "children": []
                },
                {
                    "title": "用户退出登录1",
                    "status": 1,
                    "key": "{\"test_suite_id\":424314712861,\"page_steps_result\":108,\"case_id\":11,\"page_step_id\":16}",
                    "children": []
                }
            ]
        }, {
            "title": "演示-登录退出场景2",
            "status": 1,
            "key": "{\"test_suite_id\":424314712861,\"ui_case_result\":70,\"case_id\":11}",
            "children": [
                {
                    "title": "普通权限用户登录2",
                    "status": 1,
                    "key": "{\"test_suite_id\":424314712861,\"page_steps_result\":107,\"case_id\":11,\"page_step_id\":15}",
                    "children": []
                },
                {
                    "title": "用户退出登录2",
                    "status": 1,
                    "key": "{\"test_suite_id\":424314712861,\"page_steps_result\":108,\"case_id\":11,\"page_step_id\":16}",
                    "children": []
                }
            ]
        }]]
        self.tree_widget.set_item(data)
        layout.addWidget(self.tree_widget)
        self.setLayout(layout)

    def on_child_item_clicked(self, model: TreeModel):
        # 处理子项点击信号，model 是整个 TreeModel 对象
        QMessageBox.information(self, "子项点击", f"你点击了: {model.title}\n状态: {model.status}\n键: {model.key}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpandableListWidget()
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())
