#traceback模块 跟踪异常返回信息
import traceback
#winsound模块 发出声音 only wma,mp3
import winsound
#引用winform来弹窗
import ctypes 


#蜂鸣
        
def Beep(decibel,milseconds):
    try:
        winsound.Beep(decibel, milseconds);
    except Exception as e:
        print(traceback.print_exc())
#弹窗

def MessageBoxW(title="nothing",content):
    try:
        ctypes.windll.user32.MessageBoxW(0,title,content,0)
    except Exception as e:
        print(traceback.print_exc())


