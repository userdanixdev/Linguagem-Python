# TESTE — depósitos e saques (regras básicas)
def test_depositar_sacar():
    from src.models import ContaCorrente
    cc = ContaCorrente(saldo = 100, limite_especial = 300)
    cc.depositar (50)
    assert saldo == 150

    cc.sacar(100)
    assert saldo == 50

    