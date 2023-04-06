function runPython(){
    eel.main()(function(ret){console.log(ret)});
}


function agregarapp(n,r){
    eel.agregar_aplicacion(n,r)(function(ret){console.log(ret)});
}


function agregarcontacto(n,r){
  eel.agregar_contacto(n,r)(function(ret){console.log(ret)});
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
    nombre = nombre.toLowerCase();
    // Haz lo que quieras con los valores obtenidos
    console.log("Nombre: " + nombre + ", Ruta: " + ruta);
    agregarapp(nombre,ruta);

    // Limpia los campos de entrada
    document.getElementById("nombre").value = "";
    document.getElementById("ruta").value = "";

    // Muestra el pop-up
    mostrarPopUp();

    // Limpia el formulario
    document.getElementById("miFormulario").reset();
  }


  function enviarDatoscontact(event) {
    event.preventDefault(); // Prevenir el envío del formulario
    var nombre = document.getElementById("nombre2").value;
    var correo = document.getElementById("correo").value;
    nombre = nombre.toLowerCase();
    // Haz lo que quieras con los valores obtenidos
    console.log("Nombre: " + nombre + ", Correo: " + correo);
    agregarcontacto(nombre,correo);

    // Limpia los campos de entrada
    document.getElementById("nombre2").value = "";
    document.getElementById("correo").value = "";

    // Muestra el pop-up
    mostrarPopUp();

    // Limpia el formulario
    document.getElementById("miFormulario2").reset();
  }


  function cambiarPagina() {
    var switchElem = document.getElementById("mySwitch");
    if (switchElem.checked) {
      // Si el switch está activado, almacena el estado en el almacenamiento local
      localStorage.setItem("switchState", "on");
      // Redirige a la página 1
      window.location.href = "settingsblack.html";
    } else {
      // Si el switch está desactivado, almacena el estado en el almacenamiento local
      localStorage.setItem("switchState", "off");
      // Redirige a la página 2
      window.location.href = "settings.html";
    }
  }
  
  // Función que se ejecuta cuando se carga la página
  function cargarPagina() {
    // Obtiene el estado almacenado en el almacenamiento local
    var switchState = localStorage.getItem("switchState");
    if (switchState === "on") {
      // Si el estado es "on", activa el switch
      document.getElementById("mySwitch").checked = true;
    } else {
      // Si el estado es "off", desactiva el switch
      document.getElementById("mySwitch").checked = false;
    }
  }
  
  // Registra la función cargarPagina para que se ejecute cuando se carga la página
  window.onload = cargarPagina;