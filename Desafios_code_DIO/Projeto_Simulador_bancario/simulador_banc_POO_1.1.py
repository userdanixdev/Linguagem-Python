# Simualdor Bancário Versão Orientada a Objeto 1.1
# Autor: Daniel / Data: 04/12/2025 10:50h
# Nesse versão, foi atualizado o menu. Isolado das opções.
# Foram realizadas pequenas alterações.

import re
from abc import ABC, abstractmethod
from datetime import datetime
import textwrap


# Classes do modelo (UML)

class Cliente:
    def __init__(self, endereco: dict):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta: "Conta"):
        self.contas.append(conta)

    def realizar_transacao(self, conta: "Conta", transacao: "Transacao"):
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: dict):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao: "Transacao"):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        raise NotImplementedError

    @abstractmethod
    def registrar(self, conta: "Conta"):
        raise NotImplementedError


class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: "Conta"):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)
        return sucesso


class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: "Conta"):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)
        return sucesso


class Conta:
    def __init__(self, numero: str, cliente: Cliente, agencia: str = "0001"):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()
        # Campos que a versão funcional usava:
        self.n_saques = 0
        self.transacoes = 0
        self.saques = 0
        cliente.adicionar_conta(self)

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: str):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print('\nOperação falhou. Valor informado inválido.')
            return False
        if valor > self.saldo:
            print('\nOperação falhou. Você não tem saldo.')
            return False

        self._saldo -= valor
        # atualizar campos usados na versão funcional:
        self.n_saques += 1
        self.transacoes += 1
        self.saques += 1
        print(f'\nSaque de R$ {valor:.2f} realizado com sucesso.')
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print('\nOperação falhou. Valor inválido.')
            return False
        self._saldo += valor
        self.transacoes += 1
        print(f'\nDepósito de R$ {valor:.2f} realizado com sucesso.')
        return True

    def gerar_extrato(self):
        print(f'{"+"*50}\n{"Extrato":^30}\n{"+"*50}')
        if not self.historico.transacoes:
            print('\nNão foram realizadas movimentações.\n')
        else:
            for tx in self.historico.transacoes:
                print(f"{tx['data']} - {tx['tipo']}: R$ {tx['valor']:.2f}")
                print("-"*50)
        print(f'\nSaldo:\t\tR$ {self.saldo:.2f}')
        print("-"*50)


class ContaCorrente(Conta):
    def __init__(self, numero: str, cliente: Cliente, limite: float = 500.0, limite_saques: int = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor: float) -> bool:
        numero_saques = len([t for t in self.historico.transacoes if t['tipo'] == Saque.__name__])
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print('\nOperação falhou! Valor do saque excede o limite permitido.')
            return False
        if excedeu_saques:
            print('\nOperação falhou! Número máximo de saques diários excedido.')
            return False

        return super().sacar(valor)

    def __str__(self):
        return (f"Agência: {self.agencia}\n"
                f"C/C: {self.numero}\n"
                f"Titular: {getattr(self.cliente, 'nome', '---')}")


# -------------------------
# Funções utilitárias (validações usadas no menu)
# -------------------------

def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro = 11 - (soma % 11)
    primeiro = 0 if primeiro >= 10 else primeiro

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo = 11 - (soma % 11)
    segundo = 0 if segundo >= 10 else segundo

    return cpf[-2:] == f"{primeiro}{segundo}"


# "Banco" - gerencia usuários e contas (mantém listas, mas usa classes UML)

