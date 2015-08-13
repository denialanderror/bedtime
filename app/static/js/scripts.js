// opens create modal on page load
$(document).ready(function(){
    $('#create').foundation('reveal', 'open')
});

// sends star rating to Flask without reloading page
$('#ratings').find('input').on('change', function() {
    var rating = $('input[name=rating]:checked', '#ratings').val();
    var url = $(location).attr('pathname');
    $.post(("/ending/" + url.substr(url.lastIndexOf('/') + 1)), { rating: rating } );


    //$.ajax({
    //    type: 'POST',
    //    url: '/ending',
    //    data: rating,
    //    processData: false,
    //    contentType: false,
    //    success: function(response) {
    //            console.log(rating);
    //    },
    //    error: function(error) {
    //        console.log(error);
    //    }
    //})
});
