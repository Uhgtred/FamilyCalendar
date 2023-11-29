const currentYear = new Date().getFullYear();
const currentMonth = new Date().getMonth() + 1;
const basePath = document.location.origin

function visitURLEvent(url){
    window.location.replace(basePath + url);
}

function navButtonEvent(subNavContent){
    // subNavContent.toggleClass('show');
    subNavContent.classList.toggle('show');
}

const homeClass = document.getElementsByClassName('home-btn')[0];
homeClass.addEventListener('click', function (){visitURLEvent('')});

const calendarMenuClass = document.getElementsByClassName('calendarMenu')[0];
const calendarMenuButton = document.getElementsByClassName('calendarMenu-btn')[0];
calendarMenuButton.addEventListener('click', function (){navButtonEvent(calendarMenuClass)});

const viewCalendarButton = document.getElementsByClassName('view-calendar-btn')[0];
viewCalendarButton.addEventListener('click', function (){visitURLEvent('/calendar/' + currentYear + '/' + currentMonth)});

const newCalendarButton = document.getElementsByClassName('new-calendar-btn')[0];
newCalendarButton.addEventListener('click', function (){visitURLEvent('/CreateCalendar/')});

const newAppointmentButton = document.getElementsByClassName('new-appointment-btn')[0];
newAppointmentButton.addEventListener('click', function (){visitURLEvent('/CreateAppointment/')})

const slideMenuClass = document.getElementsByClassName('slideMenu')[0];
const slideMenuButton = document.getElementsByClassName('slideMenu-btn')[0];
slideMenuButton.addEventListener('click', function () {navButtonEvent(slideMenuClass)});