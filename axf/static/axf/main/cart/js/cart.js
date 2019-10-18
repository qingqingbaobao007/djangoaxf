$(function () {
    $('.subShopping').click(function () {
        var $button = $(this);
        var $div = $button.parent().parent();

        var cartid = $div.attr('cartid');

        $.post('/axfcart/subCart/',
            {'cartid':cartid},
            function (data) {
                if (data['status']=== 200){
                    $button.next().html(data['c_goods_num']);
                    $('#total_price').html(data['total_price'])
                }else{
                    $div.remove();
                    $('#total_price').html(data['total_price'])
                }
            }
            )

    })

    $('.confirm').click(function () {
        var $confirm = $(this);
        var $div = $confirm.parent();
        var cartid = $div.attr('cartid')

        $.ajax(
            {
                url:'/axfcart/changeStatus/',
                data:{'cartid':cartid},
                type:'GET',
                dataType:'json',
                success:function (data) {
                    if (data['status']===200){
                        if (data['c_is_select']){
                            $confirm.find('span').find('span').html('✔')
                            $('#total_price').html(data['total_price'])
                        }else{
                            $confirm.find('span').find('span').html('')
                            $('#total_price').html(data['total_price'])
                        }if(data['is_all_select']){
                            $('#all_select').find('span').find('span').html('✔')
                        }else{
                            $('#all_select').find('span').find('span').html('')
                        }
                    }
                }
            }

        )

    })
    //    点击全选
//          把购物车页面中的选中的放在一个列表中
//          把购物车页面中的未选中的放在一个列表中

    $('#all_select').click(function () {
        var $all_select = $('#all_select');

        var select_list = [];
        var unselect_list = [];

        var $confirm = $('.confirm');


        $confirm.each(function () {
            var cartid = $(this).parent().attr('cartid');

            if($(this).find('span').find('span').html()){
                select_list.push(cartid);
            }else{
                unselect_list.push(cartid);
            }

        })

        if(unselect_list.length > 0){
            $.getJSON('/axfcart/allSelect/',
                    {'cartidlist':unselect_list.join('#')},
                    function (data) {
                        if(data['status'] == 200){
                            $confirm.find('span').find('span').html('✔');
                            $('#all_select').find('span').find('span').html('✔');
                            $('#total_price').html(data['total_price']);
                        }
                    })
        }else{

            $.getJSON('/axfcart/allSelect/',
                    {'cartidlist':select_list.join('#')},
                    function (data) {
                        if(data['status'] == 200){
                            $confirm.find('span').find('span').html('');
                            $('#all_select').find('span').find('span').html('');
                            $('#total_price').html(data['total_price']);
                        }
                    })
            
        }
    })
    $('#make_order').click(function () {
        var $confirm  = $('.confirm');

        var select_list = [];
        var unselect_list = [];

        $confirm.each(function () {

            var cartid = $(this).parent().attr('cartid');
            if($(this).find('span').find('span').html()){
                select_list.push(cartid);
            }else{
                unselect_list.push(cartid);
            }
        })
        if(select_list.length == 0){
            return;
        }else{
            $.ajax(
                {
                    url: '/axforder/make_order/',
                    type:'GET',
                    datatype:'json',
                    success:function (data) {
                        if(data['status']==200){
                            window.location.href = '/axforder/order_detail/?order_id='+data['order_id']

                        }
                    }
                }
            )
        }
    })
})
