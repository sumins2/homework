
const include = document.querySelector('.include')
const exclude = document.querySelector('.exclude')
const textBox = document.querySelector('.textBox')

function write(event) {
    let inputValue = "";
    inputValue = event.target.value;
    include.textContent = `${inputValue.length}`;
    exclude.textContent = `${inputValue.replace(/(\s*)/g, "").length}`;
}
textBox.addEventListener("keydown", write);


// const textCounter = function() {
//     let length  = textBox.value
//     include.textContent = length.length
//     exclude.textContent = length.replace(" ","").length

//     }]4
