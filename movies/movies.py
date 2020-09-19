from datetime import date

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import adapters.repository as repo

import movies.services as services

# from authentication.authentication import login_required


# Configure Blueprint.
movies_blueprint = Blueprint(
    'movies_bp', __name__)


@movies_blueprint.route('/movies_by_actor', methods=['GET'])
def movies_by_actor():
    # Read query parameters.
    target_actor = request.args.get('actor')

    # Fetch the first and last actors in the series.
    first_actor = services.get_first_actor(repo.repo_instance)
    last_actor = services.get_last_actor(repo.repo_instance)

    if target_actor is None:
        target_actor = first_actor.actor_full_name
    else:
        target_actor = target_actor

    # Fetch movie(s) for the target actor. This call also returns the previous and next actors immediately
    # before and after the target actor.
    movies, previous_actor, next_actor = services.get_movies_by_actor(target_actor, repo.repo_instance)

    first_actor_url = None
    last_actor_url = None
    next_actor_url = None
    prev_actor_url = None

    if len(movies) > 0:
        # There's at least one movie for the target actor.
        if previous_actor is not None:
            # There are movies on a previous actor, so generate URLs for the 'previous' and 'first' navigation buttons.
            prev_actor_url = url_for('movies_bp.movies_by_actor', actor=previous_actor.actor_full_name)
            first_actor_url = url_for('movies_bp.movies_by_actor', actor=first_actor.actor_full_name)

        # There are movies on a subsequent actor, so generate URLs for the 'next' and 'last' navigation buttons.
        if next_actor is not None:
            next_actor_url = url_for('movies_bp.movies_by_actor', actor=next_actor.actor_full_name)
            last_actor_url = url_for('movies_bp.movies_by_actor', actor=last_actor.actor_full_name)

        # Generate the webpage to display the articles.
        return render_template(
            'movies/movies.html',
            title='Movies',
            movies_title='Actor: ' + target_actor,
            movies=movies,
            first_movie_url=first_actor_url,
            last_movie_url=last_actor_url,
            prev_movie_url=prev_actor_url,
            next_movie_url=next_actor_url,
        )

    # No articles to show, so return the homepage.
    return redirect(url_for('home_bp.home'))


@movies_blueprint.route('/movies_by_genre', methods=['GET'])
def movies_by_genre():
    # Read query parameters.
    target_genre = request.args.get('genre')

    # Fetch the first and last genres in the series.
    first_genre = services.get_first_genre(repo.repo_instance)
    last_genre = services.get_last_genre(repo.repo_instance)

    if target_genre is None:
        target_genre = first_genre.genre_name

    # Fetch movie(s) for the target genre. This call also returns the previous and next genres immediately
    # before and after the target genre.
    movies, previous_genre, next_genre = services.get_movies_by_genre(target_genre, repo.repo_instance)

    first_genre_url = None
    last_genre_url = None
    next_genre_url = None
    prev_genre_url = None

    if len(movies) > 0:
        # There's at least one movie for the target genre.
        if previous_genre is not None:
            # There are movies on a previous genre, so generate URLs for the 'previous' and 'first' navigation buttons.
            prev_genre_url = url_for('movies_bp.movies_by_genre', genre=previous_genre.genre_name)
            first_genre_url = url_for('movies_bp.movies_by_genre', genre=first_genre.genre_name)

        # There are movies on a subsequent genre, so generate URLs for the 'next' and 'last' navigation buttons.
        if next_genre is not None:
            next_genre_url = url_for('movies_bp.movies_by_genre', genre=next_genre.genre_name)
            last_genre_url = url_for('movies_bp.movies_by_genre', genre=last_genre.genre_name)

        # Generate the webpage to display the articles.
        return render_template(
            'movies/movies.html',
            title='Movies',
            movies_title='Genre: ' + target_genre,
            movies=movies,
            first_movie_url=first_genre_url,
            last_movie_url=last_genre_url,
            prev_movie_url=prev_genre_url,
            next_movie_url=next_genre_url,
        )

    # No articles to show, so return the homepage.
    return redirect(url_for('home_bp.home'))


