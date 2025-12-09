# Aqui vão desafios práticos, progressivos e realistas para você evoluir seu projeto orientado a objetos + SQLAlchemy dentro do
# contexto de um sistema bancário.
# Cada desafio é pensado para treinar classes, métodos, relacionamentos, validações, transações, consultas mais avançadas e
# regras de negócio reais.

# DESAFIO — Criar novos tipos de conta
  # Sugestões de classes:
  # ContaCorrente(Conta)
  # ContaPoupanca(Conta)
  # ContaInvestimento(Conta)

      # Regras sugeridas:
        # ContaPoupança não permite mais de 3 saques/dia.
        # ContaCorrente permite limite especial (cheque especial).
        # ContaInvestimento aplica rentabilidade diária.

# Conceitos usados:
  # Herança
  # Polimorfismo
  # Métodos sobrescritos
  # Validação dentro das entidades

# FASE 1 — Fundamentos e Modelagem:
   # Estrutura inicial
   # Criar as entidades principais:
      # Usuario
      # Contas (abstrata)
      # Endereco
      # HistoricoOperacao

# Além disso, deverá Segurança e Login
# Objetivo: Adicionar autenticação, Hash de senha com bcrypt e Verificação (Usuário acessa apenas suas contas)

# Deverá ter Relatórios (CSV ou PDF) para gerar arquivos com : Extrato detalhado , Ranking, Movimentação mensal
# Poderá usar pandas, reportlab, csv, xlsx.

# Desafio Final (Sistema Completo)
# Montar uma mini API bancária usando:
# FastAPI,SQLAlchemy, Rotas:
#/login
#/depositar
#/sacar
#/transferir
#/criar_conta
#/extrato

# Aí você terá um sistema bancário OO+SQLAlchemy completamente funcional.


                  
      
