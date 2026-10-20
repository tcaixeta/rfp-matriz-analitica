# Análise da RFP nº 2026-017 — Serviços Gerenciados de SOC e IAM

**Cliente:** Banco Horizonte Fictício S.A.
**Objeto:** serviços gerenciados de SOC (24x7x365) e de IAM
**Valor estimado:** não informado (e não consta em nenhum documento recebido)
**Data da análise:** 18/10/2026
**Base documental:** 4 arquivos efetivamente recebidos (ver inventário). O 5º arquivo listado na solicitação **não foi anexado** e, portanto, **não foi analisado**.

> Convenção de citação: `RFP §x` = PDF da RFP; `AnI §x` = Anexo I (.docx); `Apres. sl.x` = apresentação (.pptx); `Q&A nº x` / `QT-xx` = planilha de Q&A e questionário. Para o PDF, indica-se a página física do arquivo e, entre parênteses, o número impresso no rodapé, porque os dois diferem em uma unidade (a capa não é numerada).

---

## 1. Inventário documental

### 1.1 Documentos listados × documentos recebidos

| # | Arquivo listado | Status | Tipo | Versão/data declarada | Versão/data encontrada no documento | Conteúdo / estrutura | Observações de leitura |
|---|---|---|---|---|---|---|---|
| 1 | RFP-2026-017_Servicos_SOC_IAM.pdf | **Recebido** | RFP | v1.0 — 15/10/2026 | v1.0 — 15/10/2026 (capa e cabeçalho) — confere | 6 páginas físicas: capa; §1–3 (p.2); §4–5 (p.3); §6 (p.4); §7 (p.5); **Anexo III** (p.6) | Páginas 1–5 com texto extraível. **Página 6 é imagem digitalizada** (sem camada de texto): contém o "Anexo III — Declaração de Localização de Dados", lido por inspeção visual. Rodapé numera de "Página 1" a "Página 5" a partir da p.2 física. |
| 2 | Anexo_I_Especificacao_Tecnica.docx | **Recebido** | Anexo técnico | v1.0 — 15/10/2026 | v1.0 — 15/10/2026 (linha de identificação) — confere | Seções 1 a 6: SOC, SLA, IAM, Transição, Equipe, Responsabilidades do Contratante | Sem controle de alterações, comentários ou texto oculto. |
| 3 | Apresentacao_Ambiente_Atual.pptx | **Recebido** | Apresentação (workshop) | 22/10/2026 | 22/10/2026 (slide 1) — confere | 5 slides, nenhum oculto | **O slide 5 tem anotação do apresentador com informação de escopo relevante** (subsidiárias) que não aparece no corpo dos slides. |
| 4 | QA_Rodada1_e_Questionario.xlsx | **Recebido** | Q&A + questionário técnico | 12/11/2026 | 12/11/2026 (coluna "Data" do Q&A) — confere | 4 abas: "Instruções", "Q&A Rodada 1" (6 perguntas), "Questionário Técnico" (QT-01 a QT-06), **"Pesos" (aba oculta)** | A aba oculta "Pesos" traz pesos por item e uma **regra de penalização que não consta na RFP** (ver C-08). |
| 5 | Anexo_IV_Planilha_de_Precos.xlsx | **NÃO RECEBIDO** | Planilha de preços | v1.0 | — | — | Arquivo citado na tabela da solicitação e exigido pela RFP §4.3, mas **não foi anexado**. Nada sobre o seu conteúdo (estrutura de preços, itens, unidades, premissas, critério de cálculo da Nota de Preço) foi analisado ou presumido nesta análise. |

### 1.2 Anexos referenciados pela RFP × anexos disponíveis

| Anexo | Onde é referenciado | Situação |
|---|---|---|
| Anexo I — Especificação Técnica | RFP §2.2 | Recebido (arquivo 2) |
| Anexo II | Não é referenciado em nenhum documento | **Lacuna de numeração**: não se sabe se existe. Confirmar com o Banco. |
| Anexo III — Declaração de Localização de Dados | Não é referenciado no corpo da RFP; aparece só como p.6 do PDF (imagem) | Recebido apenas como imagem embutida no PDF; não há versão editável. Sob pena de inabilitação. |
| Anexo IV — Planilha de Preços | RFP §4.3 | **Não recebido** (arquivo 5) |
| "Questionário técnico (planilha anexa)" | RFP §4.4 | Recebido (aba do arquivo 4) |
| Matriz de classificação de criticidade do Contratante | AnI §2.4 | **Não fornecida** |

