class Comment(object):
    def __init__(self, id, ownerID, postID, content, date):
        super(Comment, self).__init__()
        self.id = id
        self.ownerID = ownerID
        self.postID = postID
        self.content = content
        self.date = date
