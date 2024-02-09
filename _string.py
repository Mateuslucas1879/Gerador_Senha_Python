import random
import string

sybolos =string.ascii_letters
pontuacao = string.punctuation

junta_tudo = pontuacao + sybolos

print(
    ''.join(
    random.SystemRandom().choices(
        junta_tudo,
        k=8)
    )
)