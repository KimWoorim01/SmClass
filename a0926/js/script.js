
$(function () {

  var count = 1;
  var id_data;
  $(document).on("click", ".delBtn", function () {
    let id = $(this).closest().attr("id");
    alert(id + "번 학생");
    $(this).parent().parent().remove();
  });


  $(document).on("click", ".score", function () {
    let number = Number(prompt("점수를 입력하세요."));
    $(this).html(number);
    let kor = $(this).parent().children("#kor").html();
    let eng = $(this).parent().children("#eng").html();
    let math = $(this).parent().children("#math").html();

    let sum = Number(kor) + Number(eng) + Number(math);
    let avg = Number(sum / 3);
    $(this).parent().children(".sum").html(sum);
    $(this).parent().children(".avg").html(avg.toFixed(2));
  });

  $(document).on("click", "#dataBtn", function () {

  });

  $.ajax({
    url: "js/stuData.json",
    type: "get",                                   //get,post
    data: "",                                      //데이터 서버로 전송
    dataType: "json",                              //response data type : json, html, xml, text...
    success: function (data) {                       //서버송신 성공시
      console.log(data);

      let inputData = "";
      for (let i = 0; i < data.length; i++) {
        count++;
        inputData += "<tr id = 'tr_" + i + "'>";
        inputData += "<td>" + data[i].no + "</td>";
        inputData += "<td id = 'stName'>" + data[i].name + "</td>";
        inputData += "<td class = 'score' id = 'kor'>" + data[i].kor + "</td>";
        inputData += "<td class = 'score' id = 'eng'>" + data[i].eng + "</td>";
        inputData += "<td class = 'score' id = 'math'>" + data[i].math + "</td>";
        inputData += "<td class = 'sum'>" + (data[i].math + data[i].kor + data[i].eng) + "</td>";
        inputData += "<td class = 'avg'>" + ((data[i].math + data[i].kor + data[i].eng) / 3).toFixed(2) + "</td>";
        inputData += "<td><button class = 'updateBtn'>수정</button><button class = 'delBtn'>삭제</button></td>";
        inputData += "</tr>";
      }

      $("#tbody").append(inputData);

    },
    error: function (error) {                             //서버송신 실패시
      console.log("data receive fail : " + error);
      alert("실패");
    }

  });


  $(document).on("click", "#update", function () {

    let userName = $("#userName").val();
    let kor = Number($("#korScore").val());
    let eng = Number($("#engScore").val());
    let math = Number($("#mathScore").val());

    

    if (userName == null || kor == null || eng == null || math == null) {
      alert("데이터 입력 요망");
      return;
    }

    let sum = (kor + eng + math);
    let avg = (kor + eng + math) / 3;


    data = $("#" + id_data).children();

    let inputData = "";

    inputData += "<td>" + data[0].textContent + "</td>";
    inputData += "<td id = 'stName'>" + userName + "</td>";
    inputData += "<td class = 'score' id = 'kor'>" + kor + "</td>";
    inputData += "<td class = 'score' id = 'eng'>" + eng + "</td>";
    inputData += "<td class = 'score' id = 'math'>" + math + "</td>";
    inputData += "<td class = 'sum'>" + sum + "</td>";
    inputData += "<td class = 'avg'>" + avg.toFixed(2) + "</td>";
    inputData += "<td><button class = 'updateBtn'>수정</button><button class = 'delBtn'>삭제</button></td>";
    count++;
    $("#" + id_data).html(inputData);

    $("#userName").val("");
    $("#korScore").val("");
    $("#engScore").val("");
    $("#mathScore").val("");


    alert("수정완료");

  });

  $(document).on("click", ".updateBtn", function () {
    $("#createBtn").hide();
    $("#update").show();
    $("#updateCancelBtn").show();

    let stname = $(this).parent().parent().children("#stName").html();
    let stkor = $(this).parent().parent().children("#kor").html();
    let steng = $(this).parent().parent().children("#eng").html();
    let stmath = $(this).parent().parent().children("#math").html();


    $("#userName").val(stname);
    $("#korScore").val(stkor);
    $("#engScore").val(steng);
    $("#mathScore").val(stmath);

    id_data = $(this).parent().parent().attr("id");
  });

  $(document).on("click", "#updateCancelBtn", function () {
    $("#createBtn").show();
    $("#update").hide();
    $("#updateCancelBtn").hide();
  })

  $(document).on("click", "#searchBtn", function () {
    let name = $("#userName").val();
    let kor = $("#korScore").val();
    let eng = $("#engScore").val();
    let math = $("#mathScore").val();

    let table = $("#tbody");

    // var data = $(this).closest('tr').children();
    // console.log(data[1].textContent) // 이름
    // console.log(data[2].textContent) // 국어
    // console.log(data[3].textContent) // 영어
    // console.log(data[4].textContent) // 수학


    tableList = table.children();
    trdata = tableList;
    console.log(trdata);


  });


  $(document).on("click", "#createBtn", function () {
    let userName = $("#userName").val();
    let kor = Number($("#korScore").val());
    let eng = Number($("#engScore").val());
    let math = Number($("#mathScore").val());

    if (userName == null || kor == null || eng == null || math == null) {
      alert("데이터 입력 요망");
      return;
    }

    console.log(kor);
    let sum = (kor + eng + math);
    let avg = (kor + eng + math) / 3;

    let inputData = "";

    inputData += "<tr id = 'tr_" + count + "'>";
    inputData += "<td>" + count + "</td>";
    inputData += "<td id = 'stName'>" + userName + "</td>";
    inputData += "<td class = 'score' id = 'kor'>" + kor + "</td>";
    inputData += "<td class = 'score' id = 'eng'>" + eng + "</td>";
    inputData += "<td class = 'score' id = 'math'>" + math + "</td>";
    inputData += "<td class = 'sum'>" + sum + "</td>";
    inputData += "<td class = 'avg'>" + avg.toFixed(2) + "</td>";
    inputData += "<td><button class = 'updateBtn'>수정</button><button class = 'delBtn'>삭제</button></td>";
    inputData += "</tr>";
    count++;
    $("#tbody").append(inputData);

    $("#userName").val("");
    $("#korScore").val("");
    $("#engScore").val("");
    $("#mathScore").val("");

  });

});
