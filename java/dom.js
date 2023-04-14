
// let el = document.getElementById("div-1")
// let el = document.getElementsByClassName("div-2")
// let el = document.querySelector("#div-1")
// console.log(el)


// el.innerHTML= "Hellow World"

// let input = document.getElementById("input")
// console.log(input)

// input.setAttribute("type","checkbox")

// let input = document.getElementById("input")
// input.style.borderColor = "red"
// input.style.color = "yellow"

// const pElement = document.createElement("p")
// const divE1 = document.getElementById("div-1")

// divE1.appendChild(pElement)

// pElement.innerHTML = "Hellow mas"

// divE1.removeChild(pElement)

// const hello = document.getElementById("hello")
// hello.addEventListener("mouseenter",function(){
//     // console.log("Darren gay")
//     hello.style.border = "1px solid red"
// })

// const btn = document.getElementById("btn")
// btn.addEventListener("click",function(){
//     boom.style.display = "block"
// })

function showBoom (){
    const boom = document.getElementById("boom")
    boom.style.display = "block"
}

function addBorder(el){
        el.style.border = " 1px solid blue"
}