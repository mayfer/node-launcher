from unittest.mock import MagicMock

from PySide2.QtTest import QTest

from node_launcher.node_set.bitcoin import Bitcoin
from node_launcher.node_set.node_process import NodeProcess


class TestNodeProcess(object):
    def test_node_process(self, qtbot: QTest, bitcoin: Bitcoin):
        process = NodeProcess(bitcoin=bitcoin)

    def test_start(self, qtbot: QTest, bitcoin: Bitcoin):
        process = NodeProcess(bitcoin=bitcoin)
        process.start()
        process.waitForStarted()
        process.kill()
        process.waitForFinished()
        print('here')
