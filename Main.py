import cv2
import mediapipe as mp
import Utility
import Alarm
import SMS


# Global variable for fram per second and exit key:
FPS = 15
ESC = 27

# Global object for face detection and face mesh:
mp_facemesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Alarm object to play alarm:
alarm = Alarm.Alarm()

# SMS object to send sms:
sms = SMS.SMS()

# Static data set for ear calculation:
static_data = {
    "image_width"   :   640,
    "image_height"  :   480,
    "left_eye"      :   [362, 385, 387, 263, 373, 380],
    "right_eye"     :   [33, 160, 158, 133, 153, 144]
}

# ear bound:
ear_bound = 0.2

def main():
    # Define the video capture object:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Can't open camera")
        exit()
    

    with mp_facemesh.FaceMesh(
        max_num_faces = 1,
        refine_landmarks = True,
        min_detection_confidence = 0.9,
        min_tracking_confidence = 0.6
    ) as face_mesh:
        COUNTER = 0
        while True:
            # Capture the image:
            success, image = cap.read()
            image = cv2.flip(image, 1)

            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            result = face_mesh.process(rgb_image)

            if result.multi_face_landmarks:
                # Draw the landMarks and eye:
                mp_drawing.draw_landmarks(
                    image = image,
                    landmark_list = result.multi_face_landmarks[0],
                    connections = mp_facemesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = mp_drawing_styles.get_default_face_mesh_tesselation_style()
                )

                mp_drawing.draw_landmarks(
                    image = image,
                    landmark_list = result.multi_face_landmarks[0],
                    connections = mp_facemesh.FACEMESH_IRISES,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = mp_drawing_styles.get_default_face_mesh_iris_connections_style()
                )
                
                # Calculate eye state:
                ear = Utility.get_avg_EAR(
                    landmarks = result.multi_face_landmarks[0].landmark,
                    left_eye_inds = static_data["left_eye"],
                    right_eye_inds = static_data["right_eye"],
                    image_width = static_data["image_width"],
                    image_height = static_data["image_height"]
                )

                # Take action on eye state:
                if ear <= ear_bound:
                    COUNTER += 1
                else:
                    COUNTER -= 5

                if COUNTER < 0:
                    COUNTER = 0
                    sms.cooldown()

                if COUNTER >= 20:
                    alarm.play()
                    sms.send()
                    
                print(COUNTER)

            # Display the resulting image:
            cv2.imshow("WEBCAM🎥", image)

            # Set the time for per frame:
            if cv2.waitKey(1000//FPS) == ESC:
                break 

        # Release the cap obj:
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()