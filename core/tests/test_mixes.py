import pytest

from core.tests.mixes import the_matrix_movie


@pytest.fixture()
def matrix_movie():
    return the_matrix_movie()


@pytest.mark.django_db
def test_matrix_movie(matrix_movie):
    assert matrix_movie.name == "The Matrix"
