class Complex {
    constructor(complexKey='primary') {
        this.selector = `.complex-${complexKey}`;
        this.shownResults = [];
        this.objList = [];
        this.nextAmount = 4;
        this.shownAmount = 0;
       
        this.choices = new Set();
        this.typingTimer;                
        this.typingInterval = 800; 
        let me = this;   
        $.ajax({
            url: `https://${document.location.hostname}/api/${complexKey}/?ordering=-click_amount`,
            type: "GET",
            success: function (data, textStatus, jqXHR) {
                me.objList = data;
                me.shownResults = data.map((obj, i) => i);
                me.show();
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log('Error %s complexes', jqXHR);
            }
        });      
    }

    clear(){
        $(this.selector).find('.complex-collection').children(
            '.collection-item-5'
        ).remove();
        this.shownAmount = 0;
    }

    __resaleElement(obj){
        let element = `
            <div class="collection-item-4">
            <div data-w-id="983a5740-c762-b0ee-c2fc-3eb3c1b94a89" class="wrapper">
            <img loading="lazy" width="500" src="${ obj.title_image }" style="-webkit-transform:translate3d(0, 0, 0) scale3d(null, null, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 0, 0) scale3d(null, null, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 0, 0) scale3d(null, null, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 0, 0) scale3d(null, null, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0)" alt="" class="image-8">
            <div class="cover cover-3">
                <div class="w-layout-grid grid-5 g-5">
                    <div id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94a8d-e36ab9af" class="div-block-3 dd-3">
                    <a id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94a8e-e36ab9af" href="#" class="link-block-4 l4 w-inline-block">
                        <div class="text-block-7">${ obj.area.name }</div>
                        <h2 fs-cmsfilter-field="name" class="heading-7 text-link">${ obj.name }</h2>
                        <div fs-cmsfilter-field="addres" id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94aa7-e36ab9af" class="text-block-21 txt-center t3 t4">${ obj.addres }</div>
                        <h4 fs-cmsfilter-field="price" class="heading-43 en">${ obj.price } $</h4>
                        <h4 fs-cmsfilter-field="price" class="heading-43 ru">${ obj.price } ₽</h4>
                    </a>
                    </div>
                    <a id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94aaa-e36ab9af"  href="#" class="button download dw-btn w-button en">Request a presentation</a>
                    <a id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94aaa-e36ab9af"  href="#" class="button download dw-btn w-button ru">Запросить презентацию</a>
                    <a href="#" id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94aac-e36ab9af" class="hidden-link">${ obj.url }</a>
                    <a id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94aae-e36ab9af" href="#" class="link-block-3 w-inline-block">
                        <div class="button text-link about en">About</div>
                        <div class="button text-link about ru">Подробнее</div>
                    </a>
                </div>
            </div>
            </div>
            </div>
        `
        return element
    }

    __primaryElement(obj){
        let element = `
            <div class="collection-item-5">
            <div data-w-id="32da13cd-eac5-e877-d785-b77c3b085bb5" class="wrapper-2">
            <img src="${ obj.title_image }" width="500" style="" loading="lazy" alt="" class="image-43 ani-im">
            <div class="cover cover-3">
                <div class="w-layout-grid grid-26">
                <div id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bb9-16e3a100" class="div-block-3 gb">
                    <a id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bba-16e3a100" href="#" class="link-block-4 w-inline-block">
                        <div class="text-block-68">${ obj.area.name }</div>
                        <h2 class="heading-7 text-link">${ obj.name }</h2>
                    </a>
                    <div id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bc1-16e3a100" class="div-block-9">
                        <div class="en text-block-67 ttx-left">${ obj.squares_en } m<sup>2</sup></div>
                        <div class="ru text-block-67 ttx-left">${ obj.squares } м<sup>2</sup></div>
                    </div>
                    <div id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bc7-16e3a100" class="div-block-1108">
                        <div class="en text-block-21 txtx-left">${ obj.price_from_en } $/m²</div>
                        <div class="ru text-block-21 txtx-left">${ obj.price_from } ₽/м²</div>
                    </div>
                </div>
                <a id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bce-16e3a100" href="#" class="button-5 download dw-btn w-button en">Request a presentation</a>
                <a id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bce-16e3a100" href="#" class="button-5 download dw-btn w-button ru">Запросить презентацию</a>
                <a href="#" id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bd0-16e3a100" class="hidden-link">${ obj.url }</a>
                <img src="${ obj.get_logo }" id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bd2-16e3a100" loading="lazy" alt="" class="image-39">
                <a id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bd3-16e3a100" href="${ obj.url }" class="link-block-21 w-inline-block">
                    <div class="text-block-69 en">About</div>
                    <div class="text-block-69 ru">Подробнее</div>
                </a>
                <div id="w-node-_32da13cd-eac5-e877-d785-b77c3b085bd6-16e3a100" class="card-logo-wrappper"></div>
                </div>
            </div>
            </div>
            </div>
        `;
        return element;
    }

