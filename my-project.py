from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

net = detectNet(network="trafficcamnet", threshold=0.2) # model and confidence threshold

camera = videoSource("images/video/test_720.mp4") # input: file
display = videoOutput("display://0") # output: window

while display.IsStreaming():
    img = camera.Capture() # capture frame

    if img is None: # capture timeout
        continue

    detections = net.Detect(img, overlay='lines,labels,conf') # object detection, overlay setting
    
    person_exist = 0 # whether there are people crossing the road
    car_exist = 0 # whether there are cars coming

    display.Render(img) # Render image with detection overlap

    for detection in detections:

        # 0: car, 2: person
        # ROI is set based on target detection area
        if detection.ClassID == 0 and detection.Right > 1025:
             car_exist = 1

        if detection.ClassID == 2 and detection.Left < 350:
             person_exist = 1

    # summary of status
    if car_exist == 0 and person_exist == 0:
        display.SetStatus("Safety First!")

    if car_exist == 1 and person_exist == 0:
        display.SetStatus("There are cars coming!")

    if car_exist == 0 and person_exist == 1:
        display.SetStatus("There are people crossing the road!")

    # alert to be generated
    if car_exist == 1 and person_exist == 1:
        display.SetStatus("ALERT!")


