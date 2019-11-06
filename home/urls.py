from . import views
from django.urls import path

urlpatterns = [

	path('', views.Beforlogin, name='beforlogin'),
    path('home/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('/workshop/', views.Loadworkshop, name='workshop'),
    path('/chobit/', views.Loadchobit, name='chobit'),
    path('/ban/', views.Loadban, name='ban'),
    path('/traodoi/', views.Loadtraodoi, name='traodoi'),
    path('/chiase/', views.Loadchiase, name='chiase'),
    path('/mentormentee/', views.Loadmentormentee, name='mentormentee'),
    path('/prechobit/', views.Loadprechobit, name='prechobit'),
    path('/timmentor/', views.Loadtimmentor, name='timmentor'),
    path('/timmentee/', views.Loadtimmentee, name='timmentee'),
    path('/trangcanhan/', views.Loadtrangcanhan, name='trangcanhan'),


]