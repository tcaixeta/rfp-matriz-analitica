# Análise da RFP nº 2026-017 — Serviços Gerenciados de SOC e IAM

| Campo | Valor |
|---|---|
| Cliente | Banco Horizonte Fictício S.A. |
| Processo | RFP nº 2026-017 |
| Objeto | Serviços gerenciados de SOC (24x7x365) e de IAM |
| Valor estimado | Não informado (e não pôde ser inferido: a planilha de preços não foi recebida, ver seção 1.2) |
| Data desta análise | 17/10/2026 |
| Documentos efetivamente analisados | 4 de 5 listados |

**Convenção de citação:** `[D1 p.X/impr.Y, item Z]` = documento nº 1, página física X do PDF (a numeração impressa no rodapé é Y, porque a capa não é numerada), item Z. `[D2 item Z]` = Anexo I. `[D3 slide N]` = apresentação. `[D4 aba, linha]` = planilha de Q&A e questionário.

---

## 1. Inventário dos documentos

### 1.1 Documentos listados × documentos recebidos

| # | Arquivo listado | Tipo | Versão/Data informada | Recebido? | Situação da leitura |
|---|---|---|---|---|---|
| 1 | RFP-2026-017_Servicos_SOC_IAM.pdf | RFP | v1.0 — 15/10/2026 | **Sim** | Lido. 6 páginas físicas. Págs. 1 a 5 com texto extraível. **Pág. 6 é imagem digitalizada, sem camada de texto** (Anexo III embutido). Li o conteúdo visualmente; a transcrição está na seção 2.1. |
| 2 | Anexo_I_Especificacao_Tecnica.docx | Anexo técnico | v1.0 — 15/10/2026 | **Sim** | Lido integralmente (6 seções, 21 itens). Não há controle de alterações, comentários nem texto oculto. Versão e data no corpo conferem com a lista. |
| 3 | Apresentacao_Ambiente_Atual.pptx | Apresentação | 22/10/2026 | **Sim** | Lido integralmente (5 slides, sem slides ocultos). **O slide 5 tem nota do apresentador com informação de escopo** que não aparece nos slides (ver C-03). |
| 4 | QA_Rodada1_e_Questionario.xlsx | Q&A e questionário | 12/11/2026 | **Sim** | Lido integralmente: 4 abas, sendo **1 oculta ("Pesos")** com regra de pontuação (ver C-08). |
| 5 | Anexo_IV_Planilha_de_Precos.xlsx | Planilha de preços | v1.0 | **NÃO** | **Arquivo listado na solicitação mas não anexado.** Não foi analisado. Nenhum conteúdo dele foi presumido nesta análise. |

### 1.2 Pendência crítica de inventário: Anexo IV não recebido

- A RFP exige que a proposta comercial siga "a planilha modelo do Anexo IV — Planilha de Preços" [D1 p.3/impr.2, item 4.3].
- Sem o arquivo, **ficam fora desta análise**: a estrutura de preços (itens, unidades e se o preço é fixo ou por usuário/EPS/ativo), as fórmulas, a existência de item opcional para PAM, o tratamento da operação paralela na transição [D2 item 4.2], a migração de logs históricos [D3 slide 5], a franquia de volumetria e qualquer critério de cálculo da Nota de Preço (40% da nota final [D1 p.4/impr.3, item 6.1]).
- **Ação:** reenviar o arquivo `Anexo_IV_Planilha_de_Precos.xlsx`. Esta análise deve ser complementada quando ele chegar, porque vários conflitos abaixo (C-01, C-04, C-05, C-09) têm impacto direto no preço.

### 1.3 Documentos citados ou implícitos que não constam do pacote

| Referência | Onde aparece | Situação |
|---|---|---|
| Anexo II | Nenhuma menção | O pacote tem Anexo I, III (dentro do PDF) e IV, mas **o Anexo II não é citado em nenhum lugar**. Confirmar se existe (por exemplo minuta de contrato ou acordo de nível de serviço) e se foi omitido. |
| Anexo III — Declaração de Localização de Dados | Só como imagem na pág. 6 do PDF | **O corpo da RFP não cita o Anexo III**: os itens 4 e 5 não o mencionam. Mesmo assim, ele prevê **inabilitação** se não for entregue (ver H-05). |
| Matriz de classificação de criticidade do Contratante | [D2 item 2.4] | Não fornecida. O SLA de 15 minutos [D2 item 2.1] depende dela. |
| Minuta de contrato | Implícita no item 7 da RFP | Não fornecida. |
| Documentação técnica do ambiente | [D2 item 6.2] | Só será entregue em até 10 dias após a assinatura. |
| Portal de fornecedores | [D1 p.3/impr.2, item 4.1] | Endereço e regras de envio (formato, tamanho) não informados. |

