var closing = undefined;
var closingInterval = undefined;

function doClose() {
    $(closing).children("ul").stop(true, true).slideUp(100);
    closing = undefined;
    closingInterval = undefined;
}
$("#side-nav>ul>li").children("ul").hide();
$("#side-nav>ul>li>a").mouseenter(function() {
    var $menu = $(this).closest('li');
    if (closing) {
        clearTimeout(closingInterval);
        if (closing != $menu[0]) {
            doClose();
        }
        else {
            closing = undefined;
            closingInterval = undefined;
        }
    }
    $menu.children("ul").stop(true, true).slideDown(100);
});
$("#side-nav>ul>li").mouseleave(function() {
    closing = this;
    closingInterval = setTimeout(doClose, 100);
});

$(document).ready(function(){
    var current_URL = window.location.pathname;
    if (current_URL.split('/').length<=4){
        $("#side-nav>ul>li>a[href='"+current_URL+"']").addClass("active");
    }
    else{   
        $("#side-nav>ul>li>ul>li>a[href='"+current_URL+"']").parent().parent().prev().addClass("active");
    }
});