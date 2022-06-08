from decimal import Decimal

compra = Decimal(float(input("Informe o valor da compra: ")))
pagamento = Decimal(float(input("Informe o valor pago: ")))
troco = Decimal(float(pagamento - compra))
if (compra == pagamento):
    print("Pagamento efetuado.")
elif (compra < pagamento):
    print("O valor a ser devolvido: R$ {:.2f}".format(troco))
valor = Decimal(float(troco))
while valor > 1000:
    valor = Decimal(input())
dinheiro = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
for i in dinheiro:
    quantidade = float(valor) // i
    if quantidade > 0:
        print("{:.0f} Nota(s)/Moeda(S) de R$ {:.2f}.".format(quantidade, i))
        valor -= Decimal(float(quantidade * i))
