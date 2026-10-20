# Análise da RFP nº 2026-017 — Serviços Gerenciados de SOC e IAM

**Cliente:** Banco Horizonte Fictício S.A.
**Processo:** RFP nº 2026-017
**Objeto resumido:** serviços gerenciados de SOC (24x7x365) e de IAM
**Valor estimado do contrato:** não informado (nenhum dos documentos traz valor de referência)
**Data da análise:** 18/10/2026
**Documentos analisados:** 4 arquivos (lista na seção 1)

> Os documentos se declaram fictícios ("DOCUMENTO FICTÍCIO PARA TESTE"). A análise trata o conteúdo como se fosse um processo real.

### Legenda de referências
- `[RFP §x]`: item do corpo da RFP (PDF)
- `[RFP p.6 / Anexo III]`: página 6 do PDF, que é uma imagem digitalizada
- `[AnxI §x]`: item do Anexo I (DOCX)
- `[PPT sN]` / `[PPT sN-notas]`: slide N da apresentação, ou as anotações do apresentador desse slide
- `[QA #n]`: pergunta n da aba "Q&A Rodada 1" (XLSX)
- `[QT-nn]`: item da aba "Questionário Técnico" (XLSX)
- `[XLSX Pesos]`: aba oculta "Pesos" (XLSX)
- `[XLSX Instr.]`: aba "Instruções" (XLSX)

---

## Sumário executivo

