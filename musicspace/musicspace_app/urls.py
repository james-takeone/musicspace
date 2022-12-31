from django.urls import path, include

import musicspace_app.views as views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('find-a-teacher', views.ProviderListView.as_view(), name='find-a-teacher'),
    path('for-teachers', views.ForProvidersView.as_view(), name='for-teachers'),
    path('about-us', views.AboutUsView.as_view(), name='about-us'),
]