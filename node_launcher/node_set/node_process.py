from PySide2.QtCore import QProcess
from PySide2.QtWidgets import QWidget

from node_launcher.constants import IS_WINDOWS
from node_launcher.node_set.bitcoin import Bitcoin
from node_launcher.services.bitcoin_software import BitcoinSoftware


class NodeProcess(QProcess):
    def __init__(self, bitcoin: Bitcoin, parent: QWidget = None):
        super().__init__(parent)
        self.bitcoin = bitcoin
        self.bitcoin_software = BitcoinSoftware()
        self.setProgram(self.bitcoin_software.bitcoind)

        dir_arg = f'-datadir={self.bitcoin.file.datadir}'
        if IS_WINDOWS:
            dir_arg = f'-datadir="{self.bitcoin.file.datadir}"'
        arguments = [
            dir_arg,
            '-server=1',
            '-disablewallet=1',
            f'-rpcuser={self.bitcoin.file.rpcuser}',
            f'-rpcpassword={self.bitcoin.file.rpcpassword}',
            f'-zmqpubrawblock=tcp://127.0.0.1:{self.bitcoin.zmq_block_port}',
            f'-zmqpubrawtx=tcp://127.0.0.1:{self.bitcoin.zmq_tx_port}'
        ]
        if self.bitcoin.file.prune:
            arguments += [
                '-prune=600',
                '-txindex=0'
            ]
        else:
            arguments += [
                '-prune=0',
                '-txindex=1'
            ]
        if self.bitcoin.network == 'testnet':
            arguments += [
                '-testnet=1',
            ]
        else:
            arguments += [
                '-testnet=0',
            ]
        self.setArguments(arguments)
        self.setProcessChannelMode(QProcess.MergedChannels)
