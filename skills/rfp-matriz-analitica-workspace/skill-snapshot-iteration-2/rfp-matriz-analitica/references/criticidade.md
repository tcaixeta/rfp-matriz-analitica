# Criticidade (Severidade × Probabilidade)

A criticidade de cada item resulta de duas avaliações independentes: a **Severidade** do impacto para o proponente e a **Probabilidade** de esse impacto se concretizar **caso o proponente não execute a Ação recomendada**.

### Severidade (impacto para o proponente, se o evento ocorrer)

| Nível | Rótulo | Critério |
|---|---|---|
| 1 | Insignificante | Sem efeito relevante em preço, prazo, escopo, pontuação ou obrigações |
| 2 | Menor | Efeito pequeno, absorvível sem ajustar a proposta |
| 3 | Moderada | Exige ajuste de preço, premissa, esforço ou equipe; perda moderada de pontuação; exposição financeira de cerca de 1–5% do valor estimado do contrato |
| 4 | Maior | Impacto significativo em margem, prazo, escopo ou pontuação; penalidades relevantes; exposição financeira de cerca de 5–25% do valor estimado |
| 5 | Severa | Desclassificação ou inabilitação; exposição financeira ou jurídica ilimitada ou acima de 25% do valor estimado; impossibilidade de atender ou de precificar |

As faixas percentuais só se aplicam quando o valor estimado do contrato for conhecido. Se não for, use o critério qualitativo.

Regras da severidade:
- Avalie a severidade pelo impacto **do próprio item**, isoladamente. Não herde a gravidade de itens relacionados.
- Quando a combinação de vários itens criar um risco maior que cada um isolado (por exemplo: prazo de transição curto + fim do contrato do fornecedor atual + multa sem teto), registre **um único item do tipo Risco para o proponente**. Esse item recebe a severidade combinada e lista os itens que o compõem em IDs relacionados; os itens individuais mantêm a própria severidade.
- Para Contradição, Ambiguidade e Lacuna, a severidade é o impacto da diferença entre as interpretações possíveis ou da informação ausente (por exemplo: a diferença de custo entre 30 e 60 dias de transição).

### Probabilidade (chance de o impacto se concretizar se o item não for tratado)

| Nível | Rótulo | Critério |
|---|---|---|
| 1 | Remota | Só ocorreria em circunstâncias excepcionais |
| 2 | Improvável | Pode ocorrer, mas o documento indica que é pouco provável |
| 3 | Possível | Pode ocorrer; o documento não oferece indícios para mais ou para menos |
| 4 | Provável | Há evidência específica nos documentos de que o impacto tende a ocorrer (por exemplo: multa aplicada automaticamente a cada ocorrência; prazo menor que o necessário para cumprir uma obrigação explícita; o cliente já recusou ou deixou sem resposta um pedido de esclarecimento sobre o tema) |
| 5 | Quase certa | O impacto decorre diretamente do texto, sem depender de interpretação nem de evento incerto (por exemplo: não atender a um critério eliminatório leva à inabilitação; custo fixo explicitamente exigido; informação indispensável ao preço recusada formalmente pelo cliente) |

Regras da probabilidade:
- Estime a probabilidade **somente com base nos documentos do cliente**. Você não conhece a capacidade do proponente; não presuma que ele atende ou não atende.
- **Probabilidade 4 ou 5 exige evidência específica**: cite na Descrição analítica o trecho ou fato dos documentos que a sustenta. Argumentos genéricos ("tende a ser interpretado contra o proponente", "clientes costumam cobrar", "é um setor visado") não bastam; sem evidência específica, use 3.
- Para **Contradição, Ambiguidade e Lacuna**, a probabilidade é a de o proponente sofrer o impacto se seguir uma das interpretações sem esclarecimento. A simples necessidade de esclarecer não justifica 4 ou 5.
- Assim como a severidade, a probabilidade não é herdada de itens relacionados.
- Sempre que a probabilidade for diferente de 3, justifique-a brevemente na Descrição analítica.

### Cálculo da criticidade

**Pontuação = Severidade × Probabilidade**

| Pontuação | Criticidade |
|---|---|
| 1–4 | Baixa |
| 5–9 | Média |
| 10–15 | Alta |
| 16–25 | Crítica |

Regras adicionais:
- Item com **Severidade 5** nunca é classificado abaixo de **Alta**, mesmo que a pontuação seja menor. Impactos severos e improváveis (como responsabilidade ilimitada) precisam de atenção.
- Itens do tipo **Registro de cobertura** e **Oportunidade / diferencial** não recebem Severidade, Probabilidade nem Criticidade. Preencha com "—".
- **Calibragem:** a Criticidade serve para priorizar. Se, ao final de um documento, mais de cerca de um quarto dos itens avaliados estiver como Crítica, revise-os um a um e confira se as regras de efeito em cadeia e de evidência foram aplicadas. Não rebaixe um item só para cumprir proporção: mantenha a classificação que as regras sustentarem.
