const dateInput = document.getElementsByName('date')[0];
const endDateInput = document.getElementsByName('endDate')[0];
const inputs = document.getElementsByClassName('form-input');

function changeValueOfEndDate(value) {
    // setting the input from the appointment-start-date as default value for end-date
    endDateInput.setAttribute('value', value);
}

$(function inputKeyboard(){
    $('#id_name').keyboard({

    usePreview: false,

    visible: function(e, keyboard, el) {
      keyboard.$el.addClass('red');
    },
    beforeClose: function(e, keyboard, el, accepted) {
      keyboard.$el.removeClass('red');
    }
    })
});

$(function inputKeyboard(){
    $('#id_persons').keyboard({

    usePreview: false,

    visible: function(e, keyboard, el) {
      keyboard.$el.addClass('red');
    },
    beforeClose: function(e, keyboard, el, accepted) {
      keyboard.$el.removeClass('red');
    }
    })
});

$(function inputKeyboard(){
    $('#id_description').keyboard({

    usePreview: false,

    visible: function(e, keyboard, el) {
      keyboard.$el.addClass('red');
    },
    beforeClose: function(e, keyboard, el, accepted) {
      keyboard.$el.removeClass('red');
    }
    })
});

// receiving input from date-input-field
dateInput.addEventListener('input', function () {changeValueOfEndDate(dateInput.value)});
