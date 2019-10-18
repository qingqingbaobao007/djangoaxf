from django.conf.urls import url

from CartApp import views

urlpatterns=[
    url(r'^cart/',views.cart,name='cart'),
    # 添加到购物车
    url(r'^addToCart/',views.addToCart,name='addToCart'),
    # 减少商品数量
    url(r'^subCart/',views.subCart,name='subCart'),
    # 改变选中状态
    url(r'^changeStatus/',views.changeStatus,name='changeStatus'),
    # 全选
    url(r'^allSelect/',views.allSelect,name='allSelect'),


]