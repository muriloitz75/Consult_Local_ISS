# Documento de Arquitetura: Busca Assertiva ISS (Versão 1.0 - FINAL)

> **🏗️ NOTA:** Este documento foi expandido e fragmentado em módulos específicos.
> Consulte o [README.md](README.md) para navegar pela documentação completa.
>
> **Documentos relacionados:**
> - [Arquitetura Técnica Detalhada](04-arquitetura-tecnica.md)
> - [Implantação, Testes e Segurança](05-implantacao-testes-seguranca.md)
> - [Handoffs para Equipe](07-handoffs-proximos-passos.md)

### 1. Introdução e Visão Geral
Este documento detalha a arquitetura técnica para a aplicação "Busca Assertiva ISS". O sistema foi projetado como uma **aplicação web monolítica**, seguindo as premissas estabelecidas no PRD para garantir um desenvolvimento rápido e focado no MVP.

### 2. Pilha de Tecnologias (Tech Stack)
* **Arquitetura:** Monolítica
* **Linguagem:** Python
* **Banco de Dados:** MySQL
* **Hospedagem:** Hostgator
* **Interface:** Web Responsiva

### 3. Modelo de Dados e Esquema do Banco de Dados
A lógica da aplicação será suportada por duas tabelas principais no MySQL:
* **`servicos`:** Armazenará os códigos e descrições dos serviços da lista anexa à LC 116/2003.
    * `id INT PRIMARY KEY AUTO_INCREMENT`
    * `codigo VARCHAR(10)`
    * `descricao TEXT`
* **`regras`:** Codificará as exceções do Art. 3º, vinculando um serviço a um local de recolhimento e sua justificativa legal.
    * `id INT PRIMARY KEY AUTO_INCREMENT`
    * `servico_id INT`
    * `local_recolhimento VARCHAR(50)`
    * `justificativa_legal TEXT`

### 4. Estrutura de Pastas do Projeto (Source Tree)
O código será organizado na seguinte estrutura para garantir a separação de responsabilidades:

/buscafacil-iss/
|-- app/
|   |-- static/         # CSS, JS, Imagens
|   |-- templates/      # Arquivos HTML
|   |-- engine/         # Motor de Busca (lógica principal)
|   |-- models/         # Modelos do Banco de Dados
|   |-- routes.py       # Rota da página de consulta
|   |-- init.py     # Inicializador da aplicação
|-- tests/              # Testes unitários
|-- requirements.txt    # Dependências Python
|-- config.py           # Configurações
|-- run.py              # Ponto de entrada da aplicação

### 5. Estratégia de API
A aplicação seguirá um padrão monolítico, servindo as páginas HTML diretamente. Portanto, não haverá uma especificação de API REST/GraphQL externa para o MVP. A comunicação entre a interface (`templates`) e a lógica (`engine`) ocorrerá internamente no servidor.

### 6. Implantação e DevOps
A implantação será feita em um ambiente de hospedagem na Hostgator. O processo será automatizado por um pipeline de CI/CD básico (conforme a História 1.1 do PRD), que enviará o código do repositório Git para o servidor.

### 7. Estratégia de Testes
O foco dos testes do MVP será em **testes unitários** para o diretório `app/engine/`. É crucial garantir que a lógica de interpretação da lei seja 100% precisa. A biblioteca `pytest` será o padrão.

### 8. Segurança
Para o MVP, a segurança se concentrará em práticas de desenvolvimento seguro em Python (ex: prevenção de SQL Injection via ORM) e na configuração adequada do servidor. Como não há autenticação de usuário na versão inicial, a complexidade de segurança é reduzida.