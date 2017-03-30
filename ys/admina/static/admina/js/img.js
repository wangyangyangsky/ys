/**
 * Created by admin on 2017/3/28.
 */

$(function () {
    $.post("colum_info", function (data) {
        var jsonData = $.parseJSON(data);
        var dataStr = "<option value='0'>请选择</option>";
        for(i in jsonData){
            dataStr += "<option value='" + jsonData[i].columnId + "'>" +
                    jsonData[i].name + "</option>"
        }
        $("select[name='select']").empty().append(dataStr);
    })
});

$("body").on("click", "input[name='submit']", function () {
    $("#pictureForm").attr("action", "save_picture");
    $.ajaxSetup({
        
    });
    $("#pictureForm").ajaxSubmit({
        resetForm: false,
        dataType: 'json',
        success:function (data) {
            if(data == 0){
                alert("失败");
            }else if(data == 1){
                alert("成功");
                window.location.href = "img_form";
            }
        }
    });
});