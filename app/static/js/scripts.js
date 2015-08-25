// opens create modal on page load
//$(document).ready(function(){
//    $('#create').foundation('reveal', 'open')
//});

// sends star rating to Flask without reloading page
$('#ratings').find('input').on('change', function() {
    var rating = $('input[name=rating]:checked', '#ratings').val();
    var url = $(location).attr('pathname');
    $.post(("/ending/" + url.substr(url.lastIndexOf('/') + 1)), { rating: rating } );
    $('#thanks').foundation('reveal', 'open');
});

// closes thanks modal on click of No button
$('a.custom-close-reveal-modal').click(function(){
    $('#thanks').foundation('reveal', 'close');
});

$('#create-form').on('valid.fndtn.abide', function () {
    $('#create').foundation('reveal', 'close');
    $('#loading-modal').foundation('reveal', 'open');
    $("#loading").show();
    $("#content").hide();
  });

//$('#create-form').submit(function () {
//    $('#create').foundation('reveal', 'close');
//    $("#loading").show();
//    $("#content").hide();
//  });