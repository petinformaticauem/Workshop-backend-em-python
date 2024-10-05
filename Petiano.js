// Alerta ao clicar no botão "Alterar email"
document.getElementById('alterar-email').addEventListener('click', function() {
    alert('E-mail alterado com sucesso!');
});

// Validação de alteração de senha
document.getElementById('alterar-senha').addEventListener('click', function() {
    const senhaAtual = document.getElementById('senha-atual').value;
    const novaSenha = document.getElementById('nova-senha').value;
    const confirmarSenha = document.getElementById('confirmar-senha').value;

    if (novaSenha === confirmarSenha) {
        alert('Senha alterada com sucesso!');
    } else {
        alert('As senhas não coincidem!');
    }
});

// Alerta ao salvar dados
document.getElementById('salvar-dados').addEventListener('click', function() {
    alert('Dados salvos com sucesso!');
});

// Validação para excluir conta
document.getElementById('excluir-btn').addEventListener('click', function() {
    const frase = document.getElementById('excluir-conta').value;

    if (frase === "Eu quero excluir minha conta") {
        alert('Conta excluída com sucesso!');
    } else {
        alert('A frase digitada está incorreta.');
    }
});
