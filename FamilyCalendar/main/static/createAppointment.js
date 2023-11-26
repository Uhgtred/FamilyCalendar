//document.getElementsByName()//.value
const dateInput = document.getElementsByName('date')[0];
const endDateInput = document.getElementsByName('endDate')[0];

function changeValueOfEndDate(value) {
    endDateInput.setAttribute('value', value);
}

dateInput.addEventListener('input', function () {changeValueOfEndDate(dateInput.value)});
