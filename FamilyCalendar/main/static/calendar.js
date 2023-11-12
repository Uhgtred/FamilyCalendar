const days = document.getElementById('Squares')
console.log(days)
function printSomething(){
    console.log('Clicked a day of a Month!')
}

for (let counter = 0; counter < days.length; counter++){
    days[counter].addEventListener('click', printSomething)
    // switch (day.innerText) {
    //     case 'daySquare':
    //         day.addEventListener('click', printSomething);
    // }
}