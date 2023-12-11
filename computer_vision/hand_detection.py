import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            ("Ignoring empty camera frame.")
            continue
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        h, w, _ = image.shape
        # image = cv2.flip(image, 1)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # print hand is left
                thumb = hand_landmarks.landmark[4]
                index = hand_landmarks.landmark[8]
                # denormalize the coordinates
                thumb_p = int(thumb.x * w), int(thumb.y * h)
                index_p = int(index.x * w), int(index.y * h)
                # draw a circle
                cv2.circle(image, thumb_p, 10, (0, 255, 0), 5)
                cv2.circle(image, index_p, 10, (0, 255, 0), 5)
                cv2.line(image, thumb_p, index_p, (255, 255, 0), 2)
                # calculate the distance
                dist = ((thumb_p[0] - index_p[0]) ** 2 + (thumb_p[1] - index_p[1]) ** 2) ** 0.5
                cv2.putText(image, f'{dist:.2f} pixels',(50,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                
            
        
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()
cv2.destroyAllWindows()