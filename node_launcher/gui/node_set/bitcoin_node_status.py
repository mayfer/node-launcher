from typing import Dict

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QGroupBox, QWidget, QLabel, QGridLayout

from node_launcher.node_set.bitcoin import Bitcoin


class BitcoinNodeStatus(QGroupBox):
    bitcoin: Bitcoin
    grid: QGridLayout

    def __init__(self, bitcoin: Bitcoin, parent: QWidget = None):
        super().__init__(parent)
        self.bitcoin = bitcoin
        self.grid = QGridLayout()

        self.data: Dict[str, str] = {
            'release_version': self.bitcoin.software.release_version
        }

        self.populate()

    def populate(self):
        row = 1
        label_column = 1
        value_column = 2
        for key, value in self.data.items():
            key_label = QLabel(self)
            key_label.setText(key.replace('_', ' ').capitalize())
            self.grid.addWidget(key_label, row, label_column)
            value_label = QLabel(self)
            value_label.setText(value)
            self.grid.addWidget(value_label, row, value_column)
            row += 1
