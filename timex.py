#!/usr/bin/python

import time
import sys
import os

class Timex(object):
    def __init__(self):#, argv):
        import sys
        program = os.path.basename(sys.argv[0])
        args = ' '.join(sys.argv[1:])
        self.cmd = program + ' ' + args

    def start(self):
        self.start_time = time.time()
        self.start_t = time.strftime("%H:%M:%S")
        t = 'start %s\n' % self.start
        return t

    def end(self, msg=''):
        """Get string with time execution, Execution time: 0:00:01.001. 
        Extra `msg` can be added.

        Does not print! `print t.end()`
        """
        self.end_t = time.strftime("%H:%M:%S")
        et = self.secondsToStr(time.time() - self.start_time)
        f = open('timex.log','wa')
        t = 'Execution time: %s %s start: %s end: %s cmd: %s ' % (et, msg, self.start_t, self.end_t, self.cmd)
        f.write(t)
        f.close()
        return t

    def secondsToStr(self, t):
        """
        take from http://stackoverflow.com/questions/1557571/how-to-get-time-of-a-python-program-execution
        """
        return "%d:%02d:%02d.%03d" % \
        reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])

if __name__ == '__main__':
    t = Timex()#sys.argv)
    t.start()
    time.sleep(1)
    print t.end()
