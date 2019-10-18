$(function () {
    $('#exampleInputName').blur(function () {
        //获取文本框中的内容
        //html 获取的标签里面的内容
        //text 获取的是里面的文本内容
        // trim是去除空格
        var name = $(this).val().trim();

        // 校验文本框中的内容是否满足某条件
        // 使用正则表达式

        var reg = /^(?![^a-zA-Z]+$)(?!\\D+$).{3,8}$/

        // test方法会判断某字符串是否符合某正则 如果符合返回的是true 如果不符合返回的是false
        b = reg.test(name)
        if(b){
            $.getJSON(
                '/axfuser/checkName/',
                {'name':name},
                function (data) {
                    if(data['status']==200){
                        $('#nameinfo').html(data['msg']).css({'fontSize':10,'color':'green'});
                    }else{
                        $('#nameinfo').html(data['msg']).css({'fontSize':10,'color':'red'});
                    }
                }
            )



            // $('#nameinfo').html('用户名字可以使用√').css({'fontSize':10,'color':'green'})
        }else {
            $('#nameinfo').html('用户名格式不正确×').css({'fontSize':10,'color':'red'})
            $(this).val('')
        }
    })
    $('#exampleInputPassword').blur(function () {
        var password = $(this).val().trim();
        var reg1 = /^(?![^a-zA-Z]+$)(?!\\D+$).{3,8}$/
        b1 = reg1.test(password)
        if (b1){
            $('#passwordinfo').html('密码格式正确,请再次输入密码√').css({'fontSize':10,'color':'green'});
        }else {
            $('#passwordinfo').html('密码格式不正确,请重新输入×').css({'fontSize':10,'color':'red'});
             $(this).val('')
        }
    })
    $('#exampleInputPassword1').blur(function () {
        var password1 = $('#exampleInputPassword').val().trim();
        var password2 = $(this).val().trim()

        if(password1===password2){
            $('#passwordinfo1').html('输入正确√').css({'fontSize':10,'color':'green'});
        }else{
            $('#passwordinfo1').html('密码不一致，请重新输入×').css({'fontSize':10,'color':'red'});
            $(this).val('')
        }
    })

})

function parse1() {

    var password = document.getElementById('exampleInputPassword').value;

   password = md5(password)

    document.getElementById('exampleInputPassword').value = password;
    return true
}