import os,time,msvcrt

# print('Hi Rabbani@print1')
# time.sleep(5)
# os.system('cls')
# print('Hi Rabbani @ Print 2')

hh=mm=ss=0
while(True):
    os.system('cls')
    print(f'hh:{hh:0>2} mm:{mm:0>2} ss:{ss:0>2}')
    time.sleep(1)
    ss+=1
    if(msvcrt.kbhit()):
        if(msvcrt.getwch()=="Q"):
            os.system('cls')
            ss=0
            break

