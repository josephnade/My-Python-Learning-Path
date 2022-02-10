import requests


class theMovieDb:
    def __init__(self, token):
        self.api_url = "https://api.themoviedb.org/3"
        self.token = token

    def getPopular(self):
        response = requests.get(self.api_url + "/movie/popular?api_key=" + self.token + "&language=en-US&page=1")
        return response.json()
    def searchMovie(self,search):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.token}&query={search}&page=1")
        return response.json()

movie = theMovieDb("6f530e5708947eff4f1c2f08da0bfeb2")
while True:
    choose = input("[1]Popular Movie\n[2]Search Movie\n[3]Exit\nChoose= ")
    if choose == "3":
        print("Have a good day!!!".center(50,"*"))
        break
    else:
        if choose == "1":
            movies = movie.getPopular()
            c = 1
            for mov in movies['results']:
                print(f"{c}. Popular Movie: {mov['title']}")
                c+=1
        if choose == "2":
            find = input("Search =")
            movies = movie.searchMovie(find)
            c = 1
            for mov in movies['results']:
                print(f"{c}. Found Movie: {mov['name']}")
                c+=1
