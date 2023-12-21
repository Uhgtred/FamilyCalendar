const dateInput = document.getElementsByName('date')[0];
const endDateInput = document.getElementsByName('endDate')[0];
const inputs = document.getElementsByName('form-input');

function changeValueOfEndDate(value) {
    // setting the input from the appointment-start-date as default value for end-date
    endDateInput.setAttribute('value', value);
}

$(function(){
    $('#id_name').keyboard({

    usePreview: false,

    visible: function(e, keyboard, el) {
      keyboard.$el.addClass('red');
    },
    beforeClose: function(e, keyboard, el, accepted) {
      keyboard.$el.removeClass('red');
    }
    })
    // console.log('test');
    // dateInput.keyboard;
});

// receiving input from date-input-field
dateInput.addEventListener('input', function () {changeValueOfEndDate(dateInput.value)});
// dateInput.addEventListener('click', test)
