/**
 * Created by admin on 2017/3/28.
 */

$(function () {
    $.post("inspect_img", function (data) {
        var jsonData = $.parseJSON(data);
        var dataStr = "";
        for(i in jsonData){
            dataStr += "<tr><td>" + jsonData[i].url + "</td>" +
                    "<td>" + jsonData[i].img + "</td>" +
                    "<td class='tg-yw4l'><input type='button' value='修改' onsubmit=''>" +
                    "<input type='button' value='删除' onsubmit='' name='delete' id='" + jsonData[i].imageId +
                    "'></td></tr>";
        }
        $("table[name='table']").append(dataStr);
    });
});

$("body").on("click", "input[name='delete']", function () {
    if(confirm("是否删除？")){
        $.post("delete", {"imageId": this.id, "Identification": 3}, function (data) {
            if(data == 1){
                alert("删除成功");
                window.location.reload();
            }
        });
    }else{
        return;
    }

});