from sistema_cbjj import SistemaCBJJ
from models import Categoria, Escola, Atleta, Podio

def main():
    sistema = SistemaCBJJ()

    while True:
        print("\n===== SISTEMA CBJJ - CAMPEONATO JIU-JITSU =====")
        print("1. Cadastrar Escola")
        print("2. Cadastrar Categoria")
        print("3. Cadastrar Atleta")
        print("4. Cadastrar Pódio")
        print("5. Listar Escolas")
        print("6. Listar Categorias")
        print("7. Listar Atletas")
        print("8. Listar Pódios")
        print("9. Mostrar Tabelas do Banco de Dados")
        print("10. listar participantes")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            e = Escola(
                input("Nome: "),
                input("Nome fantasia: "),
                input("CNPJ: "),
                input("Endereço: "),
                input("Telefone: "),
                input("Email: "),
                input("Responsável: "),
                input("Cidade: "),
                input("Estado: ")
            )
            sistema.cadastrar_escola(e)

        elif opcao == "2":
            c = Categoria(input("Nome da categoria: "))
            sistema.cadastrar_categoria(c)

        elif opcao == "3":
            nome = input("Nome: ")
            email = input("Email: ")
            idade = int(input("Idade: "))
            categoria_idade = sistema.definir_categoria_idade(idade)
            print(f"🎯 Categoria CBJJ: {categoria_idade}")
            altura = float(input("Altura: "))
            peso = float(input("Peso: "))
            data_nasc = input("Data de nascimento (AAAA-MM-DD): ")
            telefone = input("Telefone: ")
            observacoes = input("Observações: ")
            cad_unico = 1 if input("Possui CadÚnico? (s/n): ").lower() == "s" else 0

            print("\n--- Escolas ---")
            for e in sistema.listar_escolas():
                print(f"{e['id']} - {e['nome_fantasia'] or e['nome']}")
            escola_id = int(input("Escolha ID da escola: "))

            print("\n--- Categorias ---")
            for c in sistema.listar_categorias():
                print(f"{c['id']} - {c['nome']}")
            categoria_id = int(input("Escolha ID da categoria: "))

            atleta = Atleta(nome, email, idade, altura, peso, data_nasc, telefone,
                            observacoes, cad_unico, escola_id, categoria_id, categoria_idade)
            sistema.cadastrar_atleta(atleta)

        elif opcao == "4":
            print("\n--- Atletas ---")
            for a in sistema.listar_atletas():
                print(f"{a['id']} - {a['nome']}")
            atleta_id = int(input("ID do atleta: "))
            colocacao = int(input("Colocação (1-3): "))
            evento = input("Evento: ")
            p = Podio(atleta_id, colocacao, evento)
            sistema.cadastrar_podio(p)

        elif opcao == "5":
            for e in sistema.listar_escolas():
                print(f"{e['id']} | {e['nome_fantasia'] or e['nome']} | {e['cidade']}/{e['estado']}")

        elif opcao == "6":
            for c in sistema.listar_categorias():
                print(f"{c['id']} | {c['nome']}")

        elif opcao == "7":
            for a in sistema.listar_atletas():
                print(f"{a['id']} | {a['nome']} | {a['categoria_idade']} | {a['categoria']} | {a['escola']}")

        elif opcao == "8":
            for p in sistema.listar_podios():
                print(f"{p['evento']} | {p['atleta']} - {p['colocacao']}º | {p['data_evento']}")

        elif opcao == "9":
            sistema.mostrar_tabelas()

        elif opcao == "10":
            sistema.listar_participantes()
            
            break
        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    main()
