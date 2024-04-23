from io import BytesIO
from geopy.distance import geodesic
from django.shortcuts import render
from . import models
from django.http import HttpResponse, Http404
import qrcode
import socket, requests


def index(request):
    template = "chain/index.html"

    return render(request, template)


def get_ip_address():
    """ Try and get the IP address or raise a 404 error. """
    try: 
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        raise Http404
            
    return ip_address


def qrCode(request, pk):
    process = models.Product.objects.get(pk=pk)
    try: 
        url = f"http://{get_ip_address()}:8000{process.get_product_history_url()}"
        img = qrcode.make(url)

        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)
        return HttpResponse(buffer.getvalue(), content_type="image/png")
    except Http404:
        return render(request, 'chain/errors/qrcode_error.html')


def get_carbon_footprint(coord1, coord2, co2perkilometer):
    distance = geodesic(coord1, coord2).kilometers
    return distance * co2perkilometer


def get_rating(totalC02):
    if totalC02 <= 10000:
        return "BEST"
    elif totalC02 <= 250000:
        return "GOOD"
    elif totalC02 <= 500000:
        return "BAD"
    else:
        return "WORST"


def product_history(request, pk):
    template_name = "chain/producthistory.html"
    product = models.Product.objects.get(pk=pk)
    product_processes = product.product_process_set.all()
    cow = product.cattle
    cow_location = cow.location
    cattle_processes = cow.cattle_process_set.all()

    totalCO2 = 0
    previous_coords = (cow_location.latitude, cow_location.longitude)
    all_processes = [*cattle_processes, *product_processes]
    for process in all_processes:
        location = process.location
        process_coords = (float(location.latitude), float(location.longitude))
        transport_mode = process.transportation_mode
        co2perkilo = float(transport_mode.co2perkilo)
        totalCO2 += get_carbon_footprint(previous_coords, process_coords, co2perkilo)
        previous_coords = process_coords

    rating = get_rating(totalCO2)
    totalCO2 = "{:,.2f}".format(totalCO2)
    context = {
        "co2": totalCO2,
        "rating": rating,
        "processes": all_processes,
        "cow": cow,
        "product": product,
    }

    return render(request, template_name, context)
