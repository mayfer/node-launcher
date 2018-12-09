from PySide2.QtCore import Slot
from PySide2.QtTest import QTest

from node_launcher.node_set.bitcoin import Bitcoin
from node_launcher.node_set.node_process import NodeProcess


class TestNodeProcess(object):
    def test_node_process(self, qtbot: QTest, bitcoin: Bitcoin):
        process = NodeProcess(bitcoin=bitcoin)

    def test_state_change(self, qtbot: QTest, bitcoin: Bitcoin):
        process = NodeProcess(bitcoin=bitcoin)

        @Slot(str)
        def handle_state_change(state: str):
            print(state)
            assert state

        process.state_change.connect(handle_state_change)

        process.start()
        process.waitForStarted()
        times = 0
        while True:
            process.waitForReadyRead()
            times += 1
            if times > 100:
                break
