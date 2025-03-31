from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
)
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QFont
import subprocess
import sys


class ServerThread(QThread):
    log_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)

    def __init__(self, port):
        super().__init__()
        self.port = port
        self.server_process = None

    def run(self):
        try:
            # Run the server.py script
            self.server_process = subprocess.Popen(
                ["python", "server.py"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # Send the port to the server process
            self.server_process.stdin.write(self.port + "\n")
            self.server_process.stdin.flush()

            # Read server output and emit logs
            for line in self.server_process.stdout:
                self.log_signal.emit(line.strip())
            for error_line in self.server_process.stderr:
                self.error_signal.emit(error_line.strip())
        except Exception as e:
            self.error_signal.emit(str(e))
        finally:
            self.stop()

    def stop(self):
        if self.server_process:
            self.server_process.terminate()
            self.server_process = None


class ServerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Procyon WebServer 2025")
        self.setGeometry(100, 100, 800, 600)

        self.server_thread = None

        # Main layout
        main_layout = QVBoxLayout()

        # Port input layout
        port_layout = QHBoxLayout()
        port_label = QLabel("Port:")
        port_label.setFont(QFont("Arial", 12))
        self.port_input = QLineEdit()
        self.port_input.setText("8086")  # Default port
        self.port_input.setFont(QFont("Arial", 12))
        self.start_button = QPushButton("Start Server")
        self.start_button.setFont(QFont("Arial", 12))
        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.start_button.clicked.connect(self.start_server)
        self.stop_button = QPushButton("Stop Server")
        self.stop_button.setFont(QFont("Arial", 12))
        self.stop_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336; color: white; padding: 10px; border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #e53935;
            }
        """)
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_server)

        port_layout.addWidget(port_label)
        port_layout.addWidget(self.port_input)
        port_layout.addWidget(self.start_button)
        port_layout.addWidget(self.stop_button)

        # Log display
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        self.log_display.setFont(QFont("Courier New", 10))
        self.log_display.setStyleSheet("background-color: #1e1e1e; color: #dcdcdc; padding: 10px; border-radius: 5px;")

        # Add layouts to main layout
        main_layout.addLayout(port_layout)
        main_layout.addWidget(QLabel("Server Logs:"))
        main_layout.addWidget(self.log_display)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Apply global styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c2f33;
            }
            QLabel {
                color: #ffffff;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
            }
        """)

    def resizeEvent(self, event):
        """Handle auto-resize of widgets."""
        self.log_display.setFixedHeight(self.height() - 200)
        super().resizeEvent(event)

    def start_server(self):
        port = self.port_input.text()
        if not port.isdigit():
            QMessageBox.critical(self, "Invalid Port", "Please enter a valid port number.")
            return

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

        # Start the server thread
        self.server_thread = ServerThread(port)
        self.server_thread.log_signal.connect(self.append_log)
        self.server_thread.error_signal.connect(self.handle_error)
        self.server_thread.start()

    def stop_server(self):
        if self.server_thread:
            self.server_thread.stop()
            self.server_thread = None
            self.append_log("Server stopped.")

        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def append_log(self, message):
        self.log_display.append(message)

    def handle_error(self, error_message):
        self.log_display.append(f"ERROR: {error_message}")
        QMessageBox.critical(self, "Server Error", error_message)
        self.stop_server()


def main():
    app = QApplication(sys.argv)
    gui = ServerGUI()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()