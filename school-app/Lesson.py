class Lesson:
    def __init__(self, id , name):
        if id == None:
            self.id = 0
        else:
            self.id = id
        if len(name) > 45:
            raise Exception("Too big name!")
        self.name = name
