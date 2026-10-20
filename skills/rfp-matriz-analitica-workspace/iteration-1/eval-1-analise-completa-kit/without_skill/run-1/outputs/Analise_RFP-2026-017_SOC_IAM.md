# Análise da RFP nº 2026-017 — Serviços Gerenciados de SOC e IAM

**Cliente:** Banco Horizonte Fictício S.A.
**Objeto:** serviços gerenciados de SOC (24x7x365) e de IAM
**Valor estimado:** não informado pelo cliente (nenhum documento traz valor de referência)
**Documentos analisados:** 4 arquivos (lista na seção 1)
**Data da análise:** 17/10/2026 (data do sistema). Observação: o pacote contém documentos com datas posteriores (workshop de 22/10/2026 e Q&A de 12/11/2026). Por isso a análise segue a **cronologia interna dos documentos** e considera o Q&A de 12/11/2026 como a informação mais recente.

> Todas as referências seguem o formato `[Documento, item/página]`. Siglas usadas: **RFP** = PDF principal; **AT** = Anexo I (Especificação Técnica, .docx); **APR** = Apresentação do Ambiente Atual (.pptx); **QA** = planilha de Q&A e Questionário (.xlsx).

---

## 1. Inventário dos documentos

| # | Arquivo | Tipo | Versão/Data declarada | Estrutura encontrada | Conteúdo relevante fora do texto principal | Situação da leitura |
|---|---|---|---|---|---|---|
| 1 | RFP-2026-017_Servicos_SOC_IAM.pdf | RFP | v1.0 — 15/10/2026 | 6 páginas físicas (capa + "Página 1" a "Página 5"); seções 1 a 7 | **A página física 6 ("Página 5") é uma imagem digitalizada, sem camada de texto:** é o *Anexo III — Declaração de Localização de Dados*. Foi lida visualmente porque a extração de texto não a captura. | Completa (a pág. 6 foi lida como imagem) |
| 2 | Anexo_I_Especificacao_Tecnica.docx | Anexo técnico | v1.0 — 15/10/2026 | 6 seções: SOC, SLA, IAM, Transição, Equipe, Responsabilidades do Contratante | Sem comentários, sem controle de alterações e sem texto oculto. Os metadados de criação (2013, autor "python-docx") vêm do modelo do arquivo e não são relevantes. | Completa |
| 3 | Apresentacao_Ambiente_Atual.pptx | Apresentação (workshop) | 22/10/2026 | 5 slides, nenhum oculto | **Há uma nota do apresentador no slide 5 que amplia o escopo** (subsidiárias, cerca de 900 usuários a mais). Essa nota não aparece nos slides projetados. | Completa (incluindo as notas) |
| 4 | QA_Rodada1_e_Questionario.xlsx | Q&A e questionário | 12/11/2026 | 4 abas: "Instruções", "Q&A Rodada 1" (6 perguntas), "Questionário Técnico" (QT-01 a QT-06) e **"Pesos" (aba oculta)** | **A aba oculta "Pesos"** traz pesos por requisito e uma **regra de penalização que não consta da RFP**. | Completa (incluindo a aba oculta) |

### 1.1 Documentos citados e não recebidos

| Documento | Onde é citado | Situação |
|---|---|---|
| Anexo II | Não é citado. Existe uma lacuna na numeração: há Anexos I, III e IV. | **Ausente.** É preciso confirmar se existe. |
| Anexo III — Declaração de Localização de Dados | Não é citado no corpo da RFP. Aparece apenas como imagem na pág. 6 do PDF. | Recebido só em imagem digitalizada, sem versão editável. É exigido "sob pena de inabilitação". |
| Anexo IV — Planilha de Preços | [RFP, 4.3] | **Ausente.** Sem ele não é possível montar a proposta comercial. |
| Matriz de classificação de criticidade do Contratante | [AT, 2.4] | **Ausente.** O SLA de 15 minutos depende dessa matriz. |
| Minuta de contrato | Implícita em [RFP, 7] | Ausente. As cláusulas estão só resumidas no item 7. |
| Documentação técnica do ambiente | [AT, 6.2]: será entregue "até 10 dias após a assinatura" | Só será entregue depois da assinatura do contrato. |

### 1.2 Ordem de precedência adotada

Nenhum documento define qual prevalece em caso de conflito. Esta análise adota a seguinte hierarquia, que deve ser confirmada com o cliente:
1. respostas formais do Q&A (12/11/2026, a mais recente);
2. corpo da RFP;
3. Anexo I;
4. apresentação do workshop, que serve só como informação e não é vinculante, sobretudo no caso das notas do apresentador.

---

## 2. Linha do tempo do processo

