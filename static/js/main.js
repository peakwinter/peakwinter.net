$("a[href='#top']").click(function() {
  $("html, body").animate({ scrollTop: 0 });
  return false;
});

$(window).scroll(function (event) {
  if ($(window).scrollTop() > 100 && $(".jc-scroll").css("opacity") === '1') {
    $(".jc-scroll").fadeIn();
  } else if ($(".jc-scroll").css("opacity") === '1') {
    $(".jc-scroll").fadeOut();
  }
});
