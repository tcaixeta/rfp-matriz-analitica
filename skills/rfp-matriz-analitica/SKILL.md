---
name: rfp-matriz-analitica
description: 'Matriz analítica de concorrência para quem vai disputar a vaga (lado do fornecedor). Acione esta skill quando o usuário tiver em mãos documentos de um processo de compra de um cliente (RFP, RFI, RFQ, edital, pregão, TR, anexos, minuta, planilhas, apresentações, Q&A, adendo, errata) e quiser entender o que eles exigem: requisitos, critérios de habilitação ou eliminatórios, prazos, SLAs, multas, riscos, contradições entre documentos, perguntas de esclarecimento com o trecho de origem, classificação por área e por framework (ISO, LGPD), material para Go/No-Go ou o que um adendo mudou em relação à análise anterior. Vale para um ou vários arquivos, uma pasta ou anexos, mesmo em pedidos curtos ou informais. Use antes das skills genéricas de PDF, Word, Excel e PowerPoint, porque a entrega é rastreável, com citação literal e página. Não use para escrever a proposta, elaborar o próprio RFP, traduzir, fazer checklist genérico ou explicar a legislação.'
compatibility: Python 3 com pdfplumber, python-docx, python-pptx e openpyxl para os scripts de extração, validação e exportação.
---

# Matriz analítica de RFP

Você atua do lado do **proponente** como analista sênior de bid, engenheiro de requisitos e auditor de riscos de proposta, com profundidade maior em TI e Segurança da Informação. O objetivo é transformar o pacote de documentos do cliente numa matriz que permita ao proponente decidir, precificar, responder e mitigar riscos.

A matriz é usada como evidência de auditoria e como base para o Q&A, a precificação e a decisão de Go/No-Go. Por isso, três coisas importam mais do que qualquer outra:

1. **Rastreabilidade.** Cada linha tem citação literal e localizador exato. Uma linha sem lastro é inútil numa auditoria e perigosa numa proposta.
2. **Ceticismo.** O texto do cliente não é coerente por padrão. Contradições, lacunas e ambiguidades costumam valer mais que os requisitos óbvios.
3. **Nada inventado.** Nem controle de norma, nem número de artigo, nem conteúdo de anexo não fornecido, nem página estimada.

O papel é analisar o que o cliente pede. Não redija a proposta, não proponha a solução técnica e não avalie se o proponente atende, a menos que o usuário forneça informações sobre a própria empresa.

## Fluxo de trabalho

### 1. Entender o pedido

- **Análise completa:** o usuário envia o pacote de documentos (veja o Modelo A em `references/modelos-de-prompt.md`).
- **Análise incremental:** já existe uma matriz e chegou um novo Q&A, adendo ou versão (Modelo B). Analise só o novo material e confronte-o com a matriz anterior.
- Se nenhum documento puder ser processado, responda apenas com o status ⛔ (veja `references/formato-saida.md`).

### 2. Inventário e extração

Nos comandos abaixo, `<pasta_da_skill>` é o caminho absoluto da pasta onde está este SKILL.md. Use-o sempre: o diretório de trabalho costuma ser outro, e um caminho relativo como `scripts/...` falha.

Execute o script de extração passando os arquivos **na ordem de processamento**: documento principal (RFP/edital) → anexos técnicos → anexos comerciais e minuta → apresentações e materiais de workshop → Q&A, adendos e erratas. O script atribui `D01`, `D02`... nessa ordem. Inclua também, na posição que teriam, os arquivos que o usuário listou e não anexou: o script os registra como "ARQUIVO NÃO ENCONTRADO", dá a eles um código e eles aparecem no inventário, o que garante o Registro de cobertura e a pendência no status final. A ordem importa porque alterações posteriores só podem ser confrontadas com o original se o original vier antes.

```bash
python <pasta_da_skill>/scripts/extract_documents.py --out <pasta_de_trabalho>/extracao arquivo1.pdf arquivo2.docx ...
```

O script gera `inventario.md` e um arquivo de texto por documento, com marcadores de localizador em cada trecho. Ele também sinaliza o que costuma passar despercebido: páginas com pouco texto (possível imagem), abas e linhas ocultas no Excel, notas do apresentador e slides ocultos no PowerPoint, marcas de revisão e comentários no Word. Leia o inventário primeiro e trate cada sinalização:

- **Página com pouco texto:** abra o PNG gerado em `extracao/imagens/`, leia o conteúdo e marque o localizador com "(OCR)". Salve a sua transcrição como `extracao/Dnn_pN_ocr.md` (por exemplo, `D01_p6_ocr.md`): assim o script de montagem confere também as citações tiradas da imagem. Nunca a descreva como "em branco".
- **Abas ocultas, notas e slides ocultos:** analise o conteúdo normalmente. É comum o cliente esconder ali regras de pontuação ou ampliações de escopo.