| Marco | Data | Fonte | Observação |
|---|---|---|---|
| Publicação da RFP | 15/10/2026 (qui) | [RFP, 3.1] | — |
| Workshop do ambiente | 22/10/2026 (qui) | [RFP, 3.1]; [APR, slide 1] | — |
| Prazo para perguntas | 05/11/2026 (qui) | [RFP, 3.1] | **Já encerrado** na data do Q&A. Não há previsão de 2ª rodada. |
| Divulgação das respostas | 12/11/2026 (qui) | [RFP, 3.1]; [QA, Q&A Rodada 1] | Cumprido. |
| **Entrega das propostas** | ~~20/11/2026~~ → **27/11/2026 (sex), até 18h** | [RFP, 3.1] alterado por [QA, nº 1] | A prorrogação consta só da planilha de Q&A. Não houve nova versão da RFP. |
| Fim do contrato do SIEM legado | 31/01/2027 (dom), **sem prorrogação** | [APR, slide 3] | Marco crítico para a transição. |
| Início previsto dos serviços | 01/02/2027 (seg) | [RFP, 3.1] | Restam 66 dias corridos entre a entrega das propostas e o início, incluindo o período de festas de fim de ano. |
| Conclusão da transição | 30 dias **ou** 60 dias após a assinatura | [RFP, 3.2] x [AT, 4.1] | **Conflito** (ver C-03). A data de assinatura não foi informada. |

**Leitura do cronograma.** Para o serviço começar em 01/02/2027, a assinatura teria de ocorrer até cerca de 02/01/2027 (transição de 30 dias) ou até cerca de 03/12/2026 (transição de 60 dias). A segunda hipótese fica a apenas 6 dias da entrega das propostas, o que é irrealista. Além disso, o SIEM legado termina em 31/01/2027 sem prorrogação. Assim, qualquer atraso deixa o Banco sem monitoramento e torna impossível a "operação em paralelo com o fornecedor atual" [AT, 4.2] depois dessa data.

---

## 3. Matriz analítica de requisitos

Legenda:
- **Tipo:** HAB = habilitação (eliminatório), DSC = desclassificatório, TEC = técnico, SLA = nível de serviço, COM = comercial/contratual, PRZ = prazo, FOR = forma de apresentação.
- **Natureza:** O = obrigatório; D = desejável.
- **Risco:** A = alto, M = médio, B = baixo.

### 3.1 Forma de apresentação e habilitação

| ID | Requisito | Fonte | Tipo | Nat. | Risco | Observações / ação |
|---|---|---|---|---|---|---|
| R-01 | Proposta em português, enviada exclusivamente pelo portal de fornecedores | [RFP, 4.1] | FOR | O | B | Confirmar o cadastro no portal com antecedência. |
| R-02 | Proposta técnica de no máximo 40 páginas, sem contar os anexos | [RFP, 4.2] | FOR | O | M | A RFP não define a consequência de exceder o limite. Planejar um texto enxuto. |
| R-03 | Proposta comercial no modelo do Anexo IV | [RFP, 4.3] | FOR | O | **A** | **O Anexo IV não foi recebido** (ver P-01). |
| R-04 | Questionário técnico integralmente preenchido | [RFP, 4.4]; [QA, Instruções A3] | DSC | O | **A** | A aba Instruções diz: "todas as abas" são obrigatórias e questionários incompletos serão desclassificados. Não está claro o que deve ser preenchido nas abas "Q&A" e "Pesos" (ver P-09). |
| R-05 | Certificado ISO/IEC 27001 vigente, emitido por organismo acreditado, com escopo que inclua os serviços de SOC | [RFP, 5.1a]; [QA, QT-01] | HAB | O | M | Conferir o escopo e a validade do certificado. A ISO não é exigida para IAM. |
| R-06 | No mínimo 3 atestados de SOC prestado a instituições financeiras com 2.000 usuários ou mais | [RFP, 5.1b] | HAB | O | M | Levantar os atestados disponíveis. Não basta qualquer atestado de SOC: tem de ser de instituição financeira. |
| R-07 | Comprovação de SOC localizado em território nacional | [RFP, 5.1c]; [QA, nº 2] | HAB | O | M | O Q&A confirma que não é permitido operar o SOC a partir do exterior. |
| R-08 | Equipe técnica "devidamente certificada" | [RFP, 5.2]; [QA, QT-06] | HAB | O | M | O critério é **subjetivo**: não há lista de certificações (ver P-10). |
| R-09 | Anexo III, Declaração de Localização de Dados, assinada pelo representante legal | [RFP, pág. 6, imagem] | HAB | O | **A** | O descumprimento leva à inabilitação. O anexo **conflita com AT 1.2** (ver C-04) e não é citado no corpo da RFP. |

### 3.2 Requisitos técnicos — SOC

