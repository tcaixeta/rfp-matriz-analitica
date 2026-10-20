# Gera itens.json para scripts/build_matrix.py. Uso: python itens_src.py <n_docs_concluidos> <saida.json>
import json, sys

ITENS = []


def I(chave, doc, secao, loc, ev, tipo, dom, desc, s=None, p=None, ob="Informativo", nat="Explícita", imp="—",
      fw="—", ctl="—", assoc="—", rel=(), vig="Vigente", acao="Nenhuma (informativo)", perg="—", resp="—", pend=None):
    it = dict(chave=chave, doc=doc, secao=secao, localizador=loc, evidencia=ev, tipo=tipo, dominio=dom, descricao=desc,
              obrigatoriedade=ob, natureza=nat, impacto=imp, framework=fw, controle=ctl, associacao=assoc,
              relacionados=list(rel), vigencia=vig, acao=acao, pergunta=perg, responsavel=resp)
    if s is not None:
        it["s"], it["p"] = s, p
    if pend:
        it["pendencia"] = pend
    ITENS.append(it)


ISO = "ISO/IEC 27001:2022"
NIST = "NIST CSF 2.0"
ITIL = "ITIL 4"
LGPD = "LGPD (Lei 13.709/2018)"
R4893 = "Resolução CMN nº 4.893/2021 (citada no documento)"
CC = "Código Civil (Lei 10.406/2002)"
NA = "Não aplicável"

# =====================================================================================
# D01 — RFP-2026-017_Servicos_SOC_IAM.pdf
# =====================================================================================
D = "D01"
I("d01_inventario", D, "Documento inteiro", "p. 1–6 (impressas: sem número a 5)",
  '"Solicitação de Proposta (RFP) nº 2026-017" [...] "Versão 1.0 — 15/10/2026"', "Registro de cobertura",
  "Administrativo do processo",
  "Inventário: PDF de 6 páginas, texto extraível nas p. 1–5. A p. 6 (impressa: 5) não tem camada de texto (imagem digitalizada); foi lida visualmente e transcrita em D01_p6_ocr.md: contém o Anexo III — Declaração de Localização de Dados, analisado nos itens {d01_anx3_entrega} e {d01_anx3_dados}. Cabeçalho repetido em todas as páginas ('DOCUMENTO FICTÍCIO PARA TESTE') desconsiderado. Leitura integral.",
  rel=["d01_anx3_entrega"])

I("d01_regime", D, "1. APRESENTAÇÃO, item 1.2", "p. 2 (impressa: 1)",
  '"O Banco é instituição financeira autorizada a funcionar pelo Banco Central do Brasil e está sujeito à Resolução CMN nº 4.893/2021"',
  "Registro de cobertura", "Regulatório/Compliance",
  "Regime identificado: contratação PRIVADA (sociedade anônima, 'RFP', envio pelo 'portal de fornecedores do Banco' — item 4.1; não há menção a licitação, edital ou Lei 14.133/2021) em SETOR REGULADO (instituição financeira supervisionada pelo Banco Central, sujeita à Resolução CMN nº 4.893/2021). Legislação de contratação pública não se aplica; a referência jurídica é o Código Civil e a regulação setorial citada. Natureza inferida a partir das evidências indicadas.",
  nat="Inferida", rel=["d01_res4893", "d01_portal"])

I("d01_precedencia", D, "Documento inteiro (cláusula de precedência não localizada)", "p. 1–6 · demais documentos D02–D04",
  'Não localizado. Trecho que gera a necessidade: "As especificações técnicas detalhadas constam do Anexo I — Especificação Técnica."',
  "Lacuna", "Jurídico/Contratual",
  "Nenhum dos documentos define a ordem de precedência entre RFP, Anexo I, apresentação do workshop e respostas do Q&A. Há divergências que dependem dessa regra: prazo de transição ({d02_trans60}), base de usuários ({d03_usuarios}, {d03_subsidiarias}, {d04_qa5}), localização dos dados ({d02_siem_nuvem}), retenção de logs ({d02_ret5}) e composição da Nota Técnica ({d04_pesos}). Não se presume que o Q&A, por ser mais recente, prevaleça.",
  s=4, p=3, ob="Informativo",
  imp="Sem regra de precedência, o proponente não sabe qual versão das exigências conflitantes será cobrada no contrato; afeta preço, prazo e escopo de vários itens.",
  fw=CC, ctl="interpretação dos contratos e integração de documentos contratuais (identificador a confirmar)", assoc="Correlata",
  rel=["d02_trans60", "d03_usuarios", "d03_subsidiarias", "d04_qa5", "d02_siem_nuvem", "d02_ret5", "d04_pesos"],
  acao="Esclarecer no Q&A",
  perg="Qual a ordem de precedência entre a RFP, o Anexo I, a apresentação do workshop de 22/10/2026 e as respostas do Q&A, em caso de divergência? As respostas do Q&A e o conteúdo da apresentação (inclusive notas) integram o contrato?",
  resp="Jurídico")

I("d01_res4893", D, "1. APRESENTAÇÃO, item 1.2", "p. 2 (impressa: 1)",
  '"sujeito à Resolução CMN nº 4.893/2021, que dispõe sobre a política de segurança cibernética e sobre os requisitos para a contratação de serviços de processamento e armazenamento de dados e de computação em nuvem"',
  "Requisito implícito", "Regulatório/Compliance",
  "Ao citar a Resolução CMN nº 4.893/2021 e prever SIEM em nuvem (Anexo I, item 1.2), o Banco precisará que o contrato e a operação do proponente atendam aos requisitos da norma para contratação de processamento, armazenamento e nuvem (cláusulas contratuais, acesso do regulador, comunicação de incidentes, entre outros). O RFP não detalha quais requisitos serão repassados ao proponente; o questionário pede declaração de atendimento (QT-04, {d04_qt04}).",
  s=3, p=3, ob="Mandatório", nat="Inferida",
  imp="Cláusulas regulatórias adicionais na minuta e custos de conformidade (evidências, auditorias, acesso do regulador) a precificar.",
  fw=R4893, ctl="requisitos para contratação de serviços de processamento, armazenamento de dados e computação em nuvem (identificador a confirmar)",
  assoc="Direta", rel=["d04_qt04", "d02_siem_fornecer"], acao="Esclarecer no Q&A",
  perg="Quais obrigações decorrentes da Resolução CMN nº 4.893/2021 serão atribuídas à Contratada (cláusulas contratuais obrigatórias, acesso do Banco Central, comunicação de incidentes, auditorias)? Haverá minuta contratual com essas cláusulas?",
  resp="Compliance")

I("d01_obj_soc", D, "2. OBJETO, item 2.1", "p. 2 (impressa: 1)",
  '"prestação de serviços gerenciados de Centro de Operações de Segurança (SOC), em regime 24x7x365"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber / Operação/Serviços",
  "Escopo principal: SOC gerenciado em operação contínua (24 horas, 7 dias, 365 dias). Exige escala de turnos ininterrupta. Repetido no Anexo I, item 1.1 ({d02_monit}).",
  s=3, p=3, ob="Mandatório",
  imp="Define a escala de equipe 24x7 e o principal componente de custo do serviço.",
  fw=NIST, ctl="DE.CM — Monitoramento contínuo", assoc="Direta", rel=["d02_monit"], acao="Precificar",
  resp="Delivery/Operação")

I("d01_obj_iam", D, "2. OBJETO, item 2.1", "p. 2 (impressa: 1)",
  '"gestão de identidades e acessos (IAM), abrangendo aproximadamente 4.500 colaboradores"',
  "Dado de dimensionamento", "Segurança da Informação/Cyber / Comercial/Preço",
  "Base de usuários declarada no RFP: cerca de 4.500 colaboradores. Diverge da apresentação (6.200 usuários ativos — {d03_usuarios}; mais ~900 usuários das subsidiárias — {d03_subsidiarias}) e foi substituída no Q&A 5 por 5.000 usuários ({d04_qa5}). O termo 'aproximadamente' não fixa tolerância.",
  s=3, p=3, ob="Informativo",
  imp="Base de usuários é o principal direcionador de preço do IAM; valor original já alterado pelo Q&A.",
  fw=NA, assoc="Não aplicável", rel=["d04_qa5", "d03_usuarios", "d03_subsidiarias"], vig="Alterado",
  acao="Esclarecer no Q&A", resp="Pricing/Financeiro")

I("d01_crono_workshop", D, "3. CRONOGRAMA DO PROCESSO, item 3.1", "p. 2 (impressa: 1)",
  '"Workshop de apresentação do ambiente 22/10/2026"', "Prazo / marco", "Administrativo do processo",
  "Workshop com proponentes em 22/10/2026. O material apresentado (D03) traz dados e exigências que não constam do RFP, inclusive em notas do apresentador.",
  s=2, p=3, ob="Informativo",
  imp="Ausência no workshop priva o proponente de informações de dimensionamento e de escopo.",
  fw=NA, assoc="Não aplicável", rel=["d03_inventario"], acao="Atender", resp="Bid Manager")

I("d01_crono_perguntas", D, "3. CRONOGRAMA DO PROCESSO, item 3.1", "p. 2 (impressa: 1)",
  '"Prazo final para envio de perguntas 05/11/2026"', "Prazo / marco", "Administrativo do processo",
  "Prazo único para perguntas. Todas as perguntas de esclarecimento desta matriz precisam ser enviadas até 05/11/2026; o RFP não prevê segunda rodada de perguntas.",
  s=3, p=3, ob="Mandatório",
  imp="Perguntas não enviadas no prazo deixam contradições e lacunas sem resposta, forçando premissas na proposta.",
  fw=NA, assoc="Não aplicável", acao="Atender", resp="Bid Manager")

I("d01_crono_respostas", D, "3. CRONOGRAMA DO PROCESSO, item 3.1", "p. 2 (impressa: 1)",
  '"Divulgação das respostas 12/11/2026"', "Prazo / marco", "Administrativo do processo",
  "Respostas aos esclarecimentos previstas para 12/11/2026, data do Q&A Rodada 1 (D04). Restam 15 dias corridos até a nova data de entrega (27/11/2026, {d04_qa1}).",
  s=1, p=3, imp="Janela curta para incorporar as respostas na proposta.", fw=NA, assoc="Não aplicável",
  rel=["d04_qa1"], resp="Bid Manager")

I("d01_crono_entrega", D, "3. CRONOGRAMA DO PROCESSO, item 3.1", "p. 2 (impressa: 1)",
  '"Entrega das propostas 20/11/2026, até as 18h"', "Prazo / marco", "Administrativo do processo",
  "Data original de entrega, prorrogada para 27/11/2026, até as 18h, pelo Q&A 1 ({d04_qa1}). Probabilidade 2: a data está clara e foi prorrogada; o impacto (proposta não recebida) só ocorre por falha interna de planejamento.",
  s=5, p=2, ob="Mandatório",
  imp="Proposta entregue fora do prazo não é considerada.", fw=NA, assoc="Não aplicável", rel=["d04_qa1"],
  vig="Alterado", acao="Atender", resp="Bid Manager")

I("d01_crono_inicio", D, "3. CRONOGRAMA DO PROCESSO, item 3.1", "p. 2 (impressa: 1)",
  '"Início previsto dos serviços 01/02/2027"', "Prazo / marco", "Transição/Implantação",
  "Início dos serviços em 01/02/2027, dia seguinte ao fim do contrato do SIEM legado (31/01/2027, sem prorrogação — {d03_siem_legado}). A data de assinatura do contrato não é informada ({d01_assinatura}), de modo que não se sabe se a transição (30 ou 60 dias) cabe antes do início.",
  s=3, p=3, ob="Informativo",
  imp="Data rígida de entrada em operação; condiciona o plano de transição e a mobilização da equipe.",
  fw=NA, assoc="Não aplicável", rel=["d03_siem_legado", "d01_assinatura", "d03_risco_transicao"],
  acao="Registrar premissa na proposta", resp="Delivery/Operação")

