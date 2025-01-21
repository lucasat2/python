# Crie uma função chamada criar_email que recebe nome, sobrenome e dominio (com valor padrão "empresa.com.br") e retorna um email no formato "nome.sobrenome@dominio".


def criar_email(nome, sobrenome, dominio="empresa.com.br"):
    email = f"{nome.lower()}.{sobrenome.lower()}@{dominio}"
    return email

email = criar_email("Lucas", "Ataide")
print(email)  

email_personalizado = criar_email("Lucas", "Ataide", "exemplo.com")
print(email_personalizado)
