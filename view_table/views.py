from django.http import HttpResponse
from view_table.models import Stocks, Alibaba_Group_Holding_Limited
from django.shortcuts import render


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_Stocks = Stocks.objects.all().count()
    num_Alibaba_Group_Holding_Limited = Alibaba_Group_Holding_Limited.objects.all().count()

    # Equity Stocks(status = 'e')
    # num_equities = Stocks.objects.filter(status__exact='e').count()

    context = {
        'num_Stocks': num_Stocks,
        'num_Alibaba_Group_Holding_Limited': num_Alibaba_Group_Holding_Limited,
        # 'num_equities': num_equities,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
