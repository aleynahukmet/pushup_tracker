#importing dependencies
import cv2
import mediapipe as mp
import numpy as np
#set up mediapipe
#get pose estimation model(there are many other models within mediapipe)
mp_pose = mp.solutions.pose
#get the drawing utilities for visualization
mp_draw = mp.solutions.drawing_utils


#load video
cap = cv2.VideoCapture("production ID_4945123.mp4") #0 for webcam
#setting up the Pose function
pose = mp_pose.Pose()
#push-up counter
counter = 0
#stage going to represent whether or not down or up
Stage= False

#loop to read each frame of video
while True:
    ret, img = cap.read()

    #resize the image
    img = cv2.resize(img,(1000,800))
    #recolor the image
    #we want the image to be RGB when we are passing it to mediapipe
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #perform pose detection
    #store our detections in results array
    results = pose.process(img)
    #recolor the image back to BGR to feed the opencv
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    # extract landmark
    # sometimes landmarks are not visible so have a try and except block

    #calculate angles
    def calculate_angle(a,b,c):
        a = np.array(a) #first point
        b = np.array(b) #mid point
        c = np.array(c) #end point

        radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)

        if angle>180.0:
            angle = 360 - angle

        return angle

    #store landmarks in landmarks variable
    landmarks = results.pose_landmarks.landmark

    #three different joint coordinates for shoulder angle
    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y]
    elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW].y]
    wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST].y]
    #calculate the angle
    angle1 = calculate_angle(shoulder, elbow, wrist)

    #get the height and width of original image for rescaling the coordinates
    height, width, _ = img.shape
    shape = [width,height]
    print(shape)

    #visualize
    cv2.putText(img,"Elbow angle:"+ " " + str(angle1),tuple(np.multiply(elbow,shape).astype(int)),
                cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

    # print(landmarks)
    # if there is no detection pass

    #push-up counter logic
    if angle1 > 90:
        stage = 'up'
    if angle1 <= 90 and stage=='up':
        stage = 'down'
        counter += 1
        print(counter)

    #setup status box
    cv2.rectangle(img,(0,0),(225,73),(245,117,16),-1)
    #show the counts on the status box
    cv2.putText(img, "Number of push-ups:", (15,12),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(img, str(counter), (80,60),
                cv2.FONT_HERSHEY_SIMPLEX
                , 2, (255, 255, 255), 2)

    #draw landmarks
    #first pass the image
    #then pass the landmarks list -results.pose_landmarks (coordinates)
    #then pass the connections
    #set the attributies of landmarks(dots) drawings and connections(lines) drawings
    mp_draw.draw_landmarks(img,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,
                           mp_draw.DrawingSpec(color=(245,117,66),thickness=2 ,circle_radius=2),
                           mp_draw.DrawingSpec(color=(254,66,230),thickness=2,circle_radius=2))



    #print(len(results.pose_landmarks))
    cv2.imshow("pose estimation",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()