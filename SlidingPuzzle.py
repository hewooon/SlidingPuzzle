from bangtal import *

from random import randint

import time


setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)

scene = Scene("퍼즐맞추기","Images/배경.png")

main_scene = Scene("퍼즐맞추기","Images/배경.png")

original = Object("Images/인터스텔라-원본.png")
original.locate(scene,0,0)

background = Object("Images/인터스텔라-배경.png")
background.locate(scene,0,0)

pic1 = Object("Images/인터스텔라-1.png")
pic1.locate(scene,280,480)
pic1.i = 0
pic1.j = 0

pic2 = Object("Images/인터스텔라-2.png")
pic2.locate(scene,520,480)
pic2.i = 0
pic2.j = 1

pic3 = Object("Images/인터스텔라-3.png")
pic3.locate(scene,760,480)
pic3.i = 0
pic3.j = 2

pic4 = Object("Images/인터스텔라-4.png")
pic4.locate(scene,280,240)
pic4.i = 1
pic4.j = 0

pic5 = Object("Images/인터스텔라-5.png")
pic5.locate(scene,520,240)
pic5.i = 1
pic5.j = 1

pic6 = Object("Images/인터스텔라-6.png")
pic6.locate(scene,760,240)
pic6.i = 1
pic6.j = 2

pic7 = Object("Images/인터스텔라-7.png")
pic7.locate(scene,280,0)
pic7.i = 2
pic7.j = 0

pic8 = Object("Images/인터스텔라-8.png")
pic8.locate(scene,520,0)
pic8.i = 2
pic8.j = 1

blank = Object("Images/빈칸.png")
blank.x = 760
blank.y = 0
blank.i = 2
blank.j = 2
blank.locate(scene,blank.x,blank.y)

pic = [
    [pic1,pic2,pic3],
    [pic4,pic5,pic6],
    [pic7,pic8,blank]
    ]

picture1 = Object("Images/인터스텔라-원본.png")
picture1.locate(main_scene,180,340)
picture1.setScale(0.25)
picture1.show()

picture2 = Object("Images/공작-원본.png")
picture2.locate(main_scene,520,340)
picture2.setScale(0.25)
picture2.show() 

picture3 = Object("Images/스타워즈-원본.png")
picture3.locate(main_scene,860,340)
picture3.setScale(0.25)
picture3.show() 

record_time=[0]*3
pic_number=0

def picture1_onMouseAction(x,y,action):
    global pic_number
    pic1.setImage("Images/인터스텔라-1.png")
    pic2.setImage("Images/인터스텔라-2.png")
    pic3.setImage("Images/인터스텔라-3.png")
    pic4.setImage("Images/인터스텔라-4.png")
    pic5.setImage("Images/인터스텔라-5.png")
    pic6.setImage("Images/인터스텔라-6.png")
    pic7.setImage("Images/인터스텔라-7.png")
    pic8.setImage("Images/인터스텔라-8.png")
    background.setImage("Images/인터스텔라-배경.png")
    original.setImage("Images/인터스텔라-원본.png")
    picture1.hide()
    picture2.hide()
    picture3.hide()
    record1.hide()
    record2.hide()
    record3.hide()
    scene.enter()
    start_()
    pic_number=0
picture1.onMouseAction = picture1_onMouseAction

def picture2_onMouseAction(x,y,action):
    global pic_number
    pic1.setImage("Images/공작-1.png")
    pic2.setImage("Images/공작-2.png")
    pic3.setImage("Images/공작-3.png")
    pic4.setImage("Images/공작-4.png")
    pic5.setImage("Images/공작-5.png")
    pic6.setImage("Images/공작-6.png")
    pic7.setImage("Images/공작-7.png")
    pic8.setImage("Images/공작-8.png")
    background.setImage("Images/공작-배경.png")
    original.setImage("Images/공작-원본.png")
    picture1.hide()
    picture2.hide()
    picture3.hide()
    record1.hide()
    record2.hide()
    record3.hide()
    scene.enter()
    start_()
    pic_number=1
picture2.onMouseAction = picture2_onMouseAction

def picture3_onMouseAction(x,y,action):
    global pic_number
    pic1.setImage("Images/스타워즈-1.png")
    pic2.setImage("Images/스타워즈-2.png")
    pic3.setImage("Images/스타워즈-3.png")
    pic4.setImage("Images/스타워즈-4.png")
    pic5.setImage("Images/스타워즈-5.png")
    pic6.setImage("Images/스타워즈-6.png")
    pic7.setImage("Images/스타워즈-7.png")
    pic8.setImage("Images/스타워즈-8.png")
    background.setImage("Images/스타워즈-배경.png")
    original.setImage("Images/스타워즈-원본.png")
    picture1.hide()
    picture2.hide()
    picture3.hide()
    record1.hide()
    record2.hide()
    record3.hide()
    scene.enter()
    start_()
    pic_number=2
