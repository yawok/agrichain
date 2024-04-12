from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .. import models, serialisers


class ProcessesList(APIView):
    """Base class for list of processes."""

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


class ProcessDetails(APIView):
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


class CattleProcessList(ProcessesList):
    serialiser_class = serialisers.CattleProcessSerializer
    model = models.Cattle_process


class CattleProcessDetails(ProcessDetails):
    serialiser_class = serialisers.CattleProcessSerializer
    model = models.Cattle_process


class ProductProcessList(ProcessesList):
    serialiser_class = serialisers.ProductProcessSerializer
    model = models.Product_process


class ProductProcessDetails(ProcessDetails):
    serialiser_class = serialisers.ProductProcessSerializer
    model = models.Product_process
