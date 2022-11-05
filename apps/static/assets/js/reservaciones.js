const value = JSON.parse(document.getElementById('cost').textContent);
valor = parseFloat(value)
console.log(valor)

const myForm = document.forms['reserva'];
myForm.reset();

myForm.oninput =_=>
{
let sum = valor;

myForm.querySelectorAll('input[type=checkbox]').forEach( chkBx => 
    {
    if (chkBx.checked) sum += +chkBx.value
    })  
console.log(sum)
myForm.costo.value = `Tu total es: $${sum}`
myForm.cost.value = sum
}
/*myForm.onsubmit = e =>
{                                                                                                                                                 ,                 
e.preventDefault()  // disable submit
}*/
