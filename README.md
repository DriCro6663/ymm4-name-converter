ymm4-name-converter
=====

# はじめに
* [某町の沙路さん](https://note.com/maesato_1/) 様の [kyara-ugoku v1.1](https://www.dropbox.com/s/vwo2xqcn2yr8vjc/kyara-ugoku%20v1.1.zip?dl=1)
* [あいすもなか](https://note.com/icemonaka_note/) 様の [kamui_1.0](https://www.dropbox.com/sh/xzdcneywrigp8xq/AAD8KoaxDJYsWOT2utpaSha0a), [rakugaki_1.0](https://www.dropbox.com/sh/uur70k2lfvf8xbd/AAAlLTGa87nF8E5IStmFJd9Za)

上記の bat ファイルのおかげでゆっくり素材を [YMM4](https://manjubox.net/ymm4/) に対応できました。

略儀ながら、ここに感謝の意を表します。

しかし、「[新きつね式](http://www.nicotalk.com/charasozai_sky.html)」と「[QH 式](https://qhqh123souko.hatenablog.com/entry/2021/09/21/231021)」には対応していなかったため、本プログラムを作成いたしました。

（上記の素晴らしい bat ファイルを完成後に知ったなんて死んでも言えない……）

これから、[YMM4](https://manjubox.net/ymm4/) でゆっくり動画を制作する人たちの助けになれば幸いです。

[Release](https://github.com/DriCro6663/ymm4-name-converter/releases) からダウンロードしてください。

# 概要
[nicotalk](http://www.nicotalk.com/charasozai.html) からダウンロードできるゆっくり画像の目や口の画像を [YMM3](https://manjubox.net/ymm3/) -> [YMM4](https://manjubox.net/ymm4/) に対応させるプログラムです。

[Release](https://github.com/DriCro6663/ymm4-name-converter/releases) からダウンロードしてください。

|  YMM3  |   YMM4   | State                 |
| :----: |  :----:  | :----                 |
| 00.png | 00.0.png | 口や目が閉じた状態    |
| 01.png | 00.1.png | 中間フレーム1         |
| 02.png | 00.2.png | 中間フレーム2         |
| 03.png | 00.3.png | 中間フレーム3         |
| 04.png | 00.4.png | 中間フレーム4         |
| 05.png | 00.png   | 口や目が開いた状態    |

# 使い方
0. [Release](https://github.com/DriCro6663/ymm4-name-converter/releases) からダウンロードしてフォルダを解凍してください。

1. 解凍したフォルダに移動して、[01-新きつね], [02-QH], [03-Other] フォルダにゆっくり素材フォルダを入れてください。

```
# Example tree
/ymm4-name-converter
|-- 01-新きつね
|   |-- 新きつね式ありす
|-- 02-QH
|   |-- QH式博麗霊夢
|-- 03-Other
|   |-- きつね式正邪
|   |   |-- 目
|   |   |-- 口
|   |   |-- その他のフォルダ
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

2. [Y3toY4-name-converter.exe] または、[Y3toY4-name-converter.bat] を実行してください。exe Ver. と bat Ver. の違いは以下の通りです。

* exe Ver.: 使用モジュールを含めた実行ファイル <br>
    利点：単独の実行ファイル <br>
    欠点： bat Ver. よりも実行速度が遅い
* bat Ver.: 使用モジュールと実行ファイルが分かれている <br>
    利点： exe Ver. よりも実行測度が速い <br>
    欠点：大量のファイルと関係付けられている

3. 実行後、[10-result] フォルダに YMM4 用のゆっくり素材フォルダが作成されます。

```
# Example tree
/ymm4-name-converter
|-- 01-新きつね
|   |-- 新きつね式ありす
|-- 02-QH
|   |-- QH式博麗霊夢
|-- 03-Other
|   |-- きつね式正邪
|-- 10-result
|   |-- QH式博麗霊夢-YMM4
|   |-- きつね式正邪-YMM4
|   |-- 新きつね式ありす-YMM4
|-- Y3toY4-name-converter.bat <= [Quick Ver.]
|-- Y3toY4-name-converter.exe <= [OneFile Ver.]
```

# 環境構築
ソースコードを編集したい方は、下記を参考に環境を構築してください。

<details>
    <summary>こちらをクリックしてください</summary>
    <div>　　

## 仮想環境構築
Anaconda Ver.
```
# create virtual env: python ver. 3.8 or higher
conda create --name exepy python=3.8
    - or -
conda create -n pyins

# Active virtual env
conda activate [venv-name]
```

## 使用モジュール

* syy           : 標準ライブラリ
* os            : 標準ライブラリ
* re            : 標準ライブラリ
* shutil        : 標準ライブラリ
* copy          : 標準ライブラリ
* numpy         : 計算拡張ライブラリ
* pyinstaller   : py -> exe に使用

```
conda install -y numpy pyinstaller
    - or -
pip install numpy pyinstaller
```

プロキシ設定が必要な方は、下記を参考に設定してください。
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
    --name          : exe ファイル名の指定
    --onefile       : exe ファイルを１つにまとめる
    --noconsole     : exe 実行時にコンソールの表示を抑制
    --debug all     : デバッグ出力
    --clean         : キャッシュを削除
    --icon          : アイコンファイルのパスを指定

pyinstaller main.py --name [fileName] --onefile --icon [./img/icon.ico] --noconsole
"""
```

</div></details>　　

# 注意

* セキュリティーソフトを導入している場合、保護機能が働く場合があるかもしれません。その場合、一時的に保護機能をオフにするか、本プログラムを検知対象外にした後に再度お試しください。

# 免責事項
本プログラムを使用するために、一時的にセキュリティーソフトの保護機能をオフにしたことで生じた如何なる損失・損害も保証いたしません。

ご了承ください。

また、本プログラムは予告なく配布を終了する場合があります。

# 更新情報

* 2022/01/07: <br>
ワンクリックで改名できるように改良 <br>
YMM3 に対応したフォルダから [YMM4 に対応したフォルダ](https://manjubox.net/ymm4/faq/%E7%AB%8B%E3%81%A1%E7%B5%B5%E6%A9%9F%E8%83%BD/%E5%8B%95%E3%81%8F%E7%AB%8B%E3%81%A1%E7%B5%B5%E7%B4%A0%E6%9D%90%E3%81%AE%E4%BD%9C%E3%82%8A%E6%96%B9/)に出力するように改良
* 2021/12/19: <br>
全ての饅頭に対応・完成・First commit

# 開発者情報

* [Github DriCro6663](https://github.com/DriCro6663)
* [Twitter Dri_Cro_6663](https://twitter.com/Dri_Cro_6663)
* [YouTube ドリクロ -DriCro-](https://www.youtube.com/channel/UCyWgav9wdiPVjYphB7jrWCQ)
* [PieceX DriCro6663](https://www.piecex.com/users/profile/DriCro6663)
* [ドリクロの備忘録](https://dri-cro-6663.jp/)
* dri.cro.6663@gmail.com

# ライセンス

[LICENSE](./LISENCE) ファイルをご確認してください。