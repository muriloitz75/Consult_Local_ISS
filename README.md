# Busca Assertiva ISS - LC 116/2003

Aplicação web para consulta rápida e precisa sobre o local de recolhimento do ISS baseada na Lei Complementar 116/2003.

## 📋 Sobre o Projeto

Esta aplicação foi desenvolvida para reduzir em 95% o tempo necessário para consultas sobre o local de recolhimento do ISS, eliminando o processo manual demorado e sujeito a erros na interpretação da LC 116/2003.

### Funcionalidades

- ✅ Consulta assertiva do local de recolhimento do ISS
- ✅ Interface moderna e intuitiva
- ✅ Validação automática de campos obrigatórios
- ✅ Resultado com base legal fundamentada
- ✅ Design responsivo para desktop e mobile

## 🚀 Tecnologias Utilizadas

- **Backend**: Python 3.8+ com Flask
- **Banco de Dados**: MySQL (SQLite para desenvolvimento)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Arquitetura**: Monolítica

## 📁 Estrutura do Projeto

```
buscafacil-iss/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   ├── templates/
│   │   └── index.html
│   ├── engine/
│   │   └── __init__.py      # Motor de busca principal
│   ├── models/
│   │   └── __init__.py      # Modelos do banco de dados
│   ├── routes.py            # Rotas da aplicação
│   └── __init__.py          # Inicializador da aplicação
├── tests/                   # Testes unitários
├── Docs/                    # Documentação do projeto
│   ├── prd.md              # Product Requirements Document
│   └── architecture.md     # Documento de Arquitetura
├── requirements.txt         # Dependências Python
├── config.py               # Configurações
├── run.py                  # Ponto de entrada
├── init_db.py              # Script de inicialização do BD
├── .env.example            # Exemplo de variáveis de ambiente
└── README.md               # Este arquivo
```

## 🛠️ Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- MySQL (ou SQLite para desenvolvimento)
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd Consult_local_ISS
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**
   ```bash
   # Copie o arquivo de exemplo
   copy .env.example .env
   
   # Edite o arquivo .env com suas configurações
   ```

5. **Inicialize o banco de dados**
   ```bash
   python init_db.py
   ```

6. **Execute a aplicação**
   ```bash
   python run.py
   ```

7. **Acesse a aplicação**
   - Abra seu navegador em: `http://localhost:5000`

## 🗄️ Configuração do Banco de Dados

### Para Desenvolvimento (SQLite)
```env
DATABASE_URL=sqlite:///iss_database.db
```

### Para Produção (MySQL)
```env
DATABASE_URL=mysql+pymysql://usuario:senha@localhost/iss_database
```

## 📊 Estrutura do Banco de Dados

### Tabela `servicos`
- `id`: Chave primária
- `codigo`: Código do serviço (ex: "1.01")
- `descricao`: Descrição completa do serviço

### Tabela `regras`
- `id`: Chave primária
- `servico_id`: Referência ao serviço
- `local_recolhimento`: Local onde deve ser recolhido o ISS
- `justificativa_legal`: Base legal da regra

## 🧪 Testes

```bash
# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=app

# Executar testes específicos
pytest tests/test_engine.py
```

## 📝 Como Usar

1. **Selecione o Serviço**: Escolha o serviço da lista baseada na LC 116/2003
2. **Preencha os Municípios**: 
   - Município do Prestador
   - Município do Tomador
   - Município da Execução
3. **Clique em "Analisar"**: O sistema processará a consulta
4. **Visualize o Resultado**: Uma janela modal exibirá:
   - Local correto de recolhimento
   - Base legal da decisão
   - Detalhes da consulta

## 🔧 Desenvolvimento

### Adicionando Novos Serviços

1. Edite o arquivo `init_db.py`
2. Adicione o novo serviço na lista `servicos_exemplo`
3. Se necessário, adicione regras específicas em `regras_exemplo`
4. Execute: `python init_db.py`

### Estrutura de Regras

As regras seguem o Art. 3º da LC 116/2003:
- **Regra Geral**: Local do estabelecimento prestador
- **Exceções**: Definidas na tabela `regras` para casos específicos

## 🚀 Deploy

### Hostgator (Produção)

1. Configure as variáveis de ambiente no painel
2. Faça upload dos arquivos via FTP
3. Configure o banco MySQL
4. Execute o script de inicialização

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para dúvidas ou suporte, consulte a documentação em `/Docs/` ou abra uma issue no repositório.

---

**Desenvolvido com ❤️ para simplificar consultas de ISS**