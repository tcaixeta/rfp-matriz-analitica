# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado no [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/)
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Unreleased]

## [1.0.0] - 2026-10-20 — Matriz Analítica de Concorrência (RFP)

### Adicionado
- **Persona Analista de RFP (`persona-analista-rfp.md`)**: Prompt monolítico de sistema portátil compatível com qualquer LLM (Claude, ChatGPT, Gemini, Copilot e modelos locais).
- **Skill Claude (`skills/rfp-matriz-analitica/`)**:
  - `SKILL.md` definindo o ciclo de vida, instruções analíticas e guardrails do agente.
  - Script `extract_documents.py` para extração de texto multi-formato (PDF com localizadores físico/impresso e detecção de imagens/OCR, Word com marcas de revisão e comentários, PowerPoint com slides e notas do apresentador, Excel com abas ocultas e linhas/colunas ocultas).
  - Script `build_matrix.py` para montagem da matriz de 23 colunas a partir de JSON estruturado, cálculo de criticidade, resolução de dependências `{chave}` e conferência automatizada de citações literais.
  - Script `check_matrix.py` (linter) para auditoria estrutural das 23 colunas, unicidade de IDs, integridade aritmética da fórmula de criticidade e detecção de controles obsoletos.
  - Script `export_xlsx.py` para geração de planilha Excel estilizada com abas *Matriz* (com formatação condicional), *Documentos* e *Resumo*.
  - Catálogo de referências modulares em `references/` (`criticidade.md`, `formato-saida.md`, `frameworks.md`, `modelos-de-prompt.md`, `rastreabilidade.md`, `taxonomias.md`).
  - Pacote compactado pronto para importação `skills/rfp-matriz-analitica.skill`.
- **Kit de Testes Sintético (`kit-de-testes/`)**:
  - Cenário fictício de contratação de serviços de SOC e IAM (*Banco Horizonte Fictício S.A.*, RFP nº 2026-017) em 4 formatos (PDF, DOCX, PPTX, XLSX).
  - Gabarito com 68 itens esperados, 31 essenciais e 13 armadilhas intencionais mapeadas.
  - Planilha de avaliação para aferição e histórico de benchmarks.
  - Script `grade_matrix.py` e `evals.json` contendo 38 asserções automáticas de auditoria.
- **Documentação**:
  - `README.md` abrangente com visão geral, arquitetura das 23 colunas, guias de início rápido, referências de CLI, motor de criticidade e solução de problemas.
  - `HELP.md` operacional com guia prático de execução e resolução de dúvidas.
