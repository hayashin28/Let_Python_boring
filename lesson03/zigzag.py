import time, sys

indent = 0 # インデント(字下げ)の幅
indent_increasing = True # インデントの幅が増えているか否か

try:
    while True: # メインプログラムのループ
        print(' ' * indent, end = '')
        print('********')
        time.sleep(0.1) # 0.1秒間止める
        
        if indent_increasing:
            # インデントを増やす
            indent = indent + 1
            if indent == 20:
                # 方向を変える
                indent_increasing = False
        else:
            # インデントを減らす
            indent = indent - 1
            if indent == 0:
                # 方向を変える
                indent_increasing = True

# キーボードから停止信号を受け取る
except KeyboardInterrupt:
    sys.exit() # プログラムを終了する