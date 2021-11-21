import time
class PomodoroTimer:
    def __init__(self):
        self.focus = False
        # defining time for each pomodoro focus (25 min) in seconds
        self.pomodoroTime = 25*60

    def timer(self):
        while (not self.pomodoroTime == 0) and (not self.focus == False): 
            if(self.focus == True):
                mins = self.pomodoroTime // 60
                secs = self.pomodoroTime % 60
                return('{:02d}:{:02d}'.format(mins, secs))
                time.sleep(1)
                self.pomodoroTime -= 1
            else:
                break

    def stop_timer(self):
        self.focus = False
        print(self.focus)

    def start_timer(self):
        self.focus = True
        timer(self)

