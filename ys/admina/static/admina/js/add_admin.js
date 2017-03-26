/**
 * Created by admin on 2017/3/26.
 */

$(function () {
    if($("input[name='name']").val() == ""){
        alert("请输入姓名");
    }else if($("input[name='username']").val() == ""){
        alert("请输入账号");
    }else if($("input[name='password']").val() == 0){
        alert("请输入密码")
    }
});
