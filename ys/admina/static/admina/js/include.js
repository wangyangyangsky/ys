/**
 * Created by admin on 2017/3/28.
 */

$(function () {
    $.post("colum_info", function (data) {
        var jsonData = $.parseJSON(data);
        var dataStr = "";
        for(i in jsonData){
            if(jsonData[i].name == "首页"){
                continue;
            }
            dataStr += "<a href='add_news_column?columnId=" + jsonData[i].columnId + "'>" +
                    jsonData[i].name + "</a>";
        }
        $("span[name='news']").append(dataStr);
    });
});