| ID | Requisito | Fonte | Tipo | Nat. | Risco | Observações / ação |
|---|---|---|---|---|---|---|
| R-10 | Monitoramento contínuo 24x7x365 | [RFP, 2.1]; [AT, 1.1] | TEC | O | M | Dimensionar os turnos. Hoje o ambiente gera cerca de 1.200 alertas/dia, com 70% de falsos positivos [APR, slide 4]. |
| R-11 | Fornecimento da solução de SIEM, que pode estar em nuvem pública "em região de livre escolha" | [AT, 1.2] | TEC | O | **A** | Conflita com o Anexo III e com a Res. CMN 4.893/2021 (ver C-04). O custo de licenças/consumo depende do volume de EPS, que não foi informado (ver P-03). |
| R-12 | Retenção mínima de logs por 12 meses | [AT, 1.3]; [QA, QT-03: "online"] | TEC | O | **A** | Conflita com R-14 (ver C-05). |
| R-13 | SIEM integrado a "todos os ativos relevantes" | [AT, 1.4] | TEC | O | **A** | O escopo não está definido. Ambiente: 850 servidores, 2 data centers e 2 nuvens públicas [APR, slide 2]. Pelo [QA, nº 3], o EPS só será informado ao vencedor. |
| R-14 | Logs mantidos por 5 anos para fins de auditoria | [AT, 1.6] | TEC | O | **A** | Impacto relevante em armazenamento ao longo de 36 meses. Não está definido se o armazenamento pode ser frio/offline. |
| R-15 | Resposta a incidentes: contenção, erradicação e relatório pós-incidente | [AT, 1.5] | TEC | O | M | Definir os limites: a resposta é remota (por VPN, [AT, 6.1]) ou inclui atuação presencial? |
| R-16 | Migração de 24 meses de logs históricos do SIEM legado | [APR, slide 5] | TEC | ? | **A** | **Não consta da RFP nem do AT.** O volume é desconhecido e o SIEM legado se encerra em 31/01/2027 (ver C-06). |
| R-17 | Visão unificada de riscos para a diretoria | [APR, slide 5] | TEC | ? | M | É uma expectativa nova, ausente da RFP e do AT. Pode ser atendida com um dashboard executivo. Esclarecer se é obrigatória. |
| R-18 | Reduzir os falsos positivos a 10% no 1º trimestre de operação | [APR, slide 4] | TEC/SLA | ? | **A** | É uma "meta" apresentada no workshop. Se virar SLA contratual, combinada com a multa do item 7.4, gera risco elevado (ver P-12). |
| R-19 | Integração nativa com SOAR | [QA, QT-02] | TEC | D | M | Não obrigatório, mas a aba oculta "Pesos" penaliza "Não atende" em 2 pontos (ver C-08). |
| R-20 | Serviço de threat intelligence | [QA, QT-05] | TEC | D | M | Mesma situação de R-19. |
| R-21 | Aderência à Resolução CMN nº 4.893/2021 | [RFP, 1.2]; [QA, QT-04] | TEC/COM | O | **A** | A norma rege a contratação de processamento, armazenamento e nuvem. Implica, entre outras coisas, permitir acesso ao Banco Central e apoiar as comunicações regulatórias do Banco. Tem relação direta com a localização dos dados (C-04). |

### 3.3 Níveis de serviço (SLA)

| ID | Requisito | Fonte | Tipo | Nat. | Risco | Observações / ação |
|---|---|---|---|---|---|---|
| R-22 | Início do tratamento de incidentes críticos em no máximo 15 minutos | [AT, 2.1] | SLA | O | **A** | A criticidade segue uma matriz do Contratante que não foi fornecida [AT, 2.4]. Cada descumprimento gera multa de 10% do valor mensal [RFP, 7.4]. |
| R-23 | Disponibilidade mensal mínima de 99,9% do SIEM | [AT, 2.2] | SLA | O | M | Equivale a cerca de 43 minutos de indisponibilidade por mês. Alinhar com o SLA do provedor de nuvem e com a regra de subcontratação (C-09). |
| R-24 | Relatório mensal até o 5º dia útil | [AT, 2.3] | SLA | O | B | — |
| R-25 | Classificação de criticidade pela matriz do Contratante | [AT, 2.4] | SLA | O | M | A matriz não foi entregue (ver P-05). |

### 3.4 Requisitos técnicos — IAM