I("d01_transicao30", D, "3. CRONOGRAMA DO PROCESSO, item 3.2", "p. 2 (impressa: 1)",
  '"A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato."',
  "Prazo / marco", "Transição/Implantação",
  "Prazo de transição de 30 dias corridos. Contraditório com o Anexo I, item 4.1, que fixa 60 dias ({d02_trans60}). Para SOC com fornecimento de SIEM, integração de ativos e migração de logs, 30 dias é prazo curto.",
  s=4, p=3, ob="Mandatório",
  imp="Define esforço de mobilização, equipe de transição e risco de multa por atraso; diferença de 30 dias altera custo e cronograma.",
  fw=ITIL, ctl="práticas de transição de serviço (identificador a confirmar)", assoc="Boa prática",
  rel=["d02_trans60", "d03_risco_transicao"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  resp="Delivery/Operação")

I("d01_assinatura", D, "3. CRONOGRAMA DO PROCESSO, item 3.1 e 3.2", "p. 2 (impressa: 1)",
  'Não localizado. Trecho que gera a necessidade: "deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato"',
  "Lacuna", "Transição/Implantação",
  "O cronograma não informa a data prevista de assinatura do contrato, que é o marco inicial da transição. Sem ela não é possível verificar se a transição termina antes do início dos serviços (01/02/2027) e do fim do SIEM legado (31/01/2027).",
  s=3, p=3, ob="Informativo",
  imp="Impede planejar a transição e dimensionar a equipe de mobilização; pode comprimir o prazo real.",
  fw=NA, assoc="Não aplicável", rel=["d01_crono_inicio", "d03_risco_transicao"], acao="Esclarecer no Q&A",
  perg="Qual a data prevista para assinatura do contrato? A transição deve estar concluída até 01/02/2027 independentemente da data de assinatura?",
  resp="Bid Manager")

I("d01_idioma", D, "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA, item 4.1", "p. 3 (impressa: 2)",
  '"A proposta deverá ser redigida em língua portuguesa"', "Instrução de resposta", "Administrativo do processo",
  "Proposta em português. Não há regra sobre documentos de terceiros em outro idioma (certificados, atestados, datasheets).",
  s=2, p=3, ob="Mandatório", imp="Exige tradução de materiais e possivelmente de certificados/atestados emitidos em outro idioma.",
  fw=NA, assoc="Não aplicável", acao="Atender",
  perg="Certificados, atestados e catálogos técnicos emitidos em outro idioma precisam de tradução (simples ou juramentada)?",
  resp="Bid Manager")

I("d01_portal", D, "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA, item 4.1", "p. 3 (impressa: 2)",
  '"enviada exclusivamente pelo portal de fornecedores do Banco"', "Instrução de resposta", "Administrativo do processo",
  "Canal único de envio. O RFP não informa endereço do portal, exigência de cadastro prévio, prazo de homologação nem limite de tamanho de arquivo.",
  s=3, p=3, ob="Mandatório", imp="Proposta enviada por outro meio ou não carregada a tempo no portal não é recebida.",
  fw=NA, assoc="Não aplicável", acao="Esclarecer no Q&A",
  perg="Qual o endereço do portal de fornecedores, há cadastro ou homologação prévia exigida (e com que antecedência) e qual o limite de tamanho e formato dos arquivos?",
  resp="Bid Manager")

I("d01_paginas", D, "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA, item 4.2", "p. 3 (impressa: 2)",
  '"A proposta técnica deverá ter no máximo 40 (quarenta) páginas, excluídos os anexos."',
  "Instrução de resposta", "Administrativo do processo",
  "Limite de 40 páginas para a proposta técnica. Não define formato de página, fonte, nem a consequência do excesso (desclassificação ou desconsideração das páginas excedentes), nem o que pode ir para anexos.",
  s=3, p=3, ob="Mandatório", imp="Excesso pode levar à desconsideração de conteúdo pontuável; limita a resposta aos quatro critérios técnicos.",
  fw=NA, assoc="Não aplicável", acao="Esclarecer no Q&A",
  perg="Qual a consequência de exceder 40 páginas? Há formato mínimo de fonte/página? Conteúdo pontuável (ex.: currículos, plano de transição) pode ser apresentado em anexo?",
  resp="Bid Manager")

I("d01_instr_anexo4", D, "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA, item 4.3", "p. 3 (impressa: 2)",
  '"A proposta comercial deverá ser apresentada conforme a planilha modelo do Anexo IV — Planilha de Preços."',
  "Instrução de resposta", "Comercial/Preço",
  "Proposta comercial obrigatoriamente no modelo do Anexo IV, que não foi fornecido no pacote ({d01_lac_anexo4}).",
  s=3, p=3, ob="Mandatório", imp="Sem o modelo, não é possível estruturar o preço na forma exigida.",
  fw=NA, assoc="Não aplicável", rel=["d01_lac_anexo4"], acao="Atender", resp="Pricing/Financeiro")

I("d01_lac_anexo4", D, "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA, item 4.3", "p. 3 (impressa: 2)",
  'Não localizado. Trecho que gera a necessidade: "conforme a planilha modelo do Anexo IV — Planilha de Preços"',
  "Lacuna", "Comercial/Preço",
  "O Anexo IV é citado pelo cliente e não está no pacote recebido nem na lista de documentos do usuário. Sem ele, não se conhecem a estrutura de itens de preço, unidades de medida, quantitativos de referência nem a base para a Nota de Preço.",
  s=4, p=3, ob="Mandatório",
  imp="Impede montar a proposta comercial no formato exigido e pode esconder quantitativos que alteram o preço.",
  fw=NA, assoc="Não aplicável", rel=["d01_instr_anexo4", "d01_lac_preco"], acao="Esclarecer no Q&A",
  perg="Solicitamos o envio do Anexo IV — Planilha de Preços, que é citado no item 4.3 da RFP e não consta do pacote disponibilizado.",
  resp="Pricing/Financeiro", pend="Anexo IV — Planilha de Preços citado pelo cliente e não fornecido")

I("d01_lac_anexo2", D, "Documento inteiro (numeração dos anexos)", "p. 3 (impressa: 2) e p. 6 (impressa: 5) (OCR)",
  'Não localizado. Trechos que geram a necessidade: "planilha modelo do Anexo IV — Planilha de Preços" [...] "ANEXO III — DECLARAÇÃO DE LOCALIZAÇÃO DE DADOS"',
  "Lacuna", "Administrativo do processo",
  "O pacote traz os Anexos I, III (na p. 6 do RFP) e cita o IV, mas nenhum documento menciona um Anexo II. A numeração sugere a existência de um anexo não citado nem fornecido (por exemplo, minuta contratual ou modelo de proposta). Inferência a partir da sequência numérica.",
  s=2, p=3, ob="Informativo", nat="Inferida",
  imp="Possível documento faltante com exigências não conhecidas (ex.: minuta contratual).",
  fw=NA, assoc="Não aplicável", rel=["d01_lac_anexo4"], acao="Esclarecer no Q&A",
  perg="Existe um Anexo II desta RFP? Em caso positivo, solicitamos seu envio; há minuta contratual a ser disponibilizada?",
  resp="Bid Manager", pend="possível Anexo II não citado nem fornecido")

I("d01_questionario", D, "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA, item 4.4", "p. 3 (impressa: 2)",
  '"O questionário técnico (planilha anexa) deverá ser integralmente preenchido."',
  "Instrução de resposta", "Administrativo do processo",
  "Preenchimento integral do questionário técnico (D04). A planilha acrescenta que questionários incompletos são desclassificados ({d04_instr_elim}) e contém aba oculta com pesos e regra de dedução de pontos ({d04_pesos}), não mencionadas no RFP.",
  s=3, p=3, ob="Mandatório", imp="Questionário incompleto leva à desclassificação (conforme D04).",
  fw=NA, assoc="Não aplicável", rel=["d04_instr_elim", "d04_pesos"], acao="Atender", resp="Pré-venda/Arquitetura")

I("d01_hab_iso", D, "5. CRITÉRIOS DE HABILITAÇÃO, item 5.1 a", "p. 3 (impressa: 2)",
  '"certificado ISO/IEC 27001 vigente, emitido por organismo acreditado, cujo escopo inclua os serviços de SOC"',
  "Critério eliminatório / de habilitação", "Segurança da Informação/Cyber",
  "Habilitação exige certificado ISO/IEC 27001 vigente, de organismo acreditado, com escopo que inclua SOC. Não exige que o escopo inclua IAM. Repetido como QT-01 ({d04_qt01}). Probabilidade 5: o texto determina a inabilitação ('Serão inabilitados') de quem não apresentar o certificado, sem margem de interpretação.",
  s=5, p=5, ob="Mandatório",
  imp="Não apresentação leva à inabilitação.", fw=ISO, ctl="Certificação do SGSI (cláusulas 4 a 10) com escopo incluindo SOC",
  assoc="Direta", rel=["d04_qt01"], acao="Avaliar Go/No-Go",
  perg="O certificado pode ser de empresa do mesmo grupo econômico do proponente? Certificado com escopo que cite o SOC, mas não o IAM, atende?",
  resp="Compliance")

I("d01_hab_atestados", D, "5. CRITÉRIOS DE HABILITAÇÃO, item 5.1 b", "p. 3 (impressa: 2)",
  '"no mínimo 3 (três) atestados de capacidade técnica de prestação de serviços de SOC para instituições financeiras, com ambiente de no mínimo 2.000 usuários"',
  "Critério eliminatório / de habilitação", "Segurança da Informação/Cyber / Administrativo do processo",
  "Três atestados de SOC para instituições financeiras, cada um (presumivelmente) com ambiente de ao menos 2.000 usuários. Não está claro se os 2.000 usuários valem por atestado ou somados, se contratos em andamento valem e se atestados de IAM são exigidos. Probabilidade 5: inabilitação expressa para quem não apresentar.",
  s=5, p=5, ob="Mandatório", imp="Não apresentação leva à inabilitação.", fw=NA, assoc="Não aplicável",
  acao="Avaliar Go/No-Go",
  perg="O mínimo de 2.000 usuários se aplica a cada atestado ou ao somatório? Atestados de contratos ainda vigentes são aceitos? Cooperativas, seguradoras e instituições de pagamento contam como instituições financeiras?",
  resp="Bid Manager")

I("d01_hab_soc_br", D, "5. CRITÉRIOS DE HABILITAÇÃO, item 5.1 c", "p. 3 (impressa: 2)",
  '"comprovação de que o SOC está localizado em território nacional"', "Critério eliminatório / de habilitação",
  "Segurança da Informação/Cyber / Regulatório/Compliance",
  "SOC obrigatoriamente no Brasil, confirmado no Q&A 2 ({d04_qa2}). O RFP não define o meio de comprovação. A exigência trata da localização do SOC (equipe/operação), não dos dados; a localização dos dados é tratada no Anexo III ({d01_anx3_dados}). Probabilidade 5: inabilitação expressa.",
  s=5, p=5, ob="Mandatório", imp="Não comprovação leva à inabilitação; impede operação offshore.",
  fw=NA, assoc="Não aplicável", rel=["d04_qa2", "d01_anx3_dados", "d04_qa6"], acao="Avaliar Go/No-Go",
  perg="Qual documento será aceito como comprovação da localização do SOC em território nacional (endereço, contrato de locação, visita técnica)?",
  resp="Delivery/Operação")

I("d01_hab_equipe", D, "5. CRITÉRIOS DE HABILITAÇÃO, item 5.2", "p. 3 (impressa: 2)",
  '"O proponente deverá possuir equipe técnica devidamente certificada."', "Ambiguidade", "Pessoas/Equipe",
  "Item dentro de 'Critérios de habilitação', mas fora da lista do 5.1 ('Serão inabilitados'). Não define quais certificações, quantos profissionais, nem a forma de comprovação, e não diz se a falta inabilita. O Anexo I exige apenas CISSP do coordenador ({d02_cissp}); o QT-06 repete a exigência genérica ({d04_qt06}). Tipo alternativo: Critério eliminatório / de habilitação.",
  s=4, p=3, ob="Mandatório",
  imp="Se interpretado como critério de habilitação com certificações específicas, pode inabilitar; afeta composição e custo da equipe.",
  fw=ISO, ctl="Cláusula 7.2 — Competência", assoc="Correlata", rel=["d02_cissp", "d04_qt06", "d01_crit_equipe"],
  vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O item 5.2 é critério de habilitação? Quais certificações, em que quantidade e para quais funções são exigidas, e como devem ser comprovadas na proposta?",
  resp="RH/Staffing")

I("d01_aval_pesos", D, "6. CRITÉRIOS DE AVALIAÇÃO, item 6.1", "p. 4 (impressa: 3)",
  '"A nota final será composta pela Nota Técnica (peso de 60%) e pela Nota de Preço (peso de 40%)."',
  "Critério de avaliação / pontuação", "Administrativo do processo / Comercial/Preço",
  "Técnica e preço com pesos 60/40. Combinado com a nota de corte técnica (70%), o processo privilegia a qualidade técnica.",
  s=3, p=3, ob="Informativo", imp="Orienta a estratégia de preço versus investimento técnico.", fw=NA,
  assoc="Não aplicável", rel=["d01_lac_preco"], resp="Bid Manager")

I("d01_crit_metodologia", D, "6. CRITÉRIOS DE AVALIAÇÃO, item 6.2", "p. 4 (impressa: 3)",
  '"Metodologia de operação do SOC 20"', "Critério de avaliação / pontuação", "Segurança da Informação/Cyber",
  "Critério de maior peso, empatado com equipe. Não há subcritérios nem escala de notas (o que vale 0, 10 ou 20 pontos).",
  s=3, p=3, ob="Informativo", imp="Concentra parte relevante da Nota Técnica; sem rubrica, a pontuação é subjetiva.",
  fw=NIST, ctl="DE (Detectar) e RS (Responder)", assoc="Correlata", rel=["d01_aval_soma"], acao="Esclarecer no Q&A",
  perg="Quais subcritérios e qual escala serão usados para atribuir a pontuação de cada critério da Nota Técnica?",
  resp="Pré-venda/Arquitetura")

I("d01_crit_equipe", D, "6. CRITÉRIOS DE AVALIAÇÃO, item 6.2", "p. 4 (impressa: 3)",
  '"Qualificação da equipe 20"', "Critério de avaliação / pontuação", "Pessoas/Equipe",
  "Critério de maior peso, empatado com metodologia. Não define se pontua certificações, experiência ou currículos nominais.",
  s=3, p=3, ob="Informativo", imp="Pode exigir apresentação de equipe nominal e certificações para pontuar.",
  fw=ISO, ctl="Cláusula 7.2 — Competência", assoc="Correlata", rel=["d01_hab_equipe", "d01_aval_soma"],
  acao="Esclarecer no Q&A", resp="RH/Staffing")

I("d01_crit_ferramentas", D, "6. CRITÉRIOS DE AVALIAÇÃO, item 6.2", "p. 4 (impressa: 3)",
  '"Ferramentas e tecnologia 15"', "Critério de avaliação / pontuação", "Técnico/Arquitetura",
  "Pontua ferramentas e tecnologia (SIEM a ser fornecido — {d02_siem_fornecer}; possivelmente SOAR, PAM e threat intelligence, que aparecem no questionário). Sem rubrica.",
  s=3, p=3, ob="Informativo", imp="Escolha de ferramentas afeta pontuação e preço.", fw=NA, assoc="Não aplicável",
  rel=["d02_siem_fornecer", "d01_aval_soma"], resp="Pré-venda/Arquitetura")

I("d01_crit_transicao", D, "6. CRITÉRIOS DE AVALIAÇÃO, item 6.2", "p. 4 (impressa: 3)",
  '"Plano de transição 10"', "Critério de avaliação / pontuação", "Transição/Implantação",
  "Plano de transição pontua 10. O prazo de referência é contraditório (30 × 60 dias — {d02_trans60}).",
  s=3, p=3, ob="Informativo", imp="Plano baseado no prazo errado pode perder pontos ou ser inexequível.",
  fw=ITIL, ctl="práticas de transição de serviço (identificador a confirmar)", assoc="Boa prática",
  rel=["d02_trans60", "d01_aval_soma"], resp="Delivery/Operação")

I("d01_aval_soma", D, "6. CRITÉRIOS DE AVALIAÇÃO, item 6.2", "A: p. 4 (impressa: 3), item 6.2 · B: p. 4 (impressa: 3), tabela do item 6.2",
  'A: "A Nota Técnica, de no máximo 60 (sessenta) pontos" · B: "Metodologia de operação do SOC 20" [...] "Qualificação da equipe 20" [...] "Ferramentas e tecnologia 15" [...] "Plano de transição 10"',
  "Contradição", "Administrativo do processo",
  "A Nota Técnica tem máximo declarado de 60 pontos, mas a soma das pontuações máximas da tabela é 65 (20+20+15+10). Não se sabe se há normalização, erro em algum peso ou se a nota é limitada a 60. Afeta também o corte de 70% (42 ou 45,5 pontos — {d01_aval_corte}) e a interação com a dedução de pontos da aba oculta 'Pesos' ({d04_pesos}).",
  s=4, p=3, ob="Informativo",
  imp="Incerteza sobre o peso relativo dos critérios e sobre a nota mínima para não ser desclassificado.",
  fw=NA, assoc="Não aplicável",
  rel=["d01_crit_metodologia", "d01_crit_equipe", "d01_crit_ferramentas", "d01_crit_transicao", "d01_aval_corte", "d04_pesos"],
  vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A soma das pontuações máximas da tabela do item 6.2 é 65, mas a Nota Técnica tem máximo de 60 pontos. Qual a pontuação correta de cada critério, ou como será feita a normalização?",
  resp="Bid Manager")

I("d01_aval_corte", D, "6. CRITÉRIOS DE AVALIAÇÃO, item 6.3", "p. 4 (impressa: 3)",
  '"Serão desclassificadas as propostas com Nota Técnica inferior a 70% (setenta por cento) da pontuação máxima."',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Nota de corte técnica de 70%. A base é incerta: 42 pontos (70% de 60) ou 45,5 (70% de 65), conforme {d01_aval_soma}; e a dedução de 2 pontos por 'Não atende' em requisitos não obrigatórios ({d04_pesos}) pode empurrar a nota abaixo do corte.",
  s=5, p=3, ob="Mandatório", imp="Nota abaixo do corte desclassifica a proposta.", fw=NA, assoc="Não aplicável",
  rel=["d01_aval_soma", "d04_pesos"], acao="Esclarecer no Q&A",
  perg="A nota mínima de 70% será calculada sobre 60 ou 65 pontos? As deduções previstas na aba 'Pesos' do questionário entram no cálculo dessa nota mínima?",
  resp="Bid Manager")

I("d01_lac_preco", D, "6. CRITÉRIOS DE AVALIAÇÃO, item 6.1", "p. 4 (impressa: 3)",
  'Não localizado. Trecho que gera a necessidade: "pela Nota de Preço (peso de 40%)"', "Lacuna", "Comercial/Preço",
  "O RFP não informa a fórmula da Nota de Preço (proporcional ao menor preço, faixa, desvio da média), nem o tratamento de preços inexequíveis, nem qual valor (mensal, global de 36 meses, com ou sem reajuste) será comparado.",
  s=4, p=3, ob="Informativo", imp="Impede simular a nota final e definir a estratégia de preço.",
  fw=NA, assoc="Não aplicável", rel=["d01_aval_pesos", "d01_lac_anexo4"], acao="Esclarecer no Q&A",
  perg="Qual a fórmula de cálculo da Nota de Preço, qual valor será comparado (mensal ou global) e há critério de inexequibilidade?",
  resp="Pricing/Financeiro")

I("d01_empate", D, "6. CRITÉRIOS DE AVALIAÇÃO, item 6.4", "p. 4 (impressa: 3)",
  '"Em caso de empate na nota final, prevalecerá a proposta de menor preço."', "Critério de avaliação / pontuação",
  "Administrativo do processo", "Critério de desempate pelo menor preço.", s=2, p=3, ob="Informativo",
  imp="Reforça peso do preço em cenários de notas próximas.", fw=NA, assoc="Não aplicável", resp="Pricing/Financeiro")

I("d01_vigencia", D, "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS, item 7.1", "p. 5 (impressa: 4)",
  '"O contrato terá vigência de 36 (trinta e seis) meses, prorrogável por iguais períodos mediante acordo entre as partes."',
  "Obrigação contratual", "Jurídico/Contratual / Comercial/Preço",
  "Vigência de 36 meses, prorrogável por acordo. Base para amortização de setup, licenças de SIEM e transição.",
  s=3, p=3, ob="Informativo", imp="Define o horizonte de amortização dos investimentos iniciais.", fw=NA,
  assoc="Não aplicável", acao="Precificar", resp="Pricing/Financeiro")

I("d01_reajuste", D, "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS, item 7.2", "p. 5 (impressa: 4)",
  '"Os preços serão reajustados anualmente pela variação do IPCA."', "Obrigação contratual", "Financeiro",
  "Reajuste anual pelo IPCA. Não define a data-base (proposta ou assinatura) nem trata de custos em moeda estrangeira (licenças de SIEM/nuvem), que não acompanham o IPCA.",
  s=2, p=3, ob="Informativo", imp="Exposição cambial de licenças e nuvem não coberta pelo índice.", fw=NA,
  assoc="Não aplicável", acao="Registrar premissa na proposta",
  perg="Qual a data-base do reajuste anual pelo IPCA (data da proposta ou da assinatura)?", resp="Pricing/Financeiro")

I("d01_pagamento", D, "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS, item 7.3", "p. 5 (impressa: 4)",
  '"O pagamento será efetuado em até 60 (sessenta) dias após o aceite da nota fiscal."', "Obrigação contratual",
  "Financeiro",
  "Prazo de pagamento de até 60 dias após o aceite da nota fiscal, sem prazo definido para o próprio aceite. Prazo efetivo pode superar 60 dias.",
  s=3, p=3, ob="Informativo", imp="Custo financeiro de capital de giro a incluir no preço.", fw=NA,
  assoc="Não aplicável", acao="Precificar",
  perg="Qual o prazo do Banco para o aceite da nota fiscal após sua emissão?", resp="Pricing/Financeiro")

I("d01_multa", D, "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS, item 7.4", "p. 5 (impressa: 4)",
  '"O descumprimento de qualquer nível de serviço (SLA) previsto no Anexo I sujeitará a Contratada a multa de 10% (dez por cento) do valor mensal do contrato, por ocorrência."',
  "Penalidade / multa / glosa", "Jurídico/Contratual / Financeiro",
  "Multa de 10% do valor mensal por ocorrência de descumprimento de qualquer SLA, sem limite, sem gradação por gravidade e sem período de carência na transição. Dez ocorrências no mês consomem 100% da fatura. Probabilidade 4: a multa incide automaticamente 'por ocorrência' e o cliente, perguntado sobre teto, manteve as condições (Q&A 4 — {d04_qa4}).",
  s=5, p=4, ob="Mandatório",
  imp="Exposição financeira sem teto, potencialmente superior ao faturamento mensal.",
  fw=ITIL, ctl="Gerenciamento de nível de serviço (identificador a confirmar)", assoc="Correlata",
  rel=["d04_qa4", "d02_sla15", "d02_disp", "d02_relatorio", "d04_risco_financeiro"], acao="Propor exceção/ressalva",
  perg="Será aceita limitação do total de multas (por exemplo, a um percentual do valor mensal) e gradação por gravidade do descumprimento, com carência durante a transição?",
  resp="Jurídico")

I("d01_resp_ilimitada", D, "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS, item 7.5", "p. 5 (impressa: 4)",
  '"A Contratada responderá de forma integral e ilimitada por quaisquer danos decorrentes de incidentes de segurança ocorridos no ambiente do Contratante."',
  "Obrigação contratual", "Jurídico/Contratual",
  "Responsabilidade integral e ilimitada por quaisquer danos de incidentes no ambiente do Contratante, independentemente de culpa ou nexo com o serviço prestado (o SOC detecta e responde; não controla todo o ambiente). Não há exclusão de danos indiretos nem teto.",
  s=5, p=3, ob="Mandatório",
  imp="Exposição jurídica e financeira ilimitada; pode inviabilizar seguro e a participação.",
  fw=CC, ctl="responsabilidade civil contratual e limitação de indenização (identificador a confirmar)",
  assoc="Correlata", rel=["d01_seguro", "d04_risco_financeiro"], acao="Avaliar Go/No-Go",
  perg="Será aceita limitação de responsabilidade (por exemplo, ao valor anual do contrato), restrita a danos diretos causados por culpa comprovada da Contratada?",
  resp="Jurídico")

I("d01_seguro", D, "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS, item 7.6", "p. 5 (impressa: 4)",
  '"A Contratada deverá manter seguro de responsabilidade civil cibernética em valor compatível com os riscos do contrato."',
  "Obrigação contratual", "Jurídico/Contratual / Financeiro",
  "Seguro cyber obrigatório com valor indefinido ('compatível com os riscos'). Com responsabilidade ilimitada ({d01_resp_ilimitada}), não há valor objetivamente compatível. Item também ambíguo quanto a valor mínimo e momento de comprovação.",
  s=3, p=3, ob="Mandatório", imp="Custo de prêmio a precificar; risco de discordância sobre a suficiência da apólice.",
  fw=NA, assoc="Não aplicável", rel=["d01_resp_ilimitada"], acao="Esclarecer no Q&A",
  perg="Qual o valor mínimo segurado exigido para o seguro de responsabilidade civil cibernética e quando a apólice deve ser apresentada?",
  resp="Jurídico")

I("d01_subcontratacao", D, "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS, item 7.7", "p. 5 (impressa: 4)",
  '"É vedada a subcontratação, total ou parcial, do objeto deste contrato."', "Restrição", "Jurídico/Contratual",
  "Vedação total de subcontratação. Conflita com o fornecimento de SIEM em nuvem pública ({d02_siem_subcontr}) e restringe o uso de parceiros (ex.: threat intelligence, resposta a incidentes especializada, profissionais PJ).",
  s=3, p=3, ob="Mandatório", imp="Limita o modelo de entrega e o uso de parceiros e provedores de nuvem.",
  fw=ISO, ctl="A.5.20 — Tratamento da segurança da informação nos acordos com fornecedores", assoc="Correlata",
  rel=["d02_siem_subcontr"], acao="Esclarecer no Q&A", resp="Jurídico")

I("d01_confidencialidade", D, "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS, item 7.8", "p. 5 (impressa: 4)",
  '"As obrigações de confidencialidade vigorarão por 5 (cinco) anos após o término do contrato."',
  "Obrigação contratual", "Jurídico/Contratual", "Confidencialidade por 5 anos após o término.",
  s=2, p=3, ob="Mandatório", imp="Obrigação pós-contratual de baixo custo.", fw=ISO,
  ctl="A.6.6 — Acordos de confidencialidade ou não divulgação", assoc="Direta", acao="Atender", resp="Jurídico")

I("d01_anx3_entrega", D, "ANEXO III — DECLARAÇÃO DE LOCALIZAÇÃO DE DADOS", "p. 6 (impressa: 5) (OCR)",
  '"Esta declaração deverá ser entregue assinada pelo representante legal do proponente junto com a proposta, sob pena de inabilitação."',
  "Critério eliminatório / de habilitação", "Regulatório/Compliance / Administrativo do processo",
  "Critério eliminatório que está apenas na página escaneada (sem texto extraível) e não aparece na lista do item 5.1. Exige declaração assinada pelo representante legal junto com a proposta. Probabilidade 5: o próprio texto determina a inabilitação ('sob pena de inabilitação').",
  s=5, p=5, ob="Mandatório", imp="Ausência da declaração assinada leva à inabilitação.", fw=NA,
  assoc="Não aplicável", rel=["d01_anx3_dados", "d01_inventario"], acao="Atender", resp="Bid Manager")

I("d01_anx3_dados", D, "ANEXO III — DECLARAÇÃO DE LOCALIZAÇÃO DE DADOS", "p. 6 (impressa: 5) (OCR)",
  '"todos os dados do Banco Horizonte Fictício S.A., incluindo os registros (logs) de segurança, serão armazenados e processados exclusivamente em território nacional, durante toda a vigência do contrato"',
  "Restrição", "Privacidade/Proteção de Dados / Infraestrutura/Cloud",
  "Restrição de residência de dados: todos os dados, inclusive logs, armazenados e processados só no Brasil. Contradiz o Anexo I, item 1.2 (nuvem em 'região de livre escolha' — {d02_siem_nuvem}). Também alcança backups, réplicas de DR e processamento por ferramentas SaaS (ex.: threat intelligence, análise em nuvem). O prazo ('durante toda a vigência') não cobre a retenção de 5 anos ({d02_ret5}), que pode ultrapassar o contrato.",
  s=4, p=3, ob="Mandatório",
  imp="Restringe arquitetura e fornecedores de SIEM/nuvem; serviços SaaS globais podem ficar inviáveis.",
  fw=LGPD, ctl="Art. 33 — transferência internacional de dados", assoc="Correlata",
  rel=["d02_siem_nuvem", "d02_ret5", "d01_hab_soc_br"], acao="Atender",
  perg="A restrição de armazenamento e processamento exclusivamente em território nacional se aplica também a metadados, telemetria enviada a fabricantes de ferramentas e a serviços de threat intelligence? Como fica a guarda dos logs após o fim do contrato?",
  resp="Pré-venda/Arquitetura")

# =====================================================================================
# D02 — Anexo_I_Especificacao_Tecnica.docx
# =====================================================================================
D = "D02"
I("d02_inventario", D, "Documento inteiro", "§ Anexo I — Especificação Técnica a § 6 (22 parágrafos)",
  '"RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Versão 1.0 — 15/10/2026"', "Registro de cobertura",
  "Administrativo do processo",
  "Inventário: Word com 6 seções numeradas, 22 parágrafos, sem tabelas, sem marcas de revisão, comentários ou texto oculto. Leitura integral. Localizador por seção/item (Word sem paginação fixa).")

I("d02_monit", D, "§ 1. SERVIÇOS DE SOC, item 1.1", "§ 1. SERVIÇOS DE SOC, item 1.1",
  '"O proponente deverá prestar serviço de monitoramento contínuo de eventos de segurança, em regime 24x7x365."',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Repete o objeto do RFP, item 2.1 ({d01_obj_soc}).", s=3, p=3, ob="Mandatório",
  imp="Equipe em turnos ininterruptos.", fw=ISO, ctl="A.8.16 — Atividades de monitoramento", assoc="Direta",
  rel=["d01_obj_soc"], vig="Duplicado", acao="Atender", resp="Delivery/Operação")

I("d02_siem_fornecer", D, "§ 1. SERVIÇOS DE SOC, item 1.2", "§ 1. SERVIÇOS DE SOC, item 1.2",
  '"O proponente deverá fornecer a solução de SIEM"', "Requisito funcional / de serviço", "Técnico/Arquitetura / Comercial/Preço",
  "O proponente fornece o SIEM (licença, infraestrutura e operação). O custo do SIEM depende da volumetria (EPS/GB por dia), que o cliente se recusou a informar ({d04_qa3}).",
  s=4, p=3, ob="Mandatório",
  imp="Maior componente de custo variável do SOC; sem volumetria, o preço do SIEM fica sem base.",
  fw=ISO, ctl="A.8.15 — Registro de logs", assoc="Correlata", rel=["d04_qa3", "d03_migracao"], acao="Precificar",
  resp="Pré-venda/Arquitetura")

I("d02_siem_nuvem", D, "§ 1. SERVIÇOS DE SOC, item 1.2", "A: D02 § 1. SERVIÇOS DE SOC, item 1.2 · B: D01 p. 6 (impressa: 5) (OCR), Anexo III",
  'A: "podendo esta ser disponibilizada em nuvem pública, em região de livre escolha do proponente" · B: "serão armazenados e processados exclusivamente em território nacional"',
  "Contradição", "Infraestrutura/Cloud / Privacidade/Proteção de Dados",
  "O Anexo I permite SIEM em nuvem pública em qualquer região, mas a declaração do Anexo III (eliminatória) exige armazenamento e processamento de todos os dados, inclusive logs, exclusivamente no Brasil. O Q&A 2 ({d04_qa2}) confirma apenas a localização do SOC, não a dos dados. Assinar a declaração e usar região estrangeira seria declaração falsa.",
  s=4, p=3, ob="Mandatório",
  imp="A escolha de região/fornecedor de SIEM altera custo (regiões nacionais costumam ter preço diferente) e pode gerar inabilitação ou descumprimento contratual.",
  fw=ISO, ctl="A.5.23 — Segurança da informação para uso de serviços em nuvem", assoc="Direta",
  rel=["d01_anx3_dados", "d01_anx3_entrega", "d04_qa2", "d01_res4893"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="O item 1.2 do Anexo I permite SIEM em nuvem pública em região de livre escolha, mas o Anexo III exige armazenamento e processamento exclusivamente em território nacional. Confirmam que a nuvem deve estar em região localizada no Brasil, inclusive para backup e recuperação de desastres?",
  resp="Pré-venda/Arquitetura")

I("d02_siem_subcontr", D, "§ 1. SERVIÇOS DE SOC, item 1.2", "A: D02 § 1. SERVIÇOS DE SOC, item 1.2 · B: D01 p. 5 (impressa: 4), item 7.7",
  'A: "podendo esta ser disponibilizada em nuvem pública" · B: "É vedada a subcontratação, total ou parcial, do objeto deste contrato."',
  "Ambiguidade", "Jurídico/Contratual / Infraestrutura/Cloud",
  "Não está claro se o uso de provedor de nuvem pública ou de SIEM em modelo SaaS (serviço prestado por terceiro) configura subcontratação vedada pelo item 7.7. Interpretação restritiva inviabiliza a opção em nuvem prevista no próprio Anexo I e obriga SIEM em infraestrutura própria.",
  s=4, p=3, ob="Mandatório",
  imp="Diferença entre arquitetura em nuvem e on-premises, com impacto relevante em custo e prazo de implantação.",
  fw=ISO, ctl="A.5.21 — Gestão da segurança da informação na cadeia de suprimentos de TIC", assoc="Correlata",
  rel=["d01_subcontratacao"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O uso de provedor de nuvem pública, de SIEM em modelo SaaS e de licenças/serviços de fabricantes (ex.: threat intelligence) é considerado subcontratação vedada pelo item 7.7?",
  resp="Jurídico")

I("d02_ret12", D, "§ 1. SERVIÇOS DE SOC, item 1.3", "§ 1. SERVIÇOS DE SOC, item 1.3",
  '"Os registros (logs) de segurança deverão ser retidos por no mínimo 12 (doze) meses."',
  "Requisito não funcional", "Segurança da Informação/Cyber",
  "Retenção mínima de 12 meses. Conflita com a retenção de 5 anos do item 1.6 ({d02_ret5}); o QT-03 fala em 12 meses 'online' ({d04_qt03}).",
  s=3, p=3, ob="Mandatório", imp="Dimensiona armazenamento do SIEM.", fw=ISO, ctl="A.8.15 — Registro de logs",
  assoc="Direta", rel=["d02_ret5", "d04_qt03"], vig="Em esclarecimento", acao="Atender", resp="Pré-venda/Arquitetura")

I("d02_integracao", D, "§ 1. SERVIÇOS DE SOC, item 1.4", "§ 1. SERVIÇOS DE SOC, item 1.4",
  '"O SIEM deverá ser integrado a todos os ativos relevantes do Contratante."', "Ambiguidade",
  "Técnico/Arquitetura",
  "Não define quais ativos são 'relevantes', quem os classifica, nem o número de fontes. O ambiente informado tem 850 servidores, 2 data centers e 2 nuvens públicas ({d03_servidores}, {d03_nuvens}), e a volumetria de eventos não será informada ({d04_qa3}). Escopo aberto de integração.",
  s=4, p=3, ob="Mandatório",
  imp="Escopo de integração e de licenciamento indeterminado; risco de exigência de integrar qualquer ativo sem custo adicional.",
  fw=NIST, ctl="ID.AM — Gestão de ativos", assoc="Correlata", rel=["d04_qa3", "d03_servidores", "d03_nuvens"],
  vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Qual a lista ou quantidade e tipo de ativos considerados 'relevantes' (servidores, estações, rede, nuvem, aplicações) e quem define essa relação? Novos ativos ao longo do contrato serão remunerados?",
  resp="Pré-venda/Arquitetura")

I("d02_ir_resposta", D, "§ 1. SERVIÇOS DE SOC, item 1.5", "§ 1. SERVIÇOS DE SOC, item 1.5",
  '"O serviço deverá contemplar resposta a incidentes, incluindo contenção, erradicação"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Resposta a incidentes com contenção e erradicação (não apenas detecção). Não define se a atuação é remota ou presencial, se inclui forense, nem limite de horas/incidentes.",
  s=3, p=3, ob="Mandatório", imp="Esforço de resposta potencialmente ilimitado; precisa de premissa de volume.",
  fw=ISO, ctl="A.5.26 — Resposta a incidentes de segurança da informação", assoc="Direta",
  rel=["d01_resp_ilimitada"], acao="Registrar premissa na proposta",
  perg="A resposta a incidentes inclui atuação presencial e análise forense? Há limite de horas ou de incidentes incluídos no preço mensal?",
  resp="Segurança/Cyber")

I("d02_ir_relatorio", D, "§ 1. SERVIÇOS DE SOC, item 1.5", "§ 1. SERVIÇOS DE SOC, item 1.5",
  '"elaboração de relatório pós-incidente"', "Entregável", "Segurança da Informação/Cyber",
  "Relatório pós-incidente como entregável; sem prazo nem modelo definidos.", s=2, p=3, ob="Mandatório",
  imp="Esforço de documentação por incidente.", fw=ISO, ctl="A.5.27 — Aprendizado com incidentes de segurança da informação",
  assoc="Direta", acao="Atender", resp="Segurança/Cyber")

I("d02_ret5", D, "§ 1. SERVIÇOS DE SOC, item 1.6", "A: D02 § 1, item 1.3 · B: D02 § 1, item 1.6",
  'A: "deverão ser retidos por no mínimo 12 (doze) meses" · B: "Para fins de auditoria, os logs deverão ser mantidos por 5 (cinco) anos."',
  "Contradição", "Segurança da Informação/Cyber / Comercial/Preço",
  "Duas regras de retenção de logs no mesmo anexo: mínimo de 12 meses (1.3) e 5 anos (1.6). Podem ser lidas como camadas (12 meses online e 5 anos em arquivo), mas o texto não diz isso; o QT-03 fala em 12 meses 'online' ({d04_qt03}). Também não se sabe quem guarda os logs após o fim do contrato de 36 meses, se a retenção for de 5 anos. Tipo alternativo: Ambiguidade (registrado como Contradição por ser o de maior impacto).",
  s=4, p=3, ob="Mandatório",
  imp="Armazenar 5 anos em vez de 12 meses multiplica o custo de armazenamento do SIEM.",
  fw=ISO, ctl="A.5.33 — Proteção de registros", assoc="Correlata", rel=["d02_ret12", "d04_qt03", "d01_anx3_dados", "d03_migracao"],
  vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Os itens 1.3 e 1.6 do Anexo I preveem retenção de 12 meses e de 5 anos. Qual o período de retenção online (pesquisável) e qual o período em arquivo? Ao término do contrato, os logs são devolvidos ao Banco ou devem continuar sob guarda da Contratada?",
  resp="Pré-venda/Arquitetura")

I("d02_lgpd", D, "§ 1. SERVIÇOS DE SOC, itens 1.3 e 1.6", "§ 1. SERVIÇOS DE SOC, itens 1.3 e 1.6",
  '"Os registros (logs) de segurança deverão ser retidos"', "Requisito implícito", "Privacidade/Proteção de Dados",
  "Logs de segurança contêm dados pessoais (identificadores de usuários, IPs, e-mails de 4.500 a 7.100 usuários). Ao coletá-los, armazená-los por até 5 anos e analisá-los, o proponente atua como operador de dados pessoais em nome do Banco. Nenhum documento traz cláusula de tratamento de dados (papéis, instruções, suboperadores, comunicação de incidentes, devolução/eliminação).",
  s=3, p=3, ob="Mandatório", nat="Inferida",
  imp="Obrigações de operador (registro de operações, segurança, apoio a incidentes) e responsabilidade solidária potencial.",
  fw=LGPD, ctl="Art. 5º, VII (operador) e Art. 39", assoc="Direta", rel=["d02_ret5", "d01_anx3_dados"],
  acao="Esclarecer no Q&A",
  perg="O Banco disponibilizará acordo de tratamento de dados pessoais (papéis de controlador e operador, instruções, suboperadores, devolução e eliminação ao final do contrato)?",
  resp="Compliance")

I("d02_sla15", D, "§ 2. NÍVEIS DE SERVIÇO (SLA), item 2.1", "§ 2. NÍVEIS DE SERVIÇO (SLA), item 2.1",
  '"Tempo máximo para início do tratamento de incidentes críticos: 15 (quinze) minutos."', "SLA / KPI",
  "Operação/Serviços / Segurança da Informação/Cyber",
  "SLA de 15 minutos para início do tratamento de incidentes críticos, sujeito à multa de 10% por ocorrência ({d01_multa}). Não define o evento que inicia a contagem (alerta, abertura do chamado) nem o que é 'início do tratamento'; 'crítico' depende da matriz do Contratante, não fornecida ({d02_matriz}).",
  s=4, p=3, ob="Mandatório",
  imp="Cada violação gera multa de 10% do valor mensal; exige equipe e automação dimensionadas para 15 minutos 24x7.",
  fw=ITIL, ctl="Gerenciamento de incidentes / Gerenciamento de nível de serviço (identificador a confirmar)",
  assoc="Direta", rel=["d01_multa", "d02_matriz"], acao="Esclarecer no Q&A",
  perg="Qual evento marca o início da contagem do SLA de 15 minutos e o que caracteriza o 'início do tratamento'? O SLA vale desde o primeiro dia de operação ou após período de estabilização?",
  resp="Delivery/Operação")

I("d02_disp", D, "§ 2. NÍVEIS DE SERVIÇO (SLA), item 2.2", "§ 2. NÍVEIS DE SERVIÇO (SLA), item 2.2",
  '"Disponibilidade mínima mensal da plataforma SIEM: 99,9%."', "SLA / KPI", "Infraestrutura/Cloud / Operação/Serviços",
  "Disponibilidade mensal de 99,9% (cerca de 43 minutos de indisponibilidade por mês), sujeita à multa de 10% por ocorrência. Não define exclusões (janelas de manutenção, falhas de rede do Contratante) nem forma de medição.",
  s=4, p=3, ob="Mandatório", imp="Exige arquitetura de alta disponibilidade do SIEM; violação gera multa.",
  fw=ITIL, ctl="Gerenciamento de disponibilidade (identificador a confirmar)", assoc="Direta", rel=["d01_multa"],
  acao="Esclarecer no Q&A",
  perg="Quais exclusões se aplicam ao cálculo de disponibilidade de 99,9% (manutenções programadas, indisponibilidade de links ou ativos do Banco) e como será medida?",
  resp="Pré-venda/Arquitetura")

I("d02_relatorio", D, "§ 2. NÍVEIS DE SERVIÇO (SLA), item 2.3", "§ 2. NÍVEIS DE SERVIÇO (SLA), item 2.3",
  '"Relatório mensal de indicadores, a ser entregue até o 5º dia útil do mês subsequente."', "Entregável",
  "Operação/Serviços",
  "Relatório mensal de indicadores até o 5º dia útil. Por estar na seção de SLA, o atraso pode gerar multa de 10% ({d01_multa}). Conteúdo do relatório não definido.",
  s=3, p=3, ob="Mandatório", imp="Atraso em entregável administrativo exposto à mesma multa dos SLAs operacionais.",
  fw=ITIL, ctl="Gerenciamento de nível de serviço (identificador a confirmar)", assoc="Correlata", rel=["d01_multa"],
  acao="Atender", resp="Delivery/Operação")

I("d02_matriz", D, "§ 2. NÍVEIS DE SERVIÇO (SLA), item 2.4", "§ 2. NÍVEIS DE SERVIÇO (SLA), item 2.4",
  'Não localizado. Trecho que gera a necessidade: "A classificação de criticidade dos incidentes seguirá a matriz de classificação do Contratante."',
  "Lacuna", "Segurança da Informação/Cyber / Operação/Serviços",
  "A matriz de classificação do Contratante é citada e não foi fornecida. Ela define quais incidentes são 'críticos' e, portanto, sujeitos ao SLA de 15 minutos e à multa por ocorrência. Pode ser alterada unilateralmente pelo Contratante.",
  s=4, p=3, ob="Mandatório",
  imp="Sem a matriz, não é possível estimar o volume de incidentes críticos nem a exposição a multas.",
  fw=ISO, ctl="A.5.25 — Avaliação e decisão sobre eventos de segurança da informação", assoc="Direta",
  rel=["d02_sla15", "d01_multa"], acao="Esclarecer no Q&A",
  perg="Solicitamos a matriz de classificação de criticidade de incidentes do Banco, citada no item 2.4 do Anexo I, e o histórico mensal de incidentes por criticidade. Alterações na matriz durante o contrato serão acordadas entre as partes?",
  resp="Segurança/Cyber", pend="matriz de classificação de incidentes do Contratante citada e não fornecida")

I("d02_iam_ciclo", D, "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM), item 3.1", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM), item 3.1",
  '"Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Gestão do ciclo de vida de identidades. Não informa sistemas-alvo, integração com RH nem volume de movimentações. O ambiente atual é AD + scripts internos ({d03_iam_atual}).",
  s=3, p=3, ob="Mandatório", imp="Esforço de provisionamento proporcional à base de usuários e aos sistemas integrados.",
  fw=ISO, ctl="A.5.16 — Gestão de identidade", assoc="Direta", rel=["d03_iam_atual", "d03_iam_ferramenta"],
  acao="Esclarecer no Q&A",
  perg="Quantos sistemas-alvo devem ser integrados à gestão do ciclo de vida, qual a fonte autoritativa (sistema de RH) e qual o volume mensal de admissões, movimentações e desligamentos?",
  resp="Pré-venda/Arquitetura")

I("d02_iam_revog", D, "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM), item 3.1", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM), item 3.1",
  '"com revogação dos acessos de colaboradores desligados em até 24 (vinte e quatro) horas"', "SLA / KPI",
  "Segurança da Informação/Cyber",
  "Prazo de 24 horas para revogação. Está fora da seção 2 (SLA); não é claro se é 'nível de serviço previsto no Anexo I' sujeito à multa de 10% ({d01_multa}). Depende de o RH comunicar o desligamento a tempo (responsabilidade do Contratante não descrita).",
  s=3, p=3, ob="Mandatório", imp="Possível multa por atraso causado por comunicação tardia do RH.",
  fw=ISO, ctl="A.5.18 — Direitos de acesso", assoc="Direta", rel=["d01_multa"], acao="Esclarecer no Q&A",
  perg="O prazo de 24 horas para revogação de acessos é SLA sujeito à multa do item 7.4 da RFP? A contagem começa na comunicação formal do desligamento pelo RH?",
  resp="Delivery/Operação")

I("d02_mfa", D, "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM), item 3.2", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM), item 3.2",
  '"Autenticação multifator (MFA) obrigatória para 100% dos usuários com acesso privilegiado."',
  "Requisito não funcional", "Segurança da Informação/Cyber",
  "MFA para todos os usuários privilegiados. Não diz se o proponente fornece a solução de MFA nem quantos são os usuários privilegiados.",
  s=3, p=3, ob="Mandatório", imp="Possível custo de licenças de MFA e de implantação.", fw=ISO,
  ctl="A.8.5 — Autenticação segura", assoc="Direta", rel=["d03_iam_ferramenta"], acao="Esclarecer no Q&A",
  perg="A solução de MFA deve ser fornecida pela Contratada ou já existe no Banco? Quantos usuários com acesso privilegiado existem?",
  resp="Pré-venda/Arquitetura")

