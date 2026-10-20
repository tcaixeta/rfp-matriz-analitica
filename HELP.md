# HELP — Análise de documentos de concorrência (RFP)

Este guia explica como usar o material criado para analisar documentos de processos de concorrência (RFP, RFI, RFQ, editais, anexos, Q&A, adendos) do lado do proponente e gerar uma **matriz analítica rastreável de 23 colunas**.

O material existe em duas formas:

| Forma | Arquivo | Onde funciona | Quando usar |
|---|---|---|---|
| **Persona** | `persona-analista-rfp.md` | Qualquer LLM (Claude, ChatGPT, Gemini, Copilot, modelos locais) | Quando você só pode colar instruções num chat |
| **Skill** | `skills/rfp-matriz-analitica.skill` (pasta-fonte em `skills/rfp-matriz-analitica/`) | Claude (Claude.ai, app desktop, Claude Code) e, com adaptação, outros agentes | Quando a ferramenta consegue executar Python: a skill extrai os documentos com localizadores exatos, monta a matriz por script e valida o resultado |

A skill é a versão mais completa e mais testada. A persona é a versão portátil.

---

## Sumário

1. [Conteúdo do pacote](#1-conteúdo-do-pacote)
2. [Usar a persona em qualquer LLM](#2-usar-a-persona-em-qualquer-llm)
3. [Usar a skill no Claude](#3-usar-a-skill-no-claude)
4. [Usar a skill em outros LLMs e agentes](#4-usar-a-skill-em-outros-llms-e-agentes)
5. [Como ler a matriz](#5-como-ler-a-matriz)
6. [Scripts: referência rápida](#6-scripts-referência-rápida)
7. [Testar com o kit sintético](#7-testar-com-o-kit-sintético)
8. [Solução de problemas](#8-solução-de-problemas)
9. [Persona × skill: diferenças](#9-persona--skill-diferenças)

---

## 1. Conteúdo do pacote

```
persona-analista-rfp.md                  ← persona (texto para colar em qualquer LLM)
HELP.md                                  ← este guia
skills/
├── rfp-matriz-analitica.skill           ← skill empacotada (arquivo .zip) para instalar no Claude
├── rfp-matriz-analitica/                ← fonte da skill
│   ├── SKILL.md                         ← instruções principais e fluxo de trabalho
│   ├── references/                      ← taxonomias, criticidade, rastreabilidade, frameworks,
│   │                                      formato de saída e modelos de prompt
│   ├── scripts/
│   │   ├── extract_documents.py         ← extração com localizadores (PDF, Word, PPT, Excel)
│   │   ├── build_matrix.py              ← monta a matriz a partir de um JSON de itens
│   │   ├── check_matrix.py              ← valida estrutura, aritmética e calibragem
│   │   └── export_xlsx.py               ← exporta a matriz para Excel
│   └── evals/                           ← casos de teste da skill (não vão no .skill)
└── rfp-matriz-analitica-workspace/      ← histórico de testes, iterações e otimização da descrição
kit-de-testes/
├── LEIA-ME.md                           ← como rodar e avaliar os testes
├── documentos/                          ← RFP fictício (PDF, Word, PPT, Excel) com problemas plantados
└── avaliacao/                           ← gabarito (68 itens) e planilhas de avaliação
```

---

## 2. Usar a persona em qualquer LLM

### 2.1 Onde colar

Cole o conteúdo de `persona-analista-rfp.md` no campo de instruções da ferramenta. Se não houver um campo assim, cole como primeira mensagem da conversa.

| Ferramenta | Onde colar |
|---|---|
| Claude.ai | Em um **Projeto**: instruções do projeto. Sem projeto: primeira mensagem. |
| ChatGPT | **GPT personalizado** (campo de instruções) ou **Projeto** (instruções). Sem isso: primeira mensagem. |
| Gemini | **Gem** (campo de instruções) ou primeira mensagem. |
| Microsoft Copilot | Instruções do agente (Copilot Studio / agentes) ou primeira mensagem. |
| API / modelos locais | Mensagem de sistema (*system prompt*). |

> Algumas ferramentas limitam o tamanho do campo de instruções (a persona tem cerca de 30 mil caracteres). Se não couber, anexe o arquivo `persona-analista-rfp.md` como conhecimento ou documento do projeto e escreva nas instruções: "Siga a persona do arquivo persona-analista-rfp.md".

### 2.2 Como pedir a análise

Anexe os documentos e use o modelo abaixo. Ele também está, com as variações, em `skills/rfp-matriz-analitica/references/modelos-de-prompt.md`.

```markdown
# Solicitação de análise

## Processo
- Cliente: [nome do cliente]
- Identificação do processo: [ex.: RFP nº 2026-017]
- Objeto resumido: [ex.: serviços gerenciados de SOC e IAM]
- Valor estimado do contrato: [valor ou "não informado"]

## Documentos anexados
| # | Arquivo | Tipo | Versão/Data |
|---|---|---|---|
| 1 | [nome do arquivo] | [RFP / Anexo técnico / Minuta / Q&A / Apresentação] | [versão ou data] |

## Instruções desta análise
- Ordem de processamento: padrão
- Limite de linhas por resposta (opcional): [30]
- Contexto do proponente (opcional): [ex.: nosso SOC fica no Brasil]

## Comando
Analise os documentos acima. Comece pelo inventário.
```

Para uma **nova rodada** (novo Q&A, adendo ou errata), use o Modelo B do arquivo de modelos: ele pede a análise só do documento novo, confrontada com a matriz anterior.

### 2.3 O bloco de status e o "continuar"

Com a persona, a matriz sai em partes de até 30 linhas. Toda resposta começa com uma linha `▶ PARTE n` e termina com um bloco de status:

| No fim da resposta | O que fazer |
|---|---|
| ⏸ **ANÁLISE EM ANDAMENTO** | Envie `continuar` |
| ✅ **ANÁLISE CONCLUÍDA** | Terminou. Confira as "Pendências de cobertura" |
| ⛔ **ANÁLISE INTERROMPIDA** | Faça o que diz "Ação necessária" (por exemplo, anexar os documentos) |
| **Nenhum bloco de status** | A ferramenta cortou a resposta. Envie `continuar` |

Ao final, copie as partes para uma planilha (o cabeçalho se repete em cada parte; apague as repetições). Se tiver Python, salve as partes num arquivo `.md` e use `export_xlsx.py` (seção 6).

### 2.4 Cuidados com a persona

- **Páginas escaneadas:** se a ferramenta não lê imagens dentro do PDF, a persona registra "Possível conteúdo em imagem não lido — requer OCR". Nesse caso, envie a página como imagem (print ou PNG) ou um PDF com OCR.
- **Planilhas:** confirme que a ferramenta lê abas ocultas. Se não ler, reexiba as abas antes de anexar.
- **Notas do apresentador:** nem toda ferramenta lê as notas de slides do PowerPoint. Se a sua não ler, exporte as notas (no PowerPoint: Arquivo → Exportar → páginas de anotações) e anexe.

---

## 3. Usar a skill no Claude

### 3.1 Requisitos

- Ferramenta com **execução de código** (no Claude.ai e no app desktop, a opção de execução de código e criação de arquivos precisa estar ativada).
- Python 3.9 ou superior com as bibliotecas:

```bash
pip install pdfplumber python-docx python-pptx openpyxl
```

No ambiente de execução do Claude.ai, se uma biblioteca faltar, o próprio Claude costuma instalá-la ao rodar o script. No Claude Code, instale-as na máquina antes do primeiro uso.

### 3.2 Instalar no Claude.ai ou no app desktop

1. Quando o arquivo `rfp-matriz-analitica.skill` aparece na conversa, o cartão do arquivo pode mostrar o botão **Save skill**: clique nele para instalar no seu perfil (se a sua organização permitir criar skills).
2. Outra forma: abra **Configurações → Capacidades (Capabilities) → Skills**, use a opção de enviar uma skill e selecione o arquivo `.skill` (ele é um `.zip`). Os nomes exatos dos menus podem mudar entre versões.
3. Confirme que a skill **rfp-matriz-analitica** aparece ativa na lista.

### 3.3 Instalar no Claude Code

A skill é uma pasta com um `SKILL.md`. Copie ou descompacte a pasta para um destes lugares:

| Escopo | Destino |
|---|---|
| Pessoal (todos os projetos) | `~/.claude/skills/rfp-matriz-analitica/` |
| Só um projeto (versionável no Git) | `<pasta-do-projeto>/.claude/skills/rfp-matriz-analitica/` |

Exemplo com o arquivo empacotado:

```bash
mkdir -p ~/.claude/skills && unzip -o skills/rfp-matriz-analitica.skill -d ~/.claude/skills/
```

Depois, abra uma nova sessão do Claude Code: as skills são carregadas no início da sessão.

### 3.4 Como usar

Você não precisa chamar a skill pelo nome. Ela é acionada pela descrição sempre que você pedir algo como:

- "Analisa esse RFP e monta a matriz de requisitos" (com os arquivos anexados ou o caminho da pasta).
- "Quais são os critérios eliminatórios, prazos e multas deste edital?"
- "Chegou o adendo 2; compara com a matriz que já fizemos."
- "Prepara as perguntas de esclarecimento ligadas ao trecho de origem."

Se a skill não for acionada, peça explicitamente: **"Use a skill rfp-matriz-analitica"**. No Claude Code, as skills também podem ser chamadas pelo nome com `/`.

O modelo de pedido da seção 2.2 continua sendo a forma mais completa de pedir a análise.

### 3.5 O que a skill faz

1. Roda `extract_documents.py`, que gera um inventário e o texto de cada documento com localizadores. Ele também sinaliza páginas escaneadas (e salva PNG para leitura visual), abas ocultas, notas de slides, slides ocultos, comentários e marcas de revisão.
2. Identifica o regime (público/privado, setor regulado) e a cláusula de precedência entre documentos.
3. Decompõe os documentos em itens atômicos, classifica, cruza documentos, associa frameworks e calcula a criticidade.
4. Monta a matriz com `build_matrix.py`. O script numera os IDs, calcula a criticidade, confere as citações contra o texto extraído e roda o validador.
5. Entrega a matriz:
   - **Modo arquivo** (padrão quando há sistema de arquivos): grava `<processo>_Matriz_Analitica.md` (e `.xlsx`, se pedido) e mostra no chat só os status por documento.
   - **Modo conversa:** a tabela vai no chat em partes, com "continuar", como na persona.

Para receber em Excel, peça: "me devolve também em Excel".

### 3.6 Atualizar a skill

Edite os arquivos em `skills/rfp-matriz-analitica/` e gere o pacote de novo (com a skill-creator, peça "reempacote a skill"), ou compacte a pasta em `.zip` com a extensão `.skill`, deixando de fora a pasta `evals/`. Depois, reinstale.

---

## 4. Usar a skill em outros LLMs e agentes

O formato `.skill` (pasta com `SKILL.md`) foi feito para o Claude. Algumas ferramentas de agentes já leem pastas com `SKILL.md`; consulte a documentação da sua. Nas demais, há três caminhos, do mais simples ao mais completo.

### 4.1 Só instruções (sem executar código)

Use a **persona** (seção 2). Ela tem as mesmas regras de análise, sem depender de scripts.

### 4.2 Instruções + arquivos de apoio (ferramenta com execução de Python)

Para ChatGPT (GPT personalizado ou Projeto com análise de dados/Code Interpreter), Gemini (Gems) ou Copilot (agentes):

1. **Instruções:** cole o corpo do `SKILL.md` (sem o cabeçalho entre `---`). Se não couber, use a persona e anexe o `SKILL.md` como arquivo.
2. **Arquivos de conhecimento:** anexe os 6 arquivos de `references/` e os 4 scripts de `scripts/`.
3. **Ajuste nas instruções:** acrescente: "Os scripts estão nos arquivos anexados. Copie-os para a área de execução antes de rodar. Onde o texto diz `<pasta_da_skill>/scripts/`, use o caminho em que os scripts foram salvos."
4. Teste com o kit (seção 7). Algumas ferramentas não têm todas as bibliotecas Python (em especial `pdfplumber`) ou não permitem instalá-las. Nesse caso, use o caminho 4.3.

### 4.3 Fluxo híbrido: scripts no seu computador + qualquer LLM

Funciona com qualquer modelo, inclusive local, e mantém a rastreabilidade dos scripts:

```bash
# 1. Extrair os documentos, na ordem: RFP → anexos técnicos → comerciais/minuta → apresentações → Q&A/adendos
python skills/rfp-matriz-analitica/scripts/extract_documents.py --out trabalho/extracao \
  RFP.pdf Anexo_I.docx Apresentacao.pptx QA.xlsx
```

2. Envie ao LLM a persona (ou o `SKILL.md` com as `references/`), o `trabalho/extracao/inventario.md` e os arquivos `Dnn_*.md`. Se houver páginas escaneadas, envie também as imagens de `trabalho/extracao/imagens/`.
3. Peça os itens **em JSON**, no formato descrito no cabeçalho de `build_matrix.py` (rode `python skills/rfp-matriz-analitica/scripts/build_matrix.py --help` para ver o formato). Salve a resposta como `trabalho/itens.json`.
4. Monte, valide e exporte:

```bash
python skills/rfp-matriz-analitica/scripts/build_matrix.py trabalho/itens.json \
  --out RFP_Matriz_Analitica.md --extracao trabalho/extracao --xlsx
```

5. Corrija o que o validador apontar (pedindo ao LLM para ajustar os itens indicados) e rode o passo 4 de novo.

---

## 5. Como ler a matriz

Cada linha é um item atômico, com 23 colunas: ID, documento, versão, seção, localizador, evidência literal, tipo, domínio, descrição analítica, obrigatoriedade, natureza da evidência, severidade, probabilidade, criticidade, impacto, framework, controle/cláusula, tipo de associação, IDs relacionados, status de vigência, ação recomendada, pergunta de esclarecimento e responsável interno.

**Pontos-chave:**

- **ID `Dnn-nnn`:** documento + sequência. Os códigos `D01`, `D02`... seguem a ordem de processamento, e não a de envio.
- **Localizador:** página física e impressa no PDF (`p. 2 (impressa: 1)`), seção no Word, slide ou notas no PowerPoint, aba e célula no Excel. `(OCR)` indica trecho lido de imagem.
- **Criticidade = Severidade (1–5) × Probabilidade (1–5):** 1–4 Baixa, 5–9 Média, 10–15 Alta, 16–25 Crítica. Severidade 5 nunca fica abaixo de Alta. Probabilidade 4 ou 5 exige evidência citada.
- **Status de vigência:**
  - Alterado ou Substituído: o Q&A ou um adendo mudou o item.
  - Duplicado: repetição sem informação nova; a criticidade fica no item original.
  - Em esclarecimento: depende de resposta do cliente.
- **Lacuna × Registro de cobertura:**
  - Documento citado pelo cliente e não fornecido = Lacuna, com criticidade.
  - Trecho não lido ou arquivo que você listou e não anexou = Registro de cobertura, sem criticidade.
- **Pendências de cobertura**, no status final: o que precisa da sua ação, como uma página que requer OCR, um arquivo faltante ou um documento a pedir ao cliente.

**Uso prático:** filtre por **Criticidade** (Crítica/Alta) para o Go/No-Go, por **Ação recomendada = Esclarecer no Q&A** para montar as perguntas e por **Responsável interno** para distribuir entre Jurídico, Pricing e Pré-venda.

---

## 6. Scripts: referência rápida

Em todos os comandos, use o caminho até a pasta da skill (ex.: `skills/rfp-matriz-analitica/scripts/...` ou `~/.claude/skills/rfp-matriz-analitica/scripts/...`).

| Script | Uso | O que faz |
|---|---|---|
| `extract_documents.py` | `python extract_documents.py --out <pasta> arq1 arq2 ... [--start 5]` | Extrai texto com localizadores e gera `inventario.md`. `--start` continua a numeração (ex.: D05) numa rodada incremental. Arquivo inexistente vira "ARQUIVO NÃO ENCONTRADO". |
| `build_matrix.py` | `python build_matrix.py itens.json --out matriz.md [--extracao <pasta>] [--xlsx]` | Monta a matriz, confere citações, roda o validador e exporta. O formato do JSON está no cabeçalho do script (`--help`). |
| `check_matrix.py` | `python check_matrix.py matriz.md [--max-critica 0.25] [--max-alta 0.40]` | Valida a matriz: ERRO = corrigir; AVISO = reexaminar com julgamento. |
| `export_xlsx.py` | `python export_xlsx.py matriz.md [saida.xlsx]` | Gera Excel com as abas Matriz (filtros e cores), Documentos e Resumo. |

**Dica para páginas escaneadas:** salve a transcrição da imagem como `<pasta de extração>/D01_p6_ocr.md` (código do documento + página). Assim o `build_matrix.py` também confere as citações tiradas da imagem.

---

## 7. Testar com o kit sintético

O kit `kit-de-testes/` tem um RFP **fictício** (Banco Horizonte Fictício S.A.) em 4 formatos, com problemas plantados de propósito: página escaneada, notas de slide, aba oculta, contradições e alterações por Q&A.

1. Rode a persona ou a skill sobre os arquivos de `kit-de-testes/documentos/` com o pedido da seção 2.2.
2. Compare o resultado com `kit-de-testes/avaliacao/Gabarito.md` (68 itens, 31 essenciais, 13 armadilhas) e preencha `Planilha_de_Avaliacao.xlsx`.
3. Metas: 100% dos itens essenciais, ao menos 85% de cobertura geral, ao menos 95% de localizadores corretos, nenhum identificador inventado e as 13 armadilhas evitadas.

**Não envie a pasta `avaliacao/` ao modelo.**

Há também uma avaliação automática (usada no desenvolvimento da skill):

```bash
python skills/rfp-matriz-analitica/evals/grade_matrix.py --eval-id 1 --matrix <matriz.md>
```

Ela faz 38 verificações: 22 de formato e rastreabilidade, e 16 de conteúdo, estas independentes do formato.

**Resultados obtidos no desenvolvimento** (detalhes em `skills/rfp-matriz-analitica-workspace/revisao-iteration-*.html`):

- Skill: 100% das verificações nos 3 casos de teste, Críticas entre 10% e 11%, Altas em cerca de 30%.
- Sem skill: o modelo encontra os mesmos problemas, mas não entrega a matriz rastreável (cerca de 55% das verificações).

---

## 8. Solução de problemas

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| A skill não é acionada | O pedido não menciona documentos de concorrência, ou a ferramenta não vê os anexos | Anexe os arquivos (ou indique a pasta) e peça "Use a skill rfp-matriz-analitica" |
| "ModuleNotFoundError" ao rodar um script | Biblioteca Python ausente | `pip install pdfplumber python-docx python-pptx openpyxl` |
| "No such file" ao chamar `scripts/...` | Caminho relativo a partir de outra pasta | Use o caminho absoluto até a pasta da skill |
| Página registrada como "requer OCR" | PDF escaneado e ferramenta sem leitura de imagem | Envie a página como imagem ou um PDF com OCR |
| AVISO de muitas Críticas (mais de 25%) ou Altas (mais de 40%) | Gravidade herdada de itens relacionados ou Severidade 4 usada demais | Revise os itens pelas regras de `references/criticidade.md` |
| AVISO "Lacuna/Contradição com Probabilidade 4/5 sem evidência" | Justificativa genérica | Use `Probabilidade 5: <motivo> — "<trecho citado>"` ou deixe registrado que o cliente recusou formalmente |
| ERRO "referência a chave inexistente" na montagem final | Item cita uma chave que não existe | Corrija a chave no JSON (na montagem parcial isso é permitido) |
| Resposta da persona termina sem status | A ferramenta cortou a resposta | Envie `continuar` |
| Matriz com documentos fora de ordem | Arquivos passados na ordem de envio | Peça "Ordem de processamento: padrão" ou indique a ordem |

---

## 9. Persona × skill: diferenças

A skill foi refinada em 3 iterações de teste depois da última versão da persona. Ela tem estas regras e recursos que **a persona não tem**:

| Recurso | Skill | Persona |
|---|---|---|
| Extração com localizadores por script (incluindo abas ocultas, notas, slides ocultos, comentários) | Sim | Depende da ferramenta |
| Montagem por script (IDs, criticidade, status) e conferência automática de citações | Sim | Não |
| Validação automática (`check_matrix.py`) | Sim | Não (checklist manual) |
| Modo arquivo (matriz completa num `.md`/`.xlsx`, sem "continuar") | Sim | Não |
| Orientação "Severidade 4 ou 3?" e calibragem de Altas | Sim | Não |
| Itens **Duplicados** sem criticidade própria | Sim | Não |
| Formato obrigatório de evidência para Probabilidade 4/5 | Sim | Parcial |
| Arquivo listado e não anexado = só Registro de cobertura | Sim | Parcial |

Se for usar a persona em produção, vale atualizá-la com essas regras. As regras correspondentes estão em `skills/rfp-matriz-analitica/references/criticidade.md` e `references/taxonomias.md`.