### 1.4 Observações sobre datas e versões

- **As datas dos documentos 3 e 4 (22/10/2026 e 12/11/2026) são posteriores à data desta análise (17/10/2026).** O PDF também foi gerado em 17/10/2026 (metadados). Há duas hipóteses: a data de referência do processo não é a data de hoje, ou os documentos foram pré-datados. **Confirmar qual é a data de referência**, porque isso define se o prazo de perguntas (05/11/2026) ainda está aberto (ver seção 6).
- Todos os documentos têm a marca "DOCUMENTO FICTÍCIO PARA TESTE".
- Os metadados de criação do .docx e do .pptx (2013) vêm do modelo usado e não têm relevância.
- **Hierarquia adotada nesta análise:** quando há conflito, prevalece o esclarecimento formal mais recente (Q&A de 12/11/2026). Depois vêm a RFP e o Anexo I. A apresentação (D3) é tratada como **informativa**, sem força vinculante, até haver confirmação formal. **A RFP não define essa hierarquia**, e isso também precisa ser esclarecido (Q-01).

---

## 2. Síntese do processo

### 2.1 Transcrição do Anexo III (pág. 6 do PDF, imagem)

> **ANEXO III — DECLARAÇÃO DE LOCALIZAÇÃO DE DADOS.** O proponente declara que todos os dados do Banco, incluindo os registros (logs) de segurança, serão armazenados e processados exclusivamente em território nacional durante toda a vigência do contrato. A declaração deve ser entregue assinada pelo representante legal junto com a proposta, sob pena de inabilitação. Campos de local e data "___ de ______ de 2026" e assinatura.

### 2.2 Cronograma consolidado

| Etapa | RFP [D1 p.2/impr.1, item 3.1] | Atualização | Data vigente |
|---|---|---|---|
| Publicação | 15/10/2026 | — | 15/10/2026 |
| Workshop do ambiente | 22/10/2026 | D3 tem essa data | 22/10/2026 |
| Prazo para perguntas | 05/11/2026 | — | 05/11/2026 |
| Respostas | 12/11/2026 | D4 tem essa data | 12/11/2026 |
| **Entrega das propostas** | 20/11/2026, 18h | **Prorrogada para 27/11/2026, 18h** [D4 Q&A nº 1] | **27/11/2026, 18h** |
| Início dos serviços | 01/02/2027 | — | 01/02/2027 |
| Fim do contrato do SIEM legado | — | 31/01/2027, sem prorrogação [D3 slide 3] | 31/01/2027 |
| Conclusão da transição | 30 dias após assinatura [D1 item 3.2] | **60 dias** [D2 item 4.1] | **Indefinida** (C-02) |

### 2.3 Números do ambiente

| Dado | Valor | Fonte |
|---|---|---|
| Colaboradores ou usuários | 4.500 / 5.000 / 6.200 / +900 | Ver C-03 |
| Servidores | 850 (70% Windows, 30% Linux) | [D3 slide 2] |
| Data centers | 2 próprios (São Paulo e Campinas) | [D3 slide 2] |
| Nuvens públicas | 2 (provedores não informados) | [D3 slide 2] |
| Alertas por dia | ~1.200, com 70% de falsos positivos | [D3 slide 4] |
| Volumetria de eventos por segundo (EPS) | **Só será informada ao vencedor** | [D4 Q&A nº 3] |
| IAM atual | Active Directory + scripts internos | [D3 slide 3] |
| PAM atual | Inexistente | [D3 slide 3] |

---

## 3. Matriz de requisitos

Legenda de **Natureza**: **ELIM** = eliminatório (inabilitação ou desclassificação), **OBR** = obrigatório (descumprir gera penalidade contratual), **DES** = desejável, **INF** = informativo ou expectativa sem força formal, **CTR** = cláusula contratual ou comercial.
Legenda de **Status**: **OK** = claro; **CONFLITO** = há divergência entre documentos; **AMBÍGUO** = redação imprecisa; **LACUNA** = falta informação para atender ou precificar.

