from os import name
from django.urls import path
from django.utils.regex_helper import normalize
from dashboard import views

urlpatterns = [
    path("", views.index, name="PrintHome"),
    path("supersignup", views.supersignup, name="SuperSignupPage"),
    path("superlogin", views.superlogin, name="SuperLoginPage"),
    path("superlogout", views.superlogout, name="SuperLogout"),
    path("adminsignup", views.adminsignup, name="AdminSignupPage"),
    path("adminlogin", views.adminlogin, name="AdminLoginPage"),
    path("adminlogout", views.adminlogout, name="AdminLogout"),
    path("mansignup", views.mansignup, name="ManagerSignupPage"),
    path("manlogin", views.manlogin, name="ManagerLoginPage"),
    path("manlogout", views.manlogout, name="ManagerLogout"),
    path("opesignup", views.opesignup, name="OperationSignupPage"),
    path("opelogin", views.opelogin, name="OperationLoginPage"),
    path("opelogout", views.opelogout, name="OperationLogout"),
    # path('productsize', views.addsize, name="productsize"),
    # path('productcolor', views.addcolor, name="productcolor"),
    # path('producttype', views.addtype, name="producttype"),
    # path('productquantity', views.addquantity, name="productquantity"),
    path('productform', views.productform, name="ProductFormpage"),
    # path('productview', views.productview, name="ProductViewPage"),
    path('sendgmail', views.send_gmail, name="SendGmailPage"),
    # path("cuponcode", views.cuponcode, name="CuponcodePage"),
    path('addcupon', views.addcupon, name="addcuponpage"),
    path('addcategories', views.addcategory, name="AddCategoryPage"),
    path('categories', views.addcategory, name="addcategory"),
    path('addsubcategories', views.addsubcategories, name="addsubcategory"),
    path('subcategories', views.addsubcategories, name="SubCategoryView"),
    path('addbanner', views.addbanner, name="AddbannerPage"),
    path('banner', views.banner, name="BannerPage"),
    path('addblogcategory', views.addblogcategory, name="addblogcategory"),
    path('blogcategory', views.blogcategory, name="BlogcategoryPage"),
    path('deleteproduct/<int:ids>/', views.Remove_Product, name="deleteproduct"),
    path('simpleproduct/<str:ids>/', views.simpleP, name="addsimpleproduct"),
    path('addproductselect', views.addproductselect, name="addproductselect"),
    path('variableproduct/<str:ids>/', views.VariableP, name="variableproduct"),
    path('variableattributes/<str:ids>/', views.attributeVariable, name="variableattributes"),
    path('globalattributes', views.globalAttributes, name="globalattributes"),
    path('gsmtype', views.gsType, name="gsmtype"),
    path('voltype', views.voType, name="voltype"),
    path('sizes', views.sizeglobal, name="sizes"),
    path('gstglobal', views.gst, name="gst"),
    path('handlegroup', views.handleGroup, name="handlegroup"),
    path('shopbycate', views.shopbycate, name="shopbycate"),
    path('allproductlist', views.allProduct, name="allproductlist"),
    path('expressshiping', views.ExpressShipping, name="expressshipping"),
    path('plusshipping', views.PlusShipping, name="plusshipping"),
    path('coupon', views.Coupon, name="coupon"),
    path('bestsellersimple', views.Best_Seller_simp, name="bestsellersimple"),
    path('bestsellervariable', views.Best_Seller_variab, name="bestsellervariable"),
    path('bestsellergrouped', views.Best_Seller_grop, name="bestsellergrouped"),
    path('bestoffers', views.bestoffers, name="bestoffers"),
    path('newlaunches', views.New_launchesSimple, name="newlauches"),
    path('newlaunchesvariable', views.New_launchesVariable, name="newlaunchesvariable"),
    path('newlaunchesgrouped', views.New_launchesGrouped, name="newlaunchesgrouped"),
    path('happyclients', views.happy_clients, name="happyclients"),
    path('blogaddhome', views.blogAdd, name="blogaddhome"),
    path('groupedproducts/<str:ids>/', views.GroupP, name="groupedproducts"),
]