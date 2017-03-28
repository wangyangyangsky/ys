/**
 * Created by admin on 2017/3/28.
 */

$(function () {
    $.post("inspect_admin", function (data) {
        var jsonData = $.parseJSON(data);
        var dataStr = "";
        for(i in jsonData){
            dataStr += "<tr><td>" + jsonData[i].name + "</td>" +
                    "<td>" + jsonData[i].department + "</td>" +
                    "<td>" + jsonData[i].username + "</td>" +
                    "<td>" + jsonData[i].password + "</td>"
            if(jsonData[i].is_use == true){
                dataStr += "<td>是</td>"
            }else{
                dataStr += "<td>否</td>"
            }
            dataStr += "<td class='tg-yw4l'><input type='button' value='修改' onsubmit=''>" +
                "<input type='button' value='删除' onsubmit='' name='delete' id='" + jsonData[i].username +
                "'></td></tr>";
        }
        $("table[name='table']").append(dataStr);
    });
});

$("body").on("click", "input[name='delete']", function () {
    if(confirm("是否删除？")){
        $.post("delete", {"username": this.id, "Identification": 2}, function (data) {
            alert("删除成功");
            $.post("inspect_admin", function (data) {
                var jsonData = $.parseJSON(data);
                var dataStr = "";
                for(i in jsonData){
                    dataStr += "<tr><td>" + jsonData[i].name + "</td>" +
                            "<td>" + jsonData[i].department + "</td>" +
                            "<td>" + jsonData[i].username + "</td>" +
                            "<td>" + jsonData[i].password + "</td>"
                    if(jsonData[i].is_use == true){
                        dataStr += "<td>是</td>"
                    }else{
                        dataStr += "<td>否</td>"
                    }
                    dataStr += "<td class='tg-yw4l'><input type='button' value='修改' onsubmit=''>" +
                        "<input type='button' value='删除' onsubmit='' name='delete' id='" + jsonData[i].username +
                        "'></td></tr>";
                }
                window.location.reload();
            });
        });
    }else{
        return
    }

});