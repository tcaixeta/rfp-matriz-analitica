# -*- coding: utf-8 -*-
"""Gera itens.json para build_matrix.py. Uso: python gerar_itens.py <saida.json> [ultimo_doc]"""
import json
import sys

ITENS = []

ISO = "ISO/IEC 27001:2022 (Anexo A)"
CSF = "NIST CSF 2.0"
LGPD = "LGPD (Lei 13.709/2018)"
ITIL = "ITIL 4"
CMN = "Resolução CMN nº 4.893/2021 (citada no RFP, item 1.2)"
CC = "Código Civil (Lei 10.406/2002) — regime privado"
CIS = "CIS Controls v8"


def I(chave, doc, secao, loc, ev, tipo, dom, desc, obr="Informativo", nat="Explícita", s=None, p=None,
      imp="—", fw="—", ctl="—", assoc=None, rel=None, vig="Vigente", acao="Nenhuma (informativo)",
      perg="—", resp="Bid Manager", pend=None):
    it = {"chave": chave, "doc": doc, "secao": secao, "localizador": loc, "evidencia": ev, "tipo": tipo,
          "dominio": dom, "descricao": desc, "obrigatoriedade": obr, "natureza": nat, "impacto": imp,
          "framework": fw, "controle": ctl, "vigencia": vig, "acao": acao, "pergunta": perg,
          "responsavel": resp, "relacionados": rel or []}
    if tipo == "Registro de cobertura":
        it["associacao"] = "—"
    else:
        it["associacao"] = assoc or ("Não aplicável" if fw == "—" else "Direta")
    if s is not None:
        it["s"], it["p"] = s, p
    if pend:
        it["pendencia"] = pend
    ITENS.append(it)


# =============================================================== D01 — RFP (PDF)
D = "D01"
I("d01_inv", D, "Documento inteiro (capa e seções 1 a 7 + página final)", "p. 1–6 (impressas: sem número, 1–5)",
  '"Solicitação de Proposta (RFP) nº 2026-017"', "Registro de cobertura", "Administrativo do processo",
  "Inventário: PDF com 6 páginas físicas (p. 1 capa sem numeração; p. 2–6 com numeração impressa 1–5). Texto extraído das p. 1–5. A p. 6 (impressa: 5) não tem camada de texto (imagem digitalizada); foi lida visualmente a partir da imagem e contém o \"ANEXO III — Declaração de Localização de Dados\" (itens com localizador marcado \"(OCR)\"). Cabeçalho repetido em todas as páginas (\"DOCUMENTO FICTÍCIO PARA TESTE\") desconsiderado. Leitura integral; nenhum trecho ilegível.")
I("d01_ocr", D, "Página final — Anexo III (imagem)", "p. 6 (impressa: 5) (OCR)",
  '"ANEXO III — DECLARAÇÃO DE LOCALIZAÇÃO DE DADOS"', "Registro de cobertura", "Administrativo do processo",
  "Página sem texto extraível (0 caracteres no corpo; imagem ocupa ~50% da página), sinalizada pelo script de extração. O conteúdo foi lido na imagem renderizada e analisado normalmente (itens {d01_anexo3_decl} e {d01_anexo3_dados}). Leitura visual completa: título, declaração, exigência de assinatura sob pena de inabilitação e campos de data/assinatura.")
I("d01_regime", D, "1. Apresentação — 1.2", "p. 2 (impressa: 1)",
  '"O Banco é instituição financeira autorizada a funcionar pelo Banco Central do Brasil e está sujeito à Resolução CMN nº 4.893/2021"',
  "Registro de cobertura", "Regulatório/Compliance",
  "Regime identificado: contratação PRIVADA (Banco Horizonte Fictício S.A., sociedade anônima; processo por RFP com portal de fornecedores próprio; não há menção a edital, licitação, pregão ou Lei 14.133/2021) em SETOR REGULADO (instituição financeira autorizada pelo Banco Central, sujeita à Resolução CMN nº 4.893/2021). Consequência: legislação de contratação pública não se aplica; aplicam-se Código Civil, LGPD e a regulação do BCB citada pelo cliente.")
