class Post(object):
    def __init__(self, id: int, title: str, content: str, date: str, publisherID: int):
        super(Post, self).__init__()
        self.id = id
        self.title = title
        self.content = content
        self.date = date
        self.publisherID = publisherID
