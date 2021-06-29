from django.shortcuts import render
from .models import Table
from django.core.paginator import Paginator
# Create your views here.
def table(request):
    table_items = Table.objects.all()
    paginator = Paginator(table_items, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'table/index.html', {'page_obj': page_obj})