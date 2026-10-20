# Gera a matriz analítica (Markdown) a partir das linhas registradas abaixo.
import sys
from pathlib import Path

OUT = Path(sys.argv[1])

DOCS = {
    "D01": ("RFP-2026-017_Servicos_SOC_IAM.pdf", "v1.0 — 15/10/2026", "RFP"),
    "D02": ("Anexo_I_Especificacao_Tecnica.docx", "v1.0 — 15/10/2026", "Anexo técnico"),
    "D03": ("Anexo_IV_Planilha_de_Precos.xlsx", "v1.0 (informada pelo usuário)", "Planilha de preços — NÃO ANEXADO"),
    "D04": ("Apresentacao_Ambiente_Atual.pptx", "22/10/2026", "Apresentação (workshop)"),
    "D05": ("QA_Rodada1_e_Questionario.xlsx", "Rodada 1 — 12/11/2026", "Q&A e questionário técnico"),
}
SEV = {1: "Insignificante", 2: "Menor", 3: "Moderada", 4: "Maior", 5: "Severa"}
PROB = {1: "Remota", 2: "Improvável", 3: "Possível", 4: "Provável", 5: "Quase certa"}

ROWS = []


def R(key, doc, sec, loc, ev, tipo, dom, desc, obr, nat, sev, prob, imp, fw, ctrl, assoc, rel, st, acao, perg, resp):
    ROWS.append(dict(key=key, doc=doc, sec=sec, loc=loc, ev=ev, tipo=tipo, dom=dom, desc=desc, obr=obr, nat=nat,
                     sev=sev, prob=prob, imp=imp, fw=fw, ctrl=ctrl, assoc=assoc, rel=rel, st=st, acao=acao,
                     perg=perg, resp=resp))


NA = ("—", "—", "Não aplicável")
ISO = "ISO/IEC 27001:2022 (Anexo A)"
CSF = "NIST CSF 2.0"
ITIL = "ITIL 4"
CC = "Código Civil (Lei nº 10.406/2002)"
LGPD = "LGPD (Lei nº 13.709/2018)"
CMN = "Resolução CMN nº 4.893/2021 (citada pelo cliente)"
CIS = "CIS Controls v8"

# =========================================================================== D01 — RFP
P2, P3, P4, P5, P6 = "p. 2 (impressa: 1)", "p. 3 (impressa: 2)", "p. 4 (impressa: 3)", "p. 5 (impressa: 4)", "p. 6 (impressa: 5) (OCR)"

R("d1_inv", "D01", "Documento completo (capa e seções 1 a 7, Anexo III)", "p. 1–6",
  '''"Solicitação de Proposta (RFP) nº 2026-017" · "Versão 1.0 — 15/10/2026"''',
  "Registro de cobertura", "Administrativo do processo",
  '''Inventário: PDF com 6 páginas físicas (p. 1 = capa sem número impresso; p. 2 a 6 = impressas 1 a 5). Texto extraído integralmente das p. 1 a 5. A p. 6 (impressa: 5) não tem camada de texto (imagem escaneada ocupando 50% da página): foi lida visualmente a partir da imagem e analisada com localizador "(OCR)"; contém o Anexo III — Declaração de Localização de Dados. Cabeçalho/rodapé repetido desconsiderado. Leitura completa, sem trecho pendente.''',
  "Informativo", "Explícita", None, None, "—", "—", "—", "—", "{d1_anexo3_dados}, {d1_anexo3_decl}", "Vigente",
  "Nenhuma (informativo)", "—", "Bid Manager")

R("d1_regime", "D01", "1. APRESENTAÇÃO — 1.2 · 7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.1", f"{P2} · {P5}",
  '''"O Banco é instituição financeira autorizada a funcionar pelo Banco Central do Brasil e está sujeito à Resolução CMN nº 4.893/2021" · "prorrogável por iguais períodos mediante acordo entre as partes"''',
  "Registro de cobertura", "Regulatório/Compliance / Jurídico/Contratual",
  '''Regime identificado: contratação PRIVADA em SETOR REGULADO. Evidências do caráter privado: contratante é sociedade anônima ("S.A."), o processo é uma RFP com envio pelo "portal de fornecedores do Banco", prorrogação "mediante acordo entre as partes"; nenhum documento menciona licitação, edital, pregão ou legislação de contratação pública (inferência). Setor regulado por declaração expressa: instituição financeira autorizada pelo Banco Central do Brasil e sujeita à Resolução CMN nº 4.893/2021. Consequência para a matriz: legislação de contratações públicas não é associada; referências jurídicas usadas: Código Civil, LGPD e a resolução citada pelo cliente.''',
  "Informativo", "Inferida", None, None, "—", "—", "—", "—", "{d1_cmn}", "Vigente", "Nenhuma (informativo)", "—", "Jurídico")

R("d1_preced", "D01", "Documento completo — cláusula de ordem de precedência", "p. 1–6 (não localizada)",
  '''Não localizado · "2.2 As especificações técnicas detalhadas constam do Anexo I — Especificação Técnica."''',
  "Lacuna", "Jurídico/Contratual",
  '''Não há cláusula de ordem de precedência entre a RFP, os anexos, a apresentação do workshop e as respostas do Q&A. Já existem conflitos concretos entre documentos (transição 30 × 60 dias; SIEM em nuvem de região livre × dados exclusivamente no Brasil; 4.500 × 5.000 × 6.200 usuários). Não se presume que o Anexo ou o Q&A, por serem específicos ou mais recentes, prevaleçam.''',
  "Informativo", "Explícita", 4, 3,
  "Sem regra de prevalência, o proponente pode precificar e assumir compromissos pela versão errada de prazos, volumetria e arquitetura; risco de glosa ou multa por interpretação divergente na execução.",
  CC, "Interpretação dos negócios jurídicos (identificador a confirmar)", "Correlata",
  "{d2_c_trans}, {d2_c_nuvem}, {d4_c_users}, {d5_c_users}", "Em esclarecimento", "Esclarecer no Q&A",
  "Qual a ordem de precedência entre a RFP, o Anexo I, os demais anexos, a apresentação do workshop de 22/10/2026 e as respostas do Q&A em caso de divergência? As respostas do Q&A passam a integrar o contrato?",
  "Jurídico")

R("d1_cmn", "D01", "1. APRESENTAÇÃO — 1.2", P2,
  '''"está sujeito à Resolução CMN nº 4.893/2021, que dispõe sobre a política de segurança cibernética e sobre os requisitos para a contratação de serviços de processamento e armazenamento de dados e de computação em nuvem"''',
  "Requisito implícito", "Regulatório/Compliance",
  '''Inferida: o SOC, com SIEM fornecido pelo proponente e possivelmente em nuvem (Anexo I, 1.2), e a guarda de logs por 5 anos configuram serviço de processamento e armazenamento de dados contratado por instituição sujeita à resolução citada. É esperável que o contrato incorpore exigências decorrentes dela (cláusulas contratuais, acesso a informações, comunicação de incidentes, continuidade), que não estão detalhadas nos documentos; o QT-04 pede declaração de atendimento à mesma norma. Não há minuta contratual entre os documentos recebidos. Artigos não citados por não constarem dos documentos.''',
  "Mandatório", "Inferida", 4, 3,
  "Obrigações regulatórias não explicitadas podem exigir cláusulas, controles, relatórios e auditorias adicionais não precificados.",
  CMN, "Contratação de serviços de processamento, armazenamento de dados e computação em nuvem (identificador a confirmar)", "Direta",
  "{d2_c_nuvem}, {d5_qt04}", "Vigente", "Esclarecer no Q&A",
  "Quais obrigações decorrentes da Resolução CMN nº 4.893/2021 serão transferidas contratualmente à Contratada (cláusulas obrigatórias, acesso do Banco Central, notificação de incidentes, continuidade, localização de dados)? Há minuta de contrato que as contemple?",
  "Compliance")

R("d1_soc", "D01", "2. OBJETO — 2.1", P2,
  '''"prestação de serviços gerenciados de Centro de Operações de Segurança (SOC), em regime 24x7x365"''',
  "Requisito funcional / de serviço", "Operação/Serviços / Segurança da Informação/Cyber",
  "Objeto principal: SOC gerenciado em operação ininterrupta (24 horas, 7 dias, 365 dias), o que exige escala de turnos e cobertura de feriados.",
  "Mandatório", "Explícita", 4, 3,
  "Define o dimensionamento mínimo de equipe em turnos, principal componente de custo do contrato.",
  CSF, "DE.CM — Continuous Monitoring", "Direta", "{d2_mon}", "Vigente", "Precificar", "—", "Delivery/Operação")

R("d1_iam", "D01", "2. OBJETO — 2.1", P2,
  '''"e de gestão de identidades e acessos (IAM)"''',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Segundo componente do objeto: serviço gerenciado de IAM, detalhado no Anexo I, seção 3. Não está definido se a plataforma de IAM/IGA é fornecida pelo proponente ou se o serviço opera ferramentas do Banco (ver {d2_lac_iamtool}).",
  "Mandatório", "Explícita", 4, 3,
  "Escopo e custo de plataforma de IAM indefinidos.",
  ISO, "A.5.16 — Gestão de identidade", "Direta", "{d2_iam_ciclo}, {d2_lac_iamtool}", "Vigente", "Precificar", "—",
  "Pré-venda/Arquitetura")

R("d1_users", "D01", "2. OBJETO — 2.1", P2,
  '''"abrangendo aproximadamente 4.500 colaboradores"''',
  "Dado de dimensionamento", "Operação/Serviços",
  "Base original de dimensionamento. Alterada pela resposta nº 5 do Q&A (5.000 usuários) e divergente da apresentação (6.200 usuários ativos, mais cerca de 900 das subsidiárias nas notas do slide 5). 'Colaboradores' pode não equivaler a 'usuários' (terceiros, contas de serviço).",
  "Informativo", "Explícita", 4, 3,
  "A base de preço por usuário pode variar até cerca de 58% (4.500 × 7.100).",
  *NA, "{d4_c_users}, {d4_subsid}, {d5_q5}, {d5_c_users}", "Alterado", "Esclarecer no Q&A", "—", "Pré-venda/Arquitetura")

R("d1_workshop", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2,
  '''"Workshop de apresentação do ambiente 22/10/2026"''',
  "Prazo / marco", "Administrativo do processo",
  "Workshop com proponentes. O material apresentado (D04) traz informações e expectativas não previstas na RFP (migração de logs, meta de falsos positivos, subsidiárias). A RFP não diz se a participação é obrigatória nem se o conteúdo do workshop é vinculante.",
  "Informativo", "Explícita", 2, 3,
  "Informação divulgada só no workshop pode alterar escopo e dimensionamento.",
  *NA, "{d4_inv}", "Vigente", "Esclarecer no Q&A",
  "O conteúdo apresentado no workshop de 22/10/2026, inclusive as notas do apresentador, integra formalmente a RFP?",
  "Bid Manager")

R("d1_perg", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2,
  '''"Prazo final para envio de perguntas 05/11/2026"''',
  "Prazo / marco", "Administrativo do processo",
  "Data-limite para o Q&A. A RFP não prevê nova rodada de perguntas, e várias lacunas desta matriz dependem de esclarecimento.",
  "Mandatório", "Explícita", 3, 3,
  "Perguntas não respondidas obrigam a precificar sob premissas.",
  *NA, "{d5_inv}", "Vigente", "Esclarecer no Q&A",
  "Haverá nova rodada de esclarecimentos após as respostas da Rodada 1 (12/11/2026)?", "Bid Manager")

R("d1_resp", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2,
  '''"Divulgação das respostas 12/11/2026"''',
  "Prazo / marco", "Administrativo do processo",
  "Respostas publicadas em 12/11/2026, data confirmada na aba 'Q&A Rodada 1'. Com a prorrogação da entrega, restam 15 dias corridos entre as respostas e a entrega.",
  "Informativo", "Explícita", 2, 3,
  "Janela curta para incorporar respostas ao preço e à proposta técnica.",
  *NA, "{d5_inv}, {d5_q1}", "Vigente", "Nenhuma (informativo)", "—", "Bid Manager")

R("d1_entrega", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2,
  '''"Entrega das propostas 20/11/2026, até as 18h"''',
  "Prazo / marco", "Administrativo do processo",
  "Prazo original de entrega, alterado pela resposta nº 1 do Q&A para 27/11/2026, até as 18h. A RFP não explicita a consequência da entrega fora do prazo.",
  "Mandatório", "Explícita", 5, 3,
  "Proposta fora do prazo pode não ser recebida (perda da oportunidade).",
  *NA, "{d5_q1}", "Alterado", "Atender", "—", "Bid Manager")

R("d1_inicio", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2,
  '''"Início previsto dos serviços 01/02/2027"''',
  "Prazo / marco", "Transição/Implantação",
  "Início da operação no dia seguinte ao término do contrato do SIEM legado (31/01/2027, sem prorrogação — slide 3). A data de assinatura do contrato não é informada, mas a transição é contada a partir dela.",
  "Informativo", "Explícita", 3, 3,
  "Janela de implantação fixa e sem folga em relação ao legado.",
  *NA, "{d1_trans30}, {d1_lac_assin}, {d4_legado}, {d4_risco_trans}", "Vigente", "Mitigar", "—", "Delivery/Operação")

