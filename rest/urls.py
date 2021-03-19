from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # home links
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('page/',views.page,name='page'),
    path('logout/',views.log_out,name='logout'),
    # redirecting to details page
    path('teacher/<str:pk>/',views.teachdetail,name='teachdetail'),
    path('student/<str:pk>/',views.studdetail,name='studdetail'),
    # for deleting data from database
    path('deleteteach/<str:pk>/',views.deleteteach,name='deleteteach'),
    path('deletestud/<str:pk>/',views.deletestud,name='deletestud'),
    # adding data to database
    path('page/add/',views.add,name='add'),
    path('page/addstudent/',views.addstudent,name='addstudent'),
    # to reset password
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="resetpass.html"),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="passsent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="resetform.html"),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="resetdone.html"),name='password_reset_complete'),
]