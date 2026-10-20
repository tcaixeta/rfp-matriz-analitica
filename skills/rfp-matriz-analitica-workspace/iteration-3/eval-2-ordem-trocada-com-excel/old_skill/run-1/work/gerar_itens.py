#!/usr/bin/env python3
"""Gera itens.json para a matriz da RFP 2026-017. Uso: gerar_itens.py <saida.json> <n_docs_concluidos>"""
import json
import sys

ITENS = []

ISO = "ISO/IEC 27001:2022"
CMN = "Resolução CMN nº 4.893/2021"
CC = "Código Civil (Lei 10.406/2002)"
LGPD = "LGPD (Lei 13.709/2018)"
NA = "Não aplicável"


def I(chave, doc, secao, loc, evid, tipo, dom, desc, obrig="Informativo", s=None, p=None, impacto="—",
      fw="—", ctrl="—", assoc=NA, rel=None, vig="Vigente", acao="Nenhuma (informativo)", perg="—",
      resp="Bid Manager", nat="Explícita", pend=None):
    it = dict(chave=chave, doc=doc, secao=secao, localizador=loc, evidencia=evid, tipo=tipo, dominio=dom,
              descricao=desc, obrigatoriedade=obrig, natureza=nat, impacto=impacto, framework=fw, controle=ctrl,
              associacao=assoc, relacionados=rel or [], vigencia=vig, acao=acao, pergunta=perg, responsavel=resp)
    if s is not None:
        it["s"], it["p"] = s, p
    if pend:
        it["pendencia"] = pend
    ITENS.append(it)


# =============================================================== D01 — RFP (PDF)
I("d01_inv", "D01", "Documento inteiro (capa, itens 1 a 7 e Anexo III)", "p. 1–6",
  '"Solicitação de Proposta (RFP) nº 2026-017" · "Versão 1.0 — 15/10/2026"',
  "Registro de cobertura", "Administrativo do processo",
  "Inventário: PDF com 6 páginas físicas (p. 1 capa sem número; p. 2–6 impressas 1–5). Páginas 1 a 5 com texto extraível, integralmente analisadas. A p. 6 (impressa: 5) não tem texto extraível: é imagem digitalizada do Anexo III — Declaração de Localização de Dados, lida visualmente e analisada com localizador (OCR). O corpo da RFP não cita o Anexo III; ele só aparece como página digitalizada ao final do PDF.",
  fw="—", assoc="—", resp="Bid Manager")

I("d01_regime", "D01", "1. Apresentação — 1.2 · 4. Instruções — 4.1", "p. 2 (impressa: 1) · p. 3 (impressa: 2)",
  '"O Banco é instituição financeira autorizada a funcionar pelo Banco Central do Brasil e está sujeito à Resolução CMN nº 4.893/2021" · "enviada exclusivamente pelo portal de fornecedores do Banco"',
  "Registro de cobertura", "Regulatório/Compliance",
  "Regime identificado: contratação PRIVADA (Contratante é sociedade anônima — \"Banco Horizonte Fictício S.A.\" —, processo conduzido por RFP e portal de fornecedores, sem menção a licitação, edital, pregão ou Lei 14.133/2021) em SETOR REGULADO (instituição financeira autorizada pelo Banco Central, sujeita à Resolução CMN nº 4.893/2021). Legislação associada nesta matriz: Código Civil, LGPD e Resolução CMN nº 4.893/2021. A Lei 14.133/2021 não se aplica.",
  fw="—", assoc="—", resp="Jurídico")

