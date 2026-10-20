# Gabarito — Kit de testes da persona de análise de RFP

> **Não envie este arquivo ao modelo.** Ele serve só para conferir a saída.

As faixas de criticidade são orientativas: o que conta é a coerência da Severidade e da Probabilidade com o texto. Itens marcados com ★ são **essenciais**, e a persona precisa encontrar todos. O ID que a persona atribuir (Dnn-nnn) não precisa coincidir com o ID do gabarito (Gnn). Um item da persona pode cobrir mais de um item do gabarito e vice-versa.

## Documentos do cenário

| Documento | Arquivo | O que testa |
|---|---|---|
| RFP (PDF) | `RFP-2026-017_Servicos_SOC_IAM.pdf` | Página física × impressa (capa sem número); página 6 só com imagem (OCR) |
| Anexo I (Word) | `Anexo_I_Especificacao_Tecnica.docx` | Localizador por seção; contradições no mesmo documento e entre documentos |
| Apresentação (PPT) | `Apresentacao_Ambiente_Atual.pptx` | Requisitos escondidos em slides e nas notas do apresentador |
| Q&A e Questionário (Excel) | `QA_Rodada1_e_Questionario.xlsx` | Alterações por Q&A; localizador aba/linha; aba oculta |

## Itens esperados

| ID | ★ | Documento | Localizador esperado | Tipo esperado | Domínio | Criticidade esperada | Referência esperada | Relações / Status | O que testa | Descrição |
|---|---|---|---|---|---|---|---|---|---|---|
| G01 | ★ | RFP (PDF) | p. 2 (impressa: 1) · §1.2 | Registro de cobertura (regime) | Regulatório/Compliance | — | Res. CMN 4.893/2021 | — | Detecção de regime | Regime privado, setor financeiro regulado pelo BACEN, sujeito à Res. CMN 4.893/2021. Não é contratação pública. |
| G02 | ★ | Todos | Não localizado | Lacuna | Jurídico/Contratual | Alta–Crítica | Livre (ou Não aplicável) | Relaciona-se a G30, G60, G65 | Precedência não presumida | Nenhum documento define a ordem de precedência entre RFP, anexos e Q&A. |
| G03 |  | RFP (PDF) | p. 2 (impressa: 1) · §2.1 | Requisito funcional / de serviço | Operação/Serviços | Média–Alta | ISO/IEC 27001:2022 A.8.16 · NIST CSF 2.0 DE.CM | — | Objeto | SOC 24x7x365 e IAM. |
| G04 |  | RFP (PDF) | p. 2 (impressa: 1) · §2.1 | Dado de dimensionamento | Comercial/Preço | Média–Alta | Livre (ou Não aplicável) | Parte de G30 | Volumetria | Aproximadamente 4.500 colaboradores. |
| G05 |  | RFP (PDF) | p. 2 (impressa: 1) · §3.1 (tabela) | Prazo / marco | Administrativo do processo | Média–Alta | Livre (ou Não aplicável) | — | Prazos do processo | Prazo final para envio de perguntas: 05/11/2026. |
| G06 | ★ | RFP (PDF) | p. 2 (impressa: 1) · §3.1 (tabela) | Prazo / marco | Administrativo do processo | Alta–Crítica | Livre (ou Não aplicável) | Status: Alterado por G60 | Alteração por Q&A | Entrega das propostas: 20/11/2026, 18h. |
| G07 |  | RFP (PDF) | p. 2 (impressa: 1) · §3.1 (tabela) | Prazo / marco | Transição/Implantação | Média–Alta | Livre (ou Não aplicável) | Relaciona-se a G53 | Prazos do projeto | Início previsto dos serviços: 01/02/2027. |
| G08 | ★ | RFP (PDF) × Anexo I (Word) | RFP p. 2 (impressa: 1) §3.2 × Anexo I §4.1 | Contradição | Transição/Implantação | Alta | Livre (ou Não aplicável) | Duas evidências | Contradição entre documentos | Transição em até 30 dias (RFP) × em até 60 dias (Anexo I). |
| G09 |  | RFP (PDF) | p. 3 (impressa: 2) · §4.1 | Instrução de resposta | Administrativo do processo | Baixa–Média | Livre (ou Não aplicável) | — | Instruções | Proposta em português, entregue somente pelo portal. |
| G10 |  | RFP (PDF) | p. 3 (impressa: 2) · §4.2 | Instrução de resposta | Administrativo do processo | Média | Livre (ou Não aplicável) | — | Instruções | Proposta técnica com no máximo 40 páginas. |
| G11 | ★ | RFP (PDF) | p. 3 (impressa: 2) · §4.3 | Lacuna (documento citado e não fornecido) | Comercial/Preço | Alta–Crítica | Livre (ou Não aplicável) | — | Anexo referenciado e não fornecido | Anexo IV — Planilha de Preços é citado, mas não foi fornecido. |
| G12 | ★ | RFP (PDF) | p. 3 (impressa: 2) · §5.1 a | Critério eliminatório / de habilitação | Segurança da Informação/Cyber | Crítica | ISO/IEC 27001:2022 — cláusula 4.3 (escopo) | — | Critério eliminatório | Certificado ISO/IEC 27001 vigente com escopo que inclua o SOC. |
| G13 | ★ | RFP (PDF) | p. 3 (impressa: 2) · §5.1 b | Critério eliminatório / de habilitação | Administrativo do processo | Crítica | Livre (ou Não aplicável) | — | Critério eliminatório | 3 atestados de SOC para instituições financeiras com ≥ 2.000 usuários. |
| G14 | ★ | RFP (PDF) | p. 3 (impressa: 2) · §5.1 c | Critério eliminatório / de habilitação | Regulatório/Compliance | Crítica | Livre (ou Não aplicável) | Confirmado por G61 | Critério eliminatório | SOC localizado em território nacional. |
| G15 |  | RFP (PDF) | p. 3 (impressa: 2) · §5.2 | Ambiguidade | Pessoas/Equipe | Média–Alta | Livre (ou Não aplicável) | — | Ambiguidade + pergunta | "Equipe devidamente certificada": quais certificações e quantos profissionais? |
| G16 |  | RFP (PDF) | p. 4 (impressa: 3) · §6.1 | Critério de avaliação / pontuação | Administrativo do processo | Alta | APMP BoK (Boa prática) | — | Pontuação | Técnica 60% / Preço 40%. |
| G17 | ★ | RFP (PDF) | p. 4 (impressa: 3) · §6.2 (tabela) | Contradição | Administrativo do processo | Alta | Livre (ou Não aplicável) | Relaciona-se a G18 | Contradição no mesmo documento | Máximo declarado de 60 pontos × critérios que somam 65 (20+20+15+10). |
| G18 | ★ | RFP (PDF) | p. 4 (impressa: 3) · §6.3 | Critério eliminatório / de habilitação | Administrativo do processo | Alta–Crítica | Livre (ou Não aplicável) | Relaciona-se a G17 | Efeito em cadeia | Nota técnica < 70% desclassifica; o corte fica ambíguo (42 ou 45,5 pontos?). |
| G19 |  | RFP (PDF) | p. 4 (impressa: 3) · §6.4 | Critério de avaliação / pontuação | Comercial/Preço | Baixa–Média | Livre (ou Não aplicável) | — | Pontuação | Desempate pelo menor preço. |
| G20 |  | RFP (PDF) | p. 5 (impressa: 4) · §7.1 | Obrigação contratual | Jurídico/Contratual | Baixa–Média | Livre (ou Não aplicável) | — | Contratual | Vigência de 36 meses, prorrogável. |
| G21 |  | RFP (PDF) | p. 5 (impressa: 4) · §7.2 | Obrigação contratual | Financeiro | Baixa–Média | Livre (ou Não aplicável) | — | Contratual | Reajuste anual pelo IPCA. |
| G22 |  | RFP (PDF) | p. 5 (impressa: 4) · §7.3 | Obrigação contratual | Financeiro | Média | Livre (ou Não aplicável) | — | Fluxo de caixa | Pagamento em até 60 dias após o aceite da nota fiscal. |
| G23 | ★ | RFP (PDF) | p. 5 (impressa: 4) · §7.4 | Penalidade / multa / glosa | Jurídico/Contratual | Crítica | Livre (ou Não aplicável) | Confirmado por G63; relaciona-se a G37, G40 | Exposição sem teto | Multa de 10% do valor mensal por ocorrência, sem limite máximo. |
| G24 | ★ | RFP (PDF) | p. 5 (impressa: 4) · §7.5 | Obrigação contratual (ou Risco) | Jurídico/Contratual | Alta–Crítica | Livre (ou Não aplicável) | — | Regra da Severidade 5 | Responsabilidade integral e ilimitada por incidentes de segurança. |
| G25 |  | RFP (PDF) | p. 5 (impressa: 4) · §7.6 | Ambiguidade | Jurídico/Contratual | Média | Livre (ou Não aplicável) | — | Ambiguidade + pergunta | Seguro cibernético "em valor compatível", sem valor definido. |
| G26 |  | RFP (PDF) | p. 5 (impressa: 4) · §7.7 | Restrição (+ Risco inferido) | Jurídico/Contratual | Alta | Livre (ou Não aplicável) | Relaciona-se a G32 | Conflito implícito | Subcontratação vedada × SIEM em nuvem pública de terceiro (Anexo I §1.2). |
| G27 |  | RFP (PDF) | p. 5 (impressa: 4) · §7.8 | Obrigação contratual | Jurídico/Contratual | Baixa–Média | Livre (ou Não aplicável) | — | Contratual | Confidencialidade por 5 anos após o término. |
| G28 | ★ | RFP (PDF) | p. 6 (impressa: 5) · Anexo III (OCR) | Critério eliminatório / de habilitação | Regulatório/Compliance | Crítica | Livre (ou Não aplicável) | — | Leitura de página escaneada | Declaração de localização de dados, assinada, sob pena de inabilitação. |
| G29 | ★ | RFP (PDF) × Anexo I (Word) | RFP p. 6 (impressa: 5) Anexo III (OCR) × Anexo I §1.2 | Contradição | Privacidade/Proteção de Dados | Crítica | ISO/IEC 27001:2022 A.5.23 · Res. CMN 4.893/2021 (artigo a confirmar) | Duas evidências | Contradição envolvendo OCR | Dados exclusivamente no Brasil (Anexo III) × SIEM em nuvem com região de livre escolha (Anexo I). |
| G30 | ★ | Todos | RFP §2.1 × Apresentação slide 2 × Q&A nº 5 (linha 6) × notas do slide 5 | Contradição | Comercial/Preço | Alta–Crítica | Livre (ou Não aplicável) | Relaciona-se a G02, G04, G52, G58, G64 | Contradição entre 4 fontes | Usuários: 4.500 × 6.200 × 5.000 × +900 das subsidiárias. |
| G31 |  | Anexo I (Word) | §1.1 | Requisito funcional / de serviço | Segurança da Informação/Cyber | Média–Alta | ISO/IEC 27001:2022 A.8.16 · NIST CSF 2.0 DE.CM | Pode ser duplicado de G03 | Associação a framework | Monitoramento contínuo 24x7x365. |
| G32 |  | Anexo I (Word) | §1.2 | Requisito funcional / de serviço | Infraestrutura/Cloud | Alta | ISO/IEC 27001:2022 A.5.23 | Relaciona-se a G26, G29, G51 | Associação a framework | Fornecer SIEM, podendo ser em nuvem pública com região livre. |
| G33 | ★ | Anexo I (Word) | §1.3 × §1.6 | Contradição | Segurança da Informação/Cyber | Alta | ISO/IEC 27001:2022 A.8.15 | Relaciona-se a QT-03 (G66) | Contradição no mesmo documento | Retenção de logs: mínimo de 12 meses × 5 anos. |
| G34 |  | Anexo I (Word) | §1.4 | Ambiguidade | Técnico/Arquitetura | Alta | Livre (ou Não aplicável) | Relaciona-se a G35 | Ambiguidade | "Todos os ativos relevantes": não define quais nem quantos. |
| G35 | ★ | Anexo I (Word) + Q&A e Questionário (Excel) | Anexo I §1.4 + Q&A nº 3 (linha 4) | Lacuna | Comercial/Preço | Crítica | Livre (ou Não aplicável) | Continua após o Q&A | Lacuna que impede precificar | Volumetria de EPS não informada; o Q&A diz que só o vencedor a receberá. |
| G36 |  | Anexo I (Word) | §1.5 | Requisito funcional / de serviço | Segurança da Informação/Cyber | Alta | ISO/IEC 27001:2022 A.5.24–A.5.28 (A.5.26) · NIST CSF 2.0 RS | — | Associação a framework | Resposta a incidentes: contenção, erradicação e relatório. |
| G37 | ★ | Anexo I (Word) | §2.1 | SLA / KPI | Operação/Serviços | Alta–Crítica | ITIL 4 — Gerenciamento de Nível de Serviço | Relaciona-se a G23 | SLA × multa | Início do tratamento de incidentes críticos em até 15 minutos. |
| G38 |  | Anexo I (Word) | §2.2 | SLA / KPI | Operação/Serviços | Alta | ITIL 4 — Gerenciamento de Nível de Serviço | Relaciona-se a G23 | SLA | Disponibilidade do SIEM de 99,9%. |
| G39 |  | Anexo I (Word) | §2.3 | Entregável (ou SLA) | Operação/Serviços | Média | Livre (ou Não aplicável) | Relaciona-se a G23 | Entregável | Relatório mensal até o 5º dia útil. |
| G40 | ★ | Anexo I (Word) | §2.4 | Lacuna (documento citado e não fornecido) | Operação/Serviços | Alta–Crítica | Livre (ou Não aplicável) | Relaciona-se a G23, G37 | Lacuna com efeito financeiro | A matriz de criticidade do Contratante não foi fornecida e o SLA depende dela. |
| G41 |  | Anexo I (Word) | §3.1 | Requisito funcional / de serviço | Segurança da Informação/Cyber | Média–Alta | ISO/IEC 27001:2022 A.5.16 · A.5.18 | — | Associação a framework | Ciclo de vida de identidades; revogação em até 24h. |
| G42 |  | Anexo I (Word) | §3.2 | Requisito não funcional | Segurança da Informação/Cyber | Média–Alta | ISO/IEC 27001:2022 A.8.5 · A.8.2 | — | Associação a framework | MFA para 100% dos privilegiados. |
| G43 |  | Anexo I (Word) | §3.3 | Requisito funcional / de serviço | Segurança da Informação/Cyber | Média | ISO/IEC 27001:2022 A.5.18 | — | Associação a framework | Recertificação trimestral de acessos. |
| G44 |  | Anexo I (Word) | §3.4 | Requisito (Desejável) ou Oportunidade | Segurança da Informação/Cyber | Baixa–Média (ou —, se Oportunidade) | ISO/IEC 27001:2022 A.8.2 | Relaciona-se a G54 | Obrigatoriedade = Desejável | Cofre de senhas (PAM) desejável. |
| G45 |  | Anexo I (Word) | §4.2 | Risco para o proponente | Transição/Implantação | Média–Alta | Livre (ou Não aplicável) | — | Custo oculto | Operação em paralelo sem custo adicional. |
| G46 |  | Anexo I (Word) | §5.1 | Requisito funcional / de serviço | Pessoas/Equipe | Média | Livre (ou Não aplicável) | — | Equipe | Coordenador CISSP dedicado exclusivamente. |
| G47 | ★ | Anexo I (Word) | §5.2 | Restrição | Pessoas/Equipe | Média–Alta | Livre (ou Não aplicável) | Status: Alterado por G65 | Alteração por Q&A | Analistas N1 presenciais em São Paulo/SP. |
| G48 |  | Anexo I (Word) | §6.1 | Responsabilidade / dependência do cliente | Infraestrutura/Cloud | Baixa–Média | Livre (ou Não aplicável) | — | Dependência | O cliente fornece a VPN. |
| G49 |  | Anexo I (Word) | §6.2 | Responsabilidade / dependência do cliente (+ Risco) | Transição/Implantação | Média–Alta | Livre (ou Não aplicável) | Relaciona-se a G08 | Dependência × prazo | Documentação entregue em até 10 dias, dentro de uma transição de 30 dias. |
| G50 | ★ | Anexo I (Word) | §1.2 / §1.3 (motivador) | Requisito implícito (Inferida) | Privacidade/Proteção de Dados | Alta | LGPD (Lei 13.709/2018) — operador (art. 39 ou a confirmar) · ISO/IEC 27701 | — | Requisito implícito | Os logs contêm dados pessoais, o que torna o proponente operador e exige DPA. |
| G51 | ★ | Anexo I (Word) | §1.2 (motivador) + RFP §1.2 | Requisito implícito (Inferida) | Regulatório/Compliance | Alta | Res. CMN 4.893/2021 (artigo a confirmar) | Relaciona-se a G01, G32 | Uso correto do regime | SIEM em nuvem exige atender às regras de contratação de nuvem da Res. 4.893. |
| G52 |  | Apresentação (PPT) | slide 2 — "Números do ambiente" | Dado de dimensionamento | Infraestrutura/Cloud | Média | Livre (ou Não aplicável) | Parte de G30 | Volumetria | 6.200 usuários, 850 servidores, 2 data centers, 2 nuvens. |
| G53 | ★ | Apresentação (PPT) | slide 3 — "Ferramentas atuais" | Risco para o proponente (Inferida) | Transição/Implantação | Alta–Crítica | Livre (ou Não aplicável) | Relaciona-se a G07, G08 | Risco inferido por cruzamento | SIEM legado termina em 31/01/2027 sem prorrogação; transição de 30/60 dias até o início em 01/02/2027. |
| G54 |  | Apresentação (PPT) | slide 3 — "Ferramentas atuais" | Dado de dimensionamento | Segurança da Informação/Cyber | Baixa–Média | Livre (ou Não aplicável) | — | Ambiente atual | IAM com AD + scripts; não há PAM. |
| G55 |  | Apresentação (PPT) | slide 4 — "Desafios" | Dado de dimensionamento | Operação/Serviços | Média | Livre (ou Não aplicável) | — | Volumetria | Cerca de 1.200 alertas/dia, com 70% de falsos positivos. |
| G56 |  | Apresentação (PPT) | slide 4 — "Desafios" | Ambiguidade | Operação/Serviços | Média–Alta | Livre (ou Não aplicável) | — | Meta fora do SLA | Meta de 10% de falsos positivos no 1º trimestre: é obrigação? Não consta no Anexo I. |
| G57 | ★ | Apresentação (PPT) | slide 5 — "Expectativas para o novo serviço" | Requisito funcional / de serviço | Transição/Implantação | Alta | Livre (ou Não aplicável) | — | Requisito escondido em apresentação | Migrar 24 meses de logs históricos do SIEM legado. |
| G58 | ★ | Apresentação (PPT) | slide 5 — notas do apresentador | Contradição (ou Requisito de escopo) | Comercial/Preço | Alta–Crítica | Livre (ou Não aplicável) | Parte de G30 | Leitura de notas do slide | Subsidiárias com cerca de 900 usuários adicionais incluídas no escopo. |
| G59 | ★ | Q&A e Questionário (Excel) | aba Instruções · A3 | Critério eliminatório / de habilitação | Administrativo do processo | Crítica | Livre (ou Não aplicável) | Relaciona-se a G67 | Critério eliminatório em planilha | Questionário incompleto desclassifica, e todas as abas são obrigatórias. |
| G60 | ★ | Q&A e Questionário (Excel) | aba Q&A Rodada 1 · nº 1 (linha 2) | Prazo / marco | Administrativo do processo | Alta–Crítica | Livre (ou Não aplicável) | Altera G06 | Rastreio de alteração | Entrega prorrogada para 27/11/2026, 18h. |
| G61 |  | Q&A e Questionário (Excel) | aba Q&A Rodada 1 · nº 2 (linha 3) | Critério eliminatório (confirmação) | Regulatório/Compliance | Crítica | Livre (ou Não aplicável) | Duplicado de / confirma G14 | Duplicidade | O SOC não pode operar fora do Brasil. |
| G62 |  | Q&A e Questionário (Excel) | aba Q&A Rodada 1 · nº 3 (linha 4) | Lacuna (mantida) | Comercial/Preço | Crítica | Livre (ou Não aplicável) | Parte de G35 | Lacuna não resolvida | O EPS só será informado ao vencedor. |
| G63 |  | Q&A e Questionário (Excel) | aba Q&A Rodada 1 · nº 4 (linha 5) | Penalidade (confirmação) | Jurídico/Contratual | Crítica | Livre (ou Não aplicável) | Confirma G23 | Confirmação de risco | As multas continuam sem teto. |
| G64 | ★ | Q&A e Questionário (Excel) | aba Q&A Rodada 1 · nº 5 (linha 6) | Contradição / Dado de dimensionamento | Comercial/Preço | Alta–Crítica | Livre (ou Não aplicável) | Parte de G30; depende de G02 | Precedência não presumida | Considerar 5.000 usuários, um terceiro número diferente. |
| G65 | ★ | Q&A e Questionário (Excel) | aba Q&A Rodada 1 · nº 6 (linha 7) | Restrição (alteração) | Pessoas/Equipe | Média | Livre (ou Não aplicável) | Altera G47 | Rastreio de alteração | N1 pode atuar remotamente, desde que no Brasil. |
| G66 |  | Q&A e Questionário (Excel) | aba Questionário Técnico · linhas 2–7 (QT-01 a QT-06) | Requisito (um por QT) | Variado | Variado | QT-01: ISO/IEC 27001:2022 · QT-04: Res. CMN 4.893/2021 | QT-03 ↔ G33; QT-06 ↔ G15 | Atomização em planilha | Seis requisitos do questionário, cada um na sua linha. |
| G67 | ★ | Q&A e Questionário (Excel) | aba Pesos (OCULTA) | Registro de cobertura | — | — | — | Relaciona-se a G59 | Detecção de aba oculta | Existe uma aba oculta, que precisa ser registrada e analisada. |
| G68 | ★ | Q&A e Questionário (Excel) | aba Pesos (OCULTA) · A2:B7 e A9 | Critério de avaliação / pontuação | Administrativo do processo | Alta | Livre (ou Não aplicável) | Relaciona-se a G16, G17 | Regra de pontuação escondida | Pesos dos QTs; cada "Não atende" em item não obrigatório tira 2 pontos. |

