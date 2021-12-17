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

# 概要
[nicotalk](http://www.nicotalk.com/charasozai.html) からダウンロードできるゆっくり画像の目や口の画像を [YMM3](https://manjubox.net/ymm3/) -> [YMM4](https://manjubox.net/ymm4/) に対応させるプログラムです。

|  YMM3  |   YMM4   | State                 |
| :----: |  :----:  | :----                 |
| 00.png | 00.0.png | 口や目が閉じた状態    |
| 01.png | 00.1.png | 中間フレーム1         |
| 02.png | 00.2.png | 中間フレーム2         |
| 03.png | 00.3.png | 中間フレーム3         |
| 04.png | 00.4.png | 中間フレーム4         |
| 05.png | 00.png   | 口や目が開いた状態    |

# 使い方
1. Y3toY4-name-converter.exe を、ゆっくりフォルダがあるディレクトリに移動させてください。

```
# Example tree
/Chara's
|-- QH式博麗霊夢
|-- きつね式正邪
|   |-- 目
|   |-- 口
|   |-- その他のフォルダ
|-- 新きつね式ありす
|-- Y3toY4-name-converter.exe
```

2. Y3toY4-name-converter.exe を実行してください。実行すると以下のような文字列が出力されますので、YMM4 に対応させるフォルダを数字で選択してください。

```
# Example
Current directory: D:\Chara's

YMM4 に対応させるフォルダ名を選んでください．
Select the folder name that corresponds to YMM4.
00: QH式博麗霊夢
01: きつね式正邪
02: 新きつね式ありす

数字を入力して下さい．
Please enter a number.
Ex. 1 or 01:
```

3. フォルダを選択後、ゆっくりのタイプを選んでください。「新きつね式」・「QH 式」以外であれば、「00: 元祖: Original」を選択してください。

```
# Example
数字を入力して下さい．
Please enter a number.
Ex. 1 or 01: 1
[きつね式正邪] を選択しました．
Select [きつね式正邪]

改名するゆっくりのタイプを選択してください．
Select the Yukkuri type of renaming.

00: 元祖　　　　: Original
01: 新きつね式　: New Kitune Type
02: QH式　　　　: QH Type

数字を入力して下さい．
Please enter a number.
Ex. 1 or 01:
```

4. 数字を入力後、条件に問題が無ければ、ファイル名の改名が始まります。

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

5. 処理完了後、「選択したフォルダ名-YMM4」が作成されます。

```
# Example tree
/Chara's
|-- QH式博麗霊夢
|-- きつね式正邪
|-- きつね式正邪-YMM4
|-- 新きつね式ありす
|-- Y3toY4-name-converter.exe
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