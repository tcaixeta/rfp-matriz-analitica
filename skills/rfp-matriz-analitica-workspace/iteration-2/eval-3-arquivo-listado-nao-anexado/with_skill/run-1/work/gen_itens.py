# Gera itens.json para a matriz da RFP 2026-017. Uso: python gen_itens.py <ultimo_doc> <saida.json>
import json
import sys

DOCS = [
    {"codigo": "D01", "arquivo": "RFP-2026-017_Servicos_SOC_IAM.pdf", "tipo": "RFP", "versao": "v1.0 — 15/10/2026", "situacao": "processado"},
    {"codigo": "D02", "arquivo": "Anexo_I_Especificacao_Tecnica.docx", "tipo": "Anexo técnico", "versao": "v1.0 — 15/10/2026", "situacao": "processado"},
    {"codigo": "D03", "arquivo": "Anexo_IV_Planilha_de_Precos.xlsx", "tipo": "Planilha de preços", "versao": "v1.0", "situacao": "não anexado"},
    {"codigo": "D04", "arquivo": "Apresentacao_Ambiente_Atual.pptx", "tipo": "Apresentação", "versao": "22/10/2026", "situacao": "processado"},
    {"codigo": "D05", "arquivo": "QA_Rodada1_e_Questionario.xlsx", "tipo": "Q&A e questionário", "versao": "12/11/2026", "situacao": "processado"},
]
PROXIMO = {
    "D01": "Anexo_I_Especificacao_Tecnica.docx (D02), a partir de § Anexo I — Especificação Técnica",
    "D02": "Anexo_IV_Planilha_de_Precos.xlsx (D03), registro de cobertura",
    "D03": "Apresentacao_Ambiente_Atual.pptx (D04), a partir do slide 1",
    "D04": "QA_Rodada1_e_Questionario.xlsx (D05), a partir da aba \"Instruções\"",
}

ITENS = []


def I(chave, doc, secao, loc, ev, tipo, dom, desc, **kw):
    it = {"chave": chave, "doc": doc, "secao": secao, "localizador": loc, "evidencia": ev, "tipo": tipo,
          "dominio": dom, "descricao": desc}
    it.update(kw)
    ITENS.append(it)


ISO = "ISO/IEC 27001:2022"
CSF = "NIST CSF 2.0"
ITIL = "ITIL 4"
LGPD = "LGPD (Lei 13.709/2018)"
CMN = "Resolução CMN nº 4.893/2021 (citada no documento)"
CC = "Código Civil (Lei 10.406/2002)"
APMP = "APMP Body of Knowledge"
P2 = "p. 2 (impressa: 1)"
P3 = "p. 3 (impressa: 2)"
P4 = "p. 4 (impressa: 3)"
P5 = "p. 5 (impressa: 4)"
P6 = "p. 6 (impressa: 5) (OCR)"

# =============================================================== D01 — RFP
I("d01_inv", "D01", "Documento inteiro (capa, seções 1 a 7 e Anexo III)", "p. 1–6",
  '"Solicitação de Proposta (RFP) nº 2026-017"', "Registro de cobertura", "Administrativo do processo",
  "Inventário: PDF com 6 páginas físicas; numeração impressa começa na p. 2 (impressa: 1). Texto extraível nas p. 1–5. "
  "A p. 6 (impressa: 5) só tem cabeçalho/rodapé em texto e uma imagem digitalizada: foi lida visualmente (OCR) e contém o "
  "Anexo III — Declaração de localização de dados, analisado nos itens com localizador '(OCR)'. Cabeçalho/rodapé repetido "
  "desconsiderado. O documento cita o Anexo I (fornecido, D02) e o Anexo IV (listado pelo usuário e não anexado, D03).",
  responsavel="Bid Manager")

I("d01_regime", "D01", "1. APRESENTAÇÃO — 1.2", P2,
  '"O Banco é instituição financeira autorizada a funcionar pelo Banco Central do Brasil e está sujeito à Resolução CMN nº 4.893/2021"',
  "Registro de cobertura", "Regulatório/Compliance",
  "Regime identificado: contratação privada (contratante é sociedade anônima, processo por RFP; não há menção a licitação, "
  "edital ou Lei 14.133/2021) em setor regulado (instituição financeira supervisionada pelo Banco Central, sujeita à Res. CMN "
  "nº 4.893/2021). Legislação associada nesta matriz: Código Civil (contrato privado), LGPD e Res. CMN nº 4.893/2021.",
  responsavel="Compliance")

I("d01_precedencia", "D01", "Documento inteiro — ordem de precedência", "p. 1–6",
  'Não localizado · "As especificações técnicas detalhadas constam do Anexo I — Especificação Técnica."',
  "Lacuna", "Jurídico/Contratual / Administrativo do processo",
  "Não há cláusula de ordem de precedência entre a RFP, seus anexos (I, III, IV), o questionário, as respostas do Q&A e o "
  "material do workshop. Há divergências que dependem disso: transição de 30 × 60 dias ({d02_transicao_contra}), SIEM em "
  "nuvem de região livre × dados exclusivamente no país ({d02_nuvem_contra}), quantidade de usuários ({d04_usuarios_contra}, "
  "{d05_usuarios_contra}) e escopo citado só no workshop ({d04_escopo_amb}). Não se presume que o Q&A, por ser mais recente, prevaleça.",
  obrigatoriedade="Informativo", s=4, p=3,
  impacto="Sem regra de precedência, o proponente pode precificar e dimensionar com base no documento que não prevalecerá; risco de proposta inexequível ou desconforme.",
  framework=APMP, controle="Gestão de documentos e esclarecimentos da concorrência (identificador a confirmar)", associacao="Boa prática",
  relacionados=["d02_transicao_contra", "d02_nuvem_contra", "d04_usuarios_contra", "d04_escopo_amb"],
  acao="Esclarecer no Q&A",
  pergunta="Qual a ordem de precedência entre a RFP, os Anexos I, III e IV, o questionário técnico, as respostas aos esclarecimentos e o material do workshop? As respostas do Q&A e o conteúdo do workshop (inclusive notas do apresentador) têm caráter vinculante?",
  responsavel="Jurídico")

I("d01_objeto_soc", "D01", "2. OBJETO — 2.1", P2,
  '"prestação de serviços gerenciados de Centro de Operações de Segurança (SOC), em regime 24x7x365"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber / Operação/Serviços",
  "Objeto: SOC gerenciado em regime contínuo 24x7x365, o que exige escala de turnos com cobertura integral durante 36 meses.",
  obrigatoriedade="Mandatório", s=3, p=3,
  impacto="Define a base de custo de pessoal (escala 24x7) e de plataforma.",
  framework=CSF, controle="DE.CM — Monitoramento contínuo", associacao="Correlata",
  relacionados=["d02_monit"], acao="Precificar", responsavel="Delivery/Operação")

I("d01_objeto_iam", "D01", "2. OBJETO — 2.1", P2,
  '"e de gestão de identidades e acessos (IAM)"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Objeto inclui serviço gerenciado de IAM. A RFP não diz se o proponente fornece a plataforma de IAM/IGA ou só opera a do Banco (veja {d02_iam_lacuna}).",
  obrigatoriedade="Mandatório", s=3, p=3,
  impacto="Escopo de serviço e eventual licenciamento de ferramenta de IAM.",
  framework=ISO, controle="A.5.16 Gestão de identidades", associacao="Correlata",
  relacionados=["d02_iam_lacuna"], acao="Precificar", responsavel="Pré-venda/Arquitetura")

I("d01_usuarios", "D01", "2. OBJETO — 2.1", P2,
  '"abrangendo aproximadamente 4.500 colaboradores"',
  "Dado de dimensionamento", "Operação/Serviços",
  "Base de dimensionamento original: cerca de 4.500 colaboradores. Alterada pela resposta 5 do Q&A ({d05_qa5}: 5.000 usuários) e divergente "
  "da apresentação do ambiente (6.200 usuários ativos + cerca de 900 das subsidiárias). Não fica claro se o número se aplica só ao IAM ou também ao SOC.",
  obrigatoriedade="Informativo", s=4, p=3,
  impacto="Usuários são o principal direcionador de preço do IAM; a diferença entre 4.500 e cerca de 7.100 usuários é superior a 50%.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d05_qa5", "d04_usuarios_contra", "d05_usuarios_contra"], vigencia="Alterado",
  acao="Esclarecer no Q&A", responsavel="Pricing/Financeiro")

I("d01_workshop", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2,
  '"Workshop de apresentação do ambiente 22/10/2026"', "Prazo / marco", "Administrativo do processo",
  "Workshop de apresentação do ambiente. Foi nele que surgiram informações de escopo ausentes da RFP (subsidiárias, migração de logs), registradas no D04.",
  obrigatoriedade="Informativo", s=2, p=3,
  impacto="Ausência no workshop priva o proponente de informações de escopo divulgadas só nele.",
  framework=APMP, controle="Captura de informações do cliente (identificador a confirmar)", associacao="Boa prática",
  relacionados=["d04_escopo_amb"], acao="Atender", responsavel="Bid Manager")

I("d01_perguntas", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2,
  '"Prazo final para envio de perguntas 05/11/2026"', "Prazo / marco", "Administrativo do processo",
  "Prazo único para perguntas; o cronograma não prevê segunda rodada (veja {d05_rodada2}). As perguntas desta matriz precisam ser enviadas até essa data.",
  obrigatoriedade="Mandatório", s=3, p=3,
  impacto="Perguntas não enviadas no prazo deixam ambiguidades e lacunas sem resposta, a serem cobertas por premissas.",
  framework=APMP, controle="Gestão de esclarecimentos (identificador a confirmar)", associacao="Boa prática",
  relacionados=["d05_rodada2"], acao="Atender", responsavel="Bid Manager")

I("d01_respostas", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2,
  '"Divulgação das respostas 12/11/2026"', "Prazo / marco", "Administrativo do processo",
  "Data de divulgação das respostas; o Q&A Rodada 1 (D05) traz essa data.",
  obrigatoriedade="Informativo", s=1, p=3, impacto="Define o tempo entre as respostas e a entrega da proposta.",
  framework="—", controle="—", associacao="Não aplicável", relacionados=["d05_qa1"], responsavel="Bid Manager")

I("d01_entrega", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2,
  '"Entrega das propostas 20/11/2026, até as 18h"', "Prazo / marco", "Administrativo do processo",
  "Prazo original de entrega, prorrogado para 27/11/2026, até as 18h, pela resposta 1 do Q&A ({d05_qa1}). A RFP não informa o fuso horário de referência.",
  obrigatoriedade="Mandatório", s=5, p=3,
  impacto="Proposta entregue fora do prazo tende a não ser considerada.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d05_qa1"], vigencia="Alterado", acao="Atender", responsavel="Bid Manager")

I("d01_inicio", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1", P2,
  '"Início previsto dos serviços 01/02/2027"', "Prazo / marco", "Transição/Implantação",
  "Início previsto dos serviços em 01/02/2027, um dia após o fim do contrato do SIEM legado ({d04_siem_legado}). Não está claro se 'início' é o começo da transição ou da operação plena.",
  obrigatoriedade="Mandatório", s=4, p=3,
  impacto="Condiciona o cronograma de transição e o risco de lacuna de monitoramento.",
  framework=ITIL, controle="Prática de gerenciamento de implantação (identificador a confirmar)", associacao="Correlata",
  relacionados=["d04_siem_legado", "d04_risco_transicao"], acao="Esclarecer no Q&A",
  pergunta="A data de 01/02/2027 corresponde ao início da transição ou ao início da operação plena (após a transição)?",
  responsavel="Delivery/Operação")

