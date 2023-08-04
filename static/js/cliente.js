class Clientes{
    constructor (rut, nombre, apellido,  telefono, correo,contra,contra2) {
        this.rut = rut;
        this.nombre = nombre;
        this.apellido = apellido;
        this.telefono = telefono;
        this.correo = correo;
        this.contra = contra;
        this.contra2 = contra2;
        
    }
}
function agregar(){
    //alert("Entre al metodo agregar");
    console.log("Entre al metodo agregar");
    //recuperar valores del formulario de
    var rut = document.getElementById("rut").value;
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var telefono = document.getElementById("telefono").value;
    var correo = document.getElementById("correo").value;
    var contra = document.getElementById("contraseña").value;
    var contra2 = document.getElementById("contraseña1").value;
        
    var c = new Clientes(rut, nombre, apellidop, apellidom, edad, direccion, telefono, Estado, fechaNa, contra, contra2);
    

    if (!validarRut(rut)){
        return;
    }
    if (nombre.trim().length == 0){
        alert ("Error. Debe ingresar un nombre")
        return; 
       }

    if (apellido.trim().length == 0){
        alert("Error. Debe ingresar el Apellido Paterno");
        return;
    }  
    
    if( !(/^\d{9}$/.test(telefono)) ) {
        alert("Error, el número de teléfono debe tener 9 dígitos");
        return;
    }

    if (contra.trim().length == 0){
        alert("Error, debe tener una contraseña");
        return;
    }

    if (contra.trim().length <= 8){
        alert("Erro. La contraseña debe tener un largo de mínimo 8");
        return;
    }
    if (contra2.trim().length == 0){
        alert("Error, debe volver a ingresar una contraseña");
        return;
    }
    if (contra2.trim().length <= 7 ){
        alert("Error. La contraseña debe tener un largo de mínimo 8");
        return;
    }
    if (contra != contra2){
        alert ("Error. Las contraseñas son distintas");
        return;
    }
    
    //crear objeto en javascript
    //alert("codigo del producto :" + p.codigo);
    
    //crear lista de productos
    cliente = [];
    //agregar producto a la lista de productos
    cliente.push(c);

    //Uso de localStorage para almacenar la lista de objetos
    
    //1. Se obtiene el localstorage para verificar si existe 
    //   algun producto dentro de la lista
     var listaCliente = localStorage.getItem('datosC');
    //alert("Contenido inicial" + listaCliente);

     if(listaCliente == null){
         //Agrega el primer producto
         //alert("Entro al IF");
         localStorage.setItem('datosC', JSON.stringify(cliente));
     }else{
         //Agrega los siguientes productos
         //alert("Entre al Else");
         //sacar la lista del localstorage
         listaCliente = JSON.parse(localStorage.getItem('datosC'));
         //alert("datosC de la lista " + listaCliente);
         listaCliente.push(c);
         localStorage.setItem('datosC', JSON.stringify(listaCliente));
     }

     //Comprobar que la lista se guardo correctamente 
     var guardado = localStorage.getItem('datosC');
    //alert("Valor obtenido " + guardado);
    alert("Se registró correctamente");
}

function validarRut(rut){
    var suma=0;
    var arrRut = rut.split("-");
    var rutSolo = arrRut[0];
    var verif = arrRut[1];
    var continuar = true;
    for(i=2;continuar;i++){
        suma += (rutSolo%10)*i;
        rutSolo = parseInt((rutSolo /10));
        i=(i==7)?1:i;
        continuar = (rutSolo == 0)?false:true;
    }
    resto = suma%11; dv = 11-resto;
    if(dv==10){  
    if(verif.toUpperCase() == 'K') return true;
    }else if (dv == 11 && verif == 0)
        return true;
        else if (dv == verif) return true;
        else alert("RUT incorrecto, ingréselo en el formato 11111111-1");
        return false;
}  