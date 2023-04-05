function runPython(){
    eel.main()(function(ret){console.log(ret)});
}


function agregar(n,r){
    eel.agregar_aplicacion(n,r)(function(ret){console.log(ret)});
}

function mostrarPopUp() {
    document.getElementById("miPopUp").style.display = "block";
  }


function cerrarPopUp() {
  document.getElementById("miPopUp").style.display = "none";
}

function enviarDatos(event) {
    event.preventDefault(); // Prevenir el envío del formulario
    var nombre = document.getElementById("nombre").value;
    var ruta = document.getElementById("ruta").value;
    // Haz lo que quieras con los valores obtenidos
    console.log("Nombre: " + nombre + ", Ruta: " + ruta);
    agregar(nombre,ruta);

    // Limpia los campos de entrada
    document.getElementById("nombre").value = "";
    document.getElementById("ruta").value = "";

    // Muestra el pop-up
    mostrarPopUp();

    // Limpia el formulario
    document.getElementById("miFormulario").reset();
  }