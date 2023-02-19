let num_steps = document.getElementById("steps_sec").childElementCount;

var steps = document.getElementsByClassName("steps")
for (var i = 1; i < num_steps; i++) {
    steps[i].hidden = true
}
document.getElementById("results").hidden = true
document.getElementById("thanks").hidden = true

let step_num = 1

function showNext() {
    
    if (step_num == num_steps) {
        document.getElementById("next").style.display = "none"
        document.getElementById("results").hidden = false
    }
    else {
        steps[step_num].hidden = false
        step_num++
    }
    window.scrollTo(0, document.body.scrollHeight)
}

function rated() {
    document.getElementById("ratings").hidden = true
    document.getElementById("thanks").hidden = false
}