I("d01_transicao30", "D01", "3. CRONOGRAMA DO PROCESSO — 3.2", P2,
  '"A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato."',
  "Prazo / marco", "Transição/Implantação",
  "Transição em até 30 dias corridos da assinatura. Conflita com os 60 dias do Anexo I, item 4.1 ({d02_transicao_contra}).",
  obrigatoriedade="Mandatório", s=4, p=3,
  impacto="Prazo curto exige equipe de transição dimensionada e pode inviabilizar integrações e migração de logs.",
  framework=ITIL, controle="Prática de gerenciamento de mudanças / transição (identificador a confirmar)", associacao="Correlata",
  relacionados=["d02_transicao60", "d02_transicao_contra"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="O prazo de transição é de 30 dias (RFP, item 3.2) ou de 60 dias (Anexo I, item 4.1)?",
  responsavel="Delivery/Operação")

I("d01_assinatura", "D01", "3. CRONOGRAMA DO PROCESSO — 3.1 e 3.2", P2,
  'Não localizado · "a partir da assinatura do contrato"', "Lacuna", "Transição/Implantação / Administrativo do processo",
  "O cronograma não informa datas de resultado, negociação e assinatura do contrato, mas o prazo de transição conta da assinatura. Sem essa data não é possível saber se a transição termina antes do início dos serviços (01/02/2027) e do fim do SIEM legado (31/01/2027).",
  obrigatoriedade="Informativo", s=4, p=3,
  impacto="Impede planejar a transição e avaliar o risco de sobreposição ou lacuna de serviço.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d01_transicao30", "d04_risco_transicao"], acao="Esclarecer no Q&A",
  pergunta="Qual a data prevista para divulgação do resultado e para assinatura do contrato?",
  responsavel="Bid Manager")

I("d01_idioma", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.1", P3,
  '"A proposta deverá ser redigida em língua portuguesa"', "Instrução de resposta", "Administrativo do processo",
  "Proposta em português. Atestados, certificados e documentação técnica de fabricantes em outro idioma podem precisar de tradução (não especificado).",
  obrigatoriedade="Mandatório", s=2, p=3, impacto="Custo e prazo de tradução de documentos de suporte.",
  framework=APMP, controle="Conformidade com instruções de resposta (identificador a confirmar)", associacao="Boa prática",
  acao="Atender", responsavel="Bid Manager")

I("d01_portal", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.1", P3,
  '"enviada exclusivamente pelo portal de fornecedores do Banco"', "Instrução de resposta", "Administrativo do processo",
  "Envio exclusivo pelo portal de fornecedores. Endereço, necessidade de cadastro prévio, prazo de homologação e limite de tamanho de arquivo não são informados.",
  obrigatoriedade="Mandatório", s=4, p=3,
  impacto="Falta de cadastro ou falha no envio pelo único canal permitido pode impedir a entrega da proposta.",
  framework=APMP, controle="Logística de submissão (identificador a confirmar)", associacao="Boa prática",
  acao="Esclarecer no Q&A",
  pergunta="Qual o endereço do portal de fornecedores, é necessário cadastro ou homologação prévia (com que antecedência) e há limite de tamanho ou formato de arquivo?",
  responsavel="Bid Manager")

I("d01_paginas", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.2", P3,
  '"A proposta técnica deverá ter no máximo 40 (quarenta) páginas, excluídos os anexos."', "Instrução de resposta", "Administrativo do processo",
  "Limite de 40 páginas para a proposta técnica. Não se define o que pode ir para anexos nem a consequência de exceder o limite.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Excesso pode levar a desconsideração de conteúdo e perda de pontuação técnica.",
  framework=APMP, controle="Conformidade com instruções de resposta (identificador a confirmar)", associacao="Boa prática",
  acao="Atender", responsavel="Bid Manager")

I("d01_anexoIV", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.3", P3,
  '"A proposta comercial deverá ser apresentada conforme a planilha modelo do Anexo IV — Planilha de Preços."',
  "Instrução de resposta", "Comercial/Preço",
  "A proposta comercial deve seguir o modelo do Anexo IV. O arquivo foi listado pelo usuário, mas não anexado a esta análise ({d03_cobertura}); a estrutura de preços não pôde ser analisada.",
  obrigatoriedade="Mandatório", s=4, p=3,
  impacto="Proposta comercial fora do modelo pode ser desconsiderada; itens de preço do Anexo IV não foram confrontados com o escopo.",
  framework=APMP, controle="Conformidade com instruções de resposta (identificador a confirmar)", associacao="Boa prática",
  relacionados=["d03_cobertura"], acao="Atender", responsavel="Pricing/Financeiro")

I("d01_questionario", "D01", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.4", P3,
  '"O questionário técnico (planilha anexa) deverá ser integralmente preenchido."', "Instrução de resposta", "Administrativo do processo",
  "Preenchimento integral do questionário técnico. A RFP não prevê sanção; a aba 'Instruções' da planilha acrescenta a desclassificação ({d05_instr}).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Questionário incompleto leva à desclassificação, segundo a planilha.",
  framework=APMP, controle="Conformidade com instruções de resposta (identificador a confirmar)", associacao="Boa prática",
  relacionados=["d05_instr"], acao="Atender", responsavel="Pré-venda/Arquitetura")

I("d01_iso", "D01", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 a)", P3,
  '"certificado ISO/IEC 27001 vigente, emitido por organismo acreditado, cujo escopo inclua os serviços de SOC"',
  "Critério eliminatório / de habilitação", "Segurança da Informação/Cyber",
  "Inabilitação se não houver certificado ISO/IEC 27001 vigente, de organismo acreditado, com escopo que inclua o SOC. A RFP não diz por quem o organismo deve ser acreditado nem aceita certificação em andamento. Probabilidade 5: o item 5.1 diz expressamente que 'Serão inabilitados' os que não apresentarem o certificado.",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação.",
  framework=ISO, controle="Cláusula 4.3 — Determinação do escopo do SGSI", associacao="Direta",
  relacionados=["d05_qt01"], acao="Atender",
  pergunta="Serão aceitos certificados emitidos por organismos acreditados por membros do IAF (além do Inmetro/Cgcre)? O escopo pode estar no certificado de uma empresa do mesmo grupo econômico do proponente?",
  responsavel="Compliance")

I("d01_atestados", "D01", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 b)", P3,
  '"no mínimo 3 (três) atestados de capacidade técnica de prestação de serviços de SOC para instituições financeiras, com ambiente de no mínimo 2.000 usuários"',
  "Critério eliminatório / de habilitação", "Segurança da Informação/Cyber / Administrativo do processo",
  "Exige três atestados de SOC para instituições financeiras, com ambiente de pelo menos 2.000 usuários. Não está claro se o mínimo vale para cada atestado ou se pode ser somado, nem se contratos em andamento são aceitos. Probabilidade 5: inabilitação expressa no item 5.1.",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação.",
  framework="—", controle="—", associacao="Não aplicável",
  acao="Atender",
  pergunta="O mínimo de 2.000 usuários se aplica a cada atestado individualmente? São aceitos atestados de contratos em andamento e de instituições financeiras de outros segmentos (seguradoras, cooperativas)?",
  responsavel="Bid Manager")

I("d01_soc_nacional", "D01", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 c)", P3,
  '"comprovação de que o SOC está localizado em território nacional"', "Critério eliminatório / de habilitação",
  "Operação/Serviços / Regulatório/Compliance",
  "O SOC precisa estar no Brasil, confirmado pela resposta 2 do Q&A ({d05_qa2}). Não se define a forma de comprovação. Probabilidade 5: inabilitação expressa no item 5.1.",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação.",
  framework=CMN, controle="Contratação de serviços de processamento e armazenamento de dados (identificador a confirmar)", associacao="Correlata",
  relacionados=["d05_qa2", "d05_qa6"], acao="Atender",
  pergunta="Que documento será aceito como comprovação da localização do SOC em território nacional?",
  responsavel="Delivery/Operação")

I("d01_equipe_cert", "D01", "5. CRITÉRIOS DE HABILITAÇÃO — 5.2", P3,
  '"O proponente deverá possuir equipe técnica devidamente certificada."', "Ambiguidade", "Pessoas/Equipe",
  "Exigência na seção de habilitação, mas fora da lista de inabilitação do item 5.1: não define quais certificações, quantos profissionais, forma de comprovação nem se é eliminatória (tipo alternativo: Critério eliminatório / de habilitação). Relaciona-se com o CISSP do coordenador ({d02_cissp}) e com a pergunta QT-06 ({d05_qt06}).",
  obrigatoriedade="Mandatório", s=5, p=3,
  impacto="Se for tratada como eliminatória, a falta de comprovação adequada leva à inabilitação.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d02_cissp", "d05_qt06"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="O item 5.2 é critério de habilitação? Quais certificações, em que quantidade e com que comprovação serão exigidas da equipe técnica?",
  responsavel="RH/Staffing")

I("d01_pesos", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.1", P4,
  '"A nota final será composta pela Nota Técnica (peso de 60%) e pela Nota de Preço (peso de 40%)."',
  "Critério de avaliação / pontuação", "Comercial/Preço / Administrativo do processo",
  "Avaliação técnica e preço com pesos 60/40.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Orienta o equilíbrio entre qualidade técnica e agressividade de preço.",
  framework=APMP, controle="Estratégia de preço para vencer (identificador a confirmar)", associacao="Boa prática",
  acao="Precificar", responsavel="Bid Manager")

I("d01_nota_preco", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.1", P4,
  'Não localizado · "pela Nota de Preço (peso de 40%)"', "Lacuna", "Comercial/Preço",
  "A fórmula de cálculo da Nota de Preço (proporcional ao menor preço, faixas, preço de referência, critério de inexequibilidade) não foi localizada.",
  obrigatoriedade="Informativo", s=4, p=3,
  impacto="Sem a fórmula não é possível simular a nota final nem calibrar o preço.",
  framework=APMP, controle="Estratégia de preço para vencer (identificador a confirmar)", associacao="Boa prática",
  acao="Esclarecer no Q&A",
  pergunta="Qual a fórmula de cálculo da Nota de Preço e há critério de preço inexequível ou preço máximo de referência?",
  responsavel="Pricing/Financeiro")

for k, crit, pts in [("d01_c_metod", "Metodologia de operação do SOC 20", 20),
                     ("d01_c_equipe", "Qualificação da equipe 20", 20),
                     ("d01_c_ferr", "Ferramentas e tecnologia 15", 15),
                     ("d01_c_trans", "Plano de transição 10", 10)]:
    I(k, "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", P4, f'"{crit}"', "Critério de avaliação / pontuação",
      "Administrativo do processo",
      f"Critério técnico com pontuação máxima de {pts} pontos. A RFP não descreve subcritérios nem a forma de atribuição dos pontos; a soma dos critérios contradiz o máximo de 60 ({{d01_soma_contra}}).",
      obrigatoriedade="Informativo", s=3, p=3, impacto="Perda de pontuação técnica e risco de não atingir a nota mínima do item 6.3.",
      framework=APMP, controle="Resposta orientada aos critérios de avaliação (identificador a confirmar)", associacao="Boa prática",
      relacionados=["d01_soma_contra"], acao="Atender",
      pergunta="Quais os subcritérios e a escala de atribuição de pontos de cada critério técnico do item 6.2?" if k == "d01_c_metod" else "—",
      responsavel="Pré-venda/Arquitetura")

I("d01_soma_contra", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", P4,
  'A: "A Nota Técnica, de no máximo 60 (sessenta) pontos" · B: "Metodologia de operação do SOC 20 [...] Qualificação da equipe 20 [...] Ferramentas e tecnologia 15 [...] Plano de transição 10"',
  "Contradição", "Administrativo do processo",
  "O máximo declarado é de 60 pontos, mas os critérios somam 65 (20 + 20 + 15 + 10). Isso altera a nota de corte do item 6.3 (70% de 60 = 42 pontos; 70% de 65 = 45,5 pontos) e o peso relativo de cada critério.",
  obrigatoriedade="Informativo", s=4, p=3,
  impacto="Incerteza sobre a nota mínima de classificação e sobre a normalização da Nota Técnica.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d01_c_metod", "d01_c_equipe", "d01_c_ferr", "d01_c_trans", "d01_corte"], vigencia="Em esclarecimento",
  acao="Esclarecer no Q&A",
  pergunta="Os critérios do item 6.2 somam 65 pontos, mas a Nota Técnica máxima é de 60. Qual pontuação prevalece e como a nota será normalizada para o cálculo do corte de 70% (item 6.3)?",
  responsavel="Bid Manager")

