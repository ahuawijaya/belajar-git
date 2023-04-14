// const el = $("p")

// const el = $("#hello")

// const el = $(".world")
// console.log(el )

// .html
// const el = $("#text")
// el.html("<h1>hello world</h1>")

// // .attr
// const input = $("input")
// input.attr("type", "checkbox")

// // add and remove class
// el.addClass ("red")
// el.addClass("blue")
// el.removeClass()

// // css
// input.css({
//     border: "1px solid red" ,
//     marginLeft:"100px"
// })

// const el = $("#text")
// el.mouseenter(function(){
//     el.css("border", "1px solid red")
// })

// const inp = $("input")
// inp.focus(function(){
//     inp.css("border", "1px solid")
// })

const btnShow = $("#show")
const btnHide = $("#hide")
const btnFadeIn = $("#fadeIn")
const btnFadeOut = $("#fadeOut")
const btnToggle = $("#Toggle")

const div = $("div")

btnShow.click(function(){
    div.show("slow")
})

btnHide.click(function(){
    div.hide("slow")
})
btnFadeIn.click(function(){
    div.fadeIn("slow")
})
btnFadeOut.click(function(){
    div.fadeOut("slow")
})

btnToggle.click(function(){
    div.slideToggle("slow")
})