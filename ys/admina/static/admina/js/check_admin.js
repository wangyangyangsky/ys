/**
 * Created by admin on 2017/3/28.
 */

$(function () {
    $.post("/admin/inspect_admin/", function (data) {
        var jsonData = $.parseJSON(data);
        var dataStr = "";
        for(i in jsonData){
            dataStr += "<tr><td value='" + jsonData[i].username + "'>" + jsonData[i].name + "</td>" +
                    "<td>" + jsonData[i].department + "</td>" +
                    "<td>" + jsonData[i].username + "</td>" +
                    "<td>" + jsonData[i].password + "</td>"
            if(jsonData[i].is_use == true){
                dataStr += "<td>是</td>"
            }
            dataStr += "<td class='tg-yw4l'><input type='button' value='修改' onsubmit=''><input type='button' value='删除' onsubmit=''></td>"
        }
        $("table[name='table']").append(dataStr);
    });
});