| ID | Requisito | Fonte | Tipo | Nat. | Risco | Observações / ação |
|---|---|---|---|---|---|---|
| R-26 | Gestão do ciclo de vida (admissão, movimentação e desligamento) e revogação de acessos em até 24h | [AT, 3.1] | TEC/SLA | O | M | O ambiente atual usa "AD + scripts internos" [APR, slide 3]. Não está claro se o proponente deve fornecer uma ferramenta de IGA, com licenças incluídas no preço (ver P-11). |
| R-27 | MFA para 100% dos usuários com acesso privilegiado | [AT, 3.2] | TEC | O | M | Não se sabe quantas contas privilegiadas existem. |
| R-28 | Recertificação trimestral de acessos | [AT, 3.3] | TEC | O | M | Depende de ferramenta e de processo. |
| R-29 | Cofre de senhas / PAM | [AT, 3.4] | TEC | D | M | O item é desejável, mas o ambiente não tem PAM hoje [APR, slide 3]. Oferecer como opcional, com preço separado. |
| R-30 | Base de usuários para dimensionamento | [RFP, 2.1]; [APR, slide 2 e notas]; [QA, nº 5] | TEC/COM | O | **A** | Quatro números diferentes (ver C-01). |

### 3.5 Transição e equipe

| ID | Requisito | Fonte | Tipo | Nat. | Risco | Observações / ação |
|---|---|---|---|---|---|---|
| R-31 | Transição concluída em 30 dias **ou** em 60 dias | [RFP, 3.2] x [AT, 4.1] | PRZ | O | **A** | Conflito (ver C-03). |
| R-32 | Operação em paralelo com o fornecedor atual, sem custo adicional | [AT, 4.2] | COM | O | **A** | O custo da operação paralela recai sobre o proponente. É inviável depois de 31/01/2027 (fim do SIEM legado). |
| R-33 | Coordenador com CISSP, dedicado exclusivamente ao contrato | [AT, 5.1] | TEC | O | M | Custo fixo relevante. Confirmar se o profissional precisa estar alocado desde a proposta. |
| R-34 | Analistas N1 presenciais na sede em São Paulo, em horário comercial | [AT, 5.2] **alterado por** [QA, nº 6] | TEC | O | B | O Q&A permite trabalho remoto, desde que em território nacional. A resposta do Q&A prevalece. |
| R-35 | Contratante fornece VPN de acesso | [AT, 6.1] | — | — | B | Premissa a registrar na proposta. |
| R-36 | Contratante entrega a documentação técnica em até 10 dias após a assinatura | [AT, 6.2] | PRZ | — | M | Numa transição de 30 dias, isso consome um terço do prazo (ver C-03). |

### 3.6 Avaliação e condições comerciais/contratuais

| ID | Requisito | Fonte | Tipo | Nat. | Risco | Observações / ação |
|---|---|---|---|---|---|---|
| R-37 | Nota final = 60% técnica + 40% preço | [RFP, 6.1] | — | — | M | A fórmula da Nota de Preço não foi definida (ver P-07). |
| R-38 | Nota técnica máxima de 60 pontos, mas os critérios somam 65 | [RFP, 6.2] | — | — | **A** | Inconsistência aritmética (ver C-07). |
| R-39 | Desclassificação com nota técnica abaixo de 70% do máximo | [RFP, 6.3] | DSC | O | **A** | O corte é 42 pontos (base 60) ou 45,5 pontos (base 65), além da penalização oculta (C-08). |
| R-40 | Desempate pelo menor preço | [RFP, 6.4] | — | — | B | — |
| R-41 | Vigência de 36 meses, prorrogável por iguais períodos | [RFP, 7.1] | COM | — | B | — |
| R-42 | Reajuste anual pelo IPCA | [RFP, 7.2] | COM | — | B | Os custos de nuvem e de licenças costumam ser em dólar: há risco cambial sem proteção (*hedge*). |
| R-43 | Pagamento em até 60 dias após o aceite da nota fiscal | [RFP, 7.3] | COM | — | M | Impacto no fluxo de caixa. O prazo para o aceite não foi definido. |
| R-44 | Multa de 10% do valor mensal por ocorrência de descumprimento de SLA, **sem teto** | [RFP, 7.4]; [QA, nº 4] | COM | — | **Crítico** | O Q&A confirmou que não há limite. Com 1.200 alertas/dia e um SLA de 15 minutos, poucas ocorrências podem zerar a receita do mês. |
| R-45 | Responsabilidade integral e ilimitada por danos de incidentes "ocorridos no ambiente do Contratante" | [RFP, 7.5] | COM | — | **Crítico** | Não exige que a Contratada tenha causado o dano. Exposição ilimitada e possivelmente não segurável. |
| R-46 | Seguro de responsabilidade civil cibernética "em valor compatível" | [RFP, 7.6] | COM | O | **A** | O valor não foi definido e é incompatível com uma responsabilidade ilimitada. |
| R-47 | Vedada a subcontratação total ou parcial | [RFP, 7.7] | COM | O | **A** | Conflita com o SIEM em nuvem pública e com o uso de fabricantes/parceiros (ver C-09). |
| R-48 | Confidencialidade por 5 anos após o término do contrato | [RFP, 7.8] | COM | — | B | — |

