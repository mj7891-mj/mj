from django.urls import path
from app01 import views

urlpatterns = [
    # 部门管理
    path("dept/list/", views.depart_list),
    path("dept/add/", views.depart_add),
    path("dept/edit/<int:pk>/", views.depart_edit),
    path("dept/delete/<int:pk>/", views.depart_delete),

    # 用户管理
    path("user/list/", views.user_list),
    path("user/add/", views.user_add),
    path("user/edit/<int:pk>/", views.user_edit),
    path("user/delete/<int:pk>/", views.user_delete),


    # 靓号管理
    path("pretty/list/", views.pretty_list),
    path("pretty/add/", views.pretty_add),
    path("pretty/edit/<int:pk>/", views.pretty_edit),
    path("pretty/delete/<int:pk>/", views.pretty_delete),
]
