from django.urls import path, include

from fruitipediaApp.web.views import index, dashboard, create_fruit, details_fruit, delete_fruit, edit_fruit, \
    details_profile, edit_profile, delete_profile, create_profile

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create_fruit, name='create fruit'),
    path('<int:fruit_id>/', include([
        path('details/', details_fruit, name='details fruit'),
        path('edit/', edit_fruit, name='edit fruit'),
        path('delete/', delete_fruit, name='delete fruit'),
    ])),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
