class Complex {
    constructor(complexKey = 'primary') {
        this.selector = `.complex-${complexKey}`;
        this.shownResults = [];
        this.objList = [];
        this.nextAmount = 4;
        this.shownAmount = 0;

        this.choices = new Set();
        this.living_choices = new Set();
        this.decorChoice;
        this.priceMinMax = [-1, Math.pow(10, 10)];
        this.squareMinMax = [0, Math.pow(10, 4)];
        this.roomMinMax = [0, Math.pow(10, 2)];

        this.typingTimer;
        this.typingInterval = 800;
        let me = this;
        let site_id = 1;
        if(document.location.hostname.split('.')[0] === 'spb')
            site_id = 2;
        else if (document.location.hostname.split('.')[0] === 'msk')
            site_id = 1;
        else
            site_id = 3;

        $.ajax({
            url: `https://${document.location.hostname}/api/${complexKey}/?site_id=${site_id}`,
            type: "GET",
            headers: {"Authorization": "Token 5665cc8e6e3b3fe647727c92d233065e22eed513"},
            success: function (data, textStatus, jqXHR) {
                me.objList = data;
                me.shownResults = data.map((obj, i) => {
                    return {cId: i, cOrder: i};
                });
                me.show();
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log('Error %s complexes', jqXHR);
            }
        });
    }

    clear() {
        $(this.selector).find('.complex-collection').children(
            '.w-dyn-item'
        ).remove();
        this.shownAmount = 0;
    }

