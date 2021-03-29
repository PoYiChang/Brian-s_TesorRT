# Brian-s_TesorRT
tensorrt_C++

1.tensorrt的部分 我最終於windows上用C++編譯了兩個不同的sample

domo流程
執行bin\sample_fasterRCNN.exe 將會執行data\faster-RCNN中的圖片，對其進行分類，分類結果為人、車、狗、房子
執行bin\sample_mnist.exe 將會執行data\mnist中的圖片，對其進行分類，分類結果為1~10的數字

2.server收client的部分
我這邊本來打算用python完成tensorrt的部分 然後開一個client將結果傳給架好的server
但tesorrt在windows上無法執行python檔 而我手邊沒有多的GPU可以拿來灌linux
我後來嘗試使用vm模擬ubuntu ，結果VM上是讀不到GPU的
所以我這邊只剩下單純可以收發json格式資料的client與server

demom流程
執行server.py後 執行client.py 即可看到與server端使用port 127.0.0.1進行連線
於client端輸入任意字串即可看到server以json格式收到並print出來

3.後續的建立webserver browser 與docker尚未完成