### 1.3 Observações sobre o inventário

- **I-01 — Anexo IV ausente (bloqueante para a proposta comercial).** Sem a planilha modelo não é possível estruturar o preço, validar unidades de cobrança nem simular a Nota de Preço (peso de 40%). **Ação:** obter o arquivo no portal de fornecedores ou com o solicitante e reprocessar a análise com ele.
- **I-02 — Datas posteriores à data desta análise.** A apresentação (22/10/2026) e o Q&A (12/11/2026) têm datas posteriores à data de hoje (18/10/2026). Ou o cenário é simulado, ou há erro de data nos documentos ou na solicitação. Esta análise trata o Q&A como vigente e confirma as datas na seção 2.
- **I-03 — O Anexo III só existe como imagem digitalizada.** Ele não aparece em buscas de texto e pode passar despercebido. Também não há versão editável para assinatura: será preciso reproduzir o texto em papel timbrado ou pedir o modelo ao Banco.
- **I-04 — Informação de escopo nas anotações do slide 5.** Ela foi capturada na extração, mas pode não ter sido comunicada formalmente a todos os proponentes (ver C-04).

---

## 2. Ficha-resumo do processo

| Item | Conteúdo | Fonte |
|---|---|---|
| Objeto | SOC gerenciado 24x7x365 + IAM | RFP §2.1 |
| Porte declarado | "aproximadamente 4.500 colaboradores" (**conflitante**, ver C-04) | RFP §2.1 |
| Regulação | Resolução CMN nº 4.893/2021 | RFP §1.2; QT-04 |
| Vigência | 36 meses, prorrogável por iguais períodos mediante acordo | RFP §7.1 |
| Reajuste | Anual, IPCA | RFP §7.2 |
| Pagamento | Até 60 dias após o aceite da NF | RFP §7.3 |
| Julgamento | Técnica 60% + Preço 40%; corte técnico em 70%; desempate pelo menor preço | RFP §6.1–6.4 |
| Entrega | Exclusivamente pelo portal de fornecedores, em português | RFP §4.1 |
| Limite da proposta técnica | 40 páginas, excluídos os anexos | RFP §4.2 |
| Subcontratação | Vedada, total ou parcial | RFP §7.7 |
| Início dos serviços | 01/02/2027 | RFP §3.1 |

### 2.1 Cronograma consolidado (após o Q&A)

| Etapa | Data original (RFP §3.1) | Data vigente | Fonte da alteração |
|---|---|---|---|
| Publicação da RFP | 15/10/2026 | 15/10/2026 | — |
| Workshop do ambiente | 22/10/2026 | 22/10/2026 | — |
| Prazo final para perguntas | 05/11/2026 | 05/11/2026 | — |
| Divulgação das respostas | 12/11/2026 | 12/11/2026 (Rodada 1 publicada) | — |
| **Entrega das propostas** | 20/11/2026, 18h | **27/11/2026, 18h** | Q&A nº 1 |
| Assinatura do contrato | não informada | **não informada** | — |
| Fim do contrato do SIEM legado | — | 31/01/2027, sem prorrogação | Apres. sl.3 |
| Início previsto dos serviços | 01/02/2027 | 01/02/2027 | — |

---

## 3. Matriz de requisitos

Legenda de tipo: **H** = habilitação (eliminatório); **O** = obrigatório; **D** = desejável; **C** = comercial/contratual; **F** = formal/entrega.