    __showNew(complexIdsToShow){
        let me = this;
        complexIdsToShow.forEach(function (item, index) {
            let obj = me.objList[item];
            let element = (me.selector.split('-')[1] === 'primary') ? me.__primaryElement(obj): me.__resaleElement(obj)
            $(me.selector).find('.complex-collection').append(element).show(
                150, 'fast'
            );
        });
        this.shownAmount += complexIdsToShow.length;
    }

    show(){
        let complexAmount = this.shownResults.length
        let complexLeft = complexAmount - this.shownAmount;
        let count = (complexLeft >= this.nextAmount) ? this.nextAmount : complexLeft
        if(count <= 0){
            $(this.selector).find("#show-more").hide();
            return false
        }
        $(this.selector).find("#show-more").show();
        let complexIdsToShow = this.shownResults.slice(this.shownAmount, this.shownAmount+count)
        this.__showNew(complexIdsToShow);

        complexLeft = complexAmount - this.shownAmount
        if(complexLeft == 0){
            $(this.selector).find("#show-more").hide();
        }
        $(this.selector).find("#compl-left").text(complexLeft);
        $(this.selector).find('#visible-count').text(this.shownAmount)
        return true
    }

    search(query){
        let me = this;
        let searchObjs = [];
        this.shownResults.forEach(cId => {
            let r1 = me.objList[cId].name.search(query);
            let r2 = me.objList[cId].area.name.search(query);
            r1 = (r1 == -1) ? 1000: r1;
            r2 = (r2 == -1) ? 1000: r2;
            if (r1 + r2 < 2000)
                searchObjs.push({cId: cId, cOrder: r1 + r2});
        });
        console.log(searchObjs);
        this.shownResults = searchObjs.sort((a, b) => {
            (a.cOrder >= b.cOrder) ? -1: 1
        }).map(o => o.cId);
    }

    filterArea(query){
        let filterResults = [];
        this.objList.forEach((complex, cId) => {
            var exsists = false;
            query.forEach(area => {
                exsists = (complex.area.name === area) ?  true: exsists;
            })
            if(exsists){
                    filterResults.push(cId);
            }
        });
        this.shownResults = filterResults;
    }

    clearResetResults(){
        this.clear();
        this.shownResults = this.objList.map((obj, i) => i);
        $(this.selector).find("#show-more").show()
    }

    processFltering(searchVal, newChoice, isChecked){
        (isChecked) ? this.choices.add(newChoice): this.choices.delete(newChoice);
        if(this.choices.size > 0){
            this.filterArea(Array.from(this.choices));
            this.clear();
            this.show();
        }
        else {
            if(searchVal)
                this.search(searchVal);
            this.clearResetResults();
            this.show();
        }

    }

    processSearching(inputVal){
        clearTimeout(this.typingTimer);
        let me = this;
        this.typingTimer = setTimeout(function() {
            if(inputVal.length >= 2){
                me.clearResetResults();
                me.search(inputVal);
                me.show()
            }
            else if(inputVal.length == 0){
                me.clearResetResults();
                me.show()
            }

        }, this.typingInterval);
    }

    clearTimeout(){
        clearTimeout(this.typingTimer);
    }
}



$(function () {
    const primary = new Complex('primary'); 
    
    var $primaryObj = $(primary.selector);

    var $input = $primaryObj.find('#search-input');
    $input.on('keyup', function () {
        primary.processSearching($input.val())
    });
    $input.on('keydown', function () {
        primary.clearTimeout();
    });
    $primaryObj.find("#show-more").click( function() {
        primary.show()
    });
    $primaryObj.find("#reset").click( function() {
        $input.val('');
        primary.clearResetResults();
        primary.show()
        $primaryObj.find('.w--redirected-checked').removeClass('w--redirected-checked');
    });
    $primaryObj.find(".area-checkbox").change( function() {
        let choice = $(this).next().text();
        primary.processFltering($input.val(), choice, this.checked)
    });
});