from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *

# Create your views here. 
def hotel_image_view(request): 

	if request.method == 'POST': 
		form = HotelForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return redirect('hotel_images') 
	else: 
		form = HotelForm() 
	return render(request, 'index.html', {'form' : form}) 



# Python program to view 
# for displaying images 

def display_hotel_images(request): 

	if request.method == 'GET': 

		# getting all the objects of hotel. 
		Hotels = Hotel.objects.all() 
		return render(request, 'display_hotel_images.html',{'hotel_images' : Hotels}) 
