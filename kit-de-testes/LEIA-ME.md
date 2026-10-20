# Kit de testes — Persona de análise de RFP

Cenário **fictício**: o *Banco Horizonte Fictício S.A.* contrata serviços de SOC e IAM pela RFP nº 2026-017. Os quatro documentos contêm problemas **plantados de propósito**: contradições, lacunas, ambiguidades, critérios eliminatórios, alterações por Q&A, uma página escaneada, notas de slide e uma aba oculta. O gabarito lista o que a persona deve encontrar.

## Estrutura

```
kit-de-testes/
├── LEIA-ME.md                     ← este arquivo
├── documentos/                    ← ENVIE ao modelo
│   ├── RFP-2026-017_Servicos_SOC_IAM.pdf
│   ├── Anexo_I_Especificacao_Tecnica.docx
│   ├── Apresentacao_Ambiente_Atual.pptx
│   └── QA_Rodada1_e_Questionario.xlsx
└── avaliacao/                     ← NÃO envie ao modelo
    ├── Gabarito.md                ← 68 itens esperados (31 essenciais ★) e 13 armadilhas
    └── Planilha_de_Avaliacao.xlsx ← preencha e veja as métricas calculadas
```

## Como executar

### Teste 1 — Execução completa (obrigatório)

1. Abra uma conversa nova na ferramenta que quer testar.
2. Cole o conteúdo de `persona-analista-rfp.md` como instrução de sistema (ou como primeira mensagem).
3. Anexe os **quatro** arquivos de `documentos/` e envie:

   > Analise os documentos anexos do processo RFP nº 2026-017. Comece pelo inventário.

4. Olhe o **bloco de status** no fim de cada resposta:
   - **⏸ ANÁLISE EM ANDAMENTO**: envie `continuar`.
   - **✅ ANÁLISE CONCLUÍDA**: terminou.
   - **⛔ ANÁLISE INTERROMPIDA**: faça o que o campo "Ação necessária" indicar.
   - **Nenhum bloco de status**: a resposta foi cortada pela ferramenta. Envie `continuar`.
5. Copie todas as partes da tabela para uma planilha. O cabeçalho se repete em cada parte; apague as repetições. Anote também quantos `continuar` foram necessários.

### Teste 2 — Ordem trocada (opcional)

Repita o Teste 1 anexando **primeiro** a planilha de Q&A e por último o RFP. A persona deve seguir a própria ordem de processamento (RFP → anexos → Q&A) e continuar marcando as alterações (G60 altera G06; G65 altera G47).

### Teste 3 — Comparação entre ferramentas (opcional)

Rode o Teste 1 em duas ferramentas (por exemplo, Claude e ChatGPT) e compare os resultados na planilha de avaliação. Os pontos que mais variam são a página escaneada (G28, G29), as notas do slide (G58) e a aba oculta (G67, G68), porque dependem de como cada ferramenta lê os arquivos.

## Como avaliar

1. Abra `avaliacao/Planilha_de_Avaliacao.xlsx`, aba **Avaliação**.
2. Para cada item do gabarito, procure o correspondente na saída da persona e preencha as colunas amarelas. A correspondência não precisa ser um para um: um item da persona pode cobrir vários itens do gabarito.
3. Na aba **Armadilhas**, marque se cada armadilha foi evitada.
4. Na aba **Resultado**, preencha as duas linhas manuais: as citações conferidas no original (amostra de 10) e os identificadores de controle inventados ou de versão errada.

### Metas de aprovação

| Métrica | Meta |
|---|---|
| Cobertura dos itens essenciais (★) | 100% |
| Cobertura geral | ≥ 85% |
| Localizador correto | ≥ 95% |
| Citação literal fiel (amostra de 10) | 10 de 10 |
| Tipo de item coerente | ≥ 80% |
| Criticidade na faixa esperada | ≥ 80% |
| Identificadores inventados ou de versão errada | 0 |
| Armadilhas evitadas | 13 de 13 |

**Itens encontrados pela persona que não estão no gabarito** não são erro, desde que sejam relevantes e tenham evidência. Anote-os em Observações; se forem bons, acrescente-os ao gabarito.

## Se algo falhar: onde ajustar a persona

| Falha observada | Seção da persona a revisar |
|---|---|
| Não encontrou contradições entre documentos (G08, G29, G30) | [METODOLOGIA] Etapa 6 |
| Escolheu um número de usuários sem registrar a falta de precedência | [METODOLOGIA] Etapa 2 · armadilha A03 |
| Página do PDF errada (usou a impressa como física) | [RASTREABILIDADE] Localizador por formato |
| Página escaneada descrita como "em branco" ou ignorada | [METODOLOGIA] Etapa 1 — Páginas com pouco texto |
| Ignorou as notas do slide ou a aba oculta | [TRATAMENTO DE INCERTEZA] · [RESPONSABILIDADES] |
| Muitos itens como Crítica (mais de cerca de 25%) | [TAXONOMIAS] Regras da severidade e da probabilidade · Calibragem |
| Documento citado pelo cliente registrado como Registro de cobertura (sem criticidade) | [TAXONOMIAS] Lacuna × Registro de cobertura |
| Controle ISO da versão 2013 ou inventado | [ASSOCIAÇÃO A FRAMEWORKS] Regras 1 e 2 |
| Citou a Lei 14.133 | [ASSOCIAÇÃO A FRAMEWORKS] Regra 4 |
| §7.5 abaixo de Alta | [TAXONOMIAS] Cálculo da criticidade |
| Texto fora da tabela além da linha de abertura e do status | [FORMATO DE SAÍDA] · [GUARDRAILS] |
| Resposta sem status, ✅ antes do fim ou números do status errados | [FORMATO DE SAÍDA] Protocolo de processamento e continuação |
| Juntou vários requisitos na mesma linha | [METODOLOGIA] Etapa 4 |

## Observações

- Os documentos são **fictícios** e seguros para usar em qualquer ferramenta.
- Para regenerar ou criar variações do cenário, peça neste mesmo chat: os documentos foram gerados por script.
