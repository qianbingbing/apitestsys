/*****
* CONFIGURATION
*/
    //Main navigation
    $.navigation = $('nav > ul.nav');

  $.panelIconOpened = 'icon-arrow-up';
  $.panelIconClosed = 'icon-arrow-down';

  //Default colours
  $.brandPrimary =  '#20a8d8';
  $.brandSuccess =  '#4dbd74';
  $.brandInfo =     '#63c2de';
  $.brandWarning =  '#f8cb00';
  $.brandDanger =   '#f86c6b';

  $.grayDark =      '#2a2c36';
  $.gray =          '#55595c';
  $.grayLight =     '#818a91';
  $.grayLighter =   '#d1d4d7';
  $.grayLightest =  '#f8f9fa';

'use strict';

/****
* MAIN NAVIGATION
*/

$(document).ready(function($){

  // Add class .active to current link
  $.navigation.find('a').each(function(){

    var cUrl = String(window.location).split('?')[0];


    if (cUrl.substr(cUrl.length - 1) == '#') {
      cUrl = cUrl.slice(0,-1);
    }

    if ($($(this))[0].href==cUrl) {
      $(this).addClass('active');

      $(this).parents('ul').add(this).each(function(){
        $(this).parent().addClass('open');
      });
    }
  });

  // Dropdown Menu
  $.navigation.on('click', 'a', function(e){

    if ($.ajaxLoad) {
      e.preventDefault();
    }

    if ($(this).hasClass('nav-dropdown-toggle')) {
      $(this).parent().toggleClass('open');
      resizeBroadcast();
    }

  });

  function resizeBroadcast() {

    var timesRun = 0;
    var interval = setInterval(function(){
      timesRun += 1;
      if(timesRun === 5){
        clearInterval(interval);
      }
      window.dispatchEvent(new Event('resize'));
    }, 62.5);
  }

  /* ---------- Main Menu Open/Close, Min/Full ---------- */
  $('.navbar-toggler').click(function(){

    if ($(this).hasClass('sidebar-toggler')) {
      $('body').toggleClass('sidebar-hidden');
      resizeBroadcast();
    }

    if ($(this).hasClass('aside-menu-toggler')) {
      $('body').toggleClass('aside-menu-hidden');
      resizeBroadcast();
    }

    if ($(this).hasClass('mobile-sidebar-toggler')) {
      $('body').toggleClass('sidebar-mobile-show');
      resizeBroadcast();
    }

  });

  $('.sidebar-close').click(function(){
    $('body').toggleClass('sidebar-opened').parent().toggleClass('sidebar-opened');
  });

  /* ---------- Disable moving to top ---------- */
  $('a[href="#"][data-top!=true]').click(function(e){
    e.preventDefault();
  });
  /* ---------- Reload the table data ------------*/

});

/****
* CARDS ACTIONS
*/

$(document).on('click', '.card-actions a', function(e){
  e.preventDefault();

  if ($(this).hasClass('btn-close')) {
    $(this).parent().parent().parent().fadeOut();
  } else if ($(this).hasClass('btn-minimize')) {
    var $target = $(this).parent().parent().next('.card-block');
    if (!$(this).hasClass('collapsed')) {
      $('i',$(this)).removeClass($.panelIconOpened).addClass($.panelIconClosed);
    } else {
      $('i',$(this)).removeClass($.panelIconClosed).addClass($.panelIconOpened);
    }

  } else if ($(this).hasClass('btn-setting')) {
    $('#myModal').modal('show');
  }

});
var num = 0;
function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}
function init(url) {
  /* ---------- Tooltip ---------- */
  $('[rel="tooltip"],[data-rel="tooltip"]').tooltip({"placement":"bottom",delay: { show: 400, hide: 200 }});

  /* ---------- Popover ---------- */
  $('[rel="popover"],[data-rel="popover"],[data-toggle="popover"]').popover();

}
$(".card-header").each(function () {
          $(this).click(function () {
              var next = $(this).next();
              next.toggle();
        })
    })
