console.log("I am working properly!");

const author = "Adarsh Maurya!";

console.log(`Developer ${author}`);




var typed = new Typed(".dynamic-txt",{
    strings:["Flavor Master."],
    typeSpeed:100,
    backSpeed:100,
    backDelay:1000,
    loop:true,


});


let menuBtnCond = true;
let checkLabel = document.getElementById("check-label");

const menuBtnChanger = function(){

    if (menuBtnCond){
        checkLabel.innerHTML = `<i class='bx bx-x'></i>`;
        menuBtnCond = false;
    }

    else{
        checkLabel.innerHTML = `<i class='bx bx-menu'></i>`;

        menuBtnCond = true;
    }

}

let menuBtn = document.getElementById("check");
menuBtn.addEventListener("click", menuBtnChanger);