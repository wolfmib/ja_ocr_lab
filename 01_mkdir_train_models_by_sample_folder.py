import os


# Pillow
from PIL import Image, ImageFilter
from matplotlib import pyplot
import random


import analyzer_system as ana_sys




if __name__ == "__main__":

        # Obtenir args:
    main_args = ana_sys.analyzer_input_args()

    # Obtenir les information dans la 'sample' foler.
    tem_cmd = 'ls sample'
    tem_response = os.popen(tem_cmd).read()

    # Default language is English: support German, French, Japanese, Korean: german, french, korean, jap')
    if main_args.language == 'fre':
        tem_msg = "[System]: Dans le dossier, vous metez les photos suivantes: "
    elif main_args.language == 'eng':
        tem_msg = "[System]: In folder sample, you put the following information:  "
    elif main_args.language == 'ger':
        tem_msg = "[System]: In Ordner legen Sie die folgenden Fotos:  "
    elif main_args.language == 'jap':
        tem_msg = "[System]: フォルダには、次の写真を入れます"
    elif main_args.language == 'kor':
        tem_msg = "[System]: 폴더에 다음 사진을 넣습니다."
    else:
        print("Error, not support this language setting %s" %main_args.language)


    print(" %s \n %s , type = %s" %(tem_msg,tem_response,type(tem_response)))
    
    # Split String:
        # Rresult:
        # - a.jpg
        # -cherry.jpg
        # -dix.jpg
        # -douze.jpg
        # -house.jpg
        # -kid.jpg
        # -lamp.jpg
        # -onze.jpg
    image_norm_list = tem_response.splitlines()

    # Split .jpg , enregister à list.
    class_norm_list = []
    for any_class in image_norm_list:
        name, _ = any_class.split('.')
        class_norm_list.append(name)

    print(class_norm_list)


    # Faire norm_dicr:
        # map_norm = { 0: 'dix', 1: 'onze', 2: 'cherry',3:'lamp',4:'kid',5:'house',6:'a',7:'douze'}
    map_norm = {index: any_norm for index, any_norm in enumerate(class_norm_list) }
    print(map_norm)


    print("Please remove all the files under train_models ")
    print("Do you clean it (type : y for continue)")
    res = input()

    if res in ['y','Y']:
        pass    
    else:
        print("Error")
    

    for any_norm in class_norm_list:
        # Créer train_models/%s_dir
        mkdir_cmd = 'mkdir train_models/%s_dir'%any_norm
        os.system(mkdir_cmd)

        # Créer train_models/%s_dir/Train
        mkdir_train = 'mkdir train_models/%s_dir/Train'%any_norm
        os.system(mkdir_train)

        # Créer train_moddels/%s_dir/Train/%s or not_%s
        mkdir_train_class = 'mkdir train_models/%s_dir/Train/%s'%(any_norm,any_norm)
        mkdir_train_not_class = 'mkdir train_models/%s_dir/Train/not_%s'%(any_norm,any_norm)
        os.system(mkdir_train_class)
        os.system(mkdir_train_not_class)

        # Créer train_models/%s_dir/Validation
        mkdir_val = 'mkdir train_models/%s_dir/Validation' %any_norm
        os.system(mkdir_val)

        # Créer train_models/%s_dir/Validation/%s or not_%s
        mkdir_val_class = "mkdir train_models/%s_dir/Validation/%s"%(any_norm,any_norm)
        mkdir_val_not_class = "mkdir train_models/%s_dir/Validation/not_%s"%(any_norm,any_norm)
        os.system(mkdir_val_class)
        os.system(mkdir_val_not_class)


        
    