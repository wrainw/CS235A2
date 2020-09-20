import pytest

from flask import session


def test_register(client):
    # Check that we retrieve the register page.
    response_code = client.get('/authentication/register').status_code
    assert response_code == 200

    # Check that we can register a user successfully, supplying a valid username and password.
    response = client.post(
        '/authentication/register',
        data={'username': 'gmichael', 'password': 'CarelessWhisper1984'}
    )
    assert response.headers['Location'] == 'http://localhost/authentication/login'


@pytest.mark.parametrize(('username', 'password', 'message'), (
        ('', '', b'Your username is required'),
        ('cj', '', b'Your username is too short'),
        ('test', '', b'Your password is required')
))
def test_register_with_invalid_input(client, username, password, message):
    # Check that attempting to register with invalid combinations of username and password generate appropriate error
    # messages.
    response = client.post(
        '/authentication/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data


def test_login(client, auth):
    # Check that we can retrieve the login page.
    status_code = client.get('/authentication/login').status_code
    assert status_code == 200

    # Check that a successful login generates a redirect to the homepage.
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    # Check that a session has been created for the logged-in user.
    with client:
        client.get('/')
        assert session['username'] == 'thorke'


def test_logout(client, auth):
    # Login a user.
    auth.login()

    with client:
        # Check that logging out clears the user's session.
        auth.logout()
        assert 'user_id' not in session


def test_index(client):
    # Check that we can retrieve the home page.
    response = client.get('/')
    assert response.status_code == 200
    assert b'CS235 flix' in response.data


def test_movies_with_actor(client):
    # Check that we can retrieve the movie page.
    response = client.get('/movies_by_actor?actor=A.C.+Peterson')
    assert response.status_code == 200

    # Check that the page includes the desired movie.
    assert b'The Stakelander' in response.data


def test_movies_with_genre(client):
    # Check that we can retrieve the movie page.
    response = client.get('/movies_by_genre?genre=Action')
    assert response.status_code == 200

    # Check that the page includes the desired movie.
    assert b'13 Hours' in response.data
    assert b'21 Jump Street' in response.data


def test_movies_with_director(client):
    # Check that we can retrieve the movie page.
    response = client.get('/movies_by_director?director=Aamir+Khan')
    assert response.status_code == 200

    # Check that the page includes the desired movie.
    assert b'Taare Zameen Par' in response.data