I("d01_corte", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.3", P4,
  '"Serão desclassificadas as propostas com Nota Técnica inferior a 70% (setenta por cento) da pontuação máxima."',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Nota técnica mínima de 70% da pontuação máxima, cuja base é incerta (60 ou 65 pontos, veja {d01_soma_contra}). A desclassificação depende da avaliação do cliente, por isso a probabilidade fica em 3.",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Desclassificação.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d01_soma_contra", "d05_pesos_contra"], acao="Atender", responsavel="Bid Manager")

I("d01_desempate", "D01", "6. CRITÉRIOS DE AVALIAÇÃO — 6.4", P4,
  '"Em caso de empate na nota final, prevalecerá a proposta de menor preço."', "Critério de avaliação / pontuação", "Comercial/Preço",
  "Desempate pelo menor preço. Probabilidade 2: empate exato na nota final ponderada é pouco provável.",
  obrigatoriedade="Informativo", s=2, p=2, impacto="Em empate, o preço decide.",
  framework="—", controle="—", associacao="Não aplicável", responsavel="Pricing/Financeiro")

I("d01_vigencia", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.1", P5,
  '"O contrato terá vigência de 36 (trinta e seis) meses, prorrogável por iguais períodos mediante acordo entre as partes."',
  "Obrigação contratual", "Jurídico/Contratual",
  "Vigência de 36 meses, prorrogável por acordo. Horizonte de amortização de investimentos (SIEM, transição, migração).",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Define o prazo de amortização e de exposição às penalidades.",
  framework=CC, controle="Contratos em geral (identificador a confirmar)", associacao="Correlata",
  acao="Precificar", responsavel="Pricing/Financeiro")

I("d01_reajuste", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.2", P5,
  '"Os preços serão reajustados anualmente pela variação do IPCA."', "Obrigação contratual", "Financeiro",
  "Reajuste anual pelo IPCA; a data-base (proposta ou assinatura) não é informada. Custos de licenças em moeda estrangeira não são cobertos pelo índice.",
  obrigatoriedade="Mandatório", s=2, p=3, impacto="Risco de defasagem entre custos (pessoal, licenças em dólar) e reajuste.",
  framework=CC, controle="Contratos em geral (identificador a confirmar)", associacao="Correlata",
  acao="Esclarecer no Q&A", pergunta="Qual a data-base para o primeiro reajuste pelo IPCA: data da proposta ou da assinatura do contrato?",
  responsavel="Pricing/Financeiro")

I("d01_pagamento", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.3", P5,
  '"O pagamento será efetuado em até 60 (sessenta) dias após o aceite da nota fiscal."', "Obrigação contratual", "Financeiro",
  "Pagamento em até 60 dias após o aceite da nota fiscal; o prazo para o aceite não é definido, o que pode estender o ciclo de caixa. Probabilidade 5: o custo financeiro decorre diretamente do prazo fixado no texto.",
  obrigatoriedade="Mandatório", s=3, p=5, impacto="Custo de capital de giro a incluir no preço.",
  framework=CC, controle="Contratos em geral (identificador a confirmar)", associacao="Correlata",
  acao="Precificar", pergunta="Qual o prazo máximo para o aceite da nota fiscal pelo Banco?", responsavel="Pricing/Financeiro")

I("d01_multa", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.4", P5,
  '"O descumprimento de qualquer nível de serviço (SLA) previsto no Anexo I sujeitará a Contratada a multa de 10% (dez por cento) do valor mensal do contrato, por ocorrência."',
  "Penalidade / multa / glosa", "Jurídico/Contratual / Financeiro",
  "Multa de 10% do valor mensal por ocorrência de descumprimento de qualquer SLA, sem limite mensal ou global; o pedido de teto foi recusado ({d05_qa4}). Dez ocorrências num mês equivalem ao valor mensal integral. Probabilidade 4: a multa incide automaticamente 'por ocorrência' e o cliente recusou limitá-la na resposta 4 do Q&A.",
  obrigatoriedade="Mandatório", s=5, p=4, impacto="Exposição financeira sem limite, que pode superar a receita mensal do contrato.",
  framework=CC, controle="Art. 412 — limite da cláusula penal ao valor da obrigação principal", associacao="Correlata",
  relacionados=["d05_qa4", "d02_sla15", "d02_disp", "d02_relat", "d02_sla_escopo"], acao="Propor exceção/ressalva",
  pergunta="O Banco aceita teto mensal e global para as multas por descumprimento de SLA e gradação por severidade do indicador?",
  responsavel="Jurídico")

I("d01_ilimitada", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.5", P5,
  '"A Contratada responderá de forma integral e ilimitada por quaisquer danos decorrentes de incidentes de segurança ocorridos no ambiente do Contratante."',
  "Obrigação contratual", "Jurídico/Contratual",
  "Responsabilidade integral e ilimitada por quaisquer danos de incidentes no ambiente do Banco, sem exigir culpa da Contratada nem excluir danos indiretos; mantida após pedido de esclarecimento ({d05_qa4}).",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Exposição jurídica e financeira ilimitada, incompatível com seguro de valor definido.",
  framework=CC, controle="Responsabilidade civil contratual (identificador a confirmar)", associacao="Correlata",
  relacionados=["d01_seguro", "d05_qa4", "d02_lgpd_impl"], acao="Propor exceção/ressalva",
  pergunta="O Banco aceita limitar a responsabilidade da Contratada a um múltiplo do valor anual do contrato, restrita a danos diretos causados por culpa comprovada da Contratada?",
  responsavel="Jurídico")

I("d01_seguro", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.6", P5,
  '"A Contratada deverá manter seguro de responsabilidade civil cibernética em valor compatível com os riscos do contrato."',
  "Obrigação contratual", "Jurídico/Contratual / Financeiro",
  "Seguro cibernético obrigatório, com valor indefinido ('compatível com os riscos'); com responsabilidade ilimitada ({d01_ilimitada}), nenhum valor é objetivamente compatível.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Custo de prêmio não quantificável e risco de questionamento do valor contratado.",
  framework=CC, controle="Contrato de seguro (identificador a confirmar)", associacao="Correlata",
  relacionados=["d01_ilimitada"], acao="Esclarecer no Q&A",
  pergunta="Qual o valor mínimo de cobertura exigido para o seguro de responsabilidade civil cibernética?",
  responsavel="Jurídico")

I("d01_subcontr", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.7", P5,
  '"É vedada a subcontratação, total ou parcial, do objeto deste contrato."', "Restrição", "Jurídico/Contratual",
  "Vedação total de subcontratação. Inferência: o SIEM pode ser oferecido em nuvem pública (Anexo I, item 1.2), e o uso de provedor de nuvem, SaaS de terceiros, feeds de threat intelligence ou suporte de fabricante pode ser enquadrado como subcontratação parcial.",
  obrigatoriedade="Mandatório", natureza="Inferida", s=4, p=3,
  impacto="Pode inviabilizar arquiteturas baseadas em serviços de terceiros ou gerar descumprimento contratual.",
  framework=ISO, controle="A.5.19 Segurança da informação nas relações com fornecedores", associacao="Correlata",
  relacionados=["d02_siem", "d02_nuvem_contra"], acao="Esclarecer no Q&A",
  pergunta="O uso de provedores de nuvem, soluções SaaS de terceiros e suporte de fabricantes é considerado subcontratação para fins do item 7.7?",
  responsavel="Jurídico")

I("d01_confid", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.8", P5,
  '"As obrigações de confidencialidade vigorarão por 5 (cinco) anos após o término do contrato."', "Obrigação contratual", "Jurídico/Contratual",
  "Confidencialidade por 5 anos após o término.",
  obrigatoriedade="Mandatório", s=2, p=3, impacto="Obrigação pós-contratual de baixo custo.",
  framework=ISO, controle="A.6.6 Acordos de confidencialidade ou não divulgação", associacao="Direta",
  acao="Atender", responsavel="Jurídico")

I("d01_minuta", "D01", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS", P5,
  'Não localizado · "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS"', "Lacuna", "Jurídico/Contratual",
  "Inferência: a RFP traz só condições resumidas e não fornece minuta de contrato; os anexos citados ou presentes são I, III e IV, sem menção a um Anexo II. Rescisão, garantia contratual, acordo de tratamento de dados e cláusulas exigidas pela regulação não estão disponíveis para análise.",
  obrigatoriedade="Informativo", natureza="Inferida", s=3, p=3,
  impacto="Obrigações contratuais adicionais podem surgir na assinatura, sem estarem precificadas.",
  framework="—", controle="—", associacao="Não aplicável", acao="Esclarecer no Q&A",
  pergunta="Há minuta de contrato e um Anexo II? Em caso positivo, podem ser disponibilizados antes da entrega das propostas?",
  responsavel="Jurídico")

I("d01_cmn_impl", "D01", "1. APRESENTAÇÃO — 1.2", P2,
  '"requisitos para a contratação de serviços de processamento e armazenamento de dados e de computação em nuvem"',
  "Requisito implícito", "Regulatório/Compliance",
  "Inferência: como o Banco declara estar sujeito à Res. CMN nº 4.893/2021, que trata da contratação de processamento, armazenamento de dados e nuvem, o contrato do SOC (SIEM com logs do Banco, possivelmente em nuvem) tende a exigir cláusulas e evidências de conformidade da Contratada. A RFP não as detalha.",
  obrigatoriedade="Mandatório", natureza="Inferida", s=4, p=3,
  impacto="Obrigações regulatórias (acesso a dados, auditoria, localização) a absorver no contrato e no preço.",
  framework=CMN, controle="Contratação de serviços de processamento, armazenamento de dados e computação em nuvem (identificador a confirmar)",
  associacao="Direta", relacionados=["d05_qt04", "d02_nuvem_contra"], acao="Esclarecer no Q&A",
  pergunta="Quais requisitos da Resolução CMN nº 4.893/2021 o Banco espera que sejam refletidos no contrato e evidenciados pela Contratada?",
  responsavel="Compliance")