| ID | Requisito | Tipo | Fonte | Observação analítica |
|---|---|---|---|---|
| R-01 | Certificado ISO/IEC 27001 vigente, emitido por organismo acreditado, com escopo que inclua os serviços de SOC | H | RFP §5.1(a); QT-01 (obrigatório, peso 3) | Verificar se o escopo do certificado cita SOC explicitamente. |
| R-02 | No mínimo 3 atestados de SOC para instituições financeiras, cada um com ambiente de ≥2.000 usuários | H | RFP §5.1(b) | Não está claro se o limite vale para cada atestado ou para a soma; o texto sugere "cada um". Atestados de IAM não são exigidos. |
| R-03 | SOC localizado em território nacional (com comprovação) | H | RFP §5.1(c); Q&A nº 2 | Confirmado pelo Q&A. |
| R-04 | Equipe técnica "devidamente certificada" | H | RFP §5.2; QT-06 | Critério vago: não diz quais certificações nem quantas (ver C-10). |
| R-05 | Declaração de Localização de Dados (Anexo III) assinada pelo representante legal | H | RFP p.6 (imagem) | Todos os dados, **inclusive os logs**, armazenados e processados exclusivamente no Brasil durante toda a vigência. Conflita com AnI §1.2 (C-03). |
| R-06 | Monitoramento contínuo 24x7x365 | O | RFP §2.1; AnI §1.1 | — |
| R-07 | Fornecimento da solução de SIEM pelo proponente (nuvem pública admitida) | O | AnI §1.2 | O licenciamento e a infraestrutura do SIEM ficam por conta do proponente; o dimensionamento depende do EPS, que não foi informado (C-07). |
| R-08 | Retenção de logs de ≥12 meses (online, segundo QT-03) e de 5 anos para auditoria | O | AnI §1.3, §1.6; QT-03 | Duas regras de retenção sem distinção clara entre armazenamento quente e frio (C-05). |
| R-09 | SIEM integrado a "todos os ativos relevantes" | O | AnI §1.4 | Escopo indefinido (C-07). Ambiente: 850 servidores, 2 DCs, 2 nuvens públicas (Apres. sl.2). |
| R-10 | Resposta a incidentes: contenção, erradicação e relatório pós-incidente | O | AnI §1.5 | O escopo de resposta parece incluir atuação no ambiente do cliente, o que pesa sobre a responsabilidade ilimitada de §7.5. |
| R-11 | SLA: início do tratamento de incidente crítico em ≤15 min | O | AnI §2.1 | Depende da matriz de criticidade do Contratante, não fornecida (AnI §2.4). |
| R-12 | SLA: disponibilidade mensal do SIEM ≥99,9% | O | AnI §2.2 | Equivale a ~43 min de indisponibilidade por mês. |
| R-13 | Relatório mensal até o 5º dia útil | O | AnI §2.3 | — |
| R-14 | Ciclo de vida de identidades; revogação em ≤24h após o desligamento | O | AnI §3.1 | O ambiente atual é AD + scripts internos (Apres. sl.3), o que implica implantação de ferramenta de IGA. O dimensionamento de usuários está em conflito (C-04). |
| R-15 | MFA para 100% dos usuários privilegiados | O | AnI §3.2 | — |
| R-16 | Recertificação trimestral de acessos | O | AnI §3.3 | — |
| R-17 | Cofre de senhas privilegiadas (PAM) | **D** | AnI §3.4 | Hoje não há PAM (Apres. sl.3). Avaliar oferecer como item opcional. |
| R-18 | Transição concluída em 30 dias (RFP) **ou** 60 dias (Anexo I) | O | RFP §3.2 × AnI §4.1 | Conflito direto (C-01). |
| R-19 | Operação em paralelo com o fornecedor atual durante a transição, sem custo adicional | O | AnI §4.2 | Custo de sobreposição a ser absorvido no preço. |
| R-20 | Coordenador com CISSP, dedicado exclusivamente ao contrato | O | AnI §5.1 | Custo fixo relevante. |
| R-21 | Analistas N1 presenciais na sede (São Paulo/SP) em horário comercial | O → **flexibilizado** | AnI §5.2; Q&A nº 6 | O Q&A permite trabalho remoto desde que em território nacional (C-06). |
| R-22 | Migração de 24 meses de logs históricos do SIEM legado | **Indefinido** | Apres. sl.5 | Aparece só como "expectativa" na apresentação; não está na RFP nem no Anexo I (C-09). |
| R-23 | Visão unificada de riscos para a diretoria | **Indefinido** | Apres. sl.5 | Idem. |
| R-24 | Reduzir os falsos positivos de 70% para 10% no 1º trimestre | **Indefinido** | Apres. sl.4 | Apresentada como "meta"; não é SLA contratual, mas pode virar expectativa de desempenho (C-09). |
| R-25 | Proposta técnica com no máximo 40 páginas | F | RFP §4.2 | — |
| R-26 | Proposta comercial no modelo do Anexo IV | F | RFP §4.3 | **Anexo IV não recebido** (I-01). |
| R-27 | Questionário técnico integralmente preenchido; "todas as abas" são obrigatórias, sob pena de desclassificação | F | RFP §4.4; aba "Instruções" | A expressão "todas as abas" é ambígua, já que o arquivo também tem a aba de Q&A e uma aba oculta (C-08). |
| R-28 | Seguro de responsabilidade civil cibernética "em valor compatível" | C | RFP §7.6 | Valor não definido. |
| R-29 | Confidencialidade por 5 anos após o término | C | RFP §7.8 | — |
| R-30 | Aderência à Resolução CMN 4.893/2021 | O | RFP §1.2; QT-04 (obrigatório, peso 3) | Interage com a localização de dados e o uso de nuvem (C-03). |
| R-31 | Integração nativa com SOAR | D | QT-02 (não obrigatório, peso 1) | Penalidade oculta de -2 pontos se a resposta for "Não atende" (C-08). |
| R-32 | Serviço de threat intelligence | D | QT-05 (não obrigatório, peso 2) | Idem. |

