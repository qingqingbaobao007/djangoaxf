from django.conf.urls import url

from OrderApp import views

urlpatterns=[
    url(r'^make_order/',views.make_order,name='make_order'),

    url(r'^order_detail/',views.order_detail,name='order_detail'),

    # 支付
    url(r'^testpay/',views.testpay,name='testpay'),
    # url(r'^testpay1/',views.testpay1,name='testpay1')
]