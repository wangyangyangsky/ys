/**
 * Created by admin on 2017/3/26.
 */

$(function () {
    document.getElementsByName("name")[0].focus();
});

$("input[name='reset']").click(function () {
    $("input[name='name']").val("");
    $("input[name='username']").val("");
    $("input[name='password']").val("");
    $("input[name='password1']").val("");
    $("input[name='department']").val("");
});

$("input[name='submit']").click(function () {
    if($("input[name='name']").val() == ""){
        alert("请输入姓名");
    }else if($("input[name='username']").val() == ""){
        alert("请输入账号");
    }else if($("input[name='password']").val() == ""){
        alert("请输入密码");
    }else if($("input[name='password1']").val() == ""){
        alert("请第二次输入密码");
    }else if($("input[name='password']").val() != $("input[name='password1']").val()){
        alert("两次密码输入不一致");
    }else if($("input[name='department']").val() == ""){
        alert("请输入所属部门");
    }else{
        $("input[name='submit']").click(
            $.post("create_admin",{
                "name": $("input[name='name']").val(),
                "username": $("input[name='username']").val(),
                "password": $("input[name='password']").val(),
                "department": $("input[name='department']").val(),
            }, function (data) {
                if(data == 0){
                    alert("用户名已存在");
                    $("input[name='name']").val("");
                    $("input[name='username']").val("");
                    $("input[name='password']").val("");
                    $("input[name='password1']").val("");
                    $("input[name='department']").val("");
                    document.getElementsByName("name")[0].focus();
                }else if(data == 1){
                    alert("创建成功");
                    window.location.href = "check_admin";
                }else{
                    alert(data);
                }
            })
        );
    }
});
