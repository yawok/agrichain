from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .. import models, serialisers


@api_view(["GET", "POST"])
def locations(request, format=None):
    if request.method == "GET":
        locations = models.Location.objects.all()
        serialised_locations = serialisers.LocationSerializer(locations, many=True)
        return Response(serialised_locations.data)

    if request.method == "POST":
        serialised_locations = serialisers.LocationSerializer(data=request.data)
        if serialised_locations.is_valid():
            serialised_locations.save()
            return Response(serialised_locations.data, status=status.HTTP_201_CREATED)
        return Response(serialised_locations.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def location(request, pk, format=None):
    try:
        location = models.Location.objects.get(pk=pk)
    except models.Location.DoesNotExist as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serialised_location = serialisers.LocationSerializer(location)
        return Response(serialised_location.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serialised_location = serialisers.LocationSerializer(
            location, data=request.data
        )
        if serialised_location.is_valid():
            serialised_location.save()
            return Response(serialised_location.data, status=status.HTTP_200_OK)
        return Response(serialised_location.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TypesList(APIView):
    """Base class for all types."""

    def get(self, request, format=None):
        objects = self.model.objects.all()
        serialiser = self.serialiser_class(objects, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serialiser = self.serialiser_class(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


class TypeDetails(APIView):
    """Base class for all types detail endpoints."""

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist as e:
            raise Http404

    def get(self, request, pk, format=None):
        type_object = self.get_object(pk)
        serialiser = self.serialiser_class(type_object)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        type_object = self.get_object(pk)
        serialiser = self.serialiser_class(type_object, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_200_OK)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        type_object = self.get_object(pk)
        type_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrganizationTypeList(TypesList):
    model = models.Organisation_type
    serialiser_class = serialisers.OrganizationTypeSerializer


class TransportationModeList(TypesList):
    model = models.Transportation_mode
    serialiser_class = serialisers.TransportionModeSerializer


class ProcessTypeList(TypesList):
    model = models.Process_type
    serialiser_class = serialisers.ProcessTypeSerializer


class BreedList(TypesList):
    model = models.Breed
    serialiser_class = serialisers.BreedSerializer


class OrganizationTypeDetail(TypeDetails):
    model = models.Organisation_type
    serialiser_class = serialisers.OrganizationTypeSerializer


class TransportationModeDetail(TypeDetails):
    model = models.Transportation_mode
    serialiser_class = serialisers.TransportionModeSerializer


class ProcessTypeDetail(TypeDetails):
    model = models.Process_type
    serialiser_class = serialisers.ProcessTypeSerializer


class BreedDetail(TypeDetails):
    model = models.Breed
    serialiser_class = serialisers.BreedSerializer


class OrganisationsList(APIView):

    def get(self, request, format=None):
        organisations = models.Organisation.objects.all()
        serialiser = serialisers.OrganizationSerializer(organisations, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serialiser = serialisers.OrganizationSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganisationDetail(APIView):

    def get_organisation(self, pk):
        try:
            return models.Organisation.objects.get(pk=pk)
        except models.Organisation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        organisation = self.get_organisation(pk)
        serialiser = serialisers.OrganizationSerializer(organisation)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        organisation = self.get_organisation(pk)
        serialiser = serialisers.OrganizationSerializer(organisation, data=request.data)
        if serialiser.is_valid():
            return Response(serialiser.data, status=status.HTTP_200_OK)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        organisation = self.get_organisation(pk)
        organisation.delete()
        return Response(status=status.HTTP_200_OK)


class CattleList(APIView):

    def get(self, request, format=None):
        organisations = models.Cattle.objects.all()
        serialiser = serialisers.CattleSerializer(organisations, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serialiser = serialisers.CattleSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


class CattleDetail(APIView):

    def get_cattle(self, pk):
        try:
            return models.Cattle.objects.get(pk=pk)
        except models.Cattle.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cattle = self.get_cattle(pk)
        serialiser = serialisers.CattleSerializer(cattle)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        cattle = self.get_cattle(pk)
        serialiser = serialisers.CattleSerializer(cattle, data=request.data)
        if serialiser.is_valid():
            return Response(serialiser.data, status=status.HTTP_200_OK)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cattle = self.get_cattle(pk)
        cattle.delete()
        return Response(status=status.HTTP_200_OK)


class ProductsList(APIView):

    def get(self, request, format=None):
        products = models.Product.objects.all()
        serialiser = serialisers.ProductProcessSerializer(products, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        product = request.data
        serialiser = serialisers.ProductProcessSerializer(product)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetails(APIView):

    def get_product(self, pk):
        try:
            return models.Product.objects.get(pk=pk)
        except models.Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_product(pk)
        serialiser = serialisers.BreedSerializer(product)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        product = self.get_product(pk)
        serialiser = serialisers.ProductSerializer(product, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_200_OK)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

    def determine_version(self, request, pk, format=None):
        product = self.get_product(pk)
        product.delete()
        return Response(product.data, status=status.HTTP_204_NO_CONTENT)
