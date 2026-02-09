from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
    QLineEdit, QTextEdit, QHBoxLayout
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from funcoes import (
    cadastrar_senha, visualizar_senha,
    salvar_nova_senha, remover_arquivo_senha
)

# SVG Icons Data (Bootstrap Icons)
# Fill="white" added to ensure visibility on dark background
SVG_EYE = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="white" class="bi bi-eye-fill" viewBox="0 0 16 16">
  <path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0"/>
  <path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8m8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7"/>
</svg>"""

SVG_EYE_SLASH = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="white" class="bi bi-eye-slash-fill" viewBox="0 0 16 16">
  <path d="m10.79 12.912-1.614-1.615a3.5 3.5 0 0 1-4.474-4.474l-2.06-2.06C.938 6.278 0 8 0 8s3 5.5 8 5.5a7 7 0 0 1 2.79-.588M5.21 3.088A7 7 0 0 1 8 2.5c5 0 8 5.5 8 5.5s-.939 1.721-2.641 3.238l-2.062-2.062a3.5 3.5 0 0 0-4.474-4.474z"/>
  <path d="M5.525 7.646a2.5 2.5 0 0 0 2.829 2.829zm4.95.708-2.829-2.83a2.5 2.5 0 0 1 2.829 2.829zm3.171 6-12-12 .708-.708 12 12z"/>
</svg>"""

class GerenciadorSenhas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciador de Senhas")
        # Removed showFullScreen to allow minimize/close buttons
        self.resize(500, 650) 
        self.setStyleSheet("""
    QWidget {
        background-color: #121212;
        color: #E0E0E0;
        font-family: 'Segoe UI', 'Roboto', sans-serif;
        font-size: 15px;
    }
    QPushButton {
        background-color: #1F1F1F;
        color: #BB86FC;
        border: 1px solid #333333;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    QPushButton:hover {
        background-color: #333333;
        color: #FFFFFF;
        border: 1px solid #BB86FC;
    }
    QPushButton:pressed {
        background-color: #BB86FC;
        color: #000000;
    }
    QLineEdit {
        background-color: #1E1E1E;
        border: 1px solid #333333;
        color: #FFFFFF;
        padding: 8px 12px;
        border-radius: 8px;
        selection-background-color: #BB86FC;
    }
    QLineEdit:focus {
        border: 1px solid #BB86FC;
    }
    QTextEdit {
        background-color: #0F0F0F;
        color: #00E676; /* Modern terminal green */
        font-family: "Consolas", "Courier New", monospace;
        font-size: 13px;
        padding: 12px;
        border: 1px solid #333333;
        border-radius: 8px;
    }
    QLabel {
        color: #B0B0B0;
        font-size: 14px;
        font-weight: 500;
        margin-bottom: 2px;
    }
""")
        
        # Load icons
        self.icon_eye = self.create_icon(SVG_EYE)
        self.icon_eye_slash = self.create_icon(SVG_EYE_SLASH)

        self.init_ui()

    def create_icon(self, svg_data):
        pixmap = QPixmap()
        # QPixmap.loadFromData requires bytes
        pixmap.loadFromData(svg_data.encode('utf-8'))
        return QIcon(pixmap)

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label_nome = QLabel("Instituição:")
        self.entrada_nome = QLineEdit()

        self.label_senha = QLabel("Senha:")
        self.entrada_senha = QLineEdit()
        self.entrada_senha.setEchoMode(QLineEdit.Password)

        self.btn_toggle_senha = QPushButton()
        self.btn_toggle_senha.setIcon(self.icon_eye) # Default: Eye (click to show?) -> Actually standard is Eye Slash is hidden? 
        # Making assumption: Current text was "Monkey" (Hidden). 
        # Let's say: Default is Hidden. Icon should show "Eye" (Click to see).
        # When visible, Icon should show "Eye Slash" (Click to hide).
        self.btn_toggle_senha.setIcon(self.icon_eye) 
        self.btn_toggle_senha.setIconSize(QSize(20, 20))
        self.btn_toggle_senha.setCheckable(True)
        self.btn_toggle_senha.clicked.connect(self.toggle_senha)

        senha_layout = QHBoxLayout()
        senha_layout.addWidget(self.entrada_senha)
        senha_layout.addWidget(self.btn_toggle_senha)

        self.label_nova_senha = QLabel("Nova Senha:")
        self.entrada_nova_senha = QLineEdit()
        self.entrada_nova_senha.setEchoMode(QLineEdit.Password)

        self.btn_toggle_nova_senha = QPushButton()
        self.btn_toggle_nova_senha.setIcon(self.icon_eye)
        self.btn_toggle_nova_senha.setIconSize(QSize(20, 20))
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
                self.btn_toggle_nova_senha.setIcon(self.icon_eye)
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
            self.btn_toggle_senha.setIcon(self.icon_eye_slash)
        else:
            self.entrada_senha.setEchoMode(QLineEdit.Password)
            self.btn_toggle_senha.setIcon(self.icon_eye)

    def toggle_nova_senha(self):
        if self.btn_toggle_nova_senha.isChecked():
            self.entrada_nova_senha.setEchoMode(QLineEdit.Normal)
            self.btn_toggle_nova_senha.setIcon(self.icon_eye_slash)
        else:
            self.entrada_nova_senha.setEchoMode(QLineEdit.Password)
            self.btn_toggle_nova_senha.setIcon(self.icon_eye)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QApplication([])
    janela = GerenciadorSenhas()
    janela.show()
    app.exec_()
