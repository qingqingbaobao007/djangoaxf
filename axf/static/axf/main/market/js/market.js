$(function () {
    $('#all_type').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up')
        $('#all_type_container').toggle();
    })
    $('#sort_rule').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up')
        $('#sort_rule_container').toggle();
    })
    
    // 添加到购物车
    $('.addShopping').click(function () {
        var $button=$(this);
        var goodsid= $button.attr('goodsid');
        $.get('/axfcart/addToCart/',
            {'goodsid':goodsid},
            function (data) {
                if(data['status']==200 ){
                    $button.prev().html(data['c_goods_num']);
                }else{
                    window.location.href='/axfuser/login/'
                }

            }
        )
    })
})