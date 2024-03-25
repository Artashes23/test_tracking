
# QA Test Task: OpenCV Tracking

Welcome to the Inogate Company's QA Test Task repository! \
Here you will find a test task for Quality Assurance (QA) Engineers focusing on tracking using OpenCV.

---
## Task Details
Your initial task is to devise and implement ideas or algorithms for a  testing process to evaluate the performance of a tracking algorithm. \
Following the implementation, we will convene for discussions either online or offline, based on your preference, to review the proposed testing methodologies and determine the subsequent steps for refining the process.

---
## Requried Environment
- Python = 3.11
- opencv-python = 4.9.0
- opencv-contrib-python = 4.9.0
> [!NOTE]
> The installation process can vary depending on the operating system.\
> For installing OpenCV and its dependencies, you can find detailed instructions tailored to your specific OS by searching on Google or another search engine. 
---
## Getting Started
1. Clone this repository to your local machine using the following command:
```shell
git clone https://github.com/WindyLibra/opencv_tracking.git
```
2. Navigate to the cloned directory:
```shell
cd opencv_tracking
```

## Usage
1. Place your video file in the directory.
2. Run the Python script:
```shell
python3 object_tracking.py
```

By default, the program is configured to utilize the camera for capturing the video stream. To initiate the script with this default setting, simply execute the Python script without providing any additional arguments.

If you wish to process video files instead, you must explicitly specify the path to the desired video file changing video path. Replace `0` in the code below with the actual file path of your video:
> Example video link [here](https://www.youtube.com/watch?v=WvhYuDvH17I)

```python
# Define the video file path or 0 for webcamera input
video_path = 0
```
```python
# Define the video file path or 0 for webcamera input
video_path = "./your-video-name.mp4"
# or full path
video_path = "/root/Desktop/opencv_tracking/your-video-name.mp4"
```

3. Following the initialization of the video feed, the program will prompt you to designate the object to be tracked. Use your mouse to outline a box around the desired object. Upon completion, press the spacebar to commence the tracking process.


## Contact
>If you have any questions or need clarification regarding the task, please don't hesitate to contact us at info@inogate.com.
