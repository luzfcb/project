import pytest

from core.tests import factories


@pytest.fixture
def country():
    """
    will return a different country with each call.
    :return: core.Country instance
    """
    return factories.CountryFactory()


@pytest.fixture
def matrix_script():
    return factories.TheMatrixSeriesScript()


@pytest.mark.django_db
def test_country(country):
    assert country.name == "Italy"
    assert country


@pytest.mark.django_db
def test_matrix_script(matrix_script):
    assert matrix_script.name == "The Matrix Series"
    assert matrix_script.movies.filter(actors__name="Keanu Reeves").exists()