$("#db_dialog").click(function () {
          $("#myModal").show();
    })
function save_project_base() {
    $.ajax({
            //几个参数需要注意一下
                type: "POST",//方法类型
                dataType: "json",//预期服务器返回的数据类型
                url: "/save_project_base/" ,//url
                data: $("#form1").serialize(),
                success: function (result) {
                    if ( result.status == "ok" ) {
                        targeTo(1)
                        getEnvs()
                    }
                    else{
                        alert(result.result);
                    }
                },
                error : function() {
                    alert("服务器异常");
                }
            });
}

/*---------产生uuid -------------*/
function guid() {
    function S4() {
        return (((1+Math.random())*0x10000)|0).toString(16).substring(1);
    }
    var uuid = (S4()+S4()+S4()+S4()+S4()+S4()+S4()+S4());
    window.location="/addProject/?id="+ uuid;
}
/*-------------跳转对应的页面 -------------*/
function targeTo(number){
  $("#tablist").find(".nav-link").eq(number).tab("show")
}
/*-------------获取url参数-----------------*/
function getUrlParam(name) {
     var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
     var r = window.location.search.substr(1).match(reg);
     console.log(r)
     if(r!=null)return  unescape(r[2]);
     return null;
}



/*==============================================================*/
/*------ ajax保存项目基本详情 ---------------*/
function save_project_base() {
    $.ajax({
            //几个参数需要注意一下
                type: "POST",//方法类型
                dataType: "json",//预期服务器返回的数据类型
                url: "/save_project_base/" ,//url
                data: $("#form1").serialize(),
                success: function (result) {
                    if ( result.status == "ok" ) {
                        targeTo(1)
                        getEnvs()
                    }
                    else{
                        alert(result.result);
                    }
                },
                error : function() {
                    alert("服务器异常");
                }
            });
}
/*------ ajax获取项目基本详情 ---------------*/
function get_project_base(){
    var project_id = getUrlParam("id")
    $.ajax({
            //几个参数需要注意一下
                type: "POST",//方法类型
                dataType: "json",//预期服务器返回的数据类型
                url: "/get_project/", //url
                data:{"project_id":project_id},
                success: function (result) {
                    if ( result.status == "ok" ) {
                        var data = result.result
                        $("#project-name").val(data[0].project_name)
                        $("#project-desc").val(data[0].project_desc)
                        $("#interface-type").val(data[0].interface_type)
                    }
                    else{
                      alert(result.result);
                    }
                },
                error : function() {
                    alert("服务器异常");
                }
            });
}
/*------------ ajax获取项目环境列表-----------*/
function getEnvs() {
    var project_id = getUrlParam("id")
    $.ajax({
                type: "POST",//方法类型
                dataType: "json",//预期服务器返回的数据类型
                url: "/get_envs/",//url
                data:{"project_id":project_id},
                success: function (result) {
                    if ( result.status === "ok" ) {
                        var row = "";
                        var data = result.result;
                        console.log("#=---------开始渲染-------")
                        for( i in data){
                            console.log(data[i]);
                            var database = "";
                            if (data[i].database_ip == ""){
                                database = "请先设置数据库"
                            }
                            else{
                                database = data[i].database_ip
                            }
                            row += "<tr>" +
                            "<td>" + data[i].name + "</td>" +
                            "<td>" + data[i].ip + "</td>" +
                            "<td>" + data[i].port + "</td>" +
                            "<td>" + database + "</td>" +
                            "<td>\n" +
                                " <div class=\"cell\">\n" +
                                "<button type=\"button\" class=\"btn btn-primary\" data-toggle=\"modal\" data-target=\"#primaryModal\"\n" +
                                "onclick=getDB("+data[i].id+")>\n" +
                                " 关联数据库\n" +
                                "</button>\n" +
                                "<button type=\"button\" class=\"btn btn-outline-warning\" onclick=deleteEnv("+ data[i].id + ")>\n" +
                                "<span><i class=\"el-icon-delete\" ></i> 删除</span>\n" +
                                "</button>\n" +
                                "</div>\n" +
                                "<div id=\"show\"></div>\n" +
                                "</td>\n" +
                            "</tr>"
                        }
                        console.log(row)
                        $("#tb-env-list").html(row);
                        console.log("#=-------渲染结束---------")
                    }
                    else{
                      alert(result.result);
                    }
                },
                error : function() {
                    alert("服务器异常");
                }
            });
}
/*------------ajax保存项目环境 ---------------*/
function saveEnv() {
    var len = $("#env_table").find("tbody").find("tr").length;
    if(len<5){
        $.ajax({
            //几个参数需要注意一下
                type: "POST",//方法类型
                dataType: "json",//预期服务器返回的数据类型
                url: "/save_env/" ,//url
                data: $("#env_from").serialize(),
                success: function (result) {
                    if ( result.status == "ok" ) {
                        $('#primaryModal2').modal("hide")
                        getEnvs()
                    }
                    else{
                        alert(result.result);
                    }
                },
                error : function() {
                    alert("服务器异常");
                }
            });
    }
    else{
        alert("最多只能添加五个测试环境")
        $('#primaryModal2').modal("hide")

    }

}
/*------------ajax删除项目环境 -----------------*/
function deleteEnv(env_id) {
    console.log(env_id)
     var flag = window.confirm("您确定要删除?");
     if(!flag){
         return false;
         }
     else{
         $(this).parent().parent().parent().remove();
         num = num - 1
          $.ajax({
            //几个参数需要注意一下
                type: "POST",//方法类型
                dataType: "json",//预期服务器返回的数据类型
                url: "/delete_env/" ,//url
                data: {"env_id":env_id},
                success: function (result) {
                    if ( result.status == "ok" ) {

                    }
                    else{
                        alert(result.result);
                    }
                },
                error : function() {
                    alert("服务器异常");
                }
            });

         }
      }
