from .views import owasp, owasp_list
from django.urls import path

urlpatterns = [
    path('<int:page_no>', owasp, name='owasp'),
    path('', owasp_list, name='owasp_list'),
]