picture3.onMouseAction = picture3_onMouseAction

restart = Object("Images/restart.png")
restart.setScale(1.3)
restart.locate(scene,570,350)

record1 = Object("Images/record.png")
record1.setScale(1.5)
record1.locate(main_scene,280,260)
record1.show()

record2 = Object("Images/record.png")
record2.setScale(1.5)
record2.locate(main_scene,620,260)
record2.show()

record3 = Object("Images/record.png")
record3.setScale(1.5)
record3.locate(main_scene,960,260)
record3.show()

end = Object("Images/end.png")
end.setScale(1.3)
end.locate(scene,570,250)

main = Object("Images/main.png")
main.setScale(1.3)
main.locate(scene,570,450)

def main_onMouseAction(x,y,action):
    main_scene.enter()
    picture1.show()
    picture2.show()
    picture3.show()
    record1.show()
    record2.show()
    record3.show()
main.onMouseAction = main_onMouseAction

def end_onMouseAction(x,y,action):
    endGame()
end.onMouseAction = end_onMouseAction

def record1_onMouseAction(x,y,action):
    if(record_time[0]==0):
        showMessage("기록 없음")
    else:
        showMessage(format(record_time[0],".2f")+"초")
record1.onMouseAction = record1_onMouseAction

def record2_onMouseAction(x,y,action):
    if(record_time[1]==0):
        showMessage("기록 없음")
    else:
        showMessage(format(record_time[1],".2f")+"초")
record2.onMouseAction = record2_onMouseAction

def record3_onMouseAction(x,y,action):
    if(record_time[2]==0):
        showMessage("기록 없음")
    else:
        showMessage(format(record_time[2],".2f")+"초")
record3.onMouseAction = record3_onMouseAction

def up():
    if (blank.i > 0):
        pic[blank.i][blank.j],pic[blank.i-1][blank.j] = pic[blank.i-1][blank.j],pic[blank.i][blank.j]
        pic[blank.i-1][blank.j].locate(scene,blank.x,blank.y+240)
        pic[blank.i][blank.j].locate(scene,blank.x,blank.y)
        pic[blank.i][blank.j].i = pic[blank.i][blank.j].i+1
        blank.i=blank.i-1
        blank.y=blank.y+240

def down():
    if (blank.i < 2):
        pic[blank.i][blank.j],pic[blank.i+1][blank.j] = pic[blank.i+1][blank.j],pic[blank.i][blank.j]
        pic[blank.i+1][blank.j].locate(scene,blank.x,blank.y-240)
        pic[blank.i][blank.j].locate(scene,blank.x,blank.y)
        pic[blank.i][blank.j].i = pic[blank.i][blank.j].i-1
        blank.i=blank.i+1
        blank.y=blank.y-240

def left():
    if (blank.j > 0):
        pic[blank.i][blank.j],pic[blank.i][blank.j-1] = pic[blank.i][blank.j-1],pic[blank.i][blank.j]
        pic[blank.i][blank.j-1].locate(scene,blank.x-240,blank.y)
        pic[blank.i][blank.j].locate(scene,blank.x,blank.y)
        pic[blank.i][blank.j].j = pic[blank.i][blank.j].j+1
        blank.j=blank.j-1
        blank.x=blank.x-240

def right():
    if (blank.j < 2):
        pic[blank.i][blank.j],pic[blank.i][blank.j+1] = pic[blank.i][blank.j+1],pic[blank.i][blank.j]
        pic[blank.i][blank.j+1].locate(scene,blank.x+240,blank.y)
        pic[blank.i][blank.j].locate(scene,blank.x,blank.y)
        pic[blank.i][blank.j].j = pic[blank.i][blank.j].j-1
        blank.j=blank.j+1
        blank.x=blank.x+240

random_num = randint(500,1000)
count = 0

def shuffle():
    global random_num,count
    while(count<random_num):
        number = randint(1,4)
        if(number == 1):
            up()
        elif(number == 2):
            down()
        elif(number == 3):
            left()
        else:
            right()
        count=count+1

start_time=0
end_time=0

def start_():
    global count, start_time
    background.show()
    restart.hide()
    end.hide()
    main.hide()
    count=0
    shuffle()
    for i in range(3):
        for j in range(3):
            pic[i][j].show()
    start_time = time.time()

