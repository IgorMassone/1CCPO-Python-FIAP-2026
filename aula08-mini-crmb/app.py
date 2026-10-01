from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    company = input("Empresa: ")
    stage = input("Etapa de vendas: ")

    # verifique e valide os campos
    # depois dos campos validados, preciso modelar os dados
    # os leads serão estruturados como dict
    print(model_lead(name, email, company, stage))

    # com os dados modelados, preciso enviá-los para o DB
    # para isso, vamos usar os métodos criados no control
    control.create_lead(model_lead(name, email, company, stage))

    print("Lead adicionado (func)")

def list_leads():

    leads = control.read_leads()

    print(f"## | {"Nome":<10} | {"E-mail":<10} | Empresa")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]:<10} | {lead["company"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()
    if not query:
        print("Consulta vazia")
        return

    # vou agora enviar a busca do usuário (query) para o control
    # o control vai comparar a busca com a base de dados
    # e vai retornar uma lista com o resultado

    leads_found = control.read_leads_search(query)
    print(f"## | {"Nome":<10} | {"E-mail":<10} | Empresa")
    for i, lead in leads_found:
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]:<10} | {lead["company"]}")

def export_lead():

    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possível exportar os leads")
    else:
        print(f"Exportado para {path_csv}")

def update_lead():
    leads = control.read_leads()
    list_leads()
    index = input("Número (##) do lead a atualizar: ").strip()
    if not index.isdigit() or int(index) >= len(leads):
        print("Número inválido")
        return
    index = int(index)

    atual = leads[index]
    print("Enter em branco = manter o valor atual")
    name = input(f"Nome [{atual['name']}]: ") or atual["name"]
    email = input(f"E-mail [{atual['email']}]: ") or atual["email"]
    company = input(f"Empresa [{atual['company']}]: ") or atual["company"]
    stage = input(f"Etapa [{atual['stage']}]: ") or atual["stage"]

    control.update_lead(index, {"name": name, "email": email, "company": company, "stage": stage})
    print("Lead atualizado")

def delete_lead():
    leads = control.read_leads()
    list_leads()
    index = input("Número (##) do lead a remover: ").strip()
    if not index.isdigit() or int(index) >= len(leads):
        print("Número inválido")
        return
    index = int(index)

    if input(f"Remover {leads[index]['name']}? (s/n): ").strip().lower() != "s":
        print("Cancelado")
        return

    control.delete_lead(index)
    print("Lead removido")

def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar nome, email, empresa")
        print("[4] Exportar CSV")
        print("[5] Atualizar lead")
        print("[6] Remover lead")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_lead()
        elif opt == "5":
            update_lead()
        elif opt == "6":
            delete_lead()
        elif opt == "0":
            print("Até mais..")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Erro: {e}")