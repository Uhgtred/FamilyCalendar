const appointments = document.getElementsByClassName('appointmentItemBtn');

function appointmentBtnFunction (appointmentID) {
    // open url of the appointment
    console.log(appointmentID);
    let url = basePath + '/appointment/' + appointmentID;
    window.location.replace(url);
}

for (let counter = 0; counter < appointments.length; counter++){
    const appointment = appointments[counter];
    appointment.addEventListener('click', function () {appointmentBtnFunction(appointment.id)});
}