---

## 4. Conflitos e inconsistências entre documentos

A RFP **não define uma ordem de precedência** entre o edital, os anexos, a apresentação e o Q&A. Quando o Q&A trata do ponto, ele é assumido como prevalente por ser o esclarecimento formal mais recente. Fora isso, o conflito fica em aberto.

| ID | Tema | Fonte A | Fonte B | Impacto | Tratamento recomendado |
|---|---|---|---|---|---|
| **C-01** | Prazo de transição | RFP §3.2: **30 dias** da assinatura | AnI §4.1: **60 dias** da assinatura | **Alto.** Define o plano de transição (10 pontos na Nota Técnica) e o custo de operação em paralelo (AnI §4.2). Agrava o quadro o fim do SIEM legado em 31/01/2027 sem prorrogação, sem data de assinatura conhecida. | Pedir esclarecimento. Na falta de resposta, planejar com o prazo mais restritivo (30 dias) e registrar a premissa na proposta. |
| **C-02** | Retenção de logs | AnI §1.3: mínimo de **12 meses** (QT-03: "online") | AnI §1.6: **5 anos** para auditoria | **Alto** em custo de armazenamento. | Assumir 12 meses online + 5 anos em arquivamento (frio), em território nacional, e explicitar a premissa. |
| **C-03** | Localização de dados e SIEM em nuvem | AnI §1.2: SIEM em nuvem pública, "em região de **livre escolha** do proponente" | Anexo III (RFP p.6): todos os dados, **inclusive logs**, armazenados e processados **exclusivamente no Brasil**, sob pena de inabilitação; Q&A nº 2 reforça a localização nacional do SOC | **Crítico.** Escolher região fora do Brasil leva à inabilitação. A liberdade do AnI §1.2 é, na prática, anulada pelo Anexo III. | Projetar o SIEM só com região brasileira. Confirmar que backups, réplicas de DR, telemetria do fabricante e processamento de analytics/IA também ficam no Brasil. |
| **C-04** | Número de usuários (dimensionamento) | RFP §2.1: ~**4.500** colaboradores; Q&A nº 5: considerar **5.000** | Apres. sl.2: **6.200** usuários ativos; anotação do sl.5: subsidiárias Horizonte Seguros e Horizonte Investimentos, "cerca de **900** usuários adicionais", "também deverão ser incluídas no escopo" | **Crítico** para o preço de IAM e de licenças. A diferença vai de 5.000 a 7.100 (+42%). A inclusão das subsidiárias está apenas numa anotação do apresentador e muda o objeto (outras pessoas jurídicas). | Precificar com 5.000 (Q&A, formal), declarando a premissa e um preço unitário por usuário adicional. Pedir confirmação formal sobre as subsidiárias (escopo, contratante, faturamento). |
| **C-05** | Base de retenção × migração histórica | AnI §1.3/§1.6 (retenção a partir do início) | Apres. sl.5: migrar **24 meses** de logs históricos | Médio/alto. Volume desconhecido, formato do SIEM legado desconhecido e prazo curto (o legado acaba em 31/01/2027). | Tratar como item opcional/precificado à parte ou como premissa, até confirmação formal. |
| **C-06** | Presença dos analistas N1 | AnI §5.2: presencial na sede em SP, em horário comercial | Q&A nº 6: remoto permitido, desde que no Brasil | Baixo (o Q&A resolve e reduz custo). | Adotar o Q&A e citá-lo na proposta. |
| **C-07** | Dimensionamento do SIEM | AnI §1.4: integrar "todos os ativos relevantes" | Q&A nº 3: EPS "informado somente ao proponente vencedor" | **Alto.** Não dá para dimensionar licença, ingestão e armazenamento do SIEM (cobrados por EPS/GB/dia) nem a equipe. Referências indiretas: ~1.200 alertas/dia, 850 servidores, 2 DCs, 2 nuvens (Apres. sl.2 e 4). | Declarar uma faixa de EPS como premissa, com mecanismo de ajuste de preço por faixa excedente. Pedir ao menos a ordem de grandeza ou o volume em GB/dia. |
| **C-08** | Regras de pontuação ocultas e soma dos critérios | RFP §6.2: Nota Técnica de **no máximo 60 pontos** | Os critérios de RFP §6.2 somam **65** (20+20+15+10). A aba oculta "Pesos" acrescenta pesos por item e a regra: "requisitos não obrigatórios respondidos como 'Não atende' reduzem a Nota Técnica em 2 pontos cada" | **Alto.** (i) Não se sabe se o corte de 70% é sobre 60 (42 pts) ou 65 (45,5 pts). (ii) A penalidade oculta tira até 4 pontos (QT-02 SOAR e QT-05 threat intel) e **não está prevista na RFP**. (iii) Os pesos do questionário não aparecem nos critérios da RFP. | Pedir esclarecimento sobre o total e sobre a validade da aba "Pesos". Responder QT-02 e QT-05 como "Atende" ou "Parcial" sempre que for tecnicamente defensável. |
| **C-09** | Expectativas da apresentação fora do escopo formal | Apres. sl.4–5: meta de 10% de falsos positivos no 1º trimestre, migração de 24 meses de logs, visão unificada de riscos | RFP e Anexo I não têm esses itens | Médio. Risco de expectativa não contratada e de avaliação subjetiva na "Metodologia do SOC" (20 pts). | Tratar na proposta técnica como diferencial ou plano de tuning, sem assumir a meta como SLA. |
| **C-10** | Certificações exigidas | RFP §5.2: equipe "devidamente certificada" (habilitação) | AnI §5.1: só o CISSP do coordenador é especificado; QT-06: "certificações reconhecidas pelo mercado" | Médio. Critério de inabilitação subjetivo. | Apresentar uma matriz de certificações da equipe nominada. Pedir um critério objetivo. |
| **C-11** | Subcontratação × SIEM em nuvem e PAM | RFP §7.7: subcontratação vedada, total ou parcial | AnI §1.2: SIEM em nuvem pública (infraestrutura de terceiro) | Médio. Uso de hyperscaler, licenças SaaS de SIEM/IGA/PAM ou parceiros de resposta a incidentes podem ser lidos como subcontratação. | Pedir confirmação de que o fornecimento de software/infraestrutura de terceiros não conta como subcontratação. |
| **C-12** | Data de assinatura × transição × fim do legado | RFP §3.1: início em 01/02/2027; §3.2: transição em 30 dias | Apres. sl.3: SIEM legado encerra em 31/01/2027, sem prorrogação; AnI §4.2: operar em paralelo | Alto. Se o contrato for assinado depois de ~01/01/2027, o prazo de 30 dias ultrapassa a data de corte do legado e não sobra janela de operação paralela. A documentação do ambiente chega até 10 dias após a assinatura (AnI §6.2), o que consome 1/3 do prazo de transição. | Pedir a data prevista de assinatura. Condicionar o cronograma de transição à entrega da documentação e dos acessos (AnI §6.1–6.2). |

