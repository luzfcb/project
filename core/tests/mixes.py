import pytest
from mixer.backend.django import mixer
from core import models


def the_matrix_movie():
    # not work if exist duplicated values
    movie_name = "The Matrix"
    names = (name for name in ("Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss", "Hugo Weaving"))
    birthplace__names = (name for name in ("Lebanon", "USA", "Canada", "Nigeria"))
    character_names = (name for name in ("Neo", "Morpheus", "Trinity", "Agent Smith"))
    contract_salaries = (salary for salary in (1_500_000, 1_200_00, 1_200_00, 1_200_00))
    contract__names = (name for name in ("K - Matrix Trilogy", "L - Matrix Trilogy", "C - Matrix Trilogy", "H - Matrix Trilogy"))
    persons = mixer.cycle(4).blend(
        scheme=models.Person,
        name=names,
        birthplace__name=birthplace__names,
    )
    script = mixer.blend(
        scheme=models.Script,
    )
    movie = mixer.blend(
        scheme=models.Movie,
        name=movie_name,
        script=script
    )
    characters = mixer.cycle(4).blend(
        scheme=models.Character,
        movie=movie,
        actor=(actor for actor in persons),
        name=character_names,
        contract__salary=contract_salaries,
        contract__name=contract__names
    )

    return movie
