from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView, DeleteView, DetailView, UpdateView
from . models import Discover, Ttd, Book, Flight, Hotel
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.


class homePageView(TemplateView):
    template_name = 'tourism/home.html'


def discoverView(request):
    discovers = Discover.objects.all()
    ttds = Ttd.objects.all()
    context = {
        'discovers': discovers,
        'ttds': ttds
    }
    return render(request, 'tourism/discover.html', context)


# def ttdView(request):
#     ttds = Ttd.objects.all()
#     context = {'ttds': ttds}
#     return render(request, 'tourism/discover.html', context)


class adv(TemplateView):
    template_name = 'tourism/as.html'


class caves(TemplateView):
    template_name = 'tourism/caves.html'


class home(TemplateView):
    template_name = 'tourism/home.html'


class lakes(TemplateView):
    template_name = 'tourism/lakes.html'


class discoverHal(TemplateView):
    template_name = 'tourism/create.html'


class Login(TemplateView):
    template_name = 'tourism/login.html'


class SignUp(TemplateView):
    template_name = 'signup.html'


class CreateTtdView(CreateView):
    model = Ttd
    template_name = 'tourism/create2.html'
    fields = '__all__'
    success_url = reverse_lazy('discover')


class CreateDiscoverView(CreateView):
    model = Discover
    template_name = 'tourism/create.html'
    fields = '__all__'
    success_url = reverse_lazy('discover')


class DetailDiscoverView(DetailView):
    model = Discover
    template_name = 'tourism/view.html'


class DetailTtdView(DetailView):
    model = Ttd
    template_name = 'tourism/view2.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# class Booking(TemplateView):
#     model = Discover
#     template_name = 'tourism/booking.html'

# @login_required
# def Booking(request):
#     discovers = Discover.objects.all()
#     context = {
#         'discovers': discovers
#     }
#     return render(request, 'tourism/booking.html', context)


class TtdDelete(DeleteView):
    model = Ttd
    template_name = 'tourism/delete.html'
    success_url = reverse_lazy('discover')


class TtdUpdate(UpdateView):
    model = Ttd
    fields = '__all__'
    template_name = 'tourism/update.html'
    success_url = reverse_lazy('discover')


class DiscoverDelete(DeleteView):
    model = Discover
    template_name = 'tourism/delete2.html'
    success_url = reverse_lazy('discover')


class DiscoverUpdate(UpdateView):
    model = Discover
    fields = '__all__'
    template_name = 'tourism/update2.html'
    success_url = reverse_lazy('discover')


# @login_required
# def BookFormView(request):
#     model = Book
#     fields = "__all__"
#     template_name = 'tourism/booking.html'
#     success_url = reverse_lazy('home')

class BookFormView(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'tourism/booking.html'
    success_url = reverse_lazy('home')


def get_Book(request):
    books = Book.objects.all()
    context = {
        'books': books,
        'active_books': 'active'
    }
    return render(request, 'tourism/getBooks.html', context)


class FlightFormView(CreateView):
    model = Flight
    fields = '__all__'
    template_name = 'tourism/flightbooking.html'
    success_url = reverse_lazy('home')


def get_Flight(request):
    flights = Flight.objects.all()
    context = {
        'flights': flights,
        'active_flights': 'active'
    }
    return render(request, 'tourism/getFlights.html', context)


class HotelFormView(CreateView):
    model = Hotel
    fields = '__all__'
    template_name = 'tourism/hotelbooking.html'
    success_url = reverse_lazy('home')


def get_Hotel(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels,
        'active_hotels': 'active'
    }
    return render(request, 'tourism/getHotels.html', context)


# class UserView(TemplateView):
#     template_name = 'tourism/getUsers.html'

def userView(request):
    users_all = User.objects.all()
    users = users_all.filter(is_staff=0)
    context = {
        'users': users,
    }
    return render(request, 'tourism/getUsers.html', context)


class UserDelete(DeleteView):
    model = User
    template_name = 'tourism/userdelete.html'
    success_url = reverse_lazy('get_Users')


class UserUpdate(UpdateView):
    model = User
    fields = '__all__'
    template_name = 'tourism/userupdate.html'
    success_url = reverse_lazy('get_Users')


class AdminPanel(TemplateView):
    template_name = 'tourism/adminpanel.html'


class Add(TemplateView):
    template_name = 'tourism/add.html'


class TourGuides(TemplateView):
    template_name = 'tourism/tourguides.html'


class Bookings(TemplateView):
    template_name = 'tourism/bookings.html'


class AdminBooking(TemplateView):
    template_name = 'tourism/adminbooking.html'


class BookDelete(DeleteView):
    model = Book
    template_name = 'tourism/bookingdelete.html'
    success_url = reverse_lazy('get_Book')


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'tourism/bookingupdate.html'
    success_url = reverse_lazy('get_Book')


class FlightDelete(DeleteView):
    model = Flight
    template_name = 'tourism/flightdelete.html'
    success_url = reverse_lazy('get_Flight')


class FlightUpdate(UpdateView):
    model = Flight
    fields = '__all__'
    template_name = 'tourism/flightupdate.html'
    success_url = reverse_lazy('get_Flight')


class HotelDelete(DeleteView):
    model = Hotel
    template_name = 'tourism/hoteldelete.html'
    success_url = reverse_lazy('get_Hotel')


class HotelUpdate(UpdateView):
    model = Hotel
    fields = '__all__'
    template_name = 'tourism/hotelupdate.html'
    success_url = reverse_lazy('get_Hotel')