@movies_blueprint.route('/movies_by_director', methods=['GET'])
def movies_by_director():
    # Read query parameters.
    target_director = request.args.get('director')
    # movie_to_show_reviews = request.args.get('view_reviews_for')

    # Fetch the first and last genres in the series.
    first_director = services.get_first_director(repo.repo_instance)
    last_director = services.get_last_director(repo.repo_instance)

    if target_director is None:
        target_director = first_director.director_full_name

    # Fetch movie(s) for the target genre. This call also returns the previous and next genres immediately
    # before and after the target genre.
    movies, previous_director, next_director = services.get_movies_by_director(target_director, repo.repo_instance)

    first_director_url = None
    last_director_url = None
    next_director_url = None
    prev_director_url = None

    if len(movies) > 0:
        # There's at least one movie for the target genre.
        if previous_director is not None:
            # There are movies on a previous genre, so generate URLs for the 'previous' and 'first' navigation buttons.
            prev_director_url = url_for('movies_bp.movies_by_director', director=previous_director.director_full_name)
            first_director_url = url_for('movies_bp.movies_by_director', director=first_director.director_full_name)

        # There are movies on a subsequent genre, so generate URLs for the 'next' and 'last' navigation buttons.
        if next_director is not None:
            next_director_url = url_for('movies_bp.movies_by_director', director=next_director.director_full_name)
            last_director_url = url_for('movies_bp.movies_by_director', director=last_director.director_full_name)

        # Generate the webpage to display the articles.
        return render_template(
            'movies/movies.html',
            title='Movies',
            movies_title='Director: ' + target_director,
            movies=movies,
            first_movie_url=first_director_url,
            last_movie_url=last_director_url,
            prev_movie_url=prev_director_url,
            next_movie_url=next_director_url,
        )

    # No articles to show, so return the homepage.
    return redirect(url_for('home_bp.home'))


# @movies_blueprint.route('/comment', methods=['GET', 'POST'])
# @login_required
# def comment_on_article():
#     # Obtain the username of the currently logged in user.
#     username = session['username']
#
#     # Create form. The form maintains state, e.g. when this method is called with a HTTP GET request and populates
#     # the form with an article id, when subsequently called with a HTTP POST request, the article id remains in the
#     # form.
#     form = CommentForm()
#
#     if form.validate_on_submit():
#         # Successful POST, i.e. the comment text has passed data validation.
#         # Extract the article id, representing the commented article, from the form.
#         article_id = int(form.article_id.data)
#
#         # Use the service layer to store the new comment.
#         services.add_comment(article_id, form.comment.data, username, repo.repo_instance)
#
#         # Retrieve the article in dict form.
#         article = services.get_article(article_id, repo.repo_instance)
#
#         # Cause the web browser to display the page of all articles that have the same date as the commented article,
#         # and display all comments, including the new comment.
#         return redirect(url_for('news_bp.articles_by_date', date=article['date'], view_comments_for=article_id))
#
#     if request.method == 'GET':
#         # Request is a HTTP GET to display the form.
#         # Extract the article id, representing the article to comment, from a query parameter of the GET request.
#         article_id = int(request.args.get('article'))
#
#         # Store the article id in the form.
#         form.article_id.data = article_id
#     else:
#         # Request is a HTTP POST where form validation has failed.
#         # Extract the article id of the article being commented from the form.
#         article_id = int(form.article_id.data)
#
#     # For a GET or an unsuccessful POST, retrieve the article to comment in dict form, and return a Web page that allows
#     # the user to enter a comment. The generated Web page includes a form object.
#     article = services.get_article(article_id, repo.repo_instance)
#     return render_template(
#         'news/comment_on_article.html',
#         title='Edit article',
#         article=article,
#         form=form,
#         handler_url=url_for('news_bp.comment_on_article'),
#         selected_articles=utilities.get_selected_articles(),
#         tag_urls=utilities.get_tags_and_urls()
#     )


class ProfanityFree:
    def __init__(self, message=None):
        if not message:
            message = u'Field must not contain profanity'
        self.message = message

    def __call__(self, form, field):
        if profanity.contains_profanity(field.data):
            raise ValidationError(self.message)


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', [
        DataRequired(),
        Length(min=4, message='Your comment is too short'),
        ProfanityFree(message='Your comment must not contain profanity')])
    article_id = HiddenField("Article id")
    submit = SubmitField('Submit')