---

## 4. Conflitos e inconsistências entre documentos

| ID | Tema | O que diz cada fonte | Prevalência provável | Impacto | Ação |
|---|---|---|---|---|---|
| **C-01** | **Número de usuários** | RFP 2.1: cerca de 4.500 colaboradores. APR slide 2: **6.200 usuários ativos**. APR, nota do slide 5: **mais cerca de 900** das subsidiárias Horizonte Seguros e Horizonte Investimentos. QA nº 5: "Considerar **5.000** usuários". | Para fins de preço, o QA (5.000) | **Alto.** A realidade pode chegar a cerca de 7.100 usuários, 42% acima da base oficial. Afeta licenças de IAM/MFA/IGA, o esforço de recertificação e a volumetria do SIEM. | Precificar com 5.000 e registrar a premissa explicitamente. Incluir preço unitário por usuário adicional. Pedir formalmente a confirmação sobre as subsidiárias. |
| **C-02** | **Data de entrega da proposta** | RFP 3.1: 20/11/2026, 18h. QA nº 1: **27/11/2026, 18h**. | QA | Médio | Planejar para 20/11 como data de segurança e pedir confirmação de que haverá adendo formal à RFP. |
| **C-03** | **Prazo de transição** | RFP 3.2: **30 dias** corridos após a assinatura. AT 4.1: **60 dias** corridos. Somam-se: documentação entregue em até 10 dias [AT 6.2]; SIEM legado termina em 31/01/2027 sem prorrogação [APR 3]; início em 01/02/2027 [RFP 3.1]. | Indefinida | **Alto.** O plano de transição vale 10 pontos [RFP 6.2]. Planejar para 60 dias quando o prazo exigido é 30 pode reduzir a nota ou gerar descumprimento. | Montar o plano para 30 dias (cenário mais restritivo) e perguntar ao cliente a data de assinatura e o prazo que vale. |
| **C-04** | **Localização dos dados / SIEM em nuvem** | AT 1.2: SIEM em nuvem pública "em **região de livre escolha** do proponente". Anexo III (imagem, pág. 6 do PDF): todos os dados, **incluindo os logs**, armazenados e processados **exclusivamente em território nacional**, sob pena de inabilitação. RFP 1.2: Res. CMN 4.893/2021. QA nº 2: SOC no Brasil. | Anexo III (mais restritivo e eliminatório) | **Alto.** Uma arquitetura com região no exterior leva à inabilitação. Uma região no Brasil costuma ser mais cara e pode limitar a escolha do SIEM. | Desenhar a solução com região no Brasil (incluindo backup/DR e o arquivo de 5 anos). Pedir que o cliente corrija o AT 1.2 ou confirme a precedência do Anexo III. |
| **C-05** | **Retenção de logs** | AT 1.3: no mínimo 12 meses. QT-03: 12 meses "online". AT 1.6: **5 anos** para auditoria. APR 5: migrar **24 meses** de histórico. | Cumulativo: 12 meses online + 5 anos no total + 24 meses migrados | **Alto.** O custo de armazenamento cresce muito, e o volume é desconhecido sem o EPS. | Propor um modelo em camadas (quente por 12 meses, frio/arquivo até 5 anos) e pedir confirmação. Precificar a migração do histórico como item separado. |
| **C-06** | **Escopo trazido só pela apresentação** | A migração de 24 meses de logs, a visão unificada de riscos para a diretoria, a meta de 10% de falsos positivos e as subsidiárias (só na nota) **não constam da RFP nem do AT**. | RFP/AT (a apresentação não é vinculante) | Alto | Tratar como premissas ou itens opcionais na proposta. Pedir a formalização. Não ignorar: provavelmente serão cobrados na execução. |
| **C-07** | **Pontuação técnica** | RFP 6.2: máximo de **60** pontos. Critérios: 20 + 20 + 15 + 10 = **65**. RFP 6.3: corte em 70% do máximo. | Indefinida | Alto. O corte pode ser 42 ou 45,5 pontos. | Perguntar ao cliente qual é a base e se os pontos serão normalizados. |
| **C-08** | **Regra de avaliação oculta** | A aba **oculta** "Pesos" [QA] atribui pesos de 1 a 3 aos itens QT-01 a QT-06 e diz que cada requisito **não obrigatório** respondido "Não atende" **reduz a Nota Técnica em 2 pontos**. A RFP não menciona nenhuma dessas regras. | Indefinida (regra não publicada) | Alto. QT-02 (SOAR) e QT-05 (threat intelligence) podem custar até 4 pontos, perto da margem de corte. Não se sabe como os pesos entram na nota. | Pedir esclarecimento sobre a validade da regra. Avaliar a inclusão de SOAR e threat intelligence na oferta para responder "Atende" com fundamento. Responder o questionário com veracidade. |
| **C-09** | **Subcontratação x nuvem e fabricantes** | RFP 7.7 veda qualquer subcontratação. AT 1.2 permite SIEM em nuvem pública. Ferramentas de IAM/PAM e SOAR normalmente envolvem fabricantes e provedores. | Indefinida | Alto. Interpretada de forma literal, a cláusula pode inviabilizar o uso de provedor de nuvem (IaaS/SaaS). | Pedir que o cliente confirme que fornecedores de tecnologia, licenças e nuvem não contam como subcontratação. |
| **C-10** | **Analistas N1 presenciais** | AT 5.2: presencial em São Paulo. QA nº 6: remoto permitido, desde que no Brasil. | QA | Baixo (reduz custo) | Usar o modelo remoto. Avaliar se uma presença parcial ajuda na nota de metodologia. |
| **C-11** | **Fonte do conteúdo do workshop** | Informações importantes de escopo estão só nas **notas do apresentador** do slide 5. | — | Médio. Outros proponentes podem ter recebido essa informação apenas oralmente. | Tratar como informação não formalizada (ver C-01). |
| **C-12** | **Numeração e referência de anexos** | O Anexo II não existe. O Anexo III não é citado no corpo da RFP e está só em imagem. O Anexo IV é citado e não foi entregue. A numeração do PDF está deslocada (pág. física 2 = "Página 1"). | — | Médio | Pedir o pacote completo de anexos (ver P-01). |

