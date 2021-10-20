# VIDEO FEED
detector = WorkoutDetector()

cap = cv2.VideoCapture(0)
stage =None
vis = None
angle =0


message = ' '

stage_notes = ''
angle_notes = ''
message_note = ' '

IN_FRAME =False
SHOW_START_POSE=True


START_POSE= False



while cap.isOpened():
    ret, frame = cap.read()
    image = detector.findPose(frame)
    
    message_note = "inframe{}".format(IN_FRAME)
    
    angle_notes = "in pose".format( START_POSE)
    
    
    
    landmarks = detector.detect_landmarks(image)
    lmList = detector.getPosition(image, draw=False)
    cv2.putText(image, message_note , (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
    cv2.putText(image, angle_notes , (0,300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)


    if landmarks:
    
        if detector.body_in_frame(landmarks, 'nose', 'right_shoulder'):
            IN_FRAME = True
            message = 'in frame'
            
        else:
            IN_FRAME = False
            message = 'not in frame'
            
            
        if IN_FRAME:
                            
            
            if bent(arm_left_angle, 90) or bent(arm_left_angle, 90) and ankle_width > 90:
                SHOW_START_POSE=False
                START_POSE= True
                arm_left_angle = detector.calculate_angle(image,left_arm_lms)
                arm_right_angle = detector.calculate_angle(image,right_arm_lms)

            else:
                SHOW_START_POSE=False
                START_POSE= True
            
            if START_POSE:
                pass
            else:
                pass
        else:
            pass
    else:
        pass
    
    
    
    image = cv2.resize(image, (600, 600))                # Resize image
    cv2.imshow('Mediapipe Feed', image)
    
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
        