from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_admin,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('', views.index, name='index'),
    path('create/',views.create,name='create'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit_des/<int:id>',views.edit_designation,name='edit_des'),
    path('delete_des/<int:id>',views.delete_designation,name='delete_des'),
    path('edit_role/<int:id>', views.edit_role, name='edit_role'),
    path('delete_role/<int:id>', views.delete_role, name='delete_role'),
    path('create_leave/',views.create_leave,name='create_leave'),
    path('all_leave/',views.leaveapply,name='leave_all'),
    path('edit_leave/<int:id>', views.edit_leave, name='edit_leave'),
    path('delete_leave/<int:id>',views.delete_leave,name='delete_leave'),
    path('salary/', views.salary, name='salary'),
    # ... more patterns ...
]