## Armadilhas (o que NÃO pode acontecer)

| ID | Verificação | Capacidade |
|---|---|---|
| A01 | O §1.1 do RFP (história institucional do Banco) NÃO deve virar item. | Filtro de relevância |
| A02 | Nenhum item deve citar a Lei 14.133/2021: a contratação é privada. | Regime |
| A03 | O número de usuários válido não pode ser escolhido sem registrar a falta de precedência (G02). | Precedência |
| A04 | Nenhum controle ISO no formato da versão 2013 (ex.: A.9.2.x, A.12.4.x) e nenhum identificador inventado. | Frameworks |
| A05 | Páginas do PDF informadas como página física, com a impressa entre parênteses (física = impressa + 1). | Localizador |
| A06 | O conteúdo do Anexo IV (não fornecido) não pode ser inventado. | Alucinação |
| A07 | O §7.5 (responsabilidade ilimitada) não pode ficar abaixo de Alta. | Regra da Severidade 5 |
| A08 | Toda Probabilidade diferente de 3 deve vir justificada na Descrição analítica. | Matriz |
| A09 | Páginas do Word, se informadas, marcadas como "aprox.". | Localizador |
| A10 | Cada resposta tem somente: linha de abertura, tabela (até 30 linhas) e bloco de status. Nenhum outro texto. | Formato |
| A13 | Toda parte intermediária termina com ⏸ e 'Envie continuar'; ✅ aparece só na última, com totais de documentos, itens e último ID corretos. | Status e continuação |
| A11 | A página escaneada (p. 6) deve ser lida por OCR ou registrada como 'possível conteúdo em imagem não lido — requer OCR'; nunca descrita como em branco. | Cobertura |
| A12 | A persona não deve avaliar se "o proponente atende": ela não conhece a empresa. | Escopo |

## Métricas de aprovação

| Métrica | Como calcular | Meta |
|---|---|---|
| Cobertura dos itens essenciais (★) | Itens ★ encontrados ÷ total de ★ | 100% |
| Cobertura geral | Itens encontrados (S ou Parcial) ÷ 68 | ≥ 85% |
| Localizador correto | Localizador correto ÷ itens encontrados | ≥ 95% |
| Citação literal fiel | Conferir 10 citações por amostragem no original | 10 de 10 |
| Tipo de item coerente | Tipo coerente ÷ itens encontrados | ≥ 80% |
| Criticidade na faixa esperada | Na faixa ÷ itens encontrados | ≥ 80% |
| Identificadores inventados ou de versão errada | Contagem | 0 |
| Armadilhas (A01–A13) | Armadilhas evitadas ÷ 13 | 13 de 13 |
