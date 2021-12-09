from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_start_page, name='start'),
    path('error', views.get_error_page, name='error'),
    path('generate', views.get_generate_page, name='generate'),
    path('generate/<int:quiz_set_id>', views.get_generate_result_page, name='generate-result'),
    path('solve/<int:quiz_set_id>', views.get_solve_page, name='solve'),
    path('result/<int:quiz_set_id>/<int:result_id>', views.get_result_page, name='result'),
]
