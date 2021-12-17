# /* Import library */
import numpy as np
import sys
import os
import re
import shutil
import copy

# /*===================================================================================================*/

# /* Constant */
AUTHENTIC_ORDER = 0
REVERSE_ORDER = 1

# Yukkuri Type
ORIGINAL            = "元祖　　　　: Original"
KITUNE              = "きつね式　　: Kitune Type"
NEW_KITUNE          = "新きつね式　: New Kitune Type"
FULL_BODY_KITUNE    = "全身きつね式: Full body Kitune Type"
KAMUI               = "神威式　　　: Kamui Type"
RAKUGAKI            = "らくがき式　: Rakugaki Type"
WATASHI             = "私式。　　　: Watashi Type"
PUNI                = "ぷに式　　　: Puni Type"
QH                  = "QH式　　　　: QH Type"
NININON             = "弐ヶのん式　: Nininon Type"
TORIMISO            = "とりみそ式　: ToriMiso Type"
MIKAN               = "みかん式　　: Mikan Type"
KURO                = "クロ式　　　: Kuro Type"
HACHI               = "蜂旧式　　　: Hachi Type"

# Vector [eye, mouth]
# [a: close, b, c: open] -> 0: 正順: 口
# [a: open, b, c: close] -> 1: 逆順: 目
ORIGINAL_VECTOR = np.array([REVERSE_ORDER, AUTHENTIC_ORDER], dtype=np.uint8)
KITUNE_VECTOR = np.array([REVERSE_ORDER, AUTHENTIC_ORDER], dtype=np.uint8)
NEW_KITUNE_VECTOR = np.array([
    REVERSE_ORDER, REVERSE_ORDER, AUTHENTIC_ORDER, AUTHENTIC_ORDER
], dtype=np.uint8) # special
FULL_BODY_VECTOR = np.array([REVERSE_ORDER, AUTHENTIC_ORDER], dtype=np.uint8)
KAMUI_VECTOR = np.array([REVERSE_ORDER, AUTHENTIC_ORDER], dtype=np.uint8)
RAKUGAKI_VECTOR = np.array([REVERSE_ORDER, AUTHENTIC_ORDER], dtype=np.uint8)
WATASHI_VECTOR = np.array([REVERSE_ORDER, AUTHENTIC_ORDER], dtype=np.uint8)
PUNI_VECTOR = np.array([REVERSE_ORDER, AUTHENTIC_ORDER], dtype=np.uint8)
QH_VECTOR = np.array([
    REVERSE_ORDER, AUTHENTIC_ORDER, 
    REVERSE_ORDER, REVERSE_ORDER, 
    REVERSE_ORDER
], dtype=np.uint8) # special
NININON_VECTOR = np.array([REVERSE_ORDER, AUTHENTIC_ORDER], dtype=np.uint8)
TORIMISO_VECTOR = np.array([REVERSE_ORDER, AUTHENTIC_ORDER], dtype=np.uint8)
MIKAN_VECTOR = np.array([REVERSE_ORDER, AUTHENTIC_ORDER], dtype=np.uint8)
KURO_VECTOR = np.array([REVERSE_ORDER, AUTHENTIC_ORDER], dtype=np.uint8)
HACHI_VECTOR = np.array([REVERSE_ORDER, AUTHENTIC_ORDER], dtype=np.uint8)

# List
FOLDER_LIST = np.array(["目", "口"], dtype=object)
FOLDER_LIST_NEW_KITUNE = np.array(
    [os.path.join(name, num) for name in FOLDER_LIST for num in ["00", "01"]], dtype=object
)
FOLDER_LIST_QH = np.array(["目", "口", "目-どんぐり目", "目-丸目", "目-瞳のある目"], dtype=object)
Y_TYPE_LIST = np.array([
    ORIGINAL,
    NEW_KITUNE,
    QH
], dtype=object)

# Dictionary
Y_VECTOR_DICT = {
    KAMUI: KAMUI_VECTOR,
    RAKUGAKI: RAKUGAKI_VECTOR,
    WATASHI: WATASHI_VECTOR, 
    NEW_KITUNE: NEW_KITUNE_VECTOR, 
    PUNI: PUNI_VECTOR,
    KITUNE: KITUNE_VECTOR,
    FULL_BODY_KITUNE: FULL_BODY_KITUNE,
    ORIGINAL:ORIGINAL_VECTOR, 
    QH: QH_VECTOR, 
    NININON: NININON_VECTOR, 
    TORIMISO: TORIMISO_VECTOR, 
    MIKAN: MIKAN_VECTOR, 
    KURO: KURO_VECTOR, 
    HACHI: HACHI_VECTOR
}

# /*===================================================================================================*/

