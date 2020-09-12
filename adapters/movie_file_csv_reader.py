import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name):
        self.__file_name = file_name
        self._dataset_of_movies = list()
        self._dataset_of_actors = set()
        self._dataset_of_directors = set()
        self._dataset_of_genres = set()

    @property
    def dataset_of_movies(self):
        return self._dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self._dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self._dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self._dataset_of_genres

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                self._dataset_of_movies.append(Movie(row['Title'], int(row['Year'])))
                self._dataset_of_directors.add(Director(row['Director']))
                for actor in row['Actors'].split(","):
                    self._dataset_of_actors.add(Actor(actor.strip()))

                for genre in row['Genre'].split(","):
                    self._dataset_of_genres.add(Genre(genre))


# filename = 'E:\git\CS235FlixSkeleton\datafiles\Data1000Movies.csv'
# movie_file_reader = MovieFileCSVReader(filename)
# movie_file_reader.read_csv_file()
#
# print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
# print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
# print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
# print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')
#
# all_directors_sorted = sorted(movie_file_reader.dataset_of_directors)
# print(f'first 3 unique directors of sorted dataset: {all_directors_sorted[0:3]}')