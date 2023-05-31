caracteres = "AcaRQoYjlSlByityzQhvjnCNVpsaLeQPtGajQHVzbgabJuAiMHDxwfkcCwIGmZCTInlSiKvRKxAGzJsgmPeUBAReDamLzqgJgrXobzfoWiwvRPdFgJzIkSoJscWtVdEbuIRYhXOdHkayBdFIbHSyzIJtmGMhJTiFBaDIzrngCngdSnngUHFWpQpCwElHxunYWsiXKvFOkntcAHiXopTgIKkeovoLrBlPTtMfqTTAgrejUPgKeBsolCtAAjNtKBjfcAHiXopTgIKkeovoLrBlPTtMfqTTAgrejUPgKeBsolCtAAjNtKBjfcAHiXopTgIKkeovoLrBlPTtMfqTTAgrejUPgKeBsolCtAAjNtKBjfcAHiXopTgIKkeoviLrBlPTtMfqTTAgrejUPgKeBsolCtAAjNtKBjfcAHiXopTgIKkeovoLrBlPTtMfqTTAgrejUPgKeBsolCtAAjNtKBjfcAHiXopTgIKkeovoLrBlPTtMfqTTAgrejUPgKeBsolCtAAjNtKBjfcAHiXopTgIKkeovoLrBlPTtMfqTTAgrejUPgKeBsolCtAAjNtKBjfcAHiXopTgIlkeovoLrBlPTtMfqTTlgrejUPgleBsolCtAAjNtKBjfcAHiXopTgIKkeovoLrBlPTtMfqTTAgrejUPgKeBsolCtAAjNtKBjfcAHiXopTgIKkeovoLrBlPTtMfqTTAgrejUPgKeBsolCtAAjNtKBjf"
prefixoEmail = ""
def fibonacci(n): # estrutura de repetição para achar as sequencias dos numeros fibonacci
    a, b = 0, 1
    fibSeq = []
    while len(fibSeq) < n:
        fibSeq.append(b)
        a, b = b, a + b
    return fibSeq

fibSeq = fibonacci(15) # chamo a função e retorno o resultado para o array fibSeq 

for i in fibSeq[1:]: # Encontro os caracteres corretos atraves dos valores de fibSeq e transformo em caixa baixa
    if i < len(caracteres):
        prefixoEmail += caracteres[i].lower()

prt1 = prefixoEmail[:8]
prt2 = prefixoEmail[8:14]

emailCompleto = prt1 + "." + prt2

print(fibSeq)

print(emailCompleto + "@tesis.com.br")