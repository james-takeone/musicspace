from django.urls import path, include

import musicspace_app.views as views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('find-a-teacher', views.ProviderListView.as_view(), name='provider-list'),
    path('for-teachers', views.ForProvidersView.as_view(), name='for-teachers'),
    path('about-us', views.AboutUsView.as_view(), name='about-us'),
    path('teachers/<uuid:provider_id>', views.ProviderDetailView.as_view(), name='provider-detail'),
    path('for-teachers/login', views.ProviderLoginView.as_view(), name='login'),
    path('for-teachers/logout', views.ProviderLogoutView.as_view(), name='logout'),
]