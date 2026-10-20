# Taxonomias

Use estes valores exatamente como estão escritos: eles são a base para filtrar e consolidar a matriz.

## Tipo de item (o que o item é)

| Tipo | Definição |
|---|---|
| Requisito funcional / de serviço | O que a solução ou o serviço deve fazer ou entregar |
| Requisito não funcional | Desempenho, disponibilidade, segurança, escalabilidade, usabilidade, conformidade técnica |
| Critério eliminatório / de habilitação | Exigência cujo não atendimento desclassifica ou inabilita o proponente |
| Critério de avaliação / pontuação | Critério e peso usados para pontuar a proposta |
| Instrução de resposta | Formato, template, limite, idioma, forma e local de entrega da proposta |
| Prazo / marco | Data ou prazo do processo ou do projeto |
| SLA / KPI | Nível de serviço ou indicador medido |
| Penalidade / multa / glosa | Sanção financeira ou contratual |
| Obrigação contratual | Garantia, seguro, responsabilidade, PI, confidencialidade, subcontratação, reajuste, pagamento, rescisão |
| Entregável | Artefato ou produto esperado |
| Premissa do cliente | Condição declarada pelo cliente como verdadeira |
| Restrição | Limite imposto (tecnologia, local, equipe, horário, orçamento) |
| Responsabilidade / dependência do cliente | O que cabe ao cliente fornecer ou executar |
| Dado de dimensionamento | Volumetria, ambiente atual, quantidades, horários, localidades |
| Contradição | Conflito entre dois ou mais trechos |
| Ambiguidade | Trecho que admite mais de uma interpretação relevante |
| Lacuna | Informação necessária que não foi localizada, inclusive documento, anexo ou tabela citado pelo cliente e não fornecido (por exemplo: "conforme Anexo IV", "matriz de classificação do Contratante") |
| Risco para o proponente | Exposição técnica, financeira, jurídica, de prazo ou de entrega |
| Requisito implícito | Exigência não escrita, decorrente do contexto. Sempre com Natureza = Inferida |
| Oportunidade / diferencial | Ponto em que o proponente pode se destacar |
| Registro de cobertura | Inventário, regime identificado, trecho não processado ou ilegível, possível conteúdo em imagem não lido, arquivo listado pelo usuário e não anexado |

**Lacuna × Registro de cobertura.** Um documento que o **cliente cita** e não fornece é uma **Lacuna**, com Severidade, Probabilidade e Criticidade, porque afeta a resposta do proponente. O **Registro de cobertura** fica restrito ao que foi ou não foi lido nesta análise (inventário, trechos ilegíveis, imagens não lidas, arquivos que o usuário listou e não anexou) e não recebe criticidade.

Arquivo **listado pelo usuário e não anexado** gera só o Registro de cobertura, mesmo que o cliente cite o documento: o usuário tem o arquivo, então não há o que pedir ao cliente. Não registre uma Lacuna para o mesmo documento.

## Domínio (de que assunto o item trata)

Técnico/Arquitetura · Segurança da Informação/Cyber · Privacidade/Proteção de Dados · Infraestrutura/Cloud · Dados/Analytics · Operação/Serviços · Gestão de Projetos · Transição/Implantação · Comercial/Preço · Financeiro · Jurídico/Contratual · Regulatório/Compliance · Pessoas/Equipe · Qualidade · Continuidade · ESG · Administrativo do processo

Use o domínio predominante. Se um item tiver dois domínios relevantes, informe ambos separados por " / ".

## Obrigatoriedade

| Valor | Regra |
|---|---|
| Mandatório | "deve", "deverá", "obrigatoriamente", "é exigido", "sob pena de", ou equivalente |
| Desejável | "poderá", "preferencialmente", "desejável", "será considerado diferencial", ou equivalente |
| Informativo | Sem caráter de exigência (dados, contexto, premissas) |

Se o verbo for ambíguo, classifique pelo efeito descrito no documento e registre também uma **Ambiguidade**.

## Natureza da evidência

- **Explícita:** o conteúdo está escrito no documento.
- **Inferida:** dedução sua a partir do texto. Explique o raciocínio na Descrição analítica.

## Status de vigência

Vigente · Alterado · Substituído · Duplicado · Em esclarecimento. Informe na coluna IDs relacionados o ID que altera, substitui ou duplica o item.

- **Duplicado:** o item repete o conteúdo de outro, sem informação nova (por exemplo, o questionário pergunta de novo se o proponente tem a certificação já exigida no RFP). Registre-o para manter a rastreabilidade, aponte o original em IDs relacionados e deixe Severidade, Probabilidade e Criticidade com "—".
- Se a repetição acrescenta algo (o cliente recusou um pedido, confirmou um valor antes ambíguo ou mudou o efeito), não é Duplicado: o item é Vigente, com criticidade própria, e o original pode passar a Alterado.

## Ação recomendada

Atender · Precificar · Esclarecer no Q&A · Registrar premissa na proposta · Mitigar · Propor exceção/ressalva · Avaliar Go/No-Go · Nenhuma (informativo)

## Responsável interno sugerido

Bid Manager · Pré-venda/Arquitetura · Segurança/Cyber · Delivery/Operação · Pricing/Financeiro · Jurídico · Compliance · RH/Staffing
