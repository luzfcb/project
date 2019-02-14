from django.contrib.humanize.templatetags.humanize import intcomma
from django.db import models


class Country(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    def __str__(self):
        return f"{self.name}"


class Contract(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    salary = models.IntegerField()

    def __str__(self):
        salary = intcomma(self.salary)
        return f'Name: "{self.name}" salary: ${salary}'


class Person(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    birthplace = models.ForeignKey(
        to="Country",
        related_name="people",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name}"


class Character(models.Model):
    movie = models.ForeignKey(
        to="Movie",
        related_name="characters",
        on_delete=models.CASCADE
    )
    actor = models.ForeignKey(
        to="Person",
        related_name="characters",
        on_delete=models.CASCADE
    )
    contract = models.ForeignKey(
        to="Contract",
        null=True,
        related_name="characters",
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255
    )
    additional_info = models.TextField(
        null=True
    )

    def __str__(self):
        return f'Name: "{self.name}" by "{self.actor}" - contract: "{self.contract}"'

    class Meta:
        unique_together = (
            ("movie", "actor", "name", "additional_info")
        )


class Movie(models.Model):
    name = models.CharField(
        max_length=255
    )
    additional_info = models.TextField(
        null=True
    )
    actors = models.ManyToManyField(
        to="Person",
        through="Character",
        through_fields=("movie", "actor"),
        related_name="movies"
    )
    script = models.ForeignKey(
        to="Script",
        related_name="movies",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name}"


class Script(models.Model):
    name = models.CharField(
        max_length=255
    )
    content = models.TextField(
    )

    def __str__(self):
        return f"pk: {self.pk}-{self.name}"
