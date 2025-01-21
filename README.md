# Automação de Pesquisa no YouTube com Selenium

Este projeto utiliza a biblioteca [Selenium](https://www.selenium.dev/) para realizar pesquisas automatizadas no YouTube, permitindo ao usuário selecionar e assistir a vídeos diretamente a partir do terminal.

## 📋 Funcionalidades

- Realiza pesquisas no YouTube com base em palavras-chave fornecidas pelo usuário.
- Lista os vídeos encontrados e permite ao usuário escolher qual assistir.
- Automatiza ações como seleção de vídeo e entrada em tela cheia.
- Configuração personalizada do navegador para melhorar a compatibilidade.

## 🛠️ Requisitos

### Hardware Necessário
- **Sistema Operacional**: Windows, macOS ou Linux.
- **Processador**: Dual-core ou superior.
- **Memória RAM**: Pelo menos 4 GB (recomendado 8 GB ou mais).
- **Espaço em Disco**: 500 MB livres para instalação do navegador Chrome e dependências.

### Software Necessário

1. **Python 3.7 ou superior**
   - Baixe e instale o Python a partir do [site oficial](https://www.python.org/downloads/).
2. **Google Chrome**
   - Baixe e instale o navegador Google Chrome a partir do [site oficial](https://www.google.com/chrome/).
3. **ChromeDriver compatível**
   - Faça o download da versão do ChromeDriver compatível com a sua versão do Chrome em [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
4. **Pacotes Python**:
   - Instale os pacotes necessários executando o seguinte comando no terminal:
     ```bash
     pip install selenium pygetwindow pyautogui
     ```

## 📂 Estrutura do Projeto

- `index.py`: Script principal contendo o código de automação.
- `chromedriver.exe`: Arquivo necessário para controlar o navegador Chrome.

## 🚀 Como Executar

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um Ambiente Virtual (.venv)**
   - No terminal, execute o seguinte comando para criar um ambiente virtual:
     ```bash
     python -m venv .venv
     ```
   - Ative o ambiente virtual:
     - **Windows**: `source .venv\Scripts\activate`
     - **macOS/Linux**: `source .venv/bin/activate`

3. **Configure o Caminho do ChromeDriver**
   - Verifique o caminho correto do arquivo `chromedriver.exe` em sua máquina.
   - Atualize a variável `caminho` no script `index.py`:
     ```python
     caminho = "./chromedriver-win64/chromedriver.exe"
     ```

4. **Execute o Script**
   - No terminal, execute:
     ```bash
     python index.py
     ```

5. **Siga as Instruções no Terminal**
   - Insira "sim" para iniciar o processo.
   - Digite a palavra-chave da pesquisa desejada no YouTube.
   - Escolha o vídeo desejado a partir da lista apresentada.

## ⚠️ Observações Importantes

- **Segurança**: Este script foi desenvolvido para aprendizado e não deve ser usado para propósitos maliciosos.
- **Restrições do YouTube**: Alterações no site do YouTube podem afetar a funcionalidade do script. Atualize-o conforme necessário.
- **Compatibilidade**: Certifique-se de que a versão do ChromeDriver seja compatível com sua versão do Google Chrome.

## 📄 Licença
Este projeto está licenciado sob a [MIT License](LICENSE). Sinta-se à vontade para usar, modificar e distribuir.

---

### 💡 Dúvidas?
Se tiver alguma dúvida ou problema, entre em contato ou abra uma issue no repositório!
