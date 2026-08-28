from django.db import models

# Art Tags to identify the items in the artwork, for example: "dog", "wedding card", "portrait", "animal", "landscape", "etc"...
class ArtTags(models.Model):
    name = models.CharField(max_length=100)
    sonOf = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

# Art Types used to identify the type of design, for example: "painting", "drawing", "digital art", "wood design", etc...
class TypeOfArt(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timeExecutionDays = models.IntegerField()

# A discount model that causes a discount to be applied to a art Type, for some time
class Discount(models.Model):
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    type_of_art = models.ForeignKey(TypeOfArt, on_delete=models.CASCADE)

# Artwork model that represents an artwork item with its title, tags, type of art, and location.
class Artwork(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(ArtTags, blank=True)
    typeofArt = models.ForeignKey(TypeOfArt, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return f"""
            title: {self.title}
            location: {self.location}
            tags: {[tag.name for tag in self.tags.all()]}
            type of art: {self.typeofArt.name}
        """