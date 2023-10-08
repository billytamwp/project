# project
**Project Objective**
This project aims at using computer vision AI to generate alert to road users involving pedestrians and road vehicles at areas without traffic signal and with blind spots.

**Assumptions**
This version of my-project.py illustrates the idea using video file, which is more portable and convenience for offline demonstration.

The code was executed on Jetson Nano with 720p video stream.

jetson_inference and jetson_utils are required.

**Execution of Code**
The code can be executed by using
$python3 my-project.py

**Customization**
If other video files or video sources (e.g. webcam or IP camera) are used, the videoSource() shall be amended accodingly.

If the ROI are required to be modified to suit the FOV, the condition regarding the bounding box coordinates shall be updated accordingly.

If extension to external interfaces are required (e.g. display alerts to road users), the variables corresponding to the alert status can be utilized to further develop the code.
