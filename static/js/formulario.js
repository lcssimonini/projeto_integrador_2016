
$(document).ready(function() {
  $("#questionario").submit(function(e){
    e.preventDefault();

    var correctCounter = 0;
    var checkedCounter = 0;
    $("#questionario").find(':input').each(function(){
      console.log(this.checked+"  "+this.getAttribute("status"));

      if(this.checked){
        checkedCounter++;
      }

      if(this.checked && this.getAttribute("status") == "certa"){
        correctCounter++;
      }
    });

    console.log("respostas corretas: "+correctCounter);
    console.log("respostas selecionadas: "+checkedCounter);

    if(checkedCounter < 10) {
      alert("Responda todas as perguntas antes de continuar");
    } else {
      if(correctCounter > 6) {

        var aluno = prompt("Parabéns, você foi aprovado. Digite seu nome para o certificado", "Keyser Söze");
        if (aluno !== null) {
          var curso = window.location.pathname.split("/")[1];
          window.location.href = "/" + curso + "/certificado?nome="+aluno;
        }

      } else {
        alert("Você foi reprovado, tente novamente");
      }
    }
  });
});
