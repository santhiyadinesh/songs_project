from django. urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('home',views.home,name='a'),
    path('songs<str:name>',views.playsong,name='song'),
    path('profile/', views.profilepage, name='profile'),
    path('reviewsongs',views.revsong,name='c'),
    path('about',views.about,name='d'),
    path('help',views.help,name='e'),
    path('center',views.center,name='z'),
    path('price',views.price,name='f'),
    path('account',views.account,name='g'),
    path('output',views.output,name='p'),
    path('register',views.register,name='register'),
    path('login',views.loginpage,name='login'),
    path('logout',views.outlog,name='logout'),
    path('search/',views.SearchResultsList,name='search'),

    
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
