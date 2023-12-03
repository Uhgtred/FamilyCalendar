const appointments = document.getElementsByClassName('appointmentItemBtn');
const monthButtons = document.getElementsByClassName('monthSelect');

const months = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"];
const title = document.querySelector('h1');

let month = title.innerText.split(' ')[0];
let year = title.innerText.split(' ')[1];

title.innerText = months[month - 1];

function appointmentBtnFunction (appointmentID) {
    // open url of the appointment
    console.log(appointmentID);
    let url = basePath + '/appointment/' + appointmentID;
    window.location.replace(url);
}

for (let counter = 0; counter < appointments.length; counter++){
    // adding a button-event to each appointment in a calendar-day
    const appointment = appointments[counter];
    appointment.addEventListener('click', function () {appointmentBtnFunction(appointment.id)});
}

function monthSwitcher(direction){
    if (Number(month) == 12 && direction=='up'){
        window.location.replace(basePath + '/' + 'calendar' + '/' + Number(year+1) + '/' +  1);
    }
}
monthButtons[0].addEventListener('click',function (){window.location.replace(basePath + '/' + 'calendar' + '/' + year + '/' +  (Number(month)-1))});
monthButtons[1].addEventListener('click',function (){window.location.replace(basePath + '/' + 'calendar' + '/' + year + '/' +  (Number(month)+1))});