### 3.1 Habilitação e forma da proposta

| ID | Requisito | Fonte | Natureza | Status | Observação |
|---|---|---|---|---|---|
| H-01 | Certificado ISO/IEC 27001 vigente, de organismo acreditado, com escopo que inclua os serviços de SOC | [D1 p.3/impr.2, item 5.1a]; [D4 QT-01] | ELIM | OK | Conferir se o escopo do certificado cita SOC de forma explícita. O escopo não precisa cobrir IAM. |
| H-02 | Mínimo de 3 atestados de SOC para instituições financeiras, com ambiente de ≥ 2.000 usuários | [D1 item 5.1b] | ELIM | AMBÍGUO | Não diz se os 2.000 usuários são por atestado ou somados, nem se os serviços precisam estar em andamento. Não pede atestado de IAM. |
| H-03 | SOC localizado em território nacional | [D1 item 5.1c]; [D4 Q&A nº 2] | ELIM | OK | Confirmado no Q&A. Não diz qual documento comprova. |
| H-04 | Equipe técnica "devidamente certificada" | [D1 item 5.2]; [D4 QT-06] | ELIM? | AMBÍGUO | Não define quais certificações nem quantos profissionais. Fica no capítulo de habilitação, mas não diz se é motivo de inabilitação. |
| H-05 | Declaração de Localização de Dados (Anexo III) assinada pelo representante legal | [D1 p.6, Anexo III] | ELIM | CONFLITO | Prevê inabilitação, mas não é citada no item 5. **Conflita com D2 item 1.2** (C-05). |
| H-06 | Proposta em português, enviada só pelo portal | [D1 item 4.1] | ELIM? | LACUNA | Portal não identificado. |
| H-07 | Proposta técnica com no máximo 40 páginas, sem contar os anexos | [D1 item 4.2] | OBR | OK | Não diz qual é a consequência de exceder o limite. |
| H-08 | Proposta comercial no modelo do Anexo IV | [D1 item 4.3] | OBR | **LACUNA** | **Anexo IV não recebido.** |
| H-09 | Questionário técnico preenchido integralmente | [D1 item 4.4]; [D4 aba Instruções A3] | ELIM | AMBÍGUO | A planilha diz que "todas as abas" são obrigatórias e que questionário incompleto é desclassificado. Mas a aba de Q&A já vem respondida e a aba "Pesos" está oculta. Na prática, preencher as colunas D e E da aba "Questionário Técnico". |
| H-10 | Nota Técnica mínima de 70% da máxima | [D1 p.4/impr.3, item 6.3] | ELIM | CONFLITO | A pontuação máxima é inconsistente (C-07). |

### 3.2 Requisitos técnicos — SOC

| ID | Requisito | Fonte | Natureza | Status | Observação |
|---|---|---|---|---|---|
| S-01 | Monitoramento contínuo 24x7x365 | [D1 item 2.1]; [D2 item 1.1] | OBR | OK | — |
| S-02 | Fornecer a solução de SIEM, podendo ser em nuvem pública "em região de livre escolha" | [D2 item 1.2] | OBR | **CONFLITO** | Contraria o Anexo III e a Resolução CMN 4.893/2021 (C-05). |
| S-03 | Retenção de logs por no mínimo 12 meses | [D2 item 1.3]; [D4 QT-03: "online"] | OBR | CONFLITO | Diverge do item 1.6 (C-04). |
| S-04 | Retenção de logs por 5 anos "para fins de auditoria" | [D2 item 1.6] | OBR | CONFLITO | Ver C-04. Impacto alto em armazenamento. |
| S-05 | SIEM integrado a "todos os ativos relevantes" | [D2 item 1.4] | OBR | **LACUNA** | "Relevantes" não está definido. A volumetria de eventos foi negada [D4 Q&A nº 3]. Impossível dimensionar com segurança (C-09). |
| S-06 | Resposta a incidentes: contenção, erradicação e relatório pós-incidente | [D2 item 1.5] | OBR | AMBÍGUO | Não diz se a resposta é remota ou presencial, nem se inclui forense, recuperação ou limite de horas. |
| S-07 | Migração de 24 meses de logs históricos do SIEM legado | [D3 slide 5] | INF | LACUNA | Só aparece na apresentação. Não tem volume, formato nem previsão no Anexo I. Precisa entrar no preço se for confirmada (C-10). |
| S-08 | Reduzir os falsos positivos de 70% para 10% no 1º trimestre | [D3 slide 4] | INF | AMBÍGUO | Chamada de "meta". Não está no Anexo I. Risco de virar cobrança contratual (C-11). |
| S-09 | Visão unificada de riscos para a diretoria | [D3 slide 5] | INF | AMBÍGUO | Não especificada (painel? relatório?). |
| S-10 | Integração com SOAR | [D4 QT-02] | DES | OK | Não obrigatória, mas responder "Não atende" **custa 2 pontos** (C-08). |
| S-11 | Threat intelligence | [D4 QT-05] | DES | OK | Idem: responder "Não atende" custa 2 pontos. |
| S-12 | Aderência à Resolução CMN 4.893/2021 | [D1 item 1.2]; [D4 QT-04] | ELIM? | OK | Obrigatório no questionário. Reforça o problema de C-05. |

