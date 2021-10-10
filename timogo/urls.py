
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required


from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/manage_articles', login_required(views.go_to_administration), name='go_to_administration'),
    path('', views.post_list_index, name ='post_list_index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('account/manage_articles/create_post', views.createPost,  name='create_post'),
    path('account/manage_articles/update_post/<str:pk>', views.updatePost, name='update_post'),
    path('account/manage_articles/delete_post/<str:pk>', views.deletePost, name='delete_post'),

    path('post/<str:pk>/add_comment', views.add_comment, name='add-comment'),
    path('post/<str:pk>/delete_comment', views.delete_comment, name='delete-comment'),

]
