import datetime
class Logger:

    def __init__(self, loc, rot='h'):
        self.loc = loc
        rots = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 86400
        }
        self.rot = rots[rot]

        error = open(f'{self.loc}/error{datetime.date}{datetime.hour}.log', 'a')
        sql = open(f'{self.loc}/sql/{datetime.date}{datetime.hour}.log', 'a')
        debug = open(f'{self.loc}/debug/{datetime.date}{datetime.hour}.log', 'a')


        self.error = error
        self.sql = sql
        self.debug = debug

        error.close()
        sql.close()
        debug.close()

        self.entries = {
            'error': datetime.now(),
            'sql': datetime.now(),
            'debug': datetime.now()
        }

    def CreateNewFile(self, file):
        if file == 'error':
            error = open(f'{self.loc}/{file}{datetime.date}{datetime.hour}.log', 'a')
            self.error = error
            error.close()
        elif file == 'sql':
            sql = open(f'{self.loc}/{file}{datetime.date}{datetime.hour}.log', 'a')
            self.sql = sql
            sql.close()
        elif file == 'debug':
            debug = open(f'{self.loc}/{file}{datetime.date}{datetime.hour}.log', 'a')
            self.debug = debug
            debug.close()

        self.enties[file] = datetime.now()

    def Error(self, msg):
        if self.entries['error'] + self.rot > datetime.now(): self.CreateNewFile('error')

        self.debug.open()
        self.debug.write(msg)
        self.debug.close()

    def SQL(self, msg):
        if self.entries['sql'] + self.rot > datetime.now(): self.CreateNewFile('sql')

        self.sql.open()
        self.sql.write(msg)
        self.sql.close()

    def Debug(self, msg):
        if self.entries['debug'] + self.rot > datetime.now(): self.CreateNewFile('debug')

        self.debug.open()
        self.debug.write(msg)
        self.debug.close()
