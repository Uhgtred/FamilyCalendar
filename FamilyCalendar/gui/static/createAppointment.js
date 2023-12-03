const dateInput = document.getElementsByName('date')[0];
const endDateInput = document.getElementsByName('endDate')[0];

function changeValueOfEndDate(value) {
    // setting the input from the appointment-start-date as default value for end-date
    endDateInput.setAttribute('value', value);
}

// receiving input from date-input-field
dateInput.addEventListener('input', function () {changeValueOfEndDate(dateInput.value)});
