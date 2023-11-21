const basePath = window.location.origin;
const currentYear = new Date().getFullYear();

function visitURLEvent(url){
    window.close(); // TODO: change this at some point. This feels wrong.
    window.open(url);
}

const currentMonth = new Date().getMonth() + 1;
$('.clnd-btn').click(function (){$('nav ul .clnd-optn-show').toggleClass("show")});
$('.apnt-btn').click(function (){$('nav ul .apnt-optn-show').toggleClass("show")});
$('.view-clnd-btn').click(function (){visitURLEvent(basePath + '/calendar/' + currentYear + '/' + currentMonth)});
$('.new-clnd-btn').click(function (){visitURLEvent(basePath + '/CreateCalendar/')});