English | [简体中文](./readme_cn.md)

# How to install

- No installation required for web version. Open [this link](https://object-detector-and-alarm.netlify.app/generic_cv_tasks.html) in Firefox/Chrome.
- As it is developed using WebAssembly, it takes a while to compile the first time you open it. Please wait patiently.

# Introduction

- Deep learning algorithm based on object detection, supports 80 types of targets
- Supported models are [nanodet-plus-m](https://github.com/RangiLyu/nanodet) series
- Provides a simple and easy-to-use object detection tool to meet daily needs

# Third-party software used

- [opencv 4.8.0](https://github.com/opencv/opencv)
- [ncnn-20230816](https://github.com/Tencent/ncnn)
- [Qt6.5.2](https://www.qt.io/)
- [Eigen 3.4.0](https://eigen.tuxfamily.org/index.php?title=Main_Page)
- [Boost 1.81.0](https://www.boost.org/)

# Features of this software

- Object detection, tracking, and counting
- Area alarm
- Alarm record

# How to use the websocket of this software

- If you want to transmit images through websocket, please refer to [qt_base_opencv_videocapture_server.py](https://github.com/stereomatchingkiss/object_detection_and_alarm/blob/main/qt_base_opencv_videocapture_server.py)
- If you want to receive alarms, please refer to [qt_base_alert_receiver.py](https://github.com/stereomatchingkiss/object_detection_and_alarm/blob/main/qt_base_alert_receiver.py)
- [install_qt_script.md](https://github.com/stereomatchingkiss/object_detection_and_alarm/blob/main/install_qt_script.md)，explain how to install the required packages

# Limitations of the web version

- The running speed is not as fast as the desktop version
- Unable to actively write settings and alarms to local hard drive. In order to bypass this limitation, the web version provides websocket to transmit alarms.
- Deep learning algorithms do not support GPU
- When using websocket to transmit information, if it is not a local machine, SSL must be used, and the key used by the target must be recognized by the browser.

# 范例

- [Video tutorial](https://youtu.be/TNancuXjlcM)
- ![Save and load the settings](./imgs/save_and_load.png)
- ![Select the area to track the object](./imgs/select_roi.png)
- ![Tracking and Counting](./imgs/track_and_count.png)

# Future plans

- Support traditional object detection algorithms
- Support more models
- Fire/smoke detection and alarm
- Fall detection and alarm
- License plate detection and OCR
- Face recognition and alarm
- Emotion, age, and gender recognition and alarm
- Behavior detection and alarm
- Image super resolution
- Image generation(stable diffusion)
- Image restoration(image painting)
- Support opening multiple videos at the same time
- Others

# Usage occasions

- Security monitoring, logistics transportation, retail industry, etc.

# Others

- If you think it is good after using it, please give me a star, thank you
- If you find a bug, please open an issue
- If you need new features, please open an issue
- GPU support will be completed by Vulkan. We don't plan to support CUDA for now, because it's too bloated and only supports Nvidia GPUs.
-
- The copyright of this software belongs to the software developer.
- Except for direct sales, this software can be used for personal or commercial purposes.
- When using this software, please comply with relevant laws and regulations. The software developer is not responsible for any losses caused by using this software.
- How to compile Qt6.5.2 that supports SIMD and thread, please refer to [build_qt6_wasm_steps.txt](https://github.com/stereomatchingkiss/object_detection_and_alarm/blob/main/build_qt6_wasm_steps.txt)
- The UI of this program is designed for desktop, please open it on the desktop
- Release the desktop version

# Contact me

- If you have a case to ask me for help, please leave your email
- Good at solving problems using existing technologies, prefer to use Qt