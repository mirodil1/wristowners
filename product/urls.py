from django.urls import path, include

from product import views

urlpatterns = [
    path('products/', views.ProductsList.as_view()),
    path('product/<slug:brandmodel>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('categories/', views.BrandList.as_view()),
    path('category/<slug:brand_slug>', views.BrandModelList.as_view()),
    # path('products/<slug:brand_slug>/', views.ProductsList.as_view()),
    path('products/<slug:brand_model_slug>/', views.BrandModelProductsList.as_view()),
    # path('products/<slug:brand_slug>/<slug:brand_model_slug>')
    path('faqs/', views.FaqList.as_view()),
]
