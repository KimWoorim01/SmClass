

//jquery start
$(function(){       

  let boxPosition = 0;
  let boxRotate = 0;

  //rightbtn event start
  $(document).on("click","#rightMoveBtn",function(){
    // alert("right button click");
    $("#box").stop();

    if(boxPosition < 900){
      boxPosition += 100;
    }else{
      alert("오른쪽 끝이여");
    }
    boxRotate += 60; 
    
    $("#box").animate({
      left: boxPosition,
      rotate: boxRotate+"deg"
    },1000);
  });
  //rightbtn event end
  
  //leftbtn event start
  $(document).on("click","#leftMoveBtn",function(){
    // alert("left button click");
    $("#box").stop();
    
    if(boxPosition > 0){
      boxPosition -= 100;
    }else{
      alert("왼쪽 끝이여");
    }
    boxRotate -= 60; 
    
    $("#box").animate({
      left: boxPosition,
      rotate: boxRotate+"deg"
    },1000);
  });
  //leftbtn event end


});
//jquery end