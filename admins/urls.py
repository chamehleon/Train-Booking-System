from django.urls import path
from . import views

urlpatterns = [
    path('trips/', views.add_trip, name='add_trip'),
    path('trips/update/<int:id>/', views.update_trip, name='update_trip'),
    path('trips/delete/<int:id>/', views.delete_trip, name='delete_trip'),
    path('trains/', views.add_train, name='add_train'),
    path('trains/update/<int:id>/', views.update_train, name='update_train'),
    path('trains/delete/<int:id>/', views.delete_train, name='delete_train'),
    #path('addTrain',views.add, name ='add'),
    #path('update',views.update, name='update'),
    path('searchTrip',views.tripform,name='TripForm'),
    #path('addTrip',views.addTrip,name='addTrip'),
    # path('verifyBook',views.verifyBook, name ='verifyBook'),
    path('index',views.index,name='index'),
    path('viewBooks',views.viewBooks, name ='viewBooks'),
    path('cancel/<int:trip_id>',views.cancel, name ='cancel'),
    path('verifyBook/<int:trip_id>',views.verifyBook, name ='verifyBook'),

]
