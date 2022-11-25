## Raspberrypiを使って、いびきを予防する作品を作ってみた

<img src="https://user-images.githubusercontent.com/117970552/203920740-0466a280-94ab-432c-865d-ec8db3b8e0a0.jpg" width="60%">
### 目的
家族のいびきがうるさくて眠れない日々…
いびきは仰向けで寝ると舌が喉の奥に下がり気道が圧迫され、かきやすくなります。
そのため、就寝中の頭上に赤外線カメラを設置し、顔認識した際に音を鳴らすことで、いびきを予防・防止する作品を作成しました。なお、音を鳴らす機能はこぐまのトンピーを使用します。

### 準備する物

- Raspberry Pi4 ModeB
- こぐまのトンピー
- MOSFET
- ブレッドボード
- ワニ口クリップ
- 抵抗(220Ω)
- 電池ボックス(単3電池2本)
- ジャンパー線
- フレキシブルスマホアーム(ダイソー)

### ①こぐまのトンピーの下処理
(1)こぐまのトンピーを丸太から外して端子を取り出す

[参照ページ][tonpy1]

[tonpy1]: https://fabcross.jp/category/make/mobility/20220609_bunkai_tonpy.html
(2)こぐまのトンピーをRaspberrypiに連携する<br>(ブレッドボードの回路を作成、コードでは22番のポートを使用)
  
[参照ページ][tonpy2]

[tonpy2]: https://dotstud.io/blog/arduino-nodejs-twitter-connect/

### ②赤外線カメラの動作確認

就寝中に赤外線カメラを用いて顔認識を行うため、暗闇下でも動作確認を行う

[参照ページ][camera]

[camera]: https://tora-k.com/2020/11/15/raspberrypi4-cammoj/

### ③コードの作成
(1)OpenCVをインストールする
```
# パッケージを最新にする
$ sudo apt-get update
$ sudo apt-get upgrade

# OpenCVをインストール
$ pip3 install opencv-python

# 実行時に必要となるライブラリをインストール
$ sudo apt-get install libatlas-base-dev
$ sudo apt-get install libjasper-dev
```
(2)コードを記述する

### ④Raspberrypiをスマホスタンドに設置する
完成!!!

<img src="https://user-images.githubusercontent.com/117970552/203917232-908aeadc-7b43-46c1-bbc3-e13d533745c3.JPG" width="30%">



