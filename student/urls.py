from django.urls import include, path
from . import views

urlpatterns = [
    # path("<int:st_id>/", views.stu_detail, name='stu_detail'),
    # path("<int:st_id>/", views.stu_index, name="stu_index"),
    path("", views.stu_index, name="stu_index"),
    path("<int:st_id>/",views.student_sem, name="student_sem")
    

]