I("d01_anexoIII_decl", "D01", "Anexo III — Declaração de localização de dados", P6,
  '"Esta declaração deverá ser entregue assinada pelo representante legal do proponente junto com a proposta, sob pena de inabilitação."',
  "Critério eliminatório / de habilitação", "Regulatório/Compliance / Administrativo do processo",
  "Declaração assinada pelo representante legal, entregue com a proposta, sob pena de inabilitação. O conteúdo está só na página digitalizada; o Anexo III não é citado nos itens 4 e 5 da RFP. Probabilidade 5: inabilitação expressa no texto.",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d01_anexoIII_dados"], acao="Atender", responsavel="Jurídico")

I("d01_anexoIII_dados", "D01", "Anexo III — Declaração de localização de dados", P6,
  '"todos os dados do Banco Horizonte Fictício S.A., incluindo os registros (logs) de segurança, serão armazenados e processados exclusivamente em território nacional, durante toda a vigência do contrato"',
  "Restrição", "Privacidade/Proteção de Dados / Infraestrutura/Cloud",
  "Todos os dados, inclusive logs, devem ser armazenados e processados exclusivamente no Brasil. Conflita com o SIEM em nuvem pública de região livre ({d02_nuvem_contra}).",
  obrigatoriedade="Mandatório", s=4, p=3,
  impacto="Restringe a escolha de SIEM/SaaS e de regiões de nuvem; pode elevar o custo da plataforma.",
  framework=ISO, controle="A.5.23 Segurança da informação para uso de serviços em nuvem", associacao="Correlata",
  relacionados=["d02_nuvem_contra", "d01_anexoIII_decl"], acao="Atender", responsavel="Pré-venda/Arquitetura")

I("d01_anexoIII_prazo", "D01", "Anexo III — Declaração de localização de dados", P6,
  '"durante toda a vigência do contrato"', "Ambiguidade", "Privacidade/Proteção de Dados / Jurídico/Contratual",
  "A declaração cobre só a vigência do contrato (36 meses), mas o Anexo I exige manter logs por 5 anos ({d02_ret5}). Não está definido onde e por quem os logs são guardados após o término, nem se devem ser devolvidos ao Banco.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Custo e responsabilidade de guarda pós-contrato não definidos.",
  framework=LGPD, controle="Término do tratamento de dados (identificador a confirmar)", associacao="Correlata",
  relacionados=["d02_ret5", "d02_ret_amb"], acao="Esclarecer no Q&A",
  pergunta="Ao término do contrato, os logs ainda dentro do prazo de retenção de 5 anos devem ser devolvidos ao Banco, transferidos ao novo fornecedor ou mantidos pela Contratada (com que remuneração)?",
  responsavel="Jurídico")

# =============================================================== D02 — Anexo I
S1 = "§ 1. SERVIÇOS DE SOC"
S2 = "§ 2. NÍVEIS DE SERVIÇO (SLA)"
S3 = "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM)"
S4 = "§ 4. TRANSIÇÃO"
S5 = "§ 5. EQUIPE"
S6 = "§ 6. RESPONSABILIDADES DO CONTRATANTE"

I("d02_inv", "D02", "Documento inteiro (seções 1 a 6)", "§ 1 a § 6 (Word, sem paginação fixa)",
  '"Anexo I — Especificação Técnica"', "Registro de cobertura", "Administrativo do processo",
  "Inventário: documento Word com 22 parágrafos, 6 seções numeradas e nenhuma tabela; o extrator não sinalizou marcas de revisão nem comentários. Lido integralmente; localizador por seção/item (página não disponível).",
  responsavel="Bid Manager")

I("d02_monit", "D02", "1. SERVIÇOS DE SOC — 1.1", f"{S1}, item 1.1",
  '"O proponente deverá prestar serviço de monitoramento contínuo de eventos de segurança, em regime 24x7x365."',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber / Operação/Serviços",
  "Monitoramento contínuo 24x7x365, coerente com o objeto da RFP.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Escala 24x7 é o principal componente de custo de pessoal.",
  framework=ISO, controle="A.8.16 Atividades de monitoramento", associacao="Direta",
  relacionados=["d01_objeto_soc"], acao="Precificar", responsavel="Delivery/Operação")

I("d02_siem", "D02", "1. SERVIÇOS DE SOC — 1.2", f"{S1}, item 1.2",
  '"O proponente deverá fornecer a solução de SIEM"', "Requisito funcional / de serviço", "Infraestrutura/Cloud / Segurança da Informação/Cyber",
  "O proponente fornece o SIEM (licenças, infraestrutura, armazenamento). O custo depende da volumetria (EPS/GB por dia), recusada antes da contratação ({d05_qa3}).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Licenciamento e armazenamento do SIEM são um dos maiores componentes de custo.",
  framework=ISO, controle="A.8.15 Registro de logs", associacao="Correlata",
  relacionados=["d05_qa3", "d02_nuvem_contra"], acao="Precificar", responsavel="Pré-venda/Arquitetura")

I("d02_nuvem_contra", "D02", "1. SERVIÇOS DE SOC — 1.2 × RFP, Anexo III",
  f"A: {S1}, item 1.2 · B: D01, {P6}",
  'A: "podendo esta ser disponibilizada em nuvem pública, em região de livre escolha do proponente" · B: "serão armazenados e processados exclusivamente em território nacional"',
  "Contradição", "Infraestrutura/Cloud / Regulatório/Compliance",
  "O Anexo I permite SIEM em nuvem pública em qualquer região; a declaração do Anexo III, exigida sob pena de inabilitação, obriga armazenar e processar todos os dados, inclusive logs, no Brasil. Escolher região fora do país viola a declaração.",
  obrigatoriedade="Mandatório", s=5, p=3,
  impacto="Seguir o Anexo I com região estrangeira pode gerar inabilitação ou descumprimento contratual; seguir o Anexo III pode encarecer a plataforma.",
  framework=ISO, controle="A.5.23 Segurança da informação para uso de serviços em nuvem", associacao="Correlata",
  relacionados=["d01_anexoIII_dados", "d01_anexoIII_decl", "d01_precedencia", "d01_cmn_impl"], vigencia="Em esclarecimento",
  acao="Esclarecer no Q&A",
  pergunta="O SIEM em nuvem pública deve obrigatoriamente usar região localizada no Brasil, conforme a declaração do Anexo III, ou a livre escolha de região do Anexo I, item 1.2, prevalece?",
  responsavel="Pré-venda/Arquitetura")

I("d02_ret12", "D02", "1. SERVIÇOS DE SOC — 1.3", f"{S1}, item 1.3",
  '"Os registros (logs) de segurança deverão ser retidos por no mínimo 12 (doze) meses."', "Requisito não funcional",
  "Segurança da Informação/Cyber / Infraestrutura/Cloud",
  "Retenção mínima de 12 meses. Ver a relação com os 5 anos do item 1.6 ({d02_ret_amb}).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Custo de armazenamento proporcional à volumetria, que não foi informada.",
  framework=ISO, controle="A.8.15 Registro de logs", associacao="Direta",
  relacionados=["d02_ret_amb", "d05_qt03"], acao="Precificar", responsavel="Pré-venda/Arquitetura")

I("d02_integr", "D02", "1. SERVIÇOS DE SOC — 1.4", f"{S1}, item 1.4",
  '"O SIEM deverá ser integrado a todos os ativos relevantes do Contratante."', "Ambiguidade", "Técnico/Arquitetura",
  "Requisito de integração (tipo alternativo: Requisito funcional / de serviço) com escopo indefinido: 'ativos relevantes' não é listado nem quantificado, e a volumetria de EPS foi recusada ({d05_qa3}). Não se sabe se inclui as 2 nuvens públicas, os 2 data centers e as subsidiárias.",
  obrigatoriedade="Mandatório", s=4, p=3,
  impacto="Escopo aberto de integrações (conectores, parsers, coletores) e de volumetria, sem base para preço.",
  framework=ISO, controle="A.8.15 Registro de logs", associacao="Correlata",
  relacionados=["d05_qa3", "d04_servidores", "d04_nuvens", "d04_subsid"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Quais são os 'ativos relevantes' a integrar ao SIEM (tipos e quantidades de fontes de log, inclusive nuvens públicas, data centers e subsidiárias)?",
  responsavel="Pré-venda/Arquitetura")

I("d02_ir", "D02", "1. SERVIÇOS DE SOC — 1.5", f"{S1}, item 1.5",
  '"O serviço deverá contemplar resposta a incidentes, incluindo contenção, erradicação"', "Requisito funcional / de serviço",
  "Segurança da Informação/Cyber",
  "Resposta a incidentes com contenção e erradicação. Não define se é remota ou presencial, se inclui forense, recuperação, nem limite de horas ou de incidentes.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Esforço de resposta a incidentes sem limite definido.",
  framework=ISO, controle="A.5.26 Resposta a incidentes de segurança da informação", associacao="Direta",
  relacionados=["d01_ilimitada"], acao="Esclarecer no Q&A",
  pergunta="A resposta a incidentes inclui atuação presencial, análise forense e recuperação? Há limite de horas ou de incidentes por mês incluído no preço?",
  responsavel="Segurança/Cyber")

I("d02_pir", "D02", "1. SERVIÇOS DE SOC — 1.5", f"{S1}, item 1.5",
  '"elaboração de relatório pós-incidente"', "Entregável", "Segurança da Informação/Cyber",
  "Relatório pós-incidente; prazo e formato não definidos.",
  obrigatoriedade="Mandatório", s=2, p=3, impacto="Esforço de documentação por incidente.",
  framework=ISO, controle="A.5.27 Aprendizado com incidentes de segurança da informação", associacao="Correlata",
  acao="Atender", responsavel="Segurança/Cyber")

I("d02_ret5", "D02", "1. SERVIÇOS DE SOC — 1.6", f"{S1}, item 1.6",
  '"Para fins de auditoria, os logs deverão ser mantidos por 5 (cinco) anos."', "Requisito não funcional",
  "Segurança da Informação/Cyber / Regulatório/Compliance",
  "Retenção de logs por 5 anos para auditoria, além da vigência de 36 meses, sem volumetria informada.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Custo de armazenamento de longo prazo e obrigação pós-contrato.",
  framework=ISO, controle="A.5.33 Proteção de registros", associacao="Direta",
  relacionados=["d02_ret_amb", "d01_anexoIII_prazo", "d05_qa3"], acao="Precificar", responsavel="Pré-venda/Arquitetura")

I("d02_ret_amb", "D02", "1. SERVIÇOS DE SOC — 1.3 × 1.6", f"A: {S1}, item 1.3 · B: {S1}, item 1.6",
  'A: "deverão ser retidos por no mínimo 12 (doze) meses" · B: "os logs deverão ser mantidos por 5 (cinco) anos"',
  "Ambiguidade", "Segurança da Informação/Cyber / Infraestrutura/Cloud",
  "Dois prazos de retenção para os mesmos logs, sem definição de camadas: 12 meses consultáveis (a QT-03 fala em 'online', {d05_qt03}) e 5 anos em arquivo? Não se define o formato, o tempo de recuperação do arquivo nem se a retenção de 5 anos inclui os 24 meses de logs migrados do SIEM legado ({d04_migr}).",
  obrigatoriedade="Informativo", s=4, p=3, impacto="A diferença de custo entre 5 anos online e 12 meses online + arquivo é elevada.",
  framework=ISO, controle="A.8.15 Registro de logs", associacao="Correlata",
  relacionados=["d02_ret12", "d02_ret5", "d05_qt03", "d04_migr"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Os logs devem ficar consultáveis online por 12 meses e arquivados até completar 5 anos? Qual o tempo máximo aceitável para recuperar logs arquivados?",
  responsavel="Pré-venda/Arquitetura")

I("d02_sla15", "D02", "2. NÍVEIS DE SERVIÇO (SLA) — 2.1", f"{S2}, item 2.1",
  '"Tempo máximo para início do tratamento de incidentes críticos: 15 (quinze) minutos."', "SLA / KPI", "Operação/Serviços",
  "Início do tratamento de incidentes críticos em até 15 minutos, 24x7. A classificação de 'crítico' depende de matriz do Contratante não fornecida ({d02_matriz}). Cada descumprimento gera multa de 10% do valor mensal ({d01_multa}).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Exige analistas disponíveis em todos os turnos e expõe a multas por ocorrência.",
  framework=ITIL, controle="Prática de gerenciamento de nível de serviço", associacao="Direta",
  relacionados=["d01_multa", "d02_matriz"], acao="Precificar", responsavel="Delivery/Operação")

I("d02_disp", "D02", "2. NÍVEIS DE SERVIÇO (SLA) — 2.2", f"{S2}, item 2.2",
  '"Disponibilidade mínima mensal da plataforma SIEM: 99,9%."', "SLA / KPI", "Infraestrutura/Cloud",
  "Disponibilidade de 99,9% ao mês (cerca de 43 minutos de indisponibilidade). Não se definem janelas de manutenção, forma de medição nem exclusões (falhas do Contratante, da VPN ou do provedor de nuvem).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Exige arquitetura redundante; indisponibilidades geram multa por ocorrência.",
  framework=ITIL, controle="Prática de gerenciamento de disponibilidade", associacao="Direta",
  relacionados=["d01_multa"], acao="Esclarecer no Q&A",
  pergunta="Como será medida a disponibilidade do SIEM e quais as exclusões (janelas de manutenção programada, falhas de infraestrutura do Banco, VPN)?",
  responsavel="Pré-venda/Arquitetura")

I("d02_relat", "D02", "2. NÍVEIS DE SERVIÇO (SLA) — 2.3", f"{S2}, item 2.3",
  '"Relatório mensal de indicadores, a ser entregue até o 5º dia útil do mês subsequente."', "SLA / KPI", "Operação/Serviços",
  "Relatório mensal de indicadores até o 5º dia útil; está na seção de SLA, logo o atraso também gera multa de 10% ({d01_multa}). Conteúdo mínimo não definido (tipo alternativo: Entregável).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Atraso de um relatório pode custar 10% do valor mensal.",
  framework=ITIL, controle="Prática de medição e relatórios", associacao="Direta",
  relacionados=["d01_multa"], acao="Atender", responsavel="Delivery/Operação")

I("d02_matriz", "D02", "2. NÍVEIS DE SERVIÇO (SLA) — 2.4", f"{S2}, item 2.4",
  'Não localizado · "A classificação de criticidade dos incidentes seguirá a matriz de classificação do Contratante."',
  "Lacuna", "Operação/Serviços", "A matriz de classificação de criticidade do Contratante é citada, mas não foi fornecida no pacote. Sem ela não é possível estimar quantos incidentes estarão sob o SLA de 15 minutos.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Volume de incidentes críticos sujeitos a SLA e multa desconhecido.",
  framework=ISO, controle="A.5.25 Avaliação e decisão sobre eventos de segurança da informação", associacao="Correlata",
  relacionados=["d02_sla15"], acao="Esclarecer no Q&A",
  pergunta="Podem disponibilizar a matriz de classificação de criticidade de incidentes do Banco e o histórico mensal de incidentes por criticidade?",
  responsavel="Segurança/Cyber")

I("d02_sla_escopo", "D02", "2. NÍVEIS DE SERVIÇO (SLA) × 3. IAM", f"{S2} e {S3}",
  '"O descumprimento de qualquer nível de serviço (SLA) previsto no Anexo I"', "Ambiguidade", "Operação/Serviços / Jurídico/Contratual",
  "Não está claro quais indicadores são 'nível de serviço' para a multa da RFP, item 7.4: só os da seção 2 ou também os prazos e metas do IAM (revogação em 24 h, MFA em 100%, recertificação trimestral) e a meta de falsos positivos do workshop ({d04_meta_fp}).",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Cada indicador adicional sob a multa de 10% por ocorrência amplia a exposição financeira.",
  framework=ITIL, controle="Prática de gerenciamento de nível de serviço", associacao="Correlata",
  relacionados=["d01_multa", "d02_revog", "d02_mfa", "d02_recert", "d04_meta_fp"], vigencia="Em esclarecimento",
  acao="Esclarecer no Q&A",
  pergunta="Quais indicadores do Anexo I são considerados SLA para a multa do item 7.4 da RFP: apenas os da seção 2 ou também os prazos da seção 3 (IAM)?",
  responsavel="Jurídico")

I("d02_ciclo", "D02", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.1", f"{S3}, item 3.1",
  '"Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"', "Requisito funcional / de serviço",
  "Segurança da Informação/Cyber",
  "Gestão do ciclo de vida de identidades. A seção 3 não usa verbo de obrigação, mas descreve o escopo do serviço; classificado como mandatório pelo efeito. O ambiente atual é Active Directory com scripts internos ({d04_iam_atual}).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Esforço de operação proporcional ao volume de admissões, movimentações e desligamentos (não informado).",
  framework=ISO, controle="A.5.16 Gestão de identidades", associacao="Direta",
  relacionados=["d02_iam_lacuna", "d04_iam_atual"], acao="Precificar", responsavel="Delivery/Operação")

I("d02_revog", "D02", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.1", f"{S3}, item 3.1",
  '"com revogação dos acessos de colaboradores desligados em até 24 (vinte e quatro) horas"', "SLA / KPI", "Segurança da Informação/Cyber",
  "Revogação em até 24 horas do desligamento. O prazo depende de o RH comunicar o desligamento a tempo, o que não é atribuído ao Contratante na seção 6.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Descumprimento por causa externa (comunicação tardia do RH) pode gerar multa.",
  framework=ISO, controle="A.5.18 Direitos de acesso", associacao="Direta",
  relacionados=["d02_sla_escopo"], acao="Registrar premissa na proposta",
  pergunta="O prazo de 24 horas será contado a partir da comunicação formal do desligamento pelo Banco à Contratada?",
  responsavel="Delivery/Operação")

I("d02_mfa", "D02", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.2", f"{S3}, item 3.2",
  '"Autenticação multifator (MFA) obrigatória para 100% dos usuários com acesso privilegiado."', "Requisito não funcional",
  "Segurança da Informação/Cyber",
  "MFA para todos os usuários privilegiados. Não diz quem fornece a solução de MFA nem quantos são os usuários privilegiados; hoje não há PAM ({d04_sem_pam}).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Possível custo de licenças de MFA e esforço de implantação.",
  framework=ISO, controle="A.8.5 Autenticação segura", associacao="Direta",
  relacionados=["d02_iam_lacuna", "d04_sem_pam"], acao="Esclarecer no Q&A",
  pergunta="Quantos usuários têm acesso privilegiado e a solução de MFA será fornecida pelo Banco ou pela Contratada?",
  responsavel="Segurança/Cyber")

I("d02_recert", "D02", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.3", f"{S3}, item 3.3",
  '"Revisão (recertificação) trimestral dos acessos concedidos."', "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Recertificação trimestral de todos os acessos, sem informar o número de sistemas e perfis. Sem ferramenta de IGA (hoje AD + scripts), o esforço é manual.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Esforço trimestral proporcional a usuários × sistemas.",
  framework=ISO, controle="A.5.18 Direitos de acesso", associacao="Direta",
  relacionados=["d02_iam_lacuna"], acao="Precificar", responsavel="Delivery/Operação")

I("d02_pam", "D02", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.4", f"{S3}, item 3.4",
  '"É desejável que a solução contemple cofre de senhas para contas privilegiadas (PAM)."', "Oportunidade / diferencial",
  "Segurança da Informação/Cyber",
  "PAM desejável; o Banco não tem PAM hoje ({d04_sem_pam}). Pode pontuar em 'Ferramentas e tecnologia' ({d01_c_ferr}), mas a RFP não diz como itens desejáveis são pontuados.",
  obrigatoriedade="Desejável",
  framework=ISO, controle="A.8.2 Direitos de acesso privilegiado", associacao="Correlata",
  relacionados=["d04_sem_pam", "d01_c_ferr"], acao="Precificar", responsavel="Pré-venda/Arquitetura")

I("d02_iam_lacuna", "D02", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM)", f"{S3}, itens 3.1 a 3.4",
  'Não localizado · "Gestão do ciclo de vida das identidades"', "Lacuna", "Segurança da Informação/Cyber / Comercial/Preço",
  "Não localizado: (a) se o proponente deve fornecer plataforma de IAM/IGA e MFA (para o SIEM isso é explícito no item 1.2; para o IAM não); (b) volumetria de IAM: sistemas integrados, perfis, movimentações e desligamentos por mês.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Diferença relevante de preço entre operar a ferramenta do Banco e fornecer e implantar uma plataforma de IGA.",
  framework=ISO, controle="A.5.16 Gestão de identidades", associacao="Correlata",
  relacionados=["d01_objeto_iam", "d04_iam_atual"], acao="Esclarecer no Q&A",
  pergunta="O proponente deve fornecer plataforma de IAM/IGA e MFA ou operar as ferramentas do Banco? Quantos sistemas devem ser integrados e qual a média mensal de admissões, movimentações e desligamentos?",
  responsavel="Pré-venda/Arquitetura")

I("d02_lgpd_impl", "D02", "1. SERVIÇOS DE SOC — 1.3 e 3. IAM — 3.1", f"{S1}, item 1.3 · {S3}, item 3.1",
  '"Os registros (logs) de segurança deverão ser retidos"', "Requisito implícito", "Privacidade/Proteção de Dados",
  "Inferência: logs de segurança e dados de identidade de colaboradores contêm dados pessoais (nome, login, IP, horários de acesso). Ao armazená-los e tratá-los por conta do Banco, a Contratada atua como operadora, com obrigações de segurança e registro de operações e responsabilidade solidária em certas hipóteses. A RFP não prevê acordo de tratamento de dados.",
  obrigatoriedade="Mandatório", natureza="Inferida", s=4, p=3,
  impacto="Obrigações e responsabilidade da LGPD a absorver; soma-se à responsabilidade ilimitada do item 7.5 da RFP.",
  framework=LGPD, controle="Art. 5º, VII (operador) · art. 39 · art. 46", associacao="Direta",
  relacionados=["d01_ilimitada", "d01_anexoIII_dados"], acao="Registrar premissa na proposta",
  pergunta="O Banco firmará acordo de tratamento de dados pessoais (operador) definindo instruções, medidas de segurança e limites de responsabilidade da Contratada?",
  responsavel="Compliance")

I("d02_transicao60", "D02", "4. TRANSIÇÃO — 4.1", f"{S4}, item 4.1",
  '"A transição dos serviços deverá ser concluída em até 60 (sessenta) dias corridos a partir da assinatura do contrato."',
  "Prazo / marco", "Transição/Implantação",
  "Transição em até 60 dias corridos, o dobro do prazo da RFP, item 3.2 ({d02_transicao_contra}).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Define o custo e a viabilidade da transição.",
  framework=ITIL, controle="Prática de gerenciamento de mudanças / transição (identificador a confirmar)", associacao="Correlata",
  relacionados=["d01_transicao30", "d02_transicao_contra"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  responsavel="Delivery/Operação")

I("d02_transicao_contra", "D02", "RFP 3.2 × Anexo I 4.1", f"A: D01, {P2}, item 3.2 · B: {S4}, item 4.1",
  'A: "deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato" · B: "deverá ser concluída em até 60 (sessenta) dias corridos a partir da assinatura do contrato"',
  "Contradição", "Transição/Implantação",
  "Prazos de transição incompatíveis (30 × 60 dias), sem cláusula de precedência ({d01_precedencia}). A diferença afeta o tamanho da equipe de transição, o custo da operação em paralelo sem remuneração (item 4.2) e o plano de transição, que vale 10 pontos.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Dimensionar para 60 dias e ser cobrado por 30 gera descumprimento; dimensionar para 30 encarece a proposta.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d01_transicao30", "d02_transicao60", "d01_precedencia", "d02_paralelo", "d04_risco_transicao"], vigencia="Em esclarecimento",
  acao="Esclarecer no Q&A",
  pergunta="O prazo de transição é de 30 dias (RFP, item 3.2) ou de 60 dias (Anexo I, item 4.1), contados da assinatura do contrato?",
  responsavel="Delivery/Operação")

I("d02_paralelo", "D02", "4. TRANSIÇÃO — 4.2", f"{S4}, item 4.2",
  '"Durante a transição, o proponente deverá operar em paralelo com o fornecedor atual, sem custo adicional para o Contratante."',
  "Obrigação contratual", "Transição/Implantação / Comercial/Preço",
  "Operação em paralelo durante a transição, sem remuneração adicional. Probabilidade 5: o custo decorre diretamente do texto ('sem custo adicional'). O SIEM legado encerra em 31/01/2027 ({d04_siem_legado}), o que limita o período de paralelismo possível.",
  obrigatoriedade="Mandatório", s=3, p=5, impacto="Custo de 30 a 60 dias de operação não remunerada a diluir no preço.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d02_transicao_contra", "d04_siem_legado"], acao="Precificar", responsavel="Pricing/Financeiro")

I("d02_cissp", "D02", "5. EQUIPE — 5.1", f"{S5}, item 5.1",
  '"O serviço deverá contar com coordenador com certificação CISSP, dedicado exclusivamente ao contrato."', "Restrição", "Pessoas/Equipe",
  "Coordenador CISSP com dedicação exclusiva durante toda a vigência. Probabilidade 5: custo fixo de um profissional dedicado exigido expressamente.",
  obrigatoriedade="Mandatório", s=3, p=5, impacto="Custo fixo de 1 FTE sênior por 36 meses e risco de substituição.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d01_equipe_cert"], acao="Precificar", responsavel="RH/Staffing")

