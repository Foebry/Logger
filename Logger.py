from datetime import datetime
import datetime
import time
import os


class Logger:

    def __init__(self, loc, rot='h'):
        self.path = os.path.join(loc, 'Logs')
        self.rot = rot

        if not os.path.exists(self.path):
            os.makedirs('Logs')

        self.files = {
            'SQL': None,
            'Debug': None,
            'Error': None
        }

        self.timings = {
            'SQL': None,
            'Debug': None,
            'Error': None
        }

        sql = f'{self.path}//SQL'
        debug = f'{self.path}//Debug'
        error = f'{self.path}//Error'

        if os.path.exists(f'{self.path}//SQL') and len(os.listdir(sql)) >= 1: self.files['SQL'] = max(os.listdir(sql))
        if os.path.exists(f'{self.path}//Debug') and len(os.listdir(debug)) >= 1: self.files['Debug'] = max(os.listdir(debug))
        if os.path.exists(f'{self.path}//Error') and len(os.listdir(error)) >= 1: self.files['Error'] = max(os.listdir(error))


    def CreateNewFile(self, file):
        dir = os.path.join(self.path, file)
        if not os.path.exists(dir): os.makedirs(dir)

        if self.rot == 'w': filename = f'Week {datetime.date(2021, 3, 5).strftime("%V")}.log'
        elif self.rot == 'd': filename = f'{datetime.datetime.now().date()}.log'
        elif self.rot == 'h': filename = f'{datetime.datetime.now().date()}_{datetime.datetime.now().hour}h.log'
        elif self.rot == 'm': filename = f'{datetime.datetime.now().date()}_{datetime.datetime.now().hour}h_{datetime.datetime.now().minute}m.log'
        elif self.rot == 's': filename = f'{datetime.datetime.now().date()}_{datetime.datetime.now().hour}h_{datetime.datetime.now().minute}m_{datetime.datetime.now().second}s.log'

        self.files[file] = os.path.join(self.path, file, filename)
        temp = open(self.files[file], 'a')
        temp.close()
        self.timings[file] = datetime.datetime.now()

    def write(self, file, msg):
        self.IsValidTimeFrame(file)
        temp = open(self.files[file], 'a')
        temp.write(f'{datetime.datetime.now()} - {msg}')
        temp.close()

    def IsValidTimeFrame(self, file):

        if self.files[file] is None: self.CreateNewFile(file)
        else:
            pass
