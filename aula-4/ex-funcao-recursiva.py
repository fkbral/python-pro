# Na sequência de fibonacci é dado 0 e 1 como primeiros termos da sequência
# e todos os demais termos são calculados em base destes primeiros, somando
# os termos anteriores

def fibonacci(termo):
    if termo == 0:
        return 0
    if termo == 1:
        return 1

    return fibonacci(termo - 1) + fibonacci(termo - 2)


resultado = fibonacci(3)

print(resultado)
