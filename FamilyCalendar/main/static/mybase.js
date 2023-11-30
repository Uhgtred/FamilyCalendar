let currentYear = new Date().getFullYear();
let currentMonth = new Date().getMonth() + 1;
let basePath = document.location.origin

$(document).on('click', '.home-btn', function (){window.location.replace(basePath + '');});

$(document).on('click', '.calendarMenu-btn', function (){$('.calendarMenu').toggleClass('show')});

$(document).on('click', '.view-calendar-btn', function (){window.location.replace(basePath + '/calendar/' + currentYear + '/' + currentMonth)});

$(document).on('click', '.new-calendar-btn', function (){window.location.replace(basePath + '/CreateCalendar/')});

$(document).on('click', '.new-appointment-btn', function (){window.location.replace(basePath + '/CreateAppointment/')})
