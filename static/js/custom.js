$('.icp').iconpicker({
    placement: 'right'
});

$('.icp').on('iconpickerSelected', function(event){
    $(this).val('fa ' + event.iconpickerValue)
});