    __resaleElement(obj) {
        let element = `
            <div class="collection-item-4 w-dyn-item">
            <div data-w-id="983a5740-c762-b0ee-c2fc-3eb3c1b94a89" class="wrapper">
            <img loading="lazy" width="500" src="${obj.title_image}" style="-webkit-transform:translate3d(0, 0, 0) scale3d(null, null, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 0, 0) scale3d(null, null, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 0, 0) scale3d(null, null, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 0, 0) scale3d(null, null, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0)" alt="" class="image-8">
            <div class="cover cover-3">
                <div class="w-layout-grid grid-5 g-5">
                    <a id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94a8e-e36ab9af" href="#" class="link-block-4 l4 w-inline-block">
                        <div class="text-block-7">${obj.area.name}</div>
                        <h2 class="heading-7 text-link">${obj.name}</h2>
                        <div id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94aa7-e36ab9af" class="text-block-21 txt-center t3 t4">${obj.addres}</div>
                        <div>
                            <h4 class="heading-43 en">${obj.price} $</h4>
                            <h4 class="heading-43 ru">${obj.price} ₽</h4>
                        </div>
                    </a>
                    <a id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94aaa-e36ab9af"  href="#" class="button download dw-btn w-button en">Request a presentation</a>
                    <a id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94aaa-e36ab9af"  href="#" class="button download dw-btn w-button ru">Запросить презентацию</a>
                    <a href="#" id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94aac-e36ab9af" class="hidden-link">${obj.get_absolute_url}</a>
                    <a id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94aae-e36ab9af" href="${obj.get_absolute_url}" class="link-block-3 w-inline-block">
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

    __primaryElement(obj) {
        let element = `
            <div class="collection-item-4 w-dyn-item">
            <div data-w-id="983a5740-c762-b0ee-c2fc-3eb3c1b949ea" class="wrapper">
            <img src="${obj.title_image}" width="500" style="" loading="lazy" alt="" class="image-8 ani-im">
            <div class="cover cover-3">
                <div class="w-layout-grid grid-5">
                <div id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b949ee-e36ab9af" class="div-block-3 gb">
                    <a id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b949ef-e36ab9af" href="#" class="link-block-4 w-inline-block">
                        <div class="text-block-56">${obj.area.name}</div>
                        <h2 class="heading-7 text-link">${obj.name}</h2>
                    </a>
                    <div id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b949f2-e36ab9af" class="div-block-9">
                        <div class="en text-block-11 ttx-left">${obj.squares_en} m²</div>
                        <div class="ru text-block-11 ttx-left">${obj.squares} м²</div>
                    </div>
                    <div id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b949fd-e36ab9af" class="div-block-39">
                        <div class="en text-block-21 txtx-left">${obj.price_from_en} $/m²</div>
                        <div class="ru text-block-21 txtx-left">${obj.price_from} ₽/м²</div>
                    </div>
                </div>
                <a id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94a03-e36ab9af" data-w-id="983a5740-c762-b0ee-c2fc-3eb3c1b94a03" href="#" class="button download dw-btn w-button en">Request a presentation</a>
                <a id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94a03-e36ab9af" data-w-id="983a5740-c762-b0ee-c2fc-3eb3c1b94a03" href="#" class="button download dw-btn w-button ru">Запросить презентацию</a>
                <a href="#" id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94a05-e36ab9af" class="hidden-link">${obj.get_absolute_url}</a>
                <img src="${obj.get_logo}" id="w-node-f7e24c98-67ea-a3cb-9828-fd59f5de34e9-e36ab9af" loading="lazy" alt="" class="image-39">
                <a id="w-node-_0b5bb57b-8ba5-be3c-5316-ddd084df4e6d-e36ab9af" href="${obj.get_absolute_url}" class="link-block-16 w-inline-block">
                    <div class="text-block-52 en">About</div>
                    <div class="text-block-52 ru">Подробнее</div>
                </a>
                <div id="w-node-_983a5740-c762-b0ee-c2fc-3eb3c1b94a06-e36ab9af" class="card-logo-wrappper"></div>
                </div>
            </div>
            </div>
            </div>
        `;
        return element;
    }

    __showNew(complexIdsToShow) {
        let me = this;
        let rule = (this.selector.split('-')[1] === 'primary')
        complexIdsToShow.forEach(function (item, index) {
            let obj = me.objList[item.cId];
            let element = (rule) ? me.__primaryElement(obj) : me.__resaleElement(obj)
            $(me.selector).find('.complex-collection').append(element).show(
                150, 'fast'
            );
        });
        this.shownAmount += complexIdsToShow.length;
    }

    __string2ASCI(str) {
        let res = -100;
        str.split('').forEach( (v, vid) => {
            res += v.charCodeAt();
        })
        return res;
    }

    clearResetResults() {
        this.clear();
        this.shownResults = this.objList.map((obj, i) => {
            return {cId: i, cOrder: i};
        });
        $(this.selector).find(".show-more").show()
    }

    reset() {
        this.clearResetResults();
        this.choices = new Set();
        this.living_choices = new Set();
        this.show();
    }

    show() {
        let complexAmount = this.shownResults.length
        let complexLeft = complexAmount - this.shownAmount;
        let count = (complexLeft >= this.nextAmount) ? this.nextAmount : complexLeft
        if (count <= 0) {
            $(this.selector).find(".show-more").hide();
            return false
        }
        $(this.selector).find(".show-more").show();
        let complexIdsToShow = this.shownResults.slice(this.shownAmount, this.shownAmount + count)
        this.__showNew(complexIdsToShow);

        complexLeft = complexAmount - this.shownAmount
        if (complexLeft == 0) {
            $(this.selector).find(".show-more").hide();
        }
        $(this.selector).find(".compl-left").text(complexLeft);
        $(this.selector).find('.items-count').text(complexAmount);
        $(this.selector).find('.visible-count').text(this.shownAmount)
        return true
    }

    search(query) {
        let searchObjs = [];
        this.objList.forEach((complex, cId) => {
            let r1 = complex.name.search(query);
            let r2 = complex.area.name.search(query);
            r1 = (r1 == -1) ? 1000 : r1;
            r2 = (r2 == -1) ? 1000 : r2;
            if (r1 + r2 < 2000)
                searchObjs.push({ cId: cId, cOrder: r1 + r2 });
        });
        this.shownResults = searchObjs.sort((a, b) => {
            (a.cOrder >= b.cOrder) ? -1 : 1
        });
    }

    keyFilter(keyField, field) {
        let filterResults = [];
        let me = this;
        
        this.shownResults.forEach(item => {
            let complex = me.objList[item.cId];
            let val = complex[keyField];
            if (val === field)
            filterResults.push({ cId: item.cId, cOrder: me.__string2ASCI(val) });
        });
        this.shownResults = filterResults;
    }

    queryFilter(key, query) {
        query = Array.from(query);
        let filterResults = [];
        let me = this;
        this.shownResults.forEach(item => {
            let complex = me.objList[item.cId];
            var exsists = false;
            query.forEach(name => {
                exsists = (complex[key].name === name) ? true : exsists;
            });
            if (exsists) 
                filterResults.push({ cId: item.cId, cOrder: me.__string2ASCI(complex.name) });
        });
        this.shownResults = filterResults;
    }

    queryFilterLivingType(query) {
        query = Array.from(query);
        let filterResults = [];
        let me = this;
        this.shownResults.forEach(item => {
            let complex = me.objList[item.cId];
            var exsists = false;
            complex.living_type.forEach(val => {
                exsists = (query.includes(val.name)) ? true : exsists;
            })
            if (exsists)
                filterResults.push({ cId: item.cId, cOrder: me.__string2ASCI(complex.name) });
        });
        this.shownResults = filterResults;
    }

    minMaxFilter(keyField, mini, maxi) {
        let filterResults = [];
        this.shownResults.forEach(item => {
            let complex = me.objList[item.cId];
            let val = complex[keyField];
            if (mini <= val && val <= maxi)
            filterResults.push({ cId: item.cId, cOrder: val });
        });
        return filterResults
    }

    __processFltering(searchVal) {
        this.clearResetResults()

        if (searchVal)
            this.search(searchVal);
        

        if (this.choices.size > 0) 
            this.queryFilter('area', this.choices);
        

        if (this.living_choices.size > 0) 
            this.queryFilterLivingType(this.living_choices);
        

        this.shownResults = this.shownResults.sort((a, b) => {
            (a.cOrder >= b.cOrder) ? -1 : 1;
        });
        this.show();

    }

    processFltering(setKey, searchVal, newChoice, isChecked) {
        (isChecked) ? this[setKey].add(newChoice) : this[setKey].delete(newChoice);
        this.__processFltering(searchVal);
    }

    processSearching(inputVal) {
        clearTimeout(this.typingTimer);
        let me = this;
        this.typingTimer = setTimeout(function () {
            if (inputVal.length >= 2) {
                me.__processFltering(inputVal);
            }
            else if (inputVal.length == 0) {
                me.__processFltering('');
            }

        }, this.typingInterval);
    }

    clearTimeout() {
        clearTimeout(this.typingTimer);
    }

    processMinMaxFltering(keyField, mini, maxi, isChecked) {
        (isChecked) ? this.choices.add(newChoice) : this.choices.delete(newChoice);
        if (this.choices.size > 0) {
            this.queryFilterArea(Array.from(this.choices));
            this.clear();
            this.show();
        }
        else {
            if (searchVal)
                this.search(searchVal);
            this.clearResetResults();
            this.show();
        }

    }

    processFltering2(setKey, newChoice, isChecked, key, choice) {
        this.clearResetResults();

        if (newChoice) 
            (isChecked) ? this[setKey].add(newChoice) : this[setKey].delete(newChoice);
        
        if (this.choices.size > 0) 
            this.queryFilter('area', this.choices);

        if (key) 
            this.keyFilter(key, choice);
        
        if (this.living_choices.size > 0) 
            this.queryFilterLivingType(this.living_choices);
        
        this.show();
    } 
}



$(function () {
    const primary = new Complex('primary');
    var $primaryObj = $(primary.selector);
    var $input = $primaryObj.find('.search-input');

    $input.on('keyup', function () {
        primary.processSearching($input.val())
    });
    $input.on('keydown', function () {
        primary.clearTimeout();
    });
    $primaryObj.find(".show-more").click(function () {
        primary.show()
    });
    $primaryObj.find(".reset").click(function () {
        $input.val('');
        primary.reset();
        $primaryObj.find('.w--redirected-checked').removeClass('w--redirected-checked');
    });
    $primaryObj.find(".areas").change(function () {
        let choice = $(this).next().text();
        primary.processFltering('choices', $input.val(), choice, this.checked)
    });
    $primaryObj.find(".living_types").change(function () {
        let choice = $(this).next().text();
        primary.processFltering('living_choices', $input.val(), choice, this.checked)
    });


    const resale = new Complex('resale');
    var $resaleObj = $(resale.selector);

    $resaleObj.find(".show-more").click(function () {
        resale.show()
    });
    $resaleObj.find(".reset").click(function () {
        resale.reset();
        $resaleObj.find('.w--redirected-checked').removeClass('w--redirected-checked');
        $resaleObj.find(".w-radio-input").each(function () {
            this.checked = false;
        });
    });
    $resaleObj.find(".areas").change(function () {
        let choice = $(this).next().text();
        resale.processFltering2('area', choice, this.checked, '', '')
    });
    $resaleObj.find(".w-radio-input").change(function () {
        let choice = $(this).next().text();
        resale.processFltering2('', '', false, 'decor', choice)
    });
    $resaleObj.find(".living_types").change(function () {
        let choice = $(this).next().text();
        primary.processFltering2('living_choices', choice, this.checked, '', '')
    });
});