1. **O prazo de entrega mudou.** A Q&A prorrogou a entrega de 20/11/2026 para **27/11/2026, até as 18h** [QA #1]. O cronograma da RFP v1.0 não foi reemitido.
2. **O cronograma de transição tem conflito e pode ficar inviável.** A RFP fixa a transição em 30 dias [RFP §3.2] e o Anexo I em 60 dias [AnxI §4.1]. O contrato do SIEM legado acaba em **31/01/2027, sem possibilidade de prorrogação** [PPT s3], e o início dos serviços está previsto para 01/02/2027 [RFP §3.1]. Com 60 dias, o contrato teria de ser assinado até 02/12/2026, cinco dias depois da entrega das propostas.
3. **Há conflito sobre onde os dados ficam.** O Anexo I permite SIEM em nuvem pública "em região de livre escolha do proponente" [AnxI §1.2]. A declaração do Anexo III, que só existe como imagem digitalizada na p.6 do PDF, exige que todos os dados, inclusive logs, fiquem **exclusivamente em território nacional, sob pena de inabilitação** [RFP p.6 / Anexo III]. Na prática, **só uma região no Brasil é segura.**
4. **A base de usuários tem quatro números diferentes:** 4.500 colaboradores [RFP §2.1], 6.200 usuários ativos [PPT s2], cerca de 900 usuários adicionais das subsidiárias [PPT s5-notas] e 5.000 usuários para dimensionamento [QA #5]. A volumetria de EPS **não foi informada** [QA #3]. Por isso, o preço do SIEM/SOC depende de premissas.
5. **O risco contratual é muito alto.** As multas são de 10% do valor mensal **por ocorrência, sem teto**, e a Q&A manteve essa condição [RFP §7.4; QA #4]. A responsabilidade é **integral e ilimitada** por danos de incidentes [RFP §7.5]. A subcontratação é vedada [RFP §7.7], o pagamento sai em 60 dias [RFP §7.3] e a operação em paralelo durante a transição não tem custo adicional [AnxI §4.2].
6. **Há regras escondidas ou informais:**
   - A aba oculta "Pesos" desconta **2 pontos da Nota Técnica para cada requisito não obrigatório respondido como "Não atende"** [XLSX Pesos].
   - A aba "Instruções" diz que **questionário incompleto desclassifica** [XLSX Instr.].
   - As anotações do slide 5 incluem as subsidiárias no escopo [PPT s5-notas].
   - O slide 5 traz a migração de 24 meses de logs [PPT s5], que não está na RFP nem no Anexo I.
7. **A pontuação técnica não fecha.** A RFP diz que o máximo é 60 pontos, mas os critérios somam **65** [RFP §6.2]. O corte de 70% [RFP §6.3] pode ser 42 ou 45,5 pontos. A fórmula da Nota de Preço não foi definida.
8. **Faltam documentos:** o **Anexo IV (Planilha de Preços)** é obrigatório [RFP §4.3] e não foi fornecido. O Anexo II não é citado nem foi fornecido.

**Recomendação preliminar:** o processo é tecnicamente aderente para um provedor de SOC/IAM com SOC no Brasil, ISO 27001 e atestados no setor financeiro. **Mesmo assim, recomendo condicionar o "go" a três ações:**
- (a) pedir esclarecimento formal sobre transição, base de usuários/EPS e escopo das subsidiárias;
- (b) aprovar internamente, no nível jurídico e de diretoria, a exposição a multas sem teto e a responsabilidade ilimitada, ou registrar ressalvas sabendo que podem desclassificar a proposta;
- (c) obter o Anexo IV.

---

## 1. Inventário dos documentos

| # | Arquivo | Tipo / formato | Versão / data declarada | Estrutura | Observações de integridade e conteúdo não evidente |
|---|---|---|---|---|---|
| 1 | RFP-2026-017_Servicos_SOC_IAM.pdf | RFP, PDF de 6 páginas gerado por ReportLab | v1.0, 15/10/2026 | p.1 capa; p.2 a p.5 com seções 1 a 7 (rodapé "Página 1" a "Página 4"); **p.6 ("Página 5") sem camada de texto** | A **p.6 é uma imagem digitalizada** com o **Anexo III — Declaração de Localização de Dados**. A extração de texto não a captura: foi preciso ler a imagem. Esse anexo tem cláusula de inabilitação. O PDF cita os Anexos I, III e IV. **O Anexo IV não foi fornecido** e o Anexo II não é citado. |
| 2 | Anexo_I_Especificacao_Tecnica.docx | Anexo técnico, DOCX | v1.0, 15/10/2026 (no corpo) | Seções 1 a 6: SOC, SLA, IAM, Transição, Equipe, Responsabilidades do Contratante | Os metadados (autor "python-docx", datas de 2013) não correspondem ao documento e não servem para controlar versão. Não há controle de alterações, comentários nem texto oculto. |
| 3 | Apresentacao_Ambiente_Atual.pptx | Apresentação do workshop, PPTX com 5 slides | 22/10/2026 (no slide 1) | s1 capa; s2 números; s3 ferramentas; s4 desafios; s5 expectativas | **As anotações do apresentador no s5 ampliam o escopo** (subsidiárias, cerca de 900 usuários). O s5 também pede a migração de 24 meses de logs, que não está na RFP. A apresentação não tem valor contratual declarado. Não há slides ocultos. |
| 4 | QA_Rodada1_e_Questionario.xlsx | Q&A e questionário, XLSX com 4 abas | 12/11/2026 (respostas da Q&A) | "Instruções"; "Q&A Rodada 1" (6 perguntas); "Questionário Técnico" (QT-01 a QT-06, respostas em branco); **"Pesos" (aba oculta)** | **A aba oculta "Pesos"** tem pesos por item e uma **regra de desconto na Nota Técnica que não está na RFP**. A aba "Instruções" cria uma **regra de desclassificação** para questionário incompleto. |

### Observações gerais do inventário
- **Datas:** a data desta análise (18/10/2026) é anterior às datas dos documentos 3 (22/10/2026) e 4 (12/11/2026). Confirme se esses arquivos são as versões finais publicadas, e não minutas antecipadas.
- **Anexos citados e não recebidos:**
  - Anexo IV — Planilha de Preços [RFP §4.3]: obrigatório para a proposta comercial.
  - Matriz de classificação de criticidade do Contratante [AnxI §2.4]: o SLA de 15 minutos depende dela.
  - Anexo II: não é citado em nenhum documento, e a numeração salta do I para o III.
- **Versão:** a RFP continua na v1.0. Nenhuma alteração da Q&A (prazo, usuários, trabalho remoto) foi incorporada em nova versão.
- **Prazo de perguntas:** a Q&A da Rodada 1 foi publicada em 12/11/2026, depois do prazo final de perguntas (05/11/2026) [RFP §3.1]. Não há previsão de Rodada 2. Os esclarecimentos sugeridos na seção 9 podem exigir pedido de reabertura ou ressalvas na proposta.

### Ordem de precedência adotada
Nenhum documento define hierarquia entre RFP, anexos, apresentação e Q&A. Para esta análise, adotei esta ordem:
1. **Q&A** (resposta formal mais recente; altera itens específicos);
2. **RFP** (corpo) e seus anexos formais, **Anexo III** e **Anexo I**. Quando o conflito não foi resolvido pela Q&A, o ponto é tratado como **conflito aberto**;
3. **Questionário XLSX** (instrumento de resposta, inclusive as regras das abas "Instruções" e "Pesos");
4. **Apresentação** (informativa; seu conteúdo **não** foi considerado vinculante, mas é sinal de expectativa do cliente).

---

## 2. Ficha do processo

| Campo | Valor consolidado | Fonte |
|---|---|---|
| Objeto | SOC gerenciado 24x7x365 e IAM | [RFP §2.1; AnxI §1.1] |
| Base de usuários | **Indefinida**: 4.500, 5.000, 6.200 ou cerca de 7.100 (ver C-03) | [RFP §2.1; QA #5; PPT s2; PPT s5-notas] |
| Ambiente | 850 servidores (70% Windows, 30% Linux), 2 DCs próprios (São Paulo e Campinas), workloads em 2 nuvens públicas | [PPT s2] |
| Ferramentas atuais | SIEM legado (contrato termina em 31/01/2027, sem prorrogação), AD com scripts internos, nenhuma solução de PAM | [PPT s3] |
| Volume operacional | Cerca de 1.200 alertas por dia, 70% de falsos positivos. Meta: 10% no 1º trimestre | [PPT s4] |
| Vigência | 36 meses, prorrogável por iguais períodos | [RFP §7.1] |
| Reajuste | IPCA anual | [RFP §7.2] |
| Pagamento | Até 60 dias após o aceite da nota fiscal | [RFP §7.3] |
| Julgamento | Técnica 60% e Preço 40%; corte técnico de 70%; empate decidido pelo menor preço | [RFP §6] |
| Canal de entrega | Exclusivamente pelo portal de fornecedores, em português | [RFP §4.1] |
| Limite da proposta técnica | 40 páginas, sem contar os anexos | [RFP §4.2] |
| Regulação | Resolução CMN nº 4.893/2021 | [RFP §1.2; QT-04] |

---

## 3. Cronograma consolidado

| Etapa | Data original [RFP §3.1] | Data vigente | Observação |
|---|---|---|---|
| Publicação da RFP | 15/10/2026 | 15/10/2026 | |
| Workshop do ambiente | 22/10/2026 | 22/10/2026 | Apresentação = doc. 3 |
| Prazo final para perguntas | 05/11/2026 | 05/11/2026 | Não há Rodada 2 prevista |
| Divulgação das respostas | 12/11/2026 | 12/11/2026 | Doc. 4 |
| **Entrega das propostas** | 20/11/2026, até as 18h | **27/11/2026, até as 18h** | **Prorrogado** [QA #1] |
| Início dos serviços | 01/02/2027 | 01/02/2027 | Não foi alterado, apesar da prorrogação |
| Fim do contrato do SIEM legado | n/a | **31/01/2027** | Sem prorrogação [PPT s3] |
| Conclusão da transição | 30 dias após a assinatura [RFP §3.2] | **Conflito: 30 ou 60 dias** [AnxI §4.1] | Ver C-01 |
| Entrega da documentação do ambiente pelo Contratante | n/a | 10 dias após a assinatura [AnxI §6.2] | Consome de 1/3 a 1/6 da transição |

**Teste de viabilidade.** Da entrega (27/11/2026) ao início (01/02/2027) há **66 dias corridos**. Nesse intervalo cabem avaliação, negociação, assinatura, transição, operação em paralelo e migração de 24 meses de logs, tudo antes de o SIEM legado ser desligado em 31/01/2027. Para que a transição termine até 31/01/2027, a assinatura teria de ocorrer:
- até **01/01/2027**, com transição de 30 dias;
- até **02/12/2026**, com transição de 60 dias, o que é irrealista.

A operação em paralelo "com o fornecedor atual" [AnxI §4.2] também depende de o SIEM legado estar ativo.

---

## 4. Matriz de requisitos

**Tipos:** HAB = habilitação (inabilita); DESC = desclassificação; OBR = obrigatório técnico; DES = desejável; SLA = nível de serviço sujeito a multa; CTR = contratual/comercial; FORM = forma de apresentação; INF = informativo/expectativa (não vinculante).

**Criticidade para o proponente:** Alta / Média / Baixa.

| ID | Requisito | Tipo | Fonte | Crit. | Situação / observação |
|---|---|---|---|---|---|
| R-01 | Proposta em português, enviada só pelo portal | FORM | RFP §4.1 | Média | |
| R-02 | Proposta técnica com no máximo 40 páginas, sem contar anexos | FORM | RFP §4.2 | Média | Não define a consequência de ultrapassar |
| R-03 | Proposta comercial no modelo do Anexo IV | FORM | RFP §4.3 | **Alta** | **Anexo IV não fornecido** |
| R-04 | Questionário técnico integralmente preenchido | FORM / DESC | RFP §4.4; XLSX Instr. | **Alta** | Instr.: "todas as abas" são obrigatórias e o incompleto é desclassificado. Ver C-09 |
| R-05 | ISO/IEC 27001 vigente, de organismo acreditado, com escopo que inclua o SOC | HAB | RFP §5.1a; QT-01 | **Alta** | Verificar o escopo do certificado |
| R-06 | Pelo menos 3 atestados de SOC para instituições financeiras com 2.000 usuários ou mais | HAB | RFP §5.1b | **Alta** | Não pede atestado de IAM |
| R-07 | SOC localizado em território nacional | HAB | RFP §5.1c; QA #2 | **Alta** | Confirmado pela Q&A |
| R-08 | Equipe técnica "devidamente certificada" | HAB (?) | RFP §5.2 | Média | Critério subjetivo; não diz quais certificações |
| R-09 | Declaração de localização de dados (Anexo III), assinada pelo representante legal: todos os dados, inclusive logs, armazenados e processados só no Brasil | HAB | RFP p.6 / Anexo III | **Alta** | Só existe como imagem. Conflita com AnxI §1.2 (C-02) |
| R-10 | Monitoramento contínuo 24x7x365 | OBR | AnxI §1.1; RFP §2.1 | Alta | |
| R-11 | Fornecimento da solução de SIEM (pode ser em nuvem pública) | OBR | AnxI §1.2 | Alta | Região: ver C-02. Subcontratação: ver C-08 |
| R-12 | Retenção de logs por pelo menos 12 meses (online, segundo QT-03) | OBR | AnxI §1.3; QT-03 | Alta | Ver C-04 |
| R-13 | SIEM integrado a "todos os ativos relevantes" | OBR | AnxI §1.4 | **Alta** | Escopo indefinido; EPS não informado [QA #3] |
| R-14 | Resposta a incidentes: contenção, erradicação e relatório pós-incidente | OBR | AnxI §1.5 | Alta | Não diz se a resposta é remota ou presencial; forense fora do escopo? |
| R-15 | Logs mantidos por 5 anos para auditoria | OBR | AnxI §1.6 | **Alta** | Ver C-04. Grande impacto em custo de armazenamento |
| R-16 | Início do tratamento de incidente crítico em até 15 minutos | SLA | AnxI §2.1 | **Alta** | Depende da matriz de criticidade do cliente, que não foi fornecida |
| R-17 | Disponibilidade do SIEM de pelo menos 99,9% ao mês | SLA | AnxI §2.2 | Alta | Cerca de 43 minutos de indisponibilidade por mês |
| R-18 | Relatório mensal até o 5º dia útil | SLA | AnxI §2.3 | Média | Cada atraso gera multa de 10% |
| R-19 | Criticidade definida pela matriz do Contratante | SLA | AnxI §2.4 | **Alta** | Matriz não fornecida; o cliente pode reclassificar unilateralmente |
| R-20 | Ciclo de vida de identidades; revogação de desligados em até 24h | OBR / SLA | AnxI §3.1 | Alta | Depende de o RH avisar a tempo. Ferramenta de IGA: fornecida ou operar AD e scripts? |
| R-21 | MFA para 100% dos usuários privilegiados | OBR | AnxI §3.2 | Alta | Solução de MFA: quem fornece? |
| R-22 | Recertificação trimestral de acessos | OBR | AnxI §3.3 | Média | |
| R-23 | Cofre de senhas / PAM | DES | AnxI §3.4 | Média | Hoje não existe PAM [PPT s3]. Não pontua em §6.2 |
| R-24 | Transição concluída em 30 ou 60 dias | OBR | RFP §3.2; AnxI §4.1 | **Alta** | Conflito C-01 |
| R-25 | Operação em paralelo com o fornecedor atual, sem custo adicional | OBR / CTR | AnxI §4.2 | Alta | Custo absorvido pelo proponente |
| R-26 | Coordenador com CISSP, dedicado exclusivamente ao contrato | OBR | AnxI §5.1 | Alta | Custo de pessoa dedicada |
| R-27 | Analistas N1 presenciais na sede em São Paulo, em horário comercial | OBR, alterado | AnxI §5.2; **QA #6** | Média | **A Q&A permite trabalho remoto em território nacional** |
| R-28 | Integração nativa com SOAR | DES (não obrig.) | QT-02 | Média | "Não atende" tira 2 pontos [XLSX Pesos] |
| R-29 | Conformidade com a Res. CMN 4.893/2021 | OBR | RFP §1.2; QT-04 | Alta | Inclui regras de nuvem e de comunicação ao regulador |
| R-30 | Serviço de threat intelligence | DES (não obrig.) | QT-05 | Média | "Não atende" tira 2 pontos [XLSX Pesos] |
| R-31 | Equipe com certificações reconhecidas pelo mercado | OBR | QT-06 | Média | |
| R-32 | Vigência de 36 meses, prorrogável | CTR | RFP §7.1 | Baixa | |
| R-33 | Reajuste anual pelo IPCA | CTR | RFP §7.2 | Baixa | |
| R-34 | Pagamento em até 60 dias após o aceite da NF | CTR | RFP §7.3 | Média | Impacto no fluxo de caixa |
| R-35 | Multa de 10% do valor mensal por ocorrência de descumprimento de SLA | CTR | RFP §7.4; QA #4 | **Crítica** | Sem teto, confirmado pela Q&A |
| R-36 | Responsabilidade integral e ilimitada por danos de incidentes | CTR | RFP §7.5 | **Crítica** | |
| R-37 | Seguro de responsabilidade civil cibernética "em valor compatível" | CTR | RFP §7.6 | Alta | Valor indefinido; difícil de segurar com responsabilidade ilimitada |
| R-38 | Subcontratação vedada, total ou parcial | CTR | RFP §7.7 | **Alta** | Ver C-08 |
| R-39 | Confidencialidade por 5 anos após o fim do contrato | CTR | RFP §7.8 | Baixa | |
| R-40 | Contratante fornece VPN | Contratante | AnxI §6.1 | Baixa | |
| R-41 | Contratante entrega a documentação técnica em até 10 dias da assinatura | Contratante | AnxI §6.2 | Média | Prazo longo diante de uma transição de 30 dias |
| R-42 | Incluir as subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários) | INF | PPT s5-notas | **Alta** | Não formalizado. Ver C-03 e C-07 |
| R-43 | Migrar 24 meses de logs do SIEM legado | INF | PPT s5 | **Alta** | Não está na RFP nem no Anexo I. Ver C-06 |
| R-44 | Reduzir os falsos positivos para 10% no 1º trimestre | INF | PPT s4 | Média | Se virar SLA, o risco é alto |
| R-45 | Visão unificada de riscos para a diretoria | INF | PPT s5 | Baixa | Escopo indefinido |

---

## 5. Conflitos e inconsistências

| ID | Tema | Fonte A | Fonte B (e outras) | Situação | Tratamento recomendado |
|---|---|---|---|---|---|
| **C-01** | Prazo de transição | RFP §3.2: **30 dias** corridos da assinatura | AnxI §4.1: **60 dias** corridos | **Aberto** (a Q&A não tratou) | Esclarecer. Na proposta, planejar 30 dias (o prazo mais restritivo) e registrar que o cumprimento depende da data de assinatura e da entrega da documentação [AnxI §6.2]. Ver também o risco de cronograma (seção 3). |
| **C-02** | Localização dos dados e do SIEM | AnxI §1.2: nuvem pública "em região de livre escolha" | Anexo III (p.6, imagem): dados e logs **exclusivamente no Brasil**, sob pena de inabilitação. RFP §5.1c e QA #2: SOC no Brasil. Res. CMN 4.893 | **Aberto**, mas a regra mais restritiva tem consequência de inabilitação | **Usar só região de nuvem no Brasil**, inclusive para backup, DR e retenção de 5 anos. Confirmar se a telemetria e o processamento SaaS do fabricante do SIEM ficam no país. |
| **C-03** | Base de usuários | RFP §2.1: cerca de **4.500** colaboradores | PPT s2: **6.200** usuários ativos. PPT s5-notas: mais **cerca de 900** das subsidiárias. **QA #5: "Considerar 5.000"** | Parcialmente resolvido pela Q&A (5.000 para dimensionamento) | Precificar com 5.000 [QA #5] e declarar isso como premissa. Incluir **preço unitário por usuário adicional** e faixas de volume. Perguntar se os 5.000 incluem as subsidiárias e como explicar os 6.200 usuários ativos (contas de serviço, terceiros?). |
| **C-04** | Retenção de logs | AnxI §1.3: no mínimo **12 meses**. QT-03: 12 meses **online** | AnxI §1.6: **5 anos** para auditoria | Ambíguo, sem contradição direta | Interpretar como 12 meses online (*hot*) mais 5 anos em arquivamento (*cold*), tudo no Brasil. Confirmar e precificar à parte. |
| **C-05** | Pontuação técnica | RFP §6.2: Nota Técnica com "no máximo 60 pontos" | Soma dos critérios da tabela: 20 + 20 + 15 + 10 = **65** | **Aberto** | Esclarecer o máximo real e o corte de 70% (42 ou 45,5 pontos). Esclarecer como os critérios de 65 pontos são normalizados para 60. |
| **C-06** | Migração de logs históricos | RFP e Anexo I: não preveem | PPT s5: migrar **24 meses** de logs do SIEM legado | Expectativa não formalizada | Tratar como **opcional precificado à parte** ou como premissa explícita. Volume desconhecido. A janela é curta (SIEM legado termina em 31/01/2027). Perguntar o formato, o volume e quem extrai os dados do legado. |
| **C-07** | Escopo das subsidiárias | RFP §2.1: "colaboradores" do Banco | PPT s5-notas: Horizonte Seguros e Horizonte Investimentos "também deverão ser incluídas" | Informação só nas anotações | Pedir formalização. As subsidiárias são outras pessoas jurídicas e podem ter regulação própria (por exemplo, a de seguros). Perguntar quem contrata e quem paga. |
| **C-08** | Subcontratação × SIEM em nuvem | RFP §7.7: subcontratação vedada, total ou parcial | AnxI §1.2: SIEM pode ficar em nuvem pública. QT-05: threat intelligence (normalmente de terceiros) | **Aberto** | Perguntar se o uso de provedor de nuvem (IaaS/SaaS), de licenças de fabricantes e de feeds de inteligência conta como subcontratação. Sem essa confirmação, a oferta típica de SIEM SaaS fica em risco. |
| **C-09** | Preenchimento do questionário | RFP §4.4: questionário "integralmente preenchido" (sem sanção) | XLSX Instr.: "todas as abas" são obrigatórias; incompleto é **desclassificado** | Regra mais severa no XLSX | Preencher 100% da aba "Questionário Técnico" (respostas e comentários). Perguntar o que significa "todas as abas": a de Q&A já vem preenchida e a de Pesos está oculta. |
| **C-10** | Penalidade oculta | RFP §6: não prevê desconto | XLSX Pesos (oculta): cada "Não atende" em item não obrigatório tira 2 pontos | Regra não publicada no corpo da RFP | Evitar "Não atende" em QT-02 (SOAR) e QT-05 (threat intelligence). Quando possível, oferecer "Atende" ou "Parcial" com justificativa. Pedir que a regra seja formalizada e que se explique o uso dos pesos (soma 13). |
| **C-11** | Analistas N1 | AnxI §5.2: presenciais na sede em São Paulo, em horário comercial | QA #6: remoto permitido em território nacional | **Resolvido pela Q&A** | Adotar o modelo remoto no Brasil e registrar a referência à QA #6 na proposta. |
| **C-12** | Prazo de entrega | RFP §3.1: 20/11/2026 | QA #1: 27/11/2026, até as 18h | **Resolvido pela Q&A** | Data vigente: 27/11/2026, 18h. |
| **C-13** | Início dos serviços × prorrogação | RFP §3.1: início em 01/02/2027 | QA #1 adiou a entrega em 7 dias sem mudar o início. PPT s3: legado acaba em 31/01/2027 | Implícito | Ver a seção 3: janela de 66 dias. Explicitar as premissas de data de assinatura. |
| **C-14** | Meta de falsos positivos | PPT s4: 10% no 1º trimestre | Não está entre os SLAs do Anexo I | Expectativa | Não aceitar como SLA. Propor como meta de melhoria (*best effort*) com plano de *tuning*. |
| **C-15** | Equipe certificada | RFP §5.2: "devidamente certificada" (habilitação?) | AnxI §5.1: CISSP para o coordenador. QT-06: "reconhecidas pelo mercado" | Vago | Apresentar a matriz de certificações da equipe (CISSP, GIAC, CompTIA, fabricantes de SIEM/IAM). Perguntar se há certificações mínimas por papel. |

---

## 6. Informações fora do corpo formal (conteúdo oculto ou informal)

| Local | Conteúdo | Por que importa |
|---|---|---|
| PDF, p.6 (imagem digitalizada, sem camada de texto) | Anexo III — Declaração de Localização de Dados: dados e logs só no Brasil; declaração assinada pelo representante legal "sob pena de inabilitação" | Um leitor automático que só extraia texto não veria essa exigência. Ela anula a "região de livre escolha" do AnxI §1.2. |
| PPTX, anotações do apresentador do s5 | Inclusão das subsidiárias (cerca de 900 usuários) | Aumenta o escopo em cerca de 20%. Não é visível no modo de apresentação. |
| XLSX, aba oculta "Pesos" | Pesos QT-01 = 3, QT-02 = 1, QT-03 = 2, QT-04 = 3, QT-05 = 2, QT-06 = 2. Regra: cada "Não atende" em requisito não obrigatório tira 2 pontos da Nota Técnica | Critério de pontuação não divulgado na RFP. Impacto máximo identificado: −4 pontos (QT-02 e QT-05). |
| XLSX, aba "Instruções" | Questionário incompleto leva à desclassificação | Sanção que não está na RFP. |
| Metadados do DOCX e do PPTX | Datas de 2013 e autor "python-docx" | Não permitem controlar versões. Usar só a versão e a data declaradas no corpo. |

---

## 7. Riscos

**Escala:** P = probabilidade, I = impacto (A = alta, M = média, B = baixa).

| ID | Risco | Fonte | P | I | Mitigação proposta |
|---|---|---|---|---|---|
| RK-01 | **Multas sem teto.** São 10% do valor mensal por ocorrência. Com 3 SLAs de periodicidade alta (15 minutos, 99,9%, relatório), poucas falhas no mês podem consumir toda a receita mensal. | RFP §7.4; QA #4 | A | A | Propor teto (por exemplo, 10% a 20% do mensal), gradação por severidade, período de carência na transição e exclusões (causa do cliente, força maior). Avaliar ressalva formal × risco de desclassificação. |
| RK-02 | **Responsabilidade integral e ilimitada** por danos de incidentes de segurança no ambiente do cliente, mesmo sem culpa do SOC | RFP §7.5 | M | A | Propor limite (por exemplo, 12 meses de faturamento), exclusão de lucros cessantes e danos indiretos, e nexo causal com culpa ou dolo. Validar com o jurídico e com a seguradora. |
| RK-03 | **Seguro cibernético** sem valor definido e difícil de contratar diante de responsabilidade ilimitada | RFP §7.6 | M | M | Perguntar o valor mínimo. Fazer cotação com a corretora antes da entrega. |
| RK-04 | **Cronograma de transição inviável:** conflito entre 30 e 60 dias, legado termina em 31/01/2027, janela de 66 dias da entrega ao início | RFP §3.2; AnxI §4.1; PPT s3 | A | A | Plano de transição acelerado com premissas de data (assinatura até X, documentação até D+10, VPN em D+5). Propor ponte (extensão do legado ou ingestão temporária). Plano de transição vale 10 pontos [RFP §6.2]. |
| RK-05 | **EPS não informado.** Licenciamento e armazenamento do SIEM (12 meses online e 5 anos) não podem ser dimensionados | QA #3 | A | A | Estimar o EPS com base em 850 servidores, 2 DCs, 2 nuvens e 5.000 a 7.100 usuários (por exemplo, 3.000 a 8.000 EPS). Precificar por faixa com preço por EPS ou GB/dia excedente. Declarar a premissa. |
| RK-06 | **Escopo de usuários subdimensionado:** 5.000 pela Q&A contra 6.200 a 7.100 reais | QA #5; PPT s2; PPT s5-notas | A | M | Preço unitário por usuário adicional e cláusula de revisão de volume. |
| RK-07 | **Migração de 24 meses de logs** implícita, com volume e formato desconhecidos | PPT s5 | M | A | Excluir do preço-base e oferecer como opcional com premissas. |
| RK-08 | **Inabilitação pela localização de dados** se a solução SaaS do SIEM processar dados fora do país | Anexo III; AnxI §1.2 | M | A | Escolher fabricante/região com residência de dados no Brasil e comprovar por escrito. |
| RK-09 | **Subcontratação vedada** pode alcançar nuvem, fabricante de SIEM ou threat intelligence | RFP §7.7 | M | A | Esclarecer. Estruturar a oferta como fornecimento de licenças/serviços de terceiros sob responsabilidade do proponente, não como subcontratação da operação. |
| RK-10 | **SLA de 15 minutos dependente da matriz do cliente**, que não foi fornecida e pode ser reclassificada | AnxI §2.1, §2.4 | M | A | Pedir a matriz. Propor critérios objetivos de "incidente crítico" e o momento em que o relógio começa. |
| RK-11 | **"Todos os ativos relevantes"** é um escopo aberto de integração | AnxI §1.4 | A | M | Lista de fontes de log como anexo da proposta. Novas fontes tratadas como mudança de escopo. |
| RK-12 | **Revogação em 24h** depende de o RH comunicar desligamentos a tempo | AnxI §3.1 | M | M | O relógio começa com o recebimento do evento do RH. Prever integração com o RH. |
| RK-13 | **Custo da operação em paralelo** sem remuneração | AnxI §4.2 | A | M | Embutir no preço de setup ou no 1º mês. |
| RK-14 | **Custo do coordenador CISSP dedicado** | AnxI §5.1 | A | B | Prever no preço. |
| RK-15 | **Fluxo de caixa:** pagamento em 60 dias mais investimento inicial em SIEM e transição | RFP §7.3 | A | M | Precificar o custo financeiro. Propor parcela de setup. |
| RK-16 | **Desclassificação técnica:** corte de 70% e penalidade oculta de −2 por "Não atende" | RFP §6.3; XLSX Pesos | M | A | Oferecer SOAR e threat intelligence pelo menos como "Parcial". Investir nos critérios de 20 pontos. |
| RK-17 | **Desclassificação formal:** questionário incompleto ou Anexo IV ausente | XLSX Instr.; RFP §4.3 | M | A | Checklist de entrega (seção 8). Pedir o Anexo IV com urgência. |
| RK-18 | **Meta de falsos positivos (70% → 10%)** virar obrigação na negociação | PPT s4 | M | M | Tratar como meta com plano de *tuning*. Não aceitar como SLA. |
| RK-19 | **Escopo regulatório das subsidiárias**: seguradora e gestora podem ter regras próprias | PPT s5-notas | B | M | Esclarecer antes de assumir. |

---

## 8. Checklist de inabilitação e desclassificação

| # | Gatilho | Fonte | Ação |
|---|---|---|---|
| 1 | Falta de ISO/IEC 27001 vigente, acreditada, com escopo que inclua o SOC | RFP §5.1a | Juntar o certificado e a declaração de escopo |
| 2 | Menos de 3 atestados de SOC em instituições financeiras com 2.000 usuários ou mais | RFP §5.1b | Separar atestados que citem o número de usuários |
| 3 | SOC fora do Brasil | RFP §5.1c; QA #2 | Comprovar o endereço do SOC |
| 4 | Falta da declaração do Anexo III assinada | RFP p.6 / Anexo III | Assinatura do representante legal; preencher local e data |
| 5 | Equipe sem certificação (critério vago) | RFP §5.2 | Matriz de certificações e cópias dos certificados |
| 6 | Nota Técnica abaixo de 70% do máximo | RFP §6.3 | Ver C-05 |
| 7 | Questionário técnico incompleto | XLSX Instr.; RFP §4.4 | Preencher todas as linhas e colunas |
| 8 | Proposta comercial fora do modelo do Anexo IV | RFP §4.3 | Obter o Anexo IV |
| 9 | Entrega fora do portal, fora do prazo (27/11/2026, 18h) ou em outro idioma | RFP §4.1; QA #1 | Fazer o upload com antecedência |

---

## 9. Pedidos de esclarecimento sugeridos

O prazo formal de perguntas (05/11/2026) já terá passado. Sugiro solicitar uma rodada extraordinária ou, se não houver, registrar as interpretações como **premissas e ressalvas** na proposta.

1. **Transição (C-01):** qual prazo prevalece, 30 dias [RFP §3.2] ou 60 dias [AnxI §4.1]? Qual é a data prevista de assinatura?
2. **Continuidade do SIEM legado:** com o fim do contrato em 31/01/2027 [PPT s3], como será a operação em paralelo [AnxI §4.2] se a assinatura atrasar? É possível uma ponte?
3. **Localização dos dados (C-02):** confirmam que o Anexo III prevalece sobre a "região de livre escolha" do AnxI §1.2, e que backup, DR e arquivamento de 5 anos também ficam no Brasil?
4. **Usuários (C-03 / C-07):** os 5.000 usuários [QA #5] incluem a Horizonte Seguros e a Horizonte Investimentos? O que explica os 6.200 usuários ativos [PPT s2]? As subsidiárias farão parte do contrato e quem é a contratante?
5. **EPS e fontes de log (QA #3):** podem informar ao menos uma faixa de EPS, GB/dia ou o inventário de fontes, para permitir proposta comparável entre os concorrentes?
6. **Retenção (C-04):** confirmam 12 meses online e 5 anos em arquivamento?
7. **Migração (C-06):** a migração de 24 meses de logs [PPT s5] faz parte do escopo? Qual é o volume e o formato de exportação?
8. **Pontuação (C-05 / C-10):** qual é o máximo da Nota Técnica (60 ou 65)? Como os pesos da aba "Pesos" e o desconto de 2 pontos são aplicados? Qual é a fórmula da Nota de Preço?
9. **Subcontratação (C-08):** o uso de nuvem pública, de SaaS do fabricante e de feeds de threat intelligence conta como subcontratação?
10. **Anexo IV:** pedem o envio da Planilha de Preços. O Anexo II existe?
11. **Matriz de criticidade (AnxI §2.4):** podem enviar a matriz e o critério de início da contagem dos 15 minutos?
12. **Multas e responsabilidade (RFP §7.4 e §7.5):** aceitam teto de multas e limite de responsabilidade? Qual é o valor mínimo do seguro cibernético (RFP §7.6)?
13. **IAM:** o proponente deve fornecer a plataforma de IGA e MFA ou operar as ferramentas atuais (AD e scripts)? O PAM, que é desejável, pontua?
14. **Questionário (C-09):** "todas as abas" se refere só à aba "Questionário Técnico"?

---

## 10. Premissas recomendadas para a proposta

- Dimensionamento com **5.000 usuários** [QA #5] e preço unitário para usuários adicionais, inclusive os das subsidiárias.
- **EPS de referência declarado** pelo proponente, com tabela de excedente por EPS ou GB/dia.
- **SIEM hospedado só em região brasileira**, incluindo backup, DR e arquivamento [Anexo III].
- Retenção de **12 meses online e 5 anos em arquivamento**, com preço do arquivamento discriminado.
- **Migração de logs históricos fora do preço-base**, como item opcional.
- **Analistas N1 remotos no Brasil** [QA #6].
- **Transição planejada em 30 dias**, condicionada à documentação em D+10 e à VPN disponível no início.
- Meta de falsos positivos tratada como **objetivo de melhoria**, não como SLA.
- Ressalvas jurídicas (teto de multas, limite de responsabilidade) somente depois de avaliar o risco de desclassificação com o jurídico.

---

## 11. Avaliação técnica e foco de pontuação

| Critério [RFP §6.2] | Pontos | Onde concentrar esforço |
|---|---|---|
| Metodologia de operação do SOC | 20 | Processo de triagem e *tuning* (resposta ao problema de 70% de falsos positivos), playbooks, SLA de 15 minutos, aderência à Res. CMN 4.893 |
| Qualificação da equipe | 20 | CISSP do coordenador, matriz de certificações, currículos, atestados |
| Ferramentas e tecnologia | 15 | SIEM com residência de dados no Brasil, SOAR (QT-02), threat intelligence (QT-05), PAM opcional |
| Plano de transição | 10 | Plano de 30 dias com marcos, operação em paralelo, mitigação da data de 31/01/2027 e migração de logs |
| **Soma** | **65** | **Diverge do máximo declarado de 60 (C-05)** |

Ajustes do questionário [XLSX Pesos]: −2 pontos para cada "Não atende" em item não obrigatório (QT-02, QT-05).

---

## 12. Limitações desta análise

- A p.6 do PDF foi lida a partir da imagem renderizada (inspeção visual), sem OCR validado. A transcrição do Anexo III é fiel ao conteúdo visível.
- O Anexo IV, o Anexo II e a matriz de criticidade não foram fornecidos, então não foram analisados.
- Não há informação de valor estimado, volumetria (EPS) nem inventário de ativos. Toda conclusão de preço depende de premissas.
- O modelo de recomendação jurídica (aceitar ou ressalvar cláusulas) precisa de validação do jurídico do proponente.
- As referências à Res. CMN 4.893/2021 aparecem como citadas nos documentos. Não verifiquei se a norma está vigente nem se houve alterações posteriores.
