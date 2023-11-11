const subNavigationElements = document.getElementsByClassName('subNavigation');

console.log(subNavigationElements);

function printCalendarEvent(){
    console.log('CLICKED CALENDAR!!!')
}

for (let counter = 0; counter < subNavigationElements.length; counter++) {
    let subElement = subNavigationElements[counter]
    switch (subElement.innerText){
        case 'Calendar':
            subElement.addEventListener('click', printCalendarEvent)
    }
    subElement.addEventListener('click', function (){
        console.log('clicked the link!!!')
    })
}