R("d1_lac_assin", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1 e 3.2", P2,
  '''Não localizado · "A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato."''',
  "Lacuna", "Gestão de Projetos / Transição/Implantação",
  "O cronograma não informa datas de resultado, negociação e assinatura do contrato. Como a transição (3.2) e a entrega da documentação técnica pelo Banco (Anexo I, 6.2) são contadas da assinatura, não é possível verificar se a transição cabe antes do início em 01/02/2027.",
  "Informativo", "Explícita", 3, 3,
  "Impede planejar a janela real de transição e reservar equipe com antecedência.",
  *NA, "{d1_trans30}, {d4_risco_trans}", "Em esclarecimento", "Esclarecer no Q&A",
  "Qual a data prevista para divulgação do resultado e assinatura do contrato? O prazo de transição será contado da assinatura ou do início previsto dos serviços (01/02/2027)?",
  "Bid Manager")

R("d1_trans30", "D01", "3. CRONOGRAMA DO PROCESSO — 3.2", P2,
  '''"A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato."''',
  "Prazo / marco", "Transição/Implantação",
  "Prazo de transição de 30 dias corridos. Diverge do Anexo I, item 4.1 (60 dias) — ver contradição {d2_c_trans}.",
  "Mandatório", "Explícita", 4, 3,
  "Transição comprimida exige equipe de implantação concentrada e aumenta o risco de multas desde o início.",
  ITIL, "Prática de habilitação de mudanças (change enablement)", "Correlata",
  "{d2_c_trans}, {d4_risco_trans}", "Em esclarecimento", "Esclarecer no Q&A", "—", "Delivery/Operação")

R("d1_idioma", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.1", P3,
  '''"A proposta deverá ser redigida em língua portuguesa"''',
  "Instrução de resposta", "Administrativo do processo",
  "Idioma obrigatório. A RFP não trata de documentos emitidos em outro idioma (certificados, atestados, catálogos técnicos) nem de tradução.",
  "Mandatório", "Explícita", 3, 3,
  "Possível custo e prazo de tradução de documentos de habilitação.",
  *NA, "{d1_iso}, {d1_atest}", "Vigente", "Atender",
  "Documentos de habilitação emitidos em outro idioma (por exemplo, o certificado ISO/IEC 27001) precisam de tradução? Simples ou juramentada?",
  "Bid Manager")

R("d1_portal", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.1", P3,
  '''"e enviada exclusivamente pelo portal de fornecedores do Banco"''',
  "Instrução de resposta", "Administrativo do processo",
  "Canal único de entrega. Endereço do portal, cadastro prévio, limite de tamanho de arquivo e comprovante de recebimento não são informados.",
  "Mandatório", "Explícita", 3, 3,
  "Falha de cadastro ou de envio perto do prazo pode impedir a entrega.",
  *NA, "{d5_q1}", "Vigente", "Esclarecer no Q&A",
  "Qual o endereço do portal de fornecedores, há cadastro prévio exigido (com que antecedência) e qual o limite de tamanho por arquivo?",
  "Bid Manager")

R("d1_40pag", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.2", P3,
  '''"A proposta técnica deverá ter no máximo 40 (quarenta) páginas, excluídos os anexos."''',
  "Instrução de resposta", "Administrativo do processo",
  "Limite de 40 páginas. Não define formato de página/fonte, consequência do excesso nem o que pode ir como anexo (questionário, plano de transição, currículos).",
  "Mandatório", "Explícita", 3, 3,
  "Conteúdo além do limite pode ser desconsiderado na pontuação técnica.",
  *NA, "{d1_lac_sub}", "Vigente", "Atender",
  "Qual a consequência de exceder 40 páginas? Há formato mínimo de fonte e página? Plano de transição e currículos podem ser apresentados como anexos?",
  "Bid Manager")

R("d1_anexo4", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.3", P3,
  '''"A proposta comercial deverá ser apresentada conforme a planilha modelo do Anexo IV — Planilha de Preços."''',
  "Instrução de resposta", "Comercial/Preço",
  "A proposta comercial deve seguir o modelo do Anexo IV. O arquivo Anexo_IV_Planilha_de_Precos.xlsx (v1.0) foi listado na solicitação do usuário, mas não foi anexado: estrutura de preços, unidades de cobrança, campos obrigatórios e eventuais abas ou regras ocultas não foram analisados (ver {d3_inv}). Não registrado como Lacuna do cliente porque o usuário informa possuir o arquivo.",
  "Mandatório", "Explícita", 4, 3,
  "Sem o modelo, não é possível verificar se a estrutura de preços comporta os custos identificados (transição sem custo, retenção de 5 anos, variação de usuários, multas).",
  *NA, "{d3_inv}", "Vigente", "Atender", "—", "Pricing/Financeiro")

R("d1_quest", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.4", P3,
  '''"O questionário técnico (planilha anexa) deverá ser integralmente preenchido."''',
  "Instrução de resposta", "Administrativo do processo",
  "O questionário corresponde à aba 'Questionário Técnico' de QA_Rodada1_e_Questionario.xlsx. A sanção (desclassificação) e a extensão a 'todas as abas' só aparecem na aba 'Instruções' desse arquivo.",
  "Mandatório", "Explícita", 3, 3,
  "Preenchimento parcial expõe à sanção prevista no D05.",
  *NA, "{d5_instr}, {d5_amb_abas}", "Vigente", "Atender", "—", "Pré-venda/Arquitetura")

R("d1_iso", "D01", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 a)", P3,
  '''"Serão inabilitados os proponentes que não apresentarem: a) certificado ISO/IEC 27001 vigente, emitido por organismo acreditado, cujo escopo inclua os serviços de SOC"''',
  "Critério eliminatório / de habilitação", "Segurança da Informação/Cyber / Regulatório/Compliance",
  "Certificado ISO/IEC 27001 vigente, de organismo acreditado, com escopo que inclua SOC (não exige escopo de IAM). Não especifica a versão da norma, o acreditador nem se a vigência é aferida na entrega ou durante o contrato. Probabilidade 5: a ausência leva diretamente à inabilitação pelo texto.",
  "Mandatório", "Explícita", 5, 5,
  "Inabilitação.",
  "ISO/IEC 27001:2022", "Requisitos do SGSI, cláusulas 4 a 10 (certificação)", "Direta",
  "{d5_qt01}", "Vigente", "Atender",
  "O certificado deve estar vigente apenas na data de entrega ou durante todo o contrato? Certificado de empresa do mesmo grupo econômico, cujo escopo cubra o SOC, é aceito?",
  "Compliance")

R("d1_atest", "D01", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 b)", P3,
  '''"b) no mínimo 3 (três) atestados de capacidade técnica de prestação de serviços de SOC para instituições financeiras, com ambiente de no mínimo 2.000 usuários"''',
  "Critério eliminatório / de habilitação", "Administrativo do processo / Operação/Serviços",
  "Três atestados de SOC para instituições financeiras. Não está claro se o mínimo de 2.000 usuários vale para cada atestado, o que conta como 'usuário' e se seguradoras, cooperativas ou instituições de pagamento são aceitas. Probabilidade 5: o não atendimento leva diretamente à inabilitação.",
  "Mandatório", "Explícita", 5, 5,
  "Inabilitação.",
  *NA, "—", "Vigente", "Atender",
  "O mínimo de 2.000 usuários se aplica a cada atestado individualmente? Atestados emitidos por seguradoras, cooperativas de crédito ou instituições de pagamento são aceitos? Há período mínimo de prestação?",
  "Bid Manager")

R("d1_socbr", "D01", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 c)", P3,
  '''"c) comprovação de que o SOC está localizado em território nacional."''',
  "Critério eliminatório / de habilitação", "Regulatório/Compliance / Operação/Serviços",
  "SOC no Brasil, confirmado pela resposta nº 2 do Q&A. Não define o meio de comprovação nem se abrange site de contingência e infraestrutura do SIEM. Probabilidade 5: o não atendimento leva diretamente à inabilitação.",
  "Mandatório", "Explícita", 5, 5,
  "Inabilitação.",
  CMN, "Localização do processamento e armazenamento de dados (identificador a confirmar)", "Correlata",
  "{d5_q2}, {d5_q6}, {d2_c_nuvem}", "Vigente", "Atender",
  "Que documentos são aceitos como comprovação da localização do SOC? A exigência se aplica também ao site de contingência e à infraestrutura do SIEM?",
  "Delivery/Operação")

R("d1_equipe", "D01", "5. CRITÉRIOS DE HABILITAÇÃO — 5.2", P3,
  '''"5.2 O proponente deverá possuir equipe técnica devidamente certificada."''',
  "Ambiguidade", "Pessoas/Equipe",
  "Exigência sem definição de certificações, perfis, quantidades ou forma de comprovação. Está na seção de habilitação, mas fora da lista do 5.1 cujo descumprimento inabilita expressamente; não está claro se é eliminatória. Relaciona-se ao CISSP do coordenador (Anexo I, 5.1), ao critério 'Qualificação da equipe' e ao QT-06. Severidade 5 porque uma das interpretações leva à inabilitação.",
  "Mandatório", "Explícita", 5, 3,
  "Risco de inabilitação ou de perda de pontuação por critério subjetivo.",
  ISO, "A.6.3 — Conscientização, educação e treinamento em segurança da informação", "Correlata",
  "{d2_cissp}, {d1_crit_equipe}, {d5_qt06}", "Em esclarecimento", "Esclarecer no Q&A",
  "O item 5.2 é critério de habilitação eliminatório? Quais certificações, para quais perfis e em que quantidade mínima, e como devem ser comprovadas?",
  "RH/Staffing")

R("d1_nota", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.1", P4,
  '''"A nota final será composta pela Nota Técnica (peso de 60%) e pela Nota de Preço (peso de 40%)."''',
  "Critério de avaliação / pontuação", "Comercial/Preço",
  "Composição técnica/preço 60/40: o peso técnico é preponderante.",
  "Mandatório", "Explícita", 3, 3,
  "Orienta a estratégia de preço × qualidade técnica.",
  *NA, "{d1_lac_preco}, {d1_c_soma}", "Vigente", "Atender", "—", "Bid Manager")

R("d1_lac_preco", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.1", P4,
  '''Não localizado · "pela Nota de Preço (peso de 40%)"''',
  "Lacuna", "Comercial/Preço",
  "A fórmula da Nota de Preço (proporcional ao menor preço, faixas, preço de referência) e sua escala não são informadas; também não há critério de inexequibilidade.",
  "Informativo", "Explícita", 4, 3,
  "Impossível simular a nota final e calibrar o preço.",
  *NA, "{d1_nota}", "Em esclarecimento", "Esclarecer no Q&A",
  "Qual a fórmula e a escala da Nota de Preço? Há preço máximo de referência ou critério de inexequibilidade?",
  "Pricing/Financeiro")

R("d1_c_soma", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", P4,
  '''A: "A Nota Técnica, de no máximo 60 (sessenta) pontos" · B: "Metodologia de operação do SOC 20" · "Qualificação da equipe 20" · "Ferramentas e tecnologia 15" · "Plano de transição 10"''',
  "Contradição", "Administrativo do processo",
  "Contradição interna: a soma das pontuações máximas dos critérios é 65, mas a Nota Técnica é limitada a 60 pontos. Afeta o corte de 70% (6.3: 42 pontos sobre 60 ou 45,5 sobre 65) e a conversão para o peso de 60%.",
  "Mandatório", "Explícita", 4, 3,
  "Incerteza sobre a pontuação mínima e o peso relativo dos critérios; risco de desclassificação.",
  *NA, "{d1_corte}, {d1_crit_met}, {d1_crit_equipe}, {d1_crit_ferr}, {d1_crit_trans}, {d5_c_pesos}",
  "Em esclarecimento", "Esclarecer no Q&A",
  "A soma dos critérios do item 6.2 é 65 pontos, mas a Nota Técnica máxima é 60. Qual a pontuação correta de cada critério e qual a nota mínima (70%) em pontos absolutos?",
  "Bid Manager")

R("d1_crit_met", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", P4, '''"Metodologia de operação do SOC 20"''',
  "Critério de avaliação / pontuação", "Operação/Serviços",
  "Critério de maior peso (empatado), sem subcritérios ou escala definidos.",
  "Mandatório", "Explícita", 4, 3, "Perda relevante de pontuação técnica.",
  ITIL, "Prática de gerenciamento de incidentes", "Correlata", "{d1_c_soma}, {d1_lac_sub}", "Vigente", "Atender", "—",
  "Pré-venda/Arquitetura")