### 3.3 Níveis de serviço (SLA)

| ID | Requisito | Fonte | Natureza | Status | Observação |
|---|---|---|---|---|---|
| N-01 | Iniciar o tratamento de incidente crítico em até 15 minutos | [D2 item 2.1] | OBR | LACUNA | A criticidade segue a matriz do Contratante [D2 item 2.4], que não foi fornecida. Não define a partir de quando o tempo é contado (alerta, triagem ou abertura de chamado). |
| N-02 | Disponibilidade mensal mínima do SIEM de 99,9% | [D2 item 2.2] | OBR | AMBÍGUO | Não define janelas de manutenção nem exclusões. Se o SIEM rodar em nuvem de terceiro, a disponibilidade depende do SLA do provedor de nuvem. |
| N-03 | Relatório mensal até o 5º dia útil | [D2 item 2.3] | OBR | OK | — |
| N-04 | Multa de 10% do valor mensal **por ocorrência** de descumprimento de SLA, sem teto | [D1 p.5/impr.4, item 7.4]; [D4 Q&A nº 4] | CTR | **RISCO CRÍTICO** | O Q&A manteve a cláusula sem limite. Com 10 ocorrências, a multa chega a 100% do valor mensal (C-06). |

### 3.4 IAM

| ID | Requisito | Fonte | Natureza | Status | Observação |
|---|---|---|---|---|---|
| I-01 | Ciclo de vida das identidades (admissão, movimentação e desligamento) | [D2 item 3.1] | OBR | LACUNA | Não diz se o IAM é serviço gerenciado sobre a ferramenta do cliente (hoje AD + scripts) ou se o proponente fornece a plataforma. Integração com RH e sistemas-alvo não informada. |
| I-02 | Revogar o acesso de desligados em até 24h | [D2 item 3.1] | OBR | AMBÍGUO | Contar 24h a partir de quê? Da comunicação do RH ou da data do desligamento? |
| I-03 | MFA para 100% dos usuários com acesso privilegiado | [D2 item 3.2] | OBR | LACUNA | Não diz quem fornece o MFA nem quantos são os usuários privilegiados. |
| I-04 | Recertificação trimestral dos acessos | [D2 item 3.3] | OBR | OK | Não define quantos sistemas entram na revisão. |
| I-05 | Cofre de senhas para contas privilegiadas (PAM) | [D2 item 3.4] | DES | LACUNA | O cliente não tem PAM hoje [D3 slide 3]. Não se sabe se deve ser cotado como opcional (depende do Anexo IV). |
| I-06 | Número de identidades sob gestão | Ver C-03 | — | **CONFLITO** | — |

### 3.5 Transição, equipe e responsabilidades

