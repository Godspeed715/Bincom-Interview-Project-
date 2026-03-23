from django.shortcuts import render, get_object_or_404, redirect
from .models import OwaspTop10

# Create your views here.
def owasp_list(request):
    return redirect(owasp, page_no=1)

def owasp(request, page_no):
    page_count = OwaspTop10.objects.all().count()
    prev_id = page_no - 1 if page_no > 0 else None
    next_id = page_no + 1 if page_no < page_count else None
    article = get_object_or_404(OwaspTop10, page_no=page_no)
    return render(request, 'index.html', {'article': article, 'prev_id': prev_id, 'next_id': next_id})

