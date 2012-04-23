// SHOW POP-OVER
function showPopOver(divID) {
    // SET THE DIV POSITION
    //document.getElementById(divID).style.left = "200px";
    //document.getElementById(divID).style.top = "100px";
    // SHOW THE DIV
    document.getElementById(divID).style.display = "block";
    document.getElementById('blanket').style.display = "block";
}

// CLOSE POP-OVER
function closePopOver(divID) {
    // HIDE THE DIV
    document.getElementById(divID).style.display = "none";
    document.getElementById('blanket').style.display = "none";
}
