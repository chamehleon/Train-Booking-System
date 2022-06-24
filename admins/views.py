from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages

# Create your views here.
def index (request):
    return render(request,'admins/home_Admin.html')

def add_trip(request):
    if request.method == 'POST':
        new_trip = TripForm(request.POST, request.FILES)
        if new_trip.is_valid():
            new_trip.save()

    context = {
        'trips': Trip.objects.all(),
        'form': TripForm(),
    }
    return render(request, 'admins/add_trip.html', context)


def update_trip(request, id):
    trip_id = Trip.objects.get(trip_id=id)
    if request.method == 'POST':
        updated_trip = TripForm(request.POST, request.FILES, instance=trip_id)
        if updated_trip.is_valid():
            updated_trip.save()
            return redirect('add_trip')
    else:
        updated_trip = TripForm(instance=trip_id)
    context = {
        'form': updated_trip
    }
    return render(request, 'admins/update_trip.html', context)


def delete_trip(request, id):
    deleted_trip = get_object_or_404(Trip, trip_id=id)
    if request.method == 'POST':
        deleted_trip.delete()
        return redirect('add_trip')
    return render(request, 'admins/delete_trip.html')


def add_train(request):
    if request.method == 'POST':
        new_train = TrainForm(request.POST, request.FILES)
        if new_train.is_valid():
            new_train.save()

    context = {
        'trains': Train.objects.all(),
        'form': TrainForm(),
    }
    return render(request, 'admins/add_train.html', context)


def update_train(request, id):
    train_id = Train.objects.get(id=id)
    if request.method == 'POST':
        updated_train = TrainForm(request.POST, request.FILES, instance=train_id)
        if updated_train.is_valid():
            updated_train.save()
            return redirect('add_train')
    else:
        updated_train = TrainForm(instance=train_id)
    context = {
        'form': updated_train
    }
    return render(request, 'admins/update_train.html', context)


def delete_train(request, id):
    deleted_train = get_object_or_404(Train, id=id)
    if request.method == 'POST':
        deleted_train.delete()
        return redirect('add_train')
    return render(request, 'admins/delete_train.html')

def tripform(request):
    global data
    dataToPost=None
    if request.method=='POST':
        data =SearchTripForm(request.POST)
        if data.is_valid():
            dataToPost = Trip.objects.filter(source= data.cleaned_data['source'],
                                            destination =data.cleaned_data['destination'],
                                            date =data.cleaned_data['date'],
                                            number_of_seats =data.cleaned_data['number_of_seats'],
                                            ticket_price= data.cleaned_data['ticket_price'])
    elif request.method =='GET':
        data = SearchTripForm()
        dataToPost = Trip.objects.all()
    return(render(request ,'customers/Book.html',{'forms':SearchTripForm(),'trips':dataToPost}))

def verifyBook(request,trip_id):
    trip_object =Trip.objects.get(trip_id=trip_id)
    context={
            'trip':trip_object
        }
    if request.method=="POST":
            slots= request.POST['Slots']
            if trip_object.number_of_seats>=int(slots):
                trip_object.books.add(request.user)
                trip_object.number_of_seats = trip_object.number_of_seats-int(slots)
                trip_object.save()
                messages.info(request,'You have succefully booked in and transferred '+str(trip_object.ticket_price))
            else:
                messages.info(request,"please enter a number of slots smaller than "+str(trip_object.number_of_seats))
  
    return render(request,'admins/verify-book.html',context)


def cancel(request,trip_id):
    trip_object =Trip.objects.get(trip_id=trip_id)
    if request.method=="GET":
       trip_object.books.remove(request.user)
       trip_object.save() 
       messages.info(request,'your book now is cancelled') 
    return render(request,'customers/home_user.html')

def viewBooks(request):
    if request.method=='GET':
        user=request.user
        dataToPost = user.trip_set.all()
    context={
        'trips':dataToPost
    }
    return render(request,'customers/Bookings.html',context)