def restart_onMouseAction(x, y, action):
    start_()
restart.onMouseAction = restart_onMouseAction 

def finish():
    global start_time, record_time, end_time
    if(pic == [
        [pic1,pic2,pic3],
        [pic4,pic5,pic6],
        [pic7,pic8,blank]
        ]):
        for i in range(3):
            for j in range(3):
                pic[i][j].hide()
        end_time = time.time()
        if(record_time[pic_number]>end_time-start_time or record_time[pic_number] == 0):
            record_time[pic_number]=end_time-start_time
            showMessage(format(end_time - start_time,".2f")+"초 걸렸습니다!"+"\n최고 기록입니다.")
        else:
            showMessage(format(end_time - start_time,".2f")+"초 걸렸습니다!")
        background.hide()
        original.show()
        main.show()
        restart.show()
        end.show()

def pic1_onMouseAction(x,y,action):
    if(pic1.i==blank.i+1 and pic1.j==blank.j):
        down()
    elif(pic1.i==blank.i-1 and pic1.j==blank.j):
        up()
    elif(pic1.j==blank.j+1 and pic1.i==blank.i):
        right()
    elif(pic1.j==blank.j-1 and pic1.i==blank.i):
        left()
    finish()
pic1.onMouseAction = pic1_onMouseAction          

def pic2_onMouseAction(x,y,action):
    if(pic2.i==blank.i+1 and pic2.j==blank.j):
        down()
    elif(pic2.i==blank.i-1 and pic2.j==blank.j):
        up()
    elif(pic2.j==blank.j+1 and pic2.i==blank.i):
        right()
    elif(pic2.j==blank.j-1 and pic2.i==blank.i):
        left()
    finish()
pic2.onMouseAction = pic2_onMouseAction

def pic3_onMouseAction(x,y,action):
    if(pic3.i==blank.i+1 and pic3.j==blank.j):
        down()
    elif(pic3.i==blank.i-1 and pic3.j==blank.j):
        up()
    elif(pic3.j==blank.j+1 and pic3.i==blank.i):
        right()
    elif(pic3.j==blank.j-1 and pic3.i==blank.i):
        left()
    finish()
pic3.onMouseAction = pic3_onMouseAction

def pic4_onMouseAction(x,y,action):
    if(pic4.i==blank.i+1 and pic4.j==blank.j):
        down()
    elif(pic4.i==blank.i-1 and pic4.j==blank.j):
        up()
    elif(pic4.j==blank.j+1 and pic4.i==blank.i):
        right()
    elif(pic4.j==blank.j-1 and pic4.i==blank.i):
        left()
    finish()
pic4.onMouseAction = pic4_onMouseAction

def pic5_onMouseAction(x,y,action):
    if(pic5.i==blank.i+1 and pic5.j==blank.j):
        down()
    elif(pic5.i==blank.i-1 and pic5.j==blank.j):
        up()
    elif(pic5.j==blank.j+1 and pic5.i==blank.i):
        right()
    elif(pic5.j==blank.j-1 and pic5.i==blank.i):
        left()
    finish()
pic5.onMouseAction = pic5_onMouseAction

def pic6_onMouseAction(x,y,action):
    if(pic6.i==blank.i+1 and pic6.j==blank.j):
        down()
    elif(pic6.i==blank.i-1 and pic6.j==blank.j):
        up()
    elif(pic6.j==blank.j+1 and pic6.i==blank.i):
        right()
    elif(pic6.j==blank.j-1 and pic6.i==blank.i):
        left()
    finish()
pic6.onMouseAction = pic6_onMouseAction

def pic7_onMouseAction(x,y,action):
    if(pic7.i==blank.i+1 and pic7.j==blank.j):
        down()
    elif(pic7.i==blank.i-1 and pic7.j==blank.j):
        up()
    elif(pic7.j==blank.j+1 and pic7.i==blank.i):
        right()
    elif(pic7.j==blank.j-1 and pic7.i==blank.i):
        left()
    finish()
pic7.onMouseAction = pic7_onMouseAction

def pic8_onMouseAction(x,y,action):
    if(pic8.i==blank.i+1 and pic8.j==blank.j):
        down()
    elif(pic8.i==blank.i-1 and pic8.j==blank.j):
        up()
    elif(pic8.j==blank.j+1 and pic8.i==blank.i):
        right()
    elif(pic8.j==blank.j-1 and pic8.i==blank.i):
        left()
    finish()
pic8.onMouseAction = pic8_onMouseAction


startGame(main_scene)