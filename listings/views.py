from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Listing


# Create your views here.
def index(request):
    # Get all listing
    # '-' for descendent.
    # listings = Listing.object.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # Pagination (items, item_per_page)
    paginator = Paginator(listings, 1)
    # Get page number through url: '?page=xxx'.
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }

    return render(request, 'listings/listings.html', context)

# TODO: refactor to imgModel as foreign key
def listing(request, listing_id):
    # Check if object exist, if not return 404 error-page.
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