R("d1_crit_equipe", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", P4, '''"Qualificação da equipe 20"''',
  "Critério de avaliação / pontuação", "Pessoas/Equipe",
  "Critério de maior peso (empatado); não define o que é avaliado (certificações, experiência, currículos).",
  "Mandatório", "Explícita", 4, 3, "Perda relevante de pontuação técnica.",
  *NA, "{d1_equipe}, {d1_c_soma}, {d5_qt06}", "Vigente", "Atender", "—", "RH/Staffing")

R("d1_crit_ferr", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", P4, '''"Ferramentas e tecnologia 15"''',
  "Critério de avaliação / pontuação", "Técnico/Arquitetura",
  "Pontua o ferramental; relaciona-se ao SIEM (Anexo I, 1.2) e às funcionalidades do questionário (SOAR, threat intelligence).",
  "Mandatório", "Explícita", 3, 3, "Perda moderada de pontuação.",
  *NA, "{d1_c_soma}, {d2_siem}, {d5_qt02}, {d5_qt05}", "Vigente", "Atender", "—", "Pré-venda/Arquitetura")

R("d1_crit_trans", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", P4, '''"Plano de transição 10"''',
  "Critério de avaliação / pontuação", "Transição/Implantação",
  "Pontua o plano de transição, cujo prazo é contraditório (30 × 60 dias).",
  "Mandatório", "Explícita", 3, 3, "Perda moderada de pontuação.",
  *NA, "{d1_c_soma}, {d2_c_trans}, {d4_risco_trans}", "Vigente", "Atender", "—", "Delivery/Operação")

R("d1_lac_sub", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", P4,
  '''Não localizado · "será atribuída conforme os critérios abaixo"''',
  "Lacuna", "Administrativo do processo",
  "Não há subcritérios, escala de notas, evidências esperadas nem método de atribuição dentro de cada critério. O questionário técnico tem pesos (aba oculta 'Pesos') sem vínculo declarado com estes critérios.",
  "Informativo", "Explícita", 3, 3,
  "Pontuação subjetiva; dificulta priorizar o conteúdo das 40 páginas.",
  *NA, "{d1_c_soma}, {d5_c_pesos}, {d5_lac_pesos}", "Em esclarecimento", "Esclarecer no Q&A",
  "Quais os subcritérios, a escala de notas e as evidências esperadas em cada critério do item 6.2? Como o questionário técnico e seus pesos entram na Nota Técnica?",
  "Bid Manager")

R("d1_corte", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.3", P4,
  '''"Serão desclassificadas as propostas com Nota Técnica inferior a 70% (setenta por cento) da pontuação máxima."''',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Nota de corte técnica. A 'pontuação máxima' é incerta (60 declarados ou 65 somados), e a regra da aba oculta 'Pesos' pode reduzir a nota em 2 pontos por requisito não obrigatório não atendido. A desclassificação depende da avaliação, não decorre diretamente do texto.",
  "Mandatório", "Explícita", 5, 3,
  "Desclassificação.",
  *NA, "{d1_c_soma}, {d5_c_pesos}", "Vigente", "Mitigar", "—", "Bid Manager")

R("d1_empate", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.4", P4,
  '''"Em caso de empate na nota final, prevalecerá a proposta de menor preço."''',
  "Critério de avaliação / pontuação", "Comercial/Preço",
  "Desempate por menor preço. Probabilidade 2: empate exato na nota final composta é pouco provável.",
  "Mandatório", "Explícita", 2, 2, "Efeito pequeno; reforça o peso do preço.",
  *NA, "—", "Vigente", "Nenhuma (informativo)", "—", "Pricing/Financeiro")

R("d1_vig", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.1", P5,
  '''"O contrato terá vigência de 36 (trinta e seis) meses, prorrogável por iguais períodos mediante acordo entre as partes."''',
  "Obrigação contratual", "Jurídico/Contratual",
  "Vigência de 36 meses, prorrogável por iguais períodos sem limite de prorrogações. Base para amortizar transição, operação paralela sem custo e investimentos em plataforma.",
  "Informativo", "Explícita", 3, 3, "Define o prazo de amortização dos custos de implantação.",
  *NA, "{d2_paral}", "Vigente", "Precificar", "—", "Pricing/Financeiro")

R("d1_reaj", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.2", P5,
  '''"Os preços serão reajustados anualmente pela variação do IPCA."''',
  "Obrigação contratual", "Financeiro",
  "Reajuste anual pelo IPCA, sem data-base definida (proposta ou assinatura). Custos de pessoal e licenças cotadas em moeda estrangeira podem variar de forma diferente do índice.",
  "Mandatório", "Explícita", 3, 3, "Descasamento entre reajuste e custos ao longo de 36 meses.",
  *NA, "—", "Vigente", "Esclarecer no Q&A",
  "Qual a data-base do reajuste (data da proposta ou da assinatura)? Há tratamento para licenças cotadas em moeda estrangeira?",
  "Pricing/Financeiro")

R("d1_pgto", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.3", P5,
  '''"O pagamento será efetuado em até 60 (sessenta) dias após o aceite da nota fiscal."''',
  "Obrigação contratual", "Financeiro",
  "Pagamento em até 60 dias contados do aceite da nota fiscal, sem prazo definido para o próprio aceite. Probabilidade 4: o prazo longo é explícito e a ausência de prazo para o aceite permite alongar o ciclo em todos os meses do contrato.",
  "Mandatório", "Explícita", 3, 4,
  "Custo de capital de giro de cerca de dois meses de faturamento durante todo o contrato.",
  *NA, "—", "Vigente", "Precificar",
  "Qual o prazo para o aceite da nota fiscal após a emissão? Há correção ou juros em caso de atraso no pagamento?",
  "Pricing/Financeiro")

R("d1_multa", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.4", P5,
  '''"O descumprimento de qualquer nível de serviço (SLA) previsto no Anexo I sujeitará a Contratada a multa de 10% (dez por cento) do valor mensal do contrato, por ocorrência."''',
  "Penalidade / multa / glosa", "Jurídico/Contratual / Financeiro",
  "Multa de 10% do valor mensal por ocorrência, para qualquer SLA, sem teto e sem gradação por gravidade: dez ocorrências no mês equivalem a 100% do faturamento mensal. 'Ocorrência' não é definida (por incidente ou por período de medição), e não está claro se relatório mensal (2.3) e revogação em 24 h (3.1) são SLAs sujeitos à multa. Probabilidade 4: a multa é aplicada automaticamente a cada ocorrência e o cliente recusou limitá-la (Q&A nº 4).",
  "Mandatório", "Explícita", 5, 4,
  "Exposição financeira sem limite, capaz de superar a receita mensal e eliminar a margem.",
  CC, "Art. 412 — limite da cláusula penal ao valor da obrigação principal", "Correlata",
  "{d2_sla15}, {d2_sla_disp}, {d2_rel}, {d2_revog}, {d2_lac_matriz}, {d5_q4}, {d4_risco_trans}", "Vigente",
  "Propor exceção/ressalva",
  "Como se define 'ocorrência' para fins do item 7.4 e quais itens do Anexo I são considerados SLAs passíveis de multa?",
  "Jurídico")

R("d1_resp_ilim", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.5", P5,
  '''"A Contratada responderá de forma integral e ilimitada por quaisquer danos decorrentes de incidentes de segurança ocorridos no ambiente do Contratante."''',
  "Obrigação contratual", "Jurídico/Contratual",
  "Responsabilidade integral e ilimitada por quaisquer danos de incidentes no ambiente do Contratante, sem exigir nexo com falha da Contratada nem excluir danos indiretos. Num SOC, incidentes no ambiente do cliente são justamente o objeto monitorado. A resposta nº 4 do Q&A declarou o item 7 inalterado.",
  "Mandatório", "Explícita", 5, 3,
  "Exposição jurídica e financeira ilimitada; pode tornar o risco não segurável.",
  CC, "Responsabilidade civil contratual e limitação de responsabilidade (identificador a confirmar)", "Correlata",
  "{d1_seguro}, {d5_q4}, {d2_lgpd}", "Vigente", "Avaliar Go/No-Go",
  "A responsabilidade do item 7.5 se limita a danos causados por dolo ou culpa da Contratada no cumprimento de suas obrigações? É aceita limitação ao valor anual do contrato e exclusão de danos indiretos e lucros cessantes?",
  "Jurídico")

R("d1_seguro", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.6", P5,
  '''"A Contratada deverá manter seguro de responsabilidade civil cibernética em valor compatível com os riscos do contrato."''',
  "Ambiguidade", "Jurídico/Contratual / Financeiro",
  "Obrigação contratual mandatória com valor segurado indefinido; combinada com a responsabilidade ilimitada (7.5), 'compatível com os riscos' não tem parâmetro objetivo. Tipo escolhido: Ambiguidade (maior impacto); também é Obrigação contratual.",
  "Mandatório", "Explícita", 4, 3,
  "Custo de prêmio imprevisível e risco de inadimplemento por cobertura considerada insuficiente.",
  *NA, "{d1_resp_ilim}", "Em esclarecimento", "Esclarecer no Q&A",
  "Qual o valor mínimo de cobertura do seguro de responsabilidade civil cibernética e em que momento a apólice deve ser apresentada?",
  "Jurídico")

R("d1_subc", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.7", P5,
  '''"É vedada a subcontratação, total ou parcial, do objeto deste contrato."''',
  "Restrição", "Jurídico/Contratual",
  "Vedação total de subcontratação. Não está claro se o uso de nuvem pública para o SIEM (Anexo I, 1.2), SIEM em modelo SaaS, feeds de threat intelligence de terceiros ou profissionais de empresas do mesmo grupo configuram subcontratação.",
  "Mandatório", "Explícita", 4, 3,
  "Pode impedir modelos de entrega com parceiros e fabricantes e exigir equipe 100% própria.",
  ISO, "A.5.19 — Segurança da informação nas relações com fornecedores", "Correlata",
  "{d2_c_nuvem}, {d5_qt05}", "Vigente", "Esclarecer no Q&A",
  "O uso de provedor de nuvem pública, de SIEM em modelo SaaS, de feeds de threat intelligence de terceiros ou de profissionais de empresas do mesmo grupo econômico é considerado subcontratação vedada pelo item 7.7?",
  "Jurídico")

R("d1_conf", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.8", P5,
  '''"As obrigações de confidencialidade vigorarão por 5 (cinco) anos após o término do contrato."''',
  "Obrigação contratual", "Jurídico/Contratual",
  "Confidencialidade pós-contratual de 5 anos. Não trata da devolução ou eliminação dos dados e logs ao fim do contrato, embora o Anexo I (1.6) exija guarda de logs por 5 anos.",
  "Mandatório", "Explícita", 2, 3, "Baixo custo; exige controles de guarda e descarte.",
  ISO, "A.6.6 — Acordos de confidencialidade ou não divulgação", "Direta", "{d2_ret5}", "Vigente", "Atender", "—",
  "Jurídico")

R("d1_anexo3_dados", "D01", "Anexo III — Declaração de Localização de Dados", P6,
  '''"todos os dados do Banco Horizonte Fictício S.A., incluindo os registros (logs) de segurança, serão armazenados e processados exclusivamente em território nacional, durante toda a vigência do contrato"''',
  "Restrição", "Privacidade/Proteção de Dados / Regulatório/Compliance",
  "Conteúdo lido por OCR (página escaneada). Residência de dados: armazenamento e processamento exclusivamente no Brasil, inclusive logs, durante toda a vigência. Conflita com o Anexo I, 1.2 (nuvem pública em região de livre escolha). Abrange 'todos os dados', o que pode alcançar backups, réplicas de recuperação de desastre e telemetria enviada a fabricantes.",
  "Mandatório", "Explícita", 5, 3,
  "Restringe a escolha de SIEM, nuvem e serviços SaaS globais; declaração inexata pode levar a inabilitação ou rescisão.",
  LGPD, "Art. 33 — transferência internacional de dados pessoais", "Correlata",
  "{d2_c_nuvem}, {d1_socbr}, {d1_cmn}, {d1_anexo3_decl}", "Vigente", "Atender",
  "A restrição de localização de dados se aplica a backups, réplicas de recuperação de desastre, telemetria enviada a fabricantes (EDR, threat intelligence) e suporte de terceiro nível do fabricante prestado do exterior?",
  "Pré-venda/Arquitetura")

R("d1_anexo3_decl", "D01", "Anexo III — Declaração de Localização de Dados", P6,
  '''"Esta declaração deverá ser entregue assinada pelo representante legal do proponente junto com a proposta, sob pena de inabilitação."''',
  "Critério eliminatório / de habilitação", "Administrativo do processo / Regulatório/Compliance",
  "Conteúdo lido por OCR. Exigência eliminatória presente apenas no Anexo III (página escaneada), não listada no item 5.1 nem nas instruções do item 4. Probabilidade 5: a não entrega leva diretamente à inabilitação.",
  "Mandatório", "Explícita", 5, 5,
  "Inabilitação; a assinatura também vincula o proponente à restrição de dados no Brasil.",
  *NA, "{d1_anexo3_dados}, {d2_c_nuvem}", "Vigente", "Atender",
  "A Declaração de Localização de Dados (Anexo III) é documento de habilitação adicional aos do item 5.1? Deve ser enviada em arquivo específico no portal?",
  "Bid Manager")

