
# Validações de Usuários

**`validacoes_usuarios`** é uma biblioteca Python projetada para facilitar a validação de senhas e e-mails com critérios de segurança. Ela ajuda a garantir que as senhas sejam seguras e evita o uso de e-mails temporários e domínios não confiáveis.

## Índice

1. [Instalação](#instalação)
2. [Como Usar](#como-usar)
3. [Funções Principais](#funções-principais)
4. [Exemplo Completo de Uso](#exemplo-completo-de-uso)
5. [Testes](#testes)
6. [Contribuição](#contribuição)
7. [Licença](#licença)

---

## Instalação

Para instalar o pacote, você pode usar o pip. No terminal, execute:

```bash
pip install validacoes_usuarios
```

Certifique-se de que você possui o Python 3.8 ou superior.

---

## Como Usar

Após instalar o pacote, importe as funções desejadas no seu código. As funções estão disponíveis para validação de senha, verificação de e-mails temporários e validação de domínio de e-mails.

Exemplo de uso básico:

```python
from validacoes_usuarios import validar_senha, validar_email_temporario, validar_email_dns

# Validando uma senha
try:
    validar_senha("SenhaSegura123!", username="usuario", email="usuario@exemplo.com")
    print("Senha válida.")
except ValidationError as e:
    print(f"Erro: {e}")
```

---

## Funções Principais

Abaixo estão as funções principais oferecidas pela biblioteca:

### `validar_senha(senha, username=None, email=None)`

Valida a segurança de uma senha de acordo com critérios específicos, como letras maiúsculas, minúsculas, números e caracteres especiais.

- **Parâmetros**:
  - `senha` (str): A senha que você deseja validar.
  - `username` (str, opcional): Nome de usuário para evitar que esteja contido na senha.
  - `email` (str, opcional): E-mail do usuário para evitar partes do e-mail na senha.

- **Exemplo**:

  ```python
  validar_senha("SenhaSegura123!", username="usuario", email="usuario@exemplo.com")
  ```

### `validar_email_temporario(email)`

Verifica se o e-mail pertence a um domínio temporário proibido.

- **Parâmetros**:
  - `email` (str): O e-mail a ser verificado.

- **Exemplo**:

  ```python
  validar_email_temporario("teste@mailinator.com")
  ```

### `validar_email_dns(email)`

Verifica se o domínio do e-mail possui registros MX, indicando que ele pode receber e-mails.

- **Parâmetros**:
  - `email` (str): O e-mail que você deseja verificar.

- **Exemplo**:

  ```python
  validar_email_dns("usuario@exemplo.com")
  ```

---

## Exemplo Completo de Uso

Aqui está um exemplo integrando todas as funções do pacote em um único script:

```python
from validacoes_usuarios import validar_senha, validar_email_temporario, validar_email_dns

# Validando senha
try:
    validar_senha("SenhaSegura123!", username="usuario", email="usuario@exemplo.com")
    print("Senha válida.")
except ValidationError as e:
    print(f"Erro: {e}")

# Validando e-mail temporário
try:
    validar_email_temporario("teste@mailinator.com")
    print("E-mail permitido.")
except ValidationError as e:
    print(f"Erro: {e}")

# Validando se o e-mail pode receber mensagens
try:
    validar_email_dns("usuario@exemplo.com")
    print("E-mail com domínio válido.")
except ValidationError as e:
    print(f"Erro: {e}")
```

---

## Testes

Para rodar os testes e garantir que a biblioteca está funcionando corretamente, execute:

```bash
python -m unittest discover -s test
```

Isso rodará todos os testes da biblioteca, garantindo que as validações de senha e e-mail estão funcionando conforme o esperado.

---

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature-minha-melhoria`).
3. Faça suas alterações e commit (`git commit -am 'Minha melhoria'`).
4. Envie para o branch (`git push origin feature-minha-melhoria`).
5. Crie um Pull Request.

---

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
