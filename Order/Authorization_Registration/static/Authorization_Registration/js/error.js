let errors = document.querySelector(".errors")
let error = document.querySelector(".error")

error.style.color = "red"
error.style.fontSize = "2em";
error.style.left = "100%"
error.style.whiteSpace = "nowrap"
let x = error.getBoundingClientRect().left
let weld = error.getBoundingClientRect().left - error.getBoundingClientRect().width
console.log(x)
let gate = 30
setInterval(nado => {
    if (x >= weld - 50){
        x -= gate
        error.style.left = `${x}px`
    } else {
        clearInterval()
    }
    if (gate >= 20){
        gate -= 2
    } else if (gate >= 10){
        gate -= 1.5
    } else if (gate >= 3){
        gate -= 1
    }
}, 10)
console.log(x)