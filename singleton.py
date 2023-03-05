#  singleton
class SingleConnection:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        SingleConnection.__instance = None

    def __init__(self, login=None, passwrd=None, port=None):
        print('magic method __init__', self)
        self.login = login
        self.passwrd = passwrd
        self.port = port

    def connect(self):
        pass

    def close(self):
        pass


db1 = SingleConnection('log1', 'name1', 80)
db2 = SingleConnection('log2', 'name2', 8080)

print(id(db1), db1.__dict__)
print(id(db2), db2.__dict__)
