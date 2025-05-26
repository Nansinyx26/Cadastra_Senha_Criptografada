from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
    QLineEdit, QTextEdit, QHBoxLayout
)
from PyQt5.QtCore import Qt
from funcoes import (
    cadastrar_senha, visualizar_senha,
    salvar_nova_senha, remover_arquivo_senha
)

class GerenciadorSenhas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciador de Senhas")
        self.showFullScreen()
        self.setStyleSheet("""
    QWidget {
        background-color: #1e1e2f;
        color: #ffffff;
        font-family: 'Segoe UI', Arial;
        font-size: 15px;
    }
    QPushButton {
        background-color: #3a3a6a;
        color: white;
        padding: 8px 16px;
        border: none;
        border-radius: 6px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    QPushButton:hover {
        background-color: #5050a5;
    }
    QLineEdit {
        background-color: #2a2a40;
        border: 1px solid #555;
        color: #ffffff;
        padding: 6px;
        border-radius: 4px;
    }
    QTextEdit {
        background-color: #121212;
        color: #00ff90;
        font-family: "Courier New", monospace;
        font-size: 13px;
        padding: 10px;
        border: 2px solid #00ff90;
        border-radius: 6px;
    }
    QLabel {
        font-family: 'Segoe UI', Arial;
        font-size: 17px;
        font-weight: bold;
        color: #dddddd;
    }
""")

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label_nome = QLabel("Instituição:")
        self.entrada_nome = QLineEdit()

        self.label_senha = QLabel("Senha:")
        self.entrada_senha = QLineEdit()
        self.entrada_senha.setEchoMode(QLineEdit.Password)

        self.btn_toggle_senha = QPushButton("🙈")
        self.btn_toggle_senha.setCheckable(True)
        self.btn_toggle_senha.clicked.connect(self.toggle_senha)

        senha_layout = QHBoxLayout()
        senha_layout.addWidget(self.entrada_senha)
        senha_layout.addWidget(self.btn_toggle_senha)

        self.label_nova_senha = QLabel("Nova Senha:")
        self.entrada_nova_senha = QLineEdit()
        self.entrada_nova_senha.setEchoMode(QLineEdit.Password)

        self.btn_toggle_nova_senha = QPushButton("🙈")
        self.btn_toggle_nova_senha.setCheckable(True)
        self.btn_toggle_nova_senha.clicked.connect(self.toggle_nova_senha)

        nova_senha_layout = QHBoxLayout()
        nova_senha_layout.addWidget(self.entrada_nova_senha)
        nova_senha_layout.addWidget(self.btn_toggle_nova_senha)

        self.label_nova_senha.hide()
        self.entrada_nova_senha.hide()
        self.btn_toggle_nova_senha.hide()

        self.btn_cadastrar = QPushButton("Cadastrar")
        self.btn_cadastrar.clicked.connect(self.handle_cadastrar)

        self.btn_visualizar = QPushButton("Visualizar")
        self.btn_visualizar.clicked.connect(self.handle_visualizar)

        self.btn_atualizar = QPushButton("Atualizar")
        self.btn_atualizar.clicked.connect(self.mostrar_campos_nova_senha)

        self.btn_salvar = QPushButton("Salvar Alterações")
        self.btn_salvar.clicked.connect(self.handle_salvar)
        self.btn_salvar.hide()

        self.btn_remover = QPushButton("Remover Senha")
        self.btn_remover.clicked.connect(self.handle_remover)

        self.btn_sair = QPushButton("Sair")
        self.btn_sair.clicked.connect(self.close)

        self.layout.addWidget(self.label_nome)
        self.layout.addWidget(self.entrada_nome)
        self.layout.addWidget(self.label_senha)
        self.layout.addLayout(senha_layout)

        botoes_layout = QHBoxLayout()
        botoes_layout.addWidget(self.btn_cadastrar)
        botoes_layout.addWidget(self.btn_visualizar)
        botoes_layout.addWidget(self.btn_atualizar)
        self.layout.addLayout(botoes_layout)

        self.layout.addWidget(self.label_nova_senha)
        self.layout.addLayout(nova_senha_layout)
        self.layout.addWidget(self.btn_salvar)
        self.layout.addWidget(self.btn_remover)
        self.layout.addWidget(self.btn_sair)

        self.caixa_terminal = QTextEdit()
        self.caixa_terminal.setReadOnly(True)
        self.layout.addWidget(self.caixa_terminal)

        self.setLayout(self.layout)

    def log_terminal(self, mensagem):
        self.caixa_terminal.append(mensagem)

    def handle_cadastrar(self):
        nome = self.entrada_nome.text()
        senha = self.entrada_senha.text()
        if nome and senha:
            msg = cadastrar_senha(nome, senha)
        else:
            msg = "[ERRO] Preencha todos os campos para cadastrar."
        self.log_terminal(msg)

    def handle_visualizar(self):
        nome = self.entrada_nome.text()
        if nome:
            try:
                msg = visualizar_senha(nome)
            except FileNotFoundError:
                msg = "[ERRO] Instituição não encontrada."
        else:
            msg = "[ERRO] Informe a instituição para visualizar."
        self.log_terminal(msg)

    def mostrar_campos_nova_senha(self):
        if self.entrada_nome.text():
            self.label_nova_senha.show()
            self.entrada_nova_senha.show()
            self.btn_toggle_nova_senha.show()
            self.btn_salvar.show()
            self.log_terminal("[INFO] Digite a nova senha e clique em 'Salvar Alterações'.")
        else:
            self.log_terminal("[ERRO] Informe a instituição para atualizar.")

    def handle_salvar(self):
        nome = self.entrada_nome.text()
        nova_senha = self.entrada_nova_senha.text()
        if nome and nova_senha:
            try:
                msg = salvar_nova_senha(nome, nova_senha)
                self.label_nova_senha.hide()
                self.entrada_nova_senha.hide()
                self.btn_toggle_nova_senha.hide()
                self.btn_salvar.hide()
                self.entrada_nova_senha.clear()
                self.btn_toggle_nova_senha.setChecked(False)
                self.entrada_nova_senha.setEchoMode(QLineEdit.Password)
                self.btn_toggle_nova_senha.setText("🙈")
            except FileNotFoundError:
                msg = "[ERRO] Instituição não encontrada."
        else:
            msg = "[ERRO] Preencha o nome e a nova senha."
        self.log_terminal(msg)

    def handle_remover(self):
        nome = self.entrada_nome.text()
        if nome:
            msg = remover_arquivo_senha(nome)
        else:
            msg = "[ERRO] Informe a instituição para remover."
        self.log_terminal(msg)

    def toggle_senha(self):
        if self.btn_toggle_senha.isChecked():
            self.entrada_senha.setEchoMode(QLineEdit.Normal)
            self.btn_toggle_senha.setText("👁️")
        else:
            self.entrada_senha.setEchoMode(QLineEdit.Password)
            self.btn_toggle_senha.setText("🙈")

    def toggle_nova_senha(self):
        if self.btn_toggle_nova_senha.isChecked():
            self.entrada_nova_senha.setEchoMode(QLineEdit.Normal)
            self.btn_toggle_nova_senha.setText("👁️")
        else:
            self.entrada_nova_senha.setEchoMode(QLineEdit.Password)
            self.btn_toggle_nova_senha.setText("🙈")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QApplication([])
    janela = GerenciadorSenhas()
    janela.show()
    app.exec_()