| ID | Requisito | Fonte | Natureza | Status | Observação |
|---|---|---|---|---|---|
| T-01 | Concluir a transição em 30 dias | [D1 item 3.2] | OBR | **CONFLITO** | O Anexo I fala em 60 dias (C-02). |
| T-02 | Operação paralela com o fornecedor atual, sem custo adicional | [D2 item 4.2] | OBR | AMBÍGUO | Custo absorvido pelo proponente. A duração depende de T-01. |
| T-03 | Coordenador com certificação CISSP, dedicado exclusivamente | [D2 item 5.1] | OBR | OK | Custo fixo relevante. Não diz se a atuação é presencial. |
| T-04 | Analistas de nível 1 presenciais na sede (SP), em horário comercial | [D2 item 5.2] | OBR | **ALTERADO** | O Q&A nº 6 permite atuação remota em território nacional (C-12). |
| T-05 | O Contratante fornece VPN | [D2 item 6.1] | — | OK | — |
| T-06 | O Contratante entrega a documentação técnica em até 10 dias após a assinatura | [D2 item 6.2] | — | RISCO | Fica muito em cima de uma transição de 30 dias. |

### 3.6 Condições comerciais e contratuais

| ID | Cláusula | Fonte | Status | Observação |
|---|---|---|---|---|
| K-01 | Vigência de 36 meses, prorrogável por iguais períodos | [D1 item 7.1] | OK | — |
| K-02 | Reajuste anual pelo IPCA | [D1 item 7.2] | OK | Não diz qual é a data-base. |
| K-03 | Pagamento em até 60 dias após o aceite da nota fiscal | [D1 item 7.3] | RISCO | Prazo longo, com impacto no fluxo de caixa. Não há prazo para o aceite. |
| K-04 | Multa de 10% do valor mensal por ocorrência de SLA, sem teto | [D1 item 7.4]; [D4 Q&A nº 4] | **CRÍTICO** | C-06. |
| K-05 | Responsabilidade **integral e ilimitada** por danos de incidentes de segurança | [D1 item 7.5] | **CRÍTICO** | C-06. |
| K-06 | Seguro cibernético "em valor compatível" | [D1 item 7.6] | AMBÍGUO | Não diz qual é o valor mínimo. É incoerente com uma responsabilidade ilimitada. |
| K-07 | Subcontratação vedada, total ou parcial | [D1 item 7.7] | **CONFLITO** | C-13: uso de nuvem pública ou ferramentas de terceiros. |
| K-08 | Confidencialidade por 5 anos após o término | [D1 item 7.8] | OK | — |

---

## 4. Conflitos e inconsistências entre documentos

