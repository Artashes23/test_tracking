import cv2
import random

# Load the video
video_path = "C:\\Users\\artas\\OneDrive\\Desktop\\test_task\\test_tracking\\pexels_videos_2670 (1080p).mp4"
cap = cv2.VideoCapture(video_path)

# Initialize the trackers
tracker1 = cv2.TrackerCSRT_create()
tracker2 = cv2.TrackerCSRT_create()

while True:
    ret, frame = cap.read()
    if not ret:
        print("No more frames to read")
        break
    
    frame_height, frame_width = frame.shape[:2]

    # Generate random position for the rectangle
    x = random.randint(0, frame_width - 50)  
    y = random.randint(0, frame_height - 50)
    w, h = 50, 50  
    
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Define initial bounding boxes for two points to follow the object
    bbox1 = (x, y, w, h)
    bbox2 = (x + w // 2, y + h // 2, w // 4, h // 4)    # Initial point within the bounding box

    tracker1.init(frame, bbox1)
    tracker2.init(frame, bbox2)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("No more frames to read")
            break

        success1, bbox1 = tracker1.update(frame)
        success2, bbox2 = tracker2.update(frame)

        # Draw the  box around the object
        if success1:
            x1, y1, w1, h1 = [int(i) for i in bbox1]
            cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)

        if success2:
            x2, y2, w2, h2 = [int(i) for i in bbox2]
            cv2.circle(frame, (x2 + w2 // 2, y2 + h2 // 2), 5, (0, 0, 255), -1)
        
        #Check if the point stays within the box  
        assert x1 <= x2 <= x1 + w1 - w2 and y1 <= y2 <= y1 + h1 - h2, 'Point is out of the box'
       
        # Display the resulting frame
        cv2.imshow('Tracking', frame)

        # Exit the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()