class Banco:
    def __init__(self):
        self.usuarios: list[PessoaFisica] = []
        self.contas: list[ContaCorrente] = []

    def filtrar_usuario(self, cpf: str):
        for u in self.usuarios:
            if u.cpf == cpf:
                return u
        return None

    def criar_usuario(self) -> PessoaFisica | None:
        while True:
            cpf = input('Informe o CPF: ').strip()
            if validar_cpf(cpf):
                print('CPF válido.')
                break
            else:
                print('CPF inválido. Tente novamente.')

        if self.filtrar_usuario(cpf):
            print('\nJá existe usuário com esse CPF.')
            return None

        while True:
            nome_usuario = input('Informe o nome completo: ').strip()
            if nome_usuario.replace(' ', '').isalpha():
                nome = ' '.join([p.capitalize() for p in nome_usuario.split()])
                break
            else:
                print('Nome inválido. Informe apenas letras.')

        while True:
            data_nascimento = input('Informe a data de nascimento (d/m/aaaa): ').strip()
            padrao_data = r'^\d{1,2}/\d{1,2}/\d{4}$'
            if re.match(padrao_data, data_nascimento):
                dia, mes, ano = map(int, data_nascimento.split('/'))
                try:
                    _ = datetime(ano, mes, dia)
                    print(f'Data de nascimento válida: {data_nascimento}')
                    break
                except ValueError:
                    print('Data inválida. Informe uma data válida.')
            else:
                print('Formato inválido. Use d/m/aaaa.')

        while True:
            cidade_estado = input('Informe a cidade e o estado (Ex: São Paulo - SP): ').strip()
            padrao_cidade_estado = r'^[A-Za-zÀ-ú\s]+ - [A-Z]{2}$'
            if re.match(padrao_cidade_estado, cidade_estado):
                cidade, estado = cidade_estado.split(' - ')
                cidade = cidade.strip()
                estado = estado.strip()
                break
            else:
                print('Formato inválido. Informe no formato: Cidade - UF (Ex: São Paulo - SP)')

        while True:
            bairro = input('Informe o bairro: ').strip()
            if bairro.replace(' ', '').isalpha():
                break
            else:
                print('Bairro inválido. Informe apenas letras.')

        while True:
            rua = input('Informe a rua: ').strip()
            if rua.replace(' ', '').isalpha():
                break
            else:
                print('Rua inválida. Informe apenas letras.')

        while True:
            try:
                numero_casa = int(input('Informe o número da casa: ').strip())
                break
            except ValueError:
                print('Número de casa inválido. Informe um número inteiro.')

        endereco = {
            'cidade': cidade,
            'estado': estado,
            'bairro': bairro,
            'rua': rua,
            'numero_casa': numero_casa
        }

        novo = PessoaFisica(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(novo)
        print('\nUsuário criado com sucesso.\n')
        return novo

    def criar_conta(self) -> ContaCorrente | None:
        cpf = input('Informe o CPF do usuário para criar a conta: ').strip()
        usuario = self.filtrar_usuario(cpf)
        if not usuario:
            print('\nUsuário não encontrado. Crie o usuário antes de abrir conta.')
            return None

        # Verifica se já existe conta associada ao CPF
        for c in self.contas:
            if getattr(c.cliente, 'cpf', None) == cpf:
                print('\nJá existe uma conta associada a este CPF. Não é possível criar outra aqui.')
                return None

        numero_conta = f'{len(self.contas) + 1:06d}'
        conta = ContaCorrente(numero_conta, usuario)
        self.contas.append(conta)
        print('\nConta criada com sucesso...')
        return conta

    def verificar_conta_por_cpf(self, cpf: str) -> ContaCorrente | None:
        for conta in self.contas:
            if getattr(conta.cliente, 'cpf', None) == cpf:
                return conta
        return None

    def listar_dados(self, cpf: str):
        conta = self.verificar_conta_por_cpf(cpf)
        if not conta:
            print('\nConta não encontrada para o CPF informado.')
            return
        # Condição original: listar apenas se houver ao menos 1 transação e 1 saque
        if conta.transacoes > 0 and conta.saques > 0:
            usuario = conta.cliente
            end = usuario.endereco
            print(f"\nNome: {usuario.nome}\nCPF: {usuario.cpf}\nData de Nascimento: {usuario.data_nascimento}\n"
                  f"Cidade: {end['cidade']} - {end['estado']}\nBairro: {end['bairro']}\n"
                  f"Rua: {end['rua']}\nNúmero da casa: {end['numero_casa']}\n"
                  f"Agência: {conta.agencia}\nNúmero da conta: {conta.numero}\n")
        else:
            print('\nPara listar os dados do correntista, é necessário realizar ao menos uma transação e um saque.')

    # Funções que replicam a lógica da versão funcional, mas usando as classes:
    def realizar_deposito(self):
        cpf = input('Informe o CPF: ').strip()
        conta = self.verificar_conta_por_cpf(cpf)
        if not conta:
            print('\n❌ Nenhuma conta encontrada com esse CPF. Cadastre e crie conta antes.')
            return
        while True:
            try:
                valor = float(input('Informe o valor do depósito: ').strip())
                if valor > 0:
                    deposito = Deposito(valor)
                    deposito.registrar(conta)
                    # registrar adiciona ao histórico quando sucesso
                    if conta.historico.transacoes and conta.historico.transacoes[-1]['tipo'] == Deposito.__name__:
                        conta.historico.transacoes[-1]['data'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    break
                else:
                    print('Operação falhou! O valor informado é inválido.')
            except ValueError:
                print('Operação falhou! Por favor, insira um valor numérico válido.')

    def realizar_saque(self, limite: float, LIMITE_SAQUES: int):
        cpf = input('Informe o CPF: ').strip()
        conta = self.verificar_conta_por_cpf(cpf)
        if not conta:
            print('\nNenhuma conta encontrada para o CPF informado. Por favor crie uma conta primeiro.')
            return

        # Mensagens variadas para diferentes falhas (mantidas da versão funcional)
        mensagens_valores_invalidos = [
            'Operação falhou! O valor informado é inválido. Somente valores positivos são aceitos.',
            'Valor inválido! Tente um número maior que zero.',
            'Esse número não é aceitável para saque. Por favor, insira um valor positivo.',
            'Cuidado! Digite um valor válido para continuar a operação.'
        ]

        mensagens_saldo_insuficiente = [
            'Operação falhou! Você não tem saldo suficiente.',
            'Saldo insuficiente! Verifique seu saldo antes de tentar novamente.',
            'Você não possui fundos suficientes para essa operação.',
            'Saldo negativo detectado! Por favor, deposite fundos antes de tentar novamente.'
        ]

        mensagens_limite_excedido = [
            'Operação falhou! O valor do saque excede o limite.',
            'Limite de saque ultrapassado! Tente um valor menor.',
            'Valor acima do limite diário permitido para saques.',
            'Saque negado - ultrapassou o limite estabelecido.'
        ]

        mensagens_excede_saques = [
            'Operação falhou! Número máximo de saques diários excedido.',
            'Limite de saques diários atingido! Tente novamente amanhã.',
            'Você já realizou o número máximo de saques permitidos para hoje.',
            'Saque não autorizado - limite diário de saques alcançado.',
            'Tente amanhã, quem sabe você tenha mais sorte!'
        ]

        contador_valores_invalidos = 0
        contador_saldo_insuficiente = 0
        contador_limite_excedido = 0
        contador_excede_saques = 0

        while True:
            texto = input("Informe o valor do saque ou digite 'sair' para voltar ao MENU:  ").strip()
            if texto.lower() == 'sair':
                print('Voltando ao menu...\n\n')
                break
            try:
                valor = float(texto)
            except ValueError:
                print('Informe valores positivos e numéricos.')
                continue

            if valor <= 0:
                idx = contador_valores_invalidos % len(mensagens_valores_invalidos)
                print(mensagens_valores_invalidos[idx])
                contador_valores_invalidos += 1
                continue

            excedeu_saldo = valor > conta.saldo
            excedeu_limite = valor > limite
            excedeu_saque = conta.n_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                idx = contador_saldo_insuficiente % len(mensagens_saldo_insuficiente)
                print(mensagens_saldo_insuficiente[idx])
                contador_saldo_insuficiente += 1
                continue
            elif excedeu_limite:
                idx = contador_limite_excedido % len(mensagens_limite_excedido)
                print(mensagens_limite_excedido[idx])
                contador_limite_excedido += 1
                continue
            elif excedeu_saque:
                idx = contador_excede_saques % len(mensagens_excede_saques)
                print(mensagens_excede_saques[idx])
                contador_excede_saques += 1
                continue
            else:
                saque = Saque(valor)
                sucesso = saque.registrar(conta)
                if sucesso:
                    # já incrementado no método sacar do objeto Conta
                    # e historico adicionado no registrar de Saque
                    pass
                break

    def exibir_extrato(self):
        cpf = input('Informe o CPF: ').strip()
        conta = self.verificar_conta_por_cpf(cpf)
        if conta:
            conta.gerar_extrato()
        else:
            print('Nenhuma conta encontrada para o CPF informado.\nPor favor crie uma conta e um novo usuário.')

def menu():
    menu = """\n
================ MENU ================              
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nu]\tNovo Usuário
[nc]\tNova Conta
[q]\tSair
[ld]\tLista Correntistas\n\nDigite aqui:
"""
    return input(textwrap.dedent(menu))


def main():

    banco = Banco()
    LIMITE_SAQUES = 3
    limite_por_operacao = 500.0        
    while True:                    
        opcao = menu()

        if opcao == 'd':
            banco.realizar_deposito()

        elif opcao == 's':
            banco.realizar_saque(limite_por_operacao, LIMITE_SAQUES)

        elif opcao == 'e':
            banco.exibir_extrato()

        elif opcao == 'nu':
            banco.criar_usuario()

        elif opcao == 'nc':
            banco.criar_conta()

        elif opcao == 'ld':
            cpf = input('Informe o CPF: ').strip()
            banco.listar_dados(cpf)

        elif opcao == 'q':
            print('Encerrando o programa.')
            break
        else:
            print('Operação inválida. Selecione a opção correta.')

if __name__ == "__main__":
    main()
