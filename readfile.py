import androidhelper
import time
droid = androidhelper.Android()


strb = droid.dialogGetInput('text file to read', 'enter path of file').result

file = open(strb,'r')


def speak(line):
    droid.ttsSpeak(line)
    return

while True:
    
    res, result, ser = droid.ttsIsSpeaking()
    if result is False:   
        line = file.readline()
        if (len(str(line))>0):
           
            print(line)
            speak(line)
        else:
            print('finished')
            break
    else:
        time.sleep(0.01)

file.close()