R("d1_lac_anexo2", "D01", "Documento completo — referências a anexos", f"{P2} · {P3} · {P6}",
  '''Não localizado · "Anexo I — Especificação Técnica" · "Anexo IV — Planilha de Preços" · "ANEXO III — DECLARAÇÃO DE LOCALIZAÇÃO DE DADOS"''',
  "Lacuna", "Administrativo do processo",
  "Inferida: a RFP cita os Anexos I, III e IV, mas nenhum documento cita ou contém um Anexo II. A falha na numeração sugere anexo existente e não distribuído (por exemplo, minuta de contrato ou modelo de proposta técnica) ou erro de numeração. Não há minuta contratual entre os documentos.",
  "Informativo", "Inferida", 3, 3,
  "Anexo não recebido pode conter exigências de habilitação, SLAs ou cláusulas contratuais.",
  *NA, "{d1_anexo4}, {d1_cmn}", "Em esclarecimento", "Esclarecer no Q&A",
  "Existe um Anexo II da RFP nº 2026-017? Se sim, solicitamos sua disponibilização. Há minuta de contrato a ser assinada?",
  "Bid Manager")

# =========================================================================== D02 — Anexo I
S1, S2, S3, S4, S5, S6 = ("§ 1. SERVIÇOS DE SOC", "§ 2. NÍVEIS DE SERVIÇO (SLA)", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM)",
                          "§ 4. TRANSIÇÃO", "§ 5. EQUIPE", "§ 6. RESPONSABILIDADES DO CONTRATANTE")

R("d2_inv", "D02", "Documento completo (seções 1 a 6)", "§ Anexo I — Especificação Técnica a § 6. RESPONSABILIDADES DO CONTRATANTE",
  '''"RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Versão 1.0 — 15/10/2026"''',
  "Registro de cobertura", "Administrativo do processo",
  "Inventário: Word com 22 parágrafos e 0 tabelas, 6 seções numeradas; sem marcas de revisão nem comentários sinalizados. Leitura integral. Word não tem paginação fixa: localizador por seção e item.",
  "Informativo", "Explícita", None, None, "—", "—", "—", "—", "—", "Vigente", "Nenhuma (informativo)", "—", "Bid Manager")

R("d2_mon", "D02", "1. SERVIÇOS DE SOC — 1.1", f"{S1}, item 1.1",
  '''"1.1 O proponente deverá prestar serviço de monitoramento contínuo de eventos de segurança, em regime 24x7x365."''',
  "Requisito funcional / de serviço", "Operação/Serviços / Segurança da Informação/Cyber",
  "Repete o objeto da RFP (2.1): monitoramento contínuo 24x7x365.",
  "Mandatório", "Explícita", 4, 3, "Dimensionamento de turnos 24x7.",
  CSF, "DE.CM — Continuous Monitoring", "Direta", "{d1_soc}", "Duplicado", "Precificar", "—", "Delivery/Operação")

R("d2_siem", "D02", "1. SERVIÇOS DE SOC — 1.2", f"{S1}, item 1.2",
  '''"1.2 O proponente deverá fornecer a solução de SIEM"''',
  "Requisito funcional / de serviço", "Técnico/Arquitetura",
  "O proponente fornece a plataforma SIEM (licenças e infraestrutura). A volumetria (EPS) não é informada e foi recusada até a contratação (Q&A nº 3).",
  "Mandatório", "Explícita", 4, 3, "Custo de licenciamento e infraestrutura dependente de volumetria desconhecida.",
  ISO, "A.8.16 — Atividades de monitoramento", "Direta", "{d5_q3}, {d2_integ}", "Vigente", "Precificar", "—",
  "Pré-venda/Arquitetura")

R("d2_c_nuvem", "D02", "1. SERVIÇOS DE SOC — 1.2 × RFP Anexo III", f"{S1}, item 1.2 · RFP {P6}",
  '''A: "podendo esta ser disponibilizada em nuvem pública, em região de livre escolha do proponente" (Anexo I, 1.2) · B: "serão armazenados e processados exclusivamente em território nacional" (RFP, Anexo III)''',
  "Contradição", "Infraestrutura/Cloud / Regulatório/Compliance",
  "O Anexo I permite hospedar o SIEM em nuvem pública em qualquer região; a declaração eliminatória do Anexo III exige que todos os dados, incluindo logs, sejam armazenados e processados exclusivamente no Brasil. Seguir o Anexo I com região estrangeira tornaria inexata a declaração exigida sob pena de inabilitação. Não há cláusula de precedência ({d1_preced}); a resposta nº 2 do Q&A trata só da localização do SOC, não dos dados.",
  "Mandatório", "Explícita", 5, 3,
  "Define arquitetura e região do SIEM; risco de inabilitação ou de descumprimento contratual.",
  CMN, "Contratação de processamento, armazenamento de dados e computação em nuvem (identificador a confirmar)", "Correlata",
  "{d1_anexo3_dados}, {d1_anexo3_decl}, {d1_preced}, {d1_subc}, {d5_q2}", "Em esclarecimento", "Esclarecer no Q&A",
  "O Anexo I, item 1.2, permite SIEM em nuvem pública em região de livre escolha, mas o Anexo III exige armazenamento e processamento exclusivamente em território nacional. Prevalece o Anexo III, isto é, a região de nuvem deve estar obrigatoriamente no Brasil?",
  "Pré-venda/Arquitetura")

R("d2_ret12", "D02", "1. SERVIÇOS DE SOC — 1.3", f"{S1}, item 1.3",
  '''"1.3 Os registros (logs) de segurança deverão ser retidos por no mínimo 12 (doze) meses."''',
  "Requisito não funcional", "Infraestrutura/Cloud / Segurança da Informação/Cyber",
  "Retenção mínima de 12 meses; não diz se online (pesquisável) ou em arquivo. Ver ambiguidade {d2_amb_ret}.",
  "Mandatório", "Explícita", 3, 3, "Custo de armazenamento proporcional ao EPS (desconhecido).",
  ISO, "A.8.15 — Registro de logs", "Direta", "{d2_amb_ret}, {d5_qt03}", "Vigente", "Precificar", "—",
  "Pré-venda/Arquitetura")

R("d2_lgpd", "D02", "1. SERVIÇOS DE SOC — 1.3", f"{S1}, item 1.3",
  '''"Os registros (logs) de segurança deverão ser retidos"''',
  "Requisito implícito", "Privacidade/Proteção de Dados",
  "Inferida: logs de segurança (autenticação, acessos, eventos de IAM de milhares de colaboradores) contêm dados pessoais; ao coletá-los, armazená-los e analisá-los em nome do Banco, o proponente atua como operador na LGPD. Nenhum documento trata de acordo de tratamento de dados, instruções do controlador, suboperadores ou prazos de notificação de incidentes com dados pessoais.",
  "Mandatório", "Inferida", 4, 3,
  "Obrigações e responsabilidades de operador não precificadas, somadas à responsabilidade ilimitada do item 7.5.",
  LGPD, "Art. 5º, VII (operador) e Art. 39 (tratamento conforme instruções do controlador)", "Direta",
  "{d1_resp_ilim}, {d1_anexo3_dados}", "Vigente", "Registrar premissa na proposta",
  "O Banco pretende firmar acordo de tratamento de dados pessoais definindo os papéis de controlador e operador, as instruções de tratamento e os prazos de notificação de incidentes?",
  "Compliance")

R("d2_integ", "D02", "1. SERVIÇOS DE SOC — 1.4", f"{S1}, item 1.4",
  '''"1.4 O SIEM deverá ser integrado a todos os ativos relevantes do Contratante."''',
  "Ambiguidade", "Técnico/Arquitetura",
  "'Ativos relevantes' não é definido; não há inventário de fontes de log nem volumetria. A apresentação informa 850 servidores, 2 data centers e 2 nuvens públicas; o EPS foi recusado (Q&A nº 3). Tipo escolhido: Ambiguidade; é também Requisito funcional mandatório.",
  "Mandatório", "Explícita", 4, 3,
  "Escopo de integração aberto (conectores, parsers, licenças por volume).",
  CIS, "Controle 8 — Gestão de logs de auditoria", "Correlata", "{d5_q3}, {d4_serv}, {d4_dc}, {d4_nuvens}",
  "Em esclarecimento", "Esclarecer no Q&A",
  "Quais ativos são considerados 'relevantes' para integração ao SIEM (lista ou critério) e qual a quantidade por tipo de fonte (servidores, rede, nuvem, aplicações, estações)?",
  "Pré-venda/Arquitetura")

R("d2_ir_cont", "D02", "1. SERVIÇOS DE SOC — 1.5", f"{S1}, item 1.5",
  '''"1.5 O serviço deverá contemplar resposta a incidentes, incluindo contenção"''',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Contenção de incidentes: exige acesso administrativo ao ambiente do Banco e regras de atuação (quem executa, autorização prévia). Não diz se é remota ou presencial.",
  "Mandatório", "Explícita", 4, 3, "Esforço de resposta e exposição à responsabilidade do item 7.5.",
  CSF, "RS.MI — Incident Mitigation", "Direta", "{d1_resp_ilim}, {d2_vpn}", "Vigente", "Esclarecer no Q&A",
  "As ações de contenção e erradicação serão executadas pela Contratada diretamente no ambiente do Banco ou pelas equipes do Banco sob orientação do SOC? Há atendimento presencial previsto?",
  "Segurança/Cyber")

R("d2_ir_err", "D02", "1. SERVIÇOS DE SOC — 1.5", f"{S1}, item 1.5",
  '''"incluindo contenção, erradicação e elaboração de relatório pós-incidente"''',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Erradicação: pode envolver correção, reinstalação e remoção de artefatos em ativos do Banco; limite com a operação de TI do Banco não definido; forense não mencionada.",
  "Mandatório", "Explícita", 3, 3, "Esforço técnico de difícil estimativa.",
  ISO, "A.5.26 — Resposta a incidentes de segurança da informação", "Direta", "{d2_ir_cont}", "Vigente", "Precificar",
  "—", "Segurança/Cyber")

R("d2_ir_rel", "D02", "1. SERVIÇOS DE SOC — 1.5", f"{S1}, item 1.5",
  '''"elaboração de relatório pós-incidente"''',
  "Entregável", "Segurança da Informação/Cyber",
  "Relatório pós-incidente; prazo e conteúdo mínimo não definidos.",
  "Mandatório", "Explícita", 2, 3, "Esforço pequeno por incidente.",
  ISO, "A.5.27 — Aprendizado com incidentes de segurança da informação", "Direta", "—", "Vigente", "Esclarecer no Q&A",
  "Qual o prazo e o conteúdo mínimo do relatório pós-incidente?", "Segurança/Cyber")

R("d2_ret5", "D02", "1. SERVIÇOS DE SOC — 1.6", f"{S1}, item 1.6",
  '''"1.6 Para fins de auditoria, os logs deverão ser mantidos por 5 (cinco) anos."''',
  "Requisito não funcional", "Infraestrutura/Cloud / Regulatório/Compliance",
  "Guarda de logs por 5 anos para auditoria. O contrato tem 36 meses: não se define quem mantém os logs nos 2 anos seguintes nem como são devolvidos ao fim do contrato.",
  "Mandatório", "Explícita", 4, 3, "Custo de armazenamento de longo prazo e de devolução dos dados.",
  ISO, "A.5.33 — Proteção de registros", "Correlata", "{d2_amb_ret}, {d1_conf}", "Vigente", "Precificar",
  "—", "Pré-venda/Arquitetura")

R("d2_amb_ret", "D02", "1. SERVIÇOS DE SOC — 1.3 e 1.6", f"{S1}, itens 1.3 e 1.6 · D05 aba \"Questionário Técnico\" · B4 (QT-03)",
  '''A: "deverão ser retidos por no mínimo 12 (doze) meses" (1.3) · B: "os logs deverão ser mantidos por 5 (cinco) anos" (1.6) · "Retém os logs online por no mínimo 12 meses?" (QT-03)''',
  "Ambiguidade", "Infraestrutura/Cloud",
  "Dois prazos de retenção para os mesmos logs, sem distinguir retenção online (pesquisável no SIEM) e arquivamento. O QT-03 fala em 'logs online por no mínimo 12 meses', sugerindo 12 meses online e 5 anos em arquivo, mas isso não está escrito. A migração de 24 meses de logs históricos (slide 5) aumenta a dúvida.",
  "Mandatório", "Explícita", 4, 3,
  "Diferença relevante de custo de armazenamento e licenciamento entre 12 meses e 5 anos online.",
  CIS, "Controle 8 — Gestão de logs de auditoria", "Correlata", "{d2_ret12}, {d2_ret5}, {d5_qt03}, {d4_migr}",
  "Em esclarecimento", "Esclarecer no Q&A",
  "A guarda por 5 anos (item 1.6) pode ser em armazenamento de arquivo, mantendo 12 meses online e pesquisáveis no SIEM (item 1.3)? Qual o prazo máximo aceito para recuperar logs arquivados?",
  "Pré-venda/Arquitetura")

