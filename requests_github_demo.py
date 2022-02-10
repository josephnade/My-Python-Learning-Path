import requests
#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
class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    def getRepository(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    def createRepository(self,token,name):
        response = requests.post(self.api_url+'/users/repos?access_token='+token,json = {
            "name": name,
            'description': 'This is my test repository.',
            'homepage': 'https://github.com/josephnade',
            'private': False,
            'has_issues': True,
            'has_project': True,
            'has_wiki':True
        })
        return response.json()

github = Github()
def getRepo(username):
    result = github.getRepository(username)
    c = 1
    for i in result:
        print(f"{c}. Repository = {i['name']}")
        c+=1
while True:
    choose = input("[1]Find User\n[2]Get Repositories\n[3]Create Repository\n[4]Exit\nChoose [1-4] number=")
    if choose == "4":
        break
    else:
        if choose == "1":
            #Find User
            username = input("Please enter username you are looking for= ")
            result = github.getUser(username)
            print(f"User ID = {result['id']}\nNumber of Repository = {result['public_repos']}\nFollowers = {result['followers']}\nFollowing = {result['following']}")
        elif choose == "2":
            #Get Repositories
            username = ""
            if len(username) == 0:
                print("Please enter your username first!")
                username = input("Please enter username you are looking for= ")
                getRepo(username)
            else:
                getRepo(username)
        elif choose == "3":
            #Create Repository
            try:
                name = input("Please enter a repository name: ")
                token = input("Please enter the token: ")
                result = github.createRepository(token,name)
                print(result)
            except Exception as e:
                print("Wrong token")
            pass
        else:
            print("Wrong choose")