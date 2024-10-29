from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.data_list = [
            {'id': 53, 'step_sort': 0},
            {'id': 52, 'step_sort': 1},
            {'id': 51, 'step_sort': 2},
            {'id': 50, 'step_sort': 3},
        ]

        self.table = QTableWidget(len(self.data_list), 2)
        self.table.setHorizontalHeaderLabels(['ID', 'Step Sort'])
        self.populate_table()

        self.up_button = QPushButton("上移")
        self.lower_button = QPushButton("下移")

        self.up_button.clicked.connect(self.up)
        self.lower_button.clicked.connect(self.lower)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.up_button)
        layout.addWidget(self.lower_button)

        self.setLayout(layout)

    def populate_table(self):
        for row, data in enumerate(self.data_list):
            self.table.setItem(row, 0, QTableWidgetItem(str(data['id'])))
            self.table.setItem(row, 1, QTableWidgetItem(str(data['step_sort'])))

    def update_data(self):
        # 打印更新后的数据
        print("更新后的数据:")
        for index, data in enumerate(self.data_list):
            print(f"ID: {data['id']}, Step Sort: {index}")

    def up(self):
        row = self.table.currentRow()
        if row > 0:
            # 交换数据
            self.data_list[row], self.data_list[row - 1] = self.data_list[row - 1], self.data_list[row]
            # 更新表格
            self.populate_table()
            # 打印更新后的数据
            self.update_data()
            # 选择新的行
            self.table.setCurrentCell(row - 1, 0)

    def lower(self):
        row = self.table.currentRow()
        if row < len(self.data_list) - 1:
            # 交换数据
            self.data_list[row], self.data_list[row + 1] = self.data_list[row + 1], self.data_list[row]
            # 更新表格
            self.populate_table()
            # 打印更新后的数据
            self.update_data()
            # 选择新的行
            self.table.setCurrentCell(row + 1, 0)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
