import curses
from curses import wrapper
import time
import random
# Initialize the module. Allows running different commands




def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "This is the best typing game ever... Better than monkeytype")
    stdscr.addstr(3, 0, "Press 1 for punctuation sentences")
    stdscr.addstr(4, 0, "Press 2 for Non-punctuation sentences")
    stdscr.addstr(6, 0, "Enter your choice: ")
    stdscr.refresh()
    x = stdscr.getkey()  #Used stdscr.getkey() to get user input
    if x == '1':
        wpm_test(stdscr, 'easy')
    elif x == '2':
        wpm_test(stdscr, 'hard')






# Display text over other text thats already there.
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")





    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)




def load_text(level): #this loads the text based on what option you chose 
    filename = "text.txt" if level == 'easy' else "Easytext.txt"
    with open(filename, "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()
    



def wpm_test(stdscr, level): #displays the wpm 
    target_text = load_text(level)
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()




        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        

        if key in ("KEY_BACKSPACE", '\b', "\x7f"): #used to extit the app by pressing esc
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

        





def main(stdscr): #tells us the colors of the text. green is correct, red is wrong, and white is when nothing is typed 
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)





    start_screen(stdscr)
    while True: #shows if you completed the text
        stdscr.addstr(2, 0, "Press escape to exit")
        key = stdscr.getkey()

        if ord(str(key)) == 27:
            break

wrapper(main)
