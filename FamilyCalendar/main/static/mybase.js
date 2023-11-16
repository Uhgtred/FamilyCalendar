const subNavigationElements = document.getElementsByClassName('subNavigation');

const basePath = window.location.origin;
const currentYear = new Date().getFullYear();
const currentMonth = new Date().getMonth()


function printCalendarEvent(){
    const pageUrl = basePath + '/calendar/' + currentYear + '/' + currentMonth;
    window.close(); // TODO: change this at some point. This feels wrong.
    window.open(pageUrl);
}

for (let counter = 0; counter < subNavigationElements.length; counter++) {
    let subElement = subNavigationElements[counter]
    switch (subElement.innerText){
        case 'Calendar':
            subElement.addEventListener('click', printCalendarEvent);

    }
}