---

## 5. Lacunas e informações faltantes

| ID | Lacuna | Por que importa |
|---|---|---|
| L-01 | Volumetria (EPS/GB por dia) não informada; só será dada ao vencedor [QA nº 3] | É a principal variável de custo do SIEM, do armazenamento de 5 anos e da migração de 24 meses. |
| L-02 | Anexo IV (Planilha de Preços) e Anexo II ausentes | A proposta comercial não pode ser montada. |
| L-03 | Matriz de criticidade do Contratante | O SLA de 15 minutos com multa de 10% não pode ser avaliado. |
| L-04 | Definição de "ativos relevantes" [AT 1.4] | O escopo de integração fica aberto e pode ser ampliado pelo cliente sem limite. |
| L-05 | Data prevista de assinatura do contrato | O cronograma da transição não pode ser fixado. |
| L-06 | Fórmula da Nota de Preço | Impede simular a competitividade do preço. |
| L-07 | Quantidade de contas privilegiadas e de sistemas a integrar no IAM | Impede dimensionar MFA, recertificação e PAM. |
| L-08 | Escopo de IAM: serviço sobre a ferramenta do cliente ou fornecimento de ferramenta | Mudança grande no preço (licenças de IGA). |
| L-09 | Valor do seguro cibernético exigido | Impede cotar o seguro. |
| L-10 | Valor estimado do contrato | Não informado, nem pelo cliente nem pelos documentos. |
| L-11 | Critérios do item 5.2 ("equipe devidamente certificada") | Critério subjetivo de habilitação. |
| L-12 | Situação dos workloads nas 2 nuvens públicas (quais são e como serão integrados) | Afeta os conectores e o custo de coleta. |

---

## 6. Riscos principais (priorizados)

| # | Risco | Fonte | Severidade | Mitigação sugerida |
|---|---|---|---|---|
| 1 | Responsabilidade ilimitada por qualquer incidente no ambiente do cliente | RFP 7.5 | Crítica | Pedir limite (por exemplo, até 12 meses de faturamento) e nexo de causalidade. Se o cliente recusar, levar a decisão de participar (*go/no-go*) à diretoria jurídica. |
| 2 | Multa de 10% por ocorrência, sem teto (confirmado no Q&A) | RFP 7.4; QA nº 4 | Crítica | Modelar o pior caso. Propor teto mensal agregado e período de carência (*grace period*) na transição. |
| 3 | Inabilitação por arquitetura com dados fora do Brasil | AT 1.2 x Anexo III | Alta | Arquitetura 100% em região no Brasil. Assinar o Anexo III. |
| 4 | Subdimensionamento: 5.000 usuários oficiais contra cerca de 7.100 reais e EPS desconhecido | C-01; L-01 | Alta | Preços unitários por faixa de usuários e de EPS/GB, com premissas explícitas e cláusula de reequilíbrio. |
| 5 | Transição comprimida e fim do SIEM legado em 31/01/2027 | C-03 | Alta | Plano de 30 dias com ativação rápida do SIEM e coleta antecipada. Registrar a dependência da assinatura até cerca de 02/01/2027. |
| 6 | Nota técnica abaixo do corte por inconsistência na pontuação e pela penalização oculta | C-07; C-08 | Alta | Maximizar os critérios de metodologia e de equipe (40 pontos). Avaliar a oferta de SOAR e threat intelligence. |
| 7 | Custo de armazenamento de logs por 5 anos e da migração de 24 meses | C-05 | Alta | Arquitetura em camadas e itens precificados separadamente. |
| 8 | Meta de falsos positivos (10%) transformada em obrigação | APR 4 | Média | Tratar como meta de melhoria contínua, não como SLA. Atingi-la depende de calibrar as regras com o cliente. |
| 9 | Vedação de subcontratação aplicada à nuvem e aos fabricantes | C-09 | Média/Alta | Esclarecimento formal. |
| 10 | Operação paralela sem custo | AT 4.2 | Média | Embutir o custo no preço global e limitar a duração. |
| 11 | Pagamento em 60 dias, IPCA contra custos em dólar | RFP 7.2–7.3 | Média | Considerar no capital de giro e no preço. |

