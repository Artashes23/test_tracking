
# QA Test Task: OpenCV Tracking


## Task Details
To validate the accuracy of the tracking algorithm, the following steps are performed:

For each tracked object, the average distance between the two points from left side and right side (which should follow the object) is calculated for the first 100 positions.
This average distance is compared with the width of the detected object.
If the absolute difference between the average distance and the width of the detected object is within a certain threshold (e.g., 20 pixels), the tracking is considered correct. This was done to make sure that any of the points(from right or the left side) will not deviate from the tracked object

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


> Example video link to download [here](https://www.pexels.com/video/black-and-white-video-of-people-853889/)

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

