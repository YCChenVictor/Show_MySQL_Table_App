from django.db import models


class Genre(models.Model):
    """Model representing a finance instrument genre."""
    name = models.CharField(max_length=200,
                            help_text='Enter a instrument genre (e.g. Equity)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Instrument(models.Model):
    """Model representing a instrument(but not a specific copy of a instrumnet)."""
    # id = models.ForeignKey('id', on_delete=models.SET_NULL, null=True)
    ticker = models.CharField(max_length=50)
    name = models.TextField(max_length=50, help_text='Enter a of the instrument')
    exchange = models.CharField('Exchange', max_length=13, help_text='The name of exchange institution')
    Type = models.CharField('Type', max_length=1, help_text='S for stock; E for Equity ...etc')
    # ManyToManyField used because genre can contain many instruments. Instruments can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this instrument')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('instrument-detail', args=[str(self.id)])