/*------------ajax保存邮箱设置 -----------------*/
function saveEmailsetting(){
     $.ajax({
            //几个参数需要注意一下
                type: "POST",//方法类型
                dataType: "json",//预期服务器返回的数据类型
                url: "/save_email/" ,//url
                data: $("#email-form").serialize(),
                success: function (result) {
                    if ( result.status == "ok" ) {
                        alert(result.result)
                    }
                    else{
                        alert(result.result);
                    }
                },
                error : function() {
                    alert("服务器异常");
                }
            });

}
/*------------ajax获取邮箱设置 -----------------*/
function getEmailsetting(){
    var project_id = getUrlParam("id")
     $.ajax({
            //几个参数需要注意一下
                type: "POST",//方法类型
                dataType: "json",//预期服务器返回的数据类型
                url: "/get_email/" ,//url
                data: {"project_id":project_id},
                success: function (result) {
                    if ( result.status == "ok" ) {
                        var data = result.result
                        $("#email-switch").val(data[0].switch)
                        $("#email-username").val(data[0].username)
                        $("#email-password").val(data[0].password)
                        $("#email-receiver").val(data[0].receiver)
                        $("#email-cc").val(data[0].cc)
                        $("#email-subject").val(data[0].subject)
                        $("#email-content").val(data[0].content)
                    }
                    else{
                        alert(result.result);
                    }
                },
                error : function() {
                    alert("服务器异常");
                }
            });

}
/*------------ajax获取数据库信息 -----------------*/
function getDB(env_id) {
    console.log(env_id)
    $.ajax({
                type: "get",//方法类型
                dataType: "json",//预期服务器返回的数据类型
                url: "/get_db/?env_id="%env_id ,//url
                success: function (result) {
                    if ( result.status == "ok" ) {
                        console.log(result.result)
                    }
                    else{
                      alert(result.result);
                    }
                },
                error : function() {
                    alert("服务器异常");
                }
            });
}