import factory
from factory.fuzzy import FuzzyInteger
from num2words import num2words


class CountryFactory(factory.DjangoModelFactory):
    class Meta:
        model = "core.Country"
        django_get_or_create = ("name",)

    name = factory.Iterator(["Brazil", "United States of America", "Germany", "Italy"])


class ContractFactory(factory.DjangoModelFactory):
    class Meta:
        model = "core.Contract"
        django_get_or_create = ("name", "salary")

    salary = FuzzyInteger(low=200_000, high=1_500_000, step=10_000)

    @factory.lazy_attribute
    def name(self):
        return num2words(self.salary, lang="pt_BR")


class ScriptFactory(factory.DjangoModelFactory):
    class Meta:
        model = "core.Script"
        django_get_or_create = ("name",)

    name = factory.Iterator(
        ["A man in red clothes",
         "The world where people are like batteries to provide energy for intelligent robots",
         "Traveling to far, far away"
         ]
    )


class PersonFactory(factory.DjangoModelFactory):
    class Meta:
        model = "core.Person"
        django_get_or_create = ("name", "birthplace")

    name = factory.Iterator(["Cristiano", "Susana", "Fabio", "Evelyn"])
    birthplace = factory.SubFactory(CountryFactory)


class MovieFactory(factory.DjangoModelFactory):
    class Meta:
        model = "core.Movie"
        django_get_or_create = ("name", "script")

    name = factory.Iterator(["Spyderman", "The Matrix", "Interstellar"])
    script = factory.SubFactory(ScriptFactory)


class CharacterFactory(factory.DjangoModelFactory):
    class Meta:
        model = "core.Character"
        django_get_or_create = ("name", "movie", "actor")

    movie = factory.SubFactory(MovieFactory)
    actor = factory.SubFactory(PersonFactory)
    contract = factory.SubFactory(ContractFactory)
    name = factory.Iterator(["Peter Parker", "Neo", "Joseph Cooper"])


class TheMatrixMovieFactory(MovieFactory):
    name = "The Matrix"
    actor1 = factory.RelatedFactory(
        factory=CharacterFactory,
        # must contain the name of ForeignKey that points
        # to the same model of the class factory point.
        # In this case, the factory is MovieFactory, and the model is
        # core.Movie
        factory_related_name="movie",
        # this is an attribute of intermediate table
        # attributes of related tables can also
        # be defined using the syntax double underscore syntax.
        # accessing attributes by related_name's is not supported.
        name="Neo",
        actor__name="Keanu Reeves",
        actor__birthplace__name="Lebanon",
        contract__name="Five Hundred",
        contract__salary=500
    )
    actor2 = factory.RelatedFactory(
        factory=CharacterFactory,
        factory_related_name="movie",
        name="Morpheus",
        actor__name="Laurence Fishburne",
        actor__birthplace__name="USA",
        contract__name="Four Hundred",
        contract__salary=400
    )
    actor3 = factory.RelatedFactory(
        factory=CharacterFactory,
        factory_related_name="movie",
        name="Trinity",
        actor__name="Carrie-Anne Moss",
        actor__birthplace__name="Canada",
    )
    actor4 = factory.RelatedFactory(
        factory=CharacterFactory,
        factory_related_name="movie",
        name="Agent Smith",
        actor__name="Hugo Weaving",
        actor__birthplace__name="Nigeria"
    )
    actor5 = factory.RelatedFactory(
        factory=CharacterFactory,
        factory_related_name="movie",
        name="Oracle",
        actor__name="Gloria Foster",
        actor__birthplace__name="USA"
    )
    actor6 = factory.RelatedFactory(
        factory=CharacterFactory,
        factory_related_name="movie",
        name="Cypher",
        actor__name="Joe Pantoliano",
        actor__birthplace__name="USA",
        # None in a ForeignKey attribute make factory_boy not generate the value
        contract=None
    )
    script = factory.SubFactory(ScriptFactory)


class TheMatrix2MovieFactory(TheMatrixMovieFactory):
    name = "The Matrix 2"


class TheMatrixSeriesScript(ScriptFactory):
    name = "The Matrix Series"
    movie1 = factory.RelatedFactory(
        factory=TheMatrixMovieFactory,
        factory_related_name="script"
    )
    movie2 = factory.RelatedFactory(
        factory=TheMatrix2MovieFactory,
        factory_related_name="script"
    )
