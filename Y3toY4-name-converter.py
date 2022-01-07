# /* Import library */
import numpy as np
import sys
import os
import re
import shutil
import copy

# /*===================================================================================================*/

# /* Constant */
PATH = os.getcwd()
NEW_KITUNE_PATH = os.path.join(PATH, "01-新きつね")
QH_PATH = os.path.join(PATH, "02-QH")
OTHER_PATH = os.path.join(PATH, "03-Other")
OUTPUT_PATH = os.path.join(PATH, "10-result")
YMM4 = "-YMM4"

# Array
Y_FOLDER_ARR = np.array(
    ["顔色", "後", "口", "他", "体", "髪", "眉", "目"], 
    dtype=object
)
# [a: close, b, c: open] -> 0: 正順: 口
# [a: open, b, c: close] -> 1: 逆順: 目
NORMAL_ARR = np.array(
    ["後", "口", "他", "他-ピッケル", "他-メガネ", "他-看板", "他-武器シリーズ", "他-兵科記号"], dtype=object
)
NEW_KITUNE_NORMAL_ARR = np.array(
    [os.path.join(name, num) for name in NORMAL_ARR for num in ["00", "01"]], dtype=object
)
NORMAL_ARR = np.append(NORMAL_ARR, NEW_KITUNE_NORMAL_ARR)
REVERSE_ARR = np.array(
    ["目", "目-どんぐり目", "目-丸目", "目-瞳のある目"], dtype=object
)
NEW_KITUNE_REVERSE_ARR = np.array(
    [os.path.join(name, num) for name in REVERSE_ARR for num in ["00", "01"]], dtype=object
)
REVERSE_ARR = np.append(REVERSE_ARR, NEW_KITUNE_REVERSE_ARR)
IGNORE_ARR = np.array(
    ["顔", "全", "体", "体の差分", "髪", "髪の差分", "眉", "服下", "服上"], dtype=object
)
NEW_KITUNE_IGNORE_ARR = np.array(
    [os.path.join(name, num) for name in IGNORE_ARR for num in ["00", "01"]], dtype=object
)
IGNORE_ARR = np.append(IGNORE_ARR, NEW_KITUNE_IGNORE_ARR)

# Dictionary
NEW_KITUNE_DICT = {
    os.path.join("顔", "00"): "顔色",
    os.path.join("顔", "01"): "顔色",
    os.path.join("後", "00"): "後",
    os.path.join("後", "01"): "後",
    os.path.join("口", "00"): "口",
    os.path.join("口", "01"): "口",
    "全": "体",
    os.path.join("他", "00"): "他",
    os.path.join("他", "01"): "他",
    "体": "体",
    os.path.join("髪", "00"): "髪",
    os.path.join("髪", "01"): "髪",
    os.path.join("眉", "00"): "眉",
    os.path.join("眉", "01"): "眉",
    os.path.join("服下", "00"): "後",
    os.path.join("服下", "01"): "後",
    os.path.join("服上", "00"): "他",
    os.path.join("服上", "01"): "他",
    os.path.join("目", "00"): "目",
    os.path.join("目", "01"): "目",
}
QH_DICT = {
    "顔": "顔色",
    "後": "後",
    "口": "口",
    "全": "体",
    "他": "他",
    "他-ピッケル": "他",
    "他-メガネ": "他",
    "他-看板": "他",
    "他-武器シリーズ": "他",
    "他-兵科記号": "他",
    "体": "体",
    "体の差分": "体",
    "髪": "髪",
    "髪の差分": "髪",
    "服下": "後",
    "服上": "他",
    "眉": "眉",
    "目": "目",
    "目-どんぐり目": "目",
    "目-丸目": "目",
    "目-瞳のある目": "目",
}
OTHER_DICT = {
    "顔": "顔色",
    "後": "後",
    "口": "口",
    "全": "体",
    "他": "他",
    "体": "体",
    "髪": "髪",
    "眉": "眉",
    "服下": "後",
    "服上": "他",
    "目": "目",
}

# /*===================================================================================================*/

