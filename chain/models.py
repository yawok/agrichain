from django.db import models
from django.urls import reverse


class Cattle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey("cities_light.City", on_delete=models.PROTECT)
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
    location = models.ForeignKey("cities_light.City", on_delete=models.PROTECT)
    type = models.ForeignKey("Organisation_Type", on_delete=models.PROTECT)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.type})"


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cattle = models.ForeignKey(Cattle, on_delete=models.PROTECT)
    location = models.ForeignKey("cities_light.City", on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Produced from {self.cattle})"
    
    def get_product_history_url(self):
        return reverse('producthistory', args=[self.pk])


class Location(models.Model):
    city = models.ForeignKey('cities_light.City', on_delete=models.PROTECT)
    country = models.ForeignKey('cities_light.Country', on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city}, {self.country}"


class Process(models.Model):
    """Abstract base class for processes."""

    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey("cities_light.City", on_delete=models.PROTECT)
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
    co2perkilo = models.DecimalField("Carbon Emission per Kilometer", default=0, null=True, max_digits=7, decimal_places=4)


class Organisation_type(Type):
    """Type of organisation could be: Farm, Slaughters house, Boucher among others."""

    pass