R("d2_sla15", "D02", "2. NÍVEIS DE SERVIÇO (SLA) — 2.1", f"{S2}, item 2.1",
  '''"2.1 Tempo máximo para início do tratamento de incidentes críticos: 15 (quinze) minutos."''',
  "SLA / KPI", "Operação/Serviços",
  "SLA de 15 minutos para início do tratamento de incidentes críticos; cada descumprimento sujeita a multa de 10% do valor mensal (RFP 7.4). 'Crítico' depende da matriz do Contratante, não fornecida (2.4). Não define o evento que inicia a contagem nem SLAs para outras criticidades.",
  "Mandatório", "Explícita", 4, 3, "Exige analistas disponíveis 24x7 com folga; cada falha custa 10% do mês.",
  ITIL, "Prática de gerenciamento de nível de serviço", "Direta", "{d1_multa}, {d2_lac_matriz}", "Vigente", "Precificar",
  "A partir de qual evento se conta o prazo de 15 minutos (geração do alerta, triagem ou abertura do incidente)? Quais os SLAs para as demais criticidades?",
  "Delivery/Operação")

R("d2_sla_disp", "D02", "2. NÍVEIS DE SERVIÇO (SLA) — 2.2", f"{S2}, item 2.2",
  '''"2.2 Disponibilidade mínima mensal da plataforma SIEM: 99,9%."''',
  "SLA / KPI", "Infraestrutura/Cloud",
  "99,9% mensal equivale a cerca de 43 minutos de indisponibilidade por mês. Janelas de manutenção, falhas do provedor de nuvem e da conectividade do Banco não são excluídas expressamente. Sujeito à multa de 10% por ocorrência.",
  "Mandatório", "Explícita", 4, 3, "Exige arquitetura de alta disponibilidade e expõe a multa mensal.",
  ITIL, "Prática de gerenciamento de disponibilidade", "Direta", "{d1_multa}", "Vigente", "Precificar",
  "Janelas de manutenção programada e indisponibilidades causadas pela infraestrutura ou conectividade do Banco são excluídas do cálculo de disponibilidade?",
  "Pré-venda/Arquitetura")

R("d2_rel", "D02", "2. NÍVEIS DE SERVIÇO (SLA) — 2.3", f"{S2}, item 2.3",
  '''"2.3 Relatório mensal de indicadores, a ser entregue até o 5º dia útil do mês subsequente."''',
  "Entregável", "Operação/Serviços",
  "Relatório mensal até o 5º dia útil; indicadores não definidos. Por estar na seção 'NÍVEIS DE SERVIÇO (SLA)', o atraso pode ser tratado como descumprimento de SLA com multa de 10% (RFP 7.4).",
  "Mandatório", "Explícita", 3, 3, "Esforço mensal de relatório; possível exposição a multa por atraso.",
  ITIL, "Prática de gerenciamento de nível de serviço", "Correlata", "{d1_multa}, {d4_visao}", "Vigente",
  "Esclarecer no Q&A",
  "Quais indicadores devem compor o relatório mensal? O atraso na entrega do relatório é considerado descumprimento de SLA para fins do item 7.4 da RFP?",
  "Delivery/Operação")

R("d2_lac_matriz", "D02", "2. NÍVEIS DE SERVIÇO (SLA) — 2.4", f"{S2}, item 2.4",
  '''Não localizado · "2.4 A classificação de criticidade dos incidentes seguirá a matriz de classificação do Contratante."''',
  "Lacuna", "Operação/Serviços / Segurança da Informação/Cyber",
  "A matriz de classificação do Contratante é citada e não foi fornecida. Ela define quais incidentes são 'críticos' e, portanto, quais estão sujeitos ao SLA de 15 minutos e à multa por ocorrência.",
  "Mandatório", "Explícita", 4, 3,
  "Impossível estimar a quantidade de incidentes críticos e dimensionar a equipe para o SLA.",
  ISO, "A.5.25 — Avaliação e decisão sobre eventos de segurança da informação", "Correlata",
  "{d2_sla15}, {d1_multa}", "Em esclarecimento", "Esclarecer no Q&A",
  "Solicitamos a matriz de classificação de criticidade de incidentes do Contratante e o volume histórico mensal de incidentes por criticidade. A matriz poderá ser alterada unilateralmente durante o contrato?",
  "Segurança/Cyber")

R("d2_iam_ciclo", "D02", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.1", f"{S3}, item 3.1",
  '''"3.1 Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"''',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Gestão de admissão, movimentação e desligamento. Os itens 3.1 a 3.3 não têm verbo de obrigação; classificados como mandatórios pelo efeito, por contraste com o 3.4 ('desejável'). Ambiente atual: Active Directory + scripts internos (slide 3); integração com RH e sistemas-alvo não especificada.",
  "Mandatório", "Explícita", 4, 3, "Esforço de integração e automação proporcional a sistemas e usuários.",
  ISO, "A.5.16 — Gestão de identidade", "Direta", "{d1_iam}, {d2_lac_iamtool}, {d4_iam}", "Vigente", "Precificar",
  "Quantos sistemas-alvo devem ser integrados ao ciclo de vida de identidades e qual a fonte autoritativa (sistema de RH)?",
  "Pré-venda/Arquitetura")

R("d2_revog", "D02", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.1", f"{S3}, item 3.1",
  '''"com revogação dos acessos de colaboradores desligados em até 24 (vinte e quatro) horas"''',
  "SLA / KPI", "Segurança da Informação/Cyber",
  "Prazo de 24 horas para revogar acessos de desligados. Não define o marco inicial (data do desligamento ou comunicação do RH) nem se abrange sistemas fora do AD; se tratado como SLA, sujeita à multa de 10% por ocorrência.",
  "Mandatório", "Explícita", 3, 3, "Cada revogação atrasada pode gerar multa.",
  ISO, "A.5.18 — Direitos de acesso", "Direta", "{d1_multa}", "Vigente", "Esclarecer no Q&A",
  "O prazo de 24 horas conta a partir da comunicação formal do desligamento pelo Banco? Abrange todos os sistemas ou apenas os integrados à solução de IAM?",
  "Delivery/Operação")

R("d2_mfa", "D02", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.2", f"{S3}, item 3.2",
  '''"3.2 Autenticação multifator (MFA) obrigatória para 100% dos usuários com acesso privilegiado."''',
  "Requisito não funcional", "Segurança da Informação/Cyber",
  "MFA para todos os usuários privilegiados. Quantidade de privilegiados, solução de MFA existente e responsável pelo fornecimento não informados; não há PAM hoje (slide 3).",
  "Mandatório", "Explícita", 3, 3, "Possível custo de licenças de MFA.",
  ISO, "A.8.5 — Autenticação segura", "Direta", "{d4_pam}, {d2_lac_iamtool}", "Vigente", "Esclarecer no Q&A",
  "Quantos usuários têm acesso privilegiado e há solução de MFA já licenciada pelo Banco, ou ela deve ser fornecida pela Contratada?",
  "Segurança/Cyber")

R("d2_recert", "D02", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.3", f"{S3}, item 3.3",
  '''"3.3 Revisão (recertificação) trimestral dos acessos concedidos."''',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Campanhas trimestrais de recertificação. Sem ferramenta de governança de identidades no ambiente atual, implica esforço manual ou fornecimento de ferramenta; os revisores (gestores do Banco) são dependência do Contratante.",
  "Mandatório", "Explícita", 3, 3, "Esforço recorrente trimestral.",
  ISO, "A.5.18 — Direitos de acesso", "Direta", "{d2_lac_iamtool}, {d4_iam}", "Vigente", "Precificar", "—",
  "Segurança/Cyber")

R("d2_pam", "D02", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.4", f"{S3}, item 3.4",
  '''"3.4 É desejável que a solução contemple cofre de senhas para contas privilegiadas (PAM)."''',
  "Oportunidade / diferencial", "Segurança da Informação/Cyber",
  "Item desejável num ambiente sem PAM (slide 3): pode diferenciar a proposta. Não há critério de pontuação explícito, e a regra da aba oculta 'Pesos' (redução de 2 pontos por requisito não obrigatório 'Não atende') pode alcançá-lo se for tratado como requisito não obrigatório.",
  "Desejável", "Explícita", None, None, "Diferenciação técnica; custo de licenças de PAM se ofertado.",
  ISO, "A.8.2 — Direitos de acesso privilegiado", "Direta", "{d4_pam}, {d5_c_pesos}", "Vigente", "Esclarecer no Q&A",
  "A oferta de PAM (item 3.4) será pontuada? A não oferta reduz a Nota Técnica?", "Pré-venda/Arquitetura")

R("d2_lac_iamtool", "D02", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.1 a 3.4", f"{S3}, itens 3.1 a 3.4",
  '''Não localizado · "É desejável que a solução contemple cofre de senhas para contas privilegiadas (PAM)."''',
  "Lacuna", "Técnico/Arquitetura / Comercial/Preço",
  "Para o SOC, o Anexo I diz expressamente que o proponente fornece o SIEM (1.2); para o IAM, não diz se a plataforma (IAM/IGA, MFA) é fornecida pelo proponente ou se o serviço opera ferramentas do Banco (hoje AD + scripts internos). O item 3.4 menciona 'a solução', sugerindo fornecimento pelo proponente.",
  "Informativo", "Explícita", 4, 3,
  "Grande diferença de preço entre operar ferramentas do Banco e fornecer plataforma IAM/IGA licenciada para 5.000 ou mais usuários.",
  *NA, "{d1_iam}, {d2_iam_ciclo}, {d2_mfa}, {d2_recert}, {d4_iam}", "Em esclarecimento", "Esclarecer no Q&A",
  "A Contratada deve fornecer a plataforma de IAM/IGA e de MFA, com licenças, ou operar as ferramentas existentes do Banco (Active Directory e scripts internos)?",
  "Pré-venda/Arquitetura")

R("d2_c_trans", "D02", "4. TRANSIÇÃO — 4.1 × RFP 3.2", f"RFP {P2}, item 3.2 · {S4}, item 4.1",
  '''A: "A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato." (RFP, 3.2) · B: "4.1 A transição dos serviços deverá ser concluída em até 60 (sessenta) dias corridos a partir da assinatura do contrato." (Anexo I, 4.1)''',
  "Contradição", "Transição/Implantação",
  "Prazos de transição incompatíveis (30 × 60 dias), sem cláusula de precedência. O critério 'Plano de transição' e o custo da operação paralela sem remuneração dependem desse prazo.",
  "Mandatório", "Explícita", 4, 3,
  "Diferença de custo e de risco entre transição de 30 e de 60 dias; risco de penalidade se adotado o prazo mais longo.",
  *NA, "{d1_trans30}, {d1_preced}, {d1_crit_trans}, {d2_paral}, {d4_risco_trans}", "Em esclarecimento",
  "Esclarecer no Q&A",
  "A RFP (item 3.2) fixa a transição em 30 dias e o Anexo I (item 4.1) em 60 dias, ambos contados da assinatura. Qual prazo prevalece?",
  "Delivery/Operação")

R("d2_paral", "D02", "4. TRANSIÇÃO — 4.2", f"{S4}, item 4.2",
  '''"4.2 Durante a transição, o proponente deverá operar em paralelo com o fornecedor atual, sem custo adicional para o Contratante."''',
  "Requisito funcional / de serviço", "Transição/Implantação / Comercial/Preço",
  "Operação paralela durante toda a transição, sem remuneração. Probabilidade 5: o custo não remunerado decorre diretamente do texto ('sem custo adicional'). Depende da cooperação do fornecedor atual, cujas obrigações não estão definidas, e o SIEM legado encerra em 31/01/2027 sem prorrogação (slide 3).",
  "Mandatório", "Explícita", 3, 5,
  "Custo de 30 a 60 dias de operação sem faturamento, a diluir no preço.",
  *NA, "{d2_c_trans}, {d4_legado}, {d4_risco_trans}, {d1_vig}", "Vigente", "Precificar",
  "O fornecedor atual terá obrigação contratual de cooperar na transição (acesso a dados, playbooks e logs)? A operação paralela pode ocorrer antes do início previsto em 01/02/2027?",
  "Delivery/Operação")

R("d2_cissp", "D02", "5. EQUIPE — 5.1", f"{S5}, item 5.1",
  '''"5.1 O serviço deverá contar com coordenador com certificação CISSP"''',
  "Restrição", "Pessoas/Equipe",
  "Coordenador certificado CISSP: única certificação nominalmente exigida.",
  "Mandatório", "Explícita", 3, 3, "Restringe o perfil e eleva o custo do coordenador.",
  *NA, "{d1_equipe}", "Vigente", "Atender", "—", "RH/Staffing")