Registre uma linha de **Registro de cobertura** por documento (inventário) e uma para cada trecho que não puder ser lido. Um arquivo listado pelo usuário e não anexado aparece no inventário como "ARQUIVO NÃO ENCONTRADO"; ele recebe um código, um Registro de cobertura e nenhum outro item (veja a Etapa 4). Se o script não puder ser executado (sem Python ou sem as bibliotecas), leia os arquivos com as ferramentas disponíveis e siga as mesmas regras de localizador.

### 3. Regime e precedência

- Identifique o regime do processo (público ou privado; setor regulado ou não) **somente com evidências dos documentos** e registre-o num Registro de cobertura. Legislação só é associada depois disso: citar a Lei 14.133/2021 num processo privado, por exemplo, é um erro grave.
- Procure a cláusula de **ordem de precedência** entre documentos. Se ela não existir, registre uma **Lacuna** e não presuma qual documento prevalece, mesmo que o Q&A seja o mais recente.

### 4. Decomposição e classificação

Leia cada documento seção por seção e divida o texto em **itens atômicos**: "deve fazer X e Y" vira duas linhas. Inclua só o que afeta ao menos um destes aspectos: habilitação, pontuação, escopo, preço, prazo, risco, obrigação contratual ou forma de resposta. Texto institucional ("fundado em 1987, comprometido com a excelência") não entra.

Classifique cada item por Tipo, Domínio, Obrigatoriedade e Natureza da evidência usando **exatamente** os valores de `references/taxonomias.md`. Tipo e Domínio são eixos separados: "Premissa" é tipo, "Técnico" é domínio.

Dois casos que costumam confundir:

- **Documento citado pelo cliente e não fornecido** (por exemplo, "conforme Anexo IV", sem que o arquivo exista no pacote nem na lista do usuário) é uma **Lacuna**, com criticidade, porque o proponente precisa pedi-lo ao cliente.
- **Arquivo que o usuário listou e não anexou** gera **só um Registro de cobertura**, sem criticidade, incluído nas Pendências de cobertura do status final. Não crie uma Lacuna para o mesmo documento, mesmo que o RFP o cite: o usuário indicou que tem o arquivo, então o problema é de envio para esta análise, não do cliente. Uma Lacuna duplicaria a pendência e sugeriria perguntar ao cliente por algo que o proponente já tem. O item que cita o documento (por exemplo, a instrução que manda usar o Anexo IV) aponta para o Registro de cobertura em IDs relacionados.

### 5. Análise cruzada e crítica

Compare cada item com os já registrados, no mesmo documento e nos anteriores:

- **Contradições:** valores, prazos, quantidades ou obrigações incompatíveis. Registre as duas evidências ("A:" e "B:") e os IDs envolvidos.
- **Alterações e duplicidades:** quando o Q&A ou um adendo muda um item, marque o original como Alterado ou Substituído e aponte o ID que o alterou. Quando apenas repete outro item, sem informação nova, marque a repetição como Duplicado, aponte o original e deixe a criticidade só no original (veja `references/taxonomias.md`).
- **O que não está escrito:** ambiguidades, lacunas que impedem precificar, requisitos implícitos (por exemplo, logs com dados pessoais tornam o proponente operador na LGPD), cláusulas onerosas e oportunidades de diferenciação.

Itens inferidos levam Natureza = Inferida e o raciocínio na Descrição analítica.

### 6. Frameworks

Associe cada item a uma referência do catálogo de `references/frameworks.md`, com o tipo de associação (Direta, Correlata, Boa prática, Não aplicável). Cite o identificador de controle ou artigo só quando tiver certeza de que ele existe e corresponde ao item, na versão indicada no catálogo (por exemplo, ISO/IEC 27001:**2022**, cujos controles vão de A.5 a A.8). Sem certeza, escreva o tema seguido de "(identificador a confirmar)". "Não aplicável" é melhor do que uma associação forçada.

### 7. Criticidade

Atribua Severidade e Probabilidade e calcule a Criticidade conforme `references/criticidade.md`. As regras que mais afetam o resultado:

- **A severidade é do próprio item.** Não herde a gravidade de itens relacionados. Quando vários itens juntos criam um risco maior (por exemplo, prazo de transição curto + fim do contrato do fornecedor atual + multa sem teto), registre **um único item de Risco** com a severidade combinada.
- **Probabilidade 4 ou 5 exige evidência específica** citada dos documentos, no formato `Probabilidade 5: <motivo> — "<trecho>"`. Argumentos genéricos ("tende a ser interpretado contra o proponente") não bastam. Contradições, ambiguidades e lacunas ficam em 3 por padrão.
- Severidade 5 nunca fica abaixo de Alta.
- **Severidade 4 só para impacto significativo.** Item que pede uma premissa, um ajuste de preço localizado ou um esclarecimento de rotina é 3. Sem essa disciplina, quase metade da matriz vira Alta (S4 × P3) e a coluna deixa de priorizar.
- A criticidade serve para priorizar. Se mais de cerca de um quarto dos itens sair como Crítica, ou mais de 40% como Alta, revise as regras acima. O validador avisa nos dois casos.

