from django.urls import path
from . import views
from .endpoints import endpoints, process_endpoints
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("locations/", endpoints.locations),
    path("locations/<int:pk>/", endpoints.location),
    path("organisation-types/", endpoints.OrganizationTypeList.as_view()),
    path("transpotation-modes/", endpoints.TransportationModeList.as_view()),
    path("process-types/", endpoints.ProcessTypeList.as_view()),
    path("breeds/", endpoints.BreedList.as_view()),
    path("transpotation-modes/<int:pk>/", endpoints.TransportationModeDetail.as_view()),
    path("process-types/<int:pk>/", endpoints.ProcessTypeDetail.as_view()),
    path("breeds/<int:pk>/", endpoints.BreedDetail.as_view()),
    path("organisations/", endpoints.OrganisationsList.as_view()),
    path("organisations/<int:pk>/", endpoints.OrganisationDetail.as_view()),
    path("cattles/", endpoints.CattleList.as_view()),
    path("cattle/<int:pk>/", endpoints.CattleDetail.as_view()),
    path("products/", endpoints.ProductsList.as_view()),
    path("product/<int:pk>/", endpoints.ProductDetails.as_view()),
    path("cattle-processes/", process_endpoints.CattleProcessList.as_view()),
    path("cattle-processes/<int:pk>/", process_endpoints.CattleProcessList.as_view()),
    path("product-processes", process_endpoints.ProductProcessList.as_view()),
    path(
        "product-processes/<int:pk>/", process_endpoints.ProductProcessDetails.as_view()
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
