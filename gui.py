import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        processes = []

        test = {
            "name": "test",
            "cpuUsage": 37.0,
            "memoryUsage": 23.0,
            "diskUsage": 0.5,
            "networkUsage": 0.0,
        }

        for i in range(16):
            {processes.append(test)}

        numOfProcesses = len(processes)
        super().__init__()

        # Create a table widget
        self.table = QtWidgets.QTableWidget()

        # Set the number of rows and columns
        self.table.setRowCount(numOfProcesses)
        self.table.setColumnCount(5)

        # Add data to the table
        data = []
        self.setStyleSheet("background-color: #191919;")

        # Set the headers
        self.table.setHorizontalHeaderLabels(
            ["Name", "CPU", "Memory", "Disk", "Network"]
        )

        # Set the background color of the header labels
        self.table.horizontalHeader().setStyleSheet(
            """
            QHeaderView::section { background-color: #191919; color: white; border: 1px solid #2D2D2D;}
            """
        )

        self.table.verticalHeader().setStyleSheet(
            "QHeaderView::section { background-color: #191919; color: white; border: 1px solid #2D2D2D;}"
        )

        self.table.setStyleSheet(
            """
            QTableWidget  { background-color: #191919; color: white; gridline-color:#2D2D2D;}
            QTableCornerButton::section {background-color: #191919;}
            """
        )

        for process in processes:
            {
                data.append(
                    [
                        process["name"],
                        str(process["cpuUsage"]) + "%",
                        str(process["memoryUsage"]) + "%",
                        str(process["diskUsage"]) + "%",
                        str(process["networkUsage"]) + "%",
                    ]
                )
            }

        for row, rowData in enumerate(data):
            for column, item in enumerate(rowData):
                self.table.setItem(row, column, QtWidgets.QTableWidgetItem(item))
        # Create a layout and add the table to it
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(548, 600)
    widget.show()

    sys.exit(app.exec())
