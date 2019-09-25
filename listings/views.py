from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Listing


# Create your views here.
def index(request):
    # Get all listing
    # '-' for descendent
    # listings = Listing.object.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # Pagination
    paginator = Paginator(listings, 1)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
