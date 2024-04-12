from django.db import models


class Cattle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey("Location", on_delete=models.PROTECT)
    breed = models.ForeignKey(
        "Breed", on_delete=models.PROTECT
    )  # Type of animal/cattle
    birth_date = models.DateTimeField()
    organisation = models.ForeignKey("Organisation", on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.birth_date.date()})"


class Organisation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey("Location", on_delete=models.PROTECT)
    type = models.ForeignKey("Organisation_Type", on_delete=models.PROTECT)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.type})"


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cattle = models.ForeignKey(Cattle, on_delete=models.PROTECT)
    location = models.ForeignKey("Location", on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Produced from {self.cattle})"


class Location(models.Model):
    city = models.CharField("City/Town", max_length=255)
    country = models.CharField(max_length=255)
    continent = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city}, {self.country}"


class Process(models.Model):
    """Abstract base class for processes."""

    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey("Location", on_delete=models.PROTECT)
    organisation = models.ForeignKey("Organisation", on_delete=models.PROTECT)
    date = models.DateTimeField()
    type = models.ForeignKey("Process_type", on_delete=models.PROTECT)
    transportation_mode = models.ForeignKey(
        "Transportation_mode", on_delete=models.PROTECT
    )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (performed on: {self.date.date()})"

    class Meta:
        abstract = True


class Cattle_process(Process):
    organic = models.BooleanField()
    entity = models.ForeignKey(Cattle, on_delete=models.PROTECT)


class Product_process(Process):
    entity = models.ForeignKey(Product, on_delete=models.PROTECT)


# types
class Type(models.Model):
    """Abstract base class for all types."""

    name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Breed(Type):
    """A breed of cattle"""

    pass


class Process_type(Type):
    """Type of process could be: transportation, grazing, weaning, slaughtering among others."""

    pass


class Transportation_mode(Type):
    # TODO: define how carbon footprint is attained
    pass


class Organisation_type(Type):
    """Type of organisation could be: Farm, Slaughters house, Boucher among others."""

    pass