---

## 7. Perguntas de esclarecimento sugeridas

> **Atenção:** o prazo formal para perguntas [RFP 3.1] terminou em 05/11/2026 e não há 2ª rodada prevista. Recomenda-se enviar as perguntas mesmo assim, como pedido de esclarecimento adicional ou pelo canal do portal. As de prioridade A são determinantes para a decisão de participar.

| ID | Prioridade | Pergunta | Ref. |
|---|---|---|---|
| P-01 | A | Favor disponibilizar o Anexo IV (Planilha de Preços), informar se existe um Anexo II e fornecer uma versão editável do Anexo III. | RFP 4.3; pág. 6 |
| P-02 | A | O AT 1.2 permite SIEM em nuvem pública em região de livre escolha, e o Anexo III exige que todos os dados, inclusive os logs, fiquem exclusivamente no Brasil. Qual prevalece? Backup e DR também devem ficar no Brasil? | AT 1.2; Anexo III |
| P-03 | A | Embora o QA nº 3 diga que o EPS será informado só ao vencedor, solicita-se ao menos uma faixa de volumetria (EPS médio/pico ou GB/dia) e o volume dos 24 meses de histórico a migrar, para que as propostas sejam comparáveis. | AT 1.4; QA 3; APR 5 |
| P-04 | A | O prazo de transição é de 30 dias [RFP 3.2] ou de 60 dias [AT 4.1]? Qual é a data prevista de assinatura do contrato? | RFP 3.2; AT 4.1 |
| P-05 | A | Favor fornecer a matriz de classificação de criticidade citada no AT 2.4. | AT 2.1, 2.4 |
| P-06 | A | As subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários, mencionadas no workshop) fazem parte do escopo? Os 5.000 usuários do QA nº 5 já incluem essas empresas? Como se conciliam com os 6.200 usuários ativos apresentados? | RFP 2.1; APR 2 e 5; QA 5 |
| P-07 | A | A Nota Técnica máxima é de 60 pontos, mas os critérios somam 65. Qual é a base do corte de 70%? Qual é a fórmula da Nota de Preço? | RFP 6.2–6.3 |
| P-08 | A | A regra de desconto de 2 pontos por requisito não obrigatório respondido "Não atende" e os pesos por requisito (aba "Pesos" do questionário) são critérios válidos? Como entram na Nota Técnica? | QA aba Pesos |
| P-09 | M | A obrigação de preencher "todas as abas" vale para quais abas, além do Questionário Técnico? | QA Instruções |
| P-10 | M | Quais certificações atendem ao item 5.2, "equipe devidamente certificada"? Quantos profissionais certificados são exigidos? | RFP 5.2; QT-06 |
| P-11 | M | No IAM, o proponente deve fornecer uma ferramenta (IGA/MFA/PAM, com licenças) ou operar as ferramentas do Contratante? | AT 3; APR 3 |
| P-12 | M | A meta de 10% de falsos positivos no 1º trimestre, a migração de 24 meses de logs e a "visão unificada de riscos para a diretoria" fazem parte do escopo obrigatório? | APR 4–5 |
| P-13 | A | O uso de provedor de nuvem e de fabricantes de software/licenças é considerado subcontratação para fins do item 7.7? | RFP 7.7 |
| P-14 | A | O Contratante aceita limitar a responsabilidade (7.5) a um valor ou a uma proporção do contrato e com nexo de causalidade? Aceita um teto agregado para as multas (7.4)? Qual valor de seguro (7.6) será considerado compatível? | RFP 7.4–7.6 |
| P-15 | M | Os 5 anos de retenção [AT 1.6] podem ser cumpridos com armazenamento frio/arquivado, mantendo online apenas 12 meses [AT 1.3; QT-03]? | AT 1.3, 1.6 |
| P-16 | B | Qual é o prazo para o aceite da nota fiscal [RFP 7.3]? | RFP 7.3 |
| P-17 | M | A prorrogação da entrega para 27/11/2026 será formalizada por adendo à RFP? | QA 1 |