---

## 5. Riscos

| ID | Risco | Fonte | Severidade | Comentário / mitigação |
|---|---|---|---|---|
| RK-01 | **Responsabilidade integral e ilimitada** por danos decorrentes de incidentes de segurança no ambiente do Contratante | RFP §7.5 | **Crítica** | Num serviço de SOC, incidentes são esperados. Sem limite, a exposição não é segurável. Propor um teto (por exemplo, múltiplo do valor anual) e excluir danos indiretos e incidentes causados por falhas do Contratante. |
| RK-02 | **Multa de 10% do valor mensal por ocorrência** de qualquer SLA, sem teto | RFP §7.4; Q&A nº 4 ("condições do item 7 permanecem inalteradas") | **Crítica** | Bastam 10 ocorrências no mês para zerar a receita. A classificação de criticidade é definida unilateralmente pelo Contratante (AnI §2.4). Propor teto mensal/anual, gradação por severidade e período de carência na transição. |
| RK-03 | Não conformidade de localização de dados (Anexo III) | RFP p.6; AnI §1.2 | **Crítica** | Inabilitação e risco regulatório. Ver C-03. |
| RK-04 | Subdimensionamento de usuários (5.000 × 7.100) e de EPS | C-04, C-07 | Alta | Preço inexequível ou pouco competitivo. Precificar com premissas explícitas e preços unitários de excedente. |
| RK-05 | Prazo de transição e data de corte do SIEM legado | C-01, C-12 | Alta | Risco de lacuna de monitoramento a partir de 01/02/2027, que pode ser enquadrada como descumprimento de SLA (RK-02). |
| RK-06 | Seguro cibernético "em valor compatível" | RFP §7.6 | Média | Valor indefinido. Combinado com RK-01, pode exigir apólice inviável. |
| RK-07 | Penalidades ocultas no questionário e pontuação inconsistente | C-08 | Média | Pode levar à desclassificação técnica (corte de 70%) por poucos pontos. |
| RK-08 | Coordenador CISSP com dedicação exclusiva + equipe 24x7 | AnI §5.1; RFP §2.1 | Média | Custo fixo elevado. Confirmar se o coordenador precisa estar alocado em tempo integral desde a transição. |
| RK-09 | Operação em paralelo sem custo e documentação tardia | AnI §4.2, §6.2 | Média | Custo absorvido e dependência de insumos do Contratante. |
| RK-10 | Pagamento em 60 dias após o aceite da NF | RFP §7.3 | Média | Impacto no fluxo de caixa, que se soma ao custo de transição pago antecipadamente. |
| RK-11 | Escopo implícito (subsidiárias, migração histórica, painel de riscos, meta de falsos positivos) | Apres. sl.4–5 e anotações | Média | Pode haver escopo não pago (*scope creep*). Delimitar o escopo na proposta. |
| RK-12 | Ausência do Anexo IV | I-01 | Alta (processual) | Proposta comercial fora do modelo leva a risco de desclassificação. |

