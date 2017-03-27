/**
 * Created by admin on 2017/3/26.
 */

$(function () {
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
        // 在这里调用函数
    }
});
