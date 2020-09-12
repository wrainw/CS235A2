from domain.genre import Genre
from domain.actor import Actor
from domain.director import Director


class Movie:
    def __init__(self, title, release_year):
        if title == "" or type(title) is not str:
            self.title = None
        else:
            self.title = title.strip()
        if type(release_year) is not int or release_year < 1900:
            self.release_year = None
        else:
            self.release_year = release_year
        self.__description = ""
        self.director = None
        self.actors = []
        self.genres = []
        self.__runtime_minutes = 0

    def __repr__(self):
        return f"<Movie {self.title}, {self.release_year}>"

    def __eq__(self, other):
        return self.title == other.title and self.release_year == other.release_year

    def __lt__(self, other):
        if self.title < other.title:
            return True
        elif self.title == other.title:
            if self.release_year < other.release_year:
                return True
            else:
                return False
        else:
            return False

    def __hash__(self):
        return hash(self.title) + hash(self.release_year)

    def get_description(self):
        return self.__description

    def set_description(self, description):
        if type(description) is str:
            self.__description = description.strip()

    def set_director(self, director):
        self.director = director

    def set_actors(self, actors):
        self.actors = actors

    def set_genres(self, genres):
        self.genres = genres

    def get_runtime_minutes(self):
        return self.__runtime_minutes

    def set_runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) is int and runtime_minutes > 0:
            self.__runtime_minutes = runtime_minutes
        else:
            raise ValueError()

    def add_actor(self, actor):
        self.actors.append(actor)

    def remove_actor(self, actor):
        if actor in self.actors:
            self.actors.remove(actor)

    def add_genre(self, genre):
        self.genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.genres:
            self.genres.remove(genre)

    runtime_minutes = property(get_runtime_minutes, set_runtime_minutes)
    description = property(get_description, set_description)
