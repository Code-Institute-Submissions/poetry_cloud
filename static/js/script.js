$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('select').formSelect();
    $(".dropdown-content.select-dropdown > li span").css("color", "black");
  });