R("d2_dedic", "D02", "5. EQUIPE — 5.1", f"{S5}, item 5.1",
  '''"dedicado exclusivamente ao contrato"''',
  "Restrição", "Pessoas/Equipe / Comercial/Preço",
  "Dedicação exclusiva do coordenador: custo integral de um profissional sênior no preço; regime de substituição em férias e ausências não definido.",
  "Mandatório", "Explícita", 3, 3, "Custo fixo de um profissional sênior durante 36 meses.",
  *NA, "{d2_cissp}", "Vigente", "Precificar",
  "Em férias e ausências do coordenador, é aceito substituto temporário com a mesma certificação?", "RH/Staffing")

R("d2_n1", "D02", "5. EQUIPE — 5.2", f"{S5}, item 5.2",
  '''"5.2 Os analistas de nível 1 deverão atuar presencialmente na sede do Contratante, em São Paulo/SP, em horário comercial."''',
  "Restrição", "Pessoas/Equipe",
  "Presença de analistas N1 na sede em horário comercial. Alterado pela resposta nº 6 do Q&A (atuação remota permitida, desde que no Brasil). Não define quantos N1 em horário comercial nem a cobertura fora dele (o SOC é 24x7).",
  "Mandatório", "Explícita", 3, 3, "Custo de alocação presencial em São Paulo.",
  *NA, "{d5_q6}", "Alterado", "Atender", "—", "Delivery/Operação")

R("d2_vpn", "D02", "6. RESPONSABILIDADES DO CONTRATANTE — 6.1", f"{S6}, item 6.1",
  '''"6.1 Disponibilizar acesso remoto seguro (VPN) aos ambientes monitorados."''',
  "Responsabilidade / dependência do cliente", "Infraestrutura/Cloud",
  "Dependência do Banco para acesso remoto; prazo de disponibilização não definido, o que é crítico numa transição de 30 ou 60 dias.",
  "Mandatório", "Explícita", 3, 3, "Atraso do Banco consome o prazo de transição da Contratada.",
  ISO, "A.6.7 — Trabalho remoto", "Correlata", "{d2_c_trans}", "Vigente", "Registrar premissa na proposta",
  "Em que prazo após a assinatura a VPN estará disponível para a equipe da Contratada?", "Delivery/Operação")

R("d2_doc10", "D02", "6. RESPONSABILIDADES DO CONTRATANTE — 6.2", f"{S6}, item 6.2",
  '''"6.2 Disponibilizar a documentação técnica do ambiente em até 10 (dez) dias após a assinatura do contrato."''',
  "Responsabilidade / dependência do cliente", "Transição/Implantação",
  "A documentação técnica pode chegar só no 10º dia após a assinatura, um terço da transição de 30 dias (RFP 3.2). Somada à recusa do EPS até a contratação (Q&A nº 3), reduz o tempo efetivo de planejamento.",
  "Mandatório", "Explícita", 3, 3, "Reduz a janela útil de transição.",
  *NA, "{d1_trans30}, {d5_q3}, {d4_risco_trans}", "Vigente", "Registrar premissa na proposta", "—",
  "Delivery/Operação")

# =========================================================================== D03 — Anexo IV (não anexado)
R("d3_inv", "D03", "Documento completo", "Solicitação de análise — tabela \"Documentos anexados\", item 5",
  '''Listado pelo usuário: "Anexo_IV_Planilha_de_Precos.xlsx" · "Planilha de preços" · "v1.0" · Citado na RFP, 4.3: "conforme a planilha modelo do Anexo IV — Planilha de Preços"''',
  "Registro de cobertura", "Comercial/Preço",
  "Arquivo listado pelo usuário e NÃO ANEXADO: não foi recebido nesta análise (a extração registrou 'ARQUIVO NÃO ENCONTRADO'). Nenhum conteúdo foi lido: estrutura de preços, unidades de cobrança, campos obrigatórios e eventuais abas ocultas não foram analisados. A análise prosseguiu com os 4 documentos recebidos. Para completar a cobertura, anexe o arquivo e peça análise incremental (código D03 reservado).",
  "Informativo", "Explícita", None, None, "—", "—", "—", "—", "{d1_anexo4}", "Vigente", "Nenhuma (informativo)", "—",
  "Pricing/Financeiro")

# =========================================================================== D04 — Apresentação
R("d4_inv", "D04", "Documento completo (slides 1 a 5 e notas)", "slides 1–5 (inclui notas do slide 5)",
  '''"Workshop com proponentes — RFP nº 2026-017 — 22/10/2026"''',
  "Registro de cobertura", "Administrativo do processo",
  "Inventário: PowerPoint com 5 slides, sem slides ocultos sinalizados; notas do apresentador no slide 5, lidas e analisadas (contêm ampliação de escopo). Leitura integral.",
  "Informativo", "Explícita", None, None, "—", "—", "—", "—", "{d4_subsid}", "Vigente", "Nenhuma (informativo)", "—",
  "Bid Manager")

R("d4_c_users", "D04", "Números do ambiente × RFP 2.1", f"RFP {P2}, item 2.1 · slide 2 — \"Números do ambiente\"",
  '''A: "abrangendo aproximadamente 4.500 colaboradores" (RFP, 2.1) · B: "6.200 usuários ativos" (slide 2)''',
  "Contradição", "Operação/Serviços",
  "Base de usuários diverge em cerca de 38% (4.500 × 6.200). 'Colaboradores' × 'usuários ativos' pode explicar parte da diferença (terceiros, contas de serviço), mas não há definição. O Q&A nº 5 depois fixou 5.000 (ver {d5_c_users}).",
  "Informativo", "Explícita", 4, 3,
  "Preço de IAM e licenças por usuário pode ficar subdimensionado.",
  *NA, "{d1_users}, {d5_q5}, {d5_c_users}, {d4_subsid}", "Em esclarecimento", "Esclarecer no Q&A", "—",
  "Pré-venda/Arquitetura")

R("d4_serv", "D04", "Números do ambiente", "slide 2 — \"Números do ambiente\"",
  '''"850 servidores (70% Windows, 30% Linux)"''',
  "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Base de servidores para integração ao SIEM e para estimar volume de eventos (EPS não informado).",
  "Informativo", "Explícita", 3, 3, "Principal dado disponível para estimar EPS e licenças.",
  *NA, "{d2_integ}, {d5_q3}", "Vigente", "Precificar", "—", "Pré-venda/Arquitetura")

R("d4_dc", "D04", "Números do ambiente", "slide 2 — \"Números do ambiente\"",
  '''"2 data centers próprios (São Paulo e Campinas)"''',
  "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Duas localidades físicas; pode exigir coletores de log em ambas.",
  "Informativo", "Explícita", 2, 3, "Pequeno custo adicional de coleta.",
  *NA, "{d2_integ}", "Vigente", "Precificar", "—", "Pré-venda/Arquitetura")

R("d4_nuvens", "D04", "Números do ambiente", "slide 2 — \"Números do ambiente\"",
  '''"Workloads em 2 nuvens públicas"''',
  "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Provedores, contas e volume não identificados; a integração do SIEM exige conectores específicos por provedor.",
  "Informativo", "Explícita", 3, 3, "Esforço de integração não estimável sem os provedores.",
  *NA, "{d2_integ}", "Vigente", "Esclarecer no Q&A",
  "Quais são os provedores de nuvem pública, quantas contas ou assinaturas e quais serviços devem ser monitorados?",
  "Pré-venda/Arquitetura")

R("d4_legado", "D04", "Ferramentas atuais", "slide 3 — \"Ferramentas atuais\"",
  '''"SIEM legado — contrato encerra em 31/01/2027, sem possibilidade de prorrogação"''',
  "Premissa do cliente", "Transição/Implantação",
  "Data-limite rígida da plataforma atual: o SIEM do proponente precisa estar operacional até 31/01/2027, e a operação paralela (Anexo I, 4.2) e a migração de 24 meses de logs (slide 5) precisam ocorrer antes dessa data.",
  "Informativo", "Explícita", 4, 3, "Janela de transição fixa, sem o legado como contingência após 31/01/2027.",
  *NA, "{d1_inicio}, {d2_paral}, {d4_migr}, {d4_risco_trans}", "Vigente", "Mitigar", "—", "Delivery/Operação")

R("d4_risco_trans", "D04", "Combinação: RFP 3.1, 3.2 e 7.4 · Anexo I 4.1, 4.2 e 6.2 · slides 3 e 5 · Q&A nº 1, 3 e 4",
  f"slide 3 — \"Ferramentas atuais\" · RFP {P2}, itens 3.1 e 3.2",
  '''"SIEM legado — contrato encerra em 31/01/2027, sem possibilidade de prorrogação" · "Início previsto dos serviços 01/02/2027" · "A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato."''',
  "Risco para o proponente", "Transição/Implantação / Financeiro",
  "Inferida da combinação: entrega em 27/11/2026 (Q&A nº 1); legado encerra em 31/01/2027 sem prorrogação; operação paralela obrigatória e sem custo (Anexo I, 4.2); transição de 30 ou 60 dias contada de assinatura sem data; documentação técnica até 10 dias após a assinatura (6.2); EPS só informado ao vencedor (Q&A nº 3); migração de 24 meses de logs (slide 5); multa de 10% por ocorrência sem teto desde o início (7.4, mantida no Q&A nº 4). Entre a entrega e o fim do legado há 65 dias corridos para julgamento, assinatura, implantação, integração, migração e operação paralela; com 60 dias de transição, a assinatura teria de ocorrer até 02/12/2026. Probabilidade 4: as datas são explícitas, não deixam folga e o cliente declara que o legado não pode ser prorrogado. Severidade 5: exposição a multas sem teto desde o primeiro mês e risco de não conseguir entregar.",
  "Informativo", "Inferida", 5, 4,
  "Risco de iniciar a operação sem plataforma estável nem legado de contingência, sob multas sem limite; custo de implantação acelerada.",
  *NA, "{d1_entrega}, {d1_inicio}, {d1_lac_assin}, {d1_trans30}, {d2_c_trans}, {d2_paral}, {d2_doc10}, {d4_legado}, {d4_migr}, {d1_multa}, {d5_q1}, {d5_q3}, {d5_q4}",
  "Vigente", "Avaliar Go/No-Go",
  "Considerando o fim do contrato do SIEM legado em 31/01/2027 sem prorrogação, qual a data prevista de assinatura? Haverá carência na aplicação de multas de SLA nos primeiros meses de operação?",
  "Bid Manager")

R("d4_iam", "D04", "Ferramentas atuais", "slide 3 — \"Ferramentas atuais\"",
  '''"IAM: Active Directory + scripts internos"''',
  "Dado de dimensionamento", "Segurança da Informação/Cyber",
  "IAM atual sem ferramenta de governança de identidades: ciclo de vida e recertificação (Anexo I, 3.1 e 3.3) exigirão ferramenta ou esforço manual; scripts internos podem não estar documentados.",
  "Informativo", "Explícita", 3, 3, "Esforço de automação e de herança dos scripts.",
  *NA, "{d2_lac_iamtool}, {d2_iam_ciclo}, {d2_recert}", "Vigente", "Precificar", "—", "Pré-venda/Arquitetura")

R("d4_pam", "D04", "Ferramentas atuais", "slide 3 — \"Ferramentas atuais\"",
  '''"Não há solução de PAM"''',
  "Dado de dimensionamento", "Segurança da Informação/Cyber",
  "A ausência de PAM confirma o item desejável 3.4 como oportunidade e torna o MFA de privilegiados (3.2) dependente de outra solução.",
  "Informativo", "Explícita", 2, 3, "Pequeno; orienta a oferta.",
  *NA, "{d2_pam}, {d2_mfa}", "Vigente", "Nenhuma (informativo)", "—", "Pré-venda/Arquitetura")

R("d4_alertas", "D04", "Desafios", "slide 4 — \"Desafios\"",
  '''"Cerca de 1.200 alertas por dia"''',
  "Dado de dimensionamento", "Operação/Serviços",
  "Volume atual de alertas (cerca de 36.000 por mês), base para dimensionar analistas N1; pode mudar com o novo SIEM e com as subsidiárias.",
  "Informativo", "Explícita", 3, 3, "Base de dimensionamento da equipe de triagem.",
  *NA, "{d4_fp}, {d4_subsid}", "Vigente", "Precificar", "—", "Delivery/Operação")

R("d4_fp", "D04", "Desafios", "slide 4 — \"Desafios\"",
  '''"70% de falsos positivos"''',
  "Dado de dimensionamento", "Operação/Serviços",
  "Linha de base de falsos positivos (cerca de 840 alertas por dia).",
  "Informativo", "Explícita", 2, 3, "Indica esforço inicial de ajuste de regras.",
  *NA, "{d4_meta}", "Vigente", "Nenhuma (informativo)", "—", "Delivery/Operação")

