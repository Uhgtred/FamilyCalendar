const basePath = window.location.origin;
const currentYear = new Date().getFullYear();
const currentMonth = new Date().getMonth() + 1;

$('.clnd-btn').click(function (){$('nav ul .clnd-optn-show').toggleClass("show")});
$('.apnt-btn').click(function (){$('nav ul .apnt-optn-show').toggleClass("show")});
$('.home-btn').click(function (){window.location.replace(basePath)});
$('.view-clnd-btn').click(function (){window.location.replace(basePath + '/calendar/' + currentYear + '/' + currentMonth)});
$('.new-clnd-btn').click(function (){window.location.replace(basePath + '/CreateCalendar/')});
$('.new-apnt-btn').click(function (){window.location.replace(basePath + '/CreateAppointment/')})