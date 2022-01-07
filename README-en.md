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

Download it from [Release](https://github.com/DriCro6663/ymm4-name-converter/releases).

# Overview
This is a program to make the eye and mouth images of slow images downloadable from [nicotalk](http://www.nicotalk.com/charasozai.html) compatible with [YMM3](https://manjubox.net/ymm3/) to [YMM4](http://www.nicotalk.com/charasozai.html).

Download it from [Release](https://github.com/DriCro6663/ymm4-name-converter/releases).

|  YMM3  |   YMM4   | State                     |
| :----: |  :----:  | :----                     |
| 00.png | 00.0.png | Mouth and eyes close      |
| 01.png | 00.1.png | Intermediate frame 1      |
| 02.png | 00.2.png | Intermediate frame 2      |
| 03.png | 00.3.png | Intermediate frame 3      |
| 04.png | 00.4.png | Intermediate frame 4      |
| 05.png | 00.png   | Mouth and eyes open       |

# Usage

0. Download it from [Release](https://github.com/DriCro6663/ymm4-name-converter/releases) and extract the folder.

1. Go to the unzipped folder and slowly put the material folder into the [01-新きつね], [02-QH], and [03-Other] folders.

```
# Example tree
/ymm4-name-converter
|-- 01-新きつね
|   |-- New-Kitune-Alice
|-- 02-QH
|   |-- QH-Reimu
|-- 03-Other
|   |-- Kitune-Seija
|   |   |-- Eyes
|   |   |-- Mouth
|   |   |-- Other
|-- 10-result
|-- dist
|   |-- Y3toY4-name-converter
|   |   |-- 01-新きつね
|   |   |-- 02-QH
|   |   |-- 03-Other
|   |   |-- 10-result
|-- Y3toY4-name-converter.bat <= [Quick Ver.]
|-- Y3toY4-name-converter.exe <= [OneFile Ver.]
```

2. Run [Y3toY4-name-converter.exe] or [Y3toY4-name-converter.bat]. the difference between exe Ver. and bat Ver. is as follows.


* exe: An executable file that includes the modules used. <br>
    Merit: A single executable file. <br>
    Demerit: Execution speed is slower than bat Ver.
* bat: Separate modules and executables for use. <br>
    Merit: Faster execution than exe Ver. <br>
    Demerit: It is associated with a large number of files.

3. After execution, a slow material folder for YMM4 will be created in the [10-results] folder.

```
# Example tree
/ymm4-name-converter
|-- 01-新きつね
|   |-- New-Kitune-Alice
|-- 02-QH
|   |-- QH-Reimu
|-- 03-Other
|   |-- Kitune-Seija
|-- 10-result
|   |-- QH-Reimu-YMM4
|   |-- Kitune-Seija-YMM4
|   |-- New-Kitune-Alice-YMM4
|-- Y3toY4-name-converter.bat <= [Quick Ver.]
|-- Y3toY4-name-converter.exe <= [OneFile Ver.]
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

* 2022/01/07: <br>
Improved one-click name change. <br>
From the folder that supports YMM3, improved to allow one-click renaming [folder that supports YMM4](https://manjubox.net/ymm4/faq/%E7%AB%8B%E3%81%A1%E7%B5%B5%E6%A9%9F%E8%83%BD/%E5%8B%95%E3%81%8F%E7%AB%8B%E3%81%A1%E7%B5%B5%E7%B4%A0%E6%9D%90%E3%81%AE%E4%BD%9C%E3%82%8A%E6%96%B9/)
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