I("d02_n1", "D02", "5. EQUIPE — 5.2", f"{S5}, item 5.2",
  '"Os analistas de nível 1 deverão atuar presencialmente na sede do Contratante, em São Paulo/SP, em horário comercial."',
  "Restrição", "Pessoas/Equipe / Operação/Serviços",
  "N1 presencial em São Paulo no horário comercial. Alterado pela resposta 6 do Q&A ({d05_qa6}), que admite atuação remota no Brasil. Fora do horário comercial, o regime 24x7 não é detalhado.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Custo de alocação presencial; reduzido pela alteração do Q&A.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d05_qa6"], vigencia="Alterado", acao="Atender", responsavel="RH/Staffing")

I("d02_vpn", "D02", "6. RESPONSABILIDADES DO CONTRATANTE — 6.1", f"{S6}, item 6.1",
  '"Disponibilizar acesso remoto seguro (VPN) aos ambientes monitorados."', "Responsabilidade / dependência do cliente",
  "Infraestrutura/Cloud",
  "O Banco fornece VPN. Não define se cobre a coleta de logs (coletores/forwarders) ou apenas o acesso de analistas, nem se falhas de VPN excluem o SLA.",
  obrigatoriedade="Informativo", s=2, p=3, impacto="Dependência do cliente que afeta SLA e disponibilidade.",
  framework=ISO, controle="A.6.7 Trabalho remoto", associacao="Correlata",
  relacionados=["d02_disp"], acao="Registrar premissa na proposta", responsavel="Pré-venda/Arquitetura")

