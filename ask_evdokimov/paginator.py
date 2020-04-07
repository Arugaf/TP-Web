from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404


def paginate(object_list, page_id):
    pages = Paginator(object_list, 20)
    page_number = page_id

    try:
        current_page = pages.page(page_number)
    except EmptyPage:
        raise Http404("Page does not exist")
    except PageNotAnInteger:
        raise Http404("Page does not exist")

    return {'questions': current_page, 'number_of_pages': pages.page_range}