R("d4_meta", "D04", "Desafios", "slide 4 — \"Desafios\"",
  '''"Meta: reduzir os falsos positivos para 10% no primeiro trimestre de operação"''',
  "Ambiguidade", "Operação/Serviços",
  "Meta agressiva (70% para 10% em 3 meses) apresentada só no workshop, ausente do Anexo I. Não está claro se é SLA/KPI contratual sujeito à multa de 10% (7.4) nem como 'falso positivo' é medido. Tipo escolhido: Ambiguidade; poderia ser SLA / KPI.",
  "Desejável", "Explícita", 4, 3,
  "Se contratual, exige ajuste intensivo de regras no 1º trimestre, simultâneo à estabilização; se não, é diferencial.",
  *NA, "{d4_fp}, {d1_multa}", "Em esclarecimento", "Esclarecer no Q&A",
  "A meta de reduzir os falsos positivos para 10% no primeiro trimestre é SLA contratual sujeito a multa? Como será medido o percentual de falsos positivos?",
  "Delivery/Operação")

R("d4_migr", "D04", "Expectativas para o novo serviço", "slide 5 — \"Expectativas para o novo serviço\"",
  '''"Migração de 24 meses de logs históricos do SIEM legado para a nova plataforma"''',
  "Ambiguidade", "Transição/Implantação / Dados/Analytics",
  "Escopo ausente da RFP e do Anexo I, apresentado como 'expectativa'. Volume, formato e produto do legado não informados; depende de acesso ao SIEM legado, que encerra em 31/01/2027. Os 24 meses excedem a retenção mínima de 12 meses (Anexo I, 1.3). Tipo escolhido: Ambiguidade; se vinculante, é Requisito funcional.",
  "Desejável", "Explícita", 4, 3,
  "Esforço e custo de ingestão e armazenamento relevantes fora do escopo formal.",
  *NA, "{d2_amb_ret}, {d4_legado}, {d4_risco_trans}", "Em esclarecimento", "Esclarecer no Q&A",
  "A migração de 24 meses de logs históricos do SIEM legado integra o escopo contratual? Qual o volume, o produto do SIEM legado e o formato dos dados? O fornecedor atual apoiará a extração?",
  "Pré-venda/Arquitetura")

R("d4_visao", "D04", "Expectativas para o novo serviço", "slide 5 — \"Expectativas para o novo serviço\"",
  '''"Visão unificada de riscos para a diretoria"''',
  "Ambiguidade", "Dados/Analytics / Segurança da Informação/Cyber",
  "Expectativa sem definição de entregável (painel, relatório executivo, ferramenta de GRC), periodicidade ou fontes; ausente do Anexo I.",
  "Desejável", "Explícita", 3, 3, "Escopo de relatórios e ferramentas indefinido.",
  *NA, "{d2_rel}", "Em esclarecimento", "Esclarecer no Q&A",
  "O que se espera da 'visão unificada de riscos para a diretoria' (formato, periodicidade, fontes) e ela integra o escopo contratual?",
  "Pré-venda/Arquitetura")

R("d4_subsid", "D04", "Expectativas para o novo serviço — notas do apresentador", "slide 5 — notas do apresentador",
  '''"as subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários adicionais) também deverão ser incluídas no escopo"''',
  "Ambiguidade", "Operação/Serviços / Jurídico/Contratual",
  "Ampliação de escopo registrada só nas notas do apresentador (não exibidas no slide). As subsidiárias não aparecem no objeto da RFP (2.1), no Anexo I nem no Q&A nº 5 (5.000 usuários). Não está claro se serão partes do contrato, se seus usuários estão nos 6.200 ou se somam (até 7.100), nem se seus ambientes entram no SOC. Tipo escolhido: Ambiguidade; o texto usa 'deverão', o que a tornaria requisito mandatório.",
  "Mandatório", "Explícita", 4, 3,
  "Até cerca de 900 usuários e ambientes adicionais não precificados; contratação com entidades jurídicas distintas.",
  *NA, "{d1_users}, {d4_c_users}, {d5_q5}, {d5_c_users}", "Em esclarecimento", "Esclarecer no Q&A",
  "As subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários) fazem parte do escopo, como informado no workshop? Seus usuários estão incluídos nos 6.200 ou se somam a eles? Seus ambientes serão monitorados pelo SOC e elas serão partes do contrato?",
  "Bid Manager")

# =========================================================================== D05 — Q&A e questionário
QA = 'aba "Q&A Rodada 1"'
QT = 'aba "Questionário Técnico"'
PS = 'aba "Pesos" (oculta)'

R("d5_inv", "D05", "Documento completo (4 abas)", 'abas "Instruções", "Q&A Rodada 1", "Questionário Técnico", "Pesos" (oculta)',
  '''"Questionário Técnico e Respostas aos Esclarecimentos — RFP nº 2026-017"''',
  "Registro de cobertura", "Administrativo do processo",
  "Inventário: Excel com 4 abas; aba 'Pesos' OCULTA, lida e analisada (contém pesos dos requisitos e regra de pontuação não prevista na RFP). Sem linhas ou colunas ocultas nem comentários. Q&A Rodada 1 com 6 perguntas, todas datadas de 12/11/2026. Leitura integral.",
  "Informativo", "Explícita", None, None, "—", "—", "—", "—", "{d5_c_pesos}", "Vigente", "Nenhuma (informativo)", "—",
  "Bid Manager")

R("d5_instr", "D05", "Instruções — A3", 'aba "Instruções" · A3',
  '''"O preenchimento de todas as abas deste arquivo é obrigatório. Questionários incompletos serão desclassificados."''',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Acrescenta a sanção de desclassificação ao preenchimento do questionário (a RFP 4.4 não previa sanção). Probabilidade 5: questionário incompleto leva diretamente à desclassificação pelo texto.",
  "Mandatório", "Explícita", 5, 5, "Desclassificação.",
  *NA, "{d1_quest}, {d5_amb_abas}", "Vigente", "Atender", "—", "Pré-venda/Arquitetura")

R("d5_amb_abas", "D05", "Instruções — A3", 'aba "Instruções" · A3',
  '''"O preenchimento de todas as abas deste arquivo é obrigatório."''',
  "Ambiguidade", "Administrativo do processo",
  "'Todas as abas' incluiria 'Instruções', 'Q&A Rodada 1' e a aba oculta 'Pesos', que não têm campos para o proponente. Também não se define se a coluna 'Comentários' é obrigatória nem se 'Parcial' conta como preenchido. Severidade 5: uma interpretação divergente pode levar à desclassificação.",
  "Mandatório", "Explícita", 5, 3, "Risco de desclassificação por preenchimento considerado incompleto.",
  *NA, "{d5_instr}, {d1_quest}", "Em esclarecimento", "Esclarecer no Q&A",
  "Quais abas e colunas devem ser preenchidas pelo proponente? A coluna 'Comentários' é obrigatória? As abas 'Instruções', 'Q&A Rodada 1' e 'Pesos' exigem alguma ação?",
  "Bid Manager")

R("d5_q1", "D05", "Q&A Rodada 1 — pergunta nº 1 (RFP, item 3.1)", f"{QA} · E2 · pergunta nº 1 · Rodada 1 (12/11/2026)",
  '''"A data de entrega das propostas fica prorrogada para 27/11/2026, até as 18h."''',
  "Prazo / marco", "Administrativo do processo",
  "Altera a entrega de 20/11/2026 para 27/11/2026, até as 18h. Embora não haja cláusula de precedência, a alteração é expressa e posterior; tratada como vigente.",
  "Mandatório", "Explícita", 5, 3, "Proposta fora do prazo pode não ser recebida.",
  *NA, "{d1_entrega}, {d4_risco_trans}", "Vigente", "Atender", "—", "Bid Manager")

R("d5_q2", "D05", "Q&A Rodada 1 — pergunta nº 2 (RFP, item 5.1 c)", f"{QA} · E3 · pergunta nº 2 · Rodada 1 (12/11/2026)",
  '''"Não. O SOC deverá estar localizado em território nacional."''',
  "Critério eliminatório / de habilitação", "Regulatório/Compliance / Operação/Serviços",
  "Confirma o critério 5.1 c): SOC no Brasil, sem operação a partir de outro país. Não trata da localização dos dados nem da região de nuvem do SIEM; a contradição Anexo I 1.2 × Anexo III permanece. Probabilidade 5: o não atendimento leva diretamente à inabilitação.",
  "Mandatório", "Explícita", 5, 5, "Inabilitação.",
  *NA, "{d1_socbr}, {d2_c_nuvem}", "Duplicado", "Atender", "—", "Delivery/Operação")

R("d5_q3", "D05", "Q&A Rodada 1 — pergunta nº 3 (Anexo I, item 1.4)", f"{QA} · E4 · pergunta nº 3 · Rodada 1 (12/11/2026)",
  '''"A volumetria será informada somente ao proponente vencedor."''',
  "Lacuna", "Técnico/Arquitetura / Comercial/Preço",
  "O cliente recusou formalmente informar o EPS antes da contratação. O EPS é o principal direcionador de custo de licenças, armazenamento (12 meses e 5 anos) e equipe do SIEM. Probabilidade 5: informação indispensável ao preço recusada formalmente pelo cliente. Severidade 4, e não 5, porque o impacto pode ser mitigado com premissa de volumetria e cláusula de revisão na proposta.",
  "Informativo", "Explícita", 4, 5,
  "Preço do SIEM e do armazenamento calculado sobre volumetria estimada; risco de prejuízo se o volume real for maior.",
  *NA, "{d2_integ}, {d2_siem}, {d4_serv}, {d4_alertas}, {d4_risco_trans}", "Vigente", "Registrar premissa na proposta",
  "Na impossibilidade de informar o EPS, o Banco aceitará proposta com premissa de volumetria (EPS e GB/dia) e cláusula de reequilíbrio caso o volume real a exceda? É possível informar ao menos uma faixa ou o volume diário ingerido pelo SIEM legado?",
  "Pricing/Financeiro")

R("d5_q4", "D05", "Q&A Rodada 1 — pergunta nº 4 (RFP, item 7.4)", f"{QA} · E5 · pergunta nº 4 · Rodada 1 (12/11/2026)",
  '''"As condições do item 7 permanecem inalteradas."''',
  "Penalidade / multa / glosa", "Jurídico/Contratual / Financeiro",
  "À pergunta sobre limite das multas, o cliente manteve todo o item 7: multa de 10% por ocorrência sem teto (7.4) e responsabilidade ilimitada (7.5). A resposta não define 'ocorrência'. Probabilidade 4: a multa é automática por ocorrência e o cliente recusou formalmente limitá-la.",
  "Mandatório", "Explícita", 5, 4, "Exposição financeira sem limite confirmada.",
  CC, "Art. 412 — limite da cláusula penal ao valor da obrigação principal", "Correlata",
  "{d1_multa}, {d1_resp_ilim}, {d1_seguro}, {d4_risco_trans}", "Vigente", "Avaliar Go/No-Go", "—", "Jurídico")

R("d5_q5", "D05", "Q&A Rodada 1 — pergunta nº 5 (RFP, item 2.1)", f"{QA} · E6 · pergunta nº 5 · Rodada 1 (12/11/2026)",
  '''"Considerar 5.000 usuários."''',
  "Dado de dimensionamento", "Operação/Serviços",
  "Altera a base da RFP (4.500 colaboradores) para 5.000 usuários. Não esclarece se inclui as subsidiárias (notas do slide 5) nem por que difere dos 6.200 usuários ativos do slide 2.",
  "Mandatório", "Explícita", 4, 3, "Base de preço do IAM ainda incerta.",
  *NA, "{d1_users}, {d5_c_users}, {d4_subsid}", "Em esclarecimento", "Precificar", "—", "Pré-venda/Arquitetura")

R("d5_c_users", "D05", "Q&A Rodada 1 — pergunta nº 5 × Apresentação slides 2 e 5",
  f"{QA} · E6 · pergunta nº 5 · Rodada 1 (12/11/2026) · slide 2 — \"Números do ambiente\" · slide 5 — notas do apresentador",
  '''A: "Considerar 5.000 usuários." (Q&A nº 5) · B: "6.200 usuários ativos" (slide 2) · "cerca de 900 usuários adicionais" (slide 5, notas)''',
  "Contradição", "Operação/Serviços",
  "Mesmo após o esclarecimento, a base diverge: 5.000 (Q&A) × 6.200 usuários ativos (workshop) × até 7.100 com as subsidiárias. Sem cláusula de precedência, não se presume que o Q&A prevaleça sobre o workshop nem que as subsidiárias estejam excluídas.",
  "Mandatório", "Explícita", 4, 3,
  "Possível subdimensionamento de até cerca de 42% (5.000 × 7.100) em licenças e esforço de IAM.",
  *NA, "{d5_q5}, {d4_c_users}, {d4_subsid}, {d1_users}, {d1_preced}", "Em esclarecimento", "Esclarecer no Q&A",
  "O Q&A nº 5 indica 5.000 usuários; o workshop apresentou 6.200 usuários ativos e mencionou cerca de 900 usuários das subsidiárias. Qual quantidade deve ser considerada para preço e SLA, e ela inclui terceiros, contas de serviço e as subsidiárias?",
  "Pré-venda/Arquitetura")

