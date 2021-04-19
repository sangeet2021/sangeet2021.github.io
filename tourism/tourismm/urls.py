from django.urls import path
from . views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', homePageView.as_view(), name='home'),
    path('discover/', discoverView, name='discover'),

    path('discover/add', CreateDiscoverView.as_view(), name='addDiscover'),

    path('discover/view/<int:pk>/',
         DetailDiscoverView.as_view(), name='viewdiscover'),
    path('discover/add', discoverHal.as_view(), name='addDiscover'),
    path('ttd/add', CreateTtdView.as_view(), name='addTtd'),
    path('ttd/view/<int:pk>/', DetailTtdView.as_view(), name='viewttd'),
    path('ttd/<int:pk>/delete', TtdDelete.as_view(), name='deletettd'),
    path('ttd/<int:pk>/update', TtdUpdate.as_view(), name='updatettd'),
    path('discover/<int:pk>/delete',
         DiscoverDelete.as_view(), name='deletediscover'),
    path('discover/<int:pk>/update',
         DiscoverUpdate.as_view(), name='updatediscover'),
    path('login/', Login.as_view(), name='login'),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('book/', Bookings.as_view(), name='allbookings'),
    path('bookings/', BookFormView.as_view(), name='book'),
    path('hotelbooking/', HotelFormView.as_view(), name='hotelbook'),
    path('flightbooking/', FlightFormView.as_view(), name='flightbook'),

    path('getBook/', get_Book, name='get_Book'),
    path('getFlight/', get_Flight, name='get_Flight'),
    path('getHotel/', get_Hotel, name='get_Hotel'),
    path('getusers', userView, name='get_Users'),
    path('userdelete/<int:pk>/', UserDelete.as_view(), name='user_delete'),
    path('userupdate/<int:pk>/', UserUpdate.as_view(), name='user_update'),
    path('bookdelete/<int:pk>/', BookDelete.as_view(), name='book_delete'),
    path('bookupdate/<int:pk>/', BookUpdate.as_view(), name='book_update'),
    path('flightdelete/<int:pk>/', FlightDelete.as_view(), name='flight_delete'),
    path('flightupdate/<int:pk>/', FlightUpdate.as_view(), name='flight_update'),
    path('hoteldelete/<int:pk>/', HotelDelete.as_view(), name='hotel_delete'),
    path('hotelupdate/<int:pk>/', HotelUpdate.as_view(), name='hotel_update'),
    path('adminpanel/', AdminPanel.as_view(), name='adminpanel'),
    path('adminbooking/', AdminBooking.as_view(), name='adminbooking'),
    path('add/', Add.as_view(), name='add'),
    path('tourguides/', TourGuides.as_view(), name='tourguides'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