---

## 8. Checklist de entrega da proposta

| Item | Fonte | Status sugerido |
|---|---|---|
| Proposta técnica em português, até 40 páginas, sem contar os anexos | RFP 4.1–4.2 | A elaborar |
| Proposta comercial no Anexo IV | RFP 4.3 | **Bloqueado: o anexo não foi recebido** |
| Questionário técnico integralmente preenchido (QT-01 a QT-06, com resposta e comentário) | RFP 4.4; QA | A elaborar |
| Certificado ISO/IEC 27001 vigente, com escopo SOC | RFP 5.1a | Verificar escopo e validade |
| 3 ou mais atestados de SOC para instituições financeiras com 2.000 usuários ou mais | RFP 5.1b | Levantar |
| Comprovação de SOC no Brasil | RFP 5.1c | Levantar (endereço, alvará, contrato de site etc.) |
| Comprovação das certificações da equipe, incluindo o CISSP do coordenador | RFP 5.2; AT 5.1 | Levantar currículos e certificados |
| Anexo III assinado pelo representante legal | PDF pág. 6 | Preparar (verificar a procuração do signatário) |
| Apólice ou carta de intenção de seguro cibernético | RFP 7.6 | Cotar |
| Envio pelo portal até 27/11/2026, 18h (data de segurança: 20/11) | RFP 3.1; QA 1 | Agendar |

---

## 9. Respostas preliminares ao Questionário Técnico

O questionário só deve ser respondido depois da confirmação da capacidade real do proponente. A tabela abaixo serve de guia.

| ID | Requisito | Obrig. | Peso (aba oculta) | Pontos de atenção |
|---|---|---|---|---|
| QT-01 | ISO 27001 com escopo de SOC | Sim | 3 | Também é critério de habilitação (5.1a). |
| QT-02 | Integração nativa com SOAR | Não | 1 | Um "Não atende" custaria 2 pontos pela regra oculta. |
| QT-03 | Logs online por 12 meses ou mais | Sim | 2 | Comentar o modelo em camadas e o arquivo de 5 anos (AT 1.6). |
| QT-04 | Aderência à Res. CMN 4.893/2021 | Sim | 3 | Comentar a localização dos dados no Brasil e o apoio às comunicações ao Banco Central. |
| QT-05 | Threat intelligence | Não | 2 | Um "Não atende" custaria 2 pontos pela regra oculta. |
| QT-06 | Equipe com certificações de mercado | Sim | 2 | Listar as certificações (CISSP, CISM, GCIH, certificações de fabricantes de SIEM/IAM etc.). |

---

## 10. Síntese para a decisão de participar (go/no-go)

**Pontos favoráveis.**
- Escopo aderente a um portfólio típico de MSSP (SOC + IAM), com contrato de 36 meses prorrogável.
- Peso técnico de 60%.
- Analistas N1 podem trabalhar remotamente.

**Pontos impeditivos ou de alto risco, que exigem decisão executiva:**
1. responsabilidade **ilimitada** por qualquer incidente no ambiente do cliente (7.5);
2. multas de 10% por ocorrência **sem teto**, confirmado no Q&A (7.4);
3. dimensionamento sem EPS e com base de usuários inconsistente (de 4.500 a cerca de 7.100);
4. transição de 30 a 60 dias, presa ao fim do SIEM legado em 31/01/2027;
5. regra de pontuação oculta e inconsistência na nota técnica (60 contra 65);
6. Anexo IV ausente.

**Recomendação.** Seguir com a elaboração da proposta de forma **condicionada**:
- enviar imediatamente as perguntas de prioridade A (P-01 a P-08, P-13 e P-14);
- precificar com premissas explícitas (5.000 usuários, faixas de EPS, armazenamento em camadas, região no Brasil, migração de histórico como item opcional);
- submeter as cláusulas 7.4 e 7.5 à análise jurídica antes da decisão final de participar.

Sem limite de responsabilidade ou sem teto de multas, o risco do contrato tende a superar a margem esperada.

---

### Anexo A — Arquivos de trabalho

Os textos extraídos de cada documento estão na pasta `work/`:
- `rfp.txt`
- `rfp_p6.png` (renderização da página digitalizada do Anexo III)
- `anexo.txt`
- `apresentacao.txt` (inclui as notas do apresentador)
- `qa.txt` (inclui a aba oculta "Pesos")
