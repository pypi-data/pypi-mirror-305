from gingerdj.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    friends = models.ManyToManyField("self", blank=True)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    num_awards = models.IntegerField()


class ItemTag(models.Model):
    tag = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField()


class Book(models.Model):
    isbn = models.CharField(max_length=9)
    name = models.CharField(max_length=255)
    pages = models.IntegerField()
    rating = models.FloatField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    authors = models.ManyToManyField(Author)
    contact = models.ForeignKey(Author, models.CASCADE, related_name="book_contact_set")
    publisher = models.ForeignKey(Publisher, models.CASCADE)
    pubdate = models.DateField()

    class Meta:
        ordering = ("name",)


class Store(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)
    original_opening = models.DateTimeField()
    friday_night_closing = models.TimeField()


class Entries(models.Model):
    EntryID = models.AutoField(primary_key=True, db_column="Entry ID")
    Entry = models.CharField(unique=True, max_length=50)
    Exclude = models.BooleanField(default=False)


class Clues(models.Model):
    ID = models.AutoField(primary_key=True)
    EntryID = models.ForeignKey(
        Entries, models.CASCADE, verbose_name="Entry", db_column="Entry ID"
    )
    Clue = models.CharField(max_length=150)


class WithManualPK(models.Model):
    # The generic relations regression test needs two different model
    # classes with the same PK value, and there are some (external)
    # DB backends that don't work nicely when assigning integer to AutoField
    # column (MSSQL at least).
    id = models.IntegerField(primary_key=True)


class HardbackBook(Book):
    weight = models.FloatField()


# Models for ticket #21150
class Alfa(models.Model):
    name = models.CharField(max_length=10, null=True)


class Bravo(models.Model):
    pass


class Charlie(models.Model):
    alfa = models.ForeignKey(Alfa, models.SET_NULL, null=True)
    bravo = models.ForeignKey(Bravo, models.SET_NULL, null=True)


class SelfRefFK(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        "self", models.SET_NULL, null=True, blank=True, related_name="children"
    )


class AuthorProxy(Author):
    class Meta:
        proxy = True


class Recipe(models.Model):
    name = models.CharField(max_length=20)
    author = models.ForeignKey(AuthorProxy, models.CASCADE)
    tasters = models.ManyToManyField(AuthorProxy, related_name="recipes")


class RecipeProxy(Recipe):
    class Meta:
        proxy = True


class AuthorUnmanaged(models.Model):
    age = models.IntegerField()

    class Meta:
        db_table = Author._meta.db_table
        managed = False


class RecipeTasterUnmanaged(models.Model):
    recipe = models.ForeignKey("RecipeUnmanaged", models.CASCADE)
    author = models.ForeignKey(
        AuthorUnmanaged, models.CASCADE, db_column="authorproxy_id"
    )

    class Meta:
        managed = False
        db_table = Recipe.tasters.through._meta.db_table


class RecipeUnmanaged(models.Model):
    author = models.ForeignKey(AuthorUnmanaged, models.CASCADE)
    tasters = models.ManyToManyField(
        AuthorUnmanaged, through=RecipeTasterUnmanaged, related_name="+"
    )

    class Meta:
        managed = False
        db_table = Recipe._meta.db_table
