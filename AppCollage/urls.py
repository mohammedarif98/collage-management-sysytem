from AppCollage import views
from django.urls import path

urlpatterns=[
    path("",views.Index,name="Index"),
    path("Admin_Home",views.Admin_Home,name="Admin_Home"),
    path('Login_SignUp_Page',views.Login_SignUp_Page,name="Login_SignUp_Page"),
    path("CoursePage",views.CoursePage,name="CoursePage"),
    path("AddCourse",views.AddCourse,name="AddCourse"),
    path("Teacher_SignUp",views.Teacher_SignUp,name="Teacher_SignUp"),
    path("Teacher_Login",views.Teacher_Login,name="Teacher_Login"),
    path("Teacher_LogOut",views.Teacher_LogOut,name="Teacher_LogOut"),
    path("Add_Student",views.Add_Student,name="Add_Student"),
    path("Student_Page",views.Student_Page,name="Student_Page"),
    path("Student_Details",views.Student_Details,name="Student_Details"),
    path('Course_Details',views.Course_Details,name='Course_Details'),
    path('Teacher_Details',views.Teacher_Details,name='Teacher_Details'),
    path('Delete_Teacher/<int:id>',views.Delete_Teacher,name="Delete_Teacher"),
    path('Profile',views.Profile,name='Profile'),
    path("Edit_Page",views.Edit_Page,name='Edit_Page'),
    path('Edit_Profile',views.Edit_Profile,name="Edit_Profile"),


#     path('Edit_Page/<int:pk>',views.Edit_Page,name='Edit_Page'),
#     path('Edit_Profile/<int:pk>',views.Edit_Profile,name='Edit_Profile'),
]