I("d02_doc10", "D02", "6. RESPONSABILIDADES DO CONTRATANTE — 6.2", f"{S6}, item 6.2",
  '"Disponibilizar a documentação técnica do ambiente em até 10 (dez) dias após a assinatura do contrato."',
  "Responsabilidade / dependência do cliente", "Transição/Implantação",
  "Documentação técnica entregue em até 10 dias da assinatura: num prazo de transição de 30 dias, restam 20 dias de trabalho com a documentação.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Compressão do prazo efetivo de transição.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d01_transicao30", "d04_risco_transicao"], acao="Registrar premissa na proposta", responsavel="Delivery/Operação")

# =============================================================== D03 — Anexo IV (não anexado)
I("d03_cobertura", "D03", "Arquivo inteiro", "não disponível (arquivo não anexado)",
  'Arquivo não recebido · listado pelo usuário como "Anexo_IV_Planilha_de_Precos.xlsx" (Planilha de preços, v1.0)',
  "Registro de cobertura", "Comercial/Preço",
  "Arquivo listado pelo usuário na solicitação (item 5) e não anexado; o inventário da extração o registra como ARQUIVO NÃO ENCONTRADO. Conteúdo (itens de preço, unidades, quantidades, regras de preenchimento) não analisado. É o modelo exigido pelo item 4.3 da RFP ({d01_anexoIV}). Como o usuário dispõe do arquivo, não há pedido ao cliente: basta enviá-lo para análise incremental.",
  relacionados=["d01_anexoIV"], responsavel="Bid Manager",
  pendencia="Anexo_IV_Planilha_de_Precos.xlsx listado pelo usuário e não anexado; enviar para análise incremental")

# =============================================================== D04 — Apresentação
I("d04_inv", "D04", "Apresentação inteira (slides 1 a 5 e notas)", "slides 1–5",
  '"Workshop com proponentes — RFP nº 2026-017 — 22/10/2026"', "Registro de cobertura", "Administrativo do processo",
  "Inventário: 5 slides, nenhum oculto; o slide 5 tem notas do apresentador, lidas e analisadas (ampliação de escopo, {d04_subsid}). Material de workshop sem status contratual definido.",
  responsavel="Bid Manager")

