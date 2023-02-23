from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("referanslarimiz", views.references, name="referanslarimiz"),
    path("iletisim", views.contact, name="iletisim"),
    path("hakkimizda", views.about, name="hakkimizda"),
    path("hizmetlerimiz", views.services, name="hizmetlerimiz"),
    path("hizmetlerimiz/<slug:slug>", views.service_details, name="service_details"),


    # path("blogs", views.blogs, name="blogs"),
    # path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    # path("blogs/<slug:slug>", views.blog_details, name="blog_details"),
]



# configiure admin name

admin.site.site_header = 'Diriliş Metal Yönetim Paneli'
admin.site.site_title = 'Diriliş Metal'
admin.site.index_title = 'Site Yönetim Paneline Hoşgeldiniz...'