var i = 0; /* Set Global Variable i */
function increment(){
i += 1; /* Function for automatic increment of field's "Name" attribute. */
}
/*
---------------------------------------------

Function to Remove Form Elements Dynamically
---------------------------------------------

*/
function removeElement(parentDiv, childDiv){
if (childDiv == parentDiv){
alert("The parent div cannot be removed.");
}
else if (document.getElementById(childDiv)){
var child = document.getElementById(childDiv);
var parent = document.getElementById(parentDiv);
parent.removeChild(child);
}
else{
alert("Child div has already been removed or does not exist.");
return false;
}
}




function addMaterialFunction(){

    // var r = document.createElement('fieldset');
    var y = document.createElement("INPUT");
    y.setAttribute("type", "text");
    y.setAttribute("placeholder", "material name");
    y.setAttribute("name", "name[]");
    y.setAttribute("id", "name[]");
    var g = document.createElement("IMG");
    // g.setAttribute("Material")
    // g.setAttribute("src", "delete.png");
    increment();
    // y.setAttribute("Name", "textelement_" + i);
    // y.setAttribute("Name", "name");
    // r.appendChild(y);
    // g.setAttribute("onclick", "removeElement('myForm','id_" + i + "')");
    // r.appendChild(g);
    // r.setAttribute("id", "id_" + i);
    document.getElementById("myForm").appendChild(y);
}
