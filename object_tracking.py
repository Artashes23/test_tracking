import cv2

# https://www.pexels.com/video/black-and-white-video-of-people-853889/  please use this video as an example


# Load pre-trained HOG detector for pedestrian detection
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Load the video
video_path = "C:\\Users\\artas\\OneDrive\\Desktop\\test_task\\test_tracking\\pexels_videos_2670 (1080p).mp4"
cap = cv2.VideoCapture(video_path)

# Counter to keep track of detected positions
positions_detected = 0

while positions_detected < 1:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect people in the frame
    (rects, _) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
    
    # If people are detected in the frame
    if len(rects) > 0:
        # Calculate distances from the center for each detected person
        center_x = frame.shape[1] // 2
        center_y = frame.shape[0] // 2
        min_distance = float('inf')
        nearest_person_index = None
        
        for i, (x3, y3, w3, h3) in enumerate(rects):
            person_center_x = x3 + w3 // 2
            person_center_y = y3 + h3 // 2
            distance = ((center_x - person_center_x) ** 2 + (center_y - person_center_y) ** 2) ** 0.5
            
            # Update nearest person if closer to the center
            if distance < min_distance:
                min_distance = distance
                nearest_person_index = i + 1
        
        # Print position and size of the nearest person
        x3, y3, w3, h3 = rects[nearest_person_index]
        print("Position of nearest person (x, y):", x3, y3)
        print("Size of nearest person (height,width):", h3, w3)
        
        # Draw rectangle around the nearest person
        cv2.rectangle(frame, (x3, y3), (x3 + w3, y3 + h3), (0, 255, 0), 2)

        # Draw green point for the detected person
        cv2.circle(frame, (x3 + w3 // 2, y3 + h3 // 2), 5, (0, 255, 0), -1)
        
        # Increment the position counter
        positions_detected += 1
        
        # Define initial bounding boxes for two points to follow the object
        bbox1 = (x3, y3, 200, 200)
        bbox2 = (x3 - h3//2, y3 - w3//2, 200, 200)

        # Create the CSRT tracker for both points
        tracker1 = cv2.TrackerCSRT_create()
        tracker2 = cv2.TrackerCSRT_create()

        # Initialize the trackers with the bounding boxes
        tracker1.init(frame, bbox1)
        tracker2.init(frame, bbox2)

        # Define a list to store the distances between the two points
        distances = []

        while True:
            # Read the next frame
            ret, frame = cap.read()

            # Check if frame is read successfully
            if not ret:
                print("No more frames to read")
                break

            # Update the trackers with the current frame
            success1, bbox1 = tracker1.update(frame)
            success2, bbox2 = tracker2.update(frame)

            # Draw the bounding boxes on the frame
            if success1 and success2:
                x1, y1, w1, h1 = bbox1
                x2, y2, w2, h2 = bbox2
                
                # Calculate the centroids of the bounding boxes
                centroid1_x = x1 + w1 // 2
                centroid1_y = y1 + h1 // 2
                centroid2_x = x2 + w2 // 2
                centroid2_y = y2 + h2 // 2
                
                # Calculate the distance between the centroids
                distance = ((centroid1_x - centroid2_x) ** 2 + (centroid1_y - centroid2_y) ** 2) ** 0.5
                distances.append(distance)
                
                # Draw a line between the centroids
                cv2.line(frame, (centroid1_x, centroid1_y), (centroid2_x, centroid2_y), (255, 0, 0), 2)

                # Draw red and green points for the tracked objects
                cv2.circle(frame, (centroid1_x, centroid1_y), 5, (0, 255, 0), -1)
                cv2.circle(frame, (centroid2_x, centroid2_y), 5, (0, 0, 255), -1)

            # Display the resulting frame
            cv2.imshow('Tracking', frame)

            # Exit the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Print the distances between the two points for each position
        print("Distances between the two points for each position:")
        for i, distance in enumerate(distances, start=1):
            print(f"Position {i}: {distance}")

        # Calculate the average distance for the first 100 positions
        average_distance = sum(distances[:100]) / min(100, len(distances))
        print("Average distance for the first 100 positions:", average_distance)
        # Compare average distance for two initial bounding boxes from each other for first 100 positions to width of detected object
        print(average_distance-w3)
        assert average_distance - w3 < 20, 'Tracking was incorrect'
        # Release resources
        cap.release()
        cv2.destroyAllWindows()
