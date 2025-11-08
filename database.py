import sqlite3

class DatabaseConnection:
    def __init__(self, dbPath: str = 'cbjj.db'):
        self.dbPath = dbPath
        self.conn = None

    def conectar(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.dbPath, isolation_level=None)
            self.conn.row_factory = sqlite3.Row
            self.conn.execute("PRAGMA foreign_keys = ON")
        return self.conn

    def fechar(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def cursor(self):
        if self.conn is None:
            self.conectar()
        return self.conn.cursor()

    def criar_tabelas(self):
        cur = self.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS categoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS escola (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nome_fantasia TEXT,
            cnpj TEXT UNIQUE NOT NULL,
            endereco TEXT,
            telefone TEXT,
            email TEXT,
            responsavel TEXT,
            cidade TEXT,
            estado TEXT
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS atleta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            idade INTEGER CHECK (idade >= 0 AND idade <= 120),
            categoria_idade TEXT,
            altura REAL,
            peso REAL,
            data_nascimento TEXT,
            ativo INTEGER DEFAULT 1,
            observacoes TEXT,
            telefone TEXT,
            cad_unico INTEGER DEFAULT 0,
            escola_id INTEGER NOT NULL,
            categoria_id INTEGER NOT NULL,
            momento_cadastro TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (categoria_id) REFERENCES categoria(id),
            FOREIGN KEY (escola_id) REFERENCES escola(id)
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS podio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            atleta_id INTEGER NOT NULL,
            colocacao INTEGER CHECK (colocacao >= 1 AND colocacao <= 3),
            evento TEXT NOT NULL,
            data_evento TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (atleta_id) REFERENCES atleta(id)
        );
        """)