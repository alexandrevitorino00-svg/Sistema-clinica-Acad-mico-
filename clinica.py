from collections import deque

pacientes = []
fila_atendimento = deque()


def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")
    nome = input("Nome do paciente: ").strip()
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Erro: idade inválida.")
        return
    telefone = input("Telefone: ").strip()

    paciente = {"nome": nome, "idade": idade, "telefone": telefone}
    pacientes.append(paciente)
    print("✅ Paciente cadastrado com sucesso!")


def ver_estatisticas():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    total = len(pacientes)
    idades = [p["idade"] for p in pacientes]
    media = sum(idades) / total
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])

    print("\n--- Estatísticas ---")
    print(f"Total de pacientes: {total}")
    print(f"Idade média: {media:.1f}")
    print(
        f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(
        f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")


def buscar_paciente():
    nome = input("Digite o nome para buscar: ").strip().lower()
    encontrados = [p for p in pacientes if p["nome"].lower() == nome]

    if encontrados:
        for p in encontrados:
            print(
                f"Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")
    else:
        print("Paciente não encontrado.")


def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    print("\n--- Lista de Pacientes ---")
    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. {p['nome']} - {p['idade']} anos - {p['telefone']}")


def verificar_atendimento():
    print("\n--- Verificação de Atendimento ---")
    tipo = input(
        "Tipo de atendimento (1-Consulta Normal / 2-Emergência): ").strip()

    A = input("Tem agendamento (s/n)? ").lower() == 's'
    B = input("Documentos OK (s/n)? ").lower() == 's'
    C = input("Médico disponível (s/n)? ").lower() == 's'
    D = input("Pagamentos em dia (s/n)? ").lower() == 's'

    if tipo == "1":
        consulta_normal = (A and B and C) or (B and C and D)
        print("✅ Atendimento liberado." if consulta_normal else "❌ Atendimento negado.")
    elif tipo == "2":
        emergencia = C and (B or D)
        print("✅ Atendimento liberado." if emergencia else "❌ Atendimento negado.")
    else:
        print("Tipo inválido.")


def gerenciar_fila():
    print("\n--- Gerenciamento de Fila de Atendimento ---")

    for i in range(3):
        nome = input(f"Nome do paciente {i+1}: ").strip()
        cpf = input(f"CPF do paciente {i+1}: ").strip()
        fila_atendimento.append({"nome": nome, "cpf": cpf})

    print("\n📋 Fila formada:")
    for p in fila_atendimento:
        print(f"- {p['nome']} (CPF: {p['cpf']})")

    if fila_atendimento:
        atendido = fila_atendimento.popleft()
        print(
            f"\n➡️ Paciente atendido: {atendido['nome']} (CPF: {atendido['cpf']})")

    if fila_atendimento:
        print("\n👥 Pacientes ainda aguardando:")
        for p in fila_atendimento:
            print(f"- {p['nome']} (CPF: {p['cpf']})")
    else:
        print("\n✅ Nenhum paciente aguardando na fila.")


def menu():
    while True:
        print("\n=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Verificação de atendimento")
        print("6. Gerenciar fila de atendimento")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            ver_estatisticas()
        elif opcao == "3":
            buscar_paciente()
        elif opcao == "4":
            listar_pacientes()
        elif opcao == "5":
            verificar_atendimento()
        elif opcao == "6":
            gerenciar_fila()
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
