// Obtendo referências aos elementos do formulário
const criarContaBtn = document.getElementById('criar-conta');
const nomeCompletoInput = document.getElementById('nome-completo');
const cpfInput = document.getElementById('cpf');
const emailInput = document.getElementById('email');
const cursoSelect = document.getElementById('curso');
const senhaInput = document.getElementById('senha');
const confirmarSenhaInput = document.getElementById('confirmar-senha');

// Função para validar o formulário
function validarFormulario() {
    const nomeCompleto = nomeCompletoInput.value.trim();
    const cpf = cpfInput.value.trim();
    const email = emailInput.value.trim();
    const curso = cursoSelect.value;
    const senha = senhaInput.value;
    const confirmarSenha = confirmarSenhaInput.value;

    // Verificações
    if (!nomeCompleto) {
        alert('Por favor, insira seu nome completo.');
        return false;
    }
    if (!cpf) {
        alert('Por favor, insira seu CPF.');
        return false;
    }
    if (!email) {
        alert('Por favor, insira seu e-mail.');
        return false;
    }
    if (!curso) {
        alert('Por favor, selecione seu curso.');
        return false;
    }
    if (!senha) {
        alert('Por favor, insira sua senha.');
        return false;
    }
    if (senha !== confirmarSenha) {
        alert('As senhas não correspondem. Tente novamente.');
        return false;
    }

    // Se todas as validações forem bem-sucedidas
    return true;
}

// Evento de clique do botão "Criar"
criarContaBtn.addEventListener('click', function() {
    if (validarFormulario()) {
        alert('Conta criada com sucesso!');

        // lógica
    
    }
});
