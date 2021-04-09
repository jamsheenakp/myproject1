from django.urls import path
from  . import views
app_name="myapp"
urlpatterns = [
    path('adm_add_branch/', views.adm_add_branch),
    path('adm_add_branch_manager/',views.adm_add_branch_manager),
    path('adm_add_category/', views.adm_add_category),
    path('adm_add_Add_item/', views.adm_add_Add_item),
    path('adm_add_subcategory/', views.adm_add_subcategory),
    path('adm_change_password/', views.adm_change_password),
    path('adm_edit_branch/<str:id>', views.adm_edit_branch),
    path('adm_updatetbranch/',views.adm_updatetbranch),
    path('adm_edit_branchmanager/<str:id>', views.adm_edit_branchmanager),
    path('adm_updatemanager/', views.adm_updatemanager),
    path('adm_edit_category/<str:id>', views.adm_edit_category),
    path('adm_updatecategory/', views.adm_updatecategory),
    path('adm_edit_item/<str:id>', views.adm_edit_item),
    path('adm_updateitem/', views.adm_updateitem),
    path('adm_edit_subcategory/<str:id>', views.adm_edit_subcategory),
    path('adm_updatesubcategory/', views.adm_updatesubcategory),
    path('', views.adm_Login),
    path('adm_purchased_item/', views.adm_purchased_item),
    path('adm_review/', views.adm_review),
    path('adm_view_branch/', views.adm_view_branch),
    path('adm_deletebranch/<str:id>', views.adm_deletebranch),
    path('adm_view_branch_manager/', views.adm_view_branch_manager),
    path('adm_view_branch_managerpost/', views.adm_view_branch_managerpost),
    path('adm_deletemanager/<str:id>', views.adm_deletemanager),
    path('adm_view_category/', views.adm_view_category),
    path('adm_deletecategory/<str:id>', views.adm_deletecategory),
    path('adm_view_item/', views.adm_view_item,name="adm_view_item"),
    path('adm_deleteitem/<str:id>', views.adm_deleteitem),
    path('adm_view_order_details/', views.adm_view_order_details),
    path('adm_view_rating/', views.adm_view_rating),
    path('adm_view_subcategory/', views.adm_view_subcategory),
    path('adm_deletesubcategory/<str:id>', views.adm_deletesubcategory),
    path('adm_home/', views.adm_home),
    path('adm_index/',views.adt)
]