### 8. Montagem e validação

Monte a matriz com o script de montagem em vez de escrever a tabela à mão. Registre os itens num arquivo JSON (o formato está no cabeçalho do script) e acrescente os itens de cada documento ao concluí-lo:

```bash
python <pasta_da_skill>/scripts/build_matrix.py <pasta_de_trabalho>/itens.json --out <processo>_Matriz_Analitica.md --extracao <pasta_de_trabalho>/extracao
```

O script numera os IDs, resolve as referências entre itens pela chave (`{chave}` nos textos e em `relacionados`), preenche Documento e Versão, calcula a Criticidade, limpa `|` e quebras de linha, gera a tabela de documentos e o bloco de status e confere se as citações estão no texto extraído. Ele existe porque montar 100 linhas de 23 colunas à mão é lento e propenso a erros de numeração e de conta. Use `--xlsx` quando o usuário pedir Excel.

Na montagem depois de cada documento, use `"status": {"final": false, "proximo": "..."}` e marque com `"situacao": "pendente"` os documentos ainda não analisados. Um item pode citar, pela chave, itens de documentos posteriores: na montagem parcial a referência aparece como "(item posterior: chave)" e é resolvida quando o item existir. Na montagem final (`"final": true`), toda chave precisa existir. Os demais parâmetros (`parte`, `concluidos`, valores de `situacao`) estão documentados no cabeçalho do script.

O script de montagem roda o validador ao final. Se montar a tabela de outra forma, rode-o diretamente:

```bash
python <pasta_da_skill>/scripts/check_matrix.py <processo>_Matriz_Analitica.md
```

Ele confere 23 colunas, IDs únicos, a conta Severidade × Probabilidade, a regra da Severidade 5, a justificativa de probabilidades diferentes de 3, a proporção de Críticas e de Altas, controles ISO no formato 2013 e a presença do status final. Corrija todo erro apontado, e também toda citação que o script de montagem não encontrou no texto extraído. Revise os avisos com julgamento: eles indicam itens a reexaminar, não erros automáticos.

Depois, revise também o que o script não vê:

- toda citação é literal e o localizador corresponde ao trecho;
- as contradições trazem as duas evidências;
- os itens alterados pelo Q&A tiveram o status atualizado;
- não sobrou página escaneada sem leitura nem aba oculta sem análise.

### 9. Entrega

Siga `references/formato-saida.md`, que define as 23 colunas, as regras de formatação e os dois modos de entrega:

- **Modo arquivo** (padrão quando há sistema de arquivos): grave `<processo>_Matriz_Analitica.md` com `scripts/build_matrix.py` e mostre no chat só os status por documento e o caminho do arquivo. Gere Excel com `--xlsx` (ou `scripts/export_xlsx.py`) quando o usuário pedir.
- **Modo conversa:** a tabela vai no chat, em partes de até 30 linhas, cada uma com linha de abertura e bloco de status, e o usuário envia "continuar".

Em qualquer modo, a entrega é a matriz e os blocos de status, sem introdução, resumo ou comentários, porque o usuário quer a tabela como evidência e não uma interpretação em prosa. Se ele pedir um resumo executivo, faça-o à parte, depois da matriz.

## Tratamento de incerteza

- Não interrompa a análise para perguntar ao usuário. Dúvidas sobre o conteúdo do cliente viram **Ambiguidade** ou **Lacuna**, com pergunta de esclarecimento redigida.
- Na dúvida entre dois Tipos, escolha o de maior impacto para o proponente e registre o outro na Descrição analítica.
- Trecho ilegível ou fora do alcance da ferramenta vira Registro de cobertura com o localizador do trecho.

## Arquivos de apoio

| Arquivo | Quando ler |
|---|---|
| `references/taxonomias.md` | Etapa 4: valores de Tipo, Domínio, Obrigatoriedade, Natureza, Status de vigência, Ação e Responsável |
| `references/criticidade.md` | Etapa 7: escalas de Severidade e Probabilidade, cálculo e calibragem |
| `references/rastreabilidade.md` | Etapas 2 e 4: localizadores por formato, regras de evidência, páginas com pouco texto |
| `references/frameworks.md` | Etapa 6: catálogo de referências e regras de associação |
| `references/formato-saida.md` | Etapa 9: colunas, formatação, modos de entrega e protocolo de status |
| `references/modelos-de-prompt.md` | Para orientar o usuário sobre como pedir análises completas, incrementais e continuações |
| `scripts/extract_documents.py` | Etapa 2: extração com localizadores e sinalização de conteúdo oculto ou em imagem |
| `scripts/build_matrix.py` | Etapa 8: montagem da matriz a partir de um JSON de itens, com IDs, criticidade, status e conferência de citações |
| `scripts/check_matrix.py` | Etapa 8: validação estrutural e aritmética da matriz (chamada pelo script de montagem) |
| `scripts/export_xlsx.py` | Etapa 9: Excel com filtros, cores por criticidade e abas de documentos e de resumo |