| ID | Tema | Versões conflitantes | Prevalência provável | Impacto | Gravidade |
|---|---|---|---|---|---|
| **C-01** | Prazo de entrega da proposta | RFP 3.1: 20/11/2026, 18h × Q&A nº 1: **27/11/2026, 18h** | Q&A (mais recente e formal) | Planejamento interno | Média (resolvido) |
| **C-02** | Prazo da transição | RFP 3.2: **30 dias** × Anexo I 4.1: **60 dias** | **Indefinida.** Não há regra de hierarquia | Custo da operação paralela, equipe de transição, nota do critério "Plano de transição" (10 pts) | **Alta** |
| **C-03** | Número de usuários | RFP 2.1: ~4.500 colaboradores × Q&A nº 5: **5.000** × D3 slide 2: **6.200 usuários ativos** × D3 slide 5 (só nas **notas do apresentador**): **+~900 das subsidiárias** Horizonte Seguros e Horizonte Investimentos, ou seja, ~7.100 | Q&A (5.000) para o dimensionamento formal. Mas o próprio Banco mostra 6.200 ativos e uma possível ampliação de escopo que não foi formalizada | Diferença de até 42% sobre a base do Q&A no dimensionamento de IAM e licenças. A inclusão das subsidiárias muda o objeto (outras pessoas jurídicas, possivelmente outros reguladores) | **Alta** |
| **C-04** | Retenção de logs | Anexo I 1.3: mínimo de 12 meses × Anexo I 1.6: 5 anos para auditoria × QT-03: 12 meses "online" × D3 slide 5: migrar 24 meses do legado | Interpretação provável: 12 meses online + 5 anos no total (em armazenamento frio). **Não está confirmado** | Custo de armazenamento multiplicado por ~5. Os 24 meses migrados entram ou não na janela de 5 anos? | **Alta** |
| **C-05** | Localização dos dados | Anexo I 1.2: SIEM em nuvem pública "em região de livre escolha" × Anexo III: dados e logs **exclusivamente em território nacional**, sob pena de inabilitação × RFP 1.2: sujeição à Resolução CMN 4.893/2021 | Anexo III, por ser eliminatório e mais restritivo | Uma solução em região estrangeira, ainda que permitida pelo Anexo I, inabilita o proponente. **A arquitetura precisa usar região no Brasil** | **Crítica** |
| **C-06** | Exposição contratual | RFP 7.4: multa de 10% do valor mensal por ocorrência, sem teto (mantida no Q&A nº 4) + RFP 7.5: responsabilidade ilimitada + RFP 7.6: seguro "compatível" | — | Exposição financeira sem limite. Pode inviabilizar a participação ou exigir prêmio de risco alto no preço | **Crítica** |
| **C-07** | Pontuação técnica máxima | RFP 6.2: "máximo 60 pontos" × soma dos critérios = 20 + 20 + 15 + 10 = **65** | Indefinida | O corte de 70% fica em 42 pontos (sobre 60) ou 45,5 (sobre 65). Se a nota de 65 for normalizada para 60, os pesos efetivos mudam | **Alta** |
| **C-08** | Regra de pontuação oculta | Aba **oculta** "Pesos" [D4]: pesos 1 a 3 por item do questionário e "requisitos não obrigatórios respondidos como 'Não atende' reduzem a Nota Técnica em 2 pontos cada" × RFP item 6: nenhuma menção ao questionário na nota | Indefinida. A regra não foi publicada formalmente | QT-02 (SOAR) e QT-05 (threat intelligence), mesmo "não obrigatórios", valem até 4 pontos negativos. Não se sabe como os pesos entram na nota | **Alta** |
| **C-09** | Dimensionamento do SIEM | Anexo I 1.4: integrar "todos os ativos relevantes" × Q&A nº 3: volumetria de eventos só para o vencedor | — | O preço de SIEM, armazenamento e retenção depende da volumetria. Há risco de subprecificar ou de ficar caro demais. Base indireta disponível: 850 servidores, 2 DCs, 2 nuvens, ~1.200 alertas/dia | **Alta** |
| **C-10** | Migração de logs históricos | Só em D3 slide 5 (24 meses). Ausente no Anexo I | Não vinculante até ser confirmada | Volume desconhecido e prazo apertado (o SIEM legado acaba em 31/01/2027) | Média |
| **C-11** | Meta de falsos positivos | D3 slide 4: 10% no 1º trimestre. Ausente no Anexo I e no SLA | Informativa | Risco de virar cobrança informal ou critério de aceite | Média |
| **C-12** | Atuação presencial do nível 1 | Anexo I 5.2: presencial em SP, horário comercial × Q&A nº 6: remoto permitido no Brasil | Q&A | Reduz custo. Confirmar se o Q&A altera formalmente o Anexo I | Baixa (resolvido) |
| **C-13** | Subcontratação × nuvem e ferramentas | RFP 7.7: subcontratação vedada × Anexo I 1.2: SIEM em nuvem pública (provedor terceiro); threat intelligence e SOAR geralmente envolvem terceiros | Indefinida | Usar um provedor de nuvem ou feed de terceiros pode ser lido como subcontratação | **Alta** |
| **C-14** | Cronograma sem folga | Início 01/02/2027 × fim do SIEM legado em 31/01/2027 sem prorrogação × transição de 30 ou 60 dias após a assinatura × documentação entregue até 10 dias após a assinatura | — | Para cumprir 01/02/2027 com transição de 60 dias, a assinatura teria de ocorrer até ~03/12/2026, só 6 dias após a entrega das propostas. Com 30 dias, até ~02/01/2027. Qualquer atraso deixa o Banco sem SIEM | **Alta** |
| **C-15** | Abrangência do "preenchimento obrigatório" | D4, aba Instruções: "todas as abas" obrigatórias × abas de Q&A (já respondida) e "Pesos" (oculta) | — | Risco formal de desclassificação por interpretação | Baixa |
| **C-16** | Datas dos documentos | D3 (22/10/2026) e D4 (12/11/2026) são posteriores à data desta análise (17/10/2026) | — | Ver seção 1.4 | Baixa (verificar) |

---

## 5. Principais riscos (resumo para decisão)

