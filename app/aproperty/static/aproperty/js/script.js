function serializeForm(form_obj) {
    var form = form_obj.serializeArray();
    var res = {};
    form.forEach((element) => {
        res[element.name] = element.value;
    });
    return res;
}

function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        if (decodeURIComponent(pair[0]) == variable) {
            return decodeURIComponent(pair[1]);
        }
    }
    console.log('Query variable %s not found', variable);
}

$(function () {
    var href = 'text url';
    let submit_form_ids = "#Application-Form, #wf-form-Request-Prez-Form, #wf-form-Footer-Form-2, #wf-form-Footer-Form"
    $(".dw-btn").click( function() {
        href = $(this).parent().find( ".hidden-link" ).prop('href');
        let complex = $(this).parent().find( ".hidden-link" ).text();
        $(document).find(".hidden-inp").val(complex);
    });


    $(submit_form_ids).submit(function (event) {
        event.preventDefault();
        var form = $(this);

        var disabled = $(this).find(':input:disabled').removeAttr('disabled');

        var my_data = serializeForm($(this));
        disabled.attr('disabled', 'disabled');
        console.log(my_data);
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
});