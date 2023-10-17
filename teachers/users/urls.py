from django.urls import path
from .views import (
    students,
    get_associated_teachers,
    get_associated_students,
    generate_certificate,
    view_certificate,
)

urlpatterns = [
    path("", students),
    path("get_teachers_for_student/<int:std_id>/", get_associated_teachers),
    path("get_associated_students/<int:teacher_id>/", get_associated_students),
    path("generate_certificate/", generate_certificate, name="generate_certificate"),
    path("view_certificate/<int:certificate_id>/", view_certificate, name='view_certificate'),
]
