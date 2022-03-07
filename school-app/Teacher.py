class Teacher:
    def __init__(self,id,branch,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.branch  = branch
        if len(name) > 45:
            raise Exception("Too big name!")
        self.name = name
        if len(name) > 45:
            raise Exception("Too big surname!")
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender