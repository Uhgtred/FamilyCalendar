const dateInput = document.getElementsByName('date')[0];
const endDateInput = document.getElementsByName('endDate')[0];
const inputs = document.getElementsByName('form-input');

function changeValueOfEndDate(value) {
    // setting the input from the appointment-start-date as default value for end-date
    endDateInput.setAttribute('value', value);
}

// receiving input from date-input-field
dateInput.addEventListener('input', function () {changeValueOfEndDate(dateInput.value)});
$(function (){
    inputs[0].keyboard();
});
