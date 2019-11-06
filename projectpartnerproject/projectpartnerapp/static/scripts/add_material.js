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



// Function to dynamically add an empty new material field to the material form so user
// can add as many materials as needed for their project
function addMaterialFunction(){

    var y = document.createElement("INPUT");
    y.setAttribute("type", "text");
    y.setAttribute("placeholder", "material name");
    y.setAttribute("name", "name[]");
    y.setAttribute("id", "name[]");
    increment();
    document.getElementById("myForm").appendChild(y);
}
