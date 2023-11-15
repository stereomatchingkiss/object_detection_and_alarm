from PyQt5.QtNetwork import QHostAddress
from PyQt5.QtWebSockets import QWebSocketServer
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import QTimer

import argparse
import cv2
import sys

ap = argparse.ArgumentParser()
ap.add_argument("--downsample", required=False, type=int, default=1)
ap.add_argument("--max_fps", required=False, type=int, default=30, help="Increase the number if you want the server process the frame faster, maximum value is 1000")
ap.add_argument("--port", required=False, type=int, default=1234)
ap.add_argument("--opencv_url", type=str, required=True,
                help="Url of the video, could be local location of video, rtsp address, or enter number(ex : 0) to open webcam")

args = vars(ap.parse_args())

# Easier to shutdown the server if create it as a widget
class simple_websocket_server(QPushButton):
    def __init__(self, port : int = args["port"], parent = None):
        super(simple_websocket_server, self).__init__(parent)

        self.camera = None
        self.downsample = args["downsample"]
        self.max_fps = args["max_fps"]
        self.port = port
        self.server = QWebSocketServer("Simple websocket server", QWebSocketServer.NonSecureMode, self)
        self.socket = None
        self.timer = QTimer()
        self.timer.setInterval(int(1000.0/self.max_fps))

        self.setText("Close")

        self.clicked.connect(self.close)

        if(self.server.listen(QHostAddress.Any, port)):
            print("SSL Echo Server listening on port: ", port)
            self.server.newConnection.connect(self.on_new_connection)
            self.timer.timeout.connect(self.send_frame)

    def on_new_connection(self):

        print("socket connected")
        if(self.socket):
            print("This simple app only allowed one socket connection")
            return

        self.socket = self.server.nextPendingConnection()
        self.socket.disconnected.connect(self.socket_disconnected)

        self.send_frame()

    def send_frame(self):
        if self.camera is None:
            self.camera = cv2.VideoCapture(args["opencv_url"], )
            if(self.camera.isOpened() == False):
                print("cannot open camera from the url = ", args["opencv_url"])
                self.timer.stop()
                return
            else:
                self.timer.start()

        try:
            _, frame = self.camera.read()
            if frame is None:
                print("cannot capture frame")
            if self.socket:
                if args["downsample"] != 1:
                    height, width, _ = frame.shape
                    frame = cv2.resize(frame, (int(width / self.downsample), int(height / self.downsample)))

                _, buffer = cv2.imencode('.jpg', frame)
                self.socket.sendBinaryMessage(buffer.tobytes())

        except:
            self.camera.release()

    def socket_disconnected(self):
        print("socket disconnected")
        self.timer.stop()
        if self.socket:
            self.socket.deleteLater()
            self.socket = None
        if self.camera:
            self.camera.release()
            self.camera = None

def main():
    app = QApplication(sys.argv)

    win = simple_websocket_server()
    win.resize(400, 400)
    win.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()