from django.urls import include, path

from api.v1.report.business_unit.views import BusinessUnitView

urlpatterns = [
    path('data/', BusinessUnitView.as_view({'get': 'data'})),

    path('chart/', BusinessUnitView.as_view({'get': 'chart'})),
    path('chart_loan/', BusinessUnitView.as_view({'get': 'chart_loan'})),

    #SCREEN C4
    path('chart_hr/', BusinessUnitView.as_view({'get': 'chart_hr'})),
    path('chart_kpi/', BusinessUnitView.as_view({'get': 'chart_kpi'})),
    path('chart_income/', BusinessUnitView.as_view({'get': 'chart_income'})),
    path('chart_business/', BusinessUnitView.as_view({'get': 'chart_business'})),

    path('customer/', BusinessUnitView.as_view({'get': 'customer'})),
    path('region/', BusinessUnitView.as_view({'get': 'region'})),

]
