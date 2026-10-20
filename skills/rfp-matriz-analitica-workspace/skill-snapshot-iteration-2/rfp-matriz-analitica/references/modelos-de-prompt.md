# Modelos de prompt

Modelos que o usuário pode copiar para pedir análises. Eles só trazem o contexto de cada análise: método, classificações e formato já estão na skill. Campos entre `[colchetes]` são preenchidos pelo usuário; linhas opcionais podem ser apagadas.

## Modelo A — análise completa (primeira rodada)

```markdown
# Solicitação de análise

## Processo
- Cliente: [nome do cliente]
- Identificação do processo: [ex.: RFP nº 2026-017]
- Objeto resumido: [ex.: serviços gerenciados de SOC e IAM]
- Valor estimado do contrato: [valor ou "não informado"]   <!-- usado nas faixas % da Severidade -->

## Documentos anexados
| # | Arquivo | Tipo | Versão/Data |
|---|---|---|---|
| 1 | [nome do arquivo] | [RFP / Anexo técnico / Minuta / Q&A / Apresentação / Outro] | [versão ou data] |

## Instruções desta análise
- Ordem de processamento: [padrão] ou [defina a ordem]
- Entrega: [arquivo .md (padrão) · também em Excel · tabela no chat]
- Limite de linhas por resposta no chat (opcional): [30]
- Prioridade de leitura (opcional, sem reduzir a cobertura): [ex.: cláusulas contratuais e SLAs]
- Contexto do proponente (opcional): [ex.: nosso SOC fica no Brasil; não temos certificação X]
  <!-- Se preenchido, a probabilidade pode considerar esse contexto; se vazio, nada é presumido sobre o proponente -->

## Comando
Analise os documentos acima. Comece pelo inventário.
```

A lista de documentos funciona como controle: se um arquivo listado não for anexado, ou não puder ser lido, isso aparece no inventário como Registro de cobertura.

## Modelo B — análise incremental (novo Q&A, adendo ou versão)

```markdown
# Solicitação de análise incremental

## Processo
- Identificação do processo: [ex.: RFP nº 2026-017]
- Novo(s) documento(s): [nome do arquivo — tipo — data/rodada]

## Base já analisada
- Matriz anterior: [caminho do arquivo .md ou .xlsx, ou cole as linhas afetadas]
- Último ID utilizado: [ex.: D04-019] · Próximo código de documento: [ex.: D05]

## Comando
Analise somente o(s) novo(s) documento(s), confrontando-o(s) com a matriz anterior.
Registre alterações, substituições, confirmações e novas contradições, indicando em
"IDs relacionados" os itens afetados da matriz anterior. Não repita itens que não mudaram.
```

## Modelo C — continuação (modo conversa)

```markdown
continuar
```

Se a conversa ficou longa:

```markdown
Continue a partir de [documento, seção, localizador]. Próximo ID: [Dnn-nnn].
Mantenha as classificações e a numeração já usadas.
```