I("d02_recert", D, "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM), item 3.3", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM), item 3.3",
  '"Revisão (recertificação) trimestral dos acessos concedidos."', "Requisito funcional / de serviço",
  "Segurança da Informação/Cyber",
  "Recertificação trimestral de acessos. Sem ferramenta de IGA atual, o processo tende a ser manual; não define abrangência (todos os sistemas ou só críticos).",
  s=3, p=3, ob="Mandatório", imp="Esforço recorrente proporcional a usuários e sistemas.", fw=ISO,
  ctl="A.5.18 — Direitos de acesso", assoc="Direta", rel=["d03_iam_ferramenta"], acao="Precificar",
  resp="Delivery/Operação")

I("d02_pam", D, "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM), item 3.4", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM), item 3.4",
  '"É desejável que a solução contemple cofre de senhas para contas privilegiadas (PAM)."',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "PAM desejável. O Banco não possui PAM ({d03_pam}). Não está claro se oferecer PAM pontua ou se o custo entra no preço comparado.",
  s=2, p=3, ob="Desejável", imp="Decisão de incluir ou não PAM afeta preço e possivelmente pontuação em Ferramentas.",
  fw=ISO, ctl="A.8.2 — Direitos de acesso privilegiados", assoc="Direta", rel=["d03_pam"], acao="Esclarecer no Q&A",
  perg="A oferta de PAM será pontuada? Deve ser cotada como item opcional separado na planilha de preços?",
  resp="Pré-venda/Arquitetura")

