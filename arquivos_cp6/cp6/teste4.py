from pathlib import Path
import json

PROXIMO = {
    "novo": "contato",
    "contato": "proposta",
    "proposta": "ganho",
    "ganho": "ganho"
}


class CRM:
    def __init__(self, arquivo):
        self.arquivo = Path(arquivo)
        self.leads = self.carregar()

    def carregar(self):
        if not self.arquivo.exists():
            return []
        try:
            return json.loads(self.arquivo.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def salvar(self):
        texto = json.dumps(self.leads, ensure_ascii=False, indent=2)
        self.arquivo.write_text(texto, encoding="utf-8")

    def avancar_stage(self, email):
        # Percorre self.leads (como na opção 1) para que self.salvar() funcione
        for lead in self.leads:
            # Compara ambos em minúsculo (como na opção 4) para achar o e-mail maiúsculo
            if lead["email"].lower() == email.lower():
                lead["stage"] = PROXIMO[lead["stage"]]
                self.salvar()
                return lead["stage"]
                
        return None
        pass

    


crm = CRM("leads.json")
print(crm.avancar_stage("BRUNO@goodwe.com"))

# simulando o programa sendo fechado e aberto novamente
crm_reaberto = CRM("leads.json")
print(crm_reaberto.leads[1]["stage"])
