import 'bootstrap/dist/js/bootstrap';
import $ from 'jquery';

$('a[href="#top"]').click(() => {
  $('html, body').animate({ scrollTop: 0 });
  return false;
});

$(window).scroll(event => {
  if ($(window).scrollTop() > 100 && $('.jc-scroll').css('opacity') === '1') {
    $('.jc-scroll').fadeIn();
  } else if ($('.jc-scroll').css('opacity') === '1') {
    $('.jc-scroll').fadeOut();
  }
});