I("d02_trans60", D, "§ 4. TRANSIÇÃO, item 4.1", "A: D01 p. 2 (impressa: 1), item 3.2 · B: D02 § 4. TRANSIÇÃO, item 4.1",
  'A: "A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato." · B: "A transição dos serviços deverá ser concluída em até 60 (sessenta) dias corridos a partir da assinatura do contrato."',
  "Contradição", "Transição/Implantação",
  "O RFP fixa 30 dias e o Anexo I fixa 60 dias para a mesma transição, com o mesmo marco inicial. Não há cláusula de precedência ({d01_precedencia}) nem resposta no Q&A.",
  s=4, p=3, ob="Mandatório",
  imp="Diferença de 30 dias altera equipe de transição, custo de operação paralela e risco de multa por atraso.",
  fw=ITIL, ctl="práticas de transição de serviço (identificador a confirmar)", assoc="Boa prática",
  rel=["d01_transicao30", "d01_precedencia", "d03_risco_transicao"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O item 3.2 da RFP prevê transição em 30 dias e o item 4.1 do Anexo I em 60 dias. Qual prazo prevalece?",
  resp="Delivery/Operação")

I("d02_paralelo", D, "§ 4. TRANSIÇÃO, item 4.2", "§ 4. TRANSIÇÃO, item 4.2",
  '"Durante a transição, o proponente deverá operar em paralelo com o fornecedor atual, sem custo adicional para o Contratante."',
  "Obrigação contratual", "Transição/Implantação / Comercial/Preço",
  "Operação em paralelo sem remuneração durante a transição, por prazo indefinido (30 ou 60 dias). O SIEM do fornecedor atual se encerra em 31/01/2027 sem prorrogação ({d03_siem_legado}); não se sabe se haverá paralelo efetivo. Não define responsabilidades do fornecedor atual na passagem.",
  s=3, p=3, ob="Mandatório", imp="Custo da transição deve ser diluído no preço mensal.", fw=ITIL,
  ctl="práticas de transição de serviço (identificador a confirmar)", assoc="Boa prática",
  rel=["d02_trans60", "d03_siem_legado"], acao="Precificar",
  perg="O fornecedor atual terá obrigação contratual de cooperar na transição (entrega de documentação, regras de correlação e logs)?",
  resp="Pricing/Financeiro")

I("d02_cissp", D, "§ 5. EQUIPE, item 5.1", "§ 5. EQUIPE, item 5.1",
  '"O serviço deverá contar com coordenador com certificação CISSP, dedicado exclusivamente ao contrato."',
  "Restrição", "Pessoas/Equipe",
  "Coordenador CISSP dedicado exclusivamente. Profissional de custo elevado, sem possibilidade de compartilhamento entre contratos.",
  s=3, p=3, ob="Mandatório", imp="Custo fixo integral de um coordenador certificado.", fw=ISO,
  ctl="Cláusula 7.2 — Competência", assoc="Correlata", rel=["d01_hab_equipe"], acao="Precificar", resp="RH/Staffing")

I("d02_n1_presencial", D, "§ 5. EQUIPE, item 5.2", "§ 5. EQUIPE, item 5.2",
  '"Os analistas de nível 1 deverão atuar presencialmente na sede do Contratante, em São Paulo/SP, em horário comercial."',
  "Restrição", "Pessoas/Equipe",
  "Exigência de N1 presencial em São Paulo em horário comercial, alterada pelo Q&A 6, que permite atuação remota em território nacional ({d04_qa6}). Fora do horário comercial, o texto original já não exigia presença.",
  s=3, p=3, ob="Mandatório", imp="Mudança reduz custo de alocação presencial.", fw=NA, assoc="Não aplicável",
  rel=["d04_qa6"], vig="Alterado", acao="Atender", resp="RH/Staffing")

I("d02_vpn", D, "§ 6. RESPONSABILIDADES DO CONTRATANTE, item 6.1", "§ 6. RESPONSABILIDADES DO CONTRATANTE, item 6.1",
  '"Disponibilizar acesso remoto seguro (VPN) aos ambientes monitorados."',
  "Responsabilidade / dependência do cliente", "Infraestrutura/Cloud",
  "O Contratante fornece VPN. Sem prazo para disponibilização; atraso compromete a transição.",
  s=2, p=3, imp="Dependência do cliente na transição.", fw=ISO, ctl="A.6.7 — Trabalho remoto", assoc="Correlata",
  acao="Registrar premissa na proposta", resp="Delivery/Operação")

I("d02_doc10", D, "§ 6. RESPONSABILIDADES DO CONTRATANTE, item 6.2", "§ 6. RESPONSABILIDADES DO CONTRATANTE, item 6.2",
  '"Disponibilizar a documentação técnica do ambiente em até 10 (dez) dias após a assinatura do contrato."',
  "Responsabilidade / dependência do cliente", "Transição/Implantação",
  "Documentação do ambiente só até o 10º dia após a assinatura. Com transição de 30 dias ({d01_transicao30}), sobra um terço do prazo sem conhecimento do ambiente.",
  s=3, p=3, imp="Comprime o prazo útil de transição; deve constar como premissa e condição de prazo.",
  fw=NA, assoc="Não aplicável", rel=["d01_transicao30", "d03_risco_transicao"], acao="Registrar premissa na proposta",
  resp="Delivery/Operação")

# =====================================================================================
# D03 — Apresentacao_Ambiente_Atual.pptx
# =====================================================================================
D = "D03"
I("d03_inventario", D, "Documento inteiro", "slides 1–5 e notas do slide 5",
  '"Workshop com proponentes — RFP nº 2026-017 — 22/10/2026"', "Registro de cobertura", "Administrativo do processo",
  "Inventário: apresentação de 5 slides, sem slides ocultos; o slide 5 tem notas do apresentador, lidas e analisadas ({d03_subsidiarias}). Leitura integral. A apresentação não declara se seu conteúdo integra o contrato ({d01_precedencia}).",
  rel=["d03_subsidiarias", "d01_precedencia"])

I("d03_usuarios", D, 'slide 2 — "Números do ambiente"', 'A: D01 p. 2 (impressa: 1), item 2.1 · B: D03 slide 2 — "Números do ambiente"',
  'A: "abrangendo aproximadamente 4.500 colaboradores" · B: "6.200 usuários ativos"', "Contradição",
  "Comercial/Preço / Segurança da Informação/Cyber",
  "O RFP dimensiona o IAM em cerca de 4.500 colaboradores; a apresentação informa 6.200 usuários ativos (+38%). A diferença pode decorrer de contas não nominais (terceiros, serviço), mas isso não é dito. O Q&A 5 depois fixou 5.000 ({d04_qa5}), valor que também não reconcilia os números.",
  s=4, p=3, ob="Informativo",
  imp="Base de usuários muda o preço do IAM em dezenas de por cento e o licenciamento de MFA/IGA.",
  fw=NA, assoc="Não aplicável", rel=["d01_obj_iam", "d04_qa5", "d03_subsidiarias"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A", resp="Pricing/Financeiro")

I("d03_servidores", D, 'slide 2 — "Números do ambiente"', 'slide 2 — "Números do ambiente"',
  '"850 servidores (70% Windows, 30% Linux)"', "Dado de dimensionamento", "Infraestrutura/Cloud",
  "850 servidores (cerca de 595 Windows e 255 Linux). Único dado quantitativo de fontes de log; não inclui ativos de rede, estações nem aplicações.",
  s=2, p=3, imp="Base parcial para dimensionar integrações e volumetria do SIEM.", fw=NA, assoc="Não aplicável",
  rel=["d02_integracao"], acao="Registrar premissa na proposta", resp="Pré-venda/Arquitetura")

I("d03_dcs", D, 'slide 2 — "Números do ambiente"', 'slide 2 — "Números do ambiente"',
  '"2 data centers próprios (São Paulo e Campinas)"', "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Dois data centers próprios. Pode demandar coletores de log em cada site.", s=2, p=3,
  imp="Infraestrutura de coleta em dois sites.", fw=NA, assoc="Não aplicável", acao="Registrar premissa na proposta",
  resp="Pré-venda/Arquitetura")

I("d03_nuvens", D, 'slide 2 — "Números do ambiente"', 'slide 2 — "Números do ambiente"',
  '"Workloads em 2 nuvens públicas"', "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Duas nuvens públicas, sem identificação dos provedores, contas/assinaturas ou volume de workloads. Necessário para integração nativa ao SIEM.",
  s=3, p=3, imp="Integrações de nuvem e volumetria não estimáveis.", fw=NA, assoc="Não aplicável",
  rel=["d02_integracao"], acao="Esclarecer no Q&A",
  perg="Quais são os dois provedores de nuvem pública, quantas contas/assinaturas e quantos workloads devem ser monitorados?",
  resp="Pré-venda/Arquitetura")

I("d03_siem_legado", D, 'slide 3 — "Ferramentas atuais"', 'slide 3 — "Ferramentas atuais"',
  '"SIEM legado — contrato encerra em 31/01/2027, sem possibilidade de prorrogação"', "Premissa do cliente",
  "Transição/Implantação",
  "Data-limite rígida do ambiente legado: 31/01/2027, véspera do início dos serviços ({d01_crono_inicio}). Não há margem para atraso na entrada em operação do novo SIEM.",
  s=3, p=3, imp="Qualquer atraso deixa o Banco sem SIEM; condiciona a transição e a migração de logs.",
  fw=NA, assoc="Não aplicável", rel=["d01_crono_inicio", "d03_risco_transicao"], acao="Registrar premissa na proposta",
  resp="Delivery/Operação")

I("d03_iam_atual", D, 'slide 3 — "Ferramentas atuais"', 'slide 3 — "Ferramentas atuais"',
  '"IAM: Active Directory + scripts internos"', "Dado de dimensionamento", "Segurança da Informação/Cyber",
  "Maturidade baixa de IAM: sem ferramenta de governança de identidades. Os requisitos do Anexo I (ciclo de vida, recertificação) partem de processos manuais/scripts.",
  s=3, p=3, imp="Indica necessidade de ferramenta ou de esforço manual significativo.", fw=NA, assoc="Não aplicável",
  rel=["d03_iam_ferramenta"], resp="Pré-venda/Arquitetura")

I("d03_iam_ferramenta", D, 'slide 3 — "Ferramentas atuais"', 'A: D03 slide 3 — "Ferramentas atuais" · B: D02 § 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM)',
  'Não localizado. A: "IAM: Active Directory + scripts internos" · B: "Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"',
  "Lacuna", "Técnico/Arquitetura / Comercial/Preço",
  "Nenhum documento diz se o proponente deve fornecer plataforma de IAM/IGA (e MFA) ou apenas operar o AD e os scripts existentes. Para o SIEM o fornecimento é explícito (Anexo I, 1.2); para o IAM, não.",
  s=4, p=3, ob="Informativo",
  imp="Fornecer plataforma de IGA muda o preço e o prazo de implantação de forma significativa.",
  fw=NA, assoc="Não aplicável", rel=["d02_iam_ciclo", "d02_mfa", "d02_recert"], acao="Esclarecer no Q&A",
  perg="Para o escopo de IAM, a Contratada deve fornecer plataforma de governança de identidades (IGA) e MFA, ou apenas operar o Active Directory e as ferramentas existentes do Banco?",
  resp="Pré-venda/Arquitetura")

I("d03_pam", D, 'slide 3 — "Ferramentas atuais"', 'slide 3 — "Ferramentas atuais"',
  '"Não há solução de PAM"', "Oportunidade / diferencial", "Segurança da Informação/Cyber",
  "O Banco não tem PAM e o Anexo I o considera desejável ({d02_pam}). Oferta de PAM (como opcional) pode diferenciar a proposta em 'Ferramentas e tecnologia' e responder a uma necessidade explícita.",
  ob="Desejável", imp="Possível ganho de pontuação técnica.", fw=ISO, ctl="A.8.2 — Direitos de acesso privilegiados",
  assoc="Direta", rel=["d02_pam", "d01_crit_ferramentas"], acao="Precificar", resp="Pré-venda/Arquitetura")

I("d03_alertas", D, 'slide 4 — "Desafios"', 'slide 4 — "Desafios"',
  '"Cerca de 1.200 alertas por dia" [...] "70% de falsos positivos"', "Dado de dimensionamento",
  "Operação/Serviços",
  "Cerca de 1.200 alertas/dia (36 mil/mês), 70% falsos positivos (~840/dia). Único dado de carga operacional; não é volumetria de eventos (EPS), que foi negada ({d04_qa3}).",
  s=3, p=3, imp="Dimensiona analistas N1 para triagem no início da operação.", fw=NIST,
  ctl="DE.AE — Análise de eventos adversos", assoc="Correlata", rel=["d04_qa3", "d03_meta_fp"],
  acao="Registrar premissa na proposta", resp="Delivery/Operação")

I("d03_meta_fp", D, 'slide 4 — "Desafios"', 'slide 4 — "Desafios"',
  '"Meta: reduzir os falsos positivos para 10% no primeiro trimestre de operação"', "Ambiguidade",
  "Operação/Serviços",
  "Meta de reduzir falsos positivos de 70% para 10% em 3 meses aparece só na apresentação. Não se sabe se é SLA contratual (sujeito à multa de 10% por ocorrência), meta de bônus ou expectativa. Não há definição de falso positivo nem método de medição. Pode ser também oportunidade de diferenciação.",
  s=4, p=3, ob="Informativo",
  imp="Se for contratual, meta agressiva no período de estabilização expõe a multa; exige esforço de tuning no início.",
  fw=NA, assoc="Não aplicável", rel=["d03_alertas", "d01_multa", "d01_precedencia"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="A meta de reduzir falsos positivos para 10% no primeiro trimestre é um SLA contratual sujeito a multa? Como será medida a taxa de falsos positivos?",
  resp="Delivery/Operação")

I("d03_migracao", D, 'slide 5 — "Expectativas para o novo serviço"', 'slide 5 — "Expectativas para o novo serviço"',
  '"Migração de 24 meses de logs históricos do SIEM legado para a nova plataforma"', "Ambiguidade",
  "Técnico/Arquitetura / Transição/Implantação",
  "Escopo de migração de 24 meses de logs históricos que não consta do RFP nem do Anexo I. Não informa volume, formato ou fabricante do SIEM legado, nem se deve estar concluída antes de 31/01/2027. Também excede a retenção mínima de 12 meses (1.3). Tipo alternativo: Requisito funcional (ampliação de escopo).",
  s=4, p=3, ob="Informativo",
  imp="Migração de volume desconhecido de logs, em prazo de transição curto, afeta custo de armazenamento e cronograma.",
  fw=NA, assoc="Não aplicável", rel=["d02_ret5", "d03_siem_legado", "d03_risco_transicao", "d01_precedencia"],
  vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A migração de 24 meses de logs históricos faz parte do escopo contratual? Qual o volume (TB), o fabricante/formato do SIEM legado e o prazo para concluí-la? Os logs migrados devem ficar pesquisáveis online?",
  resp="Pré-venda/Arquitetura")

I("d03_visao_riscos", D, 'slide 5 — "Expectativas para o novo serviço"', 'slide 5 — "Expectativas para o novo serviço"',
  '"Visão unificada de riscos para a diretoria"', "Ambiguidade", "Dados/Analytics",
  "Expectativa genérica de 'visão unificada de riscos' não descrita no Anexo I. Pode significar dashboard executivo do SOC ou ferramenta de GRC integrando riscos, com custos muito diferentes.",
  s=3, p=3, ob="Informativo", imp="Entregável indefinido; risco de expectativa não atendida.", fw=NA,
  assoc="Não aplicável", rel=["d01_precedencia"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O que se espera da 'visão unificada de riscos para a diretoria': painel executivo de indicadores do SOC/IAM ou uma solução de gestão de riscos (GRC)? É parte do escopo contratual?",
  resp="Pré-venda/Arquitetura")

I("d03_subsidiarias", D, 'slide 5 — notas do apresentador', 'A: D01 p. 2 (impressa: 1), item 2.1 · B: D03 slide 5 — notas do apresentador',
  'A: "abrangendo aproximadamente 4.500 colaboradores" · B: "as subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários adicionais) também deverão ser incluídas no escopo"',
  "Contradição", "Comercial/Preço / Jurídico/Contratual",
  "Ampliação de escopo escondida nas notas do apresentador: duas subsidiárias (~900 usuários) 'deverão ser incluídas', o que não consta do objeto do RFP nem do Anexo I. Somadas aos 6.200 usuários do slide 2, a base chegaria a ~7.100. Também levanta questões de contratante (pessoas jurídicas distintas), faturamento e ambientes adicionais a monitorar. O Q&A 5 ({d04_qa5}) não menciona subsidiárias.",
  s=4, p=3, ob="Mandatório",
  imp="Pode aumentar a base de usuários em 20% ou mais e incluir ambientes de outras empresas no SOC.",
  fw=NA, assoc="Não aplicável", rel=["d01_obj_iam", "d03_usuarios", "d04_qa5", "d01_precedencia"],
  vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="As subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários) fazem parte do escopo de SOC e IAM? Em caso positivo, serão contratantes ou beneficiárias do contrato e quais ambientes delas devem ser monitorados?",
  resp="Bid Manager")

I("d03_risco_transicao", D, 'slide 3 — "Ferramentas atuais" (combinado com D01 e D02)',
  'A: D03 slide 3 · B: D01 p. 2 (impressa: 1), item 3.2 · C: D02 § 6, item 6.2',
  'A: "contrato encerra em 31/01/2027, sem possibilidade de prorrogação" · B: "deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato" · C: "em até 10 (dez) dias após a assinatura do contrato"',
  "Risco para o proponente", "Transição/Implantação",
  "Risco combinado: o SIEM legado termina em 31/01/2027 sem prorrogação; a transição tem prazo contraditório de 30 ou 60 dias a partir de uma assinatura sem data ({d01_assinatura}); a documentação do ambiente chega só até o 10º dia ({d02_doc10}); há operação paralela sem custo ({d02_paralelo}), migração de 24 meses de logs ({d03_migracao}) e EPS desconhecido ({d04_qa3}). Atraso deixa o Banco sem SIEM e expõe o proponente a multas sem teto ({d01_multa}) e à responsabilidade ilimitada por incidentes ({d01_resp_ilimitada}). Probabilidade 4: o prazo útil é menor que o necessário para obrigações explícitas (documentação em até 10 dias dentro de 30, migração de 24 meses de logs) e o limite de 31/01/2027 é declarado improrrogável.",
  s=5, p=4, ob="Informativo", nat="Inferida",
  imp="Risco de não entrar em operação em 01/02/2027, com multas, responsabilidade por incidentes no período descoberto e dano reputacional.",
  fw=ITIL, ctl="práticas de transição de serviço (identificador a confirmar)", assoc="Boa prática",
  rel=["d03_siem_legado", "d01_transicao30", "d02_trans60", "d01_assinatura", "d02_doc10", "d02_paralelo", "d03_migracao", "d04_qa3", "d01_multa", "d01_resp_ilimitada"],
  acao="Mitigar",
  perg="Será concedido período de estabilização sem aplicação de multas nos primeiros 90 dias de operação, e o prazo de transição será contado a partir da entrega da documentação e dos acessos pelo Banco?",
  resp="Delivery/Operação")

# =====================================================================================
# D04 — QA_Rodada1_e_Questionario.xlsx
# =====================================================================================
D = "D04"
I("d04_inventario", D, "Arquivo inteiro", 'abas "Instruções", "Q&A Rodada 1", "Questionário Técnico", "Pesos" (OCULTA)',
  '"Questionário Técnico e Respostas aos Esclarecimentos — RFP nº 2026-017"', "Registro de cobertura",
  "Administrativo do processo",
  "Inventário: planilha com 4 abas; a aba 'Pesos' está OCULTA e foi analisada ({d04_pesos}). Sem linhas/colunas ocultas nem comentários. Q&A com 6 perguntas, todas datadas de 12/11/2026 (Rodada 1). Leitura integral.",
  rel=["d04_pesos"])

I("d04_instr_elim", D, 'aba "Instruções"', 'aba "Instruções" · A3',
  '"O preenchimento de todas as abas deste arquivo é obrigatório. Questionários incompletos serão desclassificados."',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Questionário incompleto desclassifica. Consequência não prevista no RFP (item 4.4 — {d01_questionario}). Probabilidade 5: o texto determina a desclassificação sem margem de interpretação.",
  s=5, p=5, ob="Mandatório", imp="Questionário incompleto leva à desclassificação.", fw=NA, assoc="Não aplicável",
  rel=["d01_questionario", "d04_instr_ambig"], acao="Atender", resp="Pré-venda/Arquitetura")

I("d04_instr_ambig", D, 'aba "Instruções"', 'aba "Instruções" · A3',
  '"O preenchimento de todas as abas deste arquivo é obrigatório."', "Ambiguidade", "Administrativo do processo",
  "'Todas as abas' incluiria a aba do Q&A e a aba oculta 'Pesos', que não têm campos para o proponente preencher. Também não diz se a coluna 'Comentários' do questionário é obrigatória para o questionário ser considerado completo.",
  s=4, p=3, ob="Mandatório",
  imp="Interpretação diferente da do avaliador pode levar à desclassificação por 'questionário incompleto'.",
  fw=NA, assoc="Não aplicável", rel=["d04_instr_elim", "d04_pesos"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Quais abas e colunas devem ser preenchidas pelo proponente? A coluna 'Comentários' do questionário é obrigatória? As abas 'Q&A Rodada 1' e 'Pesos' exigem algum preenchimento?",
  resp="Bid Manager")

I("d04_qa1", D, 'aba "Q&A Rodada 1" · pergunta 1', 'aba "Q&A Rodada 1" · linha 2 (Nº 1) · E2 · Rodada 1 — 12/11/2026',
  '"A data de entrega das propostas fica prorrogada para 27/11/2026, até as 18h."', "Prazo / marco",
  "Administrativo do processo",
  "Altera a entrega de 20/11 para 27/11/2026, 18h ({d01_crono_entrega}). Não informa fuso horário (presume-se horário de Brasília). Probabilidade 2: data clara; o impacto só ocorre por falha interna.",
  s=5, p=2, ob="Mandatório", imp="Proposta fora do prazo não é recebida.", fw=NA, assoc="Não aplicável",
  rel=["d01_crono_entrega"], acao="Atender", resp="Bid Manager")

I("d04_qa2", D, 'aba "Q&A Rodada 1" · pergunta 2', 'aba "Q&A Rodada 1" · linha 3 (Nº 2) · E3 · Rodada 1 — 12/11/2026',
  '"Não. O SOC deverá estar localizado em território nacional."', "Critério eliminatório / de habilitação",
  "Segurança da Informação/Cyber / Regulatório/Compliance",
  "Confirma o item 5.1 c ({d01_hab_soc_br}) sem alterá-lo. Trata apenas do SOC; não resolve a contradição sobre localização dos dados do SIEM ({d02_siem_nuvem}). Probabilidade 5: critério eliminatório reiterado pelo cliente.",
  s=5, p=5, ob="Mandatório", imp="Operação do SOC fora do Brasil leva à inabilitação.", fw=NA, assoc="Não aplicável",
  rel=["d01_hab_soc_br", "d02_siem_nuvem"], vig="Duplicado", acao="Atender", resp="Delivery/Operação")

I("d04_qa3", D, 'aba "Q&A Rodada 1" · pergunta 3', 'aba "Q&A Rodada 1" · linha 4 (Nº 3) · E4 · Rodada 1 — 12/11/2026',
  '"A volumetria será informada somente ao proponente vencedor."', "Lacuna", "Comercial/Preço / Técnico/Arquitetura",
  "O cliente recusa informar a volumetria de eventos (EPS) antes da contratação. EPS é o principal direcionador de custo de licenciamento, armazenamento e infraestrutura do SIEM que o proponente deve fornecer ({d02_siem_fornecer}) e reter por até 5 anos ({d02_ret5}). Probabilidade 5: informação indispensável ao preço recusada formalmente pelo cliente.",
  s=4, p=5, ob="Informativo",
  imp="Preço do SIEM sem base; risco de subdimensionamento sem mecanismo de reequilíbrio.",
  fw=NA, assoc="Não aplicável", rel=["d02_siem_fornecer", "d02_integracao", "d02_ret5", "d03_alertas"],
  acao="Registrar premissa na proposta",
  perg="Já que a volumetria não será informada, o Banco aceita que a proposta adote um volume de referência de EPS/GB por dia como premissa, com revisão de preço caso o volume real exceda a faixa considerada?",
  resp="Pricing/Financeiro")

I("d04_qa4", D, 'aba "Q&A Rodada 1" · pergunta 4', 'aba "Q&A Rodada 1" · linha 5 (Nº 4) · E5 · Rodada 1 — 12/11/2026',
  '"As condições do item 7 permanecem inalteradas."', "Penalidade / multa / glosa", "Jurídico/Contratual / Financeiro",
  "Perguntado se as multas têm limite máximo, o cliente não respondeu diretamente e manteve o item 7, ou seja, multa de 10% por ocorrência sem teto ({d01_multa}) e, por extensão, responsabilidade ilimitada ({d01_resp_ilimitada}). Probabilidade 4: o cliente deixou sem resposta objetiva o pedido de esclarecimento sobre o tema.",
  s=5, p=4, ob="Mandatório", imp="Confirma exposição a multas sem limite.", fw=CC,
  ctl="cláusula penal e seus limites (identificador a confirmar)", assoc="Correlata",
  rel=["d01_multa", "d01_resp_ilimitada", "d04_risco_financeiro"], acao="Propor exceção/ressalva", resp="Jurídico")

I("d04_qa5", D, 'aba "Q&A Rodada 1" · pergunta 5', 'A: D04 aba "Q&A Rodada 1" · E6 (Nº 5) · B: D03 slide 2 · C: D03 slide 5 — notas do apresentador',
  'A: "Considerar 5.000 usuários." · B: "6.200 usuários ativos" · C: "cerca de 900 usuários adicionais"',
  "Contradição", "Comercial/Preço",
  "O Q&A 5 altera a base do RFP (~4.500 — {d01_obj_iam}) para 5.000 usuários, mas continua incompatível com os 6.200 usuários ativos da apresentação ({d03_usuarios}) e com os ~900 usuários das subsidiárias ({d03_subsidiarias}). Não diz se as subsidiárias estão incluídas nem se 5.000 vale para SOC e IAM.",
  s=4, p=3, ob="Informativo",
  imp="Preço de IAM calculado sobre 5.000 pode ficar até 30% abaixo da base real (6.200 a 7.100).",
  fw=NA, assoc="Não aplicável", rel=["d01_obj_iam", "d03_usuarios", "d03_subsidiarias", "d01_precedencia"],
  vig="Em esclarecimento", acao="Registrar premissa na proposta",
  perg="A resposta do Q&A 5 fixa 5.000 usuários, mas a apresentação de 22/10/2026 informa 6.200 usuários ativos e mais 900 usuários das subsidiárias. Qual número deve ser usado, ele inclui as subsidiárias, e haverá revisão de preço se a base real for maior?",
  resp="Pricing/Financeiro")

I("d04_qa6", D, 'aba "Q&A Rodada 1" · pergunta 6', 'aba "Q&A Rodada 1" · linha 7 (Nº 6) · E7 · Rodada 1 — 12/11/2026',
  '"Sim, desde que em território nacional."', "Restrição", "Pessoas/Equipe",
  "Permite N1 remoto em território nacional, alterando o Anexo I, item 5.2 ({d02_n1_presencial}). Mantém a restrição de localização no Brasil.",
  s=2, p=3, ob="Mandatório", imp="Reduz custo de alocação presencial em São Paulo.", fw=ISO,
  ctl="A.6.7 — Trabalho remoto", assoc="Correlata", rel=["d02_n1_presencial", "d01_hab_soc_br"], acao="Atender",
  resp="RH/Staffing")

I("d04_qt01", D, 'aba "Questionário Técnico" · QT-01', 'aba "Questionário Técnico" · linha 2 (QT-01) · B2:C2 · aba "Pesos" · B2',
  '"Possui certificação ISO/IEC 27001 com escopo que inclua os serviços de SOC?"', "Critério de avaliação / pontuação",
  "Segurança da Informação/Cyber",
  "Repete o critério de habilitação 5.1 a ({d01_hab_iso}); obrigatório e com peso 3 na aba oculta.", s=3, p=3,
  ob="Mandatório", imp="Resposta deve ser coerente com o certificado apresentado na habilitação.", fw=ISO,
  ctl="Certificação do SGSI (cláusulas 4 a 10)", assoc="Direta", rel=["d01_hab_iso", "d04_pesos"], vig="Duplicado",
  acao="Atender", resp="Compliance")

I("d04_qt02", D, 'aba "Questionário Técnico" · QT-02', 'aba "Questionário Técnico" · linha 3 (QT-02) · B3:C3 · aba "Pesos" · B3',
  '"Oferece integração nativa com plataforma SOAR?"', "Critério de avaliação / pontuação", "Técnico/Arquitetura",
  "SOAR não aparece no RFP nem no Anexo I, mas é perguntado no questionário (não obrigatório, peso 1). Pela regra da aba oculta, responder 'Não atende' tira 2 pontos da Nota Técnica ({d04_pesos}): na prática, requisito não declarado.",
  s=3, p=3, ob="Desejável", imp="Perda de 2 pontos se não oferecido; custo de SOAR se oferecido.", fw=NIST,
  ctl="RS.MA — Gestão de incidentes", assoc="Correlata", rel=["d04_pesos", "d04_oport"], acao="Precificar",
  resp="Pré-venda/Arquitetura")

I("d04_qt03", D, 'aba "Questionário Técnico" · QT-03', 'aba "Questionário Técnico" · linha 4 (QT-03) · B4:C4 · aba "Pesos" · B4',
  '"Retém os logs online por no mínimo 12 meses?"', "Requisito não funcional", "Segurança da Informação/Cyber",
  "Acrescenta 'online' ao requisito de 12 meses do Anexo I (1.3), sem tratar dos 5 anos do item 1.6. Reforça a leitura em camadas, mas não a confirma ({d02_ret5}). Obrigatório, peso 2.",
  s=3, p=3, ob="Mandatório", imp="Armazenamento pesquisável de 12 meses de logs, de volume desconhecido.", fw=ISO,
  ctl="A.8.15 — Registro de logs", assoc="Direta", rel=["d02_ret12", "d02_ret5", "d04_qa3"], acao="Atender",
  resp="Pré-venda/Arquitetura")

I("d04_qt04", D, 'aba "Questionário Técnico" · QT-04', 'aba "Questionário Técnico" · linha 5 (QT-04) · B5:C5 · aba "Pesos" · B5',
  '"Atende aos requisitos da Resolução CMN nº 4.893/2021?"', "Requisito não funcional", "Regulatório/Compliance",
  "Declaração genérica de atendimento à Resolução CMN nº 4.893/2021, obrigatória e com peso 3. Os requisitos da norma recaem principalmente sobre a instituição financeira; não se especifica quais obrigações o proponente deve demonstrar ({d01_res4893}).",
  s=3, p=3, ob="Mandatório", imp="Declaração ampla pode gerar obrigações contratuais não precificadas.", fw=R4893,
  ctl="requisitos para contratação de serviços de processamento, armazenamento de dados e computação em nuvem (identificador a confirmar)",
  assoc="Direta", rel=["d01_res4893", "d04_pesos"], acao="Esclarecer no Q&A",
  perg="Quais requisitos da Resolução CMN nº 4.893/2021 o proponente deve demonstrar no QT-04 e que evidências serão exigidas?",
  resp="Compliance")

I("d04_qt05", D, 'aba "Questionário Técnico" · QT-05', 'aba "Questionário Técnico" · linha 6 (QT-05) · B6:C6 · aba "Pesos" · B6',
  '"Oferece serviço de threat intelligence?"', "Critério de avaliação / pontuação", "Segurança da Informação/Cyber",
  "Threat intelligence não está no Anexo I; não obrigatório, peso 2. 'Não atende' tira 2 pontos ({d04_pesos}). Serviços de inteligência costumam ser de terceiros, o que esbarra na vedação de subcontratação ({d01_subcontratacao}) e na residência de dados ({d01_anx3_dados}).",
  s=3, p=3, ob="Desejável", imp="Perda de 2 pontos se não oferecido; custo de feeds se oferecido.", fw=ISO,
  ctl="A.5.7 — Inteligência de ameaças", assoc="Direta", rel=["d04_pesos", "d01_subcontratacao", "d04_oport"],
  acao="Precificar", resp="Segurança/Cyber")

I("d04_qt06", D, 'aba "Questionário Técnico" · QT-06', 'aba "Questionário Técnico" · linha 7 (QT-06) · B7:C7 · aba "Pesos" · B7',
  '"Possui equipe com certificações reconhecidas pelo mercado?"', "Critério de avaliação / pontuação", "Pessoas/Equipe",
  "Pergunta obrigatória (peso 2) tão genérica quanto o item 5.2 do RFP ({d01_hab_equipe}); não define quais certificações.",
  s=3, p=3, ob="Mandatório", imp="Avaliação subjetiva da equipe.", fw=ISO, ctl="Cláusula 7.2 — Competência",
  assoc="Correlata", rel=["d01_hab_equipe", "d04_pesos"], acao="Esclarecer no Q&A", resp="RH/Staffing")

I("d04_pesos", D, 'aba "Pesos" (OCULTA)', 'A: D01 p. 4 (impressa: 3), item 6.2 · B: D04 aba "Pesos" (OCULTA) · A9',
  'A: "A Nota Técnica, de no máximo 60 (sessenta) pontos, será atribuída conforme os critérios abaixo" · B: "Requisitos não obrigatórios respondidos como \'Não atende\' reduzem a Nota Técnica em 2 (dois) pontos cada."',
  "Contradição", "Administrativo do processo",
  "Regra de pontuação escondida em aba oculta: deduções de 2 pontos por requisito não obrigatório respondido 'Não atende' (QT-02 e QT-05 — até 4 pontos), além de pesos 1 a 3 por pergunta. O RFP diz que a Nota Técnica é atribuída só pelos quatro critérios do item 6.2. A dedução pode levar a nota abaixo do corte de 70% ({d01_aval_corte}).",
  s=4, p=3, ob="Informativo",
  imp="Até 4 pontos de dedução (6,7% da Nota Técnica de 60) não previstos no RFP; pode desclassificar proposta próxima do corte.",
  fw=NA, assoc="Não aplicável", rel=["d01_aval_soma", "d01_aval_corte", "d04_qt02", "d04_qt05", "d04_pesos_lacuna"],
  vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A aba oculta 'Pesos' do questionário prevê pesos por pergunta e dedução de 2 pontos da Nota Técnica para cada requisito não obrigatório respondido 'Não atende'. Essa regra é válida? Como se combina com os critérios do item 6.2 da RFP?",
  resp="Bid Manager")

I("d04_pesos_lacuna", D, 'aba "Pesos" (OCULTA)', 'aba "Pesos" (OCULTA) · A1:B7',
  'Não localizado. Trecho que gera a necessidade: "Peso" [...] "QT-01" [...] "QT-04"', "Lacuna", "Administrativo do processo",
  "A aba oculta atribui pesos (QT-01: 3, QT-02: 1, QT-03: 2, QT-04: 3, QT-05: 2, QT-06: 2), mas nenhum documento explica como os pesos entram na nota nem como respostas 'Parcial' são tratadas.",
  s=3, p=3, ob="Informativo", imp="Impede estimar o efeito do questionário na Nota Técnica.", fw=NA,
  assoc="Não aplicável", rel=["d04_pesos"], acao="Esclarecer no Q&A",
  perg="Como os pesos da aba 'Pesos' são aplicados na Nota Técnica e como são pontuadas as respostas 'Parcial'?",
  resp="Bid Manager")

I("d04_oport", D, 'aba "Questionário Técnico" · QT-02 e QT-05', 'aba "Questionário Técnico" · B3 e B6',
  '"Oferece integração nativa com plataforma SOAR?" [...] "Oferece serviço de threat intelligence?"',
  "Oportunidade / diferencial", "Segurança da Informação/Cyber",
  "SOAR e threat intelligence são valorizados no questionário, apesar de ausentes do Anexo I. Oferecê-los evita a dedução de pontos e reforça a meta de reduzir falsos positivos ({d03_meta_fp}) com automação de triagem.",
  ob="Desejável", imp="Ganho em 'Ferramentas e tecnologia' e ausência de dedução.", fw=NIST,
  ctl="DE.AE — Análise de eventos adversos", assoc="Correlata", rel=["d04_qt02", "d04_qt05", "d03_meta_fp"],
  acao="Precificar", resp="Pré-venda/Arquitetura")

I("d04_risco_financeiro", D, 'aba "Q&A Rodada 1" · pergunta 4 (combinado com D01 e D02)',
  'A: D01 p. 5 (impressa: 4), item 7.4 · B: D01 p. 5 (impressa: 4), item 7.5 · C: D04 aba "Q&A Rodada 1" · E5 (Nº 4)',
  'A: "multa de 10% (dez por cento) do valor mensal do contrato, por ocorrência" · B: "responderá de forma integral e ilimitada" · C: "As condições do item 7 permanecem inalteradas."',
  "Risco para o proponente", "Jurídico/Contratual / Financeiro",
  "Risco combinado de exposição financeira: multa de 10% por ocorrência sem teto (mantida no Q&A 4), responsabilidade ilimitada por qualquer incidente no ambiente do Contratante, SLA de 15 minutos ({d02_sla15}) cuja abrangência depende de matriz de classificação não fornecida ({d02_matriz}), volumetria negada ({d04_qa3}) e vedação de subcontratação que impede repassar riscos ({d01_subcontratacao}). Probabilidade 4: o cliente já recusou rever o item 7 (Q&A 4) e as multas incidem automaticamente por ocorrência.",
  s=5, p=4, ob="Informativo", nat="Inferida",
  imp="Exposição financeira e jurídica ilimitada, possivelmente não segurável; ponto central para a decisão de Go/No-Go.",
  fw="ISO 31000", ctl="avaliação e tratamento de riscos (identificador a confirmar)", assoc="Boa prática",
  rel=["d01_multa", "d01_resp_ilimitada", "d04_qa4", "d02_sla15", "d02_matriz", "d04_qa3", "d01_subcontratacao"],
  acao="Avaliar Go/No-Go", resp="Jurídico")

# =====================================================================================
DOCS = [
    dict(codigo="D01", arquivo="RFP-2026-017_Servicos_SOC_IAM.pdf", tipo="RFP", versao="v1.0 — 15/10/2026"),
    dict(codigo="D02", arquivo="Anexo_I_Especificacao_Tecnica.docx", tipo="Anexo técnico", versao="v1.0 — 15/10/2026"),
    dict(codigo="D03", arquivo="Apresentacao_Ambiente_Atual.pptx", tipo="Apresentação", versao="22/10/2026"),
    dict(codigo="D04", arquivo="QA_Rodada1_e_Questionario.xlsx", tipo="Q&A e questionário", versao="12/11/2026"),
]
PROX = {1: "Anexo_I_Especificacao_Tecnica.docx (D02), a partir do § 1. SERVIÇOS DE SOC",
        2: 'Apresentacao_Ambiente_Atual.pptx (D03), a partir do slide 1',
        3: 'QA_Rodada1_e_Questionario.xlsx (D04), a partir da aba "Instruções"'}

if __name__ == "__main__":
    n = int(sys.argv[1])
    codes = [d["codigo"] for d in DOCS[:n]]
    docs = [dict(d, situacao="processado" if d["codigo"] in codes else "pendente") for d in DOCS]
    itens = [it for it in ITENS if it["doc"] in codes]
    status = {"final": True} if n == len(DOCS) else {"final": False, "proximo": PROX[n], "parte": n, "concluidos": n}
    data = {"processo": "RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Serviços gerenciados de SOC e IAM",
            "documentos": docs, "itens": itens, "status": status}
    open(sys.argv[2], "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, indent=1))
    print(f"{len(itens)} itens ({', '.join(codes)})")
