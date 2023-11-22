const currentYear = new Date().getFullYear();
const currentMonth = new Date().getMonth() + 1;
const basePath = document.location.origin

function visitURLEvent(url){
    window.location.replace(url);
}

$(document).on('click', '.clnd-btn', function (){
    $('nav ul .clnd-optn-show').toggleClass("show")
});
$(document).on('click','.apnt-btn', function (){
    $('nav ul .apnt-optn-show').toggleClass("show")
});
$(document).on('click', '.home-btn', function () {
    visitURLEvent(basePath)
})
$(document).on('click', '.view-clnd-btn', function (){
    visitURLEvent(basePath + '/calendar/' + currentYear + '/' + currentMonth)
});
$(document).on('click', '.new-clnd-btn', function (){
    visitURLEvent(basePath + '/CreateCalendar/')
});
$(document).on('click', '.new-apnt-btn', function (){
    visitURLEvent(basePath + '/CreateAppointment/')
});