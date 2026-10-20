# Rastreabilidade

Cada item deve permitir que um auditor encontre a evidência no documento original sem ajuda.

## Localizador por formato

| Formato | Localizador obrigatório |
|---|---|
| PDF | Página física do arquivo. Se a numeração impressa for diferente, informe ambas: "p. 12 (impressa: 10)" |
| Word | Seção/cláusula numerada e título. A página, se informada, deve vir marcada "aprox." |
| PowerPoint | Número do slide e título do slide |
| Excel | Nome da aba e célula ou linha. Inclua o ID da pergunta/requisito se a planilha tiver um |
| Q&A / adendo | Número da pergunta ou do item e rodada/data |
| Imagem / escaneado | Localizador do formato de origem, acrescido de "(OCR)" |

## Regras de evidência

- A coluna **Evidência** contém a **citação literal** do trecho mínimo que sustenta o item, entre aspas, no idioma original, com "[...]" para supressões. Não parafraseie nessa coluna.
- **Contradição:** informe as duas evidências na coluna Evidência, identificadas como "A:" e "B:", e os dois localizadores na coluna Localizador. Registre os IDs envolvidos em IDs relacionados.
- **Lacuna:** a coluna Evidência deve conter "Não localizado", seguido da citação do trecho que gera a necessidade da informação, quando houver.
- **Requisito implícito e Risco inferido:** cite o trecho que motivou a inferência.
- Se a ferramenta em uso não expuser página, slide ou célula, escreva "não disponível" e use o melhor localizador alternativo (seção e título). **Nunca estime um número de página como se fosse exato.**

## Usando a extração do script

`scripts/extract_documents.py` marca cada trecho com o localizador já no formato desta tabela: `[p. 3 (impressa: 2)]` no PDF, `[§ 2. NÍVEIS DE SERVIÇO (SLA)]` no Word, `[slide 4 — "Desafios"]` e `[slide 5 — notas do apresentador]` no PowerPoint, `[aba "Q&A Rodada 1" · E4]` no Excel. Copie o localizador do marcador em vez de deduzi-lo: é a forma mais segura de acertar página física, página impressa e célula.

## Páginas com pouco texto

Página que traga só cabeçalho, rodapé, número de página ou pouquíssimo texto deve ser tratada como **possível conteúdo em imagem não lido** (digitalização, assinatura, anexo escaneado). O script sinaliza essas páginas no inventário e salva uma imagem PNG de cada uma.

- Abra a imagem, leia o conteúdo, analise-o como qualquer outro trecho e marque o localizador com "(OCR)".
- Nunca descreva a página como "em branco" nem afirme que o documento "não é escaneado" sem ter olhado a imagem.
- Se não for possível ler a imagem, registre um **Registro de cobertura** com "Possível conteúdo em imagem não lido — requer OCR" e o localizador da página, e inclua-o nas Pendências de cobertura do status final.
