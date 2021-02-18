from django.urls import path
from . import views

urlpatterns = [
    path('home_page', views.home_page),
    path('file_upload', views.file_upload),
    path('single_upload', views.single_upload),
    path('browse_variants', views.browse_variants),
    path('search_result', views.search_result),
    path('variant_browser', views.variant_browser),
    path('edit_variant', views.edit_variant),
    path('edit_sample', views.edit_sample),
]