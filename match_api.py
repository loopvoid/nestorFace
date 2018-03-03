import dlib
import numpy as np
import cv2
import file_api
import train_api
import database_api


def match_face(target_img_dir, db_dir, threshold_value):
    try:
        target_key_point_list = train_api.face_detecting_no_show_image(target_img_dir)
        name_list = database_api.get_based_face_name_list(db_dir)
        # name_list, name_dir_list = file_api.read_all_person(root_dir)
        # data_base_kp_list = database_api.read_one_tabel_data(name_list[0])
        # print(name_list[0])

        vote_rate_list = []

        for i in range(0, len(name_list)):
            data_base_kp_list = database_api.read_one_table_data(db_dir, name_list[i])
            vote_rate = _get_vote_rate(target_key_point_list, data_base_kp_list, threshold_value)
            vote_rate_list.append(vote_rate)

        name_index = vote_rate_list.index(max(vote_rate_list))
        return name_list[name_index], max(vote_rate_list)
        # print(data_base_kp_list)

        # _get_vote_rate(target_kp_list,data_base_kp_list,threshold_value)
    except Exception as e:
        print(e, "match_image")


def _get_vote_rate(target_kp_list, source_list, threshold_value):
    try:
        distance_list = _get_distance(target_kp_list, source_list)

        vote = 0
        for j in range(0, len(distance_list)):
            if distance_list[j] < threshold_value:
                vote = vote + 1
        vote_rate = vote / len(distance_list)
        return vote_rate
        # print(distance_list)

    except Exception as e:
        print(e, "_get_vote_rate")


def _get_distance(target_kp_list, database_list):
    try:
        distance_list = []
        for i in range(0, len(database_list)):
            distance = np.linalg.norm(np.array(target_kp_list[0]) - np.array(database_list[i]))
            distance_list.append(distance)
        return distance_list

    except Exception as e:
        print(e, "_get_distance")



if __name__ == "__main__":
    match_face("./res/Angelina/20121219035908831.jpg", "./database/face.db", 0.3)
