const subNavigationElements = document.getElementsByClassName('subNavigation')

for (let counter = 0; counter < subNavigationElements.length; counter++) {
    let button = subNavigationElements[counter]
    button.addEventListener('click', function (){
        console.log('clicked the link!!!')
    })
}