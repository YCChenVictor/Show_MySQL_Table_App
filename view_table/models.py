from django.db import models


class Genre(models.Model):
    """Model representing a finance instrument genre."""
    name = models.CharField(max_length=50,
                            help_text=('Enter an instrument genre e.g.' +
                                       ' Equity,' +
                                       ' Futures,' +
                                       ' ETF,' +
                                       ' Fund' +
                                       ' Index' +
                                       ' Option'))

    def __str__(self):
        """String for representing the Model object."""
        return self.name


# Used to generate URLs by reversing the URL patterns
from django.urls import reverse


class instrument(models.Model):
    """
    Model representing a instrument(but not a specific copy of a instrumnet).
    The column, id, will be automatically created.
    """
    ticker = models.CharField(max_length=50)

    name = models.TextField(max_length=50,
                            help_text='Enter the name of an instrument')

    exchange = models.CharField('Exchange', max_length=13,
                                help_text='The name of exchange institution')

    # Type = models.CharField('Type', max_length=1,
    #                         help_text='S for stock; E for Equity ...etc')

    genre = models.ManyToManyField(Genre,
                                   help_text='Select a genre for this instrument')
    """
    ManyToManyField used because genre can contain many instruments.
    Instruments can cover many genres.
    Genre class has already been defined so we can specify the object above.
    """

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this Instrument."""
        return reverse('instrument-detail', args=[str(self.ticker)])
