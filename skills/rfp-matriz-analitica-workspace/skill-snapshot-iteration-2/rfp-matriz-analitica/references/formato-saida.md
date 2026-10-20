# Formato de saída

## Colunas (nesta ordem)

| # | Coluna | Conteúdo |
|---|---|---|
| 1 | ID | `Dnn-nnn` (código do documento + sequência). Ex.: `D01-014` |
| 2 | Documento | Nome do arquivo |
| 3 | Versão/Data | Versão ou data do documento, ou "não informada" |
| 4 | Seção/Cláusula | Número e título da seção ou cláusula |
| 5 | Localizador | Página, slide ou aba/célula, conforme [RASTREABILIDADE] |
| 6 | Evidência | Citação literal |
| 7 | Tipo de item | Conforme taxonomia |
| 8 | Domínio | Conforme taxonomia |
| 9 | Descrição analítica | Interpretação objetiva e, se Inferida, o raciocínio |
| 10 | Obrigatoriedade | Mandatório / Desejável / Informativo |
| 11 | Natureza da evidência | Explícita / Inferida |
| 12 | Severidade | Nível e rótulo. Ex.: "4 · Maior" |
| 13 | Probabilidade | Nível e rótulo. Ex.: "3 · Possível" |
| 14 | Criticidade | Pontuação e classificação. Ex.: "12 · Alta" |
| 15 | Impacto para o proponente | Consequência para preço, prazo, escopo, risco, habilitação ou pontuação |
| 16 | Framework/Referência | Nome e versão |
| 17 | Controle/Cláusula | Identificador, ou tema + "(identificador a confirmar)" |
| 18 | Tipo de associação | Direta / Correlata / Boa prática / Não aplicável |
| 19 | IDs relacionados | IDs de contradições, alterações, duplicidades ou dependências |
| 20 | Status de vigência | Conforme taxonomia |
| 21 | Ação recomendada | Conforme taxonomia |
| 22 | Pergunta de esclarecimento | Pergunta pronta para envio ao cliente, ou "—" |
| 23 | Responsável interno sugerido | Conforme taxonomia |

## Regras de formatação

- Uma linha por item. Células vazias devem conter "—".
- Não use quebras de linha dentro das células. Para separar elementos, use " · ".
- Substitua o caractere "|" dentro do conteúdo por "/", para não quebrar a tabela.
- Ordene as linhas por documento e, dentro de cada documento, pela ordem em que aparecem no texto. As linhas de Registro de cobertura do inventário vêm primeiro.

## Modos de entrega

A matriz pode ter mais de 100 linhas de 23 colunas, o que não cabe numa única resposta de chat. Por isso há dois modos:

**Modo arquivo (padrão quando há sistema de arquivos).** Grave a matriz em `<processo>_Matriz_Analitica.md`, na pasta que o usuário indicar ou na pasta de trabalho. O arquivo tem: título com o processo, a tabela de documentos (código, arquivo, versão/data), a matriz completa e, no fim, o bloco de status final. Processe um documento por vez: ao concluir cada um, acrescente seus itens ao JSON e gere o arquivo com `scripts/build_matrix.py` (com `"status": {"final": false, "proximo": "..."}` enquanto houver documentos e `{"final": true}` no fim). No chat, a cada documento concluído, mostre só a linha de abertura e o bloco de status (⏸ ou ✅), sem a tabela, e no fim informe o caminho do arquivo. Não é preciso esperar "continuar" entre documentos. Se o usuário pedir Excel, gere-o com `scripts/export_xlsx.py`.

**Modo conversa (quando não há sistema de arquivos, ou o usuário pede a tabela no chat).** Siga o protocolo abaixo, que divide a matriz em partes e usa "continuar".

## Modo conversa: protocolo de partes e continuação

O usuário precisa saber, ao fim de cada resposta, se a análise terminou ou se deve enviar "continuar". Para isso, **toda resposta** segue esta estrutura, sem exceção:

1. **Linha de abertura** (uma linha, antes da tabela)
2. **Tabela** (cabeçalho completo + linhas de itens)
3. **Bloco de status** (depois da tabela, em um dos três formatos abaixo)

### Divisão das partes

- Cada resposta cobre **um único documento** e no máximo **30 linhas de tabela**, ou o limite que o usuário definir no prompt.
- Se o documento não couber nesse limite, divida-o em partes, encerrando cada parte em fronteira de seção. Se uma única seção exceder o limite, divida-a entre itens, nunca no meio de um item.
- Repita o cabeçalho da tabela em cada parte, para que as partes possam ser concatenadas.

### 1. Linha de abertura

```
▶ PARTE [n] · [Documento] ([Dnn]) · [trecho coberto: seções, páginas, slides ou abas] · Documento [x] de [total]
```

### 3. Bloco de status

Use **exatamente** um dos três formatos.

**Análise em andamento** (ainda há conteúdo a processar):

```
⏸ STATUS: ANÁLISE EM ANDAMENTO — parte [n]
Progresso: [k] de [total] documentos concluídos · [N] itens registrados até aqui (último ID: [Dnn-nnn])
Próximo trecho: [Documento] ([Dnn]), a partir de [seção / localizador]
➜ Envie "continuar" para prosseguir.
```

**Análise concluída** (todos os documentos foram processados):

```
✅ STATUS: ANÁLISE CONCLUÍDA
Documentos processados: [total] de [total] · Total de itens: [N] (de D01-001 a [Dnn-nnn])
Pendências de cobertura: [IDs dos Registros de cobertura (leitura parcial, trecho ilegível, possível imagem não lida, arquivo não anexado) e das Lacunas de documentos citados e não fornecidos — ou "nenhuma"]
Não é necessário enviar "continuar".
```

**Análise interrompida** (nenhum documento pôde ser processado):

```
⛔ STATUS: ANÁLISE INTERROMPIDA
Motivo: [ex.: nenhum documento anexado · nenhum arquivo legível]
➜ Ação necessária: [o que o usuário deve fazer para a análise começar]
```

Regras do status:
- Use **⏸ ANÁLISE EM ANDAMENTO** sempre que restar qualquer trecho ou documento a processar, inclusive quando a parte atual encerrar um documento e houver outro na fila.
- Use **✅ ANÁLISE CONCLUÍDA** somente depois do último trecho do último documento.
- Use **⛔ ANÁLISE INTERROMPIDA** somente quando nada puder ser processado. Problemas parciais (uma página ilegível, um arquivo listado pelo usuário e não anexado) viram **Registro de cobertura**, a análise continua com o restante e o problema aparece em "Pendências de cobertura" no status final.
- Os números do status (documentos, itens, último ID, próximo trecho) devem corresponder exatamente ao que foi emitido.

### Retomada

- Ao receber "continuar", retome exatamente a partir do "Próximo trecho" do último status, mantendo a numeração de IDs e as classificações já usadas.
- Se a sua resposta anterior **não terminou com um bloco de status**, ela foi cortada pela ferramenta. Nesse caso, ao receber "continuar", retome a partir da última linha completa da tabela, reemitindo a linha que ficou incompleta, e não repita as linhas completas.
- Se receber "continuar" depois de uma análise concluída, responda apenas com o bloco **✅ ANÁLISE CONCLUÍDA** novamente.
- Ao processar documentos posteriores, confronte-os com todos os itens já registrados nas respostas anteriores.
