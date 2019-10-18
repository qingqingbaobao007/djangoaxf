from alipay import AliPay
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from CartApp.models import AxfCart
from CartApp.views import get_total_price
from OrderApp.models import AxfOrderGoods, AxfOrder
from axf.settings import APP_PRIVATE_KEY_STRING, ALIPAY_PUBLIC_KEY_STRING


def order_detail(request):
    order_id = request.GET.get('order_id')
    order = AxfOrder.objects.get(pk=order_id)

    context = {
        'order':order,
        'total_price':order.axfordergoods_set.first().og_total_price
    }

    return render(request,'axf/order/order_Detail.html',context=context)


def make_order(request):
    # 创建order对象  -->为什么orderGoods创建的对象
    user_id = request.session.get('user_id')
    order = AxfOrder()
    order.o_user_id = user_id
    order.save()

    # 创建ordergoods对象
    orderGoods = AxfOrderGoods()
    orderGoods.og_order = order

    # 将购物车中选中的数据 交给ordergoods的og_goods
    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)

    for cart in carts:
        orderGoods = AxfOrderGoods()
        orderGoods.og_order = order
        orderGoods.og_goods=cart.c_goods
        orderGoods.og_total_price = get_total_price(user_id)

        #0g_price 就是商品de 数量
        orderGoods.og_goods_num=cart.c_goods_num
        orderGoods.save()

        cart.delete()

    data={
        'msg':'OK',
        'status':200,
        'order_id':order.id
    }



    return JsonResponse(data=data)

def testpay(request):
    alipay = AliPay(
        appid="2016101200665425",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=APP_PRIVATE_KEY_STRING,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=ALIPAY_PUBLIC_KEY_STRING,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=False  # 默认False
    )

    subject = "母婴用品"
    # 手机网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_wap_pay(
        out_trade_no="110",
        total_amount=1314,
        subject=subject,
        return_url="https://www.baidu.com",
        notify_url="https://www.baidu.com"  # 可选, 不填则使用默认notify url
    )
    return redirect('https://openapi.alipaydev.com/gateway.do?' + order_string)
