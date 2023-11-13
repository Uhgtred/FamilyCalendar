const days = document.getElementById('daySquares')
console.log(days)
function printSomething(){
    console.log('Clicked a day of a Month!')
}

for (let counter = 0; counter < days.length; counter++){
    const daySquare = days[counter]
    daySquare.addEventListener('click', printSomething)

    // switch (day.innerText) {
    //     case 'daySquare':
    //         day.addEventListener('click', printSomething);
    // }
}