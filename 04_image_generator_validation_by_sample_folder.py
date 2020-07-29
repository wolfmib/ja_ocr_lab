import os


# Pillow
from PIL import Image, ImageFilter
from matplotlib import pyplot
import random


import analyzer_system as ana_sys


# sample: foler
#  - dix.jpg
#  - onze.jpg
#  - cherry.jpg
#  - lamp.jpg
#  - kid.jpg
#  - house.jpg
#  - a.jpg
#  - douze.jpg




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

    

    # 🎈
    rotate_deg = 5

    # Faire les images , enregister a Validation:
        # -train_models:
        #   -Validation:
        #       - dix:
        #               1.jpg
        #               400.jpg
        #       - not_dix:
        #               1.jpg
        #               400.jpg
    # Créer image agent
    image_agent = ana_sys.image_process_agent()
    for map_index in range(len(map_norm)):

        if main_args.language == 'eng':
            tem_msg = "Start processing task ... \n"
        elif main_args.language == 'fre':
            tem_msg = "Commencer la tâche de traitement ... \n"
        elif main_args.language == 'jap':
            tem_msg = "タスクの処理を開始 ... \n"
        elif main_args.language == 'kor':
            tem_msg = "처리 작업 시작 ... \n"
        else:
            print("[Error]: not support language: %s"%main_args.language)
       
        print("#################\n%s\n"%tem_msg)


        # input norm
        input_name = map_norm[map_index]
        # path = './sample/dix.jpg'
        load_path =  'sample'
        input_file = load_path + "/" + input_name + ".jpg"
        image = Image.open(input_file)  # input_file = 'dix.jpg'
        print("Name:   ", input_name)
        print("format: ", image.format)
        print("mode:   ", image.mode)
        print("size:   ", image.size)  # 158, 152

        # norm
        norm = map_norm[map_index]

        # Clean the folder
        remove_cmd = 'rm -rf train_models/%s_dir/Validation/'%norm
        os.system(remove_cmd)
        print("RemoveClean folder under %s_dir/Validation"%norm)
        
        # Créer the folder
        create_cmd = 'mkdir train_models/%s_dir/Validation'%norm
        os.system(create_cmd)
        create_sub_class_cmd      = 'mkdir train_models/%s_dir/Validation/%s'%(norm,norm)
        create_sub_not_class_cmd  = 'mkdir train_models/%s_dir/Validation/not_%s'%(norm,norm)
        os.system(create_sub_class_cmd)
        os.system(create_sub_not_class_cmd)
        print("Create folder under %s_dir/Validation"%norm)
        check_cmd = 'ls -l train_models/%s_dir/Validation'%norm
        os.system(check_cmd)


        # Save to : train_models/dix_dir -> train_models/%s_dir/Train
        pre_path = "./train_models/%s_dir/Validation" % norm


        # Rotate
        for v in range(250):

            # train_models/dix_dir/Validation/dix/    0-249.jpg
            __saved_path = pre_path + "/%s/%d.jpg"%(norm,v)
            # 🎈
            image_agent.rotate_v1_add_degree(image,__saved_path,rotate_deg,'JPEG')
            

        # Blur
        for v in range(250,325):
            # train_models/dix_dir/Validation/dix/    250-324.jpg
            __saved_path = pre_path + "/%s/%d.jpg"%(norm,v)
            # 🎈
            image_agent.blur_v1_add_degree(image,__saved_path,rotate_deg,'JPEG')
            
        # Cor
        for v in range(325, 400):
            __saved_path = pre_path + "/%s/%d.jpg" % (norm, v)
            # 🎈
            image_agent.cor_v1_tune_low_effect(image, __saved_path, 'JPEG')



    ######################## Pour Train/not_class/500.jpg #######################################
    # Note, for not_class folder,  Total 8 class , 1 itself, only_loop 7 class

    sample_number = 400
    number_of_sample_per_class = sample_number / ( len(map_norm) - 1) # Revmoe itself_class

  

    for any_norm_index in map_norm:

        # Apply tem_apoly_index for each symbol.  
        tem_apply_index = [ v for v in range(len(map_norm))]
        print(tem_apply_index)
        print("-----")
        print(any_norm_index)
        tem_apply_index.remove(any_norm_index)
        print(tem_apply_index)

        # #  ./train_models/dix_dir/Train/not_dix/1.jpg
        not_class_norm = map_norm[any_norm_index]
        __saved_folder = "./train_models/%s_dir/Validation/not_%s"%(not_class_norm,not_class_norm)

        for v in range(sample_number):

            # Obtenir norm:  norm_index = 0, 1, 2, 3, 4, 5, 6  total 8 classes, dans map_norm, remove itself_index = 0
            # tem_apply_index[0] =  1
            # tem_apply_index[1] =  2
            # tem_apply_index[6] =  7 , remove current_index = 0
            norm_index = int(v// number_of_sample_per_class ) 
            norm = map_norm[tem_apply_index[norm_index]]

            # obtenir image: './sample/cherry.jpg'
            norm_image_path = "./sample/%s.jpg"%norm
            __image = Image.open(norm_image_path)

            # method: 0, 1, 2
                # 0: rotate
                # 1: Blur
                # 2: Cor
            obtenir_method = random.randrange(0,3)

            #  ./train_models/dix_dir/Train/not_dix/1.jpg
            __saved_path = __saved_folder + "/" + "%d.jpg"%(v)

            obtenir_method = 0
            if obtenir_method == 0:
                # 🎈
                image_agent.rotate_v1_add_degree(__image,__saved_path,rotate_deg)
            elif obtenir_method == 1:
                # 🎈
                image_agent.blur_v1_add_degree(__image,__saved_path,rotate_deg)
            elif obtenir_method == 2:
                # 🎈
                image_agent.cor_v1_tune_low_effect(__image,__saved_path)
            else:
                print("[Error]: Didn't support this image process method option code %d"%obtenir_method)


            

    

