/**
 * Created by admin on 2017/3/28.
 */

$(function () {
    $("input[name='name']").val("");
    // $("select[name='level']").val("");
    $("input[name='sort']").val("");
    $("input[name='is_use']").val(0);
    $("input[name='parentColum']").val("");
    $("input[name='image']").val("");
});

$("input[name='submit']").click(function () {
    var name = $("input[name='name']").val();
    var level = $("select[name='level']").val();
    var sort = $("input[name='sort']").val();
    var is_use = $("input[name='is_use']").val();
    var image = $("input[name='image']").val();
    if(name == "" || level == "" || sort == "" || is_use == "" || image == ""){
        alert("表单请填写完整");
        $("input[name='name']").val("");
        $("select[name='level']").val("");
        $("input[name='sort']").val("");
        $("input[name='is_use']").val("");
        $("input[name='image']").val("");
    }else{
        $("#pictureForm").attr("action", "create_column");
        $.ajaxSetup({

        });
        $("#pictureForm").ajaxSubmit({
            resetForm: false,
            dataType: 'json',
            success:function (data) {
                if(data == 0){
                    alert("失败");
                    $("input[name='name']").val("");
                    $("select[name='level']").val("");
                    $("input[name='sort']").val("");
                    $("input[name='is_use']").val("");
                    $("input[name='image']").val("");
                }else if(data == 1){
                    alert("成功");
                    window.location.href = "col_page2"
                }
            }
        });
    }
});

$(function () {
    $.post("inspect_column", function (data) {
        var jsonData = $.parseJSON(data);
        var dataStr = "";
        for(i in jsonData){
            dataStr += "<tr><td>" + jsonData[i].level + "</td>" +
                    "<td>" + jsonData[i].name + "</td>"
            if(jsonData[i].parentColum == ""){
                dataStr += "<td>无</td>"
            }else{
                dataStr += "<td>" + jsonData[i].parentColum + "</td>"
            }
            dataStr += "<td>" + jsonData[i].sort + "</td>"
            if(jsonData[i].is_use == true){
                dataStr += "<td>是</td>"
            }else{
                dataStr += "<td>否</td>"
            }
            dataStr += "<td class='tg-yw4l'><input type='button' value='修改' onsubmit=''>" +
                "<input type='button' value='删除' onsubmit='' name='delete' id='" +
                 jsonData[i].columnId +"'></td></tr>"
        }
        $("table[name='table']").append(dataStr);
    });
});

$("body").on("click", "input[name='delete']", function () {
    if(confirm("是否删除？")){
        $.post("delete", {"columnId": this.id, "Identification": 1}, function (data) {
            if(data == 1){
                alert("删除成功");
                window.location.reload();
            }
        });
    }else{
        return
    }

});

