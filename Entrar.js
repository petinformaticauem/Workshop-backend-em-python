// Obtendo referências aos elementos do formulário
const entrarContaBtn = document.getElementById('entrar');
const emailInput = document.getElementById('email');
const senhaInput = document.getElementById('senha');

// Função para validar o formulário
function validarFormulario() {
    const email = emailInput.value.trim();
    const senha = senhaInput.value;

    // Verificações
    if (!email) {
        alert('Por favor, insira seu e-mail.');
        return false;
    }
    if (!senha) {
        alert('Por favor, insira sua senha.');
        return false;
    }

    // Se todas as validações forem bem-sucedidas
    return true;
}

// Evento de clique do botão "Criar"
entrarContaBtn.addEventListener('click', function() {
    if (validarFormulario()) {
        alert('Conta criada com sucesso!');

        // lógica
    
    }
});
