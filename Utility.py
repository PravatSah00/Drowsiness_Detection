# Calculate the distance between two vector:
def distance(point_1, point_2):
    sqr_sum = 0
    for i, j in zip(point_1, point_2):
        sqr_sum += (i - j)**2
    dist = sqr_sum ** 0.5
    return dist

# Function to denormalize the cordinates:
def denormalize_cordinates(norm_x, norm_y, denorm_w, denorm_h):
    return [norm_x * denorm_w, norm_y * denorm_h]

# Function for calculate eye aspect ration for a particular eye:
def get_EAR(landmarks, refer_index, img_width, img_height):
    cords_points = []
    for i in refer_index:
        landmark = landmarks[i]
        cord = denormalize_cordinates(
            norm_x = landmark.x,
            norm_y = landmark.y,
            denorm_w = img_width,
            denorm_h = img_height
        )
        cords_points.append(cord)

    p2_p6 = distance(cords_points[1], cords_points[5]) ** 2
    p3_p5 = distance(cords_points[2], cords_points[4]) ** 2
    p1_p4 = distance(cords_points[0], cords_points[3]) ** 2

    ear = (p2_p6 + p3_p5) / (2.0 * p1_p4)
    return ear * 10

# Function to get avg ear:
def get_avg_EAR(landmarks, left_eye_inds, right_eye_inds, image_width, image_height):
    ear_left = get_EAR(
        landmarks = landmarks,
        refer_index = left_eye_inds,
        img_width = image_width,
        img_height = image_height
    )
    ear_right = get_EAR(
        landmarks = landmarks,
        refer_index = right_eye_inds,
        img_width = image_width,
        img_height = image_height
    )

    ear_avg = (ear_left + ear_right) / 2.0
    return ear_avg

# Function to get face bounding box:
def get_bounding_box(landmarks, face_inds, image_width, image_height):
    cords_points = []
    for i in face_inds:
        landmark = landmarks[i]
        cord = denormalize_cordinates(
            norm_x = landmark.x,
            norm_y = landmark.y,
            denorm_w = image_width,
            denorm_h = image_height
        )
        cords_points.append(cord)

    return (
        int(cords_points[0][0])-10,
        int(cords_points[1][1]),
        int(cords_points[2][0])+10,
        int(cords_points[3][1])
    )