from django.urls import path

from api.v1.employee.views import EmployeeView

urlpatterns = [
    path('emp_list/', EmployeeView.as_view({'get': 'emp_list'})),
    path('emp_detail/', EmployeeView.as_view({'get': 'emp_detail'})),
    path('emp_detail_kpi/', EmployeeView.as_view({'get': 'emp_detail_kpi'})),
    path('emp_detail_decision/', EmployeeView.as_view({'get': 'emp_detail_decision'})),
    path('emp_detail_work_process/', EmployeeView.as_view({'get': 'emp_detail_work_process'})),

    # path('dep_list/', EmployeeView.as_view({'get': 'dep_list'})),
]
