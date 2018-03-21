from django.urls import path
from . import views

app_name = 'novels'
urlpatterns=[
    path('',views.index, name='index'),
    path('bookcase/<int:bookcase_id>/',views.detail_bookcase, name='detail_bookcase'),
    path('bookcase/make/',views.make_bookcase,name='make_bookcase'),
    path('novel/upload/<int:bookcase_id>', views.upload_novel, name='upload_novel'),
    path('novel/<int:novel_id>/',views.detail_novel, name='detail_novel')

    
]
