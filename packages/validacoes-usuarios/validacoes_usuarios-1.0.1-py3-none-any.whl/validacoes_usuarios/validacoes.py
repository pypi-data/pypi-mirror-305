import re
from wtforms import ValidationError
import dns.resolver
from .config import dominios_temporarios

def validar_senha(senha, username=None, email=None):
    """
    Valida a segurança da senha de acordo com critérios específicos, incluindo
    letras maiúsculas, minúsculas, números e caracteres especiais.

    Parâmetros:
    - senha (str): A senha que será validada.
    - username (str, opcional): Nome de usuário para evitar sua presença na senha.
    - email (str, opcional): E-mail do usuário para evitar partes dele na senha.

    Levanta:
    - ValidationError: Se a senha não atender a um ou mais critérios de segurança.
    """
    # Verificar se a senha contém ao menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        raise ValidationError('A senha deve conter pelo menos uma letra maiúscula.')

    # Verificar se a senha contém ao menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        raise ValidationError('A senha deve conter pelo menos uma letra minúscula.')

    # Verificar se a senha contém ao menos um número
    if not re.search(r'[0-9]', senha):
        raise ValidationError('A senha deve conter pelo menos um número.')

    # Verificar se a senha contém ao menos um caractere especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        raise ValidationError('A senha deve conter pelo menos um caractere especial (!@#$%^&* etc.).')

    # Verificar se a senha não é uma senha comum e insegura
    senhas_comuns = ['password', '123456', 'senha123', 'admin', '12345678']
    if senha.lower() in senhas_comuns:
        raise ValidationError('Esta senha é muito comum, escolha uma senha mais segura.')

    # Evitar que a senha contenha o nome de usuário
    if username and username.lower() in senha.lower():
        raise ValidationError('A senha não deve conter seu nome de usuário.')

    # Evitar que a senha contenha partes do e-mail
    if email and email.split('@')[0].lower() in senha.lower():
        raise ValidationError('A senha não deve conter partes do seu e-mail.')

def validar_email_temporario(email):
    """
    Verifica se o e-mail pertence a um domínio temporário proibido.

    Parâmetros:
    - email (str): O e-mail a ser verificado.

    Levanta:
    - ValidationError: Se o e-mail pertence a um domínio de e-mail temporário.
    """
    dominio = email.data.split('@')[1]
    if dominio in dominios_temporarios:
        raise ValidationError('E-mails de domínios temporários não são permitidos. Use um e-mail válido.')

def validar_email_dns(email):
    """
    Verifica se o domínio do e-mail possui registros MX válidos, indicando que
    ele pode receber e-mails.

    Parâmetros:
    - email (str): O e-mail a ser verificado.

    Levanta:
    - ValidationError: Se o domínio do e-mail não possui registros MX válidos ou
      se ocorre um erro de verificação DNS.
    """
    dominio = email.data.split('@')[1]
    try:
        # Tenta resolver o registro MX para o domínio do e-mail
        dns.resolver.resolve(dominio, 'MX')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        raise ValidationError(f'O domínio {dominio} não pode receber e-mails.')
    except dns.exception.DNSException:
        raise ValidationError('Erro ao verificar o domínio. Tente novamente mais tarde.')
