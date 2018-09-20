from django.shortcuts import render
from view_table.models import Genre, instrument


def index(request):

    """View function for home page of site."""

    # numner of the Genre
    num_Genre = Genre.objects.all().count()

    # Generate counts of some of the main objects
    num_Instrument = instrument.objects.all().count()

    # Equity Stocks(status = 'e')
    # num_equities = Instrument.objects.filter(status__exact='e').count()
    context = {
        'num_Genres': num_Genre,
        'num_Instruments': num_Instrument,
    #     'num_equities': num_equities,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


from django.views import generic


class instrumentListView(generic.ListView):
    model = instrument


class instrumentDetailView(generic.DetailView):
    model = instrument


def show_table(request):
    model = instrument

    query_results = {'data': model.objects.all()}

    # Render the HTML template show_table.html with the data in the context
    # variable
    return render(request, 'show_table.html', context=query_results)