| # | Risco | Origem | Probabilidade | Impacto | Tratamento sugerido |
|---|---|---|---|---|---|
| R-1 | Exposição financeira ilimitada (multas sem teto + responsabilidade ilimitada) | C-06 | Alta | Crítico | Pedir teto de multas (por exemplo 10% a 20% da fatura mensal) e limitar a responsabilidade (por exemplo a 12 meses de contrato). Se for negado, decidir go/no-go e precificar o risco. |
| R-2 | Inabilitação por arquitetura com dados fora do Brasil | C-05 | Média | Crítico | Projetar SIEM e armazenamento só em regiões brasileiras e assinar o Anexo III. |
| R-3 | Subdimensionar SIEM e armazenamento | C-04, C-09, C-10 | Alta | Alto | Usar premissas explícitas na proposta (volumetria estimada, GB/dia, 12 meses online + 5 anos frio) com cláusula de reequilíbrio. |
| R-4 | Subdimensionar IAM e escopo (4.500 a 7.100 usuários; subsidiárias) | C-03 | Alta | Alto | Usar 5.000 (Q&A) como base formal, com preço unitário para excedentes e ressalva expressa sobre as subsidiárias. |
| R-5 | Transição inviável em 30 dias e sem custo de operação paralela | C-02, C-14, T-02, T-06 | Alta | Alto | Pedir esclarecimento e apresentar um plano de transição com marcos e dependências do cliente. |
| R-6 | Nota técnica abaixo do corte por regra mal definida | C-07, C-08 | Média | Alto | Responder "Atende" ou "Parcial" com justificativa sempre que possível em QT-02 e QT-05. Esclarecer a pontuação máxima. |
| R-7 | Interpretar a vedação de subcontratação como proibição de nuvem ou ferramentas de terceiros | C-13 | Média | Alto | Esclarecer. Declarar na proposta que provedor de infraestrutura e fabricantes não configuram subcontratação. |
| R-8 | Fluxo de caixa (pagamento em 60 dias + absorção da transição) | K-03, T-02 | Alta | Médio | Considerar no custo financeiro do preço. |
| R-9 | Precificação sem o modelo oficial | Anexo IV ausente | Certa | Alto | **Obter o Anexo IV antes de qualquer trabalho de preço.** |

---

## 6. Pedidos de esclarecimento sugeridos

> **Atenção ao prazo:** o prazo de perguntas é 05/11/2026 [D1 item 3.1], e já existe uma Rodada 1 de respostas datada de 12/11/2026. Se a data de referência for posterior a 05/11, verificar se o Banco abrirá uma 2ª rodada. Se não abrir, os itens abaixo viram **premissas e ressalvas expressas na proposta**.

