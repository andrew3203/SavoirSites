function serializeForm(form_obj) {
    var form = form_obj.serializeArray();
    var res = {};
    form.forEach((element) => {
        res[element.name] = element.value;
    });
    return res;
};


$(function () {
    let submit_form_ids = "#Application-Form, #wf-form-Request-Prez-Form, #wf-form-Footer-Form-2, #wf-form-Footer-Form"

    $(submit_form_ids).submit(function (event) {
        event.preventDefault();
        var form = $(this);

        var disabled = $(this).find(':input:disabled').removeAttr('disabled');

        var my_data = serializeForm($(this));
        disabled.attr('disabled', 'disabled');
        var my_url = $(this).attr('action');
        $.ajax({
            url: `https://${document.domain}/${my_url}`,
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