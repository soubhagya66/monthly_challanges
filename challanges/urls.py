from django.urls import path
from . import views
urlpatterns = [
    # path("january", views.index),
    # path("february", views.index1),
    # path("march", views.index2),
    # path("april", views.index3)
    path("",views.index),
    path("<int:month>", views.monthlty_challanges_by_num),
    path("<str:month>", views.monthly_challanetext,name="month_challane")
    
]
