ymm4-name-converter
=====

# Introduction

I'm not good at English. There may be parts that are difficult to understand. In that case, please feel free to ask me questions.

* [kyara-ugoku v1.1](https://www.dropbox.com/s/vwo2xqcn2yr8vjc/kyara-ugoku%20v1.1.zip?dl=1) by [Saji-san in a certain town](https://note.com/maesato_1/).
* [kamui_1.0](https://www.dropbox.com/sh/xzdcneywrigp8xq/AAD8KoaxDJYsWOT2utpaSha0a) and [rakugaki_1.0](https://www.dropbox.com/sh/uur70k2lfvf8xbd/AAAlLTGa87nF8E5IStmFJd9Za) by [IceMonaka](https://note.com/icemonaka_note/).

Thanks to the above bat files, I was able to make the slow material compatible with [YMM4](https://manjubox.net/ymm4/).

I would like to express my gratitude for the above.

However, it did not support "[new kitune style](http://www.nicotalk.com/charasozai_sky.html)" and "[QH style](https://qhqh123souko.hatenablog.com/entry/2021/09/21/231021)". (I have completed the wonderful bat file above.

(I can't say even if I die that I found out about the above wonderful bat file after it was completed: ......)

I hope it will help people who are making slow videos with [YMM4](https://manjubox.net/ymm4/).

# Overview
This is a program to make the eye and mouth images of slow images downloadable from [nicotalk](http://www.nicotalk.com/charasozai.html) compatible with [YMM3](https://manjubox.net/ymm3/) to [YMM4](http://www.nicotalk.com/charasozai.html).

|  YMM3  |   YMM4   | State                     |
| :----: |  :----:  | :----                     |
| 00.png | 00.0.png | Mouth and eyes close      |
| 01.png | 00.1.png | Intermediate frame 1      |
| 02.png | 00.2.png | Intermediate frame 2      |
| 03.png | 00.3.png | Intermediate frame 3      |
| 04.png | 00.4.png | Intermediate frame 4      |
| 05.png | 00.png   | Mouth and eyes open       |

# Usage

1. Move Y3toY4-name-converter.exe to the directory where the slow folder is located.

````
# Example tree
/Chara's
|-- QH-style_Hakurei_Reimu
|-- Kitune-style_Seija
|   |-- Eyes
|   |-- Mouth
|   |-- Other_folders
|-- New-Kitune-style-Alice
|-- Y3toY4-name-converter.exe
````

2. Run Y3toY4-name-converter.exe. When it is executed, the following string will be output. Please select the folder to be used for YMM4 by using numbers.

```
# Example
Current directory: D:\Chara's

YMM4 に対応させるフォルダ名を選んでください．
Select the folder name that corresponds to YMM4.
00: QH-style_Hakurei_Reimu
01: Kitune-style_Seija
02: New-Kitune-style-Alice

数字を入力して下さい．
Please enter a number.
Ex. 1 or 01:
```

3. After selecting a folder, select the type of slow. If it is not "New Fox" or "QH", select "00: Original".

```
# Example
数字を入力して下さい．
Please enter a number.
Ex. 1 or 01: 1
[Kitune-style_Seija] を選択しました．
Select [Kitune-style_Seija]

改名するゆっくりのタイプを選択してください．
Select the Yukkuri type of renaming.

00: 元祖　　　　: Original
01: 新きつね式　: New Kitune Type
02: QH式　　　　: QH Type

数字を入力して下さい．
Please enter a number.
Ex. 1 or 01:
```

4. After entering the numbers, if there are no problems with the conditions, the renaming of the file will begin.

```
# Example
数字を入力して下さい．
Please enter a number.
Ex. 1 or 01: 0
[元祖: Original] を選択しました．
Select [元祖: Original]

改名を開始します．
Start renaming.
改名完了
Renaming completed.
```

5. After the process is complete, "Selected_folder_name-YMM4" will be created.

```
# Example tree
/Chara's
|-- QH-style_Hakurei_Reimu
|-- Kitune-style_Seija
|-- Kitune-style_Seija-YMM4
|-- New-Kitune-style-Alice
|-- Y3toY4-name-converter.exe
```

# BuildTheEnvironment
If you want to edit the source code, please refer to the following to build the environment.

<details>
    <summary>Click here</summary>
    <div>　　

## Virtual environment construction
Anaconda Ver.
```
# create virtual env: python ver. 3.8 or higher
conda create --name exepy python=3.8
    - or -
conda create -n pyins

# Active virtual env
conda activate [venv-name]
```

## Required modules

* syy           : Standard library
* os            : Standard library
* re            : Standard library
* shutil        : Standard library
* copy          : Standard library
* numpy         : Computational Extension Library
* pyinstaller   : py -> exe

```
conda install -y numpy pyinstaller
    - or -
pip install numpy pyinstaller
```

If you need to set up a proxy, please refer to the following.
```
# windows
# if you need to use proxy, please set proxy setting.
set HTTP_PROXY=http://<userid>:<password>@<server-address>:<port>
set HTTPS_PROXY=http://<userid>:<password>@<server-address>:<port>

# example
set HTTP_PROXY=http://proxy.example.com:8080
set HTTPS_PROXY=http://proxy.example.com:8080

# check proxy
echo %HTTP_PROXY%
echo %HTTPS_PROXY%
```

## py -> exe
```
# Example
pyinstaller main.py --onefile

"""
    --name          : Specify the name of the exe file
    --onefile       : Combine all exe files into one
    --noconsole     : Suppress console display when running exe
    --debug all     : Debug output
    --clean         : Delete the cache
    --icon          : Specify the path of the icon file

pyinstaller main.py --name [fileName] --onefile --icon [./img/icon.ico] --noconsole
"""
```

</div></details>　　

# Note

* If you have installed security software, the protection function may be activated in some cases. In that case, please temporarily turn off the protection function or exclude this program from detection, and then try again.

# Disclaimer
I do not guarantee any loss or damage caused by temporarily turning off the protection function of your security software in order to use this program.

Please be aware of this.

The distribution of this program may be terminated without notice.

# Updates

* 2021/12/19: <br>
For all buns, completed and First commit

# Developer Information

* [Github DriCro6663](https://github.com/DriCro6663)
* [Twitter Dri_Cro_6663](https://twitter.com/Dri_Cro_6663)
* [YouTube -DriCro-](https://www.youtube.com/channel/UCyWgav9wdiPVjYphB7jrWCQ)
* [PieceX DriCro6663](https://www.piecex.com/users/profile/DriCro6663)
* [Dri-Cro's Memorandum](https://dri-cro-6663.jp/)
* dri.cro.6663@gmail.com

# License

Please check the [LICENSE](./LICENSE) file.