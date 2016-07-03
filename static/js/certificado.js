var monthNames = [
  "Janeiro",
  "Fevereiro",
  "Março",
  "Abril",
  "Maio",
  "Junho",
  "Julho",
  "Agosto",
  "Setembro",
  "Outubro",
  "Novembro",
  "Dezembro"
];

var date = new Date();
var day = date.getDate();
var monthIndex = date.getMonth();
var year = date.getFullYear();

var formatedDate = day + " de "+ monthNames[monthIndex] +" de "+ year;

console.log(formatedDate);

var nome = window.location.search.split("=")[1];

document.getElementById("nomeAluno").innerHTML = unescape(nome);
document.getElementById("data").innerHTML = formatedDate;
