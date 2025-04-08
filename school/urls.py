from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'school'

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    # Portal URLs
    path('student-portal/', views.StudentPortalView.as_view(), name='student_portal'),
    path('parent-portal/', views.ParentPortalView.as_view(), name='parent_portal'),
    path('teacher-portal/', views.TeacherPortalView.as_view(), name='teacher_portal'),
    
    path('leadership/', views.LeadershipTeamView.as_view(), name='leadership'),
    path('tuition/', views.TuitionFeesView.as_view(), name='tuition'),
    path('dates/', views.ImportantDatesView.as_view(), name='dates'),
    path('student-life/', views.StudentLifeView.as_view(), name='student_life'),
    path('parents-corner/', views.ParentsCornerView.as_view(), name='parents_corner'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('privacy-policy/', views.PrivacyPolicyView.as_view(), name='privacy_policy'),
] 