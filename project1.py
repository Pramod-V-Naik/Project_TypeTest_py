import curses
from curses import wrapper
import time

def start(stdscr):
    
    stdscr.clear()
    stdscr.addstr("Do you want to check your typing speed ??")
    stdscr.addstr("\nPress any key to start!!!!!")
    stdscr.refresh()
    stdscr.getkey()


def disp(stdscr , ttext , ctext, wpm=0 , accuracy=0):
      stdscr.addstr(ttext)
      stdscr.addstr(1 , 0 ,f"WPM : {wpm} |Accuracy: {accuracy}")

      for i, char in enumerate(ctext):
        crect = ttext[i]
        colors = curses.color_pair(2)


        if char != crect:
            colors = curses.color_pair(1)

        stdscr.addstr(0 , i ,char,colors)


def calculate_accuracy(ttext, ctext):
    correct_chars = sum(1 for i in range(len(ctext)) if ctext[i] == ttext[i])
    return round((correct_chars / len(ttext)) * 100) if ttext else 0



def wpm(stdscr,ttext):
     
    ctext = []  
    wpm = 0
    accuracy =0
    start_time=time.time()
    stdscr.nodelay(True)

    while True:
        elapsed_time = max(time.time() -start_time ,1)
        wpm =round((len(ctext)/(elapsed_time/60))/5)
        accuracy= calculate_accuracy(ttext,ctext)
        
        stdscr.clear()
        disp(stdscr, ttext ,  ctext, wpm , accuracy)  
        stdscr.refresh()

        if "".join(ctext) == ttext:
            stdscr.nodelay(False)
            break
        try:
            key = stdscr.getkey()


        except:
            continue


        if ord(key)==27:
            break
        
        if key in ("KEY_BACKSPACE",'\b',"\x7f"):
            if len(ctext) > 0:
                ctext.pop()

        elif len(ctext) < len(ttext):
            ctext.append(key)

    return wpm
    return accuracy
            

       
def test(stdscr):
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK )
    curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK )
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK )

    start(stdscr)
    ttext= "Hello world this is soe test text for this app!" 
    user_wpm=wpm(stdscr,ttext)


    if  user_wpm >25:
        stdscr.addstr(2,0,"VERY GOOD,Thank you for completing")
      
    else:
        stdscr.addstr(2,0,"GOOD,Thank you for completing")
    stdscr.refresh()    
    stdscr.getkey()
    
    



wrapper(test)
 