from datetime import datetime
import time
import os


class Logger:

    def __init__(self, loc, rot='h'):
        logs = os.path.join(loc, 'Logs')
        sql = os.path.join (logs, 'SQL')
        debug = os.path.join(logs, 'Debug')
        error = os.path.join(logs, 'Error')

        if not os.path.exists(logs):
            os.makedirs(logs)
            os.makedirs(sql)
            os.makedirs(debug)
            os.makedirs(error)

        else:
            if not os.path.exists(sql): os.makedirs(sql)
            if not os.path.exists(debug): os.makedirs(debug)
            if not os.path.exists(error): os.makedirs(error)

        rots = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 86400,
            'w': 604800
        }
        self.rot = rots[rot]



    def CreateNewFile(self, file):
        pass

    def Error(self, msg):
        pass

    def SQL(self, msg):
        pass

    def Debug(self, msg):
        pass
