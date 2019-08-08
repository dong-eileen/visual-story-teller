
$( document ).ready(function() {
    $('a.name-tag').attr('target', '_blank');

    $('.name-tag').popover({ 
        html: true,
        trigger: 'hover',
        placement: 'bottom',
        content: function () {
            return '<img src="'+ $(this).attr('href') + '" width=400px/>';
        }
    });
});