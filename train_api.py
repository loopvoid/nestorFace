import dlib
import numpy as np
import cv2
import file_api
from skimage import io

predictor_model = "./model/shape_predictor_68_face_landmarks.dat"
recognition_model = "./model/dlib_face_recognition_resnet_model_v1.dat"

face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor(predictor_model)
face_rec = dlib.face_recognition_model_v1(recognition_model)


# input: one image input
# output: face_descriptor_thumb

def _face_detecting(img_dir):
    try:
        img = cv2.imread(img_dir)
        dets = face_detector(img)
        face_descriptor_thumb = []
        if dets:
            for k, d in enumerate(dets):
                print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                    k, d.left(), d.top(), d.right(), d.bottom()))
                # Get the landmarks/parts for the face in box d.

                wd = dlib.image_window()
                print(img_dir)
                img = io.imread(img_dir)
                dlib.image_window.set_image(wd, img)
                wd.add_overlay(d, dlib.rgb_pixel(255, 0, 0))
                dlib.hit_enter_to_continue()


                shape = shape_predictor(img, d)
                face_descriptor = face_rec.compute_face_descriptor(img, shape)
                face_descriptor_thumb.append(face_descriptor)
        else:
            print("No face in this img!")
        return(face_descriptor_thumb)

    except Exception as e:
        print(e)


def train(name, faces_file_dir):
    try:
        print(name)
        descriptor_list = []
        detected_number = 0
        images_dir_list = file_api.get_img_list(faces_file_dir)
        for img_dir in images_dir_list:
            faces_descriptor_list = _face_detecting(img_dir)
            if faces_descriptor_list:
                for i in range(0, len(faces_descriptor_list)):
                    descriptor_list.append(faces_descriptor_list[i])
                    detected_number += 1
            else:
                pass

        print("Total images: ", len(images_dir_list))
        print("Detected face: ", detected_number)
        print(len(descriptor_list))
        print(len(descriptor_list[0]))
        print(type(descriptor_list[0]))
        print(images_dir_list)

    except Exception as e:
        print(e)


# if __name__ == '__main__':
train("Angelina", "./res/Angelina")



