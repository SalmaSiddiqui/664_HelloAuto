from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView
# from django.core.urlresolvers import reverse, reverse_lazy, resolve

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', views.AutoListView.as_view()),
    path('autos', views.AutoListView.as_view(), name='autos'),
    path('auto/<int:pk>', views.AutoDetailView.as_view(), name='auto_detail'),
    # path('ad/create',
    #     views.AdCreateView.as_view(success_url=reverse_lazy('ads')), name='ad_create'),
    # path('ad/<int:pk>/update',
    #     views.AdUpdateView.as_view(success_url=reverse_lazy('ads')), name='ad_update'),
    path('auto/<int:pk>/delete',
        views.AutoDeleteView.as_view(success_url=reverse_lazy('autos')), name='auto_delete'),
    path('auto/create',
        views.AutoFormView.as_view(success_url=reverse_lazy('autos')), name='auto_create'),
    path('auto/<int:pk>/update',
        views.AutoFormView.as_view(success_url=reverse_lazy('autos')), name='auto_update'),
    # path('auto_picture/<int:pk>',
    #     views.stream_file, name='auto_picture'),
    path('auto/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('autos')), name='comment_delete'),
    # path('auto/<int:pk>/favorite',
    #     views.AddFavoriteView.as_view(), name='auto_favorite'),
    # path('auto/<int:pk>/unfavorite',
    #     views.DeleteFavoriteView.as_view(), name='auto_unfavorite'),

]
