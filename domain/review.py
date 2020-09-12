from datetime import datetime

from domainmodel.movie import Movie


class Review:

    def __init__(self, movie, review_text, rating):
        self._movie = movie
        self._review_text = review_text
        if type(rating) is not int or rating < 1 or rating > 10:
            self._rating = None
        else:
            self._rating = rating
        self._timestamp = datetime.today()

    @property
    def movie(self):
        return self._movie

    @property
    def review_text(self):
        return self._review_text

    @property
    def rating(self):
        return self._rating

    @property
    def timestamp(self):
        return self._timestamp

    def __repr__(self):
        return f"<Review {self._movie.title}, {self._review_text}, {self._timestamp.strftime('%m/%d/%Y')}>"

    def __eq__(self, other):
        return (self._movie == other.movie and self._review_text == other.review_text and self._rating == other.rating
                and self._timestamp == other.timestamp)


# movie = Movie("Moana", 2016)
# review_text = "This movie was very enjoyable."
# review_text2 = "This movie was very"
# rating = 10
# review = Review(movie, review_text, rating)
# review2 = Review(movie, review_text2, rating)
#
# print(review.movie)
# print("Review: {}".format(review.review_text))
# print("Rating: {}".format(review.rating))
# print(review == review2)