I("d01_precedencia", "D01", "Documento inteiro (sem cláusula de precedência)", "p. 1–6",
  'Não localizado · "As especificações técnicas detalhadas constam do Anexo I — Especificação Técnica."',
  "Lacuna", "Jurídico/Contratual",
  "Nenhum dos quatro documentos (RFP, Anexo I, apresentação do workshop e Q&A/questionário) define ordem de precedência. Já existem conflitos entre eles (transição de 30 × 60 dias; 4.500 × 5.000 × 6.200 usuários; SIEM em nuvem de livre escolha × dados exclusivamente no Brasil), e o Q&A, embora mais recente, não declara que altera a RFP. Não se presume que o documento mais recente prevaleça. Também não foi fornecida minuta de contrato.",
  obrig="Informativo", s=4, p=3, nat="Inferida",
  impacto="Sem precedência definida, cada conflito pode ser resolvido contra o proponente após a assinatura; afeta preço, prazo e escopo de todos os itens em contradição.",
  fw=CC, ctrl="Interpretação dos contratos (identificador a confirmar)", assoc="Correlata",
  rel=["d02_contr_transicao", "d04_contr_usuarios", "d02_contr_nuvem"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="Qual a ordem de precedência entre a RFP, o Anexo I, o Anexo III, o material do workshop e as respostas do Q&A em caso de divergência? As respostas do Q&A integram o contrato e prevalecem sobre a RFP e seus anexos?",
  resp="Jurídico")

I("d01_cmn", "D01", "1. Apresentação — 1.2", "p. 2 (impressa: 1)",
  '"está sujeito à Resolução CMN nº 4.893/2021, que dispõe sobre a política de segurança cibernética e sobre os requisitos para a contratação de serviços de processamento e armazenamento de dados e de computação em nuvem"',
  "Requisito implícito", "Regulatório/Compliance",
  "Inferência: o SIEM em nuvem (Anexo I 1.2) e o armazenamento de logs pelo proponente caracterizam contratação de serviços de processamento, armazenamento de dados e computação em nuvem por instituição financeira, sujeita aos requisitos da resolução citada. O contrato deverá conter as cláusulas exigidas pela norma (por exemplo, acesso do regulador, continuidade e comunicação de incidentes), mas a minuta não foi fornecida e a RFP não as detalha.",
  obrig="Mandatório", s=4, p=3, nat="Inferida",
  impacto="Obrigações regulatórias adicionais (cláusulas, evidências, auditorias, local dos dados) com custo e esforço não descritos; pode restringir a arquitetura do SIEM.",
  fw=CMN, ctrl="Requisitos para contratação de processamento, armazenamento e nuvem (identificador a confirmar)",
  assoc="Direta", rel=["d02_siem_nuvem", "d04_qt04"], acao="Esclarecer no Q&A",
  perg="Quais obrigações decorrentes da Resolução CMN nº 4.893/2021 serão exigidas contratualmente da Contratada (por exemplo, acesso do Banco Central a dados e informações, notificação de incidentes, plano de continuidade, local de armazenamento)? É possível disponibilizar a minuta de contrato?",
  resp="Compliance")

I("d01_objeto_soc", "D01", "2. Objeto — 2.1", "p. 2 (impressa: 1)",
  '"prestação de serviços gerenciados de Centro de Operações de Segurança (SOC), em regime 24x7x365"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber / Operação/Serviços",
  "Escopo principal: SOC gerenciado em regime ininterrupto (24 horas, 7 dias, 365 dias). Detalhado no Anexo I, item 1.1.",
  obrig="Mandatório", s=3, p=3,
  impacto="Define a escala de turnos 24x7 e a base de custo de equipe da proposta.",
  fw="NIST CSF 2.0", ctrl="DE.CM — Monitoramento contínuo", assoc="Direta",
  rel=["d02_monit"], acao="Precificar", resp="Delivery/Operação")

I("d01_objeto_iam", "D01", "2. Objeto — 2.1", "p. 2 (impressa: 1)",
  '"de gestão de identidades e acessos (IAM)"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Escopo de IAM gerenciado. A RFP não diz se o proponente fornece a plataforma de IAM/IGA ou opera a existente (Active Directory + scripts, conforme workshop). Detalhado no Anexo I, item 3.",
  obrig="Mandatório", s=3, p=3,
  impacto="Escopo de IAM sem definição de ferramenta altera significativamente licenciamento e esforço.",
  fw=ISO, ctrl="A.5.16 — Gestão de identidade", assoc="Direta",
  rel=["d02_iam_lacuna"], acao="Precificar", resp="Pré-venda/Arquitetura")

I("d01_usuarios", "D01", "2. Objeto — 2.1", "p. 2 (impressa: 1)",
  '"abrangendo aproximadamente 4.500 colaboradores"',
  "Dado de dimensionamento", "Comercial/Preço",
  "Base de dimensionamento original: cerca de 4.500 colaboradores. Alterada pela resposta 5 do Q&A (5.000 usuários) e em conflito com o workshop (6.200 usuários ativos e mais cerca de 900 das subsidiárias).",
  s=3, p=3, impacto="Base de preço por usuário de SOC e IAM.",
  rel=["d04_q5", "d03_usuarios", "d04_contr_usuarios"], vig="Alterado", acao="Precificar",
  resp="Pricing/Financeiro")

I("d01_crono_workshop", "D01", "3. Cronograma do processo — 3.1", "p. 2 (impressa: 1)",
  '"Workshop de apresentação do ambiente 22/10/2026"',
  "Prazo / marco", "Administrativo do processo",
  "Workshop com proponentes em 22/10/2026 (material fornecido como D03).",
  s=2, p=3, impacto="Fonte de dados de dimensionamento; a ausência reduz informação para a proposta.",
  rel=["d03_inv"], acao="Atender", resp="Bid Manager")

I("d01_crono_perguntas", "D01", "3. Cronograma do processo — 3.1", "p. 2 (impressa: 1)",
  '"Prazo final para envio de perguntas 05/11/2026"',
  "Prazo / marco", "Administrativo do processo",
  "Data-limite para o envio de esclarecimentos. As perguntas desta matriz devem ser enviadas até essa data; a rodada 1 já foi respondida em 12/11/2026 e a RFP não prevê nova rodada.",
  obrig="Mandatório", s=3, p=3,
  impacto="Perguntas não enviadas no prazo obrigam a precificar o pior cenário ou a registrar ressalvas.",
  acao="Atender",
  perg="Haverá nova rodada de esclarecimentos após a divulgação das respostas de 12/11/2026, considerando que algumas respostas geram novas dúvidas (por exemplo, volumetria EPS e número de usuários)?",
  resp="Bid Manager")

I("d01_crono_respostas", "D01", "3. Cronograma do processo — 3.1", "p. 2 (impressa: 1)",
  '"Divulgação das respostas 12/11/2026"',
  "Prazo / marco", "Administrativo do processo",
  "Divulgação das respostas em 12/11/2026, data que consta nas respostas da Rodada 1 (D04).",
  s=1, p=3, impacto="Janela entre respostas e entrega da proposta.", rel=["d04_inv"], resp="Bid Manager")

I("d01_crono_entrega", "D01", "3. Cronograma do processo — 3.1", "p. 2 (impressa: 1)",
  '"Entrega das propostas 20/11/2026, até as 18h"',
  "Prazo / marco", "Administrativo do processo",
  "Prazo original de entrega das propostas. Prorrogado para 27/11/2026, até as 18h, pela resposta 1 do Q&A.",
  obrig="Mandatório", s=5, p=3,
  impacto="Proposta fora do prazo não é considerada.",
  rel=["d04_q1"], vig="Alterado", acao="Atender", resp="Bid Manager")

I("d01_crono_inicio", "D01", "3. Cronograma do processo — 3.1", "p. 2 (impressa: 1)",
  '"Início previsto dos serviços 01/02/2027"',
  "Prazo / marco", "Transição/Implantação",
  "Início previsto da operação em 01/02/2027, dia seguinte ao fim do contrato do SIEM legado (31/01/2027, sem prorrogação — workshop). A RFP não informa a data prevista de assinatura do contrato, da qual depende a contagem do prazo de transição.",
  obrig="Mandatório", s=4, p=3,
  impacto="Data rígida de entrada em operação; atraso na assinatura comprime a transição.",
  rel=["d03_risco_transicao", "d03_siem_legado"], acao="Esclarecer no Q&A",
  perg="Qual a data prevista para assinatura do contrato? O início dos serviços em 01/02/2027 é a data de início da operação plena ou da transição?",
  resp="Delivery/Operação")

I("d01_transicao30", "D01", "3. Cronograma do processo — 3.2", "p. 2 (impressa: 1)",
  '"A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato."',
  "Prazo / marco", "Transição/Implantação",
  "Prazo de transição de 30 dias corridos contados da assinatura. Diverge do Anexo I, item 4.1 (60 dias). Ver contradição registrada.",
  obrig="Mandatório", s=4, p=3,
  impacto="Dobra a intensidade de equipe de transição em relação ao prazo de 60 dias; risco de multa se a operação não estiver completa.",
  fw="ITIL 4", ctrl="Gestão de transição/implantação de serviços (identificador a confirmar)", assoc="Correlata",
  rel=["d02_transicao60", "d02_contr_transicao", "d03_risco_transicao"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A", resp="Delivery/Operação")

I("d01_idioma", "D01", "4. Instruções para apresentação da proposta — 4.1", "p. 3 (impressa: 2)",
  '"A proposta deverá ser redigida em língua portuguesa"',
  "Instrução de resposta", "Administrativo do processo",
  "Idioma obrigatório: português. Não está claro se certificados e atestados em outro idioma exigem tradução juramentada.",
  obrig="Mandatório", s=2, p=3, impacto="Custo de tradução de documentos de habilitação, se emitidos em outro idioma.",
  acao="Atender",
  perg="Certificados e atestados emitidos em outro idioma precisam de tradução juramentada ou simples?",
  resp="Bid Manager")

I("d01_portal", "D01", "4. Instruções para apresentação da proposta — 4.1", "p. 3 (impressa: 2)",
  '"enviada exclusivamente pelo portal de fornecedores do Banco"',
  "Instrução de resposta", "Administrativo do processo",
  "Canal único de envio. A RFP não informa o endereço do portal, a necessidade de cadastro prévio nem limites de tamanho de arquivo.",
  obrig="Mandatório", s=4, p=3,
  impacto="Envio por outro canal ou falha de cadastro pode impedir o recebimento da proposta.",
  acao="Esclarecer no Q&A",
  perg="Qual o endereço do portal de fornecedores, há cadastro prévio obrigatório (e com que antecedência) e há limite de tamanho ou formato de arquivo?",
  resp="Bid Manager")

I("d01_40pag", "D01", "4. Instruções para apresentação da proposta — 4.2", "p. 3 (impressa: 2)",
  '"A proposta técnica deverá ter no máximo 40 (quarenta) páginas, excluídos os anexos."',
  "Instrução de resposta", "Administrativo do processo",
  "Limite de 40 páginas para a proposta técnica. A RFP não define a consequência do excesso (desconsideração das páginas excedentes ou desclassificação) nem o que pode ir como anexo.",
  obrig="Mandatório", s=3, p=3, impacto="Conteúdo que pontua (metodologia, equipe, transição) precisa caber em 40 páginas.",
  acao="Esclarecer no Q&A",
  perg="Qual a consequência de exceder 40 páginas? Currículos, certificados, cronogramas e o questionário técnico podem ser apresentados como anexos fora do limite?",
  resp="Bid Manager")

I("d01_anexoIV_instr", "D01", "4. Instruções para apresentação da proposta — 4.3", "p. 3 (impressa: 2)",
  '"A proposta comercial deverá ser apresentada conforme a planilha modelo do Anexo IV — Planilha de Preços."',
  "Instrução de resposta", "Comercial/Preço",
  "Formato obrigatório da proposta comercial vinculado ao Anexo IV, que não foi fornecido (ver Lacuna).",
  obrig="Mandatório", s=3, p=3, impacto="Sem o modelo, não há como estruturar o preço no formato exigido.",
  rel=["d01_anexoIV_lacuna"], acao="Atender", resp="Pricing/Financeiro")

I("d01_anexoIV_lacuna", "D01", "4. Instruções para apresentação da proposta — 4.3", "p. 3 (impressa: 2)",
  'Não localizado · "conforme a planilha modelo do Anexo IV — Planilha de Preços"',
  "Lacuna", "Comercial/Preço",
  "Documento citado pelo cliente e não fornecido no pacote (o usuário não o listou). Sem ele não se conhece a estrutura de preço exigida (por usuário, por EPS, preço fixo mensal, itens de transição etc.), o que também afeta o cálculo da multa sobre o \"valor mensal do contrato\".",
  obrig="Mandatório", s=4, p=3, nat="Explícita",
  impacto="Impede montar a proposta comercial no formato exigido e definir a estrutura de preço.",
  rel=["d01_anexoIV_instr", "d01_formula_preco"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Solicitamos o envio do Anexo IV — Planilha de Preços (modelo editável), citado no item 4.3 da RFP e não incluído no pacote de documentos.",
  resp="Pricing/Financeiro", pend="Lacuna: Anexo IV — Planilha de Preços citado e não fornecido")

I("d01_anexoII_lacuna", "D01", "Documento inteiro (numeração de anexos)", "p. 3 (impressa: 2) · p. 6 (impressa: 5) (OCR)",
  'Não localizado · "Anexo IV — Planilha de Preços" · "ANEXO III — DECLARAÇÃO DE LOCALIZAÇÃO DE DADOS"',
  "Lacuna", "Administrativo do processo",
  "Inferência: o pacote traz Anexo I (D02), Anexo III (p. 6 do PDF) e cita o Anexo IV, mas nenhum documento cita ou fornece um Anexo II. Pode ser um anexo omitido (por exemplo, minuta de contrato ou acordo de nível de serviço) ou apenas salto de numeração.",
  obrig="Informativo", s=2, p=3, nat="Inferida",
  impacto="Possível documento contratual não analisado.",
  rel=["d01_anexoIV_lacuna"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Existe um Anexo II desta RFP? Em caso positivo, solicitamos seu envio; em caso negativo, solicitamos confirmar que o pacote completo é composto pela RFP e pelos Anexos I, III e IV e pelo questionário técnico.",
  resp="Bid Manager", pend="Lacuna: Anexo II não citado e não fornecido (salto de numeração)")

I("d01_questionario", "D01", "4. Instruções para apresentação da proposta — 4.4", "p. 3 (impressa: 2)",
  '"O questionário técnico (planilha anexa) deverá ser integralmente preenchido."',
  "Instrução de resposta", "Administrativo do processo",
  "Obrigatoriedade de preencher todo o questionário técnico (fornecido em D04). A RFP não prevê sanção; a aba \"Instruções\" do próprio questionário acrescenta a desclassificação.",
  obrig="Mandatório", s=3, p=3, impacto="Questionário incompleto passa a ser causa de desclassificação (D04).",
  rel=["d04_instr_obrig"], acao="Atender", resp="Pré-venda/Arquitetura")

I("d01_hab_iso", "D01", "5. Critérios de habilitação — 5.1 a)", "p. 3 (impressa: 2)",
  '"Serão inabilitados os proponentes que não apresentarem: [...] certificado ISO/IEC 27001 vigente, emitido por organismo acreditado, cujo escopo inclua os serviços de SOC"',
  "Critério eliminatório / de habilitação", "Segurança da Informação/Cyber",
  "Certificado ISO/IEC 27001 vigente, de organismo acreditado, com escopo que inclua o SOC. Probabilidade 5: a própria cláusula estabelece inabilitação automática pela não apresentação. Não se define se vale certificado de empresa do mesmo grupo nem se o escopo deve incluir também IAM.",
  obrig="Mandatório", s=5, p=5,
  impacto="Inabilitação do proponente.",
  fw=ISO, ctrl="Certificação do SGSI — requisitos das cláusulas 4 a 10", assoc="Direta",
  rel=["d04_qt01"], acao="Atender",
  perg="O certificado ISO/IEC 27001 pode estar em nome de outra empresa do mesmo grupo econômico do proponente? O escopo deve incluir também os serviços de IAM ou apenas o SOC?",
  resp="Compliance")

I("d01_hab_atestados", "D01", "5. Critérios de habilitação — 5.1 b)", "p. 3 (impressa: 2)",
  '"no mínimo 3 (três) atestados de capacidade técnica de prestação de serviços de SOC para instituições financeiras, com ambiente de no mínimo 2.000 usuários"',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Três atestados de SOC para instituições financeiras, com ambiente mínimo de 2.000 usuários. Probabilidade 5: inabilitação expressa no caput do item 5.1. Não está claro se os 2.000 usuários valem para cada atestado ou para a soma, nem se o atestado precisa ser de contrato vigente.",
  obrig="Mandatório", s=5, p=5,
  impacto="Inabilitação do proponente.",
  fw=NA, assoc=NA, acao="Atender",
  perg="O mínimo de 2.000 usuários se aplica a cada um dos três atestados ou à soma deles? São aceitos atestados de contratos encerrados, de instituições financeiras estrangeiras ou de empresas do mesmo grupo do proponente?",
  resp="Bid Manager")

I("d01_hab_soc_nacional", "D01", "5. Critérios de habilitação — 5.1 c)", "p. 3 (impressa: 2)",
  '"comprovação de que o SOC está localizado em território nacional"',
  "Critério eliminatório / de habilitação", "Operação/Serviços / Regulatório/Compliance",
  "SOC fisicamente no Brasil, confirmado pela resposta 2 do Q&A. Probabilidade 5: inabilitação expressa no caput do item 5.1. A RFP não diz que documento comprova a localização.",
  obrig="Mandatório", s=5, p=5,
  impacto="Inabilitação do proponente.",
  fw=NA, assoc=NA, rel=["d04_q2"], acao="Atender",
  perg="Quais documentos são aceitos como comprovação da localização do SOC em território nacional (por exemplo, endereço, contrato de locação, declaração, visita técnica)?",
  resp="Delivery/Operação")

I("d01_equipe_cert", "D01", "5. Critérios de habilitação — 5.2", "p. 3 (impressa: 2)",
  '"O proponente deverá possuir equipe técnica devidamente certificada."',
  "Ambiguidade", "Pessoas/Equipe",
  "Item na seção de habilitação, mas fora da lista do 5.1 (que define as causas de inabilitação). Não informa quais certificações, para quais funções, quantos profissionais nem como comprovar. Pode ser lido como critério eliminatório (pela posição) ou como requisito de execução. A única certificação nominal está no Anexo I 5.1 (CISSP do coordenador); o questionário QT-06 repete o tema de forma genérica.",
  obrig="Mandatório", s=4, p=3,
  impacto="Se for eliminatório, há risco de inabilitação por critério subjetivo; se for de execução, há custo de certificação da equipe.",
  fw=ISO, ctrl="A.6.3 — Conscientização, educação e treinamento em segurança da informação", assoc="Correlata",
  rel=["d02_cissp", "d04_qt06"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O item 5.2 é critério de habilitação (sob pena de inabilitação)? Quais certificações são exigidas, para quais funções, em que quantidade mínima e com que documentos devem ser comprovadas na proposta?",
  resp="RH/Staffing")

I("d01_pesos_notas", "D01", "6. Critérios de avaliação — 6.1", "p. 4 (impressa: 3)",
  '"A nota final será composta pela Nota Técnica (peso de 60%) e pela Nota de Preço (peso de 40%)."',
  "Critério de avaliação / pontuação", "Comercial/Preço",
  "Avaliação técnica e preço, com predominância técnica (60/40).",
  s=3, p=3, impacto="Orienta a estratégia de preço: qualidade técnica pesa mais que preço.",
  fw="APMP Body of Knowledge", ctrl="Estratégia de proposta (identificador a confirmar)", assoc="Boa prática",
  rel=["d01_formula_preco"], acao="Precificar", resp="Pricing/Financeiro")

I("d01_formula_preco", "D01", "6. Critérios de avaliação — 6.1", "p. 4 (impressa: 3)",
  'Não localizado · "Nota de Preço (peso de 40%)"',
  "Lacuna", "Comercial/Preço",
  "A RFP não define a fórmula da Nota de Preço (proporcional ao menor preço, faixas etc.), nem o preço de referência (valor mensal, total de 36 meses ou valor presente).",
  obrig="Informativo", s=4, p=3,
  impacto="Impede simular o efeito de descontos na nota final e definir a estratégia de preço.",
  rel=["d01_pesos_notas", "d01_anexoIV_lacuna"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Qual a fórmula de cálculo da Nota de Preço e qual valor será comparado (mensal, total de 36 meses, incluindo ou não a transição)?",
  resp="Pricing/Financeiro")

for k, nome, pts in [("d01_crit_metodologia", "Metodologia de operação do SOC", "20"),
                     ("d01_crit_equipe", "Qualificação da equipe", "20"),
                     ("d01_crit_ferramentas", "Ferramentas e tecnologia", "15"),
                     ("d01_crit_transicao", "Plano de transição", "10")]:
    I(k, "D01", "6. Critérios de avaliação — 6.2", "p. 4 (impressa: 3)",
      f'"{nome} {pts}"',
      "Critério de avaliação / pontuação", "Gestão de Projetos" if "transição" in nome else "Segurança da Informação/Cyber",
      f"Critério técnico \"{nome}\", máximo de {pts} pontos. A RFP não traz subcritérios, rubrica nem forma de comprovação, o que torna a avaliação subjetiva.",
      obrig="Mandatório", s=3, p=3,
      impacto="Perda de pontuação técnica e risco de não atingir a nota mínima de 70%.",
      fw="APMP Body of Knowledge", ctrl="Estratégia de proposta (identificador a confirmar)", assoc="Boa prática",
      rel=["d01_contr_soma"], acao="Esclarecer no Q&A",
      perg=f"Quais subcritérios e evidências serão usados para atribuir os {pts} pontos do critério \"{nome}\"?",
      resp="Pré-venda/Arquitetura")

I("d01_contr_soma", "D01", "6. Critérios de avaliação — 6.2", "p. 4 (impressa: 3)",
  'A: "A Nota Técnica, de no máximo 60 (sessenta) pontos" · B: "Metodologia de operação do SOC 20" · "Qualificação da equipe 20" · "Ferramentas e tecnologia 15" · "Plano de transição 10"',
  "Contradição", "Administrativo do processo",
  "A soma dos critérios da tabela é 65 pontos (20 + 20 + 15 + 10), e não os 60 declarados. Isso altera a nota mínima do item 6.3 (70% de 60 = 42 pontos; 70% de 65 = 45,5 pontos) e o peso relativo de cada critério.",
  obrig="Informativo", s=4, p=3,
  impacto="Incerteza sobre a nota de corte e a normalização da Nota Técnica; risco de desclassificação por regra mal definida.",
  rel=["d01_crit_metodologia", "d01_crit_equipe", "d01_crit_ferramentas", "d01_crit_transicao", "d01_corte70", "d04_contr_pesos"],
  vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A tabela do item 6.2 soma 65 pontos, mas a Nota Técnica tem máximo de 60. Qual a pontuação correta de cada critério e qual a nota mínima, em pontos, para o item 6.3?",
  resp="Bid Manager")

I("d01_corte70", "D01", "6. Critérios de avaliação — 6.3", "p. 4 (impressa: 3)",
  '"Serão desclassificadas as propostas com Nota Técnica inferior a 70% (setenta por cento) da pontuação máxima."',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Nota técnica mínima eliminatória. A base de cálculo é incerta (60 ou 65 pontos) e a avaliação é subjetiva. A penalidade oculta do questionário (–2 pontos por requisito não obrigatório \"Não atende\") pode empurrar a nota para baixo do corte.",
  obrig="Mandatório", s=5, p=3,
  impacto="Desclassificação da proposta.",
  rel=["d01_contr_soma", "d04_pesos_regra"], acao="Atender", resp="Pré-venda/Arquitetura")

I("d01_empate", "D01", "6. Critérios de avaliação — 6.4", "p. 4 (impressa: 3)",
  '"Em caso de empate na nota final, prevalecerá a proposta de menor preço."',
  "Critério de avaliação / pontuação", "Comercial/Preço",
  "Critério de desempate pelo menor preço.",
  s=2, p=3, impacto="Relevância marginal do preço no desempate.", resp="Pricing/Financeiro")

I("d01_vigencia", "D01", "7. Condições comerciais e contratuais — 7.1", "p. 5 (impressa: 4)",
  '"O contrato terá vigência de 36 (trinta e seis) meses, prorrogável por iguais períodos mediante acordo entre as partes."',
  "Obrigação contratual", "Jurídico/Contratual",
  "Prazo contratual de 36 meses, prorrogável por acordo. Base para amortizar os custos de transição e o licenciamento do SIEM.",
  obrig="Mandatório", s=2, p=3, impacto="Horizonte de amortização dos investimentos.",
  fw=CC, ctrl="Contratos em geral (identificador a confirmar)", assoc="Correlata",
  acao="Precificar", resp="Pricing/Financeiro")

I("d01_reajuste", "D01", "7. Condições comerciais e contratuais — 7.2", "p. 5 (impressa: 4)",
  '"Os preços serão reajustados anualmente pela variação do IPCA."',
  "Obrigação contratual", "Financeiro",
  "Reajuste anual pelo IPCA, sem data-base definida (data da proposta ou da assinatura). Licenças em moeda estrangeira (SIEM em nuvem) não são protegidas pelo IPCA.",
  obrig="Mandatório", s=3, p=3, impacto="Risco cambial e inflacionário sobre custos de licenças e de nuvem.",
  fw=CC, ctrl="Contratos em geral (identificador a confirmar)", assoc="Correlata",
  acao="Esclarecer no Q&A",
  perg="Qual a data-base do reajuste pelo IPCA (data da proposta ou da assinatura do contrato)?",
  resp="Pricing/Financeiro")

I("d01_pagamento", "D01", "7. Condições comerciais e contratuais — 7.3", "p. 5 (impressa: 4)",
  '"O pagamento será efetuado em até 60 (sessenta) dias após o aceite da nota fiscal."',
  "Obrigação contratual", "Financeiro",
  "Pagamento em até 60 dias após o aceite da nota fiscal. O prazo para o aceite não é definido, o que pode alongar o ciclo de recebimento.",
  obrig="Mandatório", s=3, p=3, impacto="Custo financeiro de capital de giro a incluir no preço.",
  fw=CC, ctrl="Contratos em geral (identificador a confirmar)", assoc="Correlata",
  acao="Esclarecer no Q&A",
  perg="Qual o prazo máximo para o aceite da nota fiscal pelo Banco, contado da sua emissão?",
  resp="Pricing/Financeiro")

I("d01_multa", "D01", "7. Condições comerciais e contratuais — 7.4", "p. 5 (impressa: 4)",
  '"O descumprimento de qualquer nível de serviço (SLA) previsto no Anexo I sujeitará a Contratada a multa de 10% (dez por cento) do valor mensal do contrato, por ocorrência."',
  "Penalidade / multa / glosa", "Jurídico/Contratual / Financeiro",
  "Multa de 10% do valor mensal do contrato inteiro por ocorrência, para qualquer SLA, sem teto mensal ou global, sem graduação por gravidade e sem período de carência na transição. Dez ocorrências no mês consomem todo o faturamento. Probabilidade 4: a multa incide automaticamente \"por ocorrência\", e o SLA de 15 minutos (Anexo I 2.1) é medido por incidente, o que torna múltiplas ocorrências no mês plausíveis. A resposta 4 do Q&A manteve o item 7 inalterado.",
  obrig="Mandatório", s=5, p=4,
  impacto="Exposição financeira sem limite, superior ao faturamento mensal; afeta a viabilidade do contrato.",
  fw=CC, ctrl="Art. 412 — limite da cláusula penal ao valor da obrigação principal", assoc="Correlata",
  rel=["d02_sla_15", "d02_sla_999", "d02_sla_escopo", "d04_q4"], acao="Propor exceção/ressalva",
  perg="Será admitido teto para as multas (por exemplo, limite mensal sobre o valor da fatura e limite global anual), graduação conforme o SLA descumprido e carência durante a transição?",
  resp="Jurídico")

I("d01_resp_ilimitada", "D01", "7. Condições comerciais e contratuais — 7.5", "p. 5 (impressa: 4)",
  '"A Contratada responderá de forma integral e ilimitada por quaisquer danos decorrentes de incidentes de segurança ocorridos no ambiente do Contratante."',
  "Obrigação contratual", "Jurídico/Contratual",
  "Responsabilidade integral e ilimitada por quaisquer danos de incidentes de segurança no ambiente do Contratante, sem vínculo com culpa ou falha da Contratada e sem exclusão de lucros cessantes ou danos indiretos. Num banco, um incidente relevante pode gerar dano de grande magnitude. Probabilidade 3: depende da ocorrência de incidente e da atribuição de responsabilidade.",
  obrig="Mandatório", s=5, p=3,
  impacto="Exposição jurídica e financeira ilimitada; pode tornar o risco inaceitável ou não segurável.",
  fw=CC, ctrl="Art. 944 — a indenização mede-se pela extensão do dano", assoc="Correlata",
  rel=["d01_seguro", "d04_q4"], acao="Propor exceção/ressalva",
  perg="O Banco aceita limitar a responsabilidade da Contratada a um múltiplo do valor anual do contrato, restrita a danos diretos comprovadamente causados por culpa ou dolo da Contratada?",
  resp="Jurídico")

I("d01_seguro", "D01", "7. Condições comerciais e contratuais — 7.6", "p. 5 (impressa: 4)",
  '"A Contratada deverá manter seguro de responsabilidade civil cibernética em valor compatível com os riscos do contrato."',
  "Ambiguidade", "Jurídico/Contratual / Financeiro",
  "Seguro cibernético obrigatório, mas \"valor compatível\" não é quantificado. Com responsabilidade ilimitada (7.5), nenhum valor de apólice cobre integralmente o risco, e o Banco pode questionar o valor contratado a qualquer momento.",
  obrig="Mandatório", s=3, p=3, impacto="Custo de apólice indefinido no preço.",
  fw=NA, assoc=NA, rel=["d01_resp_ilimitada"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Qual o valor mínimo de cobertura do seguro de responsabilidade civil cibernética, e a apólice deve ser apresentada na proposta ou na assinatura do contrato?",
  resp="Jurídico")

I("d01_subcontr", "D01", "7. Condições comerciais e contratuais — 7.7", "p. 5 (impressa: 4)",
  '"É vedada a subcontratação, total ou parcial, do objeto deste contrato."',
  "Obrigação contratual", "Jurídico/Contratual",
  "Vedação total de subcontratação. Conflita, potencialmente, com o SIEM em nuvem pública de terceiros (Anexo I 1.2), com serviços de threat intelligence (QT-05) e com equipes de parceiros ou fabricantes.",
  obrig="Mandatório", s=4, p=3,
  impacto="Pode impedir o uso de SaaS, parceiros e fornecedores especializados, ou expor o proponente a descumprimento contratual.",
  fw=ISO, ctrl="A.5.19 — Segurança da informação nas relações com fornecedores", assoc="Correlata",
  rel=["d02_ambig_subcontr", "d04_qt05"], acao="Esclarecer no Q&A", resp="Jurídico")

I("d01_confid", "D01", "7. Condições comerciais e contratuais — 7.8", "p. 5 (impressa: 4)",
  '"As obrigações de confidencialidade vigorarão por 5 (cinco) anos após o término do contrato."',
  "Obrigação contratual", "Jurídico/Contratual",
  "Confidencialidade de 5 anos após o término do contrato.",
  obrig="Mandatório", s=2, p=3, impacto="Obrigação pós-contratual de baixo custo.",
  fw=ISO, ctrl="A.6.6 — Acordos de confidencialidade ou de não divulgação", assoc="Direta",
  acao="Atender", resp="Jurídico")

I("d01_anexoIII_decl", "D01", "Anexo III — Declaração de Localização de Dados", "p. 6 (impressa: 5) (OCR)",
  '"Esta declaração deverá ser entregue assinada pelo representante legal do proponente junto com a proposta, sob pena de inabilitação."',
  "Critério eliminatório / de habilitação", "Administrativo do processo / Regulatório/Compliance",
  "Declaração assinada pelo representante legal, entregue com a proposta. Probabilidade 5: o texto prevê inabilitação expressa. O critério está apenas na página digitalizada e não consta da lista do item 5.1 nem é citado no corpo da RFP, o que facilita deixá-lo passar.",
  obrig="Mandatório", s=5, p=5,
  impacto="Inabilitação do proponente.",
  fw=NA, assoc=NA, rel=["d01_anexoIII_dados"], acao="Atender", resp="Jurídico")

I("d01_anexoIII_dados", "D01", "Anexo III — Declaração de Localização de Dados", "p. 6 (impressa: 5) (OCR)",
  '"todos os dados do Banco Horizonte Fictício S.A., incluindo os registros (logs) de segurança, serão armazenados e processados exclusivamente em território nacional, durante toda a vigência do contrato"',
  "Restrição", "Regulatório/Compliance / Infraestrutura/Cloud",
  "Restrição de residência de dados: todos os dados, inclusive logs, armazenados e processados exclusivamente no Brasil durante a vigência. Afeta a escolha do SIEM/SaaS, de backup e de ferramentas de análise ou threat intelligence que processem dados fora do país. Conflita com o Anexo I 1.2 (nuvem em região de livre escolha).",
  obrig="Mandatório", s=4, p=3,
  impacto="Restringe fornecedores de SIEM e de nuvem a regiões no Brasil, normalmente com custo maior.",
  fw=CMN, ctrl="Local de processamento e armazenamento de dados (identificador a confirmar)", assoc="Correlata",
  rel=["d02_contr_nuvem", "d01_anexoIII_decl"], acao="Atender", resp="Pré-venda/Arquitetura")

# =============================================================== D02 — Anexo I (Word)
I("d02_inv", "D02", "Documento inteiro (§ 1 a § 6)", "§ 1. Serviços de SOC a § 6. Responsabilidades do Contratante",
  '"RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Versão 1.0 — 15/10/2026"',
  "Registro de cobertura", "Administrativo do processo",
  "Inventário: Word com 22 parágrafos em 6 seções numeradas, sem tabelas; não há marcas de revisão nem comentários sinalizados na extração. Integralmente analisado. Localizador por seção e item (Word não tem paginação fixa).",
  fw="—", assoc="—", resp="Bid Manager")

I("d02_monit", "D02", "1. Serviços de SOC — 1.1", "§ 1. Serviços de SOC, item 1.1",
  '"O proponente deverá prestar serviço de monitoramento contínuo de eventos de segurança, em regime 24x7x365."',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber / Operação/Serviços",
  "Monitoramento contínuo 24x7x365, repetindo o objeto da RFP 2.1.",
  obrig="Mandatório", s=3, p=3, impacto="Escala de turnos 24x7.",
  fw=ISO, ctrl="A.8.16 — Atividades de monitoramento", assoc="Direta",
  rel=["d01_objeto_soc"], vig="Duplicado", acao="Precificar", resp="Delivery/Operação")

I("d02_siem", "D02", "1. Serviços de SOC — 1.2", "§ 1. Serviços de SOC, item 1.2",
  '"O proponente deverá fornecer a solução de SIEM"',
  "Requisito funcional / de serviço", "Técnico/Arquitetura / Segurança da Informação/Cyber",
  "O proponente fornece a plataforma SIEM (licença, infraestrutura e operação). O custo depende de volumetria (EPS/GB por dia), que o Banco se recusou a informar (Q&A 3).",
  obrig="Mandatório", s=4, p=3,
  impacto="Maior componente de custo variável da proposta, sem base de dimensionamento.",
  fw=ISO, ctrl="A.8.15 — Registro de logs", assoc="Correlata",
  rel=["d02_eps_lacuna", "d04_q3"], acao="Precificar", resp="Pré-venda/Arquitetura")

I("d02_siem_nuvem", "D02", "1. Serviços de SOC — 1.2", "§ 1. Serviços de SOC, item 1.2",
  '"podendo esta ser disponibilizada em nuvem pública, em região de livre escolha do proponente"',
  "Requisito funcional / de serviço", "Infraestrutura/Cloud",
  "Permite o SIEM em nuvem pública em qualquer região. Ver a contradição com o Anexo III (dados exclusivamente no Brasil) e a ambiguidade com a vedação de subcontratação.",
  obrig="Desejável", s=3, p=3, impacto="Flexibilidade de arquitetura que pode ser anulada pelo Anexo III.",
  fw=ISO, ctrl="A.5.23 — Segurança da informação para uso de serviços em nuvem", assoc="Direta",
  rel=["d02_contr_nuvem", "d02_ambig_subcontr"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  resp="Pré-venda/Arquitetura")

I("d02_contr_nuvem", "D02", "Anexo I 1.2 × RFP Anexo III", "A: § 1. Serviços de SOC, item 1.2 · B: D01 p. 6 (impressa: 5) (OCR)",
  'A: "podendo esta ser disponibilizada em nuvem pública, em região de livre escolha do proponente" · B: "serão armazenados e processados exclusivamente em território nacional"',
  "Contradição", "Infraestrutura/Cloud / Regulatório/Compliance",
  "O Anexo I permite o SIEM em nuvem pública em região de livre escolha; o Anexo III exige declaração, sob pena de inabilitação, de que todos os dados, inclusive logs, ficam exclusivamente no Brasil. Uma arquitetura em região estrangeira, admitida pelo Anexo I, tornaria a declaração falsa.",
  obrig="Mandatório", s=4, p=3,
  impacto="Escolha errada de arquitetura gera inabilitação ou descumprimento contratual; região nacional tende a ter custo maior.",
  fw=CMN, ctrl="Contratação de serviços de nuvem e local dos dados (identificador a confirmar)", assoc="Correlata",
  rel=["d02_siem_nuvem", "d01_anexoIII_dados", "d01_precedencia", "d01_cmn"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="O Anexo I, item 1.2, admite SIEM em nuvem pública em região de livre escolha, mas o Anexo III exige que todos os dados, inclusive logs, sejam armazenados e processados exclusivamente em território nacional. Confirmam que a nuvem deve estar em região localizada no Brasil, inclusive para backup, réplicas e processamento analítico?",
  resp="Pré-venda/Arquitetura")

I("d02_ambig_subcontr", "D02", "Anexo I 1.2 × RFP 7.7", "A: § 1. Serviços de SOC, item 1.2 · B: D01 p. 5 (impressa: 4), item 7.7",
  'A: "podendo esta ser disponibilizada em nuvem pública" · B: "É vedada a subcontratação, total ou parcial, do objeto deste contrato."',
  "Ambiguidade", "Jurídico/Contratual / Infraestrutura/Cloud",
  "Não está claro se a contratação de provedor de nuvem pública, SIEM em SaaS, feeds de threat intelligence ou suporte de fabricante configura subcontratação vedada pelo item 7.7.",
  obrig="Mandatório", s=4, p=3,
  impacto="Se for considerada subcontratação, a arquitetura em nuvem e o uso de parceiros ficam proibidos, com risco de descumprimento contratual.",
  fw=ISO, ctrl="A.5.21 — Gestão da segurança da informação na cadeia de suprimentos de TIC", assoc="Correlata",
  rel=["d01_subcontr", "d02_siem_nuvem", "d04_qt05"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A contratação, pela Contratada, de provedores de nuvem pública, de SIEM em modelo SaaS, de feeds de threat intelligence e de suporte de fabricantes configura subcontratação vedada pelo item 7.7?",
  resp="Jurídico")

I("d02_ret12", "D02", "1. Serviços de SOC — 1.3", "§ 1. Serviços de SOC, item 1.3",
  '"Os registros (logs) de segurança deverão ser retidos por no mínimo 12 (doze) meses."',
  "Requisito não funcional", "Segurança da Informação/Cyber",
  "Retenção mínima de 12 meses (o QT-03 especifica \"online\"). Ver a ambiguidade com o item 1.6 (5 anos).",
  obrig="Mandatório", s=3, p=3, impacto="Armazenamento proporcional à volumetria, que não foi informada.",
  fw=ISO, ctrl="A.8.15 — Registro de logs", assoc="Direta",
  rel=["d02_ret5", "d02_ambig_ret", "d04_qt03"], acao="Precificar", resp="Pré-venda/Arquitetura")

I("d02_integr", "D02", "1. Serviços de SOC — 1.4", "§ 1. Serviços de SOC, item 1.4",
  '"O SIEM deverá ser integrado a todos os ativos relevantes do Contratante."',
  "Ambiguidade", "Técnico/Arquitetura",
  "\"Ativos relevantes\" não está definido (quais tipos, quantidades, aplicações, workloads nas duas nuvens públicas, subsidiárias). O escopo de integração fica aberto, e o Banco pode ampliá-lo durante o contrato sem contrapartida.",
  obrig="Mandatório", s=4, p=3,
  impacto="Esforço de onboarding e volumetria de logs indeterminados; risco de escopo aberto.",
  fw=ISO, ctrl="A.8.16 — Atividades de monitoramento", assoc="Correlata",
  rel=["d02_eps_lacuna", "d03_servidores", "d03_nuvens", "d03_subsid"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="Quais são os \"ativos relevantes\" a integrar ao SIEM (tipos e quantidades de servidores, dispositivos de rede, aplicações, bancos de dados e serviços nas nuvens públicas) e eles incluem os ambientes das subsidiárias?",
  resp="Pré-venda/Arquitetura")

I("d02_eps_lacuna", "D02", "1. Serviços de SOC — 1.2 a 1.4", "§ 1. Serviços de SOC, itens 1.2 a 1.4",
  'Não localizado · "O SIEM deverá ser integrado a todos os ativos relevantes do Contratante."',
  "Lacuna", "Técnico/Arquitetura / Comercial/Preço",
  "Não há volumetria de eventos (EPS), GB por dia ou número de fontes de log, dados indispensáveis para licenciar e dimensionar o SIEM, o armazenamento de 12 meses e 5 anos e a equipe. O pedido foi feito no Q&A 3 e recusado (ver D04).",
  obrig="Informativo", s=4, p=3,
  impacto="Impede precificar SIEM e armazenamento com segurança.",
  rel=["d04_q3", "d02_siem", "d02_integr"], vig="Alterado", acao="Esclarecer no Q&A",
  resp="Pré-venda/Arquitetura")

I("d02_ir", "D02", "1. Serviços de SOC — 1.5", "§ 1. Serviços de SOC, item 1.5",
  '"O serviço deverá contemplar resposta a incidentes, incluindo contenção, erradicação"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Resposta a incidentes com contenção e erradicação. Não define se a atuação é remota ou presencial, nem limite de horas ou de incidentes, nem se inclui forense. Combinada com a responsabilidade ilimitada (7.5), amplia a exposição.",
  obrig="Mandatório", s=3, p=3, impacto="Esforço variável não limitado; risco de atuação presencial não precificada.",
  fw=ISO, ctrl="A.5.26 — Resposta a incidentes de segurança da informação", assoc="Direta",
  rel=["d01_resp_ilimitada"], acao="Esclarecer no Q&A",
  perg="A resposta a incidentes (contenção e erradicação) é remota ou presencial? Há limite de horas ou de incidentes incluído no preço mensal e ela abrange análise forense?",
  resp="Segurança/Cyber")

I("d02_relatorio_pos", "D02", "1. Serviços de SOC — 1.5", "§ 1. Serviços de SOC, item 1.5",
  '"elaboração de relatório pós-incidente"',
  "Entregável", "Segurança da Informação/Cyber",
  "Relatório pós-incidente por incidente; prazo e formato não definidos.",
  obrig="Mandatório", s=2, p=3, impacto="Esforço documental por incidente.",
  fw=ISO, ctrl="A.5.27 — Aprendizado com incidentes de segurança da informação", assoc="Direta",
  acao="Atender", resp="Segurança/Cyber")

I("d02_ret5", "D02", "1. Serviços de SOC — 1.6", "§ 1. Serviços de SOC, item 1.6",
  '"Para fins de auditoria, os logs deverão ser mantidos por 5 (cinco) anos."',
  "Requisito não funcional", "Segurança da Informação/Cyber / Regulatório/Compliance",
  "Guarda de logs por 5 anos para auditoria. Não define se online ou em arquivo, nem o que ocorre com os logs ao término do contrato de 36 meses (devolução ou guarda após o fim).",
  obrig="Mandatório", s=4, p=3, impacto="Armazenamento de 5 anos multiplica o custo de storage, sem volumetria conhecida.",
  fw=ISO, ctrl="A.8.15 — Registro de logs", assoc="Direta",
  rel=["d02_ret12", "d02_ambig_ret"], acao="Precificar", resp="Pré-venda/Arquitetura")

I("d02_ambig_ret", "D02", "1. Serviços de SOC — 1.3 × 1.6", "§ 1. Serviços de SOC, itens 1.3 e 1.6",
  'A: "Os registros (logs) de segurança deverão ser retidos por no mínimo 12 (doze) meses." · B: "Para fins de auditoria, os logs deverão ser mantidos por 5 (cinco) anos."',
  "Ambiguidade", "Segurança da Informação/Cyber",
  "Dois prazos de retenção para os mesmos logs. Uma leitura é 12 meses online e 5 anos em arquivo (sugerida pelo QT-03, \"online por no mínimo 12 meses\"); a outra é 5 anos online. Também não se sabe se os 5 anos ultrapassam o contrato de 36 meses.",
  obrig="Mandatório", s=4, p=3,
  impacto="Diferença de custo relevante entre armazenamento quente por 5 anos e arquivo frio; guarda após o fim do contrato.",
  fw=ISO, ctrl="A.8.15 — Registro de logs", assoc="Direta",
  rel=["d02_ret12", "d02_ret5", "d04_qt03", "d03_migracao"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Confirmam que os logs devem ficar disponíveis online (pesquisáveis no SIEM) por 12 meses e arquivados até completar 5 anos? Ao término do contrato, os logs arquivados devem ser devolvidos ao Banco ou mantidos pela Contratada até completar 5 anos?",
  resp="Pré-venda/Arquitetura")

I("d02_lgpd", "D02", "1. Serviços de SOC — 1.3 e 1.6 · 3. IAM — 3.1", "§ 1. Serviços de SOC, itens 1.3 e 1.6 · § 3. IAM, item 3.1",
  '"Os registros (logs) de segurança deverão ser retidos" · "Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"',
  "Requisito implícito", "Privacidade/Proteção de Dados",
  "Inferência: logs de segurança e dados de identidade (admissão, movimentação, desligamento) contêm dados pessoais de colaboradores e, possivelmente, de clientes. A Contratada atuará como operadora, com dever de seguir as instruções do controlador, adotar medidas de segurança e comunicar incidentes. A RFP não traz acordo de tratamento de dados.",
  obrig="Mandatório", s=3, p=3, nat="Inferida",
  impacto="Obrigações de operador de dados pessoais (contrato de tratamento, registros, suporte ao encarregado, incidentes) não precificadas.",
  fw=LGPD, ctrl="Art. 39 — obrigações do operador", assoc="Direta",
  rel=["d01_anexoIII_dados"], acao="Registrar premissa na proposta",
  perg="O Banco firmará acordo de tratamento de dados pessoais com a Contratada como operadora? Os logs a serem coletados incluem dados pessoais de clientes ou apenas de colaboradores?",
  resp="Compliance")

I("d02_sla_15", "D02", "2. Níveis de serviço (SLA) — 2.1", "§ 2. Níveis de serviço (SLA), item 2.1",
  '"Tempo máximo para início do tratamento de incidentes críticos: 15 (quinze) minutos."',
  "SLA / KPI", "Operação/Serviços",
  "SLA de 15 minutos para início do tratamento de incidentes críticos. Não define o marco inicial (geração do alerta, abertura do chamado, notificação), o que é \"início do tratamento\", nem quem classifica o incidente como crítico (depende da matriz do Contratante, não fornecida). Cada falha sujeita a multa de 10% (RFP 7.4).",
  obrig="Mandatório", s=4, p=3,
  impacto="Exige equipe 24x7 com capacidade de resposta imediata; cada descumprimento gera multa relevante.",
  fw="ITIL 4", ctrl="Gestão de nível de serviço (identificador a confirmar)", assoc="Direta",
  rel=["d01_multa", "d02_matriz_lacuna"], acao="Esclarecer no Q&A",
  perg="Qual o marco inicial e o evento que caracteriza o \"início do tratamento\" no SLA de 15 minutos? A medição é individual por incidente ou percentual mensal?",
  resp="Delivery/Operação")

I("d02_sla_999", "D02", "2. Níveis de serviço (SLA) — 2.2", "§ 2. Níveis de serviço (SLA), item 2.2",
  '"Disponibilidade mínima mensal da plataforma SIEM: 99,9%."',
  "SLA / KPI", "Infraestrutura/Cloud",
  "Disponibilidade mensal de 99,9% (cerca de 43 minutos de indisponibilidade por mês). Não define se janelas de manutenção programada e falhas do provedor de nuvem são excluídas.",
  obrig="Mandatório", s=3, p=3, impacto="Exige arquitetura com alta disponibilidade.",
  fw="ITIL 4", ctrl="Gestão de disponibilidade (identificador a confirmar)", assoc="Direta",
  rel=["d01_multa"], acao="Esclarecer no Q&A",
  perg="As janelas de manutenção programada previamente acordadas e as indisponibilidades do provedor de nuvem são excluídas do cálculo dos 99,9%?",
  resp="Pré-venda/Arquitetura")

I("d02_relatorio", "D02", "2. Níveis de serviço (SLA) — 2.3", "§ 2. Níveis de serviço (SLA), item 2.3",
  '"Relatório mensal de indicadores, a ser entregue até o 5º dia útil do mês subsequente."',
  "Entregável", "Operação/Serviços",
  "Relatório mensal até o 5º dia útil. Por estar na seção de SLA, o atraso pode ser tratado como descumprimento de SLA sujeito à multa de 10% (7.4).",
  obrig="Mandatório", s=3, p=3, impacto="Atraso documental pode gerar multa desproporcional.",
  fw="ITIL 4", ctrl="Gestão de nível de serviço (identificador a confirmar)", assoc="Correlata",
  rel=["d02_sla_escopo"], acao="Atender", resp="Delivery/Operação")

I("d02_matriz_lacuna", "D02", "2. Níveis de serviço (SLA) — 2.4", "§ 2. Níveis de serviço (SLA), item 2.4",
  'Não localizado · "A classificação de criticidade dos incidentes seguirá a matriz de classificação do Contratante."',
  "Lacuna", "Operação/Serviços",
  "A matriz de classificação do Contratante é citada e não foi fornecida. Sem ela não se sabe quantos incidentes serão \"críticos\" e, portanto, sujeitos ao SLA de 15 minutos e à multa.",
  obrig="Mandatório", s=4, p=3,
  impacto="Impede dimensionar a equipe de resposta e o risco de multas.",
  rel=["d02_sla_15"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Solicitamos o envio da matriz de classificação de criticidade de incidentes do Contratante citada no item 2.4 do Anexo I, com o histórico médio mensal de incidentes por criticidade.",
  resp="Segurança/Cyber", pend="Lacuna: matriz de classificação de criticidade do Contratante citada e não fornecida")

I("d02_sla_escopo", "D02", "Anexo I, seções 1 a 3 × RFP 7.4", "§ 1 a § 3 · D01 p. 5 (impressa: 4), item 7.4",
  'A: "O descumprimento de qualquer nível de serviço (SLA) previsto no Anexo I" · B: "com revogação dos acessos de colaboradores desligados em até 24 (vinte e quatro) horas"',
  "Ambiguidade", "Jurídico/Contratual / Operação/Serviços",
  "A multa do 7.4 vale para \"qualquer nível de serviço (SLA) previsto no Anexo I\", mas o Anexo I tem prazos e metas fora da seção 2 (revogação em 24 h, recertificação trimestral, MFA em 100%, retenção, relatório pós-incidente). Não se sabe quais deles são SLA para fins de multa.",
  obrig="Mandatório", s=4, p=3,
  impacto="Amplia a base de incidência da multa de 10% por ocorrência.",
  fw="ITIL 4", ctrl="Gestão de nível de serviço (identificador a confirmar)", assoc="Correlata",
  rel=["d01_multa", "d02_iam_24h", "d02_relatorio"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Quais itens do Anexo I são considerados SLA para a aplicação da multa do item 7.4 da RFP: apenas os itens 2.1 a 2.3 ou também os prazos e metas das seções 1 e 3 (por exemplo, revogação de acessos em 24 horas)?",
  resp="Jurídico")

I("d02_iam_ciclo", "D02", "3. Gestão de identidades e acessos (IAM) — 3.1", "§ 3. IAM, item 3.1",
  '"Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Gestão do ciclo de vida de identidades (joiner/mover/leaver). Depende de integração com a fonte de RH do Banco, não descrita.",
  obrig="Mandatório", s=3, p=3, impacto="Esforço de integração com RH e sistemas-alvo.",
  fw=ISO, ctrl="A.5.16 — Gestão de identidade", assoc="Direta",
  rel=["d02_iam_lacuna"], acao="Precificar", resp="Segurança/Cyber")

I("d02_iam_24h", "D02", "3. Gestão de identidades e acessos (IAM) — 3.1", "§ 3. IAM, item 3.1",
  '"com revogação dos acessos de colaboradores desligados em até 24 (vinte e quatro) horas"',
  "SLA / KPI", "Segurança da Informação/Cyber",
  "Revogação em até 24 h após o desligamento. O marco inicial (data do desligamento ou comunicação do RH ao proponente) não é definido; o cumprimento depende de o Banco informar o desligamento a tempo.",
  obrig="Mandatório", s=3, p=3, impacto="Possível multa por atraso causado por comunicação tardia do Banco.",
  fw=ISO, ctrl="A.5.18 — Direitos de acesso", assoc="Direta",
  rel=["d02_sla_escopo"], acao="Esclarecer no Q&A",
  perg="O prazo de 24 horas para revogação é contado a partir de qual evento (desligamento efetivo ou recebimento da comunicação do RH pela Contratada) e por qual canal o RH comunicará os desligamentos?",
  resp="Segurança/Cyber")

I("d02_mfa", "D02", "3. Gestão de identidades e acessos (IAM) — 3.2", "§ 3. IAM, item 3.2",
  '"Autenticação multifator (MFA) obrigatória para 100% dos usuários com acesso privilegiado."',
  "Requisito não funcional", "Segurança da Informação/Cyber",
  "MFA para 100% dos privilegiados. Não diz quem fornece a solução e as licenças de MFA nem quantos usuários privilegiados existem.",
  obrig="Mandatório", s=3, p=3, impacto="Possível custo de licenças de MFA não dimensionado.",
  fw=ISO, ctrl="A.8.5 — Autenticação segura", assoc="Direta",
  rel=["d02_iam_lacuna"], acao="Esclarecer no Q&A",
  perg="Quantos usuários com acesso privilegiado existem e quem fornece a solução e as licenças de MFA (Banco ou Contratada)?",
  resp="Segurança/Cyber")

I("d02_recert", "D02", "3. Gestão de identidades e acessos (IAM) — 3.3", "§ 3. IAM, item 3.3",
  '"Revisão (recertificação) trimestral dos acessos concedidos."',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Campanha trimestral de recertificação. Não define o universo de sistemas nem o papel do proponente (condução da campanha ou também decisão sobre os acessos).",
  obrig="Mandatório", s=3, p=3, impacto="Esforço recorrente proporcional ao número de sistemas e usuários.",
  fw=ISO, ctrl="A.5.18 — Direitos de acesso", assoc="Direta",
  rel=["d02_iam_lacuna"], acao="Precificar", resp="Segurança/Cyber")

I("d02_pam", "D02", "3. Gestão de identidades e acessos (IAM) — 3.4", "§ 3. IAM, item 3.4",
  '"É desejável que a solução contemple cofre de senhas para contas privilegiadas (PAM)."',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "PAM desejável. Não há critério de pontuação explícito para itens desejáveis do Anexo I (6.2), e o workshop informa que hoje não existe PAM.",
  obrig="Desejável", s=2, p=3, impacto="Custo adicional opcional; possível diferencial.",
  fw=ISO, ctrl="A.8.2 — Direitos de acesso privilegiados", assoc="Direta",
  rel=["d03_sem_pam"], acao="Esclarecer no Q&A",
  perg="A oferta de solução de PAM (item 3.4 do Anexo I) será pontuada? Em qual critério do item 6.2 da RFP?",
  resp="Pré-venda/Arquitetura")

I("d02_iam_lacuna", "D02", "3. Gestão de identidades e acessos (IAM)", "§ 3. IAM, itens 3.1 a 3.4",
  'Não localizado · "Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"',
  "Lacuna", "Segurança da Informação/Cyber / Comercial/Preço",
  "A seção de IAM não informa se o proponente deve fornecer plataforma de IAM/IGA ou operar a existente (AD + scripts internos, segundo o workshop), quais e quantos sistemas-alvo integrar, nem a volumetria de admissões, movimentações e desligamentos.",
  obrig="Informativo", s=4, p=3,
  impacto="A diferença entre operar o AD existente e implantar uma plataforma IGA altera muito o preço e o prazo.",
  rel=["d01_objeto_iam", "d02_iam_ciclo", "d03_iam_atual"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O proponente deve fornecer e implantar plataforma de IAM/IGA ou operar as ferramentas atuais do Banco? Quantos sistemas-alvo devem ser integrados e qual a média mensal de admissões, movimentações e desligamentos?",
  resp="Pré-venda/Arquitetura")

I("d02_transicao60", "D02", "4. Transição — 4.1", "§ 4. Transição, item 4.1",
  '"A transição dos serviços deverá ser concluída em até 60 (sessenta) dias corridos a partir da assinatura do contrato."',
  "Prazo / marco", "Transição/Implantação",
  "Prazo de transição de 60 dias corridos. Diverge da RFP 3.2 (30 dias).",
  obrig="Mandatório", s=4, p=3, impacto="Base do plano de transição e do custo de operação em paralelo.",
  fw="ITIL 4", ctrl="Gestão de transição/implantação de serviços (identificador a confirmar)", assoc="Correlata",
  rel=["d01_transicao30", "d02_contr_transicao"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  resp="Delivery/Operação")

I("d02_contr_transicao", "D02", "RFP 3.2 × Anexo I 4.1", "A: D01 p. 2 (impressa: 1), item 3.2 · B: § 4. Transição, item 4.1",
  'A: "A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato." · B: "A transição dos serviços deverá ser concluída em até 60 (sessenta) dias corridos a partir da assinatura do contrato."',
  "Contradição", "Transição/Implantação",
  "Prazos de transição incompatíveis (30 × 60 dias) para o mesmo marco. Não há cláusula de precedência. A diferença afeta o tamanho da equipe de transição, o período de operação em paralelo sem custo e o risco de multa de SLA após a transição.",
  obrig="Mandatório", s=4, p=3,
  impacto="A diferença entre 30 e 60 dias muda o custo de transição e o risco de descumprimento.",
  fw="ITIL 4", ctrl="Gestão de transição/implantação de serviços (identificador a confirmar)", assoc="Correlata",
  rel=["d01_transicao30", "d02_transicao60", "d01_precedencia", "d03_risco_transicao"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="Qual prazo de transição prevalece: 30 dias corridos (RFP, item 3.2) ou 60 dias corridos (Anexo I, item 4.1)? Os SLAs e multas passam a ser exigíveis somente após a conclusão da transição?",
  resp="Delivery/Operação")

I("d02_paralelo", "D02", "4. Transição — 4.2", "§ 4. Transição, item 4.2",
  '"Durante a transição, o proponente deverá operar em paralelo com o fornecedor atual, sem custo adicional para o Contratante."',
  "Obrigação contratual", "Transição/Implantação / Comercial/Preço",
  "Operação em paralelo durante a transição, sem custo adicional. Probabilidade 5: o custo decorre diretamente do texto (\"sem custo adicional para o Contratante\"), sem depender de evento incerto. O paralelo depende do fornecedor atual, cujo contrato de SIEM encerra em 31/01/2027, e não se define a responsabilidade pela cooperação do fornecedor atual.",
  obrig="Mandatório", s=3, p=5,
  impacto="Custo de 30 a 60 dias de operação dupla a ser absorvido no preço.",
  fw="ITIL 4", ctrl="Gestão de transição/implantação de serviços (identificador a confirmar)", assoc="Correlata",
  rel=["d02_contr_transicao", "d03_siem_legado", "d03_risco_transicao"], acao="Precificar",
  perg="O Banco garantirá contratualmente a cooperação do fornecedor atual durante a operação em paralelo (acesso, documentação e passagem de conhecimento)?",
  resp="Pricing/Financeiro")

I("d02_cissp", "D02", "5. Equipe — 5.1", "§ 5. Equipe, item 5.1",
  '"O serviço deverá contar com coordenador com certificação CISSP, dedicado exclusivamente ao contrato."',
  "Restrição", "Pessoas/Equipe",
  "Coordenador CISSP com dedicação exclusiva. Probabilidade 5: custo fixo explicitamente exigido pelo texto (\"dedicado exclusivamente ao contrato\"). Não se diz se o coordenador deve ser presencial nem se a certificação deve ser comprovada na proposta.",
  obrig="Mandatório", s=3, p=5,
  impacto="Custo fixo de um profissional sênior exclusivo durante 36 meses.",
  fw=NA, assoc=NA, rel=["d01_equipe_cert"], acao="Precificar", resp="RH/Staffing")

I("d02_n1_presencial", "D02", "5. Equipe — 5.2", "§ 5. Equipe, item 5.2",
  '"Os analistas de nível 1 deverão atuar presencialmente na sede do Contratante, em São Paulo/SP, em horário comercial."',
  "Restrição", "Pessoas/Equipe",
  "Analistas N1 presenciais na sede em São Paulo, em horário comercial. Alterado pela resposta 6 do Q&A (atuação remota permitida, desde que em território nacional).",
  obrig="Mandatório", s=3, p=3, impacto="Custo de alocação presencial e de deslocamento.",
  fw=NA, assoc=NA, rel=["d04_q6"], vig="Alterado", acao="Precificar", resp="RH/Staffing")

I("d02_vpn", "D02", "6. Responsabilidades do Contratante — 6.1", "§ 6. Responsabilidades do Contratante, item 6.1",
  '"Disponibilizar acesso remoto seguro (VPN) aos ambientes monitorados."',
  "Responsabilidade / dependência do cliente", "Infraestrutura/Cloud",
  "O Banco fornece a VPN aos ambientes monitorados. Não há prazo para disponibilizá-la.",
  s=2, p=3, impacto="Atraso do Banco pode comprometer a transição.",
  fw=NA, assoc=NA, acao="Registrar premissa na proposta", resp="Delivery/Operação")

I("d02_doc10", "D02", "6. Responsabilidades do Contratante — 6.2", "§ 6. Responsabilidades do Contratante, item 6.2",
  '"Disponibilizar a documentação técnica do ambiente em até 10 (dez) dias após a assinatura do contrato."',
  "Responsabilidade / dependência do cliente", "Transição/Implantação",
  "Documentação do ambiente em até 10 dias após a assinatura. Se a transição for de 30 dias (RFP 3.2), sobram 20 dias para executá-la com base na documentação. Não há previsão de ajuste de prazo se o Banco atrasar.",
  s=3, p=3, impacto="Compressão do prazo de transição por dependência do cliente.",
  fw=NA, assoc=NA, rel=["d02_contr_transicao", "d03_risco_transicao"], acao="Registrar premissa na proposta",
  perg="Atrasos do Banco na entrega da documentação técnica (item 6.2) ou da VPN (item 6.1) prorrogarão proporcionalmente o prazo de transição e suspenderão a aplicação de SLAs e multas?",
  resp="Delivery/Operação")

# =============================================================== D03 — Apresentação (PowerPoint)
I("d03_inv", "D03", "Apresentação inteira (slides 1 a 5 e notas)", "slides 1–5 · slide 5 — notas do apresentador",
  '"Workshop com proponentes — RFP nº 2026-017 — 22/10/2026"',
  "Registro de cobertura", "Administrativo do processo",
  "Inventário: PowerPoint com 5 slides, sem slides ocultos; o slide 5 tem notas do apresentador, analisadas (ampliam o escopo). Integralmente analisado. Data: workshop de 22/10/2026. Nenhum documento define se o material do workshop integra a RFP (ver Lacuna de precedência).",
  fw="—", assoc="—", resp="Bid Manager")

I("d03_usuarios", "D03", "Slide 2 — Números do ambiente × RFP 2.1", 'A: D01 p. 2 (impressa: 1), item 2.1 · B: slide 2 — "Números do ambiente"',
  'A: "abrangendo aproximadamente 4.500 colaboradores" · B: "6.200 usuários ativos"',
  "Contradição", "Comercial/Preço",
  "A RFP dimensiona cerca de 4.500 colaboradores; o workshop informa 6.200 usuários ativos (38% a mais). A diferença pode decorrer de contas de terceiros, de serviço ou das subsidiárias, mas isso não é explicado.",
  obrig="Informativo", s=4, p=3,
  impacto="Preço por usuário de SOC e IAM pode ficar subdimensionado em mais de um terço.",
  rel=["d01_usuarios", "d04_q5", "d04_contr_usuarios", "d03_subsid"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A", resp="Pricing/Financeiro")

I("d03_servidores", "D03", "Slide 2 — Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"850 servidores (70% Windows, 30% Linux)"',
  "Dado de dimensionamento", "Infraestrutura/Cloud",
  "850 servidores (cerca de 595 Windows e 255 Linux), base para estimar fontes de log. Faltam ativos de rede, segurança, aplicações e bancos de dados.",
  s=3, p=3, impacto="Base parcial para dimensionar a integração e a volumetria do SIEM.",
  rel=["d02_integr"], acao="Precificar", resp="Pré-venda/Arquitetura")

I("d03_dcs", "D03", "Slide 2 — Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"2 data centers próprios (São Paulo e Campinas)"',
  "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Dois data centers próprios (São Paulo e Campinas): coletores de log nos dois sites e eventual atuação presencial em Campinas.",
  s=2, p=3, impacto="Coletores e conectividade em dois sites.", acao="Precificar", resp="Pré-venda/Arquitetura")

I("d03_nuvens", "D03", "Slide 2 — Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"Workloads em 2 nuvens públicas"',
  "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Há workloads em duas nuvens públicas, que não são identificadas, nem os serviços e contas a monitorar.",
  s=3, p=3, impacto="Conectores e volumetria de logs de nuvem não dimensionáveis.",
  rel=["d02_integr"], acao="Esclarecer no Q&A",
  perg="Quais são os dois provedores de nuvem pública, quantas contas/assinaturas e quais serviços devem ser monitorados pelo SOC?",
  resp="Pré-venda/Arquitetura")

I("d03_siem_legado", "D03", "Slide 3 — Ferramentas atuais", 'slide 3 — "Ferramentas atuais"',
  '"SIEM legado — contrato encerra em 31/01/2027, sem possibilidade de prorrogação"',
  "Premissa do cliente", "Transição/Implantação",
  "O contrato do SIEM legado termina em 31/01/2027, sem prorrogação. É a data-limite para a migração e para a operação em paralelo.",
  s=4, p=3, impacto="Prazo rígido para a nova plataforma estar operacional e os logs migrados.",
  rel=["d01_crono_inicio", "d02_paralelo", "d03_migracao", "d03_risco_transicao"], acao="Registrar premissa na proposta",
  resp="Delivery/Operação")

I("d03_iam_atual", "D03", "Slide 3 — Ferramentas atuais", 'slide 3 — "Ferramentas atuais"',
  '"IAM: Active Directory + scripts internos"',
  "Dado de dimensionamento", "Segurança da Informação/Cyber",
  "IAM atual baseado em Active Directory e scripts internos, sem plataforma IGA. Indica que os requisitos do Anexo I (ciclo de vida, recertificação) podem exigir uma ferramenta nova.",
  s=3, p=3, impacto="Possível necessidade de fornecer plataforma IAM/IGA.",
  rel=["d02_iam_lacuna"], acao="Precificar", resp="Pré-venda/Arquitetura")

I("d03_sem_pam", "D03", "Slide 3 — Ferramentas atuais", 'slide 3 — "Ferramentas atuais"',
  '"Não há solução de PAM"',
  "Oportunidade / diferencial", "Segurança da Informação/Cyber",
  "Não há PAM no ambiente atual, e o Anexo I 3.4 o trata como desejável. Oferecer PAM pode diferenciar a proposta nos critérios \"Ferramentas e tecnologia\" e de pontuação do questionário.",
  obrig="Desejável", fw=ISO, ctrl="A.8.2 — Direitos de acesso privilegiados", assoc="Correlata",
  rel=["d02_pam"], acao="Precificar", resp="Pré-venda/Arquitetura")

I("d03_alertas", "D03", "Slide 4 — Desafios", 'slide 4 — "Desafios"',
  '"Cerca de 1.200 alertas por dia" · "70% de falsos positivos"',
  "Dado de dimensionamento", "Operação/Serviços",
  "Cerca de 1.200 alertas por dia, dos quais 70% falsos positivos (cerca de 840). Base para dimensionar a triagem N1. Não substitui a volumetria de eventos (EPS).",
  s=3, p=3, impacto="Dimensionamento da equipe de triagem.",
  rel=["d03_meta_fp"], acao="Precificar", resp="Delivery/Operação")

I("d03_meta_fp", "D03", "Slide 4 — Desafios", 'slide 4 — "Desafios"',
  '"Meta: reduzir os falsos positivos para 10% no primeiro trimestre de operação"',
  "Ambiguidade", "Operação/Serviços",
  "Meta agressiva (de 70% para 10% em três meses) apresentada no workshop, sem constar do Anexo I. Não se sabe se é expectativa ou SLA contratual sujeito à multa do item 7.4, nem como os falsos positivos serão medidos.",
  obrig="Desejável", s=4, p=3,
  impacto="Se for contratual, cria SLA de difícil cumprimento sujeito a multa por ocorrência.",
  fw="ITIL 4", ctrl="Gestão de nível de serviço (identificador a confirmar)", assoc="Correlata",
  rel=["d03_alertas", "d01_multa"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A meta de reduzir falsos positivos para 10% no primeiro trimestre é um SLA contratual sujeito à multa do item 7.4 ou apenas uma expectativa? Como os falsos positivos serão medidos?",
  resp="Delivery/Operação")

I("d03_migracao", "D03", "Slide 5 — Expectativas para o novo serviço", 'slide 5 — "Expectativas para o novo serviço"',
  '"Migração de 24 meses de logs históricos do SIEM legado para a nova plataforma"',
  "Ambiguidade", "Transição/Implantação / Técnico/Arquitetura",
  "Escopo adicional que não consta do Anexo I: migrar 24 meses de logs históricos do SIEM legado, cujo contrato termina em 31/01/2027. Volume, formato, ferramenta de origem e cooperação do fornecedor legado não são informados. Também amplia o armazenamento (24 meses além da retenção mínima de 12).",
  obrig="Desejável", s=4, p=3,
  impacto="Esforço de migração e armazenamento não dimensionável; deve ocorrer antes do fim do contrato legado.",
  fw=ISO, ctrl="A.8.15 — Registro de logs", assoc="Correlata",
  rel=["d03_siem_legado", "d02_ambig_ret", "d03_risco_transicao"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A migração de 24 meses de logs históricos do SIEM legado faz parte do escopo obrigatório? Qual o volume (TB), o formato e o produto do SIEM legado, e o fornecedor atual apoiará a exportação antes de 31/01/2027?",
  resp="Pré-venda/Arquitetura")

I("d03_visao_riscos", "D03", "Slide 5 — Expectativas para o novo serviço", 'slide 5 — "Expectativas para o novo serviço"',
  '"Visão unificada de riscos para a diretoria"',
  "Ambiguidade", "Operação/Serviços",
  "Expectativa vaga, sem correspondente no Anexo I. Pode significar um relatório executivo ou uma plataforma de GRC/dashboard.",
  obrig="Desejável", s=2, p=3, impacto="Possível escopo de ferramenta de painel ou GRC não previsto.",
  fw=NA, assoc=NA, vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A \"visão unificada de riscos para a diretoria\" corresponde ao relatório mensal do item 2.3 do Anexo I ou exige painel ou ferramenta específica?",
  resp="Pré-venda/Arquitetura")

I("d03_subsid", "D03", "Slide 5 — notas do apresentador × RFP 2.1", 'A: D01 p. 2 (impressa: 1), item 2.1 · B: slide 5 — notas do apresentador',
  'A: "abrangendo aproximadamente 4.500 colaboradores" · B: "as subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários adicionais) também deverão ser incluídas no escopo"',
  "Contradição", "Comercial/Preço / Regulatório/Compliance",
  "Ampliação de escopo escondida nas notas do apresentador (não exibidas nos slides): duas subsidiárias com cerca de 900 usuários adicionais. A RFP, o Anexo I e o Q&A não as mencionam. As subsidiárias podem ter ambientes, ativos e requisitos regulatórios próprios, a confirmar.",
  obrig="Mandatório", s=4, p=3,
  impacto="Escopo e dimensionamento ampliados (usuários, ativos, integrações) sem previsão formal; risco de o Banco exigir a inclusão sem contrapartida.",
  rel=["d01_usuarios", "d03_usuarios", "d04_contr_usuarios", "d02_integr"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="As subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários, conforme o workshop) fazem parte do escopo do SOC e do IAM? Em caso positivo, quais ativos e ambientes delas devem ser incluídos e quem será a parte contratante?",
  resp="Bid Manager")

I("d03_risco_transicao", "D03", "Risco combinado — transição e SIEM legado", 'D01 p. 2 (impressa: 1), itens 3.1 e 3.2 · § 4. Transição · slide 3 — "Ferramentas atuais" · slide 5 — "Expectativas para o novo serviço"',
  '"contrato encerra em 31/01/2027, sem possibilidade de prorrogação" · "Início previsto dos serviços 01/02/2027" · "deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato" · "operar em paralelo com o fornecedor atual, sem custo adicional"',
  "Risco para o proponente", "Transição/Implantação",
  "Inferência a partir de vários itens: o SIEM legado termina em 31/01/2027 sem prorrogação; a operação começa em 01/02/2027; a transição (30 ou 60 dias) conta da assinatura, cuja data não é informada; o proponente deve operar em paralelo sem custo, migrar 24 meses de logs e depende da documentação do Banco (até 10 dias). Qualquer atraso na assinatura (propostas em 27/11/2026) comprime a transição e pode deixar o Banco sem SIEM, com SLAs e multa de 10% por ocorrência sem teto desde o primeiro dia. Probabilidade 4: o próprio cronograma não deixa folga entre o fim do contrato legado (31/01/2027) e o início dos serviços (01/02/2027), e não há data de assinatura.",
  obrig="Mandatório", s=5, p=4, nat="Inferida",
  impacto="Risco de falha na transição com multas sem teto e perda de dados históricos; afeta a decisão de Go/No-Go e o preço de transição.",
  fw="ITIL 4", ctrl="Gestão de transição/implantação de serviços (identificador a confirmar)", assoc="Correlata",
  rel=["d01_transicao30", "d02_transicao60", "d02_contr_transicao", "d01_crono_inicio", "d03_siem_legado",
       "d02_paralelo", "d03_migracao", "d02_doc10", "d01_multa"],
  vig="Em esclarecimento", acao="Avaliar Go/No-Go",
  perg="Para viabilizar a transição antes de 31/01/2027, qual a data-limite prevista para assinatura do contrato? O Banco aceita período de carência de SLAs e multas durante a transição e nos primeiros 90 dias de operação?",
  resp="Bid Manager")

# =============================================================== D04 — Q&A e Questionário (Excel)
I("d04_inv", "D04", "Planilha inteira (4 abas)", 'aba "Instruções" · aba "Q&A Rodada 1" · aba "Questionário Técnico" · aba "Pesos" (OCULTA)',
  '"Questionário Técnico e Respostas aos Esclarecimentos — RFP nº 2026-017"',
  "Registro de cobertura", "Administrativo do processo",
  "Inventário: Excel com 4 abas, uma delas oculta (\"Pesos\"), todas analisadas. \"Q&A Rodada 1\": 6 perguntas e respostas datadas de 12/11/2026. \"Questionário Técnico\": 6 requisitos (QT-01 a QT-06) a preencher pelo proponente. \"Pesos\" (oculta): pesos dos requisitos e regra de penalização não divulgada na RFP. O arquivo combina documento a preencher e respostas do cliente.",
  fw="—", assoc="—", resp="Bid Manager")

I("d04_instr_obrig", "D04", "Aba Instruções", 'aba "Instruções" · A3',
  '"O preenchimento de todas as abas deste arquivo é obrigatório. Questionários incompletos serão desclassificados."',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Endurece a RFP 4.4: o questionário incompleto passa a ser causa de desclassificação. Probabilidade 5: a sanção é expressa no texto e decorre diretamente do não preenchimento.",
  obrig="Mandatório", s=5, p=5,
  impacto="Desclassificação da proposta.",
  rel=["d01_questionario", "d04_ambig_abas"], acao="Atender", resp="Pré-venda/Arquitetura")

I("d04_ambig_abas", "D04", "Aba Instruções", 'aba "Instruções" · A3',
  '"O preenchimento de todas as abas deste arquivo é obrigatório."',
  "Ambiguidade", "Administrativo do processo",
  "\"Todas as abas\" incluiria a aba de Q&A e a aba oculta \"Pesos\", que não têm campos a preencher pelo proponente. Também não se sabe se a coluna \"Comentários\" do questionário é obrigatória. Como a consequência é a desclassificação, a interpretação errada é grave.",
  obrig="Mandatório", s=5, p=3,
  impacto="Risco de desclassificação por interpretação divergente do que é \"preenchimento completo\".",
  rel=["d04_instr_obrig"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Quais abas e colunas devem ser preenchidas pelo proponente para que o questionário seja considerado completo? A coluna \"Comentários\" é obrigatória em todas as linhas?",
  resp="Bid Manager")

I("d04_q1", "D04", "Q&A Rodada 1 — Pergunta 1 (RFP, item 3.1)", 'aba "Q&A Rodada 1" · E2 · Pergunta 1 · 12/11/2026',
  '"A data de entrega das propostas fica prorrogada para 27/11/2026, até as 18h."',
  "Prazo / marco", "Administrativo do processo",
  "Altera a RFP 3.1: entrega prorrogada de 20/11 para 27/11/2026, até as 18h. A alteração foi feita por resposta de Q&A, sem adendo formal à RFP. As demais datas (início em 01/02/2027) não foram ajustadas, o que comprime ainda mais o prazo até a assinatura.",
  obrig="Mandatório", s=5, p=3,
  impacto="Proposta fora do prazo não é considerada; prazo de assinatura e transição fica mais apertado.",
  rel=["d01_crono_entrega", "d03_risco_transicao"], acao="Atender", resp="Bid Manager")

I("d04_q2", "D04", "Q&A Rodada 1 — Pergunta 2 (RFP, item 5.1 c)", 'aba "Q&A Rodada 1" · E3 · Pergunta 2 · 12/11/2026',
  '"Não. O SOC deverá estar localizado em território nacional."',
  "Critério eliminatório / de habilitação", "Operação/Serviços / Regulatório/Compliance",
  "Confirma a RFP 5.1 c): SOC no Brasil, sem exceção. Probabilidade 5: inabilitação expressa no caput do item 5.1 para quem não comprovar.",
  obrig="Mandatório", s=5, p=5,
  impacto="Inabilitação de proposta com SOC operado do exterior.",
  rel=["d01_hab_soc_nacional"], vig="Duplicado", acao="Atender", resp="Delivery/Operação")

I("d04_q3", "D04", "Q&A Rodada 1 — Pergunta 3 (Anexo I, item 1.4)", 'aba "Q&A Rodada 1" · E4 · Pergunta 3 · 12/11/2026',
  '"A volumetria será informada somente ao proponente vencedor."',
  "Risco para o proponente", "Comercial/Preço / Técnico/Arquitetura",
  "O Banco recusou formalmente informar a volumetria (EPS), indispensável para licenciar o SIEM, dimensionar o armazenamento de 12 meses e 5 anos e a equipe. Probabilidade 5: informação indispensável ao preço recusada formalmente pelo cliente. Sem a informação, o proponente precifica no escuro ou registra premissa de volumetria com reequilíbrio.",
  obrig="Informativo", s=4, p=5,
  impacto="Preço de SIEM e storage pode ficar subdimensionado, com prejuízo durante 36 meses, ou superdimensionado, perdendo competitividade.",
  rel=["d02_eps_lacuna", "d02_siem", "d02_integr", "d02_ret5"], acao="Registrar premissa na proposta",
  perg="Na impossibilidade de informar o EPS, o Banco aceita que a proposta adote uma premissa de volumetria (faixa de EPS e GB/dia) com revisão de preço caso a volumetria medida após a contratação seja superior?",
  resp="Pricing/Financeiro")

I("d04_q4", "D04", "Q&A Rodada 1 — Pergunta 4 (RFP, item 7.4)", 'aba "Q&A Rodada 1" · E5 · Pergunta 4 · 12/11/2026',
  '"As condições do item 7 permanecem inalteradas."',
  "Risco para o proponente", "Jurídico/Contratual / Financeiro",
  "Risco combinado: o Banco não respondeu à pergunta sobre o teto das multas e manteve todo o item 7. Somam-se a multa de 10% do valor mensal por ocorrência sem teto (7.4) e a responsabilidade integral e ilimitada (7.5). Probabilidade 4: o cliente já deixou sem resposta objetiva e recusou rever o tema em esclarecimento formal, o que indica que as cláusulas serão mantidas no contrato.",
  obrig="Mandatório", s=5, p=4,
  impacto="Exposição financeira e jurídica ilimitada; insumo central para o Go/No-Go e para a cotação de seguro.",
  fw=CC, ctrl="Art. 412 — limite da cláusula penal ao valor da obrigação principal", assoc="Correlata",
  rel=["d01_multa", "d01_resp_ilimitada", "d01_seguro"], acao="Avaliar Go/No-Go",
  perg="Mesmo mantidas as condições do item 7, o Banco aceita ressalvas na proposta limitando o total de multas a um percentual do valor mensal e a responsabilidade a um múltiplo do valor anual do contrato, ou tais ressalvas implicarão desclassificação?",
  resp="Jurídico")

I("d04_q5", "D04", "Q&A Rodada 1 — Pergunta 5 (RFP, item 2.1)", 'aba "Q&A Rodada 1" · E6 · Pergunta 5 · 12/11/2026',
  '"Considerar 5.000 usuários."',
  "Dado de dimensionamento", "Comercial/Preço",
  "Altera a base de dimensionamento da RFP 2.1 (cerca de 4.500) para 5.000 usuários, sem explicar a divergência com os 6.200 usuários ativos e os cerca de 900 das subsidiárias informados no workshop.",
  obrig="Mandatório", s=3, p=3, impacto="Base oficial para preço por usuário, ainda contestável.",
  rel=["d01_usuarios", "d04_contr_usuarios"], acao="Precificar", resp="Pricing/Financeiro")

I("d04_contr_usuarios", "D04", "Q&A 5 × slide 2 × notas do slide 5", 'A: aba "Q&A Rodada 1" · E6 · B: D03 slide 2 — "Números do ambiente" · C: D03 slide 5 — notas do apresentador',
  'A: "Considerar 5.000 usuários." · B: "6.200 usuários ativos" · C: "cerca de 900 usuários adicionais"',
  "Contradição", "Comercial/Preço",
  "Quatro números para a mesma base: cerca de 4.500 (RFP 2.1), 5.000 (Q&A 5), 6.200 usuários ativos (workshop) e mais cerca de 900 das subsidiárias (notas), o que pode chegar a cerca de 7.100. A diferença entre 5.000 e 7.100 é de 42%. Não há cláusula de precedência nem previsão de ajuste de preço por variação de usuários.",
  obrig="Informativo", s=4, p=3,
  impacto="Subdimensionamento de até cerca de 42% na base de usuários, se o Banco exigir a cobertura real do ambiente.",
  rel=["d01_usuarios", "d03_usuarios", "d03_subsid", "d04_q5", "d01_precedencia"], vig="Em esclarecimento",
  acao="Registrar premissa na proposta",
  perg="A resposta 5 indica 5.000 usuários, mas o workshop apresentou 6.200 usuários ativos e mais cerca de 900 usuários das subsidiárias. Qual número prevalece, ele inclui as subsidiárias e haverá ajuste de preço se a quantidade real superar a de referência?",
  resp="Pricing/Financeiro")

I("d04_q6", "D04", "Q&A Rodada 1 — Pergunta 6 (Anexo I, item 5.2)", 'aba "Q&A Rodada 1" · E7 · Pergunta 6 · 12/11/2026',
  '"Sim, desde que em território nacional."',
  "Restrição", "Pessoas/Equipe",
  "Altera o Anexo I 5.2: analistas N1 podem atuar remotamente, desde que no Brasil. Reduz o custo de alocação presencial. A resposta não esclarece se a presença em horário comercial deixa de ser exigida em qualquer hipótese.",
  obrig="Mandatório", s=2, p=3, impacto="Redução de custo de equipe N1; restrição de alocação no Brasil.",
  rel=["d02_n1_presencial"], acao="Precificar", resp="RH/Staffing")

for k, qid, cel, texto, obr, peso, desc, s, rel, perg, resp, fw, ctrl, assoc in [
    ("d04_qt01", "QT-01", "B2", "Possui certificação ISO/IEC 27001 com escopo que inclua os serviços de SOC?", "Sim", "3",
     "Questionário repete o critério de habilitação da RFP 5.1 a) (obrigatório, peso 3). A consequência de responder \"Não atende\" a um requisito obrigatório não é definida.",
     3, ["d01_hab_iso", "d04_pesos_regra"], "—", "Compliance", ISO, "Certificação do SGSI — requisitos das cláusulas 4 a 10", "Direta"),
    ("d04_qt02", "QT-02", "B3", "Oferece integração nativa com plataforma SOAR?", "Não", "1",
     "Requisito não obrigatório (peso 1) que não consta do Anexo I. Pela regra oculta da aba \"Pesos\", responder \"Não atende\" reduz 2 pontos da Nota Técnica: na prática, o SOAR vira requisito pontuado.",
     3, ["d04_pesos_regra"], "Integração com SOAR passa a fazer parte do escopo do serviço ou serve apenas para pontuação? Qual plataforma de SOAR o Banco utiliza ou pretende utilizar?",
     "Pré-venda/Arquitetura", ISO, "A.5.26 — Resposta a incidentes de segurança da informação", "Correlata"),
    ("d04_qt03", "QT-03", "B4", "Retém os logs online por no mínimo 12 meses?", "Sim", "2",
     "Requisito obrigatório (peso 2) que acrescenta a condição \"online\" ao Anexo I 1.3 e reforça a leitura de 12 meses online + arquivo até 5 anos (1.6).",
     3, ["d02_ret12", "d02_ambig_ret"], "—", "Pré-venda/Arquitetura", ISO, "A.8.15 — Registro de logs", "Direta"),
    ("d04_qt04", "QT-04", "B5", "Atende aos requisitos da Resolução CMN nº 4.893/2021?", "Sim", "3",
     "Requisito obrigatório (peso 3) e genérico: a resolução tem obrigações dirigidas à instituição financeira e aos prestadores; não se especifica quais devem ser atendidas pelo proponente nem como comprovar.",
     4, ["d01_cmn", "d04_pesos_regra"], "Quais requisitos específicos da Resolução CMN nº 4.893/2021 o proponente deve declarar atender no QT-04 e que evidências serão exigidas?",
     "Compliance", CMN, "Requisitos aplicáveis a prestadores de serviço (identificador a confirmar)", "Direta"),
    ("d04_qt05", "QT-05", "B6", "Oferece serviço de threat intelligence?", "Não", "2",
     "Requisito não obrigatório (peso 2) ausente do Anexo I. A regra oculta penaliza \"Não atende\" em 2 pontos. Feeds de threat intelligence normalmente vêm de terceiros, o que esbarra na vedação de subcontratação (7.7) e, se processarem dados fora do país, no Anexo III.",
     3, ["d04_pesos_regra", "d02_ambig_subcontr", "d01_subcontr"], "O serviço de threat intelligence (QT-05) passa a integrar o escopo? O uso de feeds de terceiros é permitido diante da vedação de subcontratação do item 7.7?",
     "Segurança/Cyber", "NIST CSF 2.0", "ID.RA — Avaliação de riscos (inteligência de ameaças)", "Correlata"),
    ("d04_qt06", "QT-06", "B7", "Possui equipe com certificações reconhecidas pelo mercado?", "Sim", "2",
     "Requisito obrigatório (peso 2) tão vago quanto a RFP 5.2: não define quais certificações nem quantos profissionais.",
     3, ["d01_equipe_cert", "d02_cissp"], "Quais certificações são consideradas \"reconhecidas pelo mercado\" no QT-06 e qual a quantidade mínima de profissionais certificados?",
     "RH/Staffing", ISO, "A.6.3 — Conscientização, educação e treinamento em segurança da informação", "Correlata"),
]:
    I(k, "D04", f"Questionário Técnico — {qid}", f'aba "Questionário Técnico" · {cel} · {qid} · aba "Pesos" (OCULTA)',
      f'"{texto}"', "Critério de avaliação / pontuação",
      "Regulatório/Compliance" if qid == "QT-04" else "Segurança da Informação/Cyber" if qid != "QT-06" else "Pessoas/Equipe",
      desc, obrig="Mandatório" if obr == "Sim" else "Desejável", s=s, p=3,
      impacto=f"Afeta a Nota Técnica (peso {peso} na aba oculta) e a completude do questionário, que é eliminatória.",
      fw=fw, ctrl=ctrl, assoc=assoc, rel=rel,
      vig="Duplicado" if qid == "QT-01" else "Vigente",
      acao="Esclarecer no Q&A" if perg != "—" else "Atender", perg=perg, resp=resp)

I("d04_pesos_regra", "D04", "Aba Pesos (OCULTA)", 'aba "Pesos" (OCULTA) · A9',
  '"Requisitos não obrigatórios respondidos como \'Não atende\' reduzem a Nota Técnica em 2 (dois) pontos cada."',
  "Critério de avaliação / pontuação", "Administrativo do processo",
  "Regra de pontuação escondida em aba oculta e ausente da RFP: cada requisito não obrigatório (QT-02 SOAR, QT-05 threat intelligence) respondido \"Não atende\" tira 2 pontos da Nota Técnica (até 4 pontos, cerca de 6,7% de 60). Isso pode levar a proposta abaixo do corte de 70% (6.3). Requisitos opcionais passam a ser, na prática, penalizados.",
  obrig="Mandatório", s=4, p=3,
  impacto="Perda de até 4 pontos técnicos e risco de desclassificação pelo corte de 70%; pressiona a incluir SOAR e threat intelligence no escopo e no preço.",
  rel=["d04_qt02", "d04_qt05", "d01_corte70", "d04_contr_pesos"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A regra da aba \"Pesos\" (redução de 2 pontos por requisito não obrigatório respondido como \"Não atende\") será aplicada? Ela não consta da RFP; solicitamos confirmar a regra e publicá-la a todos os proponentes.",
  resp="Bid Manager")

I("d04_contr_pesos", "D04", "Aba Pesos (OCULTA) × RFP 6.2", 'A: D01 p. 4 (impressa: 3), item 6.2 · B: aba "Pesos" (OCULTA) · A1:B9',
  'A: "A Nota Técnica, de no máximo 60 (sessenta) pontos, será atribuída conforme os critérios abaixo" · B: "Requisitos não obrigatórios respondidos como \'Não atende\' reduzem a Nota Técnica em 2 (dois) pontos cada."',
  "Contradição", "Administrativo do processo",
  "A RFP diz que a Nota Técnica é atribuída pelos quatro critérios do 6.2; a aba oculta cria pesos por requisito (3, 1, 2, 3, 2, 2; total 13) e uma dedução que não está na RFP. Não se sabe como os pesos entram na nota nem em qual critério do 6.2. Soma-se à divergência 60 × 65 pontos.",
  obrig="Informativo", s=4, p=3,
  impacto="Metodologia de pontuação incerta; impossível simular a Nota Técnica e o risco de corte.",
  rel=["d01_contr_soma", "d04_pesos_regra", "d01_corte70", "d01_precedencia"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="Como os pesos da aba \"Pesos\" do questionário técnico são incorporados à Nota Técnica de 60 pontos do item 6.2 da RFP e em qual critério?",
  resp="Bid Manager")

DOCS = [
    {"codigo": "D01", "arquivo": "RFP-2026-017_Servicos_SOC_IAM.pdf", "tipo": "RFP (inclui Anexo III digitalizado na p. 6)", "versao": "Versão 1.0 — 15/10/2026"},
    {"codigo": "D02", "arquivo": "Anexo_I_Especificacao_Tecnica.docx", "tipo": "Anexo técnico", "versao": "Versão 1.0 — 15/10/2026"},
    {"codigo": "D03", "arquivo": "Apresentacao_Ambiente_Atual.pptx", "tipo": "Apresentação (workshop)", "versao": "Workshop de 22/10/2026"},
    {"codigo": "D04", "arquivo": "QA_Rodada1_e_Questionario.xlsx", "tipo": "Q&A Rodada 1 + Questionário técnico", "versao": "Rodada 1 — respostas de 12/11/2026"},
]

if __name__ == "__main__":
    out, n = sys.argv[1], int(sys.argv[2])
    codes = [d["codigo"] for d in DOCS[:n]]
    nexts = {1: "Anexo_I_Especificacao_Tecnica.docx (D02), a partir do § 1", 2: "Apresentacao_Ambiente_Atual.pptx (D03), a partir do slide 1",
             3: "QA_Rodada1_e_Questionario.xlsx (D04), a partir da aba \"Instruções\""}
    itens = [i for i in ITENS if i["doc"] in codes]
    # Em rodadas parciais, referências a itens de documentos ainda não processados ficam fora
    keys = {i["chave"] for i in itens}
    import copy, re
    itens = copy.deepcopy(itens)
    for i in itens:
        i["relacionados"] = [r for r in i["relacionados"] if r in keys]
    docs = [dict(d, situacao="processado") for d in DOCS[:n]] + [dict(d, situacao="pendente") for d in DOCS[n:]]
    data = {"processo": "RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Serviços Gerenciados de SOC e IAM",
            "documentos": docs if n == len(DOCS) else docs,
            "itens": itens,
            "status": {"final": True} if n == len(DOCS) else {"final": False, "parte": n, "concluidos": n, "proximo": nexts[n]}}
    open(out, "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, indent=1))
    print(len(itens), "itens")
