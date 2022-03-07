class Class:
    def __init__(self,id,name,teacherId):
        if id == None:
            self.id = 0
        else:
            self.id = id
        if len(name) > 45:
            raise Exception("Too big name!")
        self.name = name
        self.teacherId = teacherId
    @staticmethod
    def create_class(obj):
        list = []

        for i in obj:
            list.append(Class(i[0],i[1],i[2]))
        return list