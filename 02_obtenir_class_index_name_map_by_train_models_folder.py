# Pillow
from PIL import Image, ImageFilter
from matplotlib import pyplot
import random
import pandas as pd

import os
import analyzer_system as ana_sys

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
        tem_msg = "[System]: Dans le dossier 'sample' , vous metez les photos suivantes: "
    elif main_args.language == 'eng':
        tem_msg = "[System]: In folder sample, you put the following information:  "
    elif main_args.language == 'ger':
        tem_msg = "[System]: In Ordner sample  legen Sie die folgenden Fotos:  "
    elif main_args.language == 'jap':
        tem_msg = "[System]: sample フォルダには、次の写真を入れます"
    elif main_args.language == 'kor':
        tem_msg = "[System]: sample 폴더에 다음 사진을 넣습니다."
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

    map_norm_reverse = { v:k for k,v in map_norm.items()}
    print(map_norm_reverse)


    # Commencer obtenir les information dans la train_models/%s_dir/Train/
    if main_args.language == 'fre':
        tem_msg = "[System]: Commencer a generer un fichier de carte appelé 'class_index_et_name.csv'  "
    elif main_args.language == 'eng':
        tem_msg = "[System]: Start to generate map file called 'class_index_et_name.csv' "
    elif main_args.language == 'ger':
        tem_msg = "[System]: Starten Sie die Generierung einer Kartendatei mit dem Namen 'class_index_et_name.csv'  "
    elif main_args.language == 'jap':
        tem_msg = "[System]: 'class_index_et_name.csv'という マップファイルの生成を開始します "
    elif main_args.language == 'kor':
        tem_msg = "[System]: 'class_index_et_name.csv'라는 맵 파일을 생성하기 시작합니다"
    else:
        print("Error, not support this language setting %s" %main_args.language)

    print("\n\n#########################\n%s\n\n"%tem_msg)

    index_col = []
    zero_col = []
    un_col   = []

    def __name_conver_boolean(input_class_name, current_name):
        compare_value   = "%s"%input_class_name
        compare_value_2 = "not_%s"%input_class_name
        if current_name == compare_value:
            return True
        elif current_name == compare_value_2:
            return False
        else:
            print("Error: Unexpected current_name = %s"%current_name)


    for any_norm in map_norm_reverse:
        cmd_ls = 'ls train_models/%s_dir/Train'%any_norm
        res = os.popen(cmd_ls).read()
        item_list = res.splitlines()

        # index_col faire ici:
        index_col.append("is_%s"%any_norm)

        for index , item_name in enumerate(item_list):
            print("(index, item_name) = (%d, %s)"%(index,item_name))

            if index == 0:
                tem_true_or_false = __name_conver_boolean(any_norm, item_name)
                zero_col.append(tem_true_or_false)  
            elif index == 1:
                tem_true_or_false = __name_conver_boolean(any_norm, item_name)
                un_col.append(tem_true_or_false)
            else:
                print("[Error]: Unexpected index %d"%index)


    # Save to PD
    index_name_map_df = pd.DataFrame({"class_name":index_col,'class_0':zero_col,'class_1':un_col})

    # Set 'class_name' as inex
    index_name_map_df = index_name_map_df.set_index('class_name')
    print(index_name_map_df)

    # Save to csv
    index_name_map_df.to_csv('class_index_et_name.csv')
