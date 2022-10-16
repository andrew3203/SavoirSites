function getQueryParam(url, variable) {
    var vars = url.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        if (decodeURIComponent(pair[0]) == variable) {
            return decodeURIComponent(pair[1]);
        }
    }
    console.log('Query variable %s not found', variable);
};

function insertComplexes(data) {
    for (var i = 0; i < data.length; i++) {
        complex = data[i]
        element = `
            <div class="collection-item-5">
            <div data-w-id="32da13cd-eac5-e877-d785-b77c3b085bb5" class="wrapper-2">
            <img src="${ complex.title_image }" width="500" style="" loading="lazy" alt="" class="image-43 ani-im">
            <div class="cover cover-3">
                <div class="w-layout-grid grid-26">
                <div id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bb9-16e3a100" class="div-block-3 gb">
                    <a id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bba-16e3a100" href="#" class="link-block-4 w-inline-block">
                    <div class="text-block-68">${ complex.area.name }</div>
                    <h2 class="heading-7 text-link">${ complex.name }</h2>
                    </a>
                    <div id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bc1-16e3a100" class="div-block-9">
                    <div class="text-block-67 ttx-left">${ complex.squares } м<sup>2</sup></div>
                    </div>
                    <div id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bc7-16e3a100" class="div-block-1108">
                    <div class="text-block-21 txtx-left">${ complex.price_from } ₽/м²</div>
                    </div>
                </div>
                <a id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bce-16e3a100" href="#" class="button-5 download dw-btn w-button">Запросить презентацию</a>
                <a href="#" id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bd0-16e3a100" class="hidden-link">${ complex.url }</a>
                <img src="${ complex.get_logo }" id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bd2-16e3a100" loading="lazy" alt="" class="image-39">
                <a id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bd3-16e3a100" href="${ complex.url }" class="link-block-21 w-inline-block">
                    <div class="text-block-69">Подробнее</div>
                </a>
                <div id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bd6-16e3a100" class="card-logo-wrappper"></div>
                </div>
            </div>
            </div>
        </div>
        `
        $('#complex-collection').append(element).show(
            150, 'fast'
        )
    }
};

var obj;
function loadInsertComplexes(url=NaN) {
    var lurl = (`https://${document.domain}/${url}`) ?  url: obj.next.replace("http", "https");

    $.ajax({
        url: lurl,
        type: "GET",
        success: function (data, textStatus, jqXHR) {
            insertComplexes(data.results);
            if(!data.next){
                $("#show-more").hide();
                $('#visible-count').text(data.count)
            }
            else {
                let offset = getQueryParam(data.next, 'offset')
                $('#visible-count').text(offset)
                let left = data.count - offset
                $("#compl-left").text(`(Осталось ${left})`)
            }
            obj = data

        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log('Error %s complexses', textStatus);
        }
    });      

};
function removeComplexes(){
    $('#complex-collection').children('.collection-item-5').remove()
}

$(function () {
    loadInsertComplexes('/api/primary/?ordering=-click_amount&limit=4&offset=0');
    var typingTimer;                
    var doneTypingInterval = 800;  
    var $input = $('#search-input');
    $input.on('keyup', function () {
        clearTimeout(typingTimer);
        typingTimer = setTimeout(doneTyping, doneTypingInterval);
    });
    $input.on('keydown', function () {
        clearTimeout(typingTimer);
    });
    function doneTyping () {
        let queru = $input.val()
        if(queru.length > 2){
            $('#complex-collection').children('.collection-item-5').remove();
            loadInsertComplexes(`/api/primary/?search=${queru}&limit=4`);
        }
    }
    $("#show-more").click( function() {
        loadInsertComplexes();
    });
    var arr = new Set();
    $(".area-checkbox").change( function() {
        var val = $(this).next().text();
        (this.checked ) ? arr.add(val): arr.delete(val);
        if(arr.size > 0){
            let nam = arr.values().next().value;
            $('#complex-collection').children('.collection-item-5').remove();
            console.log(`api/primary/?area__name=${nam}&limit=4`);
            loadInsertComplexes(`api/primary/?area__name=${nam}&limit=4`);
            console.log(arr);
        }
        else {
            $input.val('');
            $('#complex-collection').children('.collection-item-5').remove();
            loadInsertComplexes('/api/primary/?ordering=-click_amount&limit=4&offset=0');
            $("#show-more").show();
        }
        
    });
    $("#reset").click( function() {
        $input.val('');
        arr.clear();
        $(".areas").children('.w--redirected-checked').removeClass('w--redirected-checked');
        $('#complex-collection').children('.collection-item-5').remove();
        loadInsertComplexes('/api/primary/?ordering=-click_amount&limit=4&offset=0');
        $("#show-more").show();
    });
    $('#complex-collection').on('click', '.dw-btn', function() {
        href = $(this).parent().find( ".hidden-link" ).prop('href');
        let complex = $(this).parent().find( ".hidden-link" ).text();
        $(document).find(".hidden-inp").val(complex);
        $(".modal").css("display", "block");
        $(".modal").css("opacity", "100%");
    });
    $('#complex-collection').on('click', '.close-icon-2', function() {
        $(".modal").css("display", "none");
    });
});