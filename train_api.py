import dlib
import numpy as np
import cv2

predictor_model = "./res/shape_predictor_68_face_landmarks.dat"
recognition_model = "./res/dlib_face_recognition_resnet_model_v1.dat"

face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor(predictor_model)
face_rec = dlib.face_recognition_model_v1(recognition_model)


#imput: one image input
#output: face_descriptor_thumb
def _face_detecting(img_str):
    try:
        img = cv2.imread(img_str)
        dets = face_detector(img)
        face_descriptor_thumb = []
        if dets:
            for k, d in enumerate(dets):
                print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                    k, d.left(), d.top(), d.right(), d.bottom()))
                # Get the landmarks/parts for the face in box d.
                shape = shape_predictor(img, d)
                face_descriptor = face_rec.compute_face_descriptor(img, shape)
                face_descriptor_thumb.append(face_descriptor)
        else:
            print("No face in this img!")
        return(face_descriptor_thumb)

    except Exception as e:
        print(e)

def _train(name,faces_file_dir):
    try:
        discriptors_list = []

    except Exception as e:
        print(e)



if __name__ == '__main__':
    faces = _face_detecting("./res/1.png")
    print(faces)


