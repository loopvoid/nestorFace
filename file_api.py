import os

def _pre_rename_files(file_dir):
    root = os.walk(file_dir)
    for path,dir,filelist in root:
        for filename in filelist:
            if filename.endswith("jpg"):
                newname0 = "a{}.{}".format(filelist.index(filename), "jpg")
                os.rename(filename, newname0)

            if filename.endswith("png"):
                newname1 = "a{}.{}".format(filelist.index(filename), "png")
                os.rename(filename, newname1)

            if filename.endswith("JPG"):
                newname2 = "a{}.{}".format(filelist.index(filename), "JPG")
                os.rename(filename, newname2)

            if filename.endswith("PNG"):
                newname3 = "a{}.{}".format(filelist.index(filename), "PNG")
                os.rename(filename, newname3)
def _after_rename_files(file_dir):
    root = os.walk(file_dir)
    for path, dir, filelist in root:
        for filename in filelist:
            if filename.endswith("jpg"):
                newname0 = "{}.{}".format(filelist.index(filename), "jpg")
                os.rename(filename, newname0)

            if filename.endswith("png"):
                newname1 = "{}.{}".format(filelist.index(filename), "png")
                os.rename(filename, newname1)

            if filename.endswith("JPG"):
                newname2 = "{}.{}".format(filelist.index(filename), "JPG")
                os.rename(filename, newname2)

            if filename.endswith("PNG"):
                newname3 = "{}.{}".format(filelist.index(filename), "PNG")
                os.rename(filename, newname3)
def rename_files(file_dir):
    try:
        _pre_rename_files(file_dir)
        _after_rename_files(file_dir)
    except Exception as e:
        print(e)

def get_img_list(img_files_dir):
    try:
        root = os.walk(img_files_dir)
        for path,dir,files in root:
            break
        filelist=[]
        for i in files:
            filelist.append(img_files_dir+'\\'+i)
        return(filelist)

    except Exception as e:
        print(e)


def read_all_person(root_dir):
    try:
        name_list = []
        name_dir_list = []

        root = os.walk(root_dir)
        for name, dir, files in root:
            name_dir_list.append(name)

        # remove the root_dir in the name_dir_list
        name_dir_list.remove(name_dir_list[0])

        tmp_name_len_list = []
        for i in range(0, len(name_dir_list)):
            diff_str = len(name_dir_list[i]) - len(root_dir)
            tmp_name_len_list.append(diff_str)

        for j in range(0, len(tmp_name_len_list)):
            order_str = name_dir_list[j]
            name_len = tmp_name_len_list[j] - 4
            name_list.append(order_str[-name_len:])

        # name_list.remove(name_list[0])
        # print(name_list)
        # print(len(name_dir_list))
        return (name_list, name_dir_list)

    except Exception as e:
        print(e)