---

## 6. Informações faltantes

1. **Anexo IV — Planilha de Preços** (não recebido; exigido pela RFP §4.3).
2. Anexo II: existência e conteúdo.
3. Volumetria (EPS e/ou GB/dia) e inventário de ativos "relevantes".
4. Matriz de classificação de criticidade dos incidentes (AnI §2.4).
5. Número definitivo de usuários e confirmação formal sobre as subsidiárias.
6. Data prevista de adjudicação e de assinatura do contrato.
7. Fórmula da Nota de Preço (a RFP só informa o peso de 40%).
8. Valor mínimo do seguro cibernético.
9. Volume e formato dos 24 meses de logs históricos, e se a migração faz parte do escopo.
10. Lista de certificações aceitas para fins de habilitação (RFP §5.2).
11. Ordem de precedência entre RFP, anexos, apresentação e Q&A.
12. Valor estimado do contrato (não informado).

---

## 7. Perguntas de esclarecimento sugeridas

> O prazo para perguntas era 05/11/2026 (RFP §3.1) e a Rodada 1 já foi respondida em 12/11/2026. Uma nova rodada depende de o Banco abri-la. Se isso não acontecer, as respostas abaixo devem virar **premissas explícitas** na proposta.

1. Qual prazo de transição prevalece: 30 dias (RFP §3.2) ou 60 dias (Anexo I §4.1)? Qual é a data prevista de assinatura?
2. A "livre escolha de região" do Anexo I §1.2 está revogada pelo Anexo III? Backups e DR também precisam ficar no Brasil?
3. As subsidiárias Horizonte Seguros e Horizonte Investimentos (~900 usuários, segundo a apresentação) fazem parte do escopo? O Q&A nº 5 (5.000 usuários) já as inclui?
4. Os 12 meses de retenção (§1.3) devem ser online e os 5 anos (§1.6) podem ser em arquivamento?
5. A migração de 24 meses de logs históricos faz parte do escopo obrigatório?
6. A Nota Técnica máxima é 60 ou 65 pontos? A regra da aba "Pesos" (-2 pontos por "Não atende" em item não obrigatório) vale? Qual é a fórmula da Nota de Preço?
7. O uso de nuvem pública e de licenças SaaS de terceiros conta como subcontratação (§7.7)?
8. É possível informar uma faixa de EPS ou o volume diário de logs para o dimensionamento?
9. Qual o valor mínimo do seguro (§7.6)? O Banco aceitaria limitar a responsabilidade (§7.5) e as multas (§7.4)?
10. Existe um Anexo II?