R("d5_q6", "D05", "Q&A Rodada 1 — pergunta nº 6 (Anexo I, item 5.2)", f"{QA} · E7 · pergunta nº 6 · Rodada 1 (12/11/2026)",
  '''"Sim, desde que em território nacional."''',
  "Restrição", "Pessoas/Equipe",
  "Altera o Anexo I, 5.2: analistas N1 podem atuar remotamente, desde que no Brasil. Reduz o custo de alocação em São Paulo; não fica claro se a presença na sede deixa de ser exigida em qualquer caso.",
  "Mandatório", "Explícita", 2, 3, "Reduz custo; mantém restrição territorial.",
  *NA, "{d2_n1}, {d1_socbr}", "Vigente", "Atender", "—", "Delivery/Operação")

R("d5_qt01", "D05", "Questionário Técnico — QT-01", f"{QT} · B2:C2 (QT-01) · {PS} · B2",
  '''"Possui certificação ISO/IEC 27001 com escopo que inclua os serviços de SOC?" · Obrigatório: "Sim" · Peso: "3"''',
  "Critério de avaliação / pontuação", "Segurança da Informação/Cyber",
  "Repete a habilitação 5.1 a) da RFP, agora com peso 3 (o maior, empatado com QT-04). Efeito de 'Não atende' em item obrigatório não definido.",
  "Mandatório", "Explícita", 3, 3, "Pontuação do questionário.",
  "ISO/IEC 27001:2022", "Requisitos do SGSI, cláusulas 4 a 10 (certificação)", "Direta",
  "{d1_iso}, {d5_lac_pesos}", "Duplicado", "Atender", "—", "Compliance")

R("d5_qt02", "D05", "Questionário Técnico — QT-02", f"{QT} · B3:C3 (QT-02) · {PS} · B3",
  '''"Oferece integração nativa com plataforma SOAR?" · Obrigatório: "Não" · Peso: "1"''',
  "Critério de avaliação / pontuação", "Técnico/Arquitetura",
  "Funcionalidade ausente do Anexo I. Não obrigatória, mas pela regra da aba oculta 'Pesos' a resposta 'Não atende' reduz a Nota Técnica em 2 pontos.",
  "Desejável", "Explícita", 3, 3, "Perda de 2 pontos se não ofertado.",
  CSF, "RS.MA — Incident Management", "Correlata", "{d5_c_pesos}, {d1_crit_ferr}", "Vigente", "Precificar", "—",
  "Pré-venda/Arquitetura")

R("d5_qt03", "D05", "Questionário Técnico — QT-03", f"{QT} · B4:C4 (QT-03) · {PS} · B4",
  '''"Retém os logs online por no mínimo 12 meses?" · Obrigatório: "Sim" · Peso: "2"''',
  "Critério de avaliação / pontuação", "Infraestrutura/Cloud",
  "Introduz o termo 'online', ausente do Anexo I (1.3); sugere que os 5 anos do item 1.6 podem ser em arquivo.",
  "Mandatório", "Explícita", 3, 3, "Pontuação e definição do modelo de retenção.",
  ISO, "A.8.15 — Registro de logs", "Direta", "{d2_ret12}, {d2_amb_ret}", "Vigente", "Atender", "—",
  "Pré-venda/Arquitetura")

R("d5_qt04", "D05", "Questionário Técnico — QT-04", f"{QT} · B5:C5 (QT-04) · {PS} · B5",
  '''"Atende aos requisitos da Resolução CMN nº 4.893/2021?" · Obrigatório: "Sim" · Peso: "3"''',
  "Critério de avaliação / pontuação", "Regulatório/Compliance",
  "A resolução se dirige às instituições financeiras; não está claro quais requisitos o prestador deve atender nem como comprovar. Um 'Atende' genérico pode virar obrigação contratual ampla. Peso 3 (o maior).",
  "Mandatório", "Explícita", 3, 3, "Pontuação relevante e compromisso regulatório de alcance indefinido.",
  CMN, "Requisitos aplicáveis a prestadores de serviços contratados (identificador a confirmar)", "Direta",
  "{d1_cmn}, {d5_lac_pesos}", "Em esclarecimento", "Esclarecer no Q&A",
  "Quais requisitos da Resolução CMN nº 4.893/2021 o prestador deve atender e comprovar para responder 'Atende' ao QT-04?",
  "Compliance")

R("d5_qt05", "D05", "Questionário Técnico — QT-05", f"{QT} · B6:C6 (QT-05) · {PS} · B6",
  '''"Oferece serviço de threat intelligence?" · Obrigatório: "Não" · Peso: "2"''',
  "Critério de avaliação / pontuação", "Segurança da Informação/Cyber",
  "Serviço ausente do Anexo I. Não obrigatório, mas 'Não atende' reduz 2 pontos (regra da aba oculta). Fontes externas podem esbarrar na vedação de subcontratação (7.7) e na restrição de dados no Brasil (Anexo III).",
  "Desejável", "Explícita", 3, 3, "Perda de 2 pontos se não ofertado; custo de feeds se ofertado.",
  ISO, "A.5.7 — Inteligência de ameaças", "Direta", "{d5_c_pesos}, {d1_subc}, {d1_anexo3_dados}", "Vigente",
  "Precificar", "—", "Segurança/Cyber")

R("d5_qt06", "D05", "Questionário Técnico — QT-06", f"{QT} · B7:C7 (QT-06) · {PS} · B7",
  '''"Possui equipe com certificações reconhecidas pelo mercado?" · Obrigatório: "Sim" · Peso: "2"''',
  "Critério de avaliação / pontuação", "Pessoas/Equipe",
  "Critério subjetivo: 'certificações reconhecidas pelo mercado' não são definidas; relaciona-se à 'equipe devidamente certificada' da RFP (5.2).",
  "Mandatório", "Explícita", 3, 3, "Pontuação subjetiva.",
  *NA, "{d1_equipe}, {d1_crit_equipe}", "Em esclarecimento", "Esclarecer no Q&A", "—", "RH/Staffing")

R("d5_c_pesos", "D05", "Pesos (aba oculta) — A9 × RFP 6.2", f"{PS} · A9 · RFP {P4}, item 6.2",
  '''A: "Requisitos não obrigatórios respondidos como 'Não atende' reduzem a Nota Técnica em 2 (dois) pontos cada." (aba "Pesos", oculta) · B: "A Nota Técnica, de no máximo 60 (sessenta) pontos, será atribuída conforme os critérios abaixo" (RFP, 6.2)''',
  "Contradição", "Administrativo do processo",
  "Regra de pontuação presente só em aba oculta e ausente do item 6.2 da RFP, que define a Nota Técnica apenas pelos quatro critérios. Penaliza requisitos 'não obrigatórios' (QT-02 e QT-05: até −4 pontos), contrariando o caráter opcional, e pode levar à nota de corte de 70% (6.3). Não se sabe se alcança itens desejáveis do Anexo I (PAM, 3.4).",
  "Mandatório", "Explícita", 4, 3,
  "Perda de até 4 pontos (cerca de 7% da nota técnica máxima) e risco de desclassificação pela nota de corte.",
  *NA, "{d1_c_soma}, {d1_corte}, {d1_lac_sub}, {d5_qt02}, {d5_qt05}, {d2_pam}", "Em esclarecimento",
  "Esclarecer no Q&A",
  "A redução de 2 pontos por requisito não obrigatório respondido como 'Não atende' (aba 'Pesos' do questionário) está em vigor? Como ela se compõe com os critérios e a pontuação máxima do item 6.2 da RFP?",
  "Bid Manager")

R("d5_lac_pesos", "D05", "Pesos (aba oculta) — A1:B7", f"{PS} · A1:B7",
  '''Não localizado · "ID" · "Peso" (aba "Pesos", A1:B1)''',
  "Lacuna", "Administrativo do processo",
  "Os pesos 1 a 3 de QT-01 a QT-06 não têm regra de uso: não se sabe como entram na Nota Técnica (em qual critério do 6.2) nem o efeito de 'Não atende' ou 'Parcial' em itens obrigatórios (QT-01, 03, 04 e 06): eliminação, perda de pontos ou nenhum.",
  "Informativo", "Explícita", 4, 3, "Impossível estimar a pontuação do questionário.",
  *NA, "{d5_c_pesos}, {d1_lac_sub}, {d5_qt01}, {d5_qt04}", "Em esclarecimento", "Esclarecer no Q&A",
  "Como os pesos do questionário técnico são convertidos em pontos da Nota Técnica? Qual o efeito das respostas 'Não atende' e 'Parcial' em requisitos obrigatórios?",
  "Bid Manager")

# =========================================================================== montagem
ids, cnt = {}, {}
for r in ROWS:
    d = r["doc"]
    cnt[d] = cnt.get(d, 0) + 1
    ids[r["key"]] = f"{d}-{cnt[d]:03d}"


def band(s):
    return "Baixa" if s <= 4 else "Média" if s <= 9 else "Alta" if s <= 15 else "Crítica"


def clean(x):
    x = x.format_map(ids)
    return x.replace("|", "/").replace("\n", " ").strip() or "—"


COLS = ["ID", "Documento", "Versão/Data", "Seção/Cláusula", "Localizador", "Evidência", "Tipo de item", "Domínio",
        "Descrição analítica", "Obrigatoriedade", "Natureza da evidência", "Severidade", "Probabilidade", "Criticidade",
        "Impacto para o proponente", "Framework/Referência", "Controle/Cláusula", "Tipo de associação",
        "IDs relacionados", "Status de vigência", "Ação recomendada", "Pergunta de esclarecimento",
        "Responsável interno sugerido"]
lines = []
for r in ROWS:
    fn, ver, _ = DOCS[r["doc"]]
    if r["sev"] is None:
        s = p = c = "—"
    else:
        sc = r["sev"] * r["prob"]
        b = band(sc)
        if r["sev"] == 5 and b in ("Baixa", "Média"):
            b = "Alta"
        s, p, c = f'{r["sev"]} · {SEV[r["sev"]]}', f'{r["prob"]} · {PROB[r["prob"]]}', f"{sc} · {b}"
    cells = [ids[r["key"]], fn, ver, r["sec"], r["loc"], r["ev"], r["tipo"], r["dom"], r["desc"], r["obr"], r["nat"],
             s, p, c, r["imp"], r["fw"], r["ctrl"], r["assoc"], r["rel"], r["st"], r["acao"], r["perg"], r["resp"]]
    lines.append("| " + " | ".join(clean(x) for x in cells) + " |")

last = list(ids.values())[-1]
pend = [ids["d3_inv"], ids["d2_lac_matriz"], ids["d1_lac_anexo2"]]
md = []
md.append("# RFP nº 2026-017 — Matriz Analítica")
md.append("")
md.append("Cliente: Banco Horizonte Fictício S.A. · Objeto: serviços gerenciados de SOC e IAM · Valor estimado do contrato: não informado")
md.append("")
md.append("## Documentos")
md.append("")
md.append("| Código | Arquivo | Tipo | Versão/Data | Situação |")
md.append("|---|---|---|---|---|")
sit = {"D01": "Processado (p. 6 lida por OCR)", "D02": "Processado", "D03": "NÃO ANEXADO — não processado (ver D03-001)",
       "D04": "Processado (inclui notas do apresentador)", "D05": "Processado (inclui aba oculta \"Pesos\")"}
for k, (fn, ver, tp) in DOCS.items():
    md.append(f"| {k} | {fn} | {tp} | {ver} | {sit[k]} |")
md.append("")
md.append("## Matriz")
md.append("")
md.append("| " + " | ".join(COLS) + " |")
md.append("|" + "---|" * len(COLS))
md += lines
md.append("")
md.append("✅ STATUS: ANÁLISE CONCLUÍDA")
md.append(f"Documentos processados: 4 de 5 (D03 — Anexo_IV_Planilha_de_Precos.xlsx listado e não anexado) · Total de itens: {len(lines)} (de D01-001 a {last})")
md.append(f"Pendências de cobertura: {ids['d3_inv']} (arquivo listado pelo usuário e não anexado: Anexo_IV_Planilha_de_Precos.xlsx) · "
          f"{ids['d2_lac_matriz']} (Lacuna: matriz de classificação de incidentes do Contratante citada e não fornecida) · "
          f"{ids['d1_lac_anexo2']} (Lacuna inferida: Anexo II não citado nem fornecido)")
md.append('Não é necessário enviar "continuar".')
md.append("")
OUT.write_text("\n".join(md), encoding="utf-8")

# resumo por documento para o relatório
from collections import Counter
crit = Counter()
for r in ROWS:
    if r["sev"] is not None:
        sc = r["sev"] * r["prob"]
        b = band(sc)
        if r["sev"] == 5 and b in ("Baixa", "Média"):
            b = "Alta"
        crit[b] += 1
print("linhas:", len(lines), "por doc:", cnt, "criticidade:", dict(crit), "último:", last)