| Nº | Referência | Pergunta |
|---|---|---|
| Q-01 | RFP (geral) | Qual é a ordem de prevalência entre RFP, anexos, apresentação do workshop e respostas de Q&A em caso de divergência? |
| Q-02 | RFP 3.2 × Anexo I 4.1 | O prazo de conclusão da transição é de 30 ou de 60 dias corridos? Qual é a data prevista para assinatura do contrato? |
| Q-03 | RFP 2.1 × Q&A nº 5 × Apresentação slides 2 e 5 | Confirmar a base de dimensionamento (5.000 usuários). As subsidiárias Horizonte Seguros e Horizonte Investimentos (~900 usuários) fazem parte do escopo? Se sim, quem será a contratante e como será faturado? |
| Q-04 | Anexo I 1.3 × 1.6 | Confirmar a interpretação: 12 meses de retenção pesquisável (online) e 5 anos no total, podendo os 4 anos restantes ficar em armazenamento frio ou arquivado. Qual é o tempo de recuperação aceito para logs arquivados? |
| Q-05 | Anexo I 1.2 × Anexo III | Confirmar que o SIEM em nuvem pública deve usar exclusivamente regiões no Brasil, inclusive para backup, recuperação de desastres e processamento (por exemplo motores de análise e IA do fabricante). |
| Q-06 | RFP 7.4 / Q&A nº 4 | Reapresentar o pedido de teto global para multas e de gradação por gravidade do SLA. Confirmar se "ocorrência" é cada evento ou cada indicador apurado no mês. |
| Q-07 | RFP 7.5 e 7.6 | Aceitam limitar a responsabilidade a um múltiplo do valor anual do contrato, excluindo danos indiretos e lucros cessantes? Qual é o valor mínimo da apólice de seguro cibernético? |
| Q-08 | RFP 6.2 | A pontuação técnica máxima é 60 ou 65? Como será feita a normalização e qual é o corte de 70% em pontos? |
| Q-09 | Questionário, aba "Pesos" (oculta) | O questionário compõe a Nota Técnica? Como os pesos são aplicados? Confirmar a regra de redução de 2 pontos por item não obrigatório respondido como "Não atende". |
| Q-10 | Q&A nº 3 / Anexo I 1.4 | Sem a volumetria de eventos, podemos precificar a partir de uma volumetria declarada como premissa, com reequilíbrio se a real for diferente? Alternativamente, podem informar a ingestão diária em GB e a lista de tipos de fontes de log? |
| Q-11 | Apresentação slide 5 | A migração de 24 meses de logs históricos faz parte do escopo? Qual é o volume, o formato, o produto do SIEM legado e o prazo? |
| Q-12 | Apresentação slide 4 | A meta de 10% de falsos positivos no 1º trimestre é obrigação contratual ou SLA? |
| Q-13 | RFP 7.7 | Provedores de nuvem, fabricantes de software e fornecedores de feeds de threat intelligence configuram subcontratação vedada? |
| Q-14 | Anexo I 2.1 e 2.4 | Disponibilizar a matriz de classificação de criticidade e definir quando começa a contagem dos 15 minutos. |
| Q-15 | Anexo I item 3 | No IAM, quem fornece a plataforma (IGA e MFA): o proponente ou o Contratante? Quantos sistemas-alvo e quantas contas privilegiadas há? O PAM (item 3.4) deve ser cotado como item opcional? |
| Q-16 | RFP 5.1b | Os 2.000 usuários são exigidos em cada atestado? Atestados de contratos encerrados são aceitos? |
| Q-17 | RFP 5.2 / Anexo I 5.1 | Quais certificações e em que quantidade são exigidas da equipe para fins de habilitação? |
| Q-18 | Pacote de documentos | Existe Anexo II? O Anexo III, que só aparece como imagem na pág. 6 da RFP, está disponível em formato editável? |
| Q-19 | Anexo I 4.2 | Qual é a duração esperada da operação paralela e o que o fornecedor atual vai entregar (runbooks, casos de uso, regras de correlação)? |

---

## 7. Checklist de entrega (com base no que foi recebido)

- [ ] Proposta técnica em português, até 40 páginas sem os anexos [D1 item 4.2]
- [ ] Proposta comercial no modelo do Anexo IV [D1 item 4.3]: **modelo não recebido**
- [ ] Questionário técnico com as colunas D e E preenchidas em todos os itens QT-01 a QT-06 [D1 item 4.4; D4]
- [ ] Certificado ISO/IEC 27001 vigente, com escopo SOC [H-01]
- [ ] 3 ou mais atestados de SOC para instituições financeiras com ≥ 2.000 usuários [H-02]
- [ ] Comprovação de que o SOC fica no Brasil [H-03]
- [ ] Comprovação das certificações da equipe, incluindo o coordenador CISSP [H-04, T-03]
- [ ] Anexo III assinado pelo representante legal [H-05]
- [ ] Envio pelo portal de fornecedores até **27/11/2026, 18h** [C-01]

---

## 8. Conclusão

1. **A análise está incompleta quanto a preço:** o Anexo IV (planilha de preços) foi listado, mas não foi anexado. Nada do conteúdo dele foi presumido. Os 40% da nota final ligados a preço e a forma de precificar os itens controversos (retenção, migração, transição paralela, PAM e usuários excedentes) continuam sem análise.
2. **Pontos críticos para go/no-go:** responsabilidade ilimitada e multas sem teto (C-06), mantidas pelo Banco no Q&A; e a exigência eliminatória de dados só no Brasil, que contradiz o Anexo I (C-05).
3. **Pontos que impedem um dimensionamento confiável:** volumetria de eventos negada (C-09), base de usuários divergente com possível inclusão de subsidiárias (C-03) e retenção de 12 meses × 5 anos (C-04).
4. **Inconsistências formais a esclarecer ou ressalvar:** transição em 30 × 60 dias (C-02), pontuação máxima de 60 × 65 (C-07) e regra de pontuação na aba oculta (C-08).
5. **Atenção a conteúdo fora do texto principal:** o Anexo III só existe como imagem no PDF. A inclusão das subsidiárias só aparece nas notas do apresentador. A penalização por "Não atende" só está numa aba oculta da planilha.
