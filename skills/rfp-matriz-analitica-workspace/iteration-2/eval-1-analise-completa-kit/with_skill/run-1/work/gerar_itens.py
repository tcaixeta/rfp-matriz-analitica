#!/usr/bin/env python3
"""Gera itens.json para build_matrix.py. Uso: gerar_itens.py <saida.json> <n_docs (1-4)>"""
import json
import sys

ISO = "ISO/IEC 27001:2022 (Anexo A)"
ISO_SGSI = "ISO/IEC 27001:2022"
CSF = "NIST CSF 2.0"
ITIL = "ITIL 4"
LGPD = "LGPD (Lei 13.709/2018)"
RES = "Resolução CMN nº 4.893/2021 (citada pelo cliente)"
CC = "Código Civil (Lei 10.406/2002)"
I20000 = "ISO/IEC 20000-1"
NA = dict(framework="—", controle="—", associacao="Não aplicável")

itens = []


def I(chave, doc, secao, loc, evid, tipo, dominio, desc, **kw):
    d = dict(chave=chave, doc=doc, secao=secao, localizador=loc, evidencia=evid, tipo=tipo,
             dominio=dominio, descricao=desc)
    d.update(kw)
    itens.append(d)


P2 = "p. 2 (impressa: 1)"
P3 = "p. 3 (impressa: 2)"
P4 = "p. 4 (impressa: 3)"
P5 = "p. 5 (impressa: 4)"
P6 = "p. 6 (impressa: 5) (OCR)"

# =============================================================== D01 — RFP
I("d01_inv", "D01", "Documento inteiro (capa e seções 1 a 7 + Anexo III)", "p. 1–6",
  '"Solicitação de Proposta (RFP) nº 2026-017"', "Registro de cobertura", "Administrativo do processo",
  "Inventário D01: PDF com 6 páginas físicas; a numeração impressa começa na p. 2 ('Página 1'). Páginas 1 a 5 com texto extraível (seções 1 a 7). "
  "A p. 6 (impressa: 5) não tem camada de texto (imagem escaneada): foi lida visualmente e analisada com localizador '(OCR)'; contém o Anexo III — Declaração de Localização de Dados. "
  "Cabeçalho/rodapé repetido ignorado. Texto institucional do item 1.1 não gera item.",
  responsavel="Bid Manager")
I("d01_regime", "D01", "1. APRESENTAÇÃO — 1.2 · 4. INSTRUÇÕES — 4.1 · 7. CONDIÇÕES — 7.1", f"{P2} · {P3} · {P5}",
  '"O Banco é instituição financeira autorizada a funcionar pelo Banco Central do Brasil" · "enviada exclusivamente pelo portal de fornecedores do Banco" · "mediante acordo entre as partes"',
  "Registro de cobertura", "Regulatório/Compliance",
  "Regime identificado: contratação PRIVADA (sociedade anônima; envio pelo portal de fornecedores do Banco; prorrogação por acordo entre as partes; nenhuma menção a licitação, pregão ou Lei 14.133/2021) "
  "em SETOR REGULADO (instituição financeira autorizada pelo BCB e sujeita à Resolução CMN nº 4.893/2021). Referências jurídicas usadas na matriz: Código Civil (contratual), LGPD (dados pessoais) e a Res. CMN 4.893/2021 citada pelo cliente. Lei 14.133/2021 não se aplica.",
  responsavel="Jurídico")
I("d01_precedencia", "D01", "Documento inteiro — cláusula de ordem de precedência", "p. 1–6 (não localizada)",
  'Não localizado · trecho que gera a necessidade: "As especificações técnicas detalhadas constam do Anexo I — Especificação Técnica."',
  "Lacuna", "Jurídico/Contratual",
  "Não há cláusula de ordem de precedência entre RFP, Anexo I, material do workshop e respostas do Q&A, embora existam divergências concretas entre eles: prazo de transição (30 × 60 dias), número de usuários (4.500 × 5.000 × 6.200), local dos analistas N1 e região do SIEM × declaração de localização de dados. "
  "Não se presume que o Q&A, por ser mais recente, prevaleça.",
  obrigatoriedade="Informativo", s=4, p=3,
  impacto="Sem precedência, o proponente não sabe qual versão de prazo, escopo e dimensionamento será exigida no contrato; risco de precificar sobre base que o cliente não reconhece",
  **NA, relacionados=["d01_transicao", "d02_transicao", "d02_contr_regiao", "d04_q5", "d04_q6"],
  vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Qual a ordem de precedência entre a RFP, o Anexo I, o material do workshop de 22/10/2026 e as respostas do Q&A? As respostas do Q&A alteram formalmente a RFP e os anexos e integrarão o contrato?",
  responsavel="Jurídico")
I("d01_res4893", "D01", "1. APRESENTAÇÃO — 1.2", P2,
  '"está sujeito à Resolução CMN nº 4.893/2021, que dispõe sobre a política de segurança cibernética e sobre os requisitos para a contratação de serviços de processamento e armazenamento de dados e de computação em nuvem"',
  "Requisito implícito", "Regulatório/Compliance",
  "Inferido: o objeto inclui SIEM fornecido pelo proponente, possivelmente em nuvem (Anexo I, 1.2), e guarda de logs; o contrato tende a enquadrar-se como contratação de processamento/armazenamento de dados regida pela resolução. "
  "O proponente terá de aceitar as condições contratuais que a norma impõe ao Banco e comprovar aderência (o Questionário QT-04 pergunta isso explicitamente, com peso 3). O RFP não lista quais requisitos da norma serão exigidos do fornecedor.",
  obrigatoriedade="Mandatório", natureza="Inferida", s=4, p=3,
  impacto="Cláusulas regulatórias adicionais (acesso do regulador, continuidade, localização de dados, notificação de incidentes) com custo e risco não descritos no RFP",
  framework=RES, controle="Requisitos para contratação de processamento, armazenamento de dados e computação em nuvem (identificador a confirmar)",
  associacao="Direta", relacionados=["d02_contr_regiao", "d04_qt04"], acao="Esclarecer no Q&A",
  pergunta="Quais requisitos da Resolução CMN nº 4.893/2021 o Banco exigirá contratualmente do fornecedor (por exemplo, acesso do regulador, continuidade, notificação de incidentes, localização de dados) e em que documento serão formalizados?",
  responsavel="Compliance")
I("d01_soc", "D01", "2. OBJETO — 2.1", P2,
  '"prestação de serviços gerenciados de Centro de Operações de Segurança (SOC), em regime 24x7x365"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber / Operação/Serviços",
  "Escopo principal: SOC gerenciado em regime 24x7x365, detalhado no Anexo I, seção 1.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Equipe em turnos 24x7 e plataforma: principal base de custo",
  framework=ISO, controle="A.8.16 Atividades de monitoramento", associacao="Direta",
  relacionados=["d02_monit"], acao="Precificar", responsavel="Delivery/Operação")
I("d01_iam", "D01", "2. OBJETO — 2.1", P2, '"de gestão de identidades e acessos (IAM)"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Segundo componente do objeto: serviço gerenciado de IAM. O RFP não diz se inclui fornecimento de ferramenta (ver Lacuna no Anexo I, seção 3).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Define esforço de operação de identidades e possível fornecimento de ferramentas",
  framework=ISO, controle="A.5.16 Gestão de identidade", associacao="Direta",
  relacionados=["d02_iam_ferramenta"], acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d01_usuarios", "D01", "2. OBJETO — 2.1", P2, '"abrangendo aproximadamente 4.500 colaboradores"',
  "Dado de dimensionamento", "Técnico/Arquitetura",
  "Base de dimensionamento do objeto. Diverge da apresentação do workshop (6.200 usuários ativos e mais ~900 das subsidiárias) e foi alterada pelo Q&A nº 5 (5.000 usuários).",
  obrigatoriedade="Informativo", s=4, p=3,
  impacto="Licenças e esforço de IAM, MFA e recertificação e eventual preço por usuário dependem dessa base",
  **NA, relacionados=["d03_contr_usuarios", "d04_q5"], vigencia="Alterado", acao="Esclarecer no Q&A",
  responsavel="Pré-venda/Arquitetura")
I("d01_workshop", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2, '"Workshop de apresentação do ambiente 22/10/2026"',
  "Prazo / marco", "Administrativo do processo",
  "Workshop com proponentes; o material correspondente é o D03. O RFP não diz se o conteúdo apresentado tem valor contratual.",
  obrigatoriedade="Informativo", s=2, p=3, impacto="Fonte de dados de dimensionamento e de escopo adicional (ver D03)",
  **NA, relacionados=["d03_inv"], acao="Atender", responsavel="Bid Manager")
I("d01_perguntas", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2, '"Prazo final para envio de perguntas 05/11/2026"',
  "Prazo / marco", "Administrativo do processo",
  "Última data para pedidos de esclarecimento; as perguntas desta matriz dependem dela. O cronograma não prevê nova rodada (ver Lacuna em D04).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Perguntas não enviadas no prazo viram premissas ou ressalvas na proposta",
  **NA, relacionados=["d04_rodada"], acao="Atender", responsavel="Bid Manager")
I("d01_respostas", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2, '"Divulgação das respostas 12/11/2026"',
  "Prazo / marco", "Administrativo do processo",
  "Respostas publicadas em 12/11/2026 (D04).",
  obrigatoriedade="Informativo", s=1, p=3, impacto="Sem efeito relevante além do calendário", **NA,
  relacionados=["d04_inv"], responsavel="Bid Manager")
I("d01_entrega", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2, '"Entrega das propostas 20/11/2026, até as 18h"',
  "Prazo / marco", "Administrativo do processo",
  "Data de entrega original. Probabilidade 2: prazo explícito e objetivo, depois prorrogado para 27/11/2026 pelo Q&A nº 1, o que reduz o risco de perda.",
  obrigatoriedade="Mandatório", s=5, p=2, impacto="Proposta fora do prazo não é recebida", **NA,
  relacionados=["d04_q1"], vigencia="Alterado", acao="Atender", responsavel="Bid Manager")
I("d01_inicio", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2, '"Início previsto dos serviços 01/02/2027"',
  "Prazo / marco", "Transição/Implantação",
  "Início previsto no dia seguinte ao fim do contrato do SIEM legado (31/01/2027, sem prorrogação — D03). O cronograma não informa a data de assinatura do contrato, embora o prazo de transição (3.2) seja contado a partir dela.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Define o prazo real disponível para transição e o início da exposição a SLAs e multas",
  **NA, relacionados=["d03_siem_legado", "d03_risco_transicao"], acao="Esclarecer no Q&A",
  pergunta="Qual a data prevista de assinatura do contrato? 01/02/2027 é o início da operação plena (após a transição) ou do início da transição?",
  responsavel="Delivery/Operação")
