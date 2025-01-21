# Crie uma função chamada criar_email que recebe nome, sobrenome e dominio (com valor padrão "empresa.com.br") e retorna um email no formato "nome.sobrenome@dominio".


def criar_email(nome, sobrenome, dominio="empresa.com.br"):
    email = f"{nome.lower()}.{sobrenome.lower()}@{dominio}"
    return email



# Exemplo de uso da função
email = criar_email("Lucas", "Ataide")
print(email)  # Saída: lucas.ataide@empresa.com.br

email_personalizado = criar_email("Lucas", "Ataide", "exemplo.com")
print(email_personalizado)  # Saída: lucas.ataide@exemplo.com