# /* Class */
class Converter:
    def __init__(self, path, name, vector_arr, type):
        self.type = type
        self.path = path
        self.name = name
        self.vector_arr = vector_arr
    
    def folder_copy(self):
        if self.type == QH:
            self.folder_copy_main(
                path=self.path, name=self.path, 
                folder_list=FOLDER_LIST_QH
            )
        else:
            self.folder_copy_main(
                path=self.path, name=self.path, 
                folder_list=FOLDER_LIST
            )
    
    def folder_copy_main(self, path, name, folder_list):
        folder_path = os.path.join(path, name)
        new_folder_path = os.path.join(path, name+"-YMM4")
        if os.path.isdir(new_folder_path):
            shutil.rmtree(new_folder_path) # ディレクトリを中身ごと削除
        shutil.copytree(
            folder_path, new_folder_path, 
            ignore=shutil.ignore_patterns(*folder_list), dirs_exist_ok=True
        )
    
    def convert(self):
        print("改名を開始します．\nStart renaming.")
        if self.type == NEW_KITUNE:
            self.convert_name(
                path=self.path, name=self.name, 
                vector_arr=self.vector_arr, folder_list=FOLDER_LIST_NEW_KITUNE
            )
        elif self.type == QH:
            self.convert_name(
                path=self.path, name=self.name, 
                vector_arr=self.vector_arr, folder_list=FOLDER_LIST_QH
            )
        else:
            self.convert_name(
                path=self.path, name=self.name, 
                vector_arr=self.vector_arr, folder_list=FOLDER_LIST
            )
        print("改名完了\nRenaming completed.")
    
    def convert_name(self, path, name, vector_arr, folder_list):
        original_name = copy.copy(name)
        for folder_name, vector in zip(folder_list, vector_arr):
            target_path = os.path.join(path, folder_name)
            new_folder_path = target_path.replace(original_name, original_name+"-YMM4")
            # 改変後のフォルダー作成
            if os.path.isdir(new_folder_path):
                shutil.rmtree(new_folder_path) # ディレクトリを中身ごと削除
            elif not os.path.isdir(new_folder_path):
                os.makedirs(new_folder_path) # ディレクトリの作成
            # ファイル名読込
            files = os.listdir(target_path)
            files = np.array(files, dtype=object)
            # 重複ナンバー抽出　例：["01a", "01b", "02a", "02b"] -> ["01", "02"]
            num_arr = np.array([], dtype=object)
            for file in files:
                num_str = re.sub(r"\D", "", file)
                num_arr = np.append(num_str, num_arr)
            num_arr = np.unique(num_arr) # 重複した要素の削除
            # リネーム
            for target_num in num_arr:
                # EX. ["01a", "01b", "02a", "02b"] -> ["01a", "01b"]
                convert_list = [ s for s in files if re.sub(r"\D", "", s)==target_num ]
                convert_arr = np.array(convert_list, dtype=object)
                # 順番入れ替え
                if vector == AUTHENTIC_ORDER:
                    convert_arr = np.hstack( (convert_arr[-1], convert_arr[:-1]) )
                elif vector == REVERSE_ORDER:
                    c_arr = np.flip(convert_arr[1:])
                    convert_arr = np.hstack( (convert_arr[0], c_arr) )
                for i, file in enumerate(convert_arr):
                    ext = os.path.splitext(file)[1] # 拡張子抽出
                    before_path = os.path.join(target_path, file)
                    if i == 0:
                        rename = target_num+ext # 改変後の名前
                        after_path = os.path.join(new_folder_path, rename)
                    elif i != 0:
                        rename = target_num+"."+str(i-1)+ext # 改変後の名前
                        after_path = os.path.join(new_folder_path, rename)
                    shutil.copy2(before_path, after_path) # Copy file

# /*===================================================================================================*/

# /* Function */
def get_folder_name(path):
    files = os.listdir(path)
    files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
    files_dir = np.array(files_dir, dtype=object)
    return files_dir

def select_folder(folders):
    print("YMM4 に対応させるフォルダ名を選んでください．")
    print("Select the folder name that corresponds to YMM4.")
    for i in range(len(folders)):
        print("0"+str(i)+": "+folders[i])
    folder_str = input("\n数字を入力して下さい．\nPlease enter a number.\nEx. 1 or 01: ")
    is_number(string=folder_str)
    folder_n = int(folder_str)
    is_corresponding_number(target=folder_n, search_arr=folders)
    print("["+folders[folder_n]+"] を選択しました．\nSelect ["+folders[folder_n]+"]\n")
    
    return folders[folder_n]

def is_number(string):
    if( not string.isdigit() ):
        print("入力に文字が検出されました．")
        print("数字のみを入力してください．")
        print("A character was detected in the input.")
        print("Please enter numbers only.")
        
        input("\nPress any key to exit.")
        
        sys.exit()

def is_corresponding_number(target, search_arr):
    if ( not target in range(len(search_arr))):
        print("対応されていない数字が入力されました．")
        print("対応する数字を入力してください．")
        print("An unsupported number has been entered.")
        print("Please enter the corresponding number.")
        
        input("\nPress any key to exit.")
        
        sys.exit()

def select_type():
    print("改名するゆっくりのタイプを選択してください．")
    print("Select the Yukkuri type of renaming.\n")
    for i, yukkuri in enumerate(Y_TYPE_LIST):
        print("0"+str(i)+": "+yukkuri)
    y_str = input("\n数字を入力して下さい．\nPlease enter a number.\nEx. 1 or 01: ")
    is_number(string=y_str)
    y_num = int(y_str)
    is_corresponding_number(target=y_num, search_arr=Y_TYPE_LIST)
    type_result = Y_TYPE_LIST[y_num].replace("　", "")
    print("["+type_result+"] を選択しました．\nSelect ["+type_result+"]\n")
    vector = Y_VECTOR_DICT[Y_TYPE_LIST[y_num]]
    return (vector, Y_TYPE_LIST[y_num])

def main():
    # 現在のディレクトリ取得
    cur_path = os.getcwd()
    print("Current directory: "+cur_path+"\n")
    # 改名するフォルダの選択
    folders = get_folder_name(path=cur_path)
    folder_name = select_folder(folders=folders)
    folder_path = os.path.join(cur_path, folder_name)
    # ゆっくりのタイプ選択
    vector_arr, y_type = select_type()
    # 改名処理
    converter = Converter(type=y_type, path=folder_path, name=folder_name, vector_arr=vector_arr)
    converter.folder_copy()
    converter.convert()

# /*===================================================================================================*/

if __name__ == '__main__':
    main()