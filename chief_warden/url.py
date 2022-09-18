from django.urls import path
from . import views

urlpatterns = [
    path('int/', views.chief_warden, name='chief_warden_home'),
               path('', views.index, name='chief_warden_home'),
               path('student/', views.student, name='student'),
               path('hostel', views.hostel, name='hostel_block'),
               path('list_of_managers/', views.manager_list, name='list_of_managers'),
               path('manager_update/<str:pk>', views.update_managers, name='update'),
               path('block/', views.create_block, name='create_block_view'),
               path('create/warden/', views.create_warden, name='create_warden'),
               path('list_of_wardens/', views.warden_list, name='warden_list_name'),
               path('room/', views.create_room, name='create_room'),
               path('floor/', views.create_floor, name='create_floor'),
               path('update/student_room/<str:pk>', views.update_student_room, name='update_student_room_name'),
               path('floors/<str:pk>', views.chief_floors, name='chief_floors_page'),
               path('rooms/<str:pk>', views.chief_rooms, name='chief_rooms_page'),
               path('room/student/info/<str:pk>', views.student_view, name='student_room_info'),
               path('waden/update/<str:pk>',views.update_warden,name='update_warden_name'),
               path('search/', views.search, name='Search'),
               ]
