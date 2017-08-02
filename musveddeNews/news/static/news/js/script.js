var main = $(".main");
var mySideNav = $("#mySideNav");

function openNav() {
    mySideNav.css("width", "250px");
    main.css("margin-left", "250px");
}

function closeNav() {
    mySideNav.css("width", "0");
    main.css("margin-left", "0");
}
$(".main").on("click", function(){
    if(mySideNav.css("width") == "250px"){
       mySideNav.css("width", "0");
       main.css("margin-left", "0");
    }
});

jQuery('#news-demo').slippry({
  // general elements & wrapper
  slippryWrapper: '<div class="sy-box news-slider" />', // wrapper to wrap everything, including pager
  elements: 'article', // elments cointaining slide content

  // options
  adaptiveHeight: false, // height of the sliders adapts to current
  captions: false,

  // pager
  pagerClass: 'news-pager',

  // transitions
  transition: 'horizontal', // fade, horizontal, kenburns, false
  speed: 1200,
  pause: 8000,

  // slideshow
  autoDirection: 'prev'
});
