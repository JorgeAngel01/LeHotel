const value = JSON.parse(document.getElementById('cost').textContent);
valor = parseFloat(value)
console.log(typeof valor)

const myForm = document.forms['reserva'];
myForm.reset();

myForm.costo.value = `Tu total es: $${valor}`
myForm.oninput =_=>
{
let sum = valor;

myForm.querySelectorAll('input[type=checkbox]').forEach( chkBx => 
    {
    if (chkBx.checked) sum += +parseFloat(chkBx.value)

    })  
console.log(sum)
myForm.costo.value = `Tu total es: $${sum}`
myForm.cost.value = sum
}


function errorAlert(){

    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Something went wrong!',
        footer: '<a href>Why do I have this issue?</a>'
    })
}

/*myForm.onsubmit = e =>
{                                                                                                                                                 ,                 
e.preventDefault()  // disable submit
}*/
