$(function () {
  $('#login').click(function () {
      // window.open('/axfuser/login/',target='_self');
      window.location.href='/axfuser/login/';
  })
    $('#regis').click(function () {
        window.location.href='/axfuser/register/';
    })
})