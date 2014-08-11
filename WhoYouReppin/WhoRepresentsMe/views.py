from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import requests
from forms import EnterAddressForm
from settings_hidden import GOOGLE_GEOCODE_API_KEY, SUNLIGHT_API_KEY

def index(request):
	form = EnterAddressForm()
	if request.method == 'POST':
		form = EnterAddressForm(request.POST)
	if form.is_valid():
		address = form.cleaned_data['address']
		return HttpResponseRedirect('/WhoRepresentsMe/showLegislators/%s' % (address))
	return render(request, 'WRMLandingPage.html', {'form':form})

def showLegislators(request, address):
	# First call the Google geocode API to get latitude and longitude
	url = "https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key="+GOOGLE_GEOCODE_API_KEY
	r = requests.get(url)
	results = r.json()		# Save your answer to results
	lat = results['results'][0]['geometry']['location']['lat']
	lng = results['results'][0]['geometry']['location']['lng']

	# Now call Open States and get state legislators
	url = "http://openstates.org/api/v1//legislators/geo/?lat="+str(lat)+"&long="+str(lng)+"&apikey="+SUNLIGHT_API_KEY
	r = requests.get(url)
	state_legislators = r.json() 

	# And finally call Open Congress to find federal representatives
	url = "http://congress.api.sunlightfoundation.com/legislators/locate?latitude="+str(lat)+"&longitude="+str(lng)+"&apikey="+SUNLIGHT_API_KEY
	r = requests.get(url)
	results = r.json() 
	congressional_legislators = results['results']

	form = EnterAddressForm()
	if request.method == 'POST':
		form = EnterAddressForm(request.POST)
	if form.is_valid():
		address = form.cleaned_data['address']
		return HttpResponseRedirect('/WhoRepresentsMe/showLegislators/%s' % (address))
	return render(request, 'results.html', {'lat':lat, 'lng':lng, 'form':form, 'state_legislators':state_legislators, 'congressional_legislators': congressional_legislators})