I("d04_usuarios", "D04", "Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"6.200 usuários ativos"', "Dado de dimensionamento", "Operação/Serviços",
  "6.200 usuários ativos, acima dos 4.500 colaboradores da RFP ({d04_usuarios_contra}).",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Base de dimensionamento do IAM e do SOC.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d04_usuarios_contra"], acao="Esclarecer no Q&A", responsavel="Pricing/Financeiro")

I("d04_usuarios_contra", "D04", "RFP 2.1 × slide 2", f'A: D01, {P2}, item 2.1 · B: slide 2 — "Números do ambiente"',
  'A: "abrangendo aproximadamente 4.500 colaboradores" · B: "6.200 usuários ativos"', "Contradição", "Operação/Serviços / Comercial/Preço",
  "A RFP fala em cerca de 4.500 colaboradores; a apresentação, em 6.200 usuários ativos (38% a mais), sem contar os cerca de 900 das subsidiárias ({d04_subsid}). 'Colaboradores' e 'usuários ativos' podem não ser a mesma base (contas de terceiros e de serviço).",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Subdimensionamento do IAM e do volume de eventos se a base menor for usada.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d01_usuarios", "d04_usuarios", "d04_subsid", "d05_qa5"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Qual a base de usuários para dimensionamento: 4.500 colaboradores (RFP), 6.200 usuários ativos (workshop) ou 5.000 (Q&A)? Ela inclui terceiros, contas de serviço e as subsidiárias?",
  responsavel="Pricing/Financeiro")

I("d04_servidores", "D04", "Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"850 servidores (70% Windows, 30% Linux)"', "Dado de dimensionamento", "Infraestrutura/Cloud",
  "850 servidores, 70% Windows e 30% Linux: base parcial para estimar fontes de log. Não inclui rede, segurança de perímetro, bancos de dados nem aplicações.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Insuficiente sozinho para estimar EPS.",
  framework="—", controle="—", associacao="Não aplicável", relacionados=["d02_integr", "d05_qa3"], responsavel="Pré-venda/Arquitetura")

I("d04_dcs", "D04", "Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"2 data centers próprios (São Paulo e Campinas)"', "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Dois data centers próprios, o que exige coletores em cada localidade.",
  obrigatoriedade="Informativo", s=2, p=3, impacto="Infraestrutura de coleta em dois sites.",
  framework="—", controle="—", associacao="Não aplicável", relacionados=["d02_integr"], responsavel="Pré-venda/Arquitetura")

I("d04_nuvens", "D04", "Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"Workloads em 2 nuvens públicas"', "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Duas nuvens públicas não identificadas, sem volume de workloads. Necessário para conectores e custo de ingestão.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Escopo de integração com nuvem indefinido.",
  framework="—", controle="—", associacao="Não aplicável", relacionados=["d02_integr"], acao="Esclarecer no Q&A",
  pergunta="Quais são as duas nuvens públicas utilizadas e quantas contas, assinaturas ou projetos devem ser monitorados?",
  responsavel="Pré-venda/Arquitetura")

I("d04_siem_legado", "D04", "Ferramentas atuais", 'slide 3 — "Ferramentas atuais"',
  '"SIEM legado — contrato encerra em 31/01/2027, sem possibilidade de prorrogação"', "Restrição", "Transição/Implantação / Continuidade",
  "O SIEM atual sai de operação em 31/01/2027, sem prorrogação. A nova plataforma precisa estar operando antes dessa data, e a exportação dos 24 meses de logs ({d04_migr}) também.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Prazo rígido para transição e migração, sem alternativa de contingência.",
  framework=ISO, controle="A.5.30 Prontidão de TIC para continuidade de negócios", associacao="Correlata",
  relacionados=["d01_inicio", "d04_risco_transicao", "d04_migr"], acao="Mitigar", responsavel="Delivery/Operação")

I("d04_iam_atual", "D04", "Ferramentas atuais", 'slide 3 — "Ferramentas atuais"',
  '"IAM: Active Directory + scripts internos"', "Dado de dimensionamento", "Segurança da Informação/Cyber",
  "IAM atual baseado em Active Directory e scripts, sem ferramenta de IGA; o ciclo de vida e a recertificação exigidos no Anexo I tendem a requerer automação nova.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Esforço de implantação de IAM maior que o de mera operação.",
  framework="—", controle="—", associacao="Não aplicável", relacionados=["d02_iam_lacuna", "d02_ciclo"], responsavel="Pré-venda/Arquitetura")

I("d04_sem_pam", "D04", "Ferramentas atuais", 'slide 3 — "Ferramentas atuais"',
  '"Não há solução de PAM"', "Dado de dimensionamento", "Segurança da Informação/Cyber",
  "Não há PAM; relevante para o PAM desejável ({d02_pam}) e para MFA em privilegiados ({d02_mfa}).",
  obrigatoriedade="Informativo", s=2, p=3, impacto="Oportunidade de oferta e esforço de implantação.",
  framework="—", controle="—", associacao="Não aplicável", relacionados=["d02_pam", "d02_mfa"], responsavel="Pré-venda/Arquitetura")

I("d04_alertas", "D04", "Desafios", 'slide 4 — "Desafios"', '"Cerca de 1.200 alertas por dia"', "Dado de dimensionamento",
  "Operação/Serviços", "Cerca de 1.200 alertas por dia (cerca de 36.000 por mês) com o SIEM legado: base para o dimensionamento da triagem N1.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Direciona o tamanho da equipe de N1.",
  framework="—", controle="—", associacao="Não aplicável", responsavel="Delivery/Operação")

I("d04_fp", "D04", "Desafios", 'slide 4 — "Desafios"', '"70% de falsos positivos"', "Dado de dimensionamento", "Operação/Serviços",
  "70% de falsos positivos no cenário atual.", obrigatoriedade="Informativo", s=2, p=3, impacto="Esforço de tuning na transição.",
  framework="—", controle="—", associacao="Não aplicável", relacionados=["d04_meta_fp"], responsavel="Delivery/Operação")

I("d04_meta_fp", "D04", "Desafios", 'slide 4 — "Desafios"',
  '"Meta: reduzir os falsos positivos para 10% no primeiro trimestre de operação"', "SLA / KPI", "Operação/Serviços",
  "Meta de reduzir falsos positivos de 70% para 10% em três meses, presente só no workshop. Não está claro se é SLA contratual sujeito à multa ({d02_sla_escopo}) nem como a taxa será medida.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Meta agressiva; se for contratual, expõe a multa e exige esforço intenso de tuning.",
  framework=ITIL, controle="Prática de gerenciamento de monitoramento e eventos", associacao="Correlata",
  relacionados=["d02_sla_escopo", "d04_escopo_amb"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="A meta de 10% de falsos positivos no primeiro trimestre é obrigação contratual (SLA) ou objetivo de referência? Como a taxa será medida?",
  responsavel="Delivery/Operação")

I("d04_migr", "D04", "Expectativas para o novo serviço", 'slide 5 — "Expectativas para o novo serviço"',
  '"Migração de 24 meses de logs históricos do SIEM legado para a nova plataforma"', "Requisito funcional / de serviço",
  "Transição/Implantação / Dados/Analytics",
  "Migração de 24 meses de logs históricos, não prevista na RFP nem no Anexo I. Volume desconhecido (EPS recusado, {d05_qa3}), e a exportação depende do SIEM legado, que encerra em 31/01/2027. Apresentada como 'expectativa' (obrigatoriedade incerta, {d04_escopo_amb}).",
  obrigatoriedade="Desejável", s=4, p=3, impacto="Esforço e armazenamento adicionais não quantificáveis; risco de inviabilidade no prazo.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d04_escopo_amb", "d04_siem_legado", "d02_ret_amb"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="A migração de 24 meses de logs do SIEM legado faz parte do escopo obrigatório? Qual o volume (TB) e o formato dos dados, e quem é responsável pela exportação do SIEM legado?",
  responsavel="Pré-venda/Arquitetura")

I("d04_visao", "D04", "Expectativas para o novo serviço", 'slide 5 — "Expectativas para o novo serviço"',
  '"Visão unificada de riscos para a diretoria"', "Oportunidade / diferencial", "Dados/Analytics / Segurança da Informação/Cyber",
  "Expectativa de visão unificada de riscos para a diretoria, não especificada na RFP: dashboard executivo pode diferenciar a proposta em 'Ferramentas e tecnologia' e 'Metodologia'.",
  obrigatoriedade="Desejável", framework=CSF, controle="GV — Governança (identificador a confirmar)", associacao="Correlata",
  relacionados=["d04_escopo_amb", "d01_c_ferr"], acao="Precificar", responsavel="Pré-venda/Arquitetura")

I("d04_subsid", "D04", "Expectativas para o novo serviço — notas do apresentador", "slide 5 — notas do apresentador",
  '"as subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários adicionais) também deverão ser incluídas no escopo"',
  "Requisito funcional / de serviço", "Operação/Serviços / Comercial/Preço",
  "Ampliação de escopo para duas subsidiárias (cerca de 900 usuários), que só consta das notas do apresentador e não da RFP, do Anexo I nem do Q&A. Não se sabe se as subsidiárias têm ambientes, ativos e contratos próprios, nem se a habilitação e o contrato as abrangem.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Aumento de cerca de 15–20% na base de usuários e de ativos não previsto no preço.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d04_usuarios_contra", "d04_escopo_amb", "d05_qa5"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="As subsidiárias Horizonte Seguros e Horizonte Investimentos fazem parte do escopo (SOC e IAM)? Quais seus ativos e usuários e quem será a parte contratante para elas?",
  responsavel="Bid Manager")

I("d04_escopo_amb", "D04", "Slides 4 e 5 e notas do apresentador", "slide 4 — \"Desafios\" · slide 5 — \"Expectativas para o novo serviço\" · slide 5 — notas do apresentador",
  '"Lembrar os proponentes"', "Ambiguidade", "Administrativo do processo / Jurídico/Contratual",
  "A apresentação introduz escopo e metas ausentes da RFP e do Anexo I (subsidiárias, migração de 24 meses de logs, visão unificada de riscos, meta de 10% de falsos positivos), parte deles só em notas do apresentador. Sem cláusula de precedência ({d01_precedencia}) não se sabe se o material do workshop é vinculante.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Escopo adicional não precificado ou exigido depois da assinatura.",
  framework=APMP, controle="Gestão de escopo da oferta (identificador a confirmar)", associacao="Boa prática",
  relacionados=["d04_subsid", "d04_migr", "d04_visao", "d04_meta_fp", "d01_precedencia"], vigencia="Em esclarecimento",
  acao="Esclarecer no Q&A",
  pergunta="Os itens apresentados no workshop de 22/10/2026 e ausentes da RFP e do Anexo I (subsidiárias, migração de logs, visão unificada de riscos, meta de falsos positivos) integram o escopo contratual? Serão formalizados em adendo?",
  responsavel="Bid Manager")

I("d04_risco_transicao", "D04", "Ferramentas atuais × cronograma e transição", 'slide 3 — "Ferramentas atuais" · D01, p. 2 (impressa: 1), itens 3.1 e 3.2',
  '"contrato encerra em 31/01/2027, sem possibilidade de prorrogação"', "Risco para o proponente", "Transição/Implantação / Continuidade",
  "Risco combinado: o SIEM legado encerra em 31/01/2027 sem prorrogação ({d04_siem_legado}); os serviços começam em 01/02/2027 ({d01_inicio}); a transição conta de uma assinatura sem data ({d01_assinatura}) e tem prazo contraditório ({d02_transicao_contra}); a documentação chega até 10 dias após a assinatura ({d02_doc10}); a migração de 24 meses de logs depende do legado ({d04_migr}); e falhas de SLA geram multa sem teto ({d01_multa}). Probabilidade 4: o slide 3 afirma que não há prorrogação do legado e o cronograma não reserva prazo entre a entrega das propostas (27/11/2026) e o início dos serviços para assinatura e transição.",
  obrigatoriedade="Informativo", natureza="Inferida", s=5, p=4,
  impacto="Lacuna de monitoramento no início do contrato, perda de logs históricos e multas desde o primeiro mês.",
  framework=ISO, controle="A.5.30 Prontidão de TIC para continuidade de negócios", associacao="Correlata",
  relacionados=["d04_siem_legado", "d01_inicio", "d01_assinatura", "d02_transicao_contra", "d02_doc10", "d04_migr", "d01_multa", "d05_qa1"],
  acao="Avaliar Go/No-Go",
  pergunta="Há previsão de carência de SLA e multas durante a transição e nos primeiros meses de operação, considerando o encerramento do SIEM legado em 31/01/2027?",
  responsavel="Delivery/Operação")

# =============================================================== D05 — Q&A e questionário
QA = 'aba "Q&A Rodada 1"'
QT = 'aba "Questionário Técnico"'
PS = 'aba "Pesos" (OCULTA)'

I("d05_inv", "D05", "Planilha inteira (4 abas)", 'abas "Instruções", "Q&A Rodada 1", "Questionário Técnico", "Pesos" (OCULTA)',
  '"Questionário Técnico e Respostas aos Esclarecimentos — RFP nº 2026-017"', "Registro de cobertura", "Administrativo do processo",
  "Inventário: 4 abas; a aba 'Pesos' está oculta e foi analisada (contém pesos e regra de dedução da Nota Técnica). Q&A com 6 perguntas e respostas de 12/11/2026; questionário com 6 requisitos (QT-01 a QT-06).",
  responsavel="Bid Manager")

I("d05_instr", "D05", "Instruções", 'aba "Instruções" · A3',
  '"Questionários incompletos serão desclassificados."', "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Questionário incompleto leva à desclassificação, sanção que a RFP, item 4.4, não prevê ({d01_questionario}). Probabilidade 5: a desclassificação é expressa no texto.",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Desclassificação.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d01_questionario", "d05_instr_amb"], acao="Atender", responsavel="Pré-venda/Arquitetura")

I("d05_instr_amb", "D05", "Instruções", 'aba "Instruções" · A3',
  '"O preenchimento de todas as abas deste arquivo é obrigatório."', "Ambiguidade", "Administrativo do processo",
  "Exige preencher 'todas as abas', mas só a aba 'Questionário Técnico' tem campos de resposta; as abas 'Q&A Rodada 1' e 'Pesos' (oculta) são do cliente. Não está claro se a aba oculta deve ser exibida, alterada ou devolvida.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Risco de questionamento formal da resposta, com sanção de desclassificação.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d05_instr"], acao="Esclarecer no Q&A",
  pergunta="Quais abas da planilha devem ser preenchidas pelo proponente? Basta preencher as colunas D e E da aba 'Questionário Técnico'?",
  responsavel="Bid Manager")

I("d05_qa1", "D05", "Q&A Rodada 1 — pergunta 1 (RFP, item 3.1)", f'{QA} · E2 (pergunta nº 1, 12/11/2026)',
  '"A data de entrega das propostas fica prorrogada para 27/11/2026, até as 18h."', "Prazo / marco", "Administrativo do processo",
  "Nova data de entrega: 27/11/2026, até as 18h. Altera a RFP, item 3.1 ({d01_entrega}). O início dos serviços (01/02/2027) não foi alterado, o que comprime o tempo para assinatura e transição.",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Prazo final de entrega da proposta.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d01_entrega", "d04_risco_transicao"], acao="Atender", responsavel="Bid Manager")

I("d05_qa2", "D05", "Q&A Rodada 1 — pergunta 2 (RFP, item 5.1 c)", f'{QA} · E3 (pergunta nº 2, 12/11/2026)',
  '"Não. O SOC deverá estar localizado em território nacional."', "Critério eliminatório / de habilitação", "Operação/Serviços / Regulatório/Compliance",
  "Confirma a exigência de SOC no Brasil da RFP, item 5.1 c ({d01_soc_nacional}), sem alterá-la. Probabilidade 5: o critério é de inabilitação expressa.",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d01_soc_nacional"], vigencia="Duplicado", acao="Atender", responsavel="Delivery/Operação")

I("d05_qa3", "D05", "Q&A Rodada 1 — pergunta 3 (Anexo I, item 1.4)", f'{QA} · E4 (pergunta nº 3, 12/11/2026)',
  'Não localizado · "A volumetria será informada somente ao proponente vencedor."', "Lacuna", "Comercial/Preço / Infraestrutura/Cloud",
  "O Banco recusa informar a volumetria de eventos por segundo antes da proposta. Licenciamento e armazenamento do SIEM, retenção de 5 anos e equipe dependem dela. Probabilidade 5: informação indispensável ao preço recusada formalmente pelo cliente.",
  obrigatoriedade="Informativo", s=4, p=5, impacto="Preço do SIEM e do armazenamento estimado sem base; risco de subprecificação ou de proposta não competitiva.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d02_integr", "d02_siem", "d02_ret5", "d04_servidores"], acao="Registrar premissa na proposta",
  pergunta="Como a volumetria não será informada antes da proposta, o Banco aceita que o proponente adote uma volumetria de referência declarada na proposta, com revisão de preço caso o volume real a exceda?",
  responsavel="Pricing/Financeiro")

I("d05_qa4", "D05", "Q&A Rodada 1 — pergunta 4 (RFP, item 7.4)", f'{QA} · E5 (pergunta nº 4, 12/11/2026)',
  '"As condições do item 7 permanecem inalteradas."', "Risco para o proponente", "Jurídico/Contratual / Financeiro",
  "Risco combinado: o pedido de teto para multas foi respondido sem limite, mantendo multa de 10% por ocorrência ({d01_multa}), responsabilidade integral e ilimitada ({d01_ilimitada}) e seguro de valor indefinido ({d01_seguro}). Probabilidade 4: o cliente já recusou na resposta 4 do Q&A um pedido de esclarecimento sobre o tema.",
  obrigatoriedade="Informativo", natureza="Inferida", s=5, p=4,
  impacto="Exposição financeira e jurídica sem limite durante 36 meses; pode inviabilizar a participação.",
  framework=CC, controle="Art. 412 — limite da cláusula penal ao valor da obrigação principal", associacao="Correlata",
  relacionados=["d01_multa", "d01_ilimitada", "d01_seguro"], acao="Avaliar Go/No-Go", responsavel="Jurídico")

I("d05_qa5", "D05", "Q&A Rodada 1 — pergunta 5 (RFP, item 2.1)", f'{QA} · E6 (pergunta nº 5, 12/11/2026)',
  '"Considerar 5.000 usuários."', "Dado de dimensionamento", "Operação/Serviços / Comercial/Preço",
  "Base de dimensionamento passa a 5.000 usuários, alterando a RFP, item 2.1 ({d01_usuarios}). Continua abaixo dos 6.200 usuários ativos e das subsidiárias do workshop ({d05_usuarios_contra}).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Base oficial de preço para o IAM, possivelmente subdimensionada.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d01_usuarios", "d05_usuarios_contra"], acao="Registrar premissa na proposta", responsavel="Pricing/Financeiro")

I("d05_usuarios_contra", "D05", "Q&A pergunta 5 × slide 2 e notas do slide 5", f'A: {QA} · E6 · B: D04, slide 2 — "Números do ambiente" e slide 5 — notas do apresentador',
  'A: "Considerar 5.000 usuários." · B: "6.200 usuários ativos" [...] "cerca de 900 usuários adicionais"', "Contradição", "Operação/Serviços / Comercial/Preço",
  "A resposta oficial (5.000) diverge do ambiente apresentado (6.200 usuários ativos + cerca de 900 das subsidiárias, cerca de 7.100). A diferença é de cerca de 42%.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Se a base real for maior, o IAM e a operação ficam subprecificados.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d05_qa5", "d04_usuarios_contra", "d04_subsid", "d01_precedencia"], vigencia="Em esclarecimento", acao="Registrar premissa na proposta",
  pergunta="Os 5.000 usuários informados na resposta 5 incluem as subsidiárias e os 6.200 usuários ativos apresentados no workshop? Haverá revisão de preço se a base real exceder 5.000?",
  responsavel="Pricing/Financeiro")

I("d05_qa6", "D05", "Q&A Rodada 1 — pergunta 6 (Anexo I, item 5.2)", f'{QA} · E7 (pergunta nº 6, 12/11/2026)',
  '"Sim, desde que em território nacional."', "Restrição", "Pessoas/Equipe",
  "Analistas N1 podem atuar remotamente no Brasil, o que altera a exigência presencial do Anexo I, item 5.2 ({d02_n1}).",
  obrigatoriedade="Mandatório", s=2, p=3, impacto="Reduz o custo de alocação presencial em São Paulo.",
  framework=ISO, controle="A.6.7 Trabalho remoto", associacao="Correlata",
  relacionados=["d02_n1"], acao="Atender", responsavel="RH/Staffing")

I("d05_rodada2", "D05", "Q&A Rodada 1", f'{QA} · A1:E7',
  'Não localizado · "Questionário Técnico e Respostas aos Esclarecimentos"', "Lacuna", "Administrativo do processo",
  "O arquivo é a 'Rodada 1', mas nem o cronograma da RFP (prazo de perguntas em 05/11/2026) nem o Q&A preveem nova rodada. As perguntas desta matriz que não couberem nessa rodada ficariam sem canal.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Ambiguidades e lacunas sem resposta passam a exigir premissas e ressalvas na proposta.",
  framework=APMP, controle="Gestão de esclarecimentos (identificador a confirmar)", associacao="Boa prática",
  relacionados=["d01_perguntas"], acao="Esclarecer no Q&A",
  pergunta="Haverá nova rodada de esclarecimentos? Qual o prazo para envio das perguntas?",
  responsavel="Bid Manager")

I("d05_qt01", "D05", "Questionário Técnico — QT-01", f'{QT} · A2:C2 (QT-01) · {PS} · B2',
  '"Possui certificação ISO/IEC 27001 com escopo que inclua os serviços de SOC?"', "Critério de avaliação / pontuação",
  "Segurança da Informação/Cyber",
  "Pergunta obrigatória de peso 3 (aba oculta), que repete o critério de habilitação da RFP, item 5.1 a ({d01_iso}). Resposta 'Não atende' também leva à inabilitação.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Pontuação no questionário; coerência com a habilitação.",
  framework=ISO, controle="Cláusula 4.3 — Determinação do escopo do SGSI", associacao="Direta",
  relacionados=["d01_iso", "d05_pesos_regra"], vigencia="Duplicado", acao="Atender", responsavel="Compliance")

I("d05_qt02", "D05", "Questionário Técnico — QT-02", f'{QT} · A3:C3 (QT-02) · {PS} · B3 e A9',
  '"Oferece integração nativa com plataforma SOAR?"', "Critério de avaliação / pontuação", "Segurança da Informação/Cyber",
  "Requisito não obrigatório de peso 1, mas 'Não atende' desconta 2 pontos da Nota Técnica pela regra da aba oculta ({d05_pesos_regra}). Probabilidade 4: a dedução é automática para cada 'Não atende' (aba 'Pesos', A9).",
  obrigatoriedade="Desejável", s=3, p=4, impacto="Perda de 2 pontos da Nota Técnica, próxima ao corte de 70%.",
  framework=CSF, controle="RS.MA — Gerenciamento de incidentes", associacao="Correlata",
  relacionados=["d05_pesos_regra", "d05_oport"], acao="Atender", responsavel="Pré-venda/Arquitetura")

I("d05_qt03", "D05", "Questionário Técnico — QT-03", f'{QT} · A4:C4 (QT-03) · {PS} · B4',
  '"Retém os logs online por no mínimo 12 meses?"', "Critério de avaliação / pontuação", "Segurança da Informação/Cyber / Infraestrutura/Cloud",
  "Pergunta obrigatória de peso 2 que acrescenta 'online' ao requisito de 12 meses do Anexo I, item 1.3, sem tratar dos 5 anos do item 1.6 ({d02_ret_amb}).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Define a camada de armazenamento online a precificar.",
  framework=ISO, controle="A.8.15 Registro de logs", associacao="Direta",
  relacionados=["d02_ret12", "d02_ret_amb", "d05_pesos_regra"], acao="Atender", responsavel="Pré-venda/Arquitetura")

I("d05_qt04", "D05", "Questionário Técnico — QT-04", f'{QT} · A5:C5 (QT-04) · {PS} · B5',
  '"Atende aos requisitos da Resolução CMN nº 4.893/2021?"', "Critério de avaliação / pontuação", "Regulatório/Compliance",
  "Pergunta obrigatória de peso 3. A norma se dirige à instituição financeira; não se define quais requisitos se aplicam ao prestador nem como comprovar. Relaciona-se com a localização de dados e a nuvem ({d02_nuvem_contra}).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Resposta sem critério objetivo pode ser contestada e afetar pontuação e conformidade.",
  framework=CMN, controle="Contratação de serviços de processamento, armazenamento de dados e computação em nuvem (identificador a confirmar)",
  associacao="Direta", relacionados=["d01_cmn_impl", "d02_nuvem_contra", "d05_pesos_regra"], acao="Esclarecer no Q&A",
  pergunta="Quais requisitos da Resolução CMN nº 4.893/2021 são aplicáveis ao proponente na pergunta QT-04 e que evidências devem acompanhar a resposta?",
  responsavel="Compliance")

I("d05_qt05", "D05", "Questionário Técnico — QT-05", f'{QT} · A6:C6 (QT-05) · {PS} · B6 e A9',
  '"Oferece serviço de threat intelligence?"', "Critério de avaliação / pontuação", "Segurança da Informação/Cyber",
  "Requisito não obrigatório de peso 2, mas 'Não atende' desconta 2 pontos da Nota Técnica pela regra da aba oculta ({d05_pesos_regra}). Probabilidade 4: dedução automática para cada 'Não atende' (aba 'Pesos', A9).",
  obrigatoriedade="Desejável", s=3, p=4, impacto="Perda de 2 pontos da Nota Técnica.",
  framework=ISO, controle="A.5.7 Inteligência de ameaças", associacao="Direta",
  relacionados=["d05_pesos_regra", "d05_oport"], acao="Atender", responsavel="Segurança/Cyber")

I("d05_qt06", "D05", "Questionário Técnico — QT-06", f'{QT} · A7:C7 (QT-06) · {PS} · B7',
  '"Possui equipe com certificações reconhecidas pelo mercado?"', "Critério de avaliação / pontuação", "Pessoas/Equipe",
  "Pergunta obrigatória de peso 2, tão vaga quanto a RFP, item 5.2 ({d01_equipe_cert}): não define certificações nem quantidade.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Critério subjetivo de pontuação.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d01_equipe_cert", "d05_pesos_regra"], acao="Esclarecer no Q&A",
  pergunta="Quais certificações e em que quantidade serão consideradas na pergunta QT-06?",
  responsavel="RH/Staffing")

