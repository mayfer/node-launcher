from PySide2.QtCore import QProcess, QByteArray, Signal
from PySide2.QtWidgets import QWidget, QErrorMessage

from node_launcher.node_set.bitcoin import Bitcoin
from node_launcher.services.bitcoin_software import BitcoinSoftware


class NodeProcess(QProcess):
    state_change = Signal(str)

    def __init__(self, bitcoin: Bitcoin, parent: QWidget = None):
        super().__init__(parent)
        self.bitcoin = bitcoin
        self.bitcoin_software = BitcoinSoftware()
        self.setProgram(self.bitcoin_software.bitcoind)
        self.status = 'off'

        arguments = [
            f'-datadir={self.bitcoin.file.datadir}',
            '-server=1',
           # '-printtoconsole',
           # '-debug=1',
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

        # noinspection PyUnresolvedReferences
        self.readyReadStandardError.connect(self.handle_error)
        # noinspection PyUnresolvedReferences
        self.readyReadStandardOutput.connect(self.handle_output)

    def handle_error(self):
        output: QByteArray = self.readAllStandardError()
        message = output.data().decode('utf-8').strip()
        QErrorMessage().showMessage(message)

    def handle_output(self):
        self.setCurrentReadChannel(0)
        output: QByteArray = self.readLine()
        message = output.data().decode('utf-8').strip()
        while message:
            timestamp = message.split(' ')[0]
            message = ' '.join(message.split(' ')[1:])
            print(message)
            if message.startswith('Bitcoin Core version'):
                self.state_change.emit(message)
            output = self.readLine()
            message = output.data().decode('utf-8').strip()
