from django.urls import path
from .views import EmployeeDetails, EmployeeInfo


urlpatterns = [
    path("emp/", EmployeeDetails.as_view(), name="emp"),
    path("emp/<int:id>/", EmployeeInfo.as_view())
]