I("d05_pesos_regra", "D05", "Pesos (aba oculta)", f'{PS} · A1:B7 e A9',
  '"Requisitos não obrigatórios respondidos como \'Não atende\' reduzem a Nota Técnica em 2 (dois) pontos cada."',
  "Critério de avaliação / pontuação", "Administrativo do processo",
  "Regra de pontuação escondida em aba oculta: pesos 3, 1, 2, 3, 2, 2 para QT-01 a QT-06 e dedução de 2 pontos por requisito não obrigatório respondido 'Não atende' (QT-02 e QT-05). Paradoxalmente, a dedução (2) supera o peso do QT-02 (1). Não há regra para requisitos obrigatórios respondidos 'Não atende'.",
  obrigatoriedade="Informativo", s=3, p=3, impacto="Até 4 pontos de dedução na Nota Técnica, relevantes para o corte de 70%.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d05_qt02", "d05_qt05", "d05_pesos_contra"], acao="Atender", responsavel="Bid Manager")

I("d05_pesos_contra", "D05", "Pesos (aba oculta) × RFP 6.2", f'A: {PS} · A9 · B: D01, {P4}, item 6.2',
  'A: "reduzem a Nota Técnica em 2 (dois) pontos cada" · B: "será atribuída conforme os critérios abaixo"', "Contradição", "Administrativo do processo",
  "A RFP diz que a Nota Técnica é atribuída pelos quatro critérios do item 6.2; a aba oculta acrescenta pesos do questionário e deduções que não constam da RFP. Não se sabe como os pesos do questionário entram na nota nem o que ocorre com 'Não atende' em requisito obrigatório.",
  obrigatoriedade="Informativo", s=4, p=3, impacto="Regra de pontuação incerta, que afeta a chance de passar no corte de 70%.",
  framework="—", controle="—", associacao="Não aplicável",
  relacionados=["d05_pesos_regra", "d01_soma_contra", "d01_corte"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
  pergunta="Como os pesos e a dedução de 2 pontos da aba 'Pesos' do questionário se integram aos critérios do item 6.2 da RFP? Qual a consequência de 'Não atende' em requisito obrigatório?",
  responsavel="Bid Manager")

I("d05_oport", "D05", "Questionário Técnico — QT-02 e QT-05", f'{QT} · B3 e B6 · {PS} · A9',
  '"Oferece serviço de threat intelligence?"', "Oportunidade / diferencial", "Segurança da Informação/Cyber",
  "Oferecer SOAR e threat intelligence evita a dedução de até 4 pontos e pode pontuar em 'Ferramentas e tecnologia' ({d01_c_ferr}); também ajuda a atingir a meta de redução de falsos positivos ({d04_meta_fp}).",
  obrigatoriedade="Desejável", framework=CSF, controle="DE.AE — Análise de eventos adversos", associacao="Correlata",
  relacionados=["d05_qt02", "d05_qt05", "d04_meta_fp"], acao="Precificar", responsavel="Pré-venda/Arquitetura")


def main():
    last, out = sys.argv[1], sys.argv[2]
    order = [d["codigo"] for d in DOCS]
    upto = order[: order.index(last) + 1]
    itens = [i for i in ITENS if i["doc"] in upto]
    # Só documentos já processados na lista enquanto a análise está em andamento
    docs = DOCS if last == order[-1] else [d for d in DOCS if d["codigo"] in upto]
    status = {"final": True} if last == order[-1] else {"final": False, "proximo": PROXIMO[last],
                                                        "concluidos": len(upto), "parte": len(upto)}
    keys = {i["chave"] for i in itens}
    # Referências a itens futuros ficam pendentes nas rodadas parciais
    if last != order[-1]:
        import re
        for i in itens:
            i["relacionados"] = [r for r in i.get("relacionados", []) if r in keys]
            for f in ("descricao", "pergunta", "impacto"):
                if f in i:
                    i[f] = re.sub(r"\{([A-Za-z0-9_]+)\}", lambda m: m.group(0) if m.group(1) in keys else "(item posterior)", i[f])
    json.dump({"processo": "RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Serviços gerenciados de SOC e IAM",
               "documentos": docs, "itens": itens, "status": status}, open(out, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
