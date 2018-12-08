from PySide2.QtTest import QTest

from node_launcher.gui.node_set.node_set_widget import NodeSetWidget


class TestNodesWidget(object):
    def test_nodes_widget(self, qtbot: QTest):
        widget = NodeSetWidget()
