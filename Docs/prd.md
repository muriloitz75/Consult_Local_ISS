# PRD: Busca Assertiva ISS - Lcp 116 (Versão 1.0 - FINAL)

> **📋 NOTA:** Este documento foi fragmentado em módulos específicos para melhor organização.
> Consulte o [README.md](README.md) para navegar pela documentação completa.
>
> **Documentos relacionados:**
> - [Visão Geral do Projeto](01-visao-geral-projeto.md)
> - [Requisitos Funcionais](02-requisitos-funcionais.md)
> - [Diretrizes de Design](03-diretrizes-design-ux.md)
> - [Épicos e Histórias](06-epicos-historias-usuario.md)
> - [Próximos Passos](07-handoffs-proximos-passos.md)

### 1. Metas e Contexto de Fundo
* **Meta Primária:** Reduzir em 95% o tempo necessário para uma consulta sobre o local de recolhimento do ISS em comparação com o processo manual.
* **Contexto de Fundo:** Contadores e Auditores Fiscais dependem de um processo manual, demorado e sujeito a erros para interpretar a LC 116/2003. Esta aplicação web visa eliminar essa ineficiência, fornecendo respostas assertivas e com respaldo legal de forma instantânea.
* **Controle de Versões:**
    | Data | Versão | Descrição | Autor |
    | :--- | :--- | :--- | :--- |
    | 10/08/2025 | 1.0 | Criação e finalização do PRD inicial. | John, Product Manager |

### 2. Requisitos
* **Requisitos Funcionais:**
    * **RF1:** O sistema deve exibir a lista completa de serviços da LC 116/2003 para seleção do usuário.
    * **RF2:** O sistema deve apresentar campos para o usuário preencher: Município do Prestador, Município do Tomador e Município da Execução.
    * **RF3:** O sistema deve fornecer um botão "Analisar" para submeter a consulta.
    * **RF4:** O resultado deve ser exibido em uma janela flutuante (modal).
    * **RF5:** A janela de resultado deve apresentar o município correto e a base legal da resposta.
    * **RF6:** O sistema deve validar se todos os campos obrigatórios foram preenchidos.
    * **RF7:** Se a validação falhar, a consulta não deve prosseguir.
    * **RF8:** Se a consulta for um caso complexo (fora do escopo do MVP), o sistema deve exibir uma mensagem informativa.
* **Requisitos Não Funcionais:**
    * **RNF1:** O resultado final deve ter grande destaque visual.
    * **RNF2:** A janela de resultado deve ter animações sutis e estilizadas.
    * **RNF3:** Em caso de falha na validação (RF7), os campos vazios devem executar um efeito de "tremor".

### 3. Diretrizes de Design da Interface (UI)
* **Visão Geral da UX:** A interface terá uma base **Séria e Corporativa**, executada de forma **Moderna e Minimalista**, com uma experiência **Educacional e Guiada**.
* **Identidade Visual (Branding):** Não há identidade visual pré-existente. A criação seguirá as melhores práticas e tendências de design.
* **Telas Principais (MVP):**
    1.  **Página de Consulta:** Tela principal e única da aplicação.
    2.  **Janela Flutuante de Resultado:** Componente exibido sobre a página principal.

### 4. Premissas Técnicas
* **Tecnologia Principal:** Python, MySQL e hospedagem Hostgator.
* **Arquitetura de Serviço:** Recomendação de arquitetura Monolítica para o MVP.
* **Requisitos de Testes:** Foco em Testes Unitários para a lógica do motor de busca.

### 5. Lista de Épicos
* **Épico 1: Lançamento do MVP - Consulta Pública e Assertiva**
    * **Objetivo:** Estabelecer a infraestrutura e entregar a funcionalidade principal de consulta para os casos de uso mais comuns.

### 6. Detalhes do Épico 1
* **História 1.1: Configuração Inicial do Projeto e Infraestrutura Base**
* **História 1.2: Modelagem das Regras e Motor de Busca (Core)**
* **História 1.3: Implementação da Interface de Consulta e Resultado**

### 7. Relatório de Checklist
* **Status da Validação:** APROVADO.
* **Resumo:** O PRD está completo, alinhado com o Briefing do Projeto e com o escopo do MVP. Os requisitos são claros, testáveis e a estrutura de épico/histórias é lógica e sequencial. O documento está pronto para ser entregue ao Arquiteto e ao UX Expert.

### 8. Próximos Passos
* **Handoff para UX Expert (Sally):**
    > Com base neste PRD, especialmente na seção 'Diretrizes de Design da Interface', por favor, crie a **Especificação de UI/UX** (`front-end-spec.md`). O foco do MVP é uma única página com uma janela de resultado flutuante, seguindo uma visão de design 'Séria, Moderna e Educacional'.

* **Handoff para Arquiteto (Winston):**
    > Com base neste PRD, especialmente nas 'Premissas Técnicas', por favor, crie o **Documento de Arquitetura** (`architecture.md`). O projeto é um monolítico em Python/MySQL na Hostgator. O principal desafio é modelar as regras da LC 116 e criar o motor de busca para o MVP.