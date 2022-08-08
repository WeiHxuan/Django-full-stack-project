from django.urls import path
import shopapp.views
urlpatterns = [#二级路由
    path('all_phones/', shopapp.views.get_json),
    path('shop_info/', shopapp.views.shop_info),
    path('getall/', shopapp.views.getall),
    path('save/', shopapp.views.save),
    path('save_form/', shopapp.views.save_form),
    path('delete/', shopapp.views.delete),
    path('update/', shopapp.views.update),

]