const currentYear = new Date().getFullYear();
const currentMonth = new Date().getMonth() + 1;
const basePath = document.location.origin

function visitURLEvent(url){
    window.location.replace(basePath + url);
}

function navButtonEvent(subNavContent){
    // subNavContent.toggleClass('show');
    subNavContent.classList.toggle('calendarMenu');
}

const homeClass = document.getElementsByClassName('home-btn');
homeClass[0].addEventListener('click', function (){visitURLEvent('')});

const calendarMenuClass = document.getElementsByClassName('calendarMenu-btn')[0];
calendarMenuClass.addEventListener('click', function (){navButtonEvent(calendarMenuClass)});

const viewCalendarButton = document.getElementsByClassName('view-calendar-btn');
viewCalendarButton[0].addEventListener('click', function (){visitURLEvent('/calendar/' + currentYear + '/' + currentMonth)});

const newCalendarButton = document.getElementsByClassName('new-calendar-btn');
newCalendarButton[0].addEventListener('click', function (){visitURLEvent('/CreateCalendar/')});

const newAppointmentButton = document.getElementsByClassName('new-appointment-btn');
newAppointmentButton[0].addEventListener('click', function (){visitURLEvent('/CreateAppointment/')})

const slideMenuClass = document.getElementsByClassName('slideMenu');
slideMenuClass[0].addEventListener('click', function () {navButtonEvent($('nav ul .slideMenu'))});