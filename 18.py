def senha_segura(senha):
    if (len(senha) >= 8 and
        any(c.isupper() for c in senha) and
        any(c.islower() for c in senha) and
        any(c.isdigit() for c in senha)):
        return True
    return False
print(senha_segura("Senha123"))
print(senha_segura("fraca"))
