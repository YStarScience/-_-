function f1(){

        var tab1=document.getElementById("tab1");
    tab1.style.display=(tab1.style.display=="none"?"":"none");
    }
    function f2(){
    var tab2=document.getElementById("tab2");
    tab2.style.display=(tab2.style.display=="none"?"":"none");
    }
    function f3(){
    var tab3=document.getElementById("tab3");
    tab3.style.display=(tab3.style.display=="none"?"":"none");
    }

function setsubmit() { 
      if(province.value == 0) 
        window.location='salary/beijing.html' 
      if(province.value == 1) 
        window.location='salary/chongqing.html';
      if(province.value == 2) 
        window.location='salary/fujian.html';
      if(province.value == 3) 
        window.location='salary/guangdong.html';
      if(province.value == 4) 
        window.location='salary/hebei.html';
      if(province.value == 5) 
        window.location='salary/hunan.html';
      if(province.value == 6) 
        window.location='salary/jiangsu.html';
      if(province.value == 7) 
        window.location='salary/shandong.html';
      if(province.value == 8) 
        window.location='salary/shanghai.html';
      if(province.value == 9) 
        window.location='salary/zhejiang.html';  
    } 

function checklength(){
  
  var dom= document.getElementById('text').value;
  if(dom.length>20){
    alert("填写数据不能为空，请填写数据");
    return false;
  }
  
}



