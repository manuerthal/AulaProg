$(function () { // quando o documento estiver pronto/carregado

    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btLogin", function () {
        //pegar dados da tela
        login = $("#campoLogin").val();
        senha = $("#campoSenha").val();
        // preparar dados no formato json
        var dados = JSON.stringify({ nome: login, senha: senha});
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/atualizar/Pessoa',
            type: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: pessoaLogin, // chama a função listar para processar o resultado
        });
        function pessoaLogin(retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Pessoa logada com sucesso!");
                // encaminha para a página de edição da pessoa
                window.location = "principal.html";
            } else {
                // informar mensagem de erro
                alert("ERRO no login: " + retorno.resultado + ":" + retorno.detalhes);
                document.location.reload(true);
            }
        }
        if (login == "mylogin" && senha == "123") {
            // guarda na sessao
            sessionStorage.setItem('login', login);

            // encaminha para a página principal
            window.location = 'principal.html';
        } else {
            alert("Login ou senha inválido(s)!!");
        }        
    });   

});