---

## 8. Checklist de entrega

| Item | Exigência | Fonte | Situação |
|---|---|---|---|
| Proposta técnica (≤40 pág., em português) | Obrigatória | RFP §4.1–4.2 | A elaborar |
| Proposta comercial no modelo do Anexo IV | Obrigatória | RFP §4.3 | **Bloqueada: Anexo IV não recebido** |
| Questionário técnico (todas as linhas; "todas as abas") | Obrigatória, sob pena de desclassificação | RFP §4.4; aba "Instruções" | A preencher. Esclarecer o que se espera das abas "Q&A" e "Pesos". |
| Certificado ISO/IEC 27001 (escopo SOC) | Habilitação | RFP §5.1(a) | Verificar escopo e validade |
| 3 atestados de SOC em IF com ≥2.000 usuários | Habilitação | RFP §5.1(b) | Levantar |
| Comprovação de SOC no Brasil | Habilitação | RFP §5.1(c) | Levantar |
| Comprovação de equipe certificada (inclui CISSP do coordenador) | Habilitação / obrigatório | RFP §5.2; AnI §5.1 | Levantar |
| Anexo III assinado pelo representante legal | Habilitação | RFP p.6 | Reproduzir o texto e colher a assinatura |
| Envio pelo portal até **27/11/2026, 18h** | Obrigatória | Q&A nº 1 | — |

---

## 9. Síntese para decisão (go/no-go)

**Pontos favoráveis:** objeto claro (SOC + IAM); prazo de proposta estendido; N1 remoto permitido; contrato de 36 meses com reajuste por IPCA; ambiente com dores evidentes (70% de falsos positivos, sem PAM, IAM baseado em scripts) que abrem espaço para diferenciação técnica.

**Pontos impeditivos ou de alta atenção:**
- Cláusulas contratuais de risco desproporcional: responsabilidade ilimitada (RK-01) e multa de 10% por ocorrência sem teto (RK-02), mantidas pelo Q&A nº 4.
- Localização de dados obrigatória no Brasil (Anexo III), em contradição com o Anexo I.
- Dimensionamento incerto (usuários de 5.000 a 7.100; EPS não informado).
- Transição curta com data de corte rígida do SIEM legado.
- **Anexo IV ausente:** a análise comercial não foi feita.

**Recomendação:** a participação é viável só se: (a) o Anexo IV for obtido; (b) a proposta trouxer premissas explícitas de dimensionamento (usuários, EPS, retenção, escopo das subsidiárias e da migração) e ressalvas sobre §7.4 e §7.5, desde que isso não leve à desclassificação; (c) a arquitetura do SIEM for 100% em região brasileira. Depois de obter o Anexo IV, reprocessar a análise para incluir a parte comercial.
