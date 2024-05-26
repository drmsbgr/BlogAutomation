class Account(object):
    def __init__(
        self,
        id: int,
        username: str,
        password: str,
        mail: str,
        genderID: int,
        birthDate: str,
        roleID: int,
    ):
        self.id = id
        self.username = username
        self.password = password
        self.email = mail
        self.genderID = genderID
        self.birthDate = birthDate
        self.roleID = roleID
        super(Account, self).__init__()
