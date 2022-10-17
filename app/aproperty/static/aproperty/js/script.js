function serializeForm(form_obj) {
    var form = form_obj.serializeArray();
    var res = {};
    form.forEach((element) => {
        res[element.name] = element.value;
    });
    return res;
};


$(function () {
    let hostname = document.location.hostname;
    let pathname = document.location.pathname;
    let complex =  (pathname == "/") ? hostname: pathname.replaceAll("/", " ");
    $('.hidden-inp').each(function(){
            $(this).val(complex);
    })
    let submit_form_ids = "#Application-Form, #wf-form-Request-Prez-Form, #wf-form-Footer-Form-2, #wf-form-Footer-Form"
    $(submit_form_ids).submit(function (event) {
        event.preventDefault();
        var form = $(this);

        var disabled = $(this).find(':input:disabled').removeAttr('disabled');

        var my_data = serializeForm($(this));
        disabled.attr('disabled', 'disabled');
        var my_url = $(this).attr('action');
        $.ajax({
            url: my_url,
            type: "POST",
            data: my_data,
            success: function (data, textStatus, jqXHR) {
                form.hide();
                form.parent().find('.w-form-done').show();
                form.parent().find('.w-form-fail').hide();
            },
            error: function (jqXHR, textStatus, errorThrown) {
                form.parent().find('.w-form-fail').show();
            }
        });
        return false;
    });
    $('#complex-collection').on('click', '.dw-btn', function() {
        let complex = $(this).parent().find( ".hidden-link" ).text().replaceAll("/", " ");
        $('.modal').find('.hidden-inp').val(complex);
        $(".modal").css("display", "block");
        $(".modal").css("opacity", "100%");
        
    });
    $('#complex-collection').on('click', '.close-icon-2', function() {
        $(".modal").css("display", "none");
    });
    $('.dw-btn').click(function (event) {
        let hostname = document.location.hostname;
        let pathname = document.location.pathname;
        let complex =  (pathname == "/") ? hostname: pathname.replaceAll("/", " ");
        $(document).find(".hidden-inp").val(complex);
        $(".modal").css("display", "block");
        $(".modal").css("opacity", "100%");
    });
    $('.close-icon-2').click(function (event) {
        $(".modal").css("display", "none");
    });
});