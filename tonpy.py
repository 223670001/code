import cv2

import time

import RPi.GPIO as GPIO

from time import sleep

#トンピーを再生するための関数
def tonpy_sound():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)

    GPIO.output(21, GPIO.HIGH)
    sleep(0.5)

    GPIO.cleanup()

def function():

    #カメラを起動
    cap = cv2.VideoCapture(0)

    #始まりの時間を指定
    start_time = time.time()

    while True:

        #カスケードファイルを準備
        cascade_file = "haarcascade_frontalface_default.xml"

        #カスケードファイルを読み込む
        cascade = cv2.CascadeClassifier(cascade_file)

        #1フレームずつ取得する
        ret, frame = cap.read()

        #左右を反転する
        frame = cv2.flip(frame, 1)

        #取得できない場合は終了
        if not ret:
            break

        #画像を縮小
        frame = cv2.resize(frame, (500, 500))

        #グレイスケールに変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #顔認識を実行
        face_list = cascade.detectMultiScale(gray, minNeighbors=10)

        #顔の部分を四角で囲む
        for (x,y,w,h) in face_list:

            red = (0,0,255)

            #赤色の枠で囲む
            cv2.rectangle(frame, (x,y), (x+w,y+h),red, 1)

        #顔を検出した時，
        if len(face_list) > 0:

            #経過時間を指定する
            end_time = time.time()

            #始まりの時間から経過時間を表示する
            print(end_time-start_time)

            #3秒経過したら，
            if end_time - start_time >= 3:

                #トンピーの再生
                tonpy_sound()

            elif len(face_list) == 0:

                #時間を元に戻す
                start_time = end_time

        #結果を出力
        cv2.imshow("human_body_detect", frame)

        key = cv2.waitKey(1)
        if key == 13:
            break

    cap.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":

    function()
