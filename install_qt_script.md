# Install dependencies

## On windows
. Install anaconda
. conda create --name your_name
. conda install pip
. pip install pyqt5
. pip install opencv-python-headless

## On ubuntu 20.04

. virtualenv qt_env
. source qt_env/bin/activate
. pip install --upgrade pip
. pip install pyqt5
. pip install opencv-python-headless

# Execute

python qt_base_opencv_videocapture_server.py --opencv_url your_url/your_video.mp4 #This will send the frame to the client

# Cautions

. This simple server accept one client connection only
. If the frame is too large, please enter "--downsample 2" to scale down the image, 2 mean scale down 2 times, 3 mean times etc
. For simplicity, this simple server do not perform any error handling of socket connection

