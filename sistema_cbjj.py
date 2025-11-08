from database import DatabaseConnection
from models import Categoria, Escola, Atleta, Podio

class SistemaCBJJ:
    def __init__(self):
        self.db = DatabaseConnection()
        self.db.conectar()
        self.db.criar_tabelas()

    def definir_categoria_idade(self, idade: int) -> str:
        if idade <= 5:
            return "Pré-Mirim"
        elif idade <= 7:
            return "Mirim"
        elif idade <= 9:
            return "Infantil A"
        elif idade <= 11:
            return "Infantil B"
        elif idade <= 13:
            return "Infanto A"
        elif idade <= 15:
            return "Infanto B"
        elif idade <= 17:
            return "Juvenil"
        elif idade <= 29:
            return "Adulto"
        elif idade <= 35:
            return "Master 1"
        elif idade <= 40:
            return "Master 2"
        elif idade <= 45:
            return "Master 3"
        elif idade <= 50:
            return "Master 4"
        elif idade <= 55:
            return "Master 5"
        else:
            return "Master 6+"

    def cadastrar_escola(self, escola: Escola):
        cur = self.db.cursor()
        cur.execute("""
            INSERT INTO escola (nome, nome_fantasia, cnpj, endereco, telefone, email, responsavel, cidade, estado)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (escola.nome, escola.nome_fantasia, escola.cnpj, escola.endereco,
              escola.telefone, escola.email, escola.responsavel, escola.cidade, escola.estado))
        print(f"✅ Escola '{escola.nome_fantasia or escola.nome}' cadastrada!")

    def listar_escolas(self):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM escola")
        return cur.fetchall()

    def cadastrar_categoria(self, categoria: Categoria):
        cur = self.db.cursor()
        cur.execute("INSERT INTO categoria (nome) VALUES (?)", (categoria.nome,))
        print(f"✅ Categoria '{categoria.nome}' cadastrada!")

    def listar_categorias(self):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM categoria")
        return cur.fetchall()

    def cadastrar_atleta(self, atleta: Atleta):
        cur = self.db.cursor()
        cur.execute("""
            INSERT INTO atleta (nome, email, idade, categoria_idade, altura, peso, data_nascimento, telefone, observacoes, cad_unico, escola_id, categoria_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (atleta.nome, atleta.email, atleta.idade, atleta.categoria_idade, atleta.altura,
              atleta.peso, atleta.data_nascimento, atleta.telefone, atleta.observacoes,
              atleta.cad_unico, atleta.escola_id, atleta.categoria_id))
        print(f"✅ Atleta '{atleta.nome}' cadastrado!")

    def listar_atletas(self):
        cur = self.db.cursor()
        cur.execute("""
            SELECT a.id, a.nome, a.idade, a.categoria_idade, a.peso, c.nome AS categoria, e.nome_fantasia AS escola
            FROM atleta a
            JOIN categoria c ON a.categoria_id = c.id
            JOIN escola e ON a.escola_id = e.id
        """)
        return cur.fetchall()
        # ---------------- LISTAR PARTICIPANTES ----------------
    def listar_participantes(self):
        """Lista todos os atletas participantes com informações detalhadas."""
        cur = self.db.cursor()
        cur.execute("""
            SELECT a.id, a.nome, a.idade, a.categoria_idade, a.peso, a.altura, 
                   a.cad_unico, c.nome AS categoria, e.nome_fantasia AS escola
            FROM atleta a
            JOIN categoria c ON a.categoria_id = c.id
            JOIN escola e ON a.escola_id = e.id
            ORDER BY a.nome ASC
        """)
        participantes = cur.fetchall()

        print("\n👥 PARTICIPANTES CADASTRADOS:")
        if not participantes:
            print("Nenhum atleta cadastrado ainda.")
            return

        for p in participantes:
            cad_status = "Isento (CadÚnico)" if p["cad_unico"] == 1 else "Normal"
            print(f"""
🧍 ID: {p['id']}
    Nome: {p['nome']}
    Idade: {p['idade']} anos
    Categoria CBJJ: {p['categoria_idade']}
    Categoria Inscrição: {p['categoria']}
    Peso: {p['peso']} kg | Altura: {p['altura']} m
    Escola: {p['escola']}
    Tipo de Inscrição: {cad_status}
""")


    def cadastrar_podio(self, podio: Podio):
        cur = self.db.cursor()
        cur.execute("INSERT INTO podio (atleta_id, colocacao, evento) VALUES (?, ?, ?)",
                    (podio.atleta_id, podio.colocacao, podio.evento))
        print(f"🏆 Pódio cadastrado para atleta ID {podio.atleta_id} - {podio.colocacao}º lugar!")

    def listar_podios(self):
        cur = self.db.cursor()
        cur.execute("""
            SELECT p.id, a.nome AS atleta, p.colocacao, p.evento, p.data_evento
            FROM podio p
            JOIN atleta a ON p.atleta_id = a.id
        """)
        return cur.fetchall()

    # ---------------- EXIBIR TABELAS ----------------
    def mostrar_tabelas(self):
        """Mostra todas as tabelas e suas colunas no banco de dados."""
        cur = self.db.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabelas = cur.fetchall()

        print("\n📘 Tabelas existentes no banco de dados:")
        for t in tabelas:
            nome_tabela = t["name"]
            print(f"\n📂 {nome_tabela.upper()}")
            cur.execute(f"PRAGMA table_info({nome_tabela})")
            colunas = cur.fetchall()
            for c in colunas:
                print(f"  - {c['name']} ({c['type']})")
