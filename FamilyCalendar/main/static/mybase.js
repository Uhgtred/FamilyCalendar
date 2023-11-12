const subNavigationElements = document.getElementsByClassName('subNavigation');

// console.log(subNavigationElements);

const basePath = window.location.origin;
const currentYear = new Date().getFullYear();

function printCalendarEvent(){
    // console.log('CLICKED CALENDAR!!!');
    const pageUrl = basePath + '/calendar/' + currentYear ;
    window.open(pageUrl, '__self');
    // console.log(pageUrl);
}

for (let counter = 0; counter < subNavigationElements.length; counter++) {
    let subElement = subNavigationElements[counter]
    switch (subElement.innerText){
        case 'Calendar':
            subElement.addEventListener('click', printCalendarEvent);

    }
}
