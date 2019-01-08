from django.urls import path
from patient import views as patientviews
from hospital import views as hospitalviews
from municipal import views as municipalviews


urlpatterns = [
    path('hospital/list/', hospitalviews.HospitalList.as_view(), name = 'hospital_list'),
    path('hospital/detail/<username>', hospitalviews.HospitalDetail.as_view(), name = 'hospital_detail'),
    path('patient/list/', patientviews.PatientList.as_view(), name = 'patient_list'),
    path('patient/detail/<slug:username>', patientviews.PatientDetail.as_view(), name = 'patient_detail'),
    path('municipal/list/', municipalviews.MunicipalList.as_view(), name = 'municipal_list'),
    path('municipal/detail/<slug:username>', municipalviews.MunicipalDetail.as_view(), name = 'municipal_detail'),
]