from microbit import *

#Dictionary containing Morse Code letter & number translations

translation={
    "DoDa":"A",
    "DaDoDoDo":"B",
    "DaDoDaDo":"C",
    "DaDoDo":"D",
    "Do":"E",
    "DoDoDaDo":"F",
    "DaDaDo":"G",
    "DoDoDoDo":"H",
    "DoDo":"I",
    "DoDaDaDa":"J",
    "DaDoDa":"K",
    "DoDaDoDo":"L",
    "DaDa":"M",
    "DaDo":"N",
    "DaDaDa":"O",
    "DoDaDaDo":"P",
    "DaDaDoDa":"Q",
    "DoDaDo":"R",
    "DoDoDo":"S",
    "Da":"T",
    "DoDoDa":"U",
    "DoDoDoDa":"V",
    "DoDaDa":"W",
    "DaDoDoDa":"X",
    "DaDoDaDa":"Y",
    "DaDaDoDo":"Z",
    "DoDaDaDaDa":"1",
    "DoDoDaDaDa":"2",
    "DoDoDoDaDa":"3",
    "DoDoDoDoDa":"4",
    "DoDoDoDoDo":"5",
    "DaDoDoDoDo":"6",
    "DaDaDoDoDo":"7",
    "DaDaDaDoDo":"8",
    "DaDaDaDaDo":"9",
    "DaDaDaDaDa":"0",
    }

#Button Values & Totals

buttonA = 'Do'
buttonB = 'Da'
runningTotal = ''

#Core Code

while True:

#This code will recognise that you have pressed the A button on the micro:bit, 
#which indicates that you want to add 'Do' to the runningTotal

    if button_a.is_pressed():
        runningTotal = runningTotal + buttonA
        sleep(200)

#This code will recognise that you have pressed the B button on the micro:bit, 
#which indicates that you want to add 'Da' to the runningTotal

    elif button_b.is_pressed():
        runningTotal = runningTotal + buttonB
        sleep(200)

#This code will recognise that you have shaken the micro:bit, which indicates that you want to 
#translate (via the translation Dictionary) the DOs and DAs collected in this session and display
#the ascocaited digit on the Micro:bit screen
#If an invalid combination of DOs and DAs is entered it will display a sad face on the Micro:bit screen
#In both cases it will reset the 'runningTotal'

    elif accelerometer.was_gesture("shake"):
        if runningTotal in translation:
            display.show(translation.get(runningTotal))
            sleep(2000)
            runningTotal = ''
        else:
            display.show(Image.SAD)
            sleep(2000)
            runningTotal = ''

#This code will recognise that you have touched pin0 & pinGND on the micro:bit, 
#which indiactes that you have made a mistake and want to reset
#It will reset the 'runningTotal', and also display a tick in the LEDs as a visual confirmation

    elif pin0.is_touched():
        runningTotal = ''
        display.show(Image.YES)

#If none of the above are happening... This code will ensure the display remains blank

    else:
        display.clear()