I("d01_precedencia", D, "Documento inteiro — ordem de precedência", "p. 1–6 (cláusula não localizada)",
  'Não localizado. Trecho que gera a necessidade: "As especificações técnicas detalhadas constam do Anexo I — Especificação Técnica."',
  "Lacuna", "Jurídico/Contratual / Administrativo do processo",
  "O RFP não traz cláusula de ordem de precedência entre RFP, Anexo I, apresentação do workshop e respostas do Q&A. Há divergências entre esses documentos (transição 30 × 60 dias; 4.500 × 5.000 × 6.200 + 900 usuários; analistas N1 presenciais × remotos; região do SIEM livre × dados exclusivamente no Brasil), e não é possível afirmar qual prevalece, nem que o Q&A (mais recente) prevalece automaticamente.",
  obr="Informativo", s=4, p=3,
  imp="Sem regra de precedência, cada divergência pode ser resolvida contra o proponente após a assinatura; afeta preço, prazo e escopo.",
  fw=CC, ctl="Interpretação contratual (identificador a confirmar)", assoc="Correlata",
  rel=["d02_contr_transicao", "d03_contr_usuarios", "d04_contr_usuarios", "d02_contr_regiao"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="Qual é a ordem de precedência entre o RFP, o Anexo I, o material do workshop de 22/10/2026 e as respostas do Q&A em caso de divergência? As respostas do Q&A integram o contrato?",
  resp="Jurídico")
I("d01_req_cmn", D, "1. Apresentação — 1.2", "p. 2 (impressa: 1)",
  '"requisitos para a contratação de serviços de processamento e armazenamento de dados e de computação em nuvem"',
  "Requisito implícito", "Regulatório/Compliance",
  "Inferido: como o cliente se declara sujeito à Resolução CMN nº 4.893/2021, que trata da contratação de serviços de processamento, armazenamento de dados e computação em nuvem, o serviço de SOC (com SIEM possivelmente em nuvem, item 1.2 do Anexo I) deverá atender às exigências que a resolução impõe às contratações da instituição (cláusulas contratuais, acesso do regulador, localização de dados, comunicação ao BCB), ainda que o RFP não as detalhe. Reforçado pelo QT-04 do questionário.",
  obr="Mandatório", nat="Inferida", s=4, p=3,
  imp="Cláusulas e controles regulatórios adicionais (auditoria, acesso do BCB, localização dos dados, plano de saída) com custo e exigências de arquitetura não descritos no RFP.",
  fw=CMN, ctl="Contratação de serviços de processamento, armazenamento e nuvem (identificador a confirmar)",
  rel=["d04_qt04", "d02_siem_regiao"], acao="Esclarecer no Q&A",
  perg="Quais requisitos específicos da Resolução CMN nº 4.893/2021 o Banco exigirá contratualmente do prestador (por exemplo, cláusulas obrigatórias, acesso do Banco Central, localização e transferência dos dados, plano de saída)?",
  resp="Compliance")
I("d01_soc", D, "2. Objeto — 2.1", "p. 2 (impressa: 1)",
  '"serviços gerenciados de Centro de Operações de Segurança (SOC), em regime 24x7x365"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber / Operação/Serviços",
  "Objeto principal: SOC gerenciado em regime ininterrupto (24 horas, 7 dias, 365 dias). Exige escala de turnos e cobertura em feriados.",
  obr="Mandatório", s=3, p=3, imp="Dimensiona a equipe em turnos e o custo de operação contínua.",
  fw=ISO, ctl="A.8.16 Atividades de monitoramento", rel=["d02_monit"], acao="Precificar", resp="Delivery/Operação")
I("d01_iam", D, "2. Objeto — 2.1", "p. 2 (impressa: 1)",
  '"e de gestão de identidades e acessos (IAM)"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Segundo componente do objeto: serviço gerenciado de IAM. O RFP não diz se inclui fornecimento de ferramenta (ver {d02_lac_ferr_iam}).",
  obr="Mandatório", s=3, p=3, imp="Escopo de serviço adicional ao SOC, com equipe e eventual ferramenta próprias.",
  fw=ISO, ctl="A.5.16 Gestão de identidade", rel=["d02_lac_ferr_iam"], acao="Precificar", resp="Pré-venda/Arquitetura")
I("d01_usuarios", D, "2. Objeto — 2.1", "p. 2 (impressa: 1)",
  '"abrangendo aproximadamente 4.500 colaboradores"',
  "Dado de dimensionamento", "Operação/Serviços",
  "Base de dimensionamento declarada no RFP: cerca de 4.500 colaboradores. Diverge da apresentação (6.200 usuários ativos + ~900 das subsidiárias) e do Q&A nº 5 (5.000 usuários). Sem cláusula de precedência, o valor vigente não pode ser presumido.",
  s=4, p=3, imp="Base de cálculo de licenças, esforço de IAM e preço por usuário; variação de até ~58% (4.500 × 7.100).",
  rel=["d03_contr_usuarios", "d04_q5", "d04_contr_usuarios"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Ver pergunta do item {d04_contr_usuarios}.", resp="Pricing/Financeiro")
I("d01_workshop", D, "3. Cronograma — 3.1", "p. 2 (impressa: 1)",
  '"Workshop de apresentação do ambiente 22/10/2026"', "Prazo / marco", "Administrativo do processo",
  "Workshop realizado em 22/10/2026 (material recebido como D03). O RFP não diz se a participação é obrigatória.",
  s=2, p=3, imp="Informações do workshop (D03) trazem ampliação de escopo; ausência implicaria perda de informação.",
  rel=["d03_inv"], resp="Bid Manager")
I("d01_perguntas", D, "3. Cronograma — 3.1", "p. 2 (impressa: 1)",
  '"Prazo final para envio de perguntas 05/11/2026"', "Prazo / marco", "Administrativo do processo",
  "Prazo final de perguntas: 05/11/2026; respostas divulgadas em 12/11/2026 (Q&A Rodada 1 = D04). Várias lacunas e contradições desta matriz dependem de nova rodada; o RFP não prevê rodadas adicionais.",
  obr="Mandatório", s=3, p=3, imp="Perguntas não enviadas no prazo deixam lacunas a tratar como premissas na proposta.",
  rel=["d04_inv"], acao="Esclarecer no Q&A",
  perg="Haverá nova rodada de esclarecimentos, considerando as divergências entre RFP, Anexo I, workshop e Q&A Rodada 1?",
  resp="Bid Manager")
I("d01_entrega", D, "3. Cronograma — 3.1", "p. 2 (impressa: 1)",
  '"Entrega das propostas 20/11/2026, até as 18h"', "Prazo / marco", "Administrativo do processo",
  "Data original de entrega das propostas. Alterada pelo Q&A nº 1 para 27/11/2026, até as 18h.",
  obr="Mandatório", s=5, p=3, imp="Proposta entregue fora do prazo não é considerada.",
  rel=["d04_q1"], vig="Alterado", acao="Atender", resp="Bid Manager")
I("d01_inicio", D, "3. Cronograma — 3.1", "p. 2 (impressa: 1)",
  '"Início previsto dos serviços 01/02/2027"', "Prazo / marco", "Transição/Implantação",
  "Início previsto dos serviços em 01/02/2027, um dia após o fim do contrato do SIEM legado (31/01/2027, sem prorrogação — D03). Data não alterada pelo Q&A, apesar da prorrogação da entrega de propostas.",
  obr="Informativo", s=3, p=3, imp="Define a janela real de transição entre assinatura e início; ver risco combinado {d04_risco_transicao}.",
  rel=["d03_siem_legado", "d04_risco_transicao"], acao="Registrar premissa na proposta", resp="Delivery/Operação")
I("d01_transicao", D, "3. Cronograma — 3.2", "p. 2 (impressa: 1)",
  '"A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato"',
  "Prazo / marco", "Transição/Implantação",
  "Prazo de transição de 30 dias corridos a partir da assinatura. Contradiz o Anexo I, item 4.1 (60 dias).",
  obr="Mandatório", s=4, p=3, imp="Prazo curto exige equipe de transição reforçada; diferença de 30 dias de esforço paralelo.",
  rel=["d02_transicao", "d02_contr_transicao"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Ver pergunta do item {d02_contr_transicao}.", resp="Delivery/Operação")
I("d01_idioma", D, "4. Instruções — 4.1", "p. 3 (impressa: 2)",
  '"A proposta deverá ser redigida em língua portuguesa"', "Instrução de resposta", "Administrativo do processo",
  "Idioma obrigatório: português. Atestados ou certificados em outro idioma podem exigir tradução (não esclarecido).",
  obr="Mandatório", s=2, p=3, imp="Custo de tradução de documentos de habilitação estrangeiros, se houver.",
  acao="Atender", resp="Bid Manager")
I("d01_portal", D, "4. Instruções — 4.1", "p. 3 (impressa: 2)",
  '"enviada exclusivamente pelo portal de fornecedores do Banco"', "Instrução de resposta", "Administrativo do processo",
  "Canal único de entrega: portal de fornecedores. O RFP não informa endereço do portal, necessidade de cadastro prévio, limite de tamanho de arquivo nem formato.",
  obr="Mandatório", s=3, p=3, imp="Falha de cadastro ou upload no portal impede a entrega da proposta.",
  acao="Esclarecer no Q&A",
  perg="Qual o endereço do portal de fornecedores, há cadastro prévio obrigatório (com prazo) e quais os limites de formato e tamanho dos arquivos?",
  resp="Bid Manager")
I("d01_paginas", D, "4. Instruções — 4.2", "p. 3 (impressa: 2)",
  '"A proposta técnica deverá ter no máximo 40 (quarenta) páginas, excluídos os anexos"', "Instrução de resposta",
  "Administrativo do processo",
  "Limite de 40 páginas para a proposta técnica, sem anexos. Não define formatação (fonte, tamanho de página) nem a consequência do excesso (desconsideração das páginas excedentes ou desclassificação).",
  obr="Mandatório", s=3, p=3, imp="Conteúdo excedente pode não ser avaliado na Nota Técnica.",
  acao="Atender", perg="Qual a consequência de exceder 40 páginas e há padrão de formatação (fonte, tamanho de página)?",
  resp="Bid Manager")
I("d01_anexo4_instr", D, "4. Instruções — 4.3", "p. 3 (impressa: 2)",
  '"A proposta comercial deverá ser apresentada conforme a planilha modelo do Anexo IV — Planilha de Preços"',
  "Instrução de resposta", "Comercial/Preço",
  "A proposta comercial deve seguir a planilha modelo do Anexo IV, que não consta do pacote (ver {d01_lac_anexo4}).",
  obr="Mandatório", s=4, p=3, imp="Sem o modelo, a estrutura de preço (itens, unidades, critérios de medição) não pode ser montada no formato exigido.",
  rel=["d01_lac_anexo4"], acao="Esclarecer no Q&A", perg="Ver pergunta do item {d01_lac_anexo4}.", resp="Pricing/Financeiro")
I("d01_lac_anexo4", D, "4. Instruções — 4.3", "p. 3 (impressa: 2)",
  'Não localizado. Trecho que gera a necessidade: "conforme a planilha modelo do Anexo IV — Planilha de Preços"',
  "Lacuna", "Comercial/Preço",
  "O Anexo IV (Planilha de Preços) é citado pelo cliente e não foi fornecido no pacote nem listado pelo usuário. O Anexo II também não aparece (numeração salta de I para III e IV).",
  obr="Mandatório", s=4, p=3, imp="Impede montar a proposta comercial no formato obrigatório e conhecer a estrutura de preço (fixo, por usuário, por EPS).",
  rel=["d01_anexo4_instr"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Solicitamos o envio do Anexo IV — Planilha de Preços. Existe Anexo II? Se sim, solicitamos também o seu envio.",
  resp="Pricing/Financeiro", pend="Lacuna: Anexo IV — Planilha de Preços citado e não fornecido")
I("d01_questionario", D, "4. Instruções — 4.4", "p. 3 (impressa: 2)",
  '"O questionário técnico (planilha anexa) deverá ser integralmente preenchido"', "Instrução de resposta",
  "Administrativo do processo",
  "Preenchimento integral do questionário técnico (D04, aba \"Questionário Técnico\"). O RFP não prevê sanção; a planilha (D04, aba Instruções) prevê desclassificação.",
  obr="Mandatório", s=3, p=3, imp="Questionário incompleto leva à desclassificação, segundo D04.",
  rel=["d04_instr_desclass"], acao="Atender", resp="Pré-venda/Arquitetura")
I("d01_hab_iso", D, "5. Critérios de habilitação — 5.1 a)", "p. 3 (impressa: 2)",
  '"Serão inabilitados os proponentes que não apresentarem" [...] "certificado ISO/IEC 27001 vigente, emitido por organismo acreditado, cujo escopo inclua os serviços de SOC"',
  "Critério eliminatório / de habilitação", "Segurança da Informação/Cyber",
  "Habilitação: certificado ISO/IEC 27001 vigente, de organismo acreditado, com escopo que cubra os serviços de SOC. Probabilidade 5: o texto estabelece inabilitação direta para quem não apresentar o certificado. Não exige escopo para IAM.",
  obr="Mandatório", s=5, p=5, imp="Inabilitação.", fw=ISO, ctl="Certificação do SGSI (requisitos das cláusulas 4 a 10)",
  rel=["d04_qt01"], acao="Atender",
  perg="O certificado pode estar em nome de empresa do mesmo grupo econômico do proponente?", resp="Compliance")
I("d01_hab_atestados", D, "5. Critérios de habilitação — 5.1 b)", "p. 3 (impressa: 2)",
  '"no mínimo 3 (três) atestados de capacidade técnica de prestação de serviços de SOC para instituições financeiras, com ambiente de no mínimo 2.000 usuários"',
  "Critério eliminatório / de habilitação", "Segurança da Informação/Cyber / Administrativo do processo",
  "Habilitação: três ou mais atestados de SOC para instituições financeiras com ambiente de 2.000+ usuários. Probabilidade 5: inabilitação direta prevista no caput do 5.1. Não há exigência de atestado de IAM.",
  obr="Mandatório", s=5, p=5, imp="Inabilitação.", rel=["d01_amb_atestados"], acao="Atender", resp="Bid Manager")
I("d01_amb_atestados", D, "5. Critérios de habilitação — 5.1 b)", "p. 3 (impressa: 2)",
  '"para instituições financeiras, com ambiente de no mínimo 2.000 usuários"', "Ambiguidade",
  "Administrativo do processo",
  "Não está claro (i) se cada atestado deve comprovar 2.000 usuários ou se a soma basta; (ii) se seguradoras, gestoras, cooperativas de crédito e fintechs contam como \"instituições financeiras\"; (iii) se os atestados podem ser de contratos encerrados.",
  s=5, p=3, imp="Interpretação restritiva pode inabilitar o proponente.", rel=["d01_hab_atestados"],
  vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O mínimo de 2.000 usuários vale para cada atestado individualmente? Seguradoras, gestoras de investimento, cooperativas de crédito e instituições de pagamento são aceitas como instituições financeiras? Atestados de contratos já encerrados são aceitos?",
  resp="Bid Manager")
I("d01_hab_soc_br", D, "5. Critérios de habilitação — 5.1 c)", "p. 3 (impressa: 2)",
  '"comprovação de que o SOC está localizado em território nacional"', "Critério eliminatório / de habilitação",
  "Operação/Serviços / Regulatório/Compliance",
  "Habilitação: SOC localizado no Brasil, confirmado pelo Q&A nº 2. Probabilidade 5: inabilitação direta prevista no caput do 5.1. O RFP não define o documento que comprova a localização.",
  obr="Mandatório", s=5, p=5, imp="Inabilitação; impede uso de SOC no exterior (follow-the-sun).",
  fw=ISO, ctl="Segurança física e localização das instalações (identificador a confirmar)", assoc="Correlata",
  rel=["d04_q2", "d04_q6"], acao="Atender",
  perg="Qual documento será aceito como comprovação da localização do SOC em território nacional?", resp="Delivery/Operação")
I("d01_equipe_cert", D, "5. Critérios de habilitação — 5.2", "p. 3 (impressa: 2)",
  '"O proponente deverá possuir equipe técnica devidamente certificada"', "Critério eliminatório / de habilitação",
  "Pessoas/Equipe",
  "Exigência posta na seção de habilitação, mas fora da lista do 5.1 (que tem consequência expressa de inabilitação). Classificado como critério de habilitação por estar na seção 5; ver ambiguidade {d01_amb_equipe_cert}.",
  obr="Mandatório", s=5, p=3, imp="Possível inabilitação se o cliente considerar insuficientes as certificações apresentadas.",
  rel=["d01_amb_equipe_cert", "d02_coord_cissp", "d04_qt06"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Ver pergunta do item {d01_amb_equipe_cert}.", resp="RH/Staffing")
I("d01_amb_equipe_cert", D, "5. Critérios de habilitação — 5.2", "p. 3 (impressa: 2)",
  '"equipe técnica devidamente certificada"', "Ambiguidade", "Pessoas/Equipe",
  "\"Devidamente certificada\" não indica quais certificações, quantos profissionais, a forma de comprovação, nem se o não atendimento inabilita. Termos semelhantes e igualmente vagos aparecem no QT-06 (\"certificações reconhecidas pelo mercado\"); só o coordenador tem certificação definida (CISSP, Anexo I 5.1).",
  s=4, p=3, imp="Risco de inabilitação ou de perda de pontuação em \"Qualificação da equipe\" (20 pontos) por critério subjetivo.",
  rel=["d01_equipe_cert", "d02_coord_cissp", "d04_qt06"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Quais certificações são exigidas, para quais perfis e em que quantidade, como devem ser comprovadas na proposta e o item 5.2 é causa de inabilitação?",
  resp="RH/Staffing")
I("d01_amb_anexo3", D, "5. Critérios de habilitação × Anexo III", "p. 3 (impressa: 2) · p. 6 (impressa: 5) (OCR)",
  'A: "Serão inabilitados os proponentes que não apresentarem" · B: "Esta declaração deverá ser entregue assinada pelo representante legal do proponente junto com a proposta, sob pena de inabilitação."',
  "Ambiguidade", "Administrativo do processo",
  "A lista de causas de inabilitação do 5.1 (a–c) não menciona o Anexo III, que só aparece como página digitalizada ao final do PDF e também prevê inabilitação. O corpo do RFP não referencia o Anexo III em nenhuma seção. Não está claro se a lista do 5.1 é exaustiva nem se há outros anexos com exigências de habilitação (o Anexo II não aparece).",
  s=5, p=3, imp="Exigência eliminatória fácil de omitir por estar só em imagem no fim do documento.",
  rel=["d01_anexo3_decl"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Confirmam que a declaração do Anexo III é documento de habilitação adicional aos itens do 5.1? Existem outros documentos de habilitação ou um Anexo II não enviado?",
  resp="Bid Manager")
I("d01_nota_final", D, "6. Critérios de avaliação — 6.1", "p. 4 (impressa: 3)",
  '"A nota final será composta pela Nota Técnica (peso de 60%) e pela Nota de Preço (peso de 40%)"',
  "Critério de avaliação / pontuação", "Comercial/Preço",
  "Julgamento técnica e preço, 60/40. Peso técnico relevante favorece proposta de maior qualidade.",
  obr="Informativo", s=3, p=3, imp="Orienta o equilíbrio entre investimento na proposta técnica e agressividade de preço.",
  rel=["d01_lac_nota_preco"], acao="Atender", resp="Bid Manager")
I("d01_lac_nota_preco", D, "6. Critérios de avaliação — 6.1", "p. 4 (impressa: 3)",
  'Não localizado. Trecho que gera a necessidade: "pela Nota de Preço (peso de 40%)"', "Lacuna", "Comercial/Preço",
  "O RFP não traz a fórmula da Nota de Preço (proporcional ao menor preço, faixas, preço de referência, critério de inexequibilidade), nem como a Nota Técnica de até 60 pontos é normalizada antes da ponderação.",
  s=4, p=3, imp="Sem a fórmula não é possível simular o efeito do preço na nota final nem calibrar a estratégia de preço.",
  rel=["d01_nota_final"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Qual a fórmula de cálculo da Nota de Preço e da nota final (incluindo normalização da Nota Técnica) e há critério de inexequibilidade de preço?",
  resp="Pricing/Financeiro")
I("d01_nota_tecnica", D, "6. Critérios de avaliação — 6.2", "p. 4 (impressa: 3)",
  '"A Nota Técnica, de no máximo 60 (sessenta) pontos, será atribuída conforme os critérios abaixo"',
  "Critério de avaliação / pontuação", "Administrativo do processo",
  "Nota Técnica máxima de 60 pontos; critérios listados na tabela do 6.2. Não há rubricas ou subcritérios para atribuição das notas.",
  s=3, p=3, imp="Sem rubricas, a pontuação é discricionária.", rel=["d01_contr_pontos", "d04_contr_pontuacao"],
  acao="Esclarecer no Q&A", perg="Há subcritérios ou rubricas para a atribuição dos pontos de cada critério técnico?",
  resp="Bid Manager")
I("d01_crit_metodologia", D, "6. Critérios de avaliação — 6.2 (tabela)", "p. 4 (impressa: 3)",
  '"Metodologia de operação do SOC 20"', "Critério de avaliação / pontuação", "Operação/Serviços",
  "Critério técnico: metodologia de operação do SOC, até 20 pontos.", s=3, p=3,
  imp="Peso alto; exige descrição detalhada de processos de detecção, triagem e resposta.", fw=ITIL,
  ctl="Prática de gerenciamento de incidentes", assoc="Correlata", acao="Atender", resp="Pré-venda/Arquitetura")
I("d01_crit_equipe", D, "6. Critérios de avaliação — 6.2 (tabela)", "p. 4 (impressa: 3)",
  '"Qualificação da equipe 20"', "Critério de avaliação / pontuação", "Pessoas/Equipe",
  "Critério técnico: qualificação da equipe, até 20 pontos. Relaciona-se à exigência vaga de \"equipe devidamente certificada\" (5.2).",
  s=3, p=3, imp="Peso alto; depende de currículos e certificações da equipe alocada.", rel=["d01_amb_equipe_cert"],
  acao="Atender", resp="RH/Staffing")
I("d01_crit_ferramentas", D, "6. Critérios de avaliação — 6.2 (tabela)", "p. 4 (impressa: 3)",
  '"Ferramentas e tecnologia 15"', "Critério de avaliação / pontuação", "Técnico/Arquitetura",
  "Critério técnico: ferramentas e tecnologia, até 15 pontos.", s=3, p=3,
  imp="Escolha do SIEM e de eventual SOAR/threat intelligence influencia a nota.", rel=["d04_oport_soar_ti"],
  acao="Atender", resp="Pré-venda/Arquitetura")
I("d01_crit_transicao", D, "6. Critérios de avaliação — 6.2 (tabela)", "p. 4 (impressa: 3)",
  '"Plano de transição 10"', "Critério de avaliação / pontuação", "Transição/Implantação",
  "Critério técnico: plano de transição, até 10 pontos. O plano deve tratar o prazo divergente (30 × 60 dias) e a operação paralela.",
  s=3, p=3, imp="Plano de transição sem premissa de prazo definida pode perder pontos.", rel=["d02_contr_transicao"],
  acao="Atender", resp="Delivery/Operação")
I("d01_contr_pontos", D, "6. Critérios de avaliação — 6.2", "p. 4 (impressa: 3)",
  'A: "de no máximo 60 (sessenta) pontos" · B: "Metodologia de operação do SOC 20" [...] "Qualificação da equipe 20" [...] "Ferramentas e tecnologia 15" [...] "Plano de transição 10"',
  "Contradição", "Administrativo do processo",
  "A soma das pontuações máximas da tabela é 65 (20 + 20 + 15 + 10), mas a Nota Técnica máxima declarada é 60. A nota de corte de 70% (6.3) resulta em 42 pontos (sobre 60) ou 45,5 (sobre 65), e o peso relativo de cada critério muda conforme a correção.",
  s=4, p=3, imp="Incerteza sobre a nota mínima eliminatória e sobre o peso de cada critério.",
  rel=["d01_nota_tecnica", "d01_nota_corte"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A soma das pontuações máximas dos critérios do item 6.2 é 65, e a Nota Técnica máxima é 60. Qual valor está correto e qual a pontuação de cada critério?",
  resp="Bid Manager")
I("d01_nota_corte", D, "6. Critérios de avaliação — 6.3", "p. 4 (impressa: 3)",
  '"Serão desclassificadas as propostas com Nota Técnica inferior a 70% (setenta por cento) da pontuação máxima"',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Nota técnica mínima eliminatória (70% do máximo). A base de cálculo é incerta (60 ou 65 pontos) e pode ser afetada por descontos da aba oculta \"Pesos\" (2 pontos por \"Não atende\" em requisito não obrigatório).",
  obr="Mandatório", s=5, p=3, imp="Desclassificação.", rel=["d01_contr_pontos", "d04_regra_oculta"],
  acao="Atender", resp="Bid Manager")
I("d01_desempate", D, "6. Critérios de avaliação — 6.4", "p. 4 (impressa: 3)",
  '"Em caso de empate na nota final, prevalecerá a proposta de menor preço"', "Critério de avaliação / pontuação",
  "Comercial/Preço", "Desempate pelo menor preço.", s=2, p=3, imp="Efeito marginal.", resp="Pricing/Financeiro")
I("d01_vigencia", D, "7. Condições comerciais — 7.1", "p. 5 (impressa: 4)",
  '"O contrato terá vigência de 36 (trinta e seis) meses, prorrogável por iguais períodos mediante acordo entre as partes"',
  "Obrigação contratual", "Jurídico/Contratual",
  "Vigência de 36 meses, prorrogável por acordo. Horizonte para amortização de transição e investimentos.",
  obr="Informativo", s=2, p=3, imp="Base do cálculo de amortização.", fw=CC, ctl="Contratos (identificador a confirmar)",
  assoc="Correlata", acao="Precificar", resp="Pricing/Financeiro")
I("d01_reajuste", D, "7. Condições comerciais — 7.2", "p. 5 (impressa: 4)",
  '"Os preços serão reajustados anualmente pela variação do IPCA"', "Obrigação contratual", "Financeiro",
  "Reajuste anual pelo IPCA. Não define a data-base (data da proposta ou da assinatura); custos de mão de obra especializada podem crescer acima do IPCA.",
  obr="Mandatório", s=3, p=3, imp="Possível descasamento entre reajuste e custo de pessoal.", acao="Esclarecer no Q&A",
  perg="Qual a data-base do reajuste anual pelo IPCA: data de entrega da proposta ou de assinatura do contrato?",
  resp="Pricing/Financeiro")
I("d01_pagamento", D, "7. Condições comerciais — 7.3", "p. 5 (impressa: 4)",
  '"O pagamento será efetuado em até 60 (sessenta) dias após o aceite da nota fiscal"', "Obrigação contratual",
  "Financeiro",
  "Prazo de pagamento de até 60 dias contados do aceite da nota fiscal (o prazo de aceite não é definido). Probabilidade 5: o custo financeiro decorre diretamente do texto, sem depender de evento incerto.",
  obr="Mandatório", s=3, p=5, imp="Custo de capital de giro de ao menos dois meses de faturamento, a embutir no preço.",
  acao="Precificar", perg="Qual o prazo máximo para o aceite da nota fiscal pelo Banco?", resp="Pricing/Financeiro")
I("d01_multa", D, "7. Condições comerciais — 7.4", "p. 5 (impressa: 4)",
  '"O descumprimento de qualquer nível de serviço (SLA) previsto no Anexo I sujeitará a Contratada a multa de 10% (dez por cento) do valor mensal do contrato, por ocorrência"',
  "Penalidade / multa / glosa", "Jurídico/Contratual / Financeiro",
  "Multa de 10% do valor mensal por ocorrência, para qualquer SLA, sem teto, sem gradação e sem distinção de gravidade. Probabilidade 4: a multa é automática a cada ocorrência e o cliente, no Q&A nº 4, recusou-se a estabelecer limite (\"As condições do item 7 permanecem inalteradas\").",
  obr="Mandatório", s=5, p=4, imp="Dez ocorrências no mês anulam o faturamento mensal; exposição sem limite.", fw=CC,
  ctl="Cláusula penal (identificador a confirmar)", assoc="Correlata",
  rel=["d04_q4", "d02_amb_sla_multa", "d04_risco_exposicao"], acao="Propor exceção/ressalva",
  perg="O Banco aceitaria limitar as multas a um percentual do valor mensal (por exemplo, 10% ao mês) e graduá-las conforme o SLA descumprido?",
  resp="Jurídico")
I("d01_resp_ilimitada", D, "7. Condições comerciais — 7.5", "p. 5 (impressa: 4)",
  '"A Contratada responderá de forma integral e ilimitada por quaisquer danos decorrentes de incidentes de segurança ocorridos no ambiente do Contratante"',
  "Obrigação contratual", "Jurídico/Contratual",
  "Responsabilidade integral e ilimitada por quaisquer danos de incidentes no ambiente do Contratante, sem nexo causal com falha da Contratada, sem exclusão de lucros cessantes e sem teto.",
  obr="Mandatório", s=5, p=3, imp="Exposição jurídica e financeira ilimitada; pode inviabilizar seguro e a participação.",
  fw=CC, ctl="Responsabilidade civil (identificador a confirmar)", assoc="Correlata",
  rel=["d01_seguro", "d04_risco_exposicao"], acao="Propor exceção/ressalva",
  perg="O Banco aceita limitar a responsabilidade da Contratada a danos diretos comprovadamente causados por sua culpa, até um teto (por exemplo, 12 meses de faturamento)?",
  resp="Jurídico")
I("d01_seguro", D, "7. Condições comerciais — 7.6", "p. 5 (impressa: 4)",
  '"A Contratada deverá manter seguro de responsabilidade civil cibernética em valor compatível com os riscos do contrato"',
  "Obrigação contratual", "Jurídico/Contratual / Financeiro",
  "Seguro cibernético obrigatório durante o contrato; valor não definido (\"compatível com os riscos\"), o que, combinado com a responsabilidade ilimitada (7.5), não tem referência objetiva.",
  obr="Mandatório", s=3, p=3, imp="Custo de prêmio não estimável sem valor segurado definido.", rel=["d01_resp_ilimitada"],
  acao="Esclarecer no Q&A",
  perg="Qual o valor mínimo segurado da apólice de responsabilidade civil cibernética e o Banco deve constar como beneficiário?",
  resp="Jurídico")
I("d01_subcontratacao", D, "7. Condições comerciais — 7.7", "p. 5 (impressa: 4)",
  '"É vedada a subcontratação, total ou parcial, do objeto deste contrato"', "Restrição", "Jurídico/Contratual",
  "Vedação total de subcontratação. Afeta o uso de parceiros (SOC parceiro, MSSP, fabricante de SIEM, provedor de nuvem). Ver {d02_amb_subcontratacao}.",
  obr="Mandatório", s=4, p=3, imp="Exige execução integral com equipe e estrutura próprias.",
  fw=ISO, ctl="A.5.19 Segurança da informação nas relações com fornecedores", assoc="Correlata",
  rel=["d02_amb_subcontratacao"], acao="Esclarecer no Q&A", perg="Ver pergunta do item {d02_amb_subcontratacao}.",
  resp="Jurídico")
I("d01_confidencialidade", D, "7. Condições comerciais — 7.8", "p. 5 (impressa: 4)",
  '"As obrigações de confidencialidade vigorarão por 5 (cinco) anos após o término do contrato"', "Obrigação contratual",
  "Jurídico/Contratual", "Confidencialidade de 5 anos após o término.", obr="Mandatório", s=2, p=3,
  imp="Obrigação de longo prazo; baixo custo.", fw=ISO, ctl="A.6.6 Acordos de confidencialidade ou de não divulgação",
  acao="Atender", resp="Jurídico")
I("d01_anexo3_decl", D, "Anexo III — Declaração de Localização de Dados", "p. 6 (impressa: 5) (OCR)",
  '"Esta declaração deverá ser entregue assinada pelo representante legal do proponente junto com a proposta, sob pena de inabilitação."',
  "Critério eliminatório / de habilitação", "Regulatório/Compliance / Administrativo do processo",
  "Declaração assinada pelo representante legal, entregue com a proposta. Conteúdo lido por OCR (página digitalizada). Probabilidade 5: o texto prevê inabilitação direta para a falta da declaração.",
  obr="Mandatório", s=5, p=5, imp="Inabilitação.", rel=["d01_amb_anexo3", "d01_anexo3_dados"], acao="Atender",
  resp="Bid Manager")
I("d01_anexo3_dados", D, "Anexo III — Declaração de Localização de Dados", "p. 6 (impressa: 5) (OCR)",
  '"todos os dados do Banco Horizonte Fictício S.A., incluindo os registros (logs) de segurança, serão armazenados e processados exclusivamente em território nacional, durante toda a vigência do contrato"',
  "Restrição", "Infraestrutura/Cloud / Regulatório/Compliance",
  "Todos os dados do cliente, inclusive logs, devem ser armazenados e processados apenas no Brasil durante a vigência. Impede SIEM/SaaS hospedado em região estrangeira, inclusive processamento por ferramentas de análise ou threat intelligence fora do país. Contradiz o Anexo I 1.2 (região livre).",
  obr="Mandatório", s=5, p=3, imp="Restringe as plataformas de SIEM elegíveis; declaração falsa pode gerar inabilitação ou rescisão.",
  fw=LGPD, ctl="Art. 33 (transferência internacional de dados)", assoc="Correlata",
  rel=["d02_contr_regiao", "d01_anexo3_decl"], acao="Atender", resp="Pré-venda/Arquitetura")

# =============================================================== D02 — Anexo I (DOCX)
D = "D02"
I("d02_inv", D, "Documento inteiro — seções 1 a 6", "§ 1 a § 6 (página: não disponível)",
  '"RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Versão 1.0 — 15/10/2026"', "Registro de cobertura",
  "Administrativo do processo",
  "Inventário: Word com 22 parágrafos e 6 seções numeradas (SOC, SLA, IAM, Transição, Equipe, Responsabilidades do Contratante); sem tabelas, marcas de revisão ou comentários. Leitura integral. Localizador por seção/item (Word sem paginação fixa).")
I("d02_monit", D, "1. Serviços de SOC — 1.1", "§ 1. SERVIÇOS DE SOC — item 1.1",
  '"O proponente deverá prestar serviço de monitoramento contínuo de eventos de segurança, em regime 24x7x365"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Monitoramento contínuo 24x7x365; repete o objeto do RFP 2.1.", obr="Mandatório", s=3, p=3,
  imp="Mesmo impacto do item do RFP (equipe em turnos).", fw=CSF, ctl="DE.CM — Continuous Monitoring",
  rel=["d01_soc"], vig="Duplicado", acao="Precificar", resp="Delivery/Operação")
I("d02_siem", D, "1. Serviços de SOC — 1.2", "§ 1. SERVIÇOS DE SOC — item 1.2",
  '"O proponente deverá fornecer a solução de SIEM"', "Requisito funcional / de serviço", "Técnico/Arquitetura",
  "O proponente fornece o SIEM (licenças, infraestrutura e operação). Custo depende de volumetria (EPS) e retenção, ambas sem definição (Q&A nº 3).",
  obr="Mandatório", s=4, p=3, imp="Licenciamento e infraestrutura do SIEM são o principal custo variável da proposta.",
  fw=ISO, ctl="A.8.15 Registro de logs", assoc="Correlata", rel=["d04_q3"], acao="Precificar",
  resp="Pré-venda/Arquitetura")
I("d02_siem_regiao", D, "1. Serviços de SOC — 1.2", "§ 1. SERVIÇOS DE SOC — item 1.2",
  '"podendo esta ser disponibilizada em nuvem pública, em região de livre escolha do proponente"', "Premissa do cliente",
  "Infraestrutura/Cloud",
  "Permite SIEM em nuvem pública em qualquer região. Conflita com o Anexo III (dados exclusivamente no Brasil) e com o regime da Resolução CMN nº 4.893/2021 citado no RFP 1.2.",
  obr="Desejável", s=5, p=3, imp="Escolher região estrangeira com base neste item leva a descumprir o Anexo III (eliminatório).",
  fw=ISO, ctl="A.5.23 Segurança da informação para uso de serviços em nuvem", assoc="Correlata",
  rel=["d02_contr_regiao", "d01_anexo3_dados", "d01_req_cmn"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Ver pergunta do item {d02_contr_regiao}.", resp="Pré-venda/Arquitetura")
I("d02_contr_regiao", D, "Anexo I 1.2 × RFP Anexo III", "A: § 1. SERVIÇOS DE SOC — item 1.2 · B: D01 p. 6 (impressa: 5) (OCR)",
  'A: "podendo esta ser disponibilizada em nuvem pública, em região de livre escolha do proponente" · B: "serão armazenados e processados exclusivamente em território nacional, durante toda a vigência do contrato"',
  "Contradição", "Infraestrutura/Cloud / Regulatório/Compliance",
  "O Anexo I permite região de nuvem livre; o Anexo III (declaração eliminatória) exige armazenamento e processamento exclusivamente no Brasil. Sem cláusula de precedência ({d01_precedencia}), seguir o Anexo I pode gerar inabilitação.",
  s=5, p=3, imp="Define a arquitetura e o custo do SIEM (regiões brasileiras costumam ter oferta e preço diferentes) e a elegibilidade da proposta.",
  fw=LGPD, ctl="Art. 33 (transferência internacional de dados)", assoc="Correlata",
  rel=["d02_siem_regiao", "d01_anexo3_dados", "d01_precedencia"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O Anexo I, item 1.2, permite SIEM em nuvem pública em região de livre escolha, e o Anexo III exige armazenamento e processamento exclusivamente no Brasil. Confirmam que a região da nuvem deve ser obrigatoriamente brasileira, inclusive para backup, réplicas e processamento analítico?",
  resp="Pré-venda/Arquitetura")
I("d02_amb_subcontratacao", D, "Anexo I 1.2 × RFP 7.7", "A: D01 p. 5 (impressa: 4) · B: § 1. SERVIÇOS DE SOC — item 1.2",
  'A: "É vedada a subcontratação, total ou parcial, do objeto deste contrato" · B: "podendo esta ser disponibilizada em nuvem pública"',
  "Ambiguidade", "Jurídico/Contratual / Infraestrutura/Cloud",
  "Não está claro se o uso de provedor de nuvem pública, de SIEM em SaaS, de suporte do fabricante ou de feeds de threat intelligence configura subcontratação vedada pelo 7.7.",
  s=4, p=3, imp="Interpretação ampla da vedação inviabiliza arquiteturas em nuvem e parcerias.",
  rel=["d01_subcontratacao", "d02_siem_regiao"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A contratação de provedor de nuvem pública, de SIEM em modalidade SaaS e de suporte de fabricantes de software é considerada subcontratação vedada pelo item 7.7?",
  resp="Jurídico")
I("d02_retencao12", D, "1. Serviços de SOC — 1.3", "§ 1. SERVIÇOS DE SOC — item 1.3",
  '"Os registros (logs) de segurança deverão ser retidos por no mínimo 12 (doze) meses"', "Requisito não funcional",
  "Segurança da Informação/Cyber", "Retenção mínima de 12 meses; o QT-03 especifica retenção \"online\".",
  obr="Mandatório", s=3, p=3, imp="Armazenamento proporcional ao EPS (não informado).", fw=ISO, ctl="A.8.15 Registro de logs",
  rel=["d02_amb_retencao", "d04_qt03"], acao="Precificar", resp="Pré-venda/Arquitetura")
I("d02_monit_ativos", D, "1. Serviços de SOC — 1.4", "§ 1. SERVIÇOS DE SOC — item 1.4",
  '"O SIEM deverá ser integrado a todos os ativos relevantes do Contratante"', "Requisito funcional / de serviço",
  "Técnico/Arquitetura",
  "Integração do SIEM a \"todos os ativos relevantes\", sem lista ou critério de relevância. O ambiente inclui 850 servidores, 2 data centers e 2 nuvens públicas (D03); a volumetria foi negada no Q&A nº 3.",
  obr="Mandatório", s=4, p=3, imp="Escopo de integração aberto; cada nova fonte gera esforço e licença.",
  fw=CIS, ctl="Controle 8 — Audit Log Management", assoc="Correlata", rel=["d02_amb_ativos", "d04_q3"],
  acao="Esclarecer no Q&A", perg="Ver pergunta do item {d02_amb_ativos}.", resp="Pré-venda/Arquitetura")
I("d02_amb_ativos", D, "1. Serviços de SOC — 1.4", "§ 1. SERVIÇOS DE SOC — item 1.4", '"todos os ativos relevantes"',
  "Ambiguidade", "Técnico/Arquitetura",
  "\"Ativos relevantes\" não é definido: não se sabe quem decide a relevância, se inclui estações de trabalho, rede, aplicações, SaaS e as duas nuvens públicas, nem se ativos das subsidiárias entram.",
  s=4, p=3, imp="Escopo de integração pode crescer após a assinatura sem contrapartida de preço.",
  rel=["d02_monit_ativos", "d03_subsidiarias"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Qual a lista ou o critério de \"ativos relevantes\" (tipos e quantidades de fontes de log: servidores, rede, estações, aplicações, nuvens públicas) e quem define a relevância? Novas integrações após a transição serão remuneradas?",
  resp="Pré-venda/Arquitetura")
I("d02_resposta", D, "1. Serviços de SOC — 1.5", "§ 1. SERVIÇOS DE SOC — item 1.5",
  '"O serviço deverá contemplar resposta a incidentes, incluindo contenção, erradicação"', "Requisito funcional / de serviço",
  "Segurança da Informação/Cyber",
  "Resposta a incidentes com contenção e erradicação. Não define se é remota ou presencial, se inclui forense e recuperação, nem limites de horas. Atuação direta no ambiente do cliente combinada com responsabilidade ilimitada (7.5) aumenta a exposição.",
  obr="Mandatório", s=4, p=3, imp="Esforço de resposta sem teto definido; exposição jurídica ao atuar no ambiente do cliente.",
  fw=ISO, ctl="A.5.26 Resposta a incidentes de segurança da informação", rel=["d01_resp_ilimitada"],
  acao="Esclarecer no Q&A",
  perg="A resposta a incidentes inclui atuação presencial, análise forense e recuperação? Há limite de horas ou incidentes por mês incluído no preço?",
  resp="Segurança/Cyber")
I("d02_relatorio_pos", D, "1. Serviços de SOC — 1.5", "§ 1. SERVIÇOS DE SOC — item 1.5",
  '"elaboração de relatório pós-incidente"', "Entregável", "Segurança da Informação/Cyber",
  "Relatório pós-incidente; prazo e formato não definidos.", obr="Mandatório", s=2, p=3,
  imp="Esforço de documentação por incidente.", fw=ISO, ctl="A.5.27 Aprendizado com incidentes de segurança da informação",
  acao="Atender", resp="Segurança/Cyber")
I("d02_retencao5", D, "1. Serviços de SOC — 1.6", "§ 1. SERVIÇOS DE SOC — item 1.6",
  '"Para fins de auditoria, os logs deverão ser mantidos por 5 (cinco) anos"', "Requisito não funcional",
  "Segurança da Informação/Cyber / Regulatório/Compliance",
  "Retenção de 5 anos para auditoria, superior à vigência de 36 meses. Ver ambiguidade {d02_amb_retencao}.",
  obr="Mandatório", s=4, p=3, imp="Armazenamento de longo prazo; retenção além do contrato sem regra de custeio.",
  fw=ISO, ctl="A.5.33 Proteção de registros", assoc="Correlata", rel=["d02_amb_retencao", "d02_lac_saida"],
  acao="Precificar", resp="Pré-venda/Arquitetura")
I("d02_amb_retencao", D, "1. Serviços de SOC — 1.3 × 1.6", "§ 1. SERVIÇOS DE SOC — itens 1.3 e 1.6",
  'A: "deverão ser retidos por no mínimo 12 (doze) meses" · B: "os logs deverão ser mantidos por 5 (cinco) anos"',
  "Ambiguidade", "Segurança da Informação/Cyber",
  "Dois prazos de retenção para os mesmos logs: 12 meses (1.3) e 5 anos (1.6). Leitura provável: 12 meses online (QT-03) e 5 anos em arquivo, mas o texto não diz isso; também não informa se os 24 meses de logs históricos a migrar (D03) contam na retenção.",
  s=4, p=3, imp="Diferença de custo de armazenamento entre 12 e 60 meses, sem EPS conhecido.",
  rel=["d02_retencao12", "d02_retencao5", "d04_qt03", "d03_migracao"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Confirmam que os logs devem ficar 12 meses disponíveis online e 5 anos em arquivo (cold storage)? Qual o tempo máximo de recuperação dos logs arquivados?",
  resp="Pré-venda/Arquitetura")
I("d02_lgpd", D, "1. Serviços de SOC — 1.3 · 3. IAM — 3.1", "§ 1 — item 1.3 · § 3 — item 3.1",
  '"Os registros (logs) de segurança deverão ser retidos" [...] "Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"',
  "Requisito implícito", "Privacidade/Proteção de Dados",
  "Inferido: logs de segurança e dados de identidade (admissão, movimentação, desligamento) contêm dados pessoais de colaboradores e clientes; ao tratá-los por conta do Banco, o proponente atua como operador na LGPD. O RFP não traz cláusula de proteção de dados nem acordo de tratamento (DPA).",
  obr="Mandatório", nat="Inferida", s=4, p=3,
  imp="Obrigações de operador (seguir instruções, segurança, notificação de incidentes) e responsabilidade solidária possível, sem regra contratual definida.",
  fw=LGPD, ctl="Art. 39 (tratamento pelo operador segundo instruções do controlador)",
  rel=["d01_resp_ilimitada"], acao="Esclarecer no Q&A",
  perg="O Banco firmará acordo de tratamento de dados pessoais (DPA) com a Contratada, na qualidade de operadora, definindo instruções, prazos de notificação de incidentes e regras de eliminação?",
  resp="Compliance")
I("d02_lac_saida", D, "1. Serviços de SOC — 1.6 × RFP 7.1", "§ 1 — item 1.6 · D01 p. 5 (impressa: 4)",
  'Não localizado. Trechos que geram a necessidade: "os logs deverão ser mantidos por 5 (cinco) anos" · "O contrato terá vigência de 36 (trinta e seis) meses"',
  "Lacuna", "Continuidade / Jurídico/Contratual",
  "Não há regra de término e saída: devolução dos logs e dados, formato de exportação, transição para o próximo fornecedor, e quem custeia a retenção de 5 anos após o fim do contrato de 36 meses.",
  s=3, p=3, imp="Obrigação de guarda de dados após o contrato sem remuneração; custos de saída não previstos.",
  fw=ISO, ctl="A.5.20 Abordagem da segurança da informação nos contratos com fornecedores", assoc="Correlata",
  rel=["d02_retencao5", "d01_req_cmn"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Ao término do contrato, como devem ser devolvidos os logs e dados (formato e prazo) e quem custeia a guarda dos logs pelo período restante de 5 anos?",
  resp="Jurídico")
I("d02_sla15", D, "2. Níveis de serviço — 2.1", "§ 2. NÍVEIS DE SERVIÇO (SLA) — item 2.1",
  '"Tempo máximo para início do tratamento de incidentes críticos: 15 (quinze) minutos"', "SLA / KPI",
  "Operação/Serviços",
  "Início de tratamento de incidente crítico em até 15 minutos, 24x7. A definição de \"crítico\" depende de matriz do Contratante não fornecida (2.4); o marco inicial da medição não é definido.",
  obr="Mandatório", s=4, p=3, imp="Exige analistas disponíveis em todos os turnos; cada violação gera multa de 10% do valor mensal (7.4).",
  fw=ITIL, ctl="Práticas de gerenciamento de incidentes e de nível de serviço", assoc="Correlata",
  rel=["d02_lac_matriz", "d02_lac_apuracao", "d01_multa"], acao="Precificar", resp="Delivery/Operação")
I("d02_sla_disp", D, "2. Níveis de serviço — 2.2", "§ 2. NÍVEIS DE SERVIÇO (SLA) — item 2.2",
  '"Disponibilidade mínima mensal da plataforma SIEM: 99,9%"', "SLA / KPI", "Infraestrutura/Cloud",
  "Disponibilidade mensal de 99,9% do SIEM (cerca de 43 minutos de indisponibilidade por mês). Não trata janelas de manutenção nem indisponibilidade do provedor de nuvem.",
  obr="Mandatório", s=3, p=3, imp="Exige arquitetura redundante; SLA do provedor de nuvem precisa ser igual ou superior.",
  fw=ITIL, ctl="Prática de gerenciamento de disponibilidade", assoc="Correlata", rel=["d02_lac_apuracao"],
  acao="Precificar", resp="Pré-venda/Arquitetura")
I("d02_sla_relatorio", D, "2. Níveis de serviço — 2.3", "§ 2. NÍVEIS DE SERVIÇO (SLA) — item 2.3",
  '"Relatório mensal de indicadores, a ser entregue até o 5º dia útil do mês subsequente"', "SLA / KPI",
  "Operação/Serviços", "Relatório mensal de indicadores até o 5º dia útil. Conteúdo do relatório não definido.",
  obr="Mandatório", s=2, p=3, imp="Atraso pode ser tratado como descumprimento de SLA sujeito à multa do 7.4.",
  fw=ITIL, ctl="Prática de gerenciamento de nível de serviço", assoc="Correlata", rel=["d02_amb_sla_multa"],
  acao="Atender", resp="Delivery/Operação")
I("d02_lac_matriz", D, "2. Níveis de serviço — 2.4", "§ 2. NÍVEIS DE SERVIÇO (SLA) — item 2.4",
  'Não localizado. Trecho que gera a necessidade: "A classificação de criticidade dos incidentes seguirá a matriz de classificação do Contratante."',
  "Lacuna", "Operação/Serviços",
  "A matriz de classificação de criticidade é citada pelo cliente e não foi fornecida. Ela define quais incidentes ficam sujeitos ao SLA de 15 minutos.",
  s=4, p=3, imp="Sem a matriz não é possível estimar o volume de incidentes críticos, dimensionar a equipe nem avaliar a exposição a multas.",
  rel=["d02_sla15"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Solicitamos o envio da matriz de classificação de criticidade de incidentes do Banco e o histórico mensal de incidentes por criticidade.",
  resp="Delivery/Operação", pend="Lacuna: matriz de classificação de criticidade do Contratante citada e não fornecida")
I("d02_lac_apuracao", D, "2. Níveis de serviço", "§ 2. NÍVEIS DE SERVIÇO (SLA) — itens 2.1 a 2.3",
  'Não localizado. Trecho que gera a necessidade: "Tempo máximo para início do tratamento de incidentes críticos"',
  "Lacuna", "Operação/Serviços",
  "Não há metodologia de apuração dos SLAs: marco inicial (geração do alerta, detecção ou abertura do chamado), o que caracteriza \"início do tratamento\", período de apuração, exclusões (manutenção programada, falhas do cliente ou do provedor de nuvem) e período de carência durante a transição.",
  s=4, p=3, imp="Apuração definida unilateralmente pelo cliente aumenta a exposição à multa por ocorrência.",
  rel=["d02_sla15", "d02_sla_disp", "d01_multa"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Qual a metodologia de apuração dos SLAs (marco inicial e final, ferramenta de medição, exclusões e período de carência após a transição)?",
  resp="Delivery/Operação")
I("d02_amb_sla_multa", D, "RFP 7.4 × Anexo I", "D01 p. 5 (impressa: 4) · § 2 e § 3 — item 3.1",
  'A: "qualquer nível de serviço (SLA) previsto no Anexo I" · B: "com revogação dos acessos de colaboradores desligados em até 24 (vinte e quatro) horas"',
  "Ambiguidade", "Jurídico/Contratual / Operação/Serviços",
  "Não está claro se \"qualquer nível de serviço previsto no Anexo I\" se limita à seção 2 (SLA) ou inclui prazos de outras seções, como a revogação em 24 horas (3.1), a recertificação trimestral (3.3) e a retenção de logs (1.3 e 1.6).",
  s=4, p=3, imp="Quanto mais prazos forem tratados como SLA, maior a base de incidência da multa de 10% por ocorrência.",
  rel=["d01_multa", "d02_revogacao"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Quais itens do Anexo I são considerados níveis de serviço para fins da multa do item 7.4: apenas os itens 2.1 a 2.3 ou também prazos das seções 1 e 3?",
  resp="Jurídico")
I("d02_ciclo_vida", D, "3. IAM — 3.1", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — item 3.1",
  '"Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"', "Requisito funcional / de serviço",
  "Segurança da Informação/Cyber",
  "Gestão do ciclo de vida das identidades. O IAM atual é Active Directory com scripts internos (D03), o que sugere automação a construir; depende de integração com o sistema de RH do cliente, não mencionada.",
  obr="Mandatório", s=3, p=3, imp="Esforço de integração com RH e sistemas-alvo não dimensionado.",
  fw=ISO, ctl="A.5.16 Gestão de identidade", rel=["d03_iam_atual", "d02_lac_ferr_iam"], acao="Precificar",
  resp="Segurança/Cyber")
I("d02_revogacao", D, "3. IAM — 3.1", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — item 3.1",
  '"com revogação dos acessos de colaboradores desligados em até 24 (vinte e quatro) horas"', "SLA / KPI",
  "Segurança da Informação/Cyber",
  "Revogação de acessos de desligados em até 24 horas. O marco inicial (data do desligamento ou comunicação pelo RH) não é definido e depende de informação do cliente.",
  obr="Mandatório", s=3, p=3, imp="Prazo depende de gatilho do cliente; atraso do RH pode ser imputado ao proponente.",
  fw=ISO, ctl="A.5.18 Direitos de acesso", rel=["d02_amb_sla_multa"], acao="Registrar premissa na proposta",
  perg="O prazo de 24 horas para revogação conta a partir da comunicação formal do desligamento pelo RH do Banco à Contratada?",
  resp="Segurança/Cyber")
I("d02_mfa", D, "3. IAM — 3.2", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — item 3.2",
  '"Autenticação multifator (MFA) obrigatória para 100% dos usuários com acesso privilegiado"', "Requisito não funcional",
  "Segurança da Informação/Cyber",
  "MFA para todos os usuários privilegiados. Não diz quem fornece a solução de MFA nem quantos usuários privilegiados existem.",
  obr="Mandatório", s=3, p=3, imp="Possível custo de licenças de MFA e integração com sistemas legados.",
  fw=ISO, ctl="A.8.5 Autenticação segura", rel=["d02_lac_dim_iam"], acao="Esclarecer no Q&A",
  perg="Ver pergunta do item {d02_lac_dim_iam}.", resp="Segurança/Cyber")
I("d02_recertificacao", D, "3. IAM — 3.3", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — item 3.3",
  '"Revisão (recertificação) trimestral dos acessos concedidos"', "Requisito funcional / de serviço",
  "Segurança da Informação/Cyber", "Recertificação trimestral de acessos; abrangência (quais sistemas) não definida.",
  obr="Mandatório", s=3, p=3, imp="Esforço recorrente proporcional ao número de sistemas e usuários.",
  fw=ISO, ctl="A.5.18 Direitos de acesso", rel=["d02_lac_dim_iam"], acao="Precificar", resp="Segurança/Cyber")
I("d02_pam", D, "3. IAM — 3.4", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — item 3.4",
  '"É desejável que a solução contemple cofre de senhas para contas privilegiadas (PAM)"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "PAM desejável. O cliente não tem PAM hoje (D03, slide 3). Não consta do questionário, logo não sofre o desconto oculto de 2 pontos.",
  obr="Desejável", s=2, p=3, imp="Custo opcional de ferramenta; pode pontuar em \"Ferramentas e tecnologia\".",
  fw=ISO, ctl="A.8.2 Direitos de acesso privilegiado", rel=["d03_oport_pam"], acao="Precificar",
  resp="Pré-venda/Arquitetura")
I("d02_lac_ferr_iam", D, "3. IAM", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM)",
  'Não localizado. Trechos que geram a necessidade: "O proponente deverá fornecer a solução de SIEM" · "Gestão do ciclo de vida das identidades"',
  "Lacuna", "Técnico/Arquitetura / Comercial/Preço",
  "Para o SOC, o Anexo I exige que o proponente forneça o SIEM; para o IAM, não diz se o proponente deve fornecer ferramenta de IGA/IAM ou apenas operar o Active Directory e scripts existentes (D03).",
  s=4, p=3, imp="Diferença de preço relevante entre operar o ambiente atual e fornecer e implantar uma plataforma de IGA.",
  rel=["d02_ciclo_vida", "d03_iam_atual", "d01_iam"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O serviço de IAM inclui o fornecimento de plataforma de governança de identidades (IGA) pelo proponente ou apenas a operação das ferramentas atuais do Banco (Active Directory e scripts)?",
  resp="Pré-venda/Arquitetura")
I("d02_lac_dim_iam", D, "3. IAM", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM)",
  'Não localizado. Trecho que gera a necessidade: "100% dos usuários com acesso privilegiado"', "Lacuna",
  "Operação/Serviços",
  "Faltam dados para dimensionar o IAM: número de usuários privilegiados, de sistemas e aplicações integrados, de admissões, movimentações e desligamentos por mês e de acessos a recertificar.",
  s=4, p=3, imp="Impede estimar o esforço de IAM; erro de dimensionamento afeta preço e SLA.",
  rel=["d02_mfa", "d02_recertificacao"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Informem o número de usuários privilegiados, de sistemas e aplicações a integrar ao IAM e a média mensal de admissões, movimentações e desligamentos.",
  resp="Pré-venda/Arquitetura")
I("d02_transicao", D, "4. Transição — 4.1", "§ 4. TRANSIÇÃO — item 4.1",
  '"A transição dos serviços deverá ser concluída em até 60 (sessenta) dias corridos a partir da assinatura do contrato"',
  "Prazo / marco", "Transição/Implantação", "Prazo de transição de 60 dias. Contradiz o RFP 3.2 (30 dias).",
  obr="Mandatório", s=4, p=3, imp="Ver contradição {d02_contr_transicao}.", rel=["d01_transicao", "d02_contr_transicao"],
  vig="Em esclarecimento", acao="Esclarecer no Q&A", perg="Ver pergunta do item {d02_contr_transicao}.",
  resp="Delivery/Operação")
I("d02_contr_transicao", D, "RFP 3.2 × Anexo I 4.1", "A: D01 p. 2 (impressa: 1) · B: § 4. TRANSIÇÃO — item 4.1",
  'A: "A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos" · B: "A transição dos serviços deverá ser concluída em até 60 (sessenta) dias corridos"',
  "Contradição", "Transição/Implantação",
  "Prazo de transição de 30 dias no RFP e de 60 dias no Anexo I, ambos contados da assinatura. Sem cláusula de precedência. O Q&A Rodada 1 não tratou o tema.",
  s=4, p=3, imp="Diferença de 30 dias de esforço de transição e de operação paralela; o plano de transição vale 10 pontos.",
  rel=["d01_transicao", "d02_transicao", "d01_precedencia", "d04_risco_transicao"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="O RFP (item 3.2) prevê transição em 30 dias e o Anexo I (item 4.1) em 60 dias, ambos a partir da assinatura. Qual prazo prevalece?",
  resp="Delivery/Operação")
I("d02_paralelo", D, "4. Transição — 4.2", "§ 4. TRANSIÇÃO — item 4.2",
  '"Durante a transição, o proponente deverá operar em paralelo com o fornecedor atual, sem custo adicional para o Contratante"',
  "Obrigação contratual", "Transição/Implantação / Comercial/Preço",
  "Operação paralela ao fornecedor atual sem custo adicional. Probabilidade 5: o custo da operação paralela decorre diretamente do texto. O contrato do SIEM legado termina em 31/01/2027 sem prorrogação (D03), o que limita a janela de paralelo.",
  obr="Mandatório", s=3, p=5, imp="Custo de 30 a 60 dias de equipe e plataforma sem receita, a diluir no preço.",
  rel=["d03_siem_legado", "d02_lac_transicao_rem"], acao="Precificar", resp="Pricing/Financeiro")
I("d02_lac_transicao_rem", D, "4. Transição × RFP 3.1", "§ 4. TRANSIÇÃO · D01 p. 2 (impressa: 1)",
  'Não localizado. Trechos que geram a necessidade: "a partir da assinatura do contrato" · "Início previsto dos serviços 01/02/2027"',
  "Lacuna", "Transição/Implantação / Comercial/Preço",
  "Não há data prevista de assinatura do contrato, nem regra de remuneração da transição (se é paga à parte, diluída nas mensalidades ou faturada só a partir de 01/02/2027).",
  s=4, p=3, imp="Sem a data de assinatura não é possível verificar se a transição cabe antes de 01/02/2027; sem regra de remuneração, o custo da transição fica sem cobertura.",
  rel=["d02_paralelo", "d01_inicio", "d04_risco_transicao"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Qual a data prevista de assinatura do contrato e como será remunerado o período de transição anterior a 01/02/2027?",
  resp="Pricing/Financeiro")
I("d02_coord_cissp", D, "5. Equipe — 5.1", "§ 5. EQUIPE — item 5.1",
  '"O serviço deverá contar com coordenador com certificação CISSP, dedicado exclusivamente ao contrato"', "Restrição",
  "Pessoas/Equipe", "Coordenador com CISSP em dedicação exclusiva; custo fixo de um profissional sênior.",
  obr="Mandatório", s=3, p=3, imp="Custo de um profissional sênior exclusivo durante 36 meses.",
  rel=["d01_equipe_cert"], acao="Precificar", resp="RH/Staffing")
I("d02_n1_presencial", D, "5. Equipe — 5.2", "§ 5. EQUIPE — item 5.2",
  '"Os analistas de nível 1 deverão atuar presencialmente na sede do Contratante, em São Paulo/SP, em horário comercial"',
  "Restrição", "Pessoas/Equipe",
  "Presença física de analistas N1 em São Paulo, em horário comercial (não diz como fica a cobertura N1 fora do horário comercial no regime 24x7). Alterado pelo Q&A nº 6, que admite atuação remota em território nacional.",
  obr="Mandatório", s=3, p=3, imp="Deixa de exigir alocação física em São Paulo, se a resposta do Q&A prevalecer.",
  rel=["d04_q6"], vig="Alterado", acao="Registrar premissa na proposta", resp="RH/Staffing")
I("d02_vpn", D, "6. Responsabilidades do Contratante — 6.1", "§ 6. RESPONSABILIDADES DO CONTRATANTE — item 6.1",
  '"Disponibilizar acesso remoto seguro (VPN) aos ambientes monitorados"', "Responsabilidade / dependência do cliente",
  "Infraestrutura/Cloud", "O Banco fornece VPN de acesso aos ambientes monitorados. Viabiliza o SOC e N1 remotos.",
  s=2, p=3, imp="Atraso na VPN atrasa a transição.", fw=ISO, ctl="A.6.7 Trabalho remoto", assoc="Correlata",
  acao="Registrar premissa na proposta", resp="Delivery/Operação")
I("d02_documentacao", D, "6. Responsabilidades do Contratante — 6.2", "§ 6. RESPONSABILIDADES DO CONTRATANTE — item 6.2",
  '"Disponibilizar a documentação técnica do ambiente em até 10 (dez) dias após a assinatura do contrato"',
  "Responsabilidade / dependência do cliente", "Transição/Implantação",
  "Documentação do ambiente só até o 10º dia após a assinatura. Com transição de 30 dias (RFP 3.2), restam 20 dias para integrar as fontes de log.",
  s=3, p=3, imp="Reduz o tempo útil de transição; atraso do cliente deve suspender o prazo de transição.",
  rel=["d01_transicao", "d04_risco_transicao"], acao="Registrar premissa na proposta", resp="Delivery/Operação")

# =============================================================== D03 — Apresentação (PPTX)
D = "D03"
I("d03_inv", D, "Apresentação inteira — slides 1 a 5", "slides 1–5 + notas do slide 5",
  '"Workshop com proponentes — RFP nº 2026-017 — 22/10/2026"', "Registro de cobertura", "Administrativo do processo",
  "Inventário: PowerPoint com 5 slides, nenhum oculto. O slide 5 tem notas do apresentador, lidas e analisadas (ampliação de escopo para subsidiárias). Leitura integral.")
I("d03_amb_vinculo", D, "Apresentação inteira", "slides 1–5",
  '"Expectativas para o novo serviço"', "Ambiguidade", "Administrativo do processo / Jurídico/Contratual",
  "O RFP não diz se o material do workshop integra o processo ou o contrato. A apresentação traz exigências ausentes do RFP e do Anexo I (migração de 24 meses de logs, visão unificada de riscos, meta de falsos positivos, inclusão de subsidiárias), e não se sabe se são obrigatórias, desejáveis ou só informativas.",
  s=4, p=3, imp="Escopo adicional sem base contratual pode ser exigido após a assinatura sem estar no preço.",
  rel=["d03_migracao", "d03_visao", "d03_meta_fp", "d03_subsidiarias", "d01_precedencia"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="O conteúdo apresentado no workshop de 22/10/2026 (incluindo migração de logs, meta de falsos positivos, visão unificada de riscos e inclusão das subsidiárias) integra o escopo contratual? Em caso positivo, será formalizado em adendo ao Anexo I?",
  resp="Bid Manager")
I("d03_usuarios", D, "Slide 2 — Números do ambiente", 'slide 2 — "Números do ambiente"', '"6.200 usuários ativos"',
  "Dado de dimensionamento", "Operação/Serviços",
  "6.200 usuários ativos, acima dos 4.500 colaboradores do RFP. A diferença pode vir de terceiros, contas de serviço ou contas não desativadas, o que não é explicado.",
  s=4, p=3, imp="Base de dimensionamento de IAM e licenças.", rel=["d03_contr_usuarios"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A", perg="Ver pergunta do item {d04_contr_usuarios}.", resp="Pricing/Financeiro")
I("d03_contr_usuarios", D, "RFP 2.1 × slide 2", 'A: D01 p. 2 (impressa: 1) · B: slide 2 — "Números do ambiente"',
  'A: "abrangendo aproximadamente 4.500 colaboradores" · B: "6.200 usuários ativos"', "Contradição", "Operação/Serviços",
  "O RFP indica cerca de 4.500 colaboradores; a apresentação, 6.200 usuários ativos (+38%). Podem medir universos diferentes (colaboradores × contas), mas o RFP não define a unidade de dimensionamento. Confrontar também com o Q&A nº 5 ({d04_contr_usuarios}).",
  s=4, p=3, imp="Diferença de 1.700 usuários na base de preço do IAM.",
  rel=["d01_usuarios", "d03_usuarios", "d04_contr_usuarios", "d01_precedencia"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A", perg="Ver pergunta do item {d04_contr_usuarios}.", resp="Pricing/Financeiro")
I("d03_servidores", D, "Slide 2 — Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"850 servidores (70% Windows, 30% Linux)"', "Dado de dimensionamento", "Infraestrutura/Cloud",
  "850 servidores (cerca de 595 Windows e 255 Linux). Única volumetria de fontes de log disponível, já que o EPS foi negado (Q&A nº 3).",
  s=2, p=3, imp="Insumo para estimar EPS e esforço de integração.", rel=["d04_q3"], acao="Registrar premissa na proposta",
  resp="Pré-venda/Arquitetura")
I("d03_dcs", D, "Slide 2 — Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"2 data centers próprios (São Paulo e Campinas)"', "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Dois data centers próprios, em São Paulo e Campinas. Coletores de log necessários em ambos.", s=2, p=3,
  imp="Infraestrutura de coleta em dois sites.", acao="Registrar premissa na proposta", resp="Pré-venda/Arquitetura")
I("d03_nuvens", D, "Slide 2 — Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"Workloads em 2 nuvens públicas"', "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Workloads em duas nuvens públicas não identificadas, sem volumetria. Integração de logs de nuvem não citada no Anexo I.",
  s=3, p=3, imp="Integrações de nuvem com esforço e licenças próprios.", rel=["d02_amb_ativos"], acao="Esclarecer no Q&A",
  perg="Quais são as duas nuvens públicas utilizadas, quantas contas ou assinaturas e quais serviços devem ser monitorados?",
  resp="Pré-venda/Arquitetura")
I("d03_siem_legado", D, "Slide 3 — Ferramentas atuais", 'slide 3 — "Ferramentas atuais"',
  '"SIEM legado — contrato encerra em 31/01/2027, sem possibilidade de prorrogação"', "Premissa do cliente",
  "Transição/Implantação",
  "Data rígida de fim do SIEM legado: 31/01/2027, sem prorrogação. Coincide com a véspera do início previsto (01/02/2027). A migração de logs históricos e a operação paralela precisam ocorrer antes dessa data.",
  s=4, p=3, imp="Qualquer atraso de assinatura ou de transição deixa o Banco sem SIEM; ver risco combinado {d04_risco_transicao}.",
  rel=["d01_inicio", "d02_paralelo", "d03_migracao", "d04_risco_transicao"], acao="Mitigar", resp="Delivery/Operação")
I("d03_iam_atual", D, "Slide 3 — Ferramentas atuais", 'slide 3 — "Ferramentas atuais"',
  '"IAM: Active Directory + scripts internos"', "Dado de dimensionamento", "Segurança da Informação/Cyber",
  "IAM atual baseado em Active Directory e scripts internos, sem ferramenta de governança de identidades. Automatizar ciclo de vida e recertificação (Anexo I, 3.1 e 3.3) exigirá ferramenta ou desenvolvimento.",
  s=3, p=3, imp="Esforço de implantação de IAM maior que o de simples operação.", rel=["d02_lac_ferr_iam"],
  acao="Registrar premissa na proposta", resp="Pré-venda/Arquitetura")
I("d03_oport_pam", D, "Slide 3 — Ferramentas atuais", 'slide 3 — "Ferramentas atuais"', '"Não há solução de PAM"',
  "Oportunidade / diferencial", "Segurança da Informação/Cyber",
  "O cliente não tem PAM, e o Anexo I (3.4) o considera desejável. Oferecer PAM pode pontuar em \"Ferramentas e tecnologia\" (15 pontos) e atender a MFA de privilegiados (3.2).",
  obr="Desejável", fw=ISO, ctl="A.8.2 Direitos de acesso privilegiado", rel=["d02_pam"], acao="Precificar",
  resp="Pré-venda/Arquitetura")
I("d03_alertas", D, "Slide 4 — Desafios", 'slide 4 — "Desafios"', '"Cerca de 1.200 alertas por dia"',
  "Dado de dimensionamento", "Operação/Serviços",
  "Cerca de 1.200 alertas por dia (~50 por hora). Único indicador de carga operacional fornecido.", s=3, p=3,
  imp="Base para dimensionar analistas N1 em 24x7.", rel=["d02_sla15"], acao="Registrar premissa na proposta",
  resp="Delivery/Operação")
I("d03_fp", D, "Slide 4 — Desafios", 'slide 4 — "Desafios"', '"70% de falsos positivos"', "Dado de dimensionamento",
  "Operação/Serviços", "70% dos alertas são falsos positivos (~840/dia), o que indica regras de correlação a reconstruir.",
  s=3, p=3, imp="Esforço inicial de tuning de casos de uso.", rel=["d03_meta_fp"], acao="Registrar premissa na proposta",
  resp="Delivery/Operação")
I("d03_meta_fp", D, "Slide 4 — Desafios", 'slide 4 — "Desafios"',
  '"Meta: reduzir os falsos positivos para 10% no primeiro trimestre de operação"', "SLA / KPI", "Operação/Serviços",
  "Meta de reduzir falsos positivos de 70% para 10% em três meses, ausente do Anexo I. Se for contratual, fica sujeita à multa do 7.4. A medição depende de definição de falso positivo e de linha de base.",
  obr="Informativo", s=4, p=3, imp="Meta agressiva; se exigível, gera multas ou necessidade de esforço intenso de tuning no primeiro trimestre.",
  fw=ITIL, ctl="Prática de melhoria contínua", assoc="Correlata", rel=["d03_amb_vinculo", "d01_multa"],
  vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A meta de 10% de falsos positivos no primeiro trimestre é um SLA contratual sujeito a multa? Como será medida e qual a linha de base?",
  resp="Delivery/Operação")
I("d03_migracao", D, "Slide 5 — Expectativas para o novo serviço", 'slide 5 — "Expectativas para o novo serviço"',
  '"Migração de 24 meses de logs históricos do SIEM legado para a nova plataforma"', "Requisito funcional / de serviço",
  "Transição/Implantação / Dados/Analytics",
  "Migração de 24 meses de logs históricos, ausente do Anexo I. Volume desconhecido (EPS negado) e prazo limitado ao fim do contrato do SIEM legado (31/01/2027). Formato de exportação do legado não informado.",
  obr="Desejável", s=4, p=3, imp="Esforço e armazenamento potencialmente grandes, fora do escopo escrito.",
  rel=["d03_amb_vinculo", "d03_siem_legado", "d02_amb_retencao"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A migração de 24 meses de logs históricos é obrigatória? Qual o volume (TB), o formato de exportação do SIEM legado e quem extrai os dados antes de 31/01/2027?",
  resp="Pré-venda/Arquitetura")
I("d03_visao", D, "Slide 5 — Expectativas para o novo serviço", 'slide 5 — "Expectativas para o novo serviço"',
  '"Visão unificada de riscos para a diretoria"', "Entregável", "Operação/Serviços",
  "Painel ou relatório de riscos para a diretoria, sem especificação de conteúdo, periodicidade ou ferramenta.",
  obr="Desejável", s=2, p=3, imp="Entregável executivo com esforço indefinido.", rel=["d03_amb_vinculo"],
  acao="Esclarecer no Q&A", perg="O que deve conter a \"visão unificada de riscos para a diretoria\", com que periodicidade e em qual ferramenta?",
  resp="Delivery/Operação")
I("d03_subsidiarias", D, "Slide 5 — notas do apresentador", "slide 5 — notas do apresentador",
  '"as subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários adicionais) também deverão ser incluídas no escopo"',
  "Requisito funcional / de serviço", "Operação/Serviços",
  "Ampliação de escopo só nas notas do apresentador (não exibidas no slide): duas subsidiárias com cerca de 900 usuários adicionais. Não consta do RFP, do Anexo I nem do Q&A. Não informa ativos, data centers ou fontes de log das subsidiárias.",
  obr="Mandatório", s=4, p=3, imp="Aumento de ~20% na base de usuários e escopo de SOC não dimensionado; sem base contratual se não formalizado.",
  rel=["d03_amb_vinculo", "d04_contr_usuarios", "d02_amb_ativos"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="As subsidiárias Horizonte Seguros e Horizonte Investimentos fazem parte do escopo de SOC e IAM? Em caso positivo, informem usuários, ativos e ambientes de cada uma e se a contratação será feita por cada entidade.",
  resp="Bid Manager")

# =============================================================== D04 — Q&A e questionário (XLSX)
D = "D04"
I("d04_inv", D, "Planilha inteira — 4 abas", 'abas "Instruções", "Q&A Rodada 1", "Questionário Técnico", "Pesos" (OCULTA)',
  '"Questionário Técnico e Respostas aos Esclarecimentos — RFP nº 2026-017"', "Registro de cobertura",
  "Administrativo do processo",
  "Inventário: Excel com 4 abas; a aba \"Pesos\" está oculta e foi analisada (pesos do questionário e regra de desconto na Nota Técnica). Sem linhas ou colunas ocultas e sem comentários de célula. Q&A Rodada 1 com 6 perguntas datadas de 12/11/2026. Leitura integral.")
I("d04_instr_desclass", D, "Aba Instruções", 'aba "Instruções" · A3',
  '"O preenchimento de todas as abas deste arquivo é obrigatório. Questionários incompletos serão desclassificados."',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Questionário incompleto leva à desclassificação, sanção que não consta do RFP 4.4. Probabilidade 5: a desclassificação decorre diretamente do texto.",
  obr="Mandatório", s=5, p=5, imp="Desclassificação.", rel=["d01_questionario", "d04_amb_abas"], acao="Atender",
  resp="Pré-venda/Arquitetura")
I("d04_amb_abas", D, "Aba Instruções", 'aba "Instruções" · A3', '"O preenchimento de todas as abas deste arquivo é obrigatório"',
  "Ambiguidade", "Administrativo do processo",
  "\"Todas as abas\" incluiria, literalmente, as abas \"Q&A Rodada 1\" (respostas do Banco) e \"Pesos\" (oculta), que não têm campos para o proponente. Também não está claro se a coluna \"Comentários\" é obrigatória nem se \"Parcial\" conta como preenchido.",
  s=5, p=3, imp="Interpretação literal pode levar à desclassificação por \"questionário incompleto\".",
  rel=["d04_instr_desclass"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Confirmam que o preenchimento obrigatório se refere apenas à coluna D (\"Resposta do proponente\") da aba \"Questionário Técnico\", e que a coluna \"Comentários\" é opcional?",
  resp="Bid Manager")
I("d04_q1", D, "Q&A Rodada 1 — pergunta nº 1 (RFP, item 3.1)", 'aba "Q&A Rodada 1" · E2 (pergunta nº 1, 12/11/2026)',
  '"A data de entrega das propostas fica prorrogada para 27/11/2026, até as 18h."', "Prazo / marco",
  "Administrativo do processo",
  "Nova data de entrega: 27/11/2026, 18h (antes 20/11). O início dos serviços (01/02/2027) não foi alterado, o que comprime o período de avaliação, assinatura e transição.",
  obr="Mandatório", s=5, p=3, imp="Proposta fora do prazo não é considerada; janela de transição mais curta.",
  rel=["d01_entrega", "d04_risco_transicao"], acao="Atender", resp="Bid Manager")
I("d04_q2", D, "Q&A Rodada 1 — pergunta nº 2 (RFP, item 5.1 c)", 'aba "Q&A Rodada 1" · E3 (pergunta nº 2, 12/11/2026)',
  '"Não. O SOC deverá estar localizado em território nacional."', "Critério eliminatório / de habilitação",
  "Operação/Serviços / Regulatório/Compliance",
  "Confirma a exigência de SOC no Brasil (RFP 5.1 c), sem alterá-la. Probabilidade 5: inabilitação direta prevista no RFP 5.1.",
  obr="Mandatório", s=5, p=5, imp="Inabilitação se o SOC estiver fora do país.", rel=["d01_hab_soc_br"], vig="Duplicado",
  acao="Atender", resp="Delivery/Operação")
I("d04_q3", D, "Q&A Rodada 1 — pergunta nº 3 (Anexo I, item 1.4)", 'aba "Q&A Rodada 1" · E4 (pergunta nº 3, 12/11/2026)',
  '"A volumetria será informada somente ao proponente vencedor."', "Lacuna", "Técnico/Arquitetura / Comercial/Preço",
  "A volumetria de eventos por segundo (EPS), principal variável de custo do SIEM (licença, armazenamento, retenção de 12 meses e 5 anos), foi formalmente recusada antes da proposta. Probabilidade 5: informação indispensável ao preço recusada formalmente pelo cliente.",
  s=4, p=5, imp="Preço do SIEM baseado em estimativa; sem premissa e mecanismo de ajuste, o desvio fica com o proponente.",
  rel=["d02_monit_ativos", "d02_siem", "d03_servidores", "d04_risco_exposicao"], vig="Vigente",
  acao="Registrar premissa na proposta",
  perg="Na ausência da volumetria, o Banco aceita que a proposta adote EPS de referência como premissa, com reequilíbrio de preço caso a volumetria real seja superior?",
  resp="Pricing/Financeiro")
I("d04_q4", D, "Q&A Rodada 1 — pergunta nº 4 (RFP, item 7.4)", 'aba "Q&A Rodada 1" · E5 (pergunta nº 4, 12/11/2026)',
  '"As condições do item 7 permanecem inalteradas."', "Penalidade / multa / glosa", "Jurídico/Contratual / Financeiro",
  "Pergunta sobre teto de multas respondida sem conceder limite: confirma multa de 10% por ocorrência sem teto e mantém todo o item 7 (inclusive responsabilidade ilimitada). Probabilidade 4: recusa explícita do cliente em limitar a multa, aplicada automaticamente a cada ocorrência.",
  obr="Mandatório", s=5, p=4, imp="Elimina a via do Q&A para limitar a exposição; resta ressalva na proposta ou No-Go.",
  fw=CC, ctl="Cláusula penal (identificador a confirmar)", assoc="Correlata",
  rel=["d01_multa", "d01_resp_ilimitada", "d04_risco_exposicao"], vig="Duplicado", acao="Avaliar Go/No-Go",
  resp="Jurídico")
I("d04_q5", D, "Q&A Rodada 1 — pergunta nº 5 (RFP, item 2.1)", 'aba "Q&A Rodada 1" · E6 (pergunta nº 5, 12/11/2026)',
  '"Considerar 5.000 usuários."', "Dado de dimensionamento", "Operação/Serviços",
  "Q&A fixa 5.000 usuários para dimensionamento, diferente dos 4.500 do RFP e dos 6.200 + ~900 da apresentação.",
  s=4, p=3, imp="Base de preço; ver contradição {d04_contr_usuarios}.", rel=["d01_usuarios", "d04_contr_usuarios"],
  vig="Em esclarecimento", acao="Registrar premissa na proposta", perg="Ver pergunta do item {d04_contr_usuarios}.",
  resp="Pricing/Financeiro")
I("d04_contr_usuarios", D, "Q&A nº 5 × apresentação (slide 2 e notas do slide 5)",
  'A: aba "Q&A Rodada 1" · E6 (pergunta nº 5) · B: D03 slide 2 — "Números do ambiente" e slide 5 — notas do apresentador',
  'A: "Considerar 5.000 usuários." · B: "6.200 usuários ativos" [...] "cerca de 900 usuários adicionais"',
  "Contradição", "Operação/Serviços",
  "O Q&A manda considerar 5.000 usuários; o workshop indica 6.200 usuários ativos mais ~900 das subsidiárias (~7.100). O RFP falava em 4.500. A resposta não esclarece se as subsidiárias estão incluídas nem se 5.000 é teto ou estimativa.",
  s=4, p=3, imp="Diferença de até 2.100 usuários (~42%) entre a base de preço e o ambiente informado; risco de prestar serviço a mais usuários do que os precificados.",
  rel=["d01_usuarios", "d03_contr_usuarios", "d04_q5", "d03_subsidiarias", "d01_precedencia"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="O Q&A nº 5 indica 5.000 usuários, e o workshop indicou 6.200 usuários ativos mais cerca de 900 das subsidiárias. Qual quantidade deve ser usada, as subsidiárias estão incluídas e haverá ajuste de preço se a quantidade real for superior?",
  resp="Pricing/Financeiro")
I("d04_q6", D, "Q&A Rodada 1 — pergunta nº 6 (Anexo I, item 5.2)", 'aba "Q&A Rodada 1" · E7 (pergunta nº 6, 12/11/2026)',
  '"Sim, desde que em território nacional."', "Restrição", "Pessoas/Equipe",
  "Permite atuação remota dos analistas N1, desde que no Brasil, alterando o Anexo I 5.2 (presencial em São Paulo).",
  obr="Mandatório", s=2, p=3, imp="Reduz custo de alocação física; mantém equipe no Brasil.", rel=["d02_n1_presencial"],
  acao="Registrar premissa na proposta", resp="RH/Staffing")
I("d04_qt01", D, "Questionário Técnico — QT-01", 'aba "Questionário Técnico" · B2 (QT-01, Obrigatório: Sim; peso 3 na aba "Pesos")',
  '"Possui certificação ISO/IEC 27001 com escopo que inclua os serviços de SOC?"', "Critério eliminatório / de habilitação",
  "Segurança da Informação/Cyber",
  "Repete o critério de habilitação do RFP 5.1 a). Peso 3 na aba oculta. Probabilidade 5: inabilitação direta prevista no RFP 5.1.",
  obr="Mandatório", s=5, p=5, imp="Inabilitação.", fw=ISO, ctl="Certificação do SGSI (requisitos das cláusulas 4 a 10)",
  rel=["d01_hab_iso", "d04_pesos"], vig="Duplicado", acao="Atender", resp="Compliance")
I("d04_qt02", D, "Questionário Técnico — QT-02", 'aba "Questionário Técnico" · B3 (QT-02, Obrigatório: Não; peso 1)',
  '"Oferece integração nativa com plataforma SOAR?"', "Requisito funcional / de serviço", "Técnico/Arquitetura",
  "Requisito não obrigatório que não consta do Anexo I. Pela regra oculta, responder \"Não atende\" retira 2 pontos da Nota Técnica.",
  obr="Desejável", s=3, p=3, imp="Perda de 2 pontos na Nota Técnica se não oferecido.", fw=CSF, ctl="Função Respond (RS)",
  assoc="Correlata", rel=["d04_regra_oculta", "d04_oport_soar_ti"], acao="Precificar", resp="Pré-venda/Arquitetura")
I("d04_qt03", D, "Questionário Técnico — QT-03", 'aba "Questionário Técnico" · B4 (QT-03, Obrigatório: Sim; peso 2)',
  '"Retém os logs online por no mínimo 12 meses?"', "Requisito não funcional", "Segurança da Informação/Cyber",
  "Especifica que os 12 meses do Anexo I 1.3 são de retenção \"online\", o que é mais exigente (e mais caro) que retenção em arquivo.",
  obr="Mandatório", s=3, p=3, imp="Armazenamento online (hot) por 12 meses, sem EPS conhecido.", fw=ISO,
  ctl="A.8.15 Registro de logs", rel=["d02_retencao12", "d02_amb_retencao"], acao="Precificar", resp="Pré-venda/Arquitetura")
I("d04_qt04", D, "Questionário Técnico — QT-04", 'aba "Questionário Técnico" · B5 (QT-04, Obrigatório: Sim; peso 3)',
  '"Atende aos requisitos da Resolução CMN nº 4.893/2021?"', "Requisito não funcional", "Regulatório/Compliance",
  "Requisito obrigatório e de maior peso: atender à Resolução CMN nº 4.893/2021. A resolução se dirige às instituições financeiras; não se sabe quais requisitos o Banco espera do prestador nem como comprová-los.",
  obr="Mandatório", s=4, p=3, imp="Resposta \"Atende\" genérica pode gerar obrigações regulatórias abertas no contrato.",
  fw=CMN, ctl="Requisitos para prestadores de serviços de processamento, armazenamento e nuvem (identificador a confirmar)",
  rel=["d01_req_cmn"], acao="Esclarecer no Q&A", perg="Ver pergunta do item {d01_req_cmn}.", resp="Compliance")
I("d04_qt05", D, "Questionário Técnico — QT-05", 'aba "Questionário Técnico" · B6 (QT-05, Obrigatório: Não; peso 2)',
  '"Oferece serviço de threat intelligence?"', "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Serviço de threat intelligence não obrigatório e ausente do Anexo I. \"Não atende\" retira 2 pontos (regra oculta). Feeds de inteligência processados fora do Brasil podem conflitar com o Anexo III.",
  obr="Desejável", s=3, p=3, imp="Perda de 2 pontos na Nota Técnica se não oferecido; custo de feeds se oferecido.",
  fw=ISO, ctl="A.5.7 Inteligência de ameaças", rel=["d04_regra_oculta", "d04_oport_soar_ti", "d01_anexo3_dados"],
  acao="Precificar", resp="Segurança/Cyber")
I("d04_qt06", D, "Questionário Técnico — QT-06", 'aba "Questionário Técnico" · B7 (QT-06, Obrigatório: Sim; peso 2)',
  '"Possui equipe com certificações reconhecidas pelo mercado?"', "Requisito não funcional", "Pessoas/Equipe",
  "Requisito obrigatório subjetivo: não define quais certificações são \"reconhecidas\". Relaciona-se ao RFP 5.2 e ao CISSP do coordenador.",
  obr="Mandatório", s=3, p=3, imp="Risco de avaliação subjetiva da resposta.", rel=["d01_amb_equipe_cert"],
  acao="Esclarecer no Q&A", perg="Ver pergunta do item {d01_amb_equipe_cert}.", resp="RH/Staffing")
I("d04_lac_obrigatorios", D, "Questionário Técnico — coluna \"Obrigatório\"", 'aba "Questionário Técnico" · C1 e D1',
  'Não localizado. Trecho que gera a necessidade: "Resposta do proponente (Atende / Não atende / Parcial)"', "Lacuna",
  "Administrativo do processo",
  "Os documentos não dizem a consequência de responder \"Não atende\" ou \"Parcial\" a requisito obrigatório (inabilitação, desclassificação, perda de pontos), nem o efeito de \"Parcial\" em requisito não obrigatório. A regra oculta trata só de \"Não atende\" em não obrigatórios.",
  s=4, p=3, imp="Uma resposta \"Parcial\" honesta pode levar à desclassificação sem regra conhecida.",
  rel=["d04_regra_oculta", "d04_pesos"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Qual a consequência de responder \"Não atende\" ou \"Parcial\" a um requisito marcado como obrigatório e de responder \"Parcial\" a um requisito não obrigatório?",
  resp="Bid Manager")
I("d04_pesos", D, "Aba Pesos (OCULTA)", 'aba "Pesos" (OCULTA) · A1:B7',
  '"Peso" · QT-01 = 3 · QT-02 = 1 · QT-03 = 2 · QT-04 = 3 · QT-05 = 2 · QT-06 = 2', "Critério de avaliação / pontuação",
  "Administrativo do processo",
  "Pesos do questionário em aba oculta (soma 13). Nem o RFP nem a planilha visível explicam como esses pesos entram na Nota Técnica. Maiores pesos: ISO 27001 (QT-01) e Resolução CMN nº 4.893/2021 (QT-04).",
  s=3, p=3, imp="Critério de pontuação não divulgado; prioriza as respostas de QT-01 e QT-04.",
  rel=["d04_contr_pontuacao", "d04_regra_oculta"], vig="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Ver pergunta do item {d04_contr_pontuacao}.", resp="Bid Manager")
I("d04_regra_oculta", D, "Aba Pesos (OCULTA)", 'aba "Pesos" (OCULTA) · A9',
  '"Requisitos não obrigatórios respondidos como \'Não atende\' reduzem a Nota Técnica em 2 (dois) pontos cada."',
  "Critério de avaliação / pontuação", "Administrativo do processo",
  "Regra de pontuação oculta: cada \"Não atende\" em requisito não obrigatório (QT-02 SOAR, QT-05 threat intelligence) desconta 2 pontos da Nota Técnica. Até 4 pontos a menos podem levar a nota abaixo do corte de 70% (6.3). Requisito \"não obrigatório\" passa a ter efeito de quase obrigatório.",
  obr="Mandatório", s=4, p=3, imp="Perda de até 4 pontos na Nota Técnica e risco de desclassificação pela nota de corte.",
  rel=["d04_qt02", "d04_qt05", "d01_nota_corte", "d04_contr_pontuacao"], acao="Precificar", resp="Pré-venda/Arquitetura")
I("d04_contr_pontuacao", D, "RFP 6.2 × aba Pesos (OCULTA)", 'A: D01 p. 4 (impressa: 3) · B: aba "Pesos" (OCULTA) · A9',
  'A: "A Nota Técnica, de no máximo 60 (sessenta) pontos, será atribuída conforme os critérios abaixo" · B: "Requisitos não obrigatórios respondidos como \'Não atende\' reduzem a Nota Técnica em 2 (dois) pontos cada."',
  "Contradição", "Administrativo do processo",
  "O RFP diz que a Nota Técnica é atribuída conforme os quatro critérios do 6.2, sem mencionar o questionário; a aba oculta cria descontos e pesos adicionais. Não se sabe se os pesos (QT-01 a QT-06) somam pontos, em qual critério do 6.2 entram, nem se o desconto incide antes ou depois da nota de corte.",
  s=4, p=3, imp="Critério de julgamento não publicado no RFP afeta a nota e a nota de corte; base para impugnação ou pedido de esclarecimento.",
  rel=["d01_nota_tecnica", "d04_pesos", "d04_regra_oculta", "d01_contr_pontos"], vig="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="A planilha do questionário traz em aba oculta pesos por requisito e desconto de 2 pontos na Nota Técnica para requisitos não obrigatórios respondidos como \"Não atende\". Essas regras valem? Como os pesos se integram aos critérios do item 6.2 do RFP?",
  resp="Bid Manager")
I("d04_oport_soar_ti", D, "Questionário Técnico — QT-02 e QT-05", 'aba "Questionário Técnico" · B3 e B6',
  '"Oferece integração nativa com plataforma SOAR?" · "Oferece serviço de threat intelligence?"',
  "Oportunidade / diferencial", "Segurança da Informação/Cyber",
  "SOAR e threat intelligence não estão no Anexo I, mas são pontuados (e penalizados se ausentes, pela regra oculta). Oferecê-los evita desconto de 4 pontos, pode pontuar em \"Ferramentas e tecnologia\" e ajuda a cumprir a meta de redução de falsos positivos (D03).",
  obr="Desejável", fw=CSF, ctl="Função Respond (RS)", assoc="Correlata", rel=["d04_qt02", "d04_qt05", "d03_meta_fp"],
  acao="Precificar", resp="Pré-venda/Arquitetura")
I("d04_risco_transicao", D, "Risco combinado — transição", 'D01 p. 2 (impressa: 1) · D02 § 4 · D03 slides 3 e 5 · aba "Q&A Rodada 1" · E2',
  'A: "Início previsto dos serviços 01/02/2027" · B: "contrato encerra em 31/01/2027, sem possibilidade de prorrogação" · C: "A data de entrega das propostas fica prorrogada para 27/11/2026"',
  "Risco para o proponente", "Transição/Implantação",
  "Combinação: entrega de propostas adiada para 27/11/2026 sem mudança do início (01/02/2027); SIEM legado termina em 31/01/2027 sem prorrogação; data de assinatura indefinida; prazo de transição divergente (30 × 60 dias); documentação do ambiente só até 10 dias após a assinatura; operação paralela sem custo; migração de 24 meses de logs a extrair do legado; EPS desconhecido até a contratação. Probabilidade 4: o prazo final do legado é rígido e declarado pelo cliente, e a janela entre entrega (27/11/2026) e início (01/02/2027) é de pouco mais de 2 meses para avaliação, negociação, assinatura e transição. Se a transição não terminar a tempo, o Banco fica sem SIEM e o proponente fica exposto a SLAs com multa sem teto desde o primeiro dia.",
  nat="Inferida", s=5, p=4, imp="Atraso na transição gera multas por ocorrência sem teto, possível responsabilidade por incidentes no período e dano reputacional.",
  rel=["d01_inicio", "d03_siem_legado", "d04_q1", "d02_contr_transicao", "d02_documentacao", "d02_paralelo",
       "d03_migracao", "d04_q3", "d02_lac_transicao_rem"],
  acao="Mitigar",
  perg="Haverá período de carência para aplicação de multas de SLA após o início dos serviços e suspensão do prazo de transição em caso de atraso de responsabilidades do Banco?",
  resp="Delivery/Operação")
I("d04_risco_exposicao", D, "Risco combinado — exposição financeira", "D01 p. 5 (impressa: 4) · D02 § 2 · D03 slide 4 · aba \"Q&A Rodada 1\" · E4 e E5",
  'A: "multa de 10% (dez por cento) do valor mensal do contrato, por ocorrência" · B: "responderá de forma integral e ilimitada" · C: "As condições do item 7 permanecem inalteradas." · D: "A volumetria será informada somente ao proponente vencedor."',
  "Risco para o proponente", "Jurídico/Contratual / Financeiro",
  "Combinação: multa de 10% por ocorrência sem teto (7.4), aplicável a qualquer SLA; recusa do cliente em limitá-la (Q&A nº 4); responsabilidade integral e ilimitada por incidentes (7.5); seguro com valor indefinido (7.6); SLA de 15 minutos com matriz de criticidade não fornecida; 1.200 alertas por dia com 70% de falsos positivos; EPS recusado (Q&A nº 3). Probabilidade 4: a multa é automática por ocorrência e o cliente já recusou formalmente limitar as condições do item 7. A exposição total não tem limite e não é precificável nem segurável com os dados fornecidos.",
  nat="Inferida", s=5, p=4, imp="Exposição financeira e jurídica ilimitada; candidato a ressalva formal ou decisão de No-Go.",
  rel=["d01_multa", "d04_q4", "d01_resp_ilimitada", "d01_seguro", "d02_sla15", "d02_lac_matriz", "d03_alertas", "d04_q3"],
  acao="Avaliar Go/No-Go",
  perg="O Banco aceitaria ressalvas na proposta limitando multas e responsabilidade (teto anual e exclusão de danos indiretos), ou propostas com ressalvas serão desclassificadas?",
  resp="Jurídico")


DOCS = [
    {"codigo": "D01", "arquivo": "RFP-2026-017_Servicos_SOC_IAM.pdf", "tipo": "RFP", "versao": "v1.0 — 15/10/2026"},
    {"codigo": "D02", "arquivo": "Anexo_I_Especificacao_Tecnica.docx", "tipo": "Anexo técnico", "versao": "v1.0 — 15/10/2026"},
    {"codigo": "D03", "arquivo": "Apresentacao_Ambiente_Atual.pptx", "tipo": "Apresentação", "versao": "22/10/2026"},
    {"codigo": "D04", "arquivo": "QA_Rodada1_e_Questionario.xlsx", "tipo": "Q&A e questionário", "versao": "12/11/2026"},
]
PROXIMO = {"D01": "Anexo_I_Especificacao_Tecnica.docx (D02), a partir do § 1. SERVIÇOS DE SOC",
           "D02": "Apresentacao_Ambiente_Atual.pptx (D03), a partir do slide 1",
           "D03": "QA_Rodada1_e_Questionario.xlsx (D04), a partir da aba \"Instruções\""}

if __name__ == "__main__":
    out = sys.argv[1]
    upto = sys.argv[2] if len(sys.argv) > 2 else "D04"
    n = int(upto[1:])
    docs = []
    for d in DOCS:
        d = dict(d)
        d["situacao"] = "processado" if int(d["codigo"][1:]) <= n else "pendente"
        docs.append(d)
    keep = [i for i in ITENS if int(i["doc"][1:]) <= n]
    keys = {i["chave"] for i in keep}
    # em execuções parciais, referências a itens futuros ficam como texto
    if n < 4:
        import re
        for i in keep:
            i["relacionados"] = [r for r in i["relacionados"] if r in keys]
            for f in ("descricao", "pergunta", "impacto"):
                i[f] = re.sub(r"\{([a-z0-9_]+)\}", lambda m: m.group(0) if m.group(1) in keys else "(item de documento posterior)", i[f])
    status = {"final": True} if n == 4 else {"final": False, "proximo": PROXIMO[upto], "parte": n, "concluidos": n}
    data = {"processo": "RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Serviços gerenciados de SOC e IAM",
            "documentos": docs, "itens": keep, "status": status}
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f"{len(keep)} itens até {upto}")