# /* Class */
class Converter:
    def __init__(self):
        self.folder_paths = np.array([], dtype=object)
        self.style_arr = np.array([], dtype=object)
        self.load_paths = np.array([NEW_KITUNE_PATH, QH_PATH, OTHER_PATH], dtype=object)
        self.y_names = np.array([], dtype=object)
        self.output_path_arr = np.array([], dtype=object)
    
    def convert(self):
        print("改名を開始します．")
        self.load_folder()
        self.create_folder()
        self.convert_name()
        print("改名完了．")
    
    def load_folder(self):
        # Get a list of file names only
        for path in self.load_paths:
            files = os.listdir(path)
            files_file = [os.path.join(path, f) for f in files if os.path.isdir(os.path.join(path, f))]
            files_file = np.array(files_file, dtype=object)
            self.folder_paths = np.append(self.folder_paths, files_file)
            style = np.array([path]*len(files_file), dtype=object)
            self.style_arr = np.append(self.style_arr, style)
        return self.folder_paths
    
    def create_folder(self):
        y_names = [os.path.splitext(os.path.basename(p))[0] for p in self.folder_paths]
        y_names = np.array(y_names, dtype=object)
        self.y_names = y_names
        for folder_name, y_path, style in zip(y_names, self.folder_paths, self.style_arr):
            output_path = os.path.join(OUTPUT_PATH, folder_name)
            output_path = output_path + YMM4
            if os.path.isdir(output_path):
                shutil.rmtree(output_path) # ディレクトリを中身ごと削除
            if style != QH_PATH:
                shutil.copytree(
                    y_path, output_path, 
                    ignore=shutil.ignore_patterns(*OTHER_DICT.keys()), dirs_exist_ok=True
                )
            elif style == QH_PATH:
                shutil.copytree(
                    y_path, output_path, 
                    ignore=shutil.ignore_patterns(*QH_DICT.keys()), dirs_exist_ok=True
                )
            for sub_name in Y_FOLDER_ARR:
                sub_path = os.path.join(output_path, sub_name)
                os.makedirs(sub_path, exist_ok=True)
                self.output_path_arr = np.append(self.output_path_arr, sub_path)
        return self.output_path_arr
    
    def convert_name(self):
        for y_path, style in zip(self.folder_paths, self.style_arr):
            y_name = os.path.splitext(os.path.basename(y_path))[0]
            print(str(y_name)+" の改名中……")
            # 辞書の選択
            if style == NEW_KITUNE_PATH:
                y_dict = copy.copy(NEW_KITUNE_DICT)
            elif style == QH_PATH:
                y_dict = copy.copy(QH_DICT)
            elif style == OTHER_PATH:
                y_dict = copy.copy(OTHER_DICT)
            # ゆっくりパーツの改名
            for (n, folder_name) in enumerate( y_dict.keys() ):
                target_path = os.path.join(y_path, folder_name)
                output_path = os.path.join(OUTPUT_PATH, y_name)
                output_path = output_path + YMM4
                output_path = os.path.join(output_path, y_dict[folder_name])
                # コピー元のフォルダーが無ければ、コンテニュー
                if not os.path.isdir(target_path):
                    continue
                # folder_name が IGNORE_ARR に含まれているなら、コピー＆コンテニュー
                if folder_name in IGNORE_ARR:
                    if style != NEW_KITUNE_PATH:
                        shutil.copytree(
                            target_path, output_path, dirs_exist_ok=True
                        )
                    elif style == NEW_KITUNE_PATH:
                        # ファイル名読込
                        files = os.listdir(target_path)
                        files = np.array(files, dtype=object)
                        # コピー
                        for file in files:
                            before_path = os.path.join(target_path, file)
                            rename = str(n).zfill(2)+"-"+file # 改変後の名前
                            after_path = os.path.join(output_path, rename)
                            shutil.copy2(before_path, after_path) # Copy file
                    continue
                # ファイル名読込
                files = os.listdir(target_path)
                files = np.array(files, dtype=object)
                # 重複ナンバー抽出　例：["01a", "01b", "02a", "02b"] -> ["01", "02"]
                num_arr = np.array([], dtype=object)
                for file in files:
                    num_str = re.findall(r'^\d+', file)
                    num_arr = np.append(num_str, num_arr)
                num_arr = np.unique(num_arr) # 重複した要素の削除
                # リネーム
                for target_num in num_arr:
                    # EX. ["01a", "01b", "02a", "02b"] -> ["01a", "01b"]
                    convert_list = [ s for s in files if (target_num in re.findall(r'^\d+', s)) ]
                    convert_arr = np.array(convert_list, dtype=object)
                    # 順番入れ替え
                    if folder_name in NORMAL_ARR:
                        convert_arr = np.hstack( (convert_arr[-1], convert_arr[:-1]) )
                    elif folder_name in REVERSE_ARR:
                        c_arr = np.flip(convert_arr[1:])
                        convert_arr = np.hstack( (convert_arr[0], c_arr) )
                    # YMM4 Ver. に対応
                    for i, file in enumerate(convert_arr):
                        ext = os.path.splitext(file)[1] # 拡張子抽出
                        before_path = os.path.join(target_path, file)
                        if i == 0:
                            rename = str(n).zfill(2)+"-"+target_num+ext # 改変後の名前
                            after_path = os.path.join(output_path, rename)
                        elif i != 0:
                            rename = str(n).zfill(2)+"-"+target_num+"."+str(i-1)+ext # 改変後の名前
                            after_path = os.path.join(output_path, rename)
                        shutil.copy2(before_path, after_path) # Copy file

# /*===================================================================================================*/

if __name__ == '__main__':
    converter = Converter()
    converter.convert()