I("d01_transicao", "D01", "3. CRONOGRAMA DO PROCESSO — 3.2", P2,
  '"A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato."',
  "Prazo / marco", "Transição/Implantação",
  "Prazo de transição de 30 dias corridos. Contradito pelo Anexo I, 4.1 (60 dias).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Dimensiona a equipe e o custo da transição e o risco de multas iniciais",
  framework=I20000, controle="Planejamento e transição de serviços (identificador a confirmar)", associacao="Correlata",
  relacionados=["d02_transicao"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A", responsavel="Delivery/Operação")
I("d01_idioma", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.1", P3,
  '"A proposta deverá ser redigida em língua portuguesa"', "Instrução de resposta", "Administrativo do processo",
  "Idioma obrigatório: português. Documentos técnicos de fabricantes em inglês podem exigir tradução; o RFP não diz se anexos em outro idioma são aceitos.",
  obrigatoriedade="Mandatório", s=2, p=3, impacto="Esforço de tradução de anexos", **NA, acao="Atender",
  responsavel="Bid Manager")
I("d01_portal", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.1", P3,
  '"enviada exclusivamente pelo portal de fornecedores do Banco"', "Instrução de resposta", "Administrativo do processo",
  "Canal único de envio. O RFP não informa endereço do portal, exigência e prazo de cadastro prévio do fornecedor, nem limites de tamanho ou formato de arquivo.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Falha de cadastro ou de upload impede a entrega", **NA,
  acao="Esclarecer no Q&A",
  pergunta="Qual o endereço do portal de fornecedores, há cadastro prévio obrigatório (com prazo) e há limite de tamanho ou formato de arquivo para envio?",
  responsavel="Bid Manager")
I("d01_paginas", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.2", P3,
  '"A proposta técnica deverá ter no máximo 40 (quarenta) páginas, excluídos os anexos."', "Instrução de resposta",
  "Administrativo do processo",
  "Limite de 40 páginas. Não define formato de página e fonte, a consequência de exceder o limite, nem se o questionário conta como anexo.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Excesso pode levar à desconsideração de conteúdo pontuável", **NA,
  acao="Esclarecer no Q&A",
  pergunta="Qual a consequência de exceder 40 páginas (desconsideração das páginas excedentes ou desclassificação)? Há formato mínimo de página e fonte?",
  responsavel="Bid Manager")
I("d01_planilha_precos", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.3", P3,
  '"A proposta comercial deverá ser apresentada conforme a planilha modelo do Anexo IV — Planilha de Preços."',
  "Instrução de resposta", "Comercial/Preço",
  "Formato obrigatório da proposta comercial, dependente de anexo não fornecido (ver Lacuna seguinte).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Proposta comercial fora do modelo pode ser rejeitada; estrutura de preço desconhecida",
  **NA, relacionados=["d01_lac_anexo4"], acao="Atender", responsavel="Pricing/Financeiro")
I("d01_lac_anexo4", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.3", P3,
  'Não localizado · "conforme a planilha modelo do Anexo IV — Planilha de Preços"', "Lacuna", "Comercial/Preço",
  "Anexo IV citado pelo cliente e não fornecido no pacote (nem listado pelo usuário). Sem ele não se conhece a estrutura de preços (itens, unidades, parcelas fixas e variáveis, preço por usuário ou por volumetria), que afeta a formação do preço e a Nota de Preço.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Impede montar a proposta comercial no formato exigido e alinhar o modelo de custos",
  **NA, relacionados=["d01_planilha_precos"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Solicitamos o envio do Anexo IV — Planilha de Preços, citado no item 4.3 da RFP, que não consta do pacote disponibilizado.",
  responsavel="Pricing/Financeiro", pendencia="Anexo IV — Planilha de Preços citado e não fornecido")
I("d01_questionario", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.4", P3,
  '"O questionário técnico (planilha anexa) deverá ser integralmente preenchido."', "Instrução de resposta",
  "Administrativo do processo",
  "O questionário é o D04 (aba 'Questionário Técnico'). O D04 agrava a regra: todas as abas são obrigatórias, sob pena de desclassificação.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Esforço de resposta; ver critério eliminatório em D04", **NA,
  relacionados=["d04_instr"], acao="Atender", responsavel="Bid Manager")
I("d01_iso", "D01", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 a)", P3,
  '"certificado ISO/IEC 27001 vigente, emitido por organismo acreditado, cujo escopo inclua os serviços de SOC"',
  "Critério eliminatório / de habilitação", "Segurança da Informação/Cyber",
  "Probabilidade 5: o caput do 5.1 determina inabilitação direta de quem não apresentar o certificado. O escopo deve incluir o SOC; IAM não é exigido no escopo. Repetido no Questionário (QT-01, peso 3).",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação", framework=ISO_SGSI,
  controle="Certificação do SGSI (requisitos das cláusulas 4 a 10)", associacao="Direta",
  relacionados=["d04_qt01"], acao="Atender", responsavel="Compliance")
I("d01_atestados", "D01", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 b)", P3,
  '"no mínimo 3 (três) atestados de capacidade técnica de prestação de serviços de SOC para instituições financeiras, com ambiente de no mínimo 2.000 usuários"',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Probabilidade 5: inabilitação direta pelo caput do 5.1. Ver ambiguidade sobre a forma de contagem.",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação", **NA,
  relacionados=["d01_atestados_amb"], acao="Atender", responsavel="Bid Manager")
I("d01_atestados_amb", "D01", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 b)", P3, '"com ambiente de no mínimo 2.000 usuários"',
  "Ambiguidade", "Administrativo do processo",
  "Não está claro se cada atestado deve comprovar 2.000 usuários ou se a soma é admitida; se valem contratos encerrados; se 'instituições financeiras' inclui seguradoras, cooperativas e fintechs; e se atestados de empresas do mesmo grupo são aceitos. A interpretação errada leva à inabilitação.",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Risco de inabilitação por interpretação divergente dos atestados", **NA,
  relacionados=["d01_atestados"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Cada um dos 3 atestados deve comprovar individualmente ambiente com no mínimo 2.000 usuários, ou é admitido o somatório? São aceitos atestados de contratos encerrados e de empresas do mesmo grupo econômico? Quais entidades contam como 'instituições financeiras'?",
  responsavel="Bid Manager")
I("d01_soc_br", "D01", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 c)", P3,
  '"comprovação de que o SOC está localizado em território nacional"', "Critério eliminatório / de habilitação",
  "Segurança da Informação/Cyber / Regulatório/Compliance",
  "Probabilidade 5: inabilitação direta pelo caput do 5.1. Confirmado pelo Q&A nº 2. O RFP não define o meio de comprovação.",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação; impede SOC no exterior (follow-the-sun)",
  framework=RES, controle="Contratação de serviços prestados no exterior (identificador a confirmar)", associacao="Correlata",
  relacionados=["d04_q2", "d01_anexo3_decl"], acao="Atender",
  pergunta="Que documento será aceito como comprovação de que o SOC está em território nacional (declaração, comprovante de endereço, vistoria)?",
  responsavel="Compliance")
