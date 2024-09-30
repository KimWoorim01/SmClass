
//jquery start
$(function(){
  
  //search_txt_btn event start
  $(document).on("click","#serach_txt_btn",function(){
    // alert("search_click");
    
    let urlString = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=wBCDYHwh4VaKpHJHaDpRSIEzvIwQ2I%2ByakSIRZYmrHjsKIjcgcXco%2B6yZG12SI8NhnfyXmXsDniYNozNiadU%2BQ%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    urlString += searchWord;


    $.ajax({
      url: urlString,
      type: "get",                                   //get,post
      data: "",                                      //데이터 서버로 전송
      dataType: "json",                              //response data type : json, html, xml, text...
      success: function(data) {                       //서버송신 성공시
        console.log(data);
  
        let itemList = data.response.body.items.item;
        let strData = "";

        for (let i = 0; i < itemList.length; i++) {  
          strData += "<tr id = 'tr_"+i+"'>";
          strData += "<td>" + itemList[i].galContentId + "</td>";
          strData += "<td>" + itemList[i].galTitle + "</td>";
          strData += "<td>"+itemList[i].galPhotographer+"</td>";
          strData += "<td>"+itemList[i].galModifiedtime+"</td>";
          strData += "<td> <img src = '"+itemList[i].galWebImageUrl+"'></td>";
          strData += "</tr>";
        }
        
        $("#tbody").html(strData);

      },
      error: function (error) {                             //서버송신 실패시
        console.log("data receive fail : " + error);
        alert("실패");
      }
      
    });
    
  });
  //search_txt_btn event end

})
//jquery end