import fcntl, struct, array, time

EVIOCRMFF = 0x40044581
EVIOCSFF = 0x40304580
LOG_CLASS_ON = False
TIME_DELTA = 2500

class Vibrate:

    def __init__(self, file):
        self.ff_joy = open(file, "r+")

    def close(self):
        self.ff_joy.close()

    def new_effect(self, strong, weak, length):
        effect = struct.pack('HhHHHHHxHH', 0x50, -1, 0, 0, 0, length, 0, int(strong * 0xFFFF), int(weak * 0xFFFF))
        a = array.array('h', effect)
        fcntl.ioctl(self.ff_joy, EVIOCSFF, a, True)
        return a[1]
        id = a[1]
        return (ev_play, ev_stop)

    def play_efect(self, id):
        if type(id) == tuple or type(id) == list:
            ev_play = ''
            for i in id:
                ev_play = ev_play + struct.pack('LLHHi', 0, 0, 0x15, i, 1)
        else:
            ev_play = struct.pack('LLHHi', 0, 0, 0x15, id, 1)
        self.ff_joy.write(ev_play)
        self.ff_joy.flush()

    def stop_effect(self, id):
        if type(id) == tuple or type(id) == list:
            ev_stop = ''
            for i in id:
                ev_stop = ev_stop + struct.pack('LLHHi', 0, 0, 0x15, i, 0)
        else:
            ev_stop = struct.pack('LLHHi', 0, 0, 0x15, id, 0)
        self.ff_joy.write(ev_stop)
        self.ff_joy.flush()

    def forget_effect(self, id):
        if type(id) == tuple or type(id) == list:
            for i in id:
                fcntl.ioctl(self.ff_joy, EVIOCRMFF, i)
        else:
            fcntl.ioctl(self.ff_joy, EVIOCRMFF, id)

f = Vibrate("/dev/input/event14")
p = f.new_effect(1.0, 1.0, TIME_DELTA )
f.play_efect((p))
time.sleep(TIME_DELTA / 1000.0)
f.stop_effect((p))
f.forget_effect((p))
