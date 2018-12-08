from unittest.mock import MagicMock

from PySide2.QtTest import QTest

from node_launcher.constants import TARGET_BITCOIN_RELEASE
from node_launcher.gui.node_set.bitcoin_node_status import BitcoinNodeStatus


class TestBitcoinNodeStatus(object):
    def test_bitcoin_node_status(self, qtbot: QTest):
        mock_bitcoin = MagicMock()
        mock_bitcoin.software.release_version = TARGET_BITCOIN_RELEASE

        widget = BitcoinNodeStatus(mock_bitcoin)

    def test_release_version(self, qtbot: QTest):
        mock_bitcoin = MagicMock()
        mock_bitcoin.software.release_version = TARGET_BITCOIN_RELEASE

        widget = BitcoinNodeStatus(mock_bitcoin)
        version = widget.release_version.text()
        assert version == TARGET_BITCOIN_RELEASE
