import datetime as dt
class SMBotTimer:

    def __init__(self,default=3600,start="08:00:00",end="20:00:00"):
        """
        Timer object for storing default sleep time and  general playing times.
        :param default: default sleep time between matches
        :param start: start time for bot to play
        :param end:  end time when bot stops playing
        """
        self.default = default
        self.start = dt.datetime.strptime(start, "%H:%M:%S")
        self.end = dt.datetime.strptime(end, "%H:%M:%S")

    def playable(self,time):
        playable = True
        self.start = dt.datetime.combine(time,self.start.time())
        self.end = dt.datetime.combine(time,self.end.time())

        if self.start < self.end:
            playable = time >= self.start and time <= self.end
        else:
            playable = time >= self.start or time <= self.end

        return playable


