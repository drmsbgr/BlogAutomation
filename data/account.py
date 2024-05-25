class Account(object):
    def __init__(self, username: str, password: str, gender: bool, date: str):
        self.username = username
        self.password = password
        self.gender = gender
        self.date = date
        super(Account, self).__init__()
