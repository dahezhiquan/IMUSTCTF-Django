// 登录页面点击事件发生
$(function () {
    $('.forgotBtn').click(function () {
        $('#forgot').toggleClass('toggle')
    })

    $('.registerBtn').click(function () {
        $('#register, #formContainer').toggleClass('toggle')
    })
})