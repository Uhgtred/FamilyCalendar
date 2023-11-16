const days = document.getElementsByClassName('daySquares')
console.log(days)

function printSomething(day){
    console.log('Clicked day ' + day + ' of a Month!')
}

for (let counter = 0; counter < days.length; counter++){
    const daySquare = days[counter]
    daySquare.addEventListener('click', function (){printSomething(counter)})
}