I("d01_equipe_cert", "D01", "5. CRITÉRIOS DE HABILITAÇÃO — 5.2", P3,
  '"O proponente deverá possuir equipe técnica devidamente certificada."', "Ambiguidade", "Pessoas/Equipe",
  "Está na seção de habilitação, mas fora da lista de motivos de inabilitação do 5.1. Não define quais certificações, para quais perfis, em que quantidade nem como comprovar. A única certificação nominada é a CISSP do coordenador (Anexo I, 5.1). Se tratado como habilitação, pode inabilitar.",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Risco de inabilitação ou de perda de pontos em 'Qualificação da equipe' sem critério objetivo",
  framework=ISO_SGSI, controle="Cláusula 7.2 Competência", associacao="Correlata",
  relacionados=["d02_cissp", "d04_qt06", "d01_crit_equipe"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="O item 5.2 é critério de habilitação? Quais certificações, para quais perfis e em que quantidade são exigidas, e que documentos comprovam (certificados nominais, vínculo com o proponente)?",
  responsavel="RH/Staffing")
I("d01_pesos", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.1", P4,
  '"A nota final será composta pela Nota Técnica (peso de 60%) e pela Nota de Preço (peso de 40%)."',
  "Critério de avaliação / pontuação", "Administrativo do processo",
  "Técnica e preço com pesos 60/40: a qualidade técnica pesa mais que o preço.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Orienta a estratégia de preço × investimento na solução técnica", **NA,
  acao="Nenhuma (informativo)", responsavel="Bid Manager")
I("d01_lac_preco", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.1", P4, 'Não localizado · "pela Nota de Preço (peso de 40%)"',
  "Lacuna", "Comercial/Preço",
  "Não há fórmula de cálculo da Nota de Preço (proporcional ao menor preço, faixas, preço de referência) nem critério de inexequibilidade.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Impede simular o efeito do preço na nota final e definir a estratégia de preço",
  **NA, vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Qual a fórmula de cálculo da Nota de Preço? Há critério de preço inexequível ou preço máximo aceitável?",
  responsavel="Pricing/Financeiro")
for k, txt, pts, d in [
    ("d01_crit_metod", "Metodologia de operação do SOC 20", 20, "Maior peso junto com equipe; sem subcritérios definidos."),
    ("d01_crit_equipe", "Qualificação da equipe 20", 20, "Sem critério objetivo de certificações (ver 5.2)."),
    ("d01_crit_ferr", "Ferramentas e tecnologia 15", 15, "Oferta de PAM (desejável) e SOAR pode influenciar a nota."),
    ("d01_crit_transicao", "Plano de transição 10", 10, "Pontuado sobre prazo contraditório (30 × 60 dias)."),
]:
    I(k, "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", P4, f'"{txt}"', "Critério de avaliação / pontuação",
      "Administrativo do processo", f"Critério técnico com pontuação máxima de {pts}. {d}",
      obrigatoriedade="Informativo", s=3, p=3, impacto="Distribuição da Nota Técnica e do esforço de redação", **NA,
      relacionados=["d01_contr_nota"], acao="Atender", responsavel="Bid Manager")
I("d01_contr_nota", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", P4,
  'A: "A Nota Técnica, de no máximo 60 (sessenta) pontos" · B: "Metodologia de operação do SOC 20" · "Qualificação da equipe 20" · "Ferramentas e tecnologia 15" · "Plano de transição 10" (soma: 65 pontos)',
  "Contradição", "Administrativo do processo",
  "A soma dos critérios (65) excede o máximo declarado (60). Afeta o corte de 70% do 6.3 (42 ou 45,5 pontos) e o peso relativo de cada critério; não se sabe se haverá normalização.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Incerteza sobre a nota mínima para não ser desclassificado e sobre onde investir esforço",
  **NA, relacionados=["d01_crit_metod", "d01_crit_equipe", "d01_crit_ferr", "d01_crit_transicao", "d01_corte"],
  vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="A soma dos critérios do item 6.2 é 65 pontos, mas o máximo declarado é 60. Qual a pontuação correta de cada critério e a máxima? Haverá normalização? O corte de 70% do item 6.3 incidirá sobre qual total?",
  responsavel="Bid Manager")
I("d01_lac_criterios", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", P4,
  'Não localizado · "será atribuída conforme os critérios abaixo"', "Lacuna", "Administrativo do processo",
  "Não há subcritérios, escala de notas nem evidências esperadas por critério; a avaliação fica subjetiva, e o corte eliminatório de 70% depende dela.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Proposta pode não endereçar o que será pontuado; risco no corte técnico",
  **NA, relacionados=["d01_corte"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Quais subcritérios, escala de pontuação e evidências serão usados para atribuir a nota de cada critério do item 6.2?",
  responsavel="Bid Manager")
I("d01_corte", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.3", P4,
  '"Serão desclassificadas as propostas com Nota Técnica inferior a 70% (setenta por cento) da pontuação máxima."',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Corte técnico eliminatório. Probabilidade mantida em 3 porque o resultado depende de avaliação sem critérios definidos; a base (60 ou 65 pontos) é contraditória e há dedução de 2 pontos por requisito não obrigatório não atendido escondida na aba 'Pesos' do D04.",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Desclassificação", **NA,
  relacionados=["d01_contr_nota", "d01_lac_criterios", "d04_pesos_regra"], acao="Atender", responsavel="Bid Manager")
I("d01_empate", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.4", P4,
  '"Em caso de empate na nota final, prevalecerá a proposta de menor preço."', "Critério de avaliação / pontuação",
  "Administrativo do processo", "Critério de desempate por menor preço.",
  obrigatoriedade="Informativo", s=1, p=3, impacto="Efeito apenas em caso de empate exato", **NA,
  acao="Nenhuma (informativo)", responsavel="Pricing/Financeiro")
I("d01_vigencia", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.1", P5,
  '"O contrato terá vigência de 36 (trinta e seis) meses, prorrogável por iguais períodos mediante acordo entre as partes."',
  "Obrigação contratual", "Jurídico/Contratual",
  "Vigência de 36 meses para amortizar SIEM e transição; prorrogação por acordo, sem limite de vezes. Não há regras de rescisão antecipada nem de saída (ver Lacuna no Anexo I).",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Prazo de amortização de investimentos e de licenças", **NA,
  relacionados=["d02_lac_saida"], acao="Precificar", responsavel="Pricing/Financeiro")
I("d01_reajuste", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.2", P5,
  '"Os preços serão reajustados anualmente pela variação do IPCA."', "Obrigação contratual", "Comercial/Preço",
  "Reajuste anual pelo IPCA, sem data-base definida (proposta ou assinatura). Custos atrelados a moeda estrangeira (licenças, nuvem) ficam sem proteção cambial.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Perda de margem por defasagem ou variação cambial", **NA,
  acao="Esclarecer no Q&A", pergunta="Qual a data-base para o primeiro reajuste pelo IPCA: a data da proposta ou a da assinatura do contrato?",
  responsavel="Pricing/Financeiro")
I("d01_pagamento", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.3", P5,
  '"O pagamento será efetuado em até 60 (sessenta) dias após o aceite da nota fiscal."', "Obrigação contratual",
  "Financeiro",
  "Probabilidade 5: o prazo de 60 dias após o aceite é explícito, e o custo financeiro decorre diretamente do texto. Não há prazo para o aceite da nota fiscal, o que pode alongar o ciclo de recebimento.",
  obrigatoriedade="Mandatório", s=3, p=5, impacto="Custo de capital de giro de pelo menos 2 meses de faturamento", **NA,
  acao="Precificar", pergunta="Qual o prazo máximo para o aceite da nota fiscal após sua emissão?", responsavel="Pricing/Financeiro")
I("d01_multa", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.4", P5,
  '"O descumprimento de qualquer nível de serviço (SLA) previsto no Anexo I sujeitará a Contratada a multa de 10% (dez por cento) do valor mensal do contrato, por ocorrência."',
  "Penalidade / multa / glosa", "Jurídico/Contratual / Financeiro",
  "Multa fixa de 10% do valor mensal por ocorrência, sem gradação por gravidade, sem teto e sem relação com a causa. Com SLA de 15 minutos por incidente crítico (Anexo I, 2.1), poucas ocorrências no mês anulam a receita mensal. 'Ocorrência' não é definida para indicadores mensais (disponibilidade). "
  "Probabilidade 4: a multa incide automaticamente a cada ocorrência, e o cliente recusou fixar limite (Q&A nº 4).",
  obrigatoriedade="Mandatório", s=5, p=4, impacto="Exposição financeira sem teto; pode superar o faturamento mensal",
  framework=CC, controle="Cláusula penal — arts. 412 e 413", associacao="Correlata",
  relacionados=["d02_sla15", "d04_q4"], acao="Propor exceção/ressalva",
  pergunta="Como se define 'ocorrência' para indicadores mensais (por exemplo, disponibilidade de 99,9%)? O Banco admite gradação da multa por gravidade do SLA e carência durante a transição?",
  responsavel="Jurídico")
I("d01_resp_ilimitada", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.5", P5,
  '"A Contratada responderá de forma integral e ilimitada por quaisquer danos decorrentes de incidentes de segurança ocorridos no ambiente do Contratante."',
  "Obrigação contratual", "Jurídico/Contratual",
  "Responsabilidade sem teto e sem vínculo com culpa ou causa atribuível à Contratada: alcança qualquer incidente no ambiente do Contratante, inclusive os causados por terceiros ou fora do escopo monitorado, e não exclui danos indiretos nem lucros cessantes. O Q&A nº 4 indica que o cliente não pretende alterar o item 7.",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Exposição jurídica e financeira ilimitada; pode inviabilizar seguro e aprovação interna",
  framework=CC, controle="Responsabilidade civil contratual e limitação de responsabilidade (identificador a confirmar)",
  associacao="Correlata", relacionados=["d01_seguro", "d04_q4"], acao="Propor exceção/ressalva",
  pergunta="A responsabilidade do item 7.5 se limita a danos causados por culpa ou dolo da Contratada? O Banco admite teto (por exemplo, valor anual do contrato) e exclusão de danos indiretos e lucros cessantes?",
  responsavel="Jurídico")
I("d01_seguro", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.6", P5,
  '"seguro de responsabilidade civil cibernética em valor compatível com os riscos do contrato"', "Ambiguidade",
  "Jurídico/Contratual / Financeiro",
  "Obrigação de manter seguro cibernético sem valor mínimo, franquia ou critério para 'compatível'. Com responsabilidade ilimitada (7.5), nenhum valor de apólice é objetivamente compatível, e o prêmio não pode ser estimado com segurança.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Custo de prêmio indeterminado; risco de descumprimento contratual", **NA,
  relacionados=["d01_resp_ilimitada"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Qual o valor mínimo de cobertura do seguro cibernético exigido e em que momento a apólice deve ser apresentada (proposta, assinatura ou início dos serviços)?",
  responsavel="Jurídico")
I("d01_subcontratacao", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.7", P5,
  '"É vedada a subcontratação, total ou parcial, do objeto deste contrato."', "Restrição", "Jurídico/Contratual",
  "Veda qualquer subcontratação. Não está claro se provedor de nuvem para o SIEM (Anexo I, 1.2), fabricantes de software, serviço de threat intelligence (QT-05) ou parceiros de resposta a incidentes configuram subcontratação. Impede modelos com SOC ou IAM operados por parceiro.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Restringe a arquitetura da solução e alianças; pode exigir capacidade própria",
  framework=ISO, controle="A.5.19 Segurança da informação nas relações com fornecedores", associacao="Correlata",
  relacionados=["d02_siem", "d04_qt05"], acao="Esclarecer no Q&A",
  pergunta="O uso de provedores de nuvem (IaaS/SaaS) para hospedar o SIEM, de licenças de fabricantes e de serviços de inteligência de ameaças de terceiros é considerado subcontratação vedada pelo item 7.7?",
  responsavel="Jurídico")
I("d01_confid", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.8", P5,
  '"As obrigações de confidencialidade vigorarão por 5 (cinco) anos após o término do contrato."',
  "Obrigação contratual", "Jurídico/Contratual", "Confidencialidade com sobrevida de 5 anos após o término.",
  obrigatoriedade="Mandatório", s=2, p=3, impacto="Obrigação pós-contratual de baixo custo",
  framework=ISO, controle="A.6.6 Acordos de confidencialidade ou de não divulgação", associacao="Direta",
  acao="Atender", responsavel="Jurídico")
I("d01_anexo3_decl", "D01", "Anexo III — Declaração de Localização de Dados", P6,
  '"Esta declaração deverá ser entregue assinada pelo representante legal do proponente junto com a proposta, sob pena de inabilitação."',
  "Critério eliminatório / de habilitação", "Regulatório/Compliance",
  "Conteúdo lido da imagem escaneada da p. 6. Probabilidade 5: o texto determina inabilitação direta se a declaração assinada não for entregue. Assinar a declaração vincula o proponente à residência de dados no Brasil, o que conflita com a liberdade de região do SIEM (Anexo I, 1.2).",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação; declaração vinculante durante toda a vigência", **NA,
  relacionados=["d01_residencia", "d02_contr_regiao"], acao="Atender", responsavel="Jurídico")
I("d01_residencia", "D01", "Anexo III — Declaração de Localização de Dados", P6,
  '"todos os dados do Banco Horizonte Fictício S.A., incluindo os registros (logs) de segurança, serão armazenados e processados exclusivamente em território nacional, durante toda a vigência do contrato"',
  "Restrição", "Regulatório/Compliance / Infraestrutura/Cloud",
  "Residência de dados obrigatória no Brasil para todos os dados, inclusive logs, tanto no armazenamento quanto no processamento. Restringe SIEM SaaS, análise por terceiros e suporte de fabricante no exterior. A declaração cobre só a vigência, mas a retenção de logs por 5 anos (Anexo I, 1.6) pode ultrapassá-la.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Limita a escolha de plataforma e região de nuvem; pode elevar custo de infraestrutura",
  framework=RES, controle="Processamento e armazenamento de dados e computação em nuvem no exterior (identificador a confirmar)",
  associacao="Correlata", relacionados=["d02_contr_regiao", "d02_contr_logs"], acao="Atender",
  responsavel="Pré-venda/Arquitetura")
I("d01_lac_anexo2", "D01", "2.2 · 4.3 · Anexo III (numeração de anexos)", f"{P2} · {P3} · {P6}",
  'Não localizado · "constam do Anexo I — Especificação Técnica" · "Anexo IV — Planilha de Preços" · "ANEXO III — DECLARAÇÃO DE LOCALIZAÇÃO DE DADOS"',
  "Lacuna", "Administrativo do processo",
  "Inferido: a numeração dos anexos (I, III e IV citados ou presentes) indica a existência de um Anexo II, que não é citado nem fornecido. Pode conter conteúdo relevante (minuta contratual, modelo de proposta, SLAs).",
  obrigatoriedade="Informativo", natureza="Inferida", s=3, p=3, impacto="Possível documento do pacote não analisado", **NA,
  vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Existe um Anexo II desta RFP? Em caso positivo, solicitamos o envio.", responsavel="Bid Manager",
  pendencia="possível Anexo II, inferido pela numeração, não citado nem fornecido")

# =============================================================== D02 — Anexo I
S1 = "§ 1. SERVIÇOS DE SOC"
S2 = "§ 2. NÍVEIS DE SERVIÇO (SLA)"
S3 = "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM)"
S4 = "§ 4. TRANSIÇÃO"
S5 = "§ 5. EQUIPE"
S6 = "§ 6. RESPONSABILIDADES DO CONTRATANTE"
I("d02_inv", "D02", "Documento inteiro (§ 1 a § 6)", "§ Anexo I — Especificação Técnica a § 6",
  '"Anexo I — Especificação Técnica"', "Registro de cobertura", "Administrativo do processo",
  "Inventário D02: Word com 22 parágrafos em 6 seções numeradas, sem tabelas; a extração não sinalizou comentários nem marcas de revisão. Sem paginação fixa: localizador por seção e item. Versão no cabeçalho: 'Versão 1.0 — 15/10/2026'.",
  responsavel="Bid Manager")
I("d02_monit", "D02", "1. SERVIÇOS DE SOC — 1.1", f"{S1} · item 1.1",
  '"O proponente deverá prestar serviço de monitoramento contínuo de eventos de segurança, em regime 24x7x365."',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber / Operação/Serviços",
  "Detalha o objeto da RFP (2.1): monitoramento contínuo 24x7x365.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Equipe em turnos 24x7", framework=ISO,
  controle="A.8.16 Atividades de monitoramento", associacao="Direta", relacionados=["d01_soc"],
  vigencia="Duplicado", acao="Precificar", responsavel="Delivery/Operação")
I("d02_siem", "D02", "1. SERVIÇOS DE SOC — 1.2", f"{S1} · item 1.2", '"O proponente deverá fornecer a solução de SIEM"',
  "Requisito funcional / de serviço", "Técnico/Arquitetura / Infraestrutura/Cloud",
  "SIEM (licenças e infraestrutura) é fornecimento do proponente. O custo depende da volumetria (EPS/GB por dia), negada até a contratação (Q&A nº 3), da retenção (12 meses × 5 anos) e da migração de 24 meses de logs (D03). Não há regra sobre propriedade de licenças e dados ao fim do contrato.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Maior componente variável do preço, sem base de dimensionamento",
  framework=ISO, controle="A.8.15 Registros (logging)", associacao="Correlata",
  relacionados=["d04_q3", "d02_contr_logs", "d02_lac_saida"], acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d02_contr_regiao", "D02", "1. SERVIÇOS DE SOC — 1.2 × RFP Anexo III", f"{S1} · item 1.2 · D01 {P6}",
  'A: D02 "podendo esta ser disponibilizada em nuvem pública, em região de livre escolha do proponente" · B: D01 "serão armazenados e processados exclusivamente em território nacional"',
  "Contradição", "Infraestrutura/Cloud / Regulatório/Compliance",
  "O Anexo I permite SIEM em nuvem em qualquer região; o Anexo III (eliminatório) exige que todos os dados, inclusive logs, sejam armazenados e processados no Brasil. Quem dimensionar o SIEM em região estrangeira (em geral mais barata) não pode assinar a declaração sem descumpri-la. A Res. CMN 4.893/2021 (RFP 1.2) reforça a necessidade de definição.",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Inabilitação ou descumprimento contratual se a região errada for adotada; diferença de custo de infraestrutura",
  framework=ISO, controle="A.5.23 Segurança da informação para uso de serviços em nuvem", associacao="Correlata",
  relacionados=["d01_residencia", "d01_anexo3_decl", "d01_res4893", "d01_precedencia"], vigencia="Em esclarecimento",
  acao="Esclarecer no Q&A",
  pergunta="O item 1.2 do Anexo I admite SIEM em nuvem pública em região de livre escolha, mas o Anexo III exige armazenamento e processamento exclusivamente em território nacional. Prevalece o Anexo III, isto é, a região de nuvem deve estar no Brasil?",
  responsavel="Pré-venda/Arquitetura")
I("d02_ret12", "D02", "1. SERVIÇOS DE SOC — 1.3", f"{S1} · item 1.3",
  '"Os registros (logs) de segurança deverão ser retidos por no mínimo 12 (doze) meses."', "Requisito não funcional",
  "Segurança da Informação/Cyber", "Retenção mínima de 12 meses; conflita com os 5 anos do item 1.6.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Dimensiona o armazenamento do SIEM", framework=ISO,
  controle="A.8.15 Registros (logging)", associacao="Direta", relacionados=["d02_contr_logs", "d04_qt03"],
  vigencia="Em esclarecimento", acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d02_lgpd", "D02", "1. SERVIÇOS DE SOC — 1.3 · 3. IAM — 3.1", f"{S1} · item 1.3 · {S3} · item 3.1",
  '"Os registros (logs) de segurança deverão ser retidos" · "Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"',
  "Requisito implícito", "Privacidade/Proteção de Dados",
  "Inferido: logs de segurança e dados de identidade de 4.500 a 7.100 usuários contêm dados pessoais (usuário, IP, nome, cargo, eventos de RH). Ao tratá-los por conta do Banco, o proponente atua como operador na LGPD, com dever de seguir as instruções do controlador, adotar medidas de segurança e apoiar a comunicação de incidentes. O RFP não traz cláusula de proteção de dados nem acordo de tratamento.",
  obrigatoriedade="Mandatório", natureza="Inferida", s=4, p=3,
  impacto="Obrigações e responsabilidade de operador não precificadas; somam-se à responsabilidade ilimitada do 7.5",
  framework=LGPD, controle="art. 5º, VII (operador) · art. 39 (tratamento conforme instruções do controlador) · art. 46 (medidas de segurança)",
  associacao="Direta", relacionados=["d01_resp_ilimitada"], acao="Esclarecer no Q&A",
  pergunta="O Banco celebrará acordo de tratamento de dados pessoais com a Contratada, na condição de operadora? Quais obrigações e prazos de comunicação de incidentes serão exigidos?",
  responsavel="Compliance")
I("d02_integracao", "D02", "1. SERVIÇOS DE SOC — 1.4", f"{S1} · item 1.4",
  '"O SIEM deverá ser integrado a todos os ativos relevantes do Contratante."', "Ambiguidade", "Técnico/Arquitetura",
  "'Ativos relevantes' não é definido: não há lista de fontes de log, tecnologias, quantidade de conectores nem volumetria. O ambiente tem 850 servidores, 2 data centers e 2 nuvens públicas (D03), e a volumetria foi negada até a contratação (Q&A nº 3).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Escopo de integração aberto; risco de integrações não previstas no preço fixo",
  framework=ISO, controle="A.8.15 Registros (logging)", associacao="Correlata",
  relacionados=["d04_q3", "d03_servidores", "d03_nuvens"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Qual a lista (ou quantidade por tipo) de ativos 'relevantes' a integrar ao SIEM: servidores, estações, ativos de rede, aplicações, bancos de dados, serviços de nuvem? Integrações customizadas (parsers) estão incluídas no preço?",
  responsavel="Pré-venda/Arquitetura")
I("d02_resposta", "D02", "1. SERVIÇOS DE SOC — 1.5", f"{S1} · item 1.5",
  '"O serviço deverá contemplar resposta a incidentes, incluindo contenção, erradicação"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Contenção e erradicação pressupõem atuação sobre ativos do Contratante. Não define se a atuação é remota ou presencial, os limites de autoridade (isolar servidor, bloquear conta) nem limite de horas ou de incidentes. Somada à responsabilidade ilimitada (7.5), amplia a exposição.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Esforço de resposta sem limite definido; exposição a responsabilidade por ações de contenção",
  framework=CSF, controle="RS.MI-01 (contenção) · RS.MI-02 (erradicação)", associacao="Direta",
  relacionados=["d01_resp_ilimitada"], acao="Esclarecer no Q&A",
  pergunta="A resposta a incidentes (contenção e erradicação) é remota ou inclui atuação presencial? Há limite de horas ou de incidentes incluído no preço? Quais ações a Contratada pode executar sem aprovação prévia?",
  responsavel="Delivery/Operação")
I("d02_rel_pos", "D02", "1. SERVIÇOS DE SOC — 1.5", f"{S1} · item 1.5", '"elaboração de relatório pós-incidente"',
  "Entregável", "Segurança da Informação/Cyber", "Relatório por incidente; prazo e modelo não definidos.",
  obrigatoriedade="Mandatório", s=2, p=3, impacto="Esforço de documentação por incidente", framework=ISO,
  controle="A.5.27 Aprendizado com incidentes de segurança da informação", associacao="Correlata",
  acao="Atender", responsavel="Delivery/Operação")
I("d02_contr_logs", "D02", "1. SERVIÇOS DE SOC — 1.3 × 1.6", f"{S1} · itens 1.3 e 1.6",
  'A: "Os registros (logs) de segurança deverão ser retidos por no mínimo 12 (doze) meses." · B: "Para fins de auditoria, os logs deverão ser mantidos por 5 (cinco) anos."',
  "Contradição", "Segurança da Informação/Cyber / Infraestrutura/Cloud",
  "Retenção de 12 meses (1.3, repetida no QT-03 como 'online') × 5 anos para auditoria (1.6). Pode significar 12 meses online + 5 anos em arquivo, mas isso não está escrito. A diferença de armazenamento é de até 5 vezes, sem volumetria (Q&A nº 3). Os 5 anos ultrapassam a vigência de 36 meses e a declaração do Anexo III, que cobre só a vigência.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Diferença relevante no custo de armazenamento e obrigação pós-contratual indefinida",
  framework=ISO, controle="A.8.15 Registros (logging)", associacao="Correlata",
  relacionados=["d02_ret12", "d04_qt03", "d04_q3", "d01_vigencia"], vigencia="Em esclarecimento",
  acao="Esclarecer no Q&A",
  pergunta="A retenção é de 12 meses (item 1.3) ou de 5 anos (item 1.6)? Se ambas, os 12 meses são em armazenamento online pesquisável e os 5 anos em arquivo? Quem guarda os logs após o término do contrato, se os 5 anos ultrapassarem a vigência?",
  responsavel="Pré-venda/Arquitetura")
I("d02_sla15", "D02", "2. NÍVEIS DE SERVIÇO (SLA) — 2.1", f"{S2} · item 2.1",
  '"Tempo máximo para início do tratamento de incidentes críticos: 15 (quinze) minutos."', "SLA / KPI",
  "Operação/Serviços",
  "SLA por incidente; cada descumprimento gera multa de 10% do valor mensal (RFP 7.4). 'Incidente crítico' depende da matriz do Contratante, não fornecida (2.4). Não define o evento que inicia a contagem (alerta, detecção, abertura de chamado).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Exige equipe 24x7 com capacidade de resposta imediata; principal gatilho de multas",
  framework=ITIL, controle="Prática de gerenciamento de nível de serviço", associacao="Correlata",
  relacionados=["d01_multa", "d02_lac_matriz"], acao="Esclarecer no Q&A",
  pergunta="O prazo de 15 minutos conta a partir de qual evento (geração do alerta no SIEM, triagem ou abertura de chamado) e o que caracteriza o 'início do tratamento'?",
  responsavel="Delivery/Operação")
I("d02_sla_disp", "D02", "2. NÍVEIS DE SERVIÇO (SLA) — 2.2", f"{S2} · item 2.2",
  '"Disponibilidade mínima mensal da plataforma SIEM: 99,9%."', "SLA / KPI", "Infraestrutura/Cloud",
  "Cerca de 43 minutos de indisponibilidade por mês. Não define janelas de manutenção programada, método de medição nem se falha do provedor de nuvem conta contra a Contratada.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Exige arquitetura redundante do SIEM", framework=ITIL,
  controle="Prática de gerenciamento de disponibilidade", associacao="Direta", relacionados=["d01_multa"],
  acao="Esclarecer no Q&A",
  pergunta="Janelas de manutenção programada são excluídas do cálculo da disponibilidade de 99,9%? Como e por qual ferramenta a disponibilidade será medida?",
  responsavel="Pré-venda/Arquitetura")
I("d02_rel_mensal", "D02", "2. NÍVEIS DE SERVIÇO (SLA) — 2.3", f"{S2} · item 2.3",
  '"Relatório mensal de indicadores, a ser entregue até o 5º dia útil do mês subsequente."', "SLA / KPI",
  "Operação/Serviços",
  "Entrega mensal com prazo; por estar na seção de SLA, o atraso está sujeito à multa de 10% (RFP 7.4). Conteúdo do relatório não definido.",
  obrigatoriedade="Mandatório", s=2, p=3, impacto="Esforço mensal de relatório; risco de multa por atraso",
  framework=ITIL, controle="Prática de gerenciamento de nível de serviço", associacao="Correlata",
  relacionados=["d01_multa"], acao="Atender", responsavel="Delivery/Operação")
I("d02_lac_matriz", "D02", "2. NÍVEIS DE SERVIÇO (SLA) — 2.4", f"{S2} · item 2.4",
  'Não localizado · "A classificação de criticidade dos incidentes seguirá a matriz de classificação do Contratante."',
  "Lacuna", "Segurança da Informação/Cyber",
  "Matriz citada pelo cliente e não fornecida. Sem ela não se sabe quantos incidentes serão 'críticos' e sujeitos ao SLA de 15 minutos com multa por ocorrência.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Impede estimar o volume de incidentes sob SLA e a exposição a multas",
  framework=ISO, controle="A.5.25 Avaliação e decisão sobre eventos de segurança da informação", associacao="Correlata",
  relacionados=["d02_sla15"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Solicitamos a matriz de classificação de criticidade de incidentes do Contratante, citada no item 2.4 do Anexo I, e o histórico mensal de incidentes por nível.",
  responsavel="Segurança/Cyber", pendencia="matriz de classificação de incidentes do Contratante citada e não fornecida")
I("d02_iam_ciclo", "D02", "3. IAM — 3.1", f"{S3} · item 3.1",
  '"Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Hoje feito com Active Directory e scripts internos (D03). Depende de integração com o RH, que não é mencionada.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Esforço de operação e de integração com o RH", framework=ISO,
  controle="A.5.16 Gestão de identidade", associacao="Direta", relacionados=["d03_iam_atual", "d02_iam_ferramenta"],
  acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d02_revog24", "D02", "3. IAM — 3.1", f"{S3} · item 3.1",
  '"com revogação dos acessos de colaboradores desligados em até 24 (vinte e quatro) horas"', "SLA / KPI",
  "Segurança da Informação/Cyber",
  "SLA de revogação sujeito à multa de 10% por ocorrência (7.4). Não define o marco inicial (data do desligamento ou recebimento da comunicação do RH) nem os sistemas cobertos.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Multa por ocorrência se a comunicação do RH atrasar", framework=ISO,
  controle="A.5.18 Direitos de acesso", associacao="Direta", relacionados=["d01_multa"], acao="Esclarecer no Q&A",
  pergunta="O prazo de 24 horas conta a partir do desligamento ou do recebimento da comunicação formal do RH pela Contratada? Quais sistemas estão no escopo da revogação?",
  responsavel="Delivery/Operação")
I("d02_mfa", "D02", "3. IAM — 3.2", f"{S3} · item 3.2",
  '"Autenticação multifator (MFA) obrigatória para 100% dos usuários com acesso privilegiado."',
  "Requisito não funcional", "Segurança da Informação/Cyber",
  "Não define quem fornece a solução de MFA nem o número de usuários privilegiados.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Possível custo de licenças e implantação de MFA", framework=ISO,
  controle="A.8.5 Autenticação segura", associacao="Direta", relacionados=["d02_iam_ferramenta"], acao="Precificar",
  responsavel="Pré-venda/Arquitetura")
I("d02_recert", "D02", "3. IAM — 3.3", f"{S3} · item 3.3", '"Revisão (recertificação) trimestral dos acessos concedidos."',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Esforço depende do número de usuários (4.500 a 7.100) e de sistemas; hoje não há ferramenta de governança de identidades (D03).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Esforço trimestral recorrente", framework=ISO,
  controle="A.5.18 Direitos de acesso", associacao="Direta", relacionados=["d03_iam_atual"], acao="Precificar",
  responsavel="Delivery/Operação")
I("d02_pam", "D02", "3. IAM — 3.4", f"{S3} · item 3.4",
  '"É desejável que a solução contemple cofre de senhas para contas privilegiadas (PAM)."',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Desejável; o ambiente não tem PAM (D03, slide 3). Incluir aumenta o preço; não incluir pode reduzir a nota em 'Ferramentas e tecnologia'. Ver oportunidade em D03.",
  obrigatoriedade="Desejável", s=3, p=3, impacto="Decisão de oferta opcional com efeito em preço e pontuação",
  framework=ISO, controle="A.8.2 Direitos de acesso privilegiado", associacao="Direta",
  relacionados=["d03_pam", "d01_crit_ferr"], acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d02_iam_ferramenta", "D02", "1. SERVIÇOS DE SOC — 1.2 × 3. IAM", f"{S1} · item 1.2 · {S3} · itens 3.1 a 3.4",
  'Não localizado · "O proponente deverá fornecer a solução de SIEM" · "Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"',
  "Lacuna", "Técnico/Arquitetura",
  "Para o SOC, o Anexo I diz que o proponente fornece o SIEM; para o IAM, não diz se o proponente fornece ferramentas (governança de identidades, MFA, PAM) ou opera as do Banco (hoje Active Directory e scripts internos, D03).",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Diferença relevante de preço entre operar e fornecer a plataforma de IAM",
  **NA, relacionados=["d01_iam", "d03_iam_atual"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Para o IAM, o proponente deve fornecer as ferramentas (governança de identidades, MFA e, se ofertado, PAM) com licenças, ou apenas operar as ferramentas existentes do Banco? Quais sistemas-alvo devem ser integrados ao ciclo de vida?",
  responsavel="Pré-venda/Arquitetura")
I("d02_transicao", "D02", "4. TRANSIÇÃO — 4.1 × RFP 3.2", f"{S4} · item 4.1 · D01 {P2}, item 3.2",
  'A: D01 "A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato." · B: D02 "A transição dos serviços deverá ser concluída em até 60 (sessenta) dias corridos a partir da assinatura do contrato."',
  "Contradição", "Transição/Implantação",
  "Diferença de 30 dias no prazo de transição, sem cláusula de precedência. Afeta equipe de transição, custo da operação paralela (4.2) e o Plano de transição pontuado (10 pontos). Em qualquer caso, o fim do SIEM legado em 31/01/2027 limita o prazo real.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Custo de transição e risco de multas iniciais variam com o prazo adotado",
  framework=I20000, controle="Planejamento e transição de serviços (identificador a confirmar)", associacao="Correlata",
  relacionados=["d01_transicao", "d01_precedencia", "d03_risco_transicao"], vigencia="Em esclarecimento",
  acao="Esclarecer no Q&A",
  pergunta="A RFP (3.2) fixa a transição em 30 dias e o Anexo I (4.1) em 60 dias, ambos a partir da assinatura. Qual prazo prevalece e qual a data prevista de assinatura?",
  responsavel="Delivery/Operação")
I("d02_paralelo", "D02", "4. TRANSIÇÃO — 4.2", f"{S4} · item 4.2",
  '"Durante a transição, o proponente deverá operar em paralelo com o fornecedor atual, sem custo adicional para o Contratante."',
  "Restrição", "Comercial/Preço / Transição/Implantação",
  "Probabilidade 5: o texto exige expressamente operação paralela sem remuneração adicional, então o custo é certo e precisa ser embutido no preço. A duração (30 ou 60 dias) é contraditória, e não há obrigação de cooperação do fornecedor atual (dados, acessos, conhecimento).",
  obrigatoriedade="Mandatório", s=3, p=5, impacto="Custo de equipe e plataforma na transição sem faturamento",
  framework=I20000, controle="Planejamento e transição de serviços (identificador a confirmar)", associacao="Correlata",
  relacionados=["d02_transicao", "d03_siem_legado"], acao="Precificar",
  pergunta="O Banco garantirá contratualmente a cooperação do fornecedor atual durante a transição (acesso a dados, configurações e documentação)?",
  responsavel="Pricing/Financeiro")
I("d02_cissp", "D02", "5. EQUIPE — 5.1", f"{S5} · item 5.1",
  '"O serviço deverá contar com coordenador com certificação CISSP, dedicado exclusivamente ao contrato."',
  "Restrição", "Pessoas/Equipe",
  "Probabilidade 5: custo fixo explicitamente exigido (profissional certificado com dedicação exclusiva durante toda a vigência). Não define se o coordenador deve ser indicado na proposta ou na assinatura.",
  obrigatoriedade="Mandatório", s=3, p=5, impacto="Custo fixo de um profissional sênior dedicado por 36 meses",
  framework=ISO_SGSI, controle="Cláusula 7.2 Competência", associacao="Correlata", relacionados=["d01_equipe_cert"],
  acao="Precificar", responsavel="RH/Staffing")
I("d02_n1", "D02", "5. EQUIPE — 5.2", f"{S5} · item 5.2",
  '"Os analistas de nível 1 deverão atuar presencialmente na sede do Contratante, em São Paulo/SP, em horário comercial."',
  "Restrição", "Pessoas/Equipe",
  "Presença física dos analistas N1 na sede em horário comercial. Alterado pelo Q&A nº 6, que admite atuação remota no território nacional; sem cláusula de precedência, a alteração precisa ser confirmada.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Custo de alocação presencial em São Paulo", **NA,
  relacionados=["d04_q6", "d01_precedencia"], vigencia="Alterado", acao="Registrar premissa na proposta",
  responsavel="RH/Staffing")
I("d02_vpn", "D02", "6. RESPONSABILIDADES DO CONTRATANTE — 6.1", f"{S6} · item 6.1",
  '"Disponibilizar acesso remoto seguro (VPN) aos ambientes monitorados."', "Responsabilidade / dependência do cliente",
  "Infraestrutura/Cloud", "Dependência do cliente para a operação remota. Não há prazo para disponibilizar o acesso.",
  obrigatoriedade="Mandatório", s=2, p=3, impacto="Atraso do acesso atrasa a transição", framework=ISO,
  controle="A.6.7 Trabalho remoto", associacao="Correlata", acao="Registrar premissa na proposta",
  responsavel="Delivery/Operação")
I("d02_doc", "D02", "6. RESPONSABILIDADES DO CONTRATANTE — 6.2", f"{S6} · item 6.2",
  '"Disponibilizar a documentação técnica do ambiente em até 10 (dez) dias após a assinatura do contrato."',
  "Responsabilidade / dependência do cliente", "Transição/Implantação",
  "Com transição de 30 dias (RFP 3.2), a documentação chega no 10º dia e restam 20 dias para integrar o ambiente. Não há consequência prevista se o Contratante atrasar.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Encurta o prazo útil da transição", **NA,
  relacionados=["d01_transicao", "d03_risco_transicao"], acao="Registrar premissa na proposta",
  pergunta="Atrasos do Contratante na entrega da documentação ou do acesso VPN suspenderão os prazos de transição e os SLAs?",
  responsavel="Delivery/Operação")
I("d02_lac_saida", "D02", "Documento inteiro × RFP seção 7", f"{S1} · itens 1.2 e 1.6 · D01 {P5}, seção 7",
  'Não localizado · "O proponente deverá fornecer a solução de SIEM" · "Para fins de auditoria, os logs deverão ser mantidos por 5 (cinco) anos."',
  "Lacuna", "Jurídico/Contratual / Transição/Implantação",
  "Não há regras de encerramento: transição de saída, devolução de logs e configurações, propriedade das licenças do SIEM fornecido, nem condições de rescisão antecipada. Como o SIEM é do proponente e os logs devem ser mantidos por 5 anos, a saída tem custo não descrito.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Custo de saída e investimentos não amortizados em caso de rescisão",
  framework=ISO, controle="A.5.23 Segurança da informação para uso de serviços em nuvem", associacao="Correlata",
  relacionados=["d01_vigencia", "d02_contr_logs"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Ao término ou rescisão do contrato, quais as obrigações de transição de saída (prazo, devolução de logs em formato aberto, licenças do SIEM)? Há condições de rescisão antecipada e indenização de investimentos não amortizados?",
  responsavel="Jurídico")

# =============================================================== D03 — Apresentação
SL2 = 'slide 2 — "Números do ambiente"'
SL3 = 'slide 3 — "Ferramentas atuais"'
SL4 = 'slide 4 — "Desafios"'
SL5 = 'slide 5 — "Expectativas para o novo serviço"'
I("d03_inv", "D03", "Apresentação inteira (slides 1 a 5 e notas)", "slides 1–5 (inclusive notas do slide 5)",
  '"Workshop com proponentes — RFP nº 2026-017 — 22/10/2026"', "Registro de cobertura", "Administrativo do processo",
  "Inventário D03: 5 slides, sem slides ocultos sinalizados; o slide 5 tem notas do apresentador, analisadas (contêm ampliação de escopo). Material de workshop: a RFP não define seu valor contratual.",
  responsavel="Bid Manager")
I("d03_contr_usuarios", "D03", "Números do ambiente × RFP 2.1", f"{SL2} · D01 {P2}, item 2.1",
  'A: D01 "abrangendo aproximadamente 4.500 colaboradores" · B: D03 "6.200 usuários ativos"', "Contradição",
  "Técnico/Arquitetura",
  "Diferença de 38% na base de usuários. Pode refletir conceitos diferentes (colaboradores × contas ativas, com terceiros e contas de serviço), mas nenhum documento explica.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Licenças de IAM/MFA, esforço de recertificação e preço por usuário",
  **NA, relacionados=["d01_usuarios", "d03_subsidiarias", "d04_q5"], vigencia="Em esclarecimento",
  acao="Esclarecer no Q&A",
  pergunta="Os 6.200 'usuários ativos' incluem terceiros, contas de serviço e contas privilegiadas? Qual a quantidade por tipo?",
  responsavel="Pré-venda/Arquitetura")
I("d03_servidores", "D03", "Números do ambiente", SL2, '"850 servidores (70% Windows, 30% Linux)"',
  "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Principal volumetria disponível para estimar fontes de log; não há quantidade de ativos de rede, estações nem aplicações.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Base para estimar EPS e conectores na falta de volumetria", **NA,
  relacionados=["d04_q3"], acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d03_dcs", "D03", "Números do ambiente", SL2, '"2 data centers próprios (São Paulo e Campinas)"',
  "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Duas localidades físicas para coletores de log; eventual atuação presencial na resposta a incidentes (Anexo I, 1.5) pode exigir deslocamento.",
  obrigatoriedade="Informativo", s=2, p=3, impacto="Coletores e links em dois sites", **NA, acao="Precificar",
  responsavel="Pré-venda/Arquitetura")
I("d03_nuvens", "D03", "Números do ambiente", SL2, '"Workloads em 2 nuvens públicas"', "Dado de dimensionamento",
  "Infraestrutura/Cloud", "Provedores e volume de workloads não informados; conectores e custo de ingestão variam por provedor.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Integrações de nuvem não dimensionáveis", **NA,
  relacionados=["d02_integracao"], acao="Esclarecer no Q&A",
  pergunta="Quais são os dois provedores de nuvem pública e quais contas e serviços devem ser integrados ao SIEM?",
  responsavel="Pré-venda/Arquitetura")
I("d03_siem_legado", "D03", "Ferramentas atuais", SL3,
  '"SIEM legado — contrato encerra em 31/01/2027, sem possibilidade de prorrogação"', "Premissa do cliente",
  "Transição/Implantação",
  "Data-limite rígida para a substituição do SIEM legado; o serviço novo começa em 01/02/2027. Não há margem para atraso.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Corte obrigatório em data fixa, independentemente da assinatura", **NA,
  relacionados=["d01_inicio", "d03_risco_transicao"], acao="Registrar premissa na proposta",
  responsavel="Delivery/Operação")
I("d03_risco_transicao", "D03", "Ferramentas atuais × RFP 3.1, 3.2, 7.4 × Anexo I § 4",
  f"{SL3} · D01 {P2}, itens 3.1 e 3.2 · D01 {P5}, item 7.4 · D02 {S4}",
  '"contrato encerra em 31/01/2027, sem possibilidade de prorrogação" · "Início previsto dos serviços 01/02/2027" · "concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato" · "multa de 10% (dez por cento) do valor mensal do contrato, por ocorrência"',
  "Risco para o proponente", "Transição/Implantação",
  "Risco combinado: (a) SIEM legado termina em 31/01/2027 sem prorrogação; (b) serviço novo começa em 01/02/2027; (c) transição de 30 ou 60 dias contada da assinatura, cuja data não é informada; (d) operação paralela sem custo; (e) documentação do ambiente só no 10º dia; (f) migração esperada de 24 meses de logs (slide 5); (g) multas de 10% por ocorrência sem teto. "
  "Qualquer atraso na assinatura ou na transição deixa o Banco sem SIEM ou leva a multas sem limite. Severidade 5 pela exposição sem teto. Probabilidade 4: o slide 3 afirma que o contrato do SIEM legado não pode ser prorrogado, e o Q&A nº 1 adiou a entrega das propostas para 27/11/2026 sem mudar o início dos serviços, o que comprime o prazo entre seleção, assinatura e transição.",
  obrigatoriedade="Informativo", natureza="Inferida", s=5, p=4,
  impacto="Multas sem teto desde o início da operação e risco de entrada em produção incompleta",
  framework=I20000, controle="Planejamento e transição de serviços (identificador a confirmar)", associacao="Correlata",
  relacionados=["d01_inicio", "d01_transicao", "d02_transicao", "d02_paralelo", "d02_doc", "d03_siem_legado",
                "d03_migracao", "d01_multa", "d04_q1"],
  acao="Mitigar",
  pergunta="Diante do fim do contrato do SIEM legado em 31/01/2027 sem prorrogação, o Banco aceita carência de SLAs e multas durante a transição e no primeiro mês de operação? Qual a data-limite de assinatura do contrato considerada pelo Banco?",
  responsavel="Delivery/Operação")
I("d03_iam_atual", "D03", "Ferramentas atuais", SL3, '"IAM: Active Directory + scripts internos"',
  "Dado de dimensionamento", "Técnico/Arquitetura",
  "Sem ferramenta de governança de identidades; automatizar ciclo de vida e recertificação (Anexo I, 3.1 a 3.3) exigirá ferramenta ou desenvolvimento, cujo fornecimento não está definido.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Esforço de implantação de IAM maior que o de mera operação", **NA,
  relacionados=["d02_iam_ferramenta"], acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d03_pam", "D03", "Ferramentas atuais", SL3, '"Não há solução de PAM"', "Oportunidade / diferencial",
  "Segurança da Informação/Cyber",
  "PAM é desejável (Anexo I, 3.4) e inexistente hoje: ofertá-lo pode diferenciar em 'Ferramentas e tecnologia' (15 pontos) e apoiar o MFA obrigatório para privilegiados (3.2).",
  obrigatoriedade="Informativo", framework=ISO, controle="A.8.2 Direitos de acesso privilegiado", associacao="Correlata",
  relacionados=["d02_pam", "d01_crit_ferr"], acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d03_alertas", "D03", "Desafios", SL4, '"Cerca de 1.200 alertas por dia"', "Dado de dimensionamento",
  "Operação/Serviços",
  "Cerca de 36.000 alertas por mês com o SIEM atual: principal base disponível para dimensionar analistas N1. Não substitui a volumetria de EPS.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Dimensionamento da equipe de triagem", **NA,
  relacionados=["d04_q3"], acao="Precificar", responsavel="Delivery/Operação")
I("d03_meta_fp", "D03", "Desafios", SL4,
  '"70% de falsos positivos" · "Meta: reduzir os falsos positivos para 10% no primeiro trimestre de operação"',
  "Ambiguidade", "Operação/Serviços",
  "Meta agressiva (de 70% para 10% em 3 meses) apresentada só no workshop; não consta dos SLAs do Anexo I. Se for incorporada como SLA, fica sujeita à multa de 10% por ocorrência (7.4). Não define como se mede falso positivo.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Possível SLA adicional de difícil cumprimento e esforço intenso de ajuste fino",
  framework=CSF, controle="DE.AE — Análise de eventos adversos", associacao="Correlata",
  relacionados=["d01_multa"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="A meta de reduzir falsos positivos para 10% no primeiro trimestre é obrigação contratual (SLA sujeito ao item 7.4) ou apenas expectativa? Como a taxa de falsos positivos será medida?",
  responsavel="Delivery/Operação")
I("d03_migracao", "D03", "Expectativas para o novo serviço", SL5,
  '"Migração de 24 meses de logs históricos do SIEM legado para a nova plataforma"', "Ambiguidade",
  "Transição/Implantação / Dados/Analytics",
  "Escopo não previsto na RFP nem no Anexo I. Volume não informado; o formato de exportação depende do fornecedor legado, cujo contrato termina em 31/01/2027. Os 24 meses excedem a retenção de 12 meses do Anexo I (1.3).",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Esforço e armazenamento adicionais não precificados; dependência do fornecedor legado",
  framework=ISO, controle="A.8.15 Registros (logging)", associacao="Correlata",
  relacionados=["d02_contr_logs", "d03_siem_legado", "d03_risco_transicao"], vigencia="Em esclarecimento",
  acao="Esclarecer no Q&A",
  pergunta="A migração de 24 meses de logs históricos faz parte do escopo contratual? Qual o volume (TB) e o formato de exportação? O fornecedor atual é obrigado a entregar os dados?",
  responsavel="Pré-venda/Arquitetura")
I("d03_visao_riscos", "D03", "Expectativas para o novo serviço", SL5, '"Visão unificada de riscos para a diretoria"',
  "Ambiguidade", "Dados/Analytics",
  "Expectativa sem entregável definido (painel executivo, relatório, ferramenta de GRC); não consta do Anexo I.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Escopo adicional de relatórios ou ferramenta não dimensionado",
  framework="ISO 31000", controle="Comunicação e reporte de riscos (identificador a confirmar)", associacao="Correlata",
  vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="A 'visão unificada de riscos para a diretoria' é escopo contratual? Que formato, periodicidade e fontes de dados são esperados?",
  responsavel="Pré-venda/Arquitetura")
I("d03_subsidiarias", "D03", "Expectativas para o novo serviço — notas do apresentador", "slide 5 — notas do apresentador",
  '"as subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários adicionais) também deverão ser incluídas no escopo"',
  "Ambiguidade", "Técnico/Arquitetura / Jurídico/Contratual",
  "Ampliação de escopo escrita só nas notas do apresentador (não exibidas nos slides); não consta da RFP (objeto: Banco, ~4.500 colaboradores) nem do Anexo I. Inclui ~900 usuários e duas pessoas jurídicas distintas, o que afeta dimensionamento, quem contrata e paga, e a declaração de localização de dados. Classificada como Ambiguidade porque a validade contratual de uma nota de apresentação é incerta.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Escopo cerca de 20% maior não precificado; partes contratuais indefinidas",
  **NA, relacionados=["d01_usuarios", "d03_contr_usuarios", "d04_q5"], vigencia="Em esclarecimento",
  acao="Esclarecer no Q&A",
  pergunta="As subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários) fazem parte do escopo? Em caso positivo, serão partes contratantes e o escopo inclui SOC e IAM para elas?",
  responsavel="Bid Manager")

# =============================================================== D04 — Q&A e Questionário
QA = 'aba "Q&A Rodada 1"'
QT = 'aba "Questionário Técnico"'
PS = 'aba "Pesos" (OCULTA)'
I("d04_inv", "D04", "Planilha inteira (4 abas)", 'abas "Instruções", "Q&A Rodada 1", "Questionário Técnico" e "Pesos" (oculta)',
  '"Questionário Técnico e Respostas aos Esclarecimentos — RFP nº 2026-017"', "Registro de cobertura",
  "Administrativo do processo",
  "Inventário D04: 4 abas; a aba 'Pesos' está oculta e foi analisada (contém pesos e regra de dedução não divulgados na RFP). Sem outras linhas ou colunas ocultas sinalizadas. Q&A Rodada 1 com 6 perguntas de 12/11/2026; Questionário com 6 requisitos (QT-01 a QT-06).",
  responsavel="Bid Manager")
I("d04_instr", "D04", "Instruções", 'aba "Instruções" · A3',
  '"O preenchimento de todas as abas deste arquivo é obrigatório. Questionários incompletos serão desclassificados."',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Probabilidade 5: o texto determina desclassificação direta de questionário incompleto. Agrava o item 4.4 da RFP, que não previa sanção.",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Desclassificação", **NA,
  relacionados=["d01_questionario", "d04_instr_amb"], acao="Atender", responsavel="Bid Manager")
I("d04_instr_amb", "D04", "Instruções", 'aba "Instruções" · A3',
  '"O preenchimento de todas as abas deste arquivo é obrigatório."', "Ambiguidade", "Administrativo do processo",
  "'Todas as abas' inclui a aba 'Q&A Rodada 1', já preenchida pelo cliente, e a aba oculta 'Pesos', sem campo de resposta. Também não está claro se a coluna 'Comentários' é obrigatória. Interpretação errada leva à desclassificação.",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Risco de desclassificação por preenchimento considerado incompleto", **NA,
  relacionados=["d04_instr"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="A obrigação de preencher 'todas as abas' se refere apenas à aba 'Questionário Técnico' (colunas D e E)? A coluna 'Comentários' é obrigatória?",
  responsavel="Bid Manager")
I("d04_q1", "D04", "Q&A Rodada 1 — pergunta nº 1 (RFP, item 3.1)", f"{QA} · E2 (Q&A nº 1, 12/11/2026)",
  '"A data de entrega das propostas fica prorrogada para 27/11/2026, até as 18h."', "Prazo / marco",
  "Administrativo do processo",
  "Altera a data de 20/11/2026 do cronograma (RFP 3.1). As demais datas, inclusive o início dos serviços em 01/02/2027, não mudaram. Probabilidade 2: prazo explícito, com uma semana adicional.",
  obrigatoriedade="Mandatório", s=5, p=2, impacto="Proposta fora do prazo não é recebida", **NA,
  relacionados=["d01_entrega", "d03_risco_transicao"], acao="Atender", responsavel="Bid Manager")
I("d04_q2", "D04", "Q&A Rodada 1 — pergunta nº 2 (RFP, item 5.1 c)", f"{QA} · E3 (Q&A nº 2, 12/11/2026)",
  '"Não. O SOC deverá estar localizado em território nacional."', "Restrição", "Regulatório/Compliance",
  "Confirma o critério 5.1 c) e veda operar o SOC a partir do exterior. Não esclarece se N2/N3, especialistas de resposta a incidentes ou serviços de inteligência de ameaças podem atuar do exterior.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Exclui modelos de entrega offshore em todos os níveis, se interpretado amplamente",
  framework=RES, controle="Contratação de serviços prestados no exterior (identificador a confirmar)", associacao="Correlata",
  relacionados=["d01_soc_br"], acao="Esclarecer no Q&A",
  pergunta="A restrição de território nacional vale para todos os níveis de atendimento (N2, N3, especialistas) e para serviços de apoio prestados remotamente, como inteligência de ameaças?",
  responsavel="Compliance")
I("d04_q3", "D04", "Q&A Rodada 1 — pergunta nº 3 (Anexo I, item 1.4)", f"{QA} · D4:E4 (Q&A nº 3, 12/11/2026)",
  '"Qual a volumetria de eventos por segundo (EPS) a considerar?" · "A volumetria será informada somente ao proponente vencedor."',
  "Lacuna", "Técnico/Arquitetura / Comercial/Preço",
  "Probabilidade 5: o cliente recusou formalmente informar a volumetria (EPS), indispensável para dimensionar licenças, armazenamento (12 meses ou 5 anos) e infraestrutura do SIEM, que é fornecido pelo proponente (Anexo I, 1.2). O preço terá de se apoiar em premissa (por exemplo, derivada dos 850 servidores e 1.200 alertas por dia).",
  obrigatoriedade="Informativo", s=4, p=5, impacto="SIEM precificado sem base; risco de subdimensionamento ou de preço não competitivo",
  **NA, relacionados=["d02_siem", "d02_integracao", "d02_contr_logs", "d03_servidores", "d03_alertas"],
  acao="Registrar premissa na proposta",
  pergunta="Na falta do EPS, o Banco aceita que a proposta adote volumetria de referência como premissa, com revisão de preço se a volumetria real exceder essa referência em percentual definido?",
  responsavel="Pricing/Financeiro")
I("d04_q4", "D04", "Q&A Rodada 1 — pergunta nº 4 (RFP, item 7.4)", f"{QA} · D5:E5 (Q&A nº 4, 12/11/2026)",
  '"As multas possuem limite máximo?" · "As condições do item 7 permanecem inalteradas."',
  "Risco para o proponente", "Jurídico/Contratual / Financeiro",
  "Risco combinado de exposição contratual: o cliente recusou limitar as multas e manteve todo o item 7, inclusive multa de 10% do valor mensal por ocorrência (7.4), responsabilidade integral e ilimitada (7.5) e seguro 'compatível' sem valor (7.6). A exposição financeira não tem limite, o que pede decisão de Go/No-Go e ressalvas formais. Probabilidade 4: o cliente já recusou, nesta rodada, o pedido de esclarecimento sobre teto de multas.",
  obrigatoriedade="Informativo", natureza="Inferida", s=5, p=4,
  impacto="Exposição financeira e jurídica ilimitada; pode inviabilizar seguro e aprovação interna da proposta",
  framework=CC, controle="Cláusula penal — arts. 412 e 413", associacao="Correlata",
  relacionados=["d01_multa", "d01_resp_ilimitada", "d01_seguro", "d02_sla15"], acao="Avaliar Go/No-Go",
  responsavel="Jurídico")
I("d04_q5", "D04", "Q&A Rodada 1 — pergunta nº 5 (RFP, item 2.1)",
  f"{QA} · E6 (Q&A nº 5, 12/11/2026) · D03 {SL2} · slide 5 — notas do apresentador",
  'A: D04 "Considerar 5.000 usuários." · B: D03 "6.200 usuários ativos" · "cerca de 900 usuários adicionais"',
  "Contradição", "Técnico/Arquitetura / Comercial/Preço",
  "O Q&A fixa 5.000 usuários para dimensionamento, alterando os 4.500 colaboradores da RFP (2.1), mas fica abaixo dos 6.200 usuários ativos do workshop e dos ~7.100 com as subsidiárias (diferença de 42%). Sem precedência entre documentos, não se sabe se o excedente será cobrado à parte ou absorvido.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Subdimensionamento de licenças e esforço de IAM, ou preço não competitivo",
  **NA, relacionados=["d01_usuarios", "d03_contr_usuarios", "d03_subsidiarias", "d01_precedencia"],
  vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="O Q&A nº 5 indica 5.000 usuários, mas a apresentação de 22/10/2026 informa 6.200 usuários ativos e mais cerca de 900 das subsidiárias. Qual quantidade será contratada e como serão remunerados os usuários acima de 5.000?",
  responsavel="Pricing/Financeiro")
I("d04_q6", "D04", "Q&A Rodada 1 — pergunta nº 6 (Anexo I, item 5.2)", f"{QA} · D7:E7 (Q&A nº 6, 12/11/2026)",
  '"Os analistas de nível 1 podem atuar remotamente?" · "Sim, desde que em território nacional."', "Restrição",
  "Pessoas/Equipe",
  "Altera o Anexo I, 5.2: analistas N1 podem atuar remotamente, desde que no Brasil. Reduz custo de alocação na sede. A alteração depende de confirmar que o Q&A prevalece sobre o Anexo I (não há cláusula de precedência).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Permite modelo remoto para N1, com redução de custo", **NA,
  relacionados=["d02_n1", "d01_precedencia"], acao="Registrar premissa na proposta", responsavel="RH/Staffing")
I("d04_rodada", "D04", "Q&A Rodada 1 × RFP 3.1", f"{QA} · A1:E7 · D01 {P2}, item 3.1",
  'Não localizado · "Prazo final para envio de perguntas 05/11/2026"', "Lacuna", "Administrativo do processo",
  "O cronograma prevê uma única data para perguntas (05/11/2026), anterior às respostas (12/11/2026), e não há previsão de segunda rodada, embora a aba se chame 'Rodada 1'. As questões desta matriz (prazo de transição, usuários, retenção, região de nuvem, nota técnica) podem ficar sem resposta antes da entrega de 27/11/2026 e terão de virar premissas ou ressalvas.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Contradições não resolvidas antes da entrega; proposta com muitas premissas",
  **NA, relacionados=["d01_perguntas", "d04_q1"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Haverá segunda rodada de esclarecimentos antes da entrega de 27/11/2026? Em caso positivo, qual o prazo para envio das perguntas?",
  responsavel="Bid Manager")
for k, row, req, obr, peso, tipo_ob, desc, fw, ctl, assoc, rel, vig, acao, perg, resp in [
    ("d04_qt01", 2, "Possui certificação ISO/IEC 27001 com escopo que inclua os serviços de SOC?", "Sim", 3, "Mandatório",
     "Repete o critério de habilitação 5.1 a) da RFP.", ISO_SGSI, "Certificação do SGSI (requisitos das cláusulas 4 a 10)",
     "Direta", ["d01_iso"], "Duplicado", "Atender", "—", "Compliance"),
    ("d04_qt02", 3, "Oferece integração nativa com plataforma SOAR?", "Não", 1, "Desejável",
     "Requisito não previsto no Anexo I. Pela regra da aba oculta, responder 'Não atende' tira 2 pontos da Nota Técnica.",
     CSF, "Função Responder (RS) — automação da resposta (identificador a confirmar)", "Correlata",
     ["d04_pesos_regra"], "Vigente", "Precificar", "—", "Pré-venda/Arquitetura"),
    ("d04_qt03", 4, "Retém os logs online por no mínimo 12 meses?", "Sim", 2, "Mandatório",
     "Acrescenta 'online' ao requisito de 12 meses do Anexo I (1.3) e reforça a leitura de 12 meses online + 5 anos em arquivo, ainda não confirmada.",
     ISO, "A.8.15 Registros (logging)", "Direta", ["d02_ret12", "d02_contr_logs"], "Vigente", "Atender", "—",
     "Pré-venda/Arquitetura"),
    ("d04_qt04", 5, "Atende aos requisitos da Resolução CMN nº 4.893/2021?", "Sim", 3, "Mandatório",
     "Pergunta ampla: a resolução se dirige à instituição financeira e não há lista dos requisitos que o fornecedor deve atender. Responder 'Atende' sem delimitação cria compromisso aberto.",
     RES, "Requisitos para contratação de processamento, armazenamento de dados e computação em nuvem (identificador a confirmar)",
     "Direta", ["d01_res4893"], "Vigente", "Esclarecer no Q&A",
     "Quais requisitos específicos da Resolução CMN nº 4.893/2021 o QT-04 considera para a resposta do fornecedor?",
     "Compliance"),
    ("d04_qt05", 6, "Oferece serviço de threat intelligence?", "Não", 2, "Desejável",
     "Serviço não previsto no Anexo I; 'Não atende' tira 2 pontos (regra oculta). Se prestado por terceiro, pode esbarrar na vedação de subcontratação (7.7) e no processamento exclusivo no Brasil (Anexo III).",
     ISO, "A.5.7 Inteligência de ameaças", "Direta", ["d04_pesos_regra", "d01_subcontratacao"], "Vigente",
     "Precificar", "—", "Segurança/Cyber"),
    ("d04_qt06", 7, "Possui equipe com certificações reconhecidas pelo mercado?", "Sim", 2, "Mandatório",
     "Vago como o item 5.2 da RFP: não diz quais certificações nem para quais perfis.", ISO_SGSI,
     "Cláusula 7.2 Competência", "Correlata", ["d01_equipe_cert"], "Vigente", "Atender", "—", "RH/Staffing"),
]:
    I(k, "D04", f"Questionário Técnico — {k[4:].upper().replace('QT', 'QT-')}",
      f"{QT} · linha {row} (A{row}:C{row}) · {PS} · B{row}",
      f'"{req}" · Obrigatório: "{obr}" · Peso (aba oculta): {peso}', "Critério de avaliação / pontuação",
      "Administrativo do processo", f"Item do questionário com peso {peso} na aba oculta 'Pesos'. {desc}",
      obrigatoriedade=tipo_ob, s=3, p=3, impacto="Contribui para a Nota Técnica conforme pesos não divulgados na RFP",
      framework=fw, controle=ctl, associacao=assoc, relacionados=rel, vigencia=vig, acao=acao, pergunta=perg,
      responsavel=resp)
I("d04_pesos_regra", "D04", "Pesos (aba oculta)", f"{PS} · A9",
  '"Requisitos não obrigatórios respondidos como \'Não atende\' reduzem a Nota Técnica em 2 (dois) pontos cada."',
  "Critério de avaliação / pontuação", "Administrativo do processo",
  "Regra de pontuação que só existe em aba oculta. Penaliza não atender requisitos não obrigatórios (QT-02 SOAR e QT-05 threat intelligence): até 4 pontos a menos, relevantes para o corte de 70% (RFP 6.3). Os pesos de B2:B7 (3, 1, 2, 3, 2, 2) não têm uso definido.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Perda de até 4 pontos técnicos; aumenta o risco no corte eliminatório",
  **NA, relacionados=["d01_corte", "d04_qt02", "d04_qt05", "d04_contr_nota"], vigencia="Em esclarecimento",
  acao="Esclarecer no Q&A",
  pergunta="A aba oculta 'Pesos' do questionário vale para a avaliação? Como os pesos de QT-01 a QT-06 entram na Nota Técnica e a dedução de 2 pontos por requisito não obrigatório 'Não atende' se aplica?",
  responsavel="Bid Manager")
I("d04_contr_nota", "D04", "Pesos (aba oculta) × RFP 6.2", f"{PS} · A9 · D01 {P4}, item 6.2",
  'A: D01 "A Nota Técnica, de no máximo 60 (sessenta) pontos, será atribuída conforme os critérios abaixo" · B: D04 "reduzem a Nota Técnica em 2 (dois) pontos cada"',
  "Contradição", "Administrativo do processo",
  "A RFP diz que a Nota Técnica resulta só dos quatro critérios do 6.2; a aba oculta cria uma dedução não prevista ali. O questionário com pesos também não aparece como critério no 6.2.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Regra de avaliação divergente entre documentos; risco no corte técnico",
  **NA, relacionados=["d01_contr_nota", "d01_lac_criterios", "d04_pesos_regra"], vigencia="Em esclarecimento",
  acao="Esclarecer no Q&A", responsavel="Bid Manager")
I("d04_oport_pesos", "D04", "Pesos (aba oculta)", f"{PS} · A2:B7",
  'Aba oculta "Pesos": QT-01 = 3 · QT-02 = 1 · QT-03 = 2 · QT-04 = 3 · QT-05 = 2 · QT-06 = 2',
  "Oportunidade / diferencial", "Administrativo do processo",
  "Os pesos ocultos mostram as prioridades do cliente: certificação ISO/IEC 27001 e aderência à Res. CMN 4.893/2021 (peso 3). Ofertar SOAR e threat intelligence evita a dedução de 2 pontos cada e reforça 'Ferramentas e tecnologia'.",
  obrigatoriedade="Informativo", relacionados=["d04_pesos_regra", "d04_qt02", "d04_qt05"], acao="Precificar",
  responsavel="Bid Manager")

# ---------------------------------------------------------------- saída
DOCS = [
    {"codigo": "D01", "arquivo": "RFP-2026-017_Servicos_SOC_IAM.pdf", "tipo": "RFP", "versao": "v1.0 — 15/10/2026"},
    {"codigo": "D02", "arquivo": "Anexo_I_Especificacao_Tecnica.docx", "tipo": "Anexo técnico", "versao": "v1.0 — 15/10/2026"},
    {"codigo": "D03", "arquivo": "Apresentacao_Ambiente_Atual.pptx", "tipo": "Apresentação (workshop)", "versao": "22/10/2026"},
    {"codigo": "D04", "arquivo": "QA_Rodada1_e_Questionario.xlsx", "tipo": "Q&A e questionário", "versao": "12/11/2026 (Q&A Rodada 1)"},
]
NEXT = {1: "Anexo_I_Especificacao_Tecnica.docx (D02), a partir do § 1", 2: "Apresentacao_Ambiente_Atual.pptx (D03), a partir do slide 1",
        3: "QA_Rodada1_e_Questionario.xlsx (D04), a partir da aba \"Instruções\""}

if __name__ == "__main__":
    out, n = sys.argv[1], int(sys.argv[2])
    codes = [d["codigo"] for d in DOCS[:n]]
    docs = [dict(d, situacao="processado") for d in DOCS[:n]]
    sel = [it for it in itens if it["doc"] in codes]
    # relacionados que apontam para documentos ainda não processados são omitidos nas rodadas parciais
    keys = {it["chave"] for it in sel}
    if n < 4:
        sel = [dict(it, relacionados=[r for r in it.get("relacionados", []) if r in keys]) for it in sel]
    status = {"final": True} if n == 4 else {"final": False, "parte": n, "concluidos": n, "proximo": NEXT[n]}
    data = {"processo": "RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Serviços gerenciados de SOC e IAM",
            "documentos": docs if n == 4 else docs + [dict(d, situacao="pendente") for d in DOCS[n:]],
            "itens": sel, "status": status}
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f"{len(sel)} itens · documentos {codes}")
