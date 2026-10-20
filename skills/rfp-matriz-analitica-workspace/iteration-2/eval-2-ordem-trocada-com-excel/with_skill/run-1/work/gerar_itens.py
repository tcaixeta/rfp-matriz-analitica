# -*- coding: utf-8 -*-
"""Gera itens.json para build_matrix.py — RFP 2026-017 Banco Horizonte (SOC + IAM)."""
import json
from pathlib import Path

ISO = "ISO/IEC 27001:2022"
CC = "Código Civil (Lei 10.406/2002)"
LGPD = "LGPD (Lei 13.709/2018)"
CMN = "Resolução CMN nº 4.893/2021"
NA = dict(framework="—", controle="—", associacao="Não aplicável")

P1 = "p. 2 (impressa: 1)"
P2 = "p. 3 (impressa: 2)"
P3 = "p. 4 (impressa: 3)"
P4 = "p. 5 (impressa: 4)"
P5 = "p. 6 (impressa: 5) (OCR)"
QA = 'aba "Q&A Rodada 1"'
QT = 'aba "Questionário Técnico"'

def q(t):
    return f'"{t}"'

itens = []
def add(**k):
    for f, v in NA.items():
        k.setdefault(f, v)
    itens.append(k)

# =========================================================== D01 — RFP (PDF)
add(chave="d01_inv", doc="D01", secao="Documento inteiro (capa, seções 1 a 7 e Anexo III)", localizador="p. 1–6",
    evidencia=q("Solicitação de Proposta (RFP) nº 2026-017"), tipo="Registro de cobertura", dominio="Administrativo do processo",
    descricao="Inventário: PDF de 6 páginas, Versão 1.0 de 15/10/2026, lido integralmente. A p. 6 (impressa: 5) não tem camada de texto (imagem digitalizada do Anexo III — Declaração de Localização de Dados); foi lida visualmente e seus itens levam o localizador '(OCR)'. Documento principal: processado como D01, embora tenha sido o último arquivo enviado pelo usuário, para que o Q&A (D04) seja confrontado com o original. Cabeçalho repetido 'DOCUMENTO FICTÍCIO PARA TESTE' desconsiderado.",
    framework="—", controle="—", associacao="—", responsavel="Bid Manager")

add(chave="d01_regime", doc="D01", secao="1. APRESENTAÇÃO — 1.2", localizador=P1,
    evidencia=q("O Banco é instituição financeira autorizada a funcionar pelo Banco Central do Brasil e está sujeito à Resolução CMN nº 4.893/2021"),
    tipo="Registro de cobertura", dominio="Regulatório/Compliance",
    descricao="Regime identificado: contratação privada (sociedade anônima, sem menção a licitação, órgão público ou Lei 14.133/2021) em setor regulado pelo Banco Central do Brasil, com sujeição declarada à Resolução CMN nº 4.893/2021. Referências jurídicas usadas nesta matriz: Código Civil, LGPD e a regulação setorial citada pelo próprio documento. A Lei 14.133/2021 não se aplica.",
    framework="—", controle="—", associacao="—", responsavel="Jurídico")

add(chave="d01_cmn", doc="D01", secao="1. APRESENTAÇÃO — 1.2", localizador=P1,
    evidencia=q("requisitos para a contratação de serviços de processamento e armazenamento de dados e de computação em nuvem"),
    tipo="Requisito implícito", dominio="Regulatório/Compliance", natureza="Inferida",
    descricao="Inferência: o proponente fornecerá o SIEM, possivelmente em nuvem pública (Anexo I, 1.2), e processará logs do Banco; o próprio RFP declara que a regulação citada trata da contratação de processamento, armazenamento de dados e nuvem. Logo, é provável que o contrato traga cláusulas regulatórias repassadas ao prestador (localização de dados, acesso do regulador, comunicação de incidentes, continuidade), que o RFP não detalha. O QT-04 do questionário exige declarar atendimento à Resolução.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Obrigações regulatórias não precificadas (auditoria, relatórios, localização de dados); risco de descumprimento contratual.",
    framework=CMN, controle="Contratação de serviços de processamento, armazenamento de dados e computação em nuvem (identificador a confirmar)", associacao="Direta",
    relacionados=["d02_contr_siem", "d04_qt04"], acao="Esclarecer no Q&A",
    pergunta="Quais obrigações decorrentes da Resolução CMN nº 4.893/2021 serão repassadas à Contratada no contrato (por exemplo, acesso do Banco Central aos dados e instalações, comunicação de incidentes, local de armazenamento, plano de continuidade) e o Banco classificará este serviço como relevante para fins de comunicação ao regulador?",
    responsavel="Compliance")

add(chave="d01_soc", doc="D01", secao="2. OBJETO — 2.1", localizador=P1,
    evidencia=q("serviços gerenciados de Centro de Operações de Segurança (SOC), em regime 24x7x365"),
    tipo="Requisito funcional / de serviço", dominio="Segurança da Informação/Cyber / Operação/Serviços",
    descricao="Objeto principal: SOC gerenciado em regime ininterrupto. Detalhado no Anexo I, §1 e §2.",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Dimensionamento de equipe 24x7 e plataforma; principal componente de custo.",
    framework="NIST CSF 2.0", controle="DE.CM — Monitoramento contínuo", associacao="Direta",
    relacionados=["d02_monit"], acao="Precificar", responsavel="Delivery/Operação")

add(chave="d01_usuarios", doc="D01", secao="2. OBJETO — 2.1", localizador=P1,
    evidencia=q("gestão de identidades e acessos (IAM), abrangendo aproximadamente 4.500 colaboradores"),
    tipo="Dado de dimensionamento", dominio="Técnico/Arquitetura / Comercial/Preço",
    descricao="Quantitativo-base do serviço. Alterado pela resposta 5 do Q&A (5.000 usuários) e divergente da apresentação (6.200 usuários ativos e mais cerca de 900 das subsidiárias). 'Aproximadamente' e 'colaboradores' não esclarecem se terceiros, contas de serviço e contas privilegiadas entram na conta.",
    obrigatoriedade="Informativo", s=4, p=3, impacto="Base de preço do IAM (por identidade) e do SOC; variação de até cerca de 58% entre as fontes.",
    relacionados=["d04_q5", "d03_contr_usuarios", "d03_subsid", "d04_contr_usuarios"], vigencia="Alterado", acao="Esclarecer no Q&A",
    pergunta="Além dos colaboradores, devem ser considerados no quantitativo de identidades terceiros, prestadores, contas de serviço e contas técnicas?",
    responsavel="Pré-venda/Arquitetura")

add(chave="d01_lgpd", doc="D01", secao="2. OBJETO — 2.1", localizador=P1,
    evidencia=q("gestão de identidades e acessos (IAM), abrangendo aproximadamente 4.500 colaboradores"),
    tipo="Requisito implícito", dominio="Privacidade/Proteção de Dados", natureza="Inferida",
    descricao="Inferência: o IAM trata dados cadastrais de colaboradores (admissão, movimentação, desligamento) e o SOC processa logs que contêm identificadores pessoais (usuários, IPs, e-mails). O proponente atuará como operador de dados pessoais, mas o RFP não traz acordo de tratamento de dados, regras de suboperadores nem prazos de comunicação de incidentes com dados pessoais.",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Obrigações de operador (segurança, registro de operações, apoio ao controlador) e exposição a responsabilidade solidária.",
    framework=LGPD, controle="Art. 5º, VII (operador); Art. 39", associacao="Direta",
    relacionados=["d01_anexo3_local", "d02_logs_pos"], acao="Registrar premissa na proposta",
    pergunta="O Banco fornecerá acordo de tratamento de dados pessoais definindo as instruções ao operador, a autorização de suboperadores (por exemplo, provedor de nuvem do SIEM), prazos de comunicação de incidentes e regras de devolução ou eliminação dos dados ao fim do contrato?",
    responsavel="Jurídico")

add(chave="d01_workshop", doc="D01", secao="3. CRONOGRAMA DO PROCESSO — 3.1", localizador=P1,
    evidencia=q("Workshop de apresentação do ambiente 22/10/2026"), tipo="Prazo / marco", dominio="Administrativo do processo",
    descricao="Workshop de apresentação do ambiente. A apresentação usada (D03) traz informações e escopo que não constam do RFP nem do Anexo I.",
    obrigatoriedade="Informativo", s=2, p=3, impacto="Perda de informações de dimensionamento se o proponente não participar.",
    relacionados=["d03_inv"], acao="Atender", responsavel="Bid Manager")

add(chave="d01_perguntas", doc="D01", secao="3. CRONOGRAMA DO PROCESSO — 3.1", localizador=P1,
    evidencia=q("Prazo final para envio de perguntas 05/11/2026"), tipo="Prazo / marco", dominio="Administrativo do processo",
    descricao="Data limite para os pedidos de esclarecimento. As perguntas desta matriz precisam ser enviadas até essa data; o RFP não prevê nova rodada de Q&A.",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Contradições e lacunas sem resposta passam a ser premissas ou riscos na proposta.",
    acao="Atender", responsavel="Bid Manager")

add(chave="d01_entrega", doc="D01", secao="3. CRONOGRAMA DO PROCESSO — 3.1", localizador=P1,
    evidencia=q("Entrega das propostas 20/11/2026, até as 18h"), tipo="Prazo / marco", dominio="Administrativo do processo",
    descricao="Prazo original de entrega, prorrogado para 27/11/2026, até as 18h, pela resposta 1 do Q&A. Prevalência do Q&A depende da ordem de precedência, não definida.",
    obrigatoriedade="Mandatório", s=5, p=3, impacto="Entrega fora do prazo exclui o proponente do processo.",
    relacionados=["d04_q1", "d01_precedencia"], vigencia="Alterado", acao="Atender", responsavel="Bid Manager")

add(chave="d01_inicio", doc="D01", secao="3. CRONOGRAMA DO PROCESSO — 3.1", localizador=P1,
    evidencia=q("Início previsto dos serviços 01/02/2027"), tipo="Prazo / marco", dominio="Transição/Implantação",
    descricao="Data de início dos serviços. Coincide com o dia seguinte ao fim do contrato do SIEM legado (31/01/2027, sem prorrogação — apresentação, slide 3). Não está claro se é o início da transição ou da operação plena.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Janela de implantação rígida; descontinuidade de monitoramento se a nova plataforma não estiver operacional.",
    relacionados=["d01_assinatura", "d03_siem_legado", "d03_risco_transicao"], acao="Esclarecer no Q&A", responsavel="Delivery/Operação")

add(chave="d01_transicao", doc="D01", secao="3. CRONOGRAMA DO PROCESSO — 3.2", localizador=P1,
    evidencia=q("A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato."),
    tipo="Prazo / marco", dominio="Transição/Implantação",
    descricao="Prazo de transição de 30 dias corridos, contraditório com os 60 dias do Anexo I, item 4.1.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Equipe de implantação e operação paralela comprimidas; afeta o Plano de transição (10 pontos).",
    framework="ITIL 4", controle="Transição de serviços / gestão de implantação (identificador a confirmar)", associacao="Correlata",
    relacionados=["d02_contr_transicao", "d02_transicao60"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A", responsavel="Delivery/Operação")

add(chave="d01_assinatura", doc="D01", secao="3. CRONOGRAMA DO PROCESSO — 3.1 e 3.2", localizador=P1,
    evidencia="Não localizado · " + q("A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura"),
    tipo="Lacuna", dominio="Transição/Implantação",
    descricao="O prazo de transição corre a partir da assinatura, mas o cronograma não informa a data prevista de assinatura nem a de adjudicação. Sem ela, não é possível verificar se a transição termina antes de 01/02/2027 nem antes do fim do contrato do SIEM legado.",
    obrigatoriedade="Informativo", s=4, p=3, impacto="Impossibilidade de planejar a transição e de estimar o custo de operação paralela.",
    relacionados=["d01_inicio", "d03_risco_transicao"], acao="Esclarecer no Q&A",
    pergunta="Qual a data prevista de adjudicação e de assinatura do contrato? O 'início previsto dos serviços' em 01/02/2027 corresponde ao início da transição ou ao início da operação plena, após a transição?",
    responsavel="Bid Manager")

add(chave="d01_idioma", doc="D01", secao="4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.1", localizador=P2,
    evidencia=q("A proposta deverá ser redigida em língua portuguesa"), tipo="Instrução de resposta", dominio="Administrativo do processo",
    descricao="Idioma obrigatório da proposta. Atestados e certificados em outro idioma podem exigir tradução (não tratado no RFP).",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Proposta fora do idioma pode ser rejeitada.", acao="Atender", responsavel="Bid Manager")

add(chave="d01_portal", doc="D01", secao="4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.1", localizador=P2,
    evidencia=q("enviada exclusivamente pelo portal de fornecedores do Banco"), tipo="Instrução de resposta", dominio="Administrativo do processo",
    descricao="Único canal de entrega. O RFP não informa endereço do portal, exigência de cadastro prévio nem limite de tamanho de arquivo.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Falha de cadastro ou upload no prazo impede a participação.",
    acao="Esclarecer no Q&A",
    pergunta="Qual o endereço do portal de fornecedores, há exigência de cadastro prévio (com prazo) e há limite de tamanho ou formato dos arquivos?",
    responsavel="Bid Manager")

add(chave="d01_paginas", doc="D01", secao="4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.2", localizador=P2,
    evidencia=q("A proposta técnica deverá ter no máximo 40 (quarenta) páginas, excluídos os anexos."), tipo="Instrução de resposta", dominio="Administrativo do processo",
    descricao="Limite de extensão da proposta técnica. Não define a consequência do excesso nem o que pode ir para anexos.",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Conteúdo excedente pode ser desconsiderado na pontuação técnica.", acao="Atender", responsavel="Bid Manager")

add(chave="d01_anexo4", doc="D01", secao="4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.3", localizador=P2,
    evidencia=q("A proposta comercial deverá ser apresentada conforme a planilha modelo do Anexo IV — Planilha de Preços."),
    tipo="Instrução de resposta", dominio="Comercial/Preço",
    descricao="Formato obrigatório da proposta comercial; o modelo não foi fornecido (ver Lacuna relacionada).",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Proposta comercial fora do modelo pode ser rejeitada.",
    relacionados=["d01_anexo4_lac"], acao="Atender", responsavel="Pricing/Financeiro")

add(chave="d01_anexo4_lac", doc="D01", secao="4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.3", localizador=P2,
    evidencia="Não localizado · " + q("conforme a planilha modelo do Anexo IV — Planilha de Preços"),
    tipo="Lacuna", dominio="Comercial/Preço",
    descricao="O Anexo IV é citado pelo cliente, mas não integra o pacote recebido nem a lista de arquivos do usuário. Sem ele não se conhecem os itens de preço, unidades (por usuário, por EPS, mensal fixo), nem como reajuste e multas incidem sobre cada componente.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Impossibilidade de estruturar a proposta comercial no formato exigido.",
    relacionados=["d01_anexo4"], acao="Esclarecer no Q&A",
    pergunta="Favor disponibilizar o Anexo IV — Planilha de Preços, citado no item 4.3 da RFP e não incluído no pacote de documentos.",
    responsavel="Pricing/Financeiro", pendencia="Anexo IV — Planilha de Preços citado no item 4.3 e não fornecido")

add(chave="d01_anexo2_lac", doc="D01", secao="Numeração de anexos (4.3 e Anexo III)", localizador="p. 3 (impressa: 2) · p. 6 (impressa: 5) (OCR)",
    evidencia="Não localizado · " + q("ANEXO III — DECLARAÇÃO DE LOCALIZAÇÃO DE DADOS"),
    tipo="Lacuna", dominio="Administrativo do processo", natureza="Inferida",
    descricao="Inferência: o pacote traz Anexo I, Anexo III (p. 6) e cita Anexo IV, mas não há Anexo II nem referência a ele. Pode haver documento omitido (por exemplo, minuta de contrato ou modelo de proposta técnica).",
    obrigatoriedade="Informativo", s=2, p=3, impacto="Possível obrigação ou modelo não considerado na proposta.",
    acao="Esclarecer no Q&A",
    pergunta="Existe um Anexo II desta RFP (por exemplo, minuta de contrato)? Se sim, favor disponibilizá-lo.",
    responsavel="Bid Manager")

add(chave="d01_questionario", doc="D01", secao="4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.4", localizador=P2,
    evidencia=q("O questionário técnico (planilha anexa) deverá ser integralmente preenchido."), tipo="Instrução de resposta", dominio="Administrativo do processo",
    descricao="Preenchimento integral do questionário (D04). A aba 'Instruções' da planilha acrescenta a consequência: questionários incompletos serão desclassificados.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Questionário incompleto leva à desclassificação (conforme D04).",
    relacionados=["d04_instrucoes", "d04_instr_amb"], acao="Atender", responsavel="Pré-venda/Arquitetura")

add(chave="d01_hab_a", doc="D01", secao="5. CRITÉRIOS DE HABILITAÇÃO — 5.1 a)", localizador=P2,
    evidencia=q("certificado ISO/IEC 27001 vigente, emitido por organismo acreditado, cujo escopo inclua os serviços de SOC"),
    tipo="Critério eliminatório / de habilitação", dominio="Segurança da Informação/Cyber / Regulatório/Compliance",
    descricao="Certificação ISO/IEC 27001 com escopo cobrindo o SOC. Não exige que o escopo inclua IAM nem especifica a versão da norma. Probabilidade 5: o item 5.1 determina que 'Serão inabilitados' os que não apresentarem o certificado; o impacto decorre diretamente do texto.",
    obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação.",
    framework=ISO, controle="Cláusulas 4 a 10 (requisitos do SGSI) — certificação", associacao="Direta",
    relacionados=["d04_qt01"], acao="Atender", responsavel="Compliance")

add(chave="d01_hab_b", doc="D01", secao="5. CRITÉRIOS DE HABILITAÇÃO — 5.1 b)", localizador=P2,
    evidencia=q("no mínimo 3 (três) atestados de capacidade técnica de prestação de serviços de SOC para instituições financeiras, com ambiente de no mínimo 2.000 usuários"),
    tipo="Critério eliminatório / de habilitação", dominio="Administrativo do processo",
    descricao="Três atestados de SOC em instituições financeiras. Não está claro se cada atestado precisa comprovar 2.000 usuários ou se podem ser somados, nem se atestados de IAM são exigidos. Probabilidade 5: o item 5.1 prevê inabilitação para quem não apresentar os atestados.",
    obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação.",
    acao="Esclarecer no Q&A",
    pergunta="O mínimo de 2.000 usuários deve ser comprovado em cada um dos três atestados ou pode ser obtido pela soma? Atestados de grupos financeiros com várias entidades e de cooperativas de crédito são aceitos?",
    responsavel="Bid Manager")

add(chave="d01_hab_c", doc="D01", secao="5. CRITÉRIOS DE HABILITAÇÃO — 5.1 c)", localizador=P2,
    evidencia=q("comprovação de que o SOC está localizado em território nacional"),
    tipo="Critério eliminatório / de habilitação", dominio="Operação/Serviços / Regulatório/Compliance",
    descricao="SOC no Brasil, confirmado pela resposta 2 do Q&A. A forma de comprovação (endereço, contrato de locação, visita técnica) não é definida. Probabilidade 5: o item 5.1 prevê inabilitação para quem não comprovar.",
    obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação; impede modelo offshore ou follow-the-sun.",
    relacionados=["d04_q2"], acao="Atender",
    pergunta="Qual documento será aceito como comprovação da localização do SOC em território nacional?",
    responsavel="Delivery/Operação")

add(chave="d01_equipe_cert", doc="D01", secao="5. CRITÉRIOS DE HABILITAÇÃO — 5.2", localizador=P2,
    evidencia=q("O proponente deverá possuir equipe técnica devidamente certificada."), tipo="Ambiguidade", dominio="Pessoas/Equipe",
    descricao="Está sob o título de habilitação, mas fora do rol 'Serão inabilitados' do 5.1, e não define quais certificações, para quais perfis, em que quantidade nem como comprovar. O Anexo I exige CISSP só para o coordenador; o QT-06 repete a exigência de forma genérica.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Risco de inabilitação ou de perda de pontos em 'Qualificação da equipe' (20 pontos) por critério subjetivo.",
    framework=ISO, controle="Cláusula 7.2 — Competência", associacao="Correlata",
    relacionados=["d02_cissp", "d04_qt06"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="O item 5.2 é critério de inabilitação? Quais certificações, para quais perfis e em que quantidade serão aceitas, e como devem ser comprovadas na proposta?",
    responsavel="RH/Staffing")

add(chave="d01_pesos_nota", doc="D01", secao="6. CRITÉRIOS DE AVALIAÇÃO — 6.1", localizador=P3,
    evidencia=q("A nota final será composta pela Nota Técnica (peso de 60%) e pela Nota de Preço (peso de 40%)."),
    tipo="Critério de avaliação / pontuação", dominio="Administrativo do processo",
    descricao="Técnica e preço com pesos 60/40: orienta a estratégia de preço.",
    obrigatoriedade="Informativo", s=3, p=3, impacto="Define o equilíbrio entre investimento técnico e preço.", acao="Nenhuma (informativo)", responsavel="Bid Manager")

add(chave="d01_formula_preco", doc="D01", secao="6. CRITÉRIOS DE AVALIAÇÃO — 6.1", localizador=P3,
    evidencia="Não localizado · " + q("pela Nota de Preço (peso de 40%)"), tipo="Lacuna", dominio="Comercial/Preço",
    descricao="O RFP não define a fórmula da Nota de Preço nem o valor comparado (mensal, global de 36 meses, com ou sem reajuste).",
    obrigatoriedade="Informativo", s=4, p=3, impacto="Impossibilidade de simular a nota final e calibrar o preço.",
    acao="Esclarecer no Q&A",
    pergunta="Qual a fórmula da Nota de Preço (por exemplo, proporcional ao menor preço) e qual valor será comparado (mensal, global de 36 meses, com ou sem itens opcionais)?",
    responsavel="Pricing/Financeiro")

for k, crit, pts, extra in [
    ("d01_crit_met", "Metodologia de operação do SOC 20", 20, "Critério subjetivo, sem subcritérios publicados."),
    ("d01_crit_eq", "Qualificação da equipe 20", 20, "Sem definição de como certificações e experiência são pontuadas (ver 5.2)."),
    ("d01_crit_ferr", "Ferramentas e tecnologia 15", 15, "Sem subcritérios; SOAR e threat intelligence aparecem só no questionário (QT-02 e QT-05)."),
    ("d01_crit_trans", "Plano de transição 10", 10, "O prazo de transição é contraditório (30 × 60 dias)."),
]:
    add(chave=k, doc="D01", secao="6. CRITÉRIOS DE AVALIAÇÃO — 6.2", localizador=P3, evidencia=q(crit),
        tipo="Critério de avaliação / pontuação", dominio="Administrativo do processo",
        descricao=f"Critério da Nota Técnica com pontuação máxima de {pts}. {extra}",
        obrigatoriedade="Informativo", s=3, p=3, impacto=f"Até {pts} pontos da Nota Técnica.",
        relacionados=["d01_contr_pontos"], acao="Atender", responsavel="Pré-venda/Arquitetura")

add(chave="d01_contr_pontos", doc="D01", secao="6. CRITÉRIOS DE AVALIAÇÃO — 6.2 e 6.3", localizador=P3,
    evidencia="A: " + q("A Nota Técnica, de no máximo 60 (sessenta) pontos") + " · B: " + q("Metodologia de operação do SOC 20") + " + " + q("Qualificação da equipe 20") + " + " + q("Ferramentas e tecnologia 15") + " + " + q("Plano de transição 10"),
    tipo="Contradição", dominio="Administrativo do processo",
    descricao="A soma das pontuações máximas da tabela é 65, acima do teto de 60 pontos. Afeta o corte do item 6.3 (70% = 42 de 60 ou 45,5 de 65) e a conversão para o peso de 60%.",
    obrigatoriedade="Informativo", s=4, p=3, impacto="Incerteza sobre a nota mínima para não ser desclassificado e sobre o peso relativo de cada critério.",
    relacionados=["d01_crit_met", "d01_crit_eq", "d01_crit_ferr", "d01_crit_trans", "d01_corte", "d04_contr_pontuacao"],
    vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="A soma dos critérios da tabela do item 6.2 é 65 pontos, mas a Nota Técnica tem máximo de 60. Qual pontuação está correta e como será aplicado o corte de 70% do item 6.3?",
    responsavel="Bid Manager")

add(chave="d01_corte", doc="D01", secao="6. CRITÉRIOS DE AVALIAÇÃO — 6.3", localizador=P3,
    evidencia=q("Serão desclassificadas as propostas com Nota Técnica inferior a 70% (setenta por cento) da pontuação máxima."),
    tipo="Critério eliminatório / de habilitação", dominio="Administrativo do processo",
    descricao="Nota técnica mínima. O valor de referência é incerto (60 ou 65 pontos) e a aba oculta 'Pesos' do questionário prevê descontos que podem levar a proposta abaixo do corte.",
    obrigatoriedade="Mandatório", s=5, p=3, impacto="Desclassificação.",
    relacionados=["d01_contr_pontos", "d04_pesos"], acao="Atender", responsavel="Bid Manager")

add(chave="d01_empate", doc="D01", secao="6. CRITÉRIOS DE AVALIAÇÃO — 6.4", localizador=P3,
    evidencia=q("Em caso de empate na nota final, prevalecerá a proposta de menor preço."), tipo="Critério de avaliação / pontuação", dominio="Administrativo do processo",
    descricao="Critério de desempate por preço. Probabilidade 2: depende de empate exato na nota final ponderada, situação pouco provável.", obrigatoriedade="Informativo", s=2, p=2, impacto="Relevante apenas em empate.",
    acao="Nenhuma (informativo)", responsavel="Bid Manager")

add(chave="d01_vigencia", doc="D01", secao="7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.1", localizador=P4,
    evidencia=q("O contrato terá vigência de 36 (trinta e seis) meses, prorrogável por iguais períodos mediante acordo entre as partes."),
    tipo="Obrigação contratual", dominio="Jurídico/Contratual / Comercial/Preço",
    descricao="Prazo contratual de 36 meses: horizonte de amortização de licenças e da transição. O prazo de retenção de logs de 5 anos (Anexo I, 1.6) ultrapassa a vigência.",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Define amortização de investimentos iniciais e de licenças.",
    relacionados=["d02_logs_pos"], acao="Precificar", responsavel="Pricing/Financeiro")

add(chave="d01_reajuste", doc="D01", secao="7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.2", localizador=P4,
    evidencia=q("Os preços serão reajustados anualmente pela variação do IPCA."), tipo="Obrigação contratual", dominio="Comercial/Preço / Financeiro",
    descricao="Reajuste anual por IPCA, sem data-base definida. Custos de licenças e nuvem do SIEM costumam estar atrelados a moeda estrangeira, o que o IPCA não cobre.",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Exposição cambial e de inflação setorial não repassável.",
    acao="Registrar premissa na proposta",
    pergunta="Qual a data-base do reajuste (data da proposta ou da assinatura)? Haverá previsão de reequilíbrio para custos atrelados a moeda estrangeira (licenças e nuvem do SIEM)?",
    responsavel="Pricing/Financeiro")

add(chave="d01_pagamento", doc="D01", secao="7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.3", localizador=P4,
    evidencia=q("O pagamento será efetuado em até 60 (sessenta) dias após o aceite da nota fiscal."), tipo="Obrigação contratual", dominio="Financeiro",
    descricao="Prazo de pagamento de 60 dias contado do aceite, cujo prazo não é definido; o recebimento efetivo pode passar de 60 dias após a emissão.",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Custo financeiro de capital de giro a precificar.",
    acao="Esclarecer no Q&A", pergunta="Qual o prazo máximo para o aceite da nota fiscal após a sua emissão e quais as condições para recusa?",
    responsavel="Pricing/Financeiro")

add(chave="d01_multa", doc="D01", secao="7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.4", localizador=P4,
    evidencia=q("O descumprimento de qualquer nível de serviço (SLA) previsto no Anexo I sujeitará a Contratada a multa de 10% (dez por cento) do valor mensal do contrato, por ocorrência."),
    tipo="Penalidade / multa / glosa", dominio="Jurídico/Contratual / Comercial/Preço",
    descricao="Multa fixa de 10% do valor mensal por ocorrência, sem gradação por gravidade do SLA, sem teto mensal ou global e sem carência na transição: dez ocorrências no mês igualam o faturamento mensal. Probabilidade 4: a multa incide automaticamente 'por ocorrência' e o cliente, perguntado se as multas têm limite (Q&A nº 4), respondeu que as condições do item 7 permanecem inalteradas.",
    obrigatoriedade="Mandatório", s=5, p=4, impacto="Exposição financeira ilimitada; pode superar a receita do contrato.",
    framework=CC, controle="Art. 412 (limite da cláusula penal ao valor da obrigação principal)", associacao="Correlata",
    relacionados=["d04_q4", "d02_sla_escopo", "d03_risco_transicao"], acao="Propor exceção/ressalva",
    pergunta="Será aceito teto para as multas (percentual do valor mensal e do valor global), gradação conforme a gravidade do SLA descumprido e carência durante a transição?",
    responsavel="Jurídico")

add(chave="d01_resp", doc="D01", secao="7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.5", localizador=P4,
    evidencia=q("A Contratada responderá de forma integral e ilimitada por quaisquer danos decorrentes de incidentes de segurança ocorridos no ambiente do Contratante."),
    tipo="Obrigação contratual", dominio="Jurídico/Contratual",
    descricao="Responsabilidade ilimitada por qualquer incidente no ambiente do cliente, sem exigir nexo com falha da Contratada e sem excluir danos indiretos ou lucros cessantes. A resposta 4 do Q&A manteve inalterado todo o item 7.",
    obrigatoriedade="Mandatório", s=5, p=3, impacto="Exposição jurídica e financeira ilimitada; pode inviabilizar seguro e a própria participação.",
    framework=CC, controle="Responsabilidade civil contratual e limitação de responsabilidade (identificador a confirmar)", associacao="Correlata",
    relacionados=["d04_q4", "d01_seguro"], acao="Avaliar Go/No-Go",
    pergunta="A responsabilidade do item 7.5 se limita a danos causados por ação ou omissão comprovada da Contratada? Será aceito teto de responsabilidade (por exemplo, múltiplo do valor anual) e exclusão de danos indiretos e lucros cessantes?",
    responsavel="Jurídico")

add(chave="d01_seguro", doc="D01", secao="7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.6", localizador=P4,
    evidencia=q("seguro de responsabilidade civil cibernética em valor compatível com os riscos do contrato"), tipo="Ambiguidade", dominio="Jurídico/Contratual / Financeiro",
    descricao="Obrigação de manter seguro cibernético sem valor mínimo definido. Com responsabilidade ilimitada (7.5), nenhum valor é objetivamente 'compatível'.",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Custo de prêmio indefinido; risco de questionamento do valor contratado.",
    relacionados=["d01_resp"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="Qual o valor mínimo de cobertura do seguro de responsabilidade civil cibernética e o Banco deve figurar como segurado adicional ou beneficiário?",
    responsavel="Jurídico")

add(chave="d01_subcontrat", doc="D01", secao="7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.7", localizador=P4,
    evidencia=q("É vedada a subcontratação, total ou parcial, do objeto deste contrato."), tipo="Restrição", dominio="Jurídico/Contratual",
    descricao="Vedação total de subcontratação. Conflita potencialmente com o SIEM em nuvem pública (Anexo I, 1.2) e com o uso de fornecedores de licenças, feeds de threat intelligence ou especialistas terceiros.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Pode impedir o modelo de entrega com parceiros e plataformas de terceiros.",
    relacionados=["d02_amb_subcontrat"], acao="Esclarecer no Q&A", responsavel="Jurídico")

add(chave="d01_confid", doc="D01", secao="7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.8", localizador=P4,
    evidencia=q("As obrigações de confidencialidade vigorarão por 5 (cinco) anos após o término do contrato."), tipo="Obrigação contratual", dominio="Jurídico/Contratual",
    descricao="Confidencialidade pós-contratual de 5 anos.", obrigatoriedade="Mandatório", s=2, p=3, impacto="Obrigação de longo prazo, absorvível.",
    framework=ISO, controle="A.6.6 — Acordos de confidencialidade ou de não divulgação", associacao="Correlata",
    acao="Atender", responsavel="Jurídico")

add(chave="d01_anexo3_decl", doc="D01", secao="Anexo III — Declaração de Localização de Dados", localizador=P5,
    evidencia=q("Esta declaração deverá ser entregue assinada pelo representante legal do proponente junto com a proposta, sob pena de inabilitação."),
    tipo="Critério eliminatório / de habilitação", dominio="Administrativo do processo / Regulatório/Compliance",
    descricao="Critério eliminatório que consta apenas da página digitalizada (sem texto pesquisável) e não está no rol do item 5.1. Probabilidade 5: o texto prevê inabilitação direta para quem não entregar a declaração assinada.",
    obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação.",
    relacionados=["d01_anexo3_local"], acao="Atender", responsavel="Jurídico")

add(chave="d01_anexo3_local", doc="D01", secao="Anexo III — Declaração de Localização de Dados", localizador=P5,
    evidencia=q("todos os dados do Banco Horizonte Fictício S.A., incluindo os registros (logs) de segurança, serão armazenados e processados exclusivamente em território nacional, durante toda a vigência do contrato."),
    tipo="Restrição", dominio="Infraestrutura/Cloud / Regulatório/Compliance",
    descricao="Localização exclusiva no Brasil de armazenamento e processamento, inclusive dos logs. Restringe região de nuvem do SIEM, backups, ferramentas SaaS de análise e suporte do fabricante a partir do exterior. Contradiz o Anexo I, 1.2 ('região de livre escolha'). Não cobre o período posterior à vigência, embora os logs devam ser mantidos por 5 anos.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Limita a escolha de plataforma e pode elevar custos de nuvem; declaração falsa gera inabilitação ou rescisão.",
    framework=f"{LGPD} · {CMN}", controle="Arts. 33 a 36 da LGPD (transferência internacional) · localização de dados na Resolução CMN (identificador a confirmar)", associacao="Correlata",
    relacionados=["d02_contr_siem", "d01_cmn"], acao="Atender", responsavel="Pré-venda/Arquitetura")

add(chave="d01_precedencia", doc="D01", secao="Documento inteiro (seções 1 a 7)", localizador="p. 1–6",
    evidencia="Não localizado · " + q("As especificações técnicas detalhadas constam do Anexo I — Especificação Técnica."),
    tipo="Lacuna", dominio="Jurídico/Contratual",
    descricao="Não há cláusula de ordem de precedência entre RFP, Anexos, apresentação do workshop, respostas do Q&A e questionário. Há conflitos diretos entre esses documentos (transição 30 × 60 dias; usuários 4.500 × 5.000 × 6.200; região do SIEM × Anexo III; analistas presenciais × remotos), e não se pode presumir que o Q&A, por ser o mais recente, prevaleça, nem que a apresentação e suas notas sejam vinculantes.",
    obrigatoriedade="Informativo", s=4, p=3, impacto="Incerteza sobre qual obrigação valerá no contrato; risco de disputa sobre escopo e prazo.",
    framework=CC, controle="Interpretação e integração dos documentos contratuais (identificador a confirmar)", associacao="Correlata",
    relacionados=["d02_contr_transicao", "d02_contr_siem", "d04_contr_usuarios", "d04_q6"], acao="Esclarecer no Q&A",
    pergunta="Qual a ordem de precedência entre RFP, Anexo I, Anexo III, Anexo IV, apresentação do workshop de 22/10/2026 (inclusive notas), respostas do Q&A e questionário técnico? As respostas do Q&A e o conteúdo da apresentação integrarão o contrato?",
    responsavel="Jurídico")

# =========================================================== D02 — Anexo I (DOCX)
S1 = "§ 1. SERVIÇOS DE SOC"
S2 = "§ 2. NÍVEIS DE SERVIÇO (SLA)"
S3 = "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM)"
S4 = "§ 4. TRANSIÇÃO"
S5 = "§ 5. EQUIPE"
S6 = "§ 6. RESPONSABILIDADES DO CONTRATANTE"

add(chave="d02_inv", doc="D02", secao="Documento inteiro (seções 1 a 6)", localizador="§ 1 a § 6 (Word, sem paginação fixa)",
    evidencia=q("Anexo I — Especificação Técnica"), tipo="Registro de cobertura", dominio="Administrativo do processo",
    descricao="Inventário: Word com 6 seções numeradas (22 parágrafos, sem tabelas), Versão 1.0 de 15/10/2026, lido integralmente. A extração não sinalizou marcas de revisão, comentários nem texto oculto. Localizador por seção e item.",
    framework="—", controle="—", associacao="—", responsavel="Bid Manager")

add(chave="d02_monit", doc="D02", secao="1. SERVIÇOS DE SOC — 1.1", localizador=f"{S1} · item 1.1",
    evidencia=q("O proponente deverá prestar serviço de monitoramento contínuo de eventos de segurança, em regime 24x7x365."),
    tipo="Requisito funcional / de serviço", dominio="Segurança da Informação/Cyber / Operação/Serviços",
    descricao="Monitoramento contínuo; consistente com o objeto da RFP (2.1).", obrigatoriedade="Mandatório", s=3, p=3,
    impacto="Escala 24x7 de analistas e plataforma.", framework=ISO, controle="A.8.16 — Atividades de monitoramento", associacao="Direta",
    relacionados=["d01_soc"], acao="Precificar", responsavel="Delivery/Operação")

add(chave="d02_siem", doc="D02", secao="1. SERVIÇOS DE SOC — 1.2", localizador=f"{S1} · item 1.2",
    evidencia=q("O proponente deverá fornecer a solução de SIEM"), tipo="Requisito funcional / de serviço", dominio="Técnico/Arquitetura / Comercial/Preço",
    descricao="O proponente fornece e licencia o SIEM. O licenciamento costuma depender de volumetria (EPS ou GB/dia), que o cliente se recusou a informar (Q&A nº 3).",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Custo de licença e infraestrutura sem base de volumetria.",
    framework=ISO, controle="A.8.15 — Registro de eventos (logging)", associacao="Correlata",
    relacionados=["d04_q3", "d02_contr_siem"], acao="Precificar", responsavel="Pré-venda/Arquitetura")

add(chave="d02_contr_siem", doc="D02", secao="1. SERVIÇOS DE SOC — 1.2 × RFP, Anexo III", localizador=f"A: {S1} · item 1.2 · B: D01 {P5}",
    evidencia="A: " + q("podendo esta ser disponibilizada em nuvem pública, em região de livre escolha do proponente") + " · B: " + q("serão armazenados e processados exclusivamente em território nacional"),
    tipo="Contradição", dominio="Infraestrutura/Cloud / Regulatório/Compliance",
    descricao="O Anexo I permite região de nuvem livre, mas a declaração eliminatória do Anexo III exige armazenamento e processamento exclusivos no Brasil. Escolher região estrangeira tornaria falsa a declaração. A diferença de custo e de oferta de SIEM SaaS entre regiões no Brasil e no exterior é relevante.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Escolha de arquitetura e de fornecedor de SIEM; risco de inabilitação ou de rescisão.",
    framework=CMN, controle="Localização de dados e contratação de nuvem (identificador a confirmar)", associacao="Correlata",
    relacionados=["d02_siem", "d01_anexo3_local", "d01_anexo3_decl", "d01_precedencia"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="Confirmam que, apesar do item 1.2 do Anexo I ('região de livre escolha'), o SIEM e todos os logs devem ser hospedados e processados exclusivamente em região de nuvem ou data center no Brasil, conforme o Anexo III? Isso inclui backups e acesso de suporte do fabricante a partir do exterior?",
    responsavel="Pré-venda/Arquitetura")

add(chave="d02_amb_subcontrat", doc="D02", secao="1. SERVIÇOS DE SOC — 1.2 × RFP 7.7", localizador=f"A: {S1} · item 1.2 · B: D01 {P4}, item 7.7",
    evidencia="A: " + q("podendo esta ser disponibilizada em nuvem pública") + " · B: " + q("É vedada a subcontratação, total ou parcial, do objeto deste contrato."),
    tipo="Ambiguidade", dominio="Jurídico/Contratual / Infraestrutura/Cloud", natureza="Inferida",
    descricao="Inferência: hospedar o SIEM em nuvem pública ou usá-lo como SaaS envolve terceiro na execução do objeto. Não está claro se isso, licenças de software e feeds de inteligência de terceiros contam como subcontratação vedada.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Pode inviabilizar o modelo SaaS/nuvem ou gerar alegação de descumprimento.",
    relacionados=["d01_subcontrat"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="A contratação de provedor de nuvem pública, de SIEM em modelo SaaS, de licenças de software e de feeds de inteligência de ameaças de terceiros é considerada subcontratação vedada pelo item 7.7 da RFP?",
    responsavel="Jurídico")

add(chave="d02_ret12", doc="D02", secao="1. SERVIÇOS DE SOC — 1.3", localizador=f"{S1} · item 1.3",
    evidencia=q("Os registros (logs) de segurança deverão ser retidos por no mínimo 12 (doze) meses."), tipo="Requisito não funcional", dominio="Segurança da Informação/Cyber / Infraestrutura/Cloud",
    descricao="Retenção mínima de 12 meses; conflita com os 5 anos do item 1.6.", obrigatoriedade="Mandatório", s=3, p=3,
    impacto="Armazenamento do SIEM.", framework=ISO, controle="A.8.15 — Registro de eventos (logging)", associacao="Direta",
    relacionados=["d02_contr_logs"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura")

add(chave="d02_integracao", doc="D02", secao="1. SERVIÇOS DE SOC — 1.4", localizador=f"{S1} · item 1.4",
    evidencia=q("O SIEM deverá ser integrado a todos os ativos relevantes do Contratante."), tipo="Ambiguidade", dominio="Técnico/Arquitetura",
    descricao="'Ativos relevantes' não é definido. A apresentação traz 850 servidores, 2 data centers e 2 nuvens, mas nada sobre ativos de rede, endpoints, aplicações e bancos de dados; a volumetria foi recusada (Q&A nº 3).",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Esforço de integração e volume de logs indefinidos; escopo aberto.",
    framework=ISO, controle="A.8.16 — Atividades de monitoramento", associacao="Correlata",
    relacionados=["d04_q3", "d03_servidores", "d03_nuvens"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="Qual a lista ou o critério de 'ativos relevantes' a integrar ao SIEM, com tipos e quantidades (servidores, ativos de rede, firewalls, endpoints, aplicações, bancos de dados, contas de nuvem)? Quem desenvolve conectores para sistemas proprietários?",
    responsavel="Pré-venda/Arquitetura")

add(chave="d02_resposta", doc="D02", secao="1. SERVIÇOS DE SOC — 1.5", localizador=f"{S1} · item 1.5",
    evidencia=q("O serviço deverá contemplar resposta a incidentes, incluindo contenção, erradicação"), tipo="Requisito funcional / de serviço", dominio="Segurança da Informação/Cyber",
    descricao="Resposta ativa a incidentes. Não define se a contenção e a erradicação são executadas pela Contratada nos ativos do Banco (com acesso privilegiado) ou só orientadas, nem se há atuação presencial. Execução direta aumenta a exposição à responsabilidade ilimitada do 7.5.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Escopo e responsabilidade da resposta a incidentes; equipe de IR.",
    framework=ISO, controle="A.5.26 — Resposta a incidentes de segurança da informação", associacao="Direta",
    relacionados=["d01_resp"], acao="Esclarecer no Q&A",
    pergunta="A contenção e a erradicação serão executadas pela Contratada diretamente nos ativos do Banco ou apenas orientadas à equipe do Banco? Há necessidade de atendimento presencial em incidentes, e em quais localidades?",
    responsavel="Segurança/Cyber")

add(chave="d02_pos_incidente", doc="D02", secao="1. SERVIÇOS DE SOC — 1.5", localizador=f"{S1} · item 1.5",
    evidencia=q("elaboração de relatório pós-incidente"), tipo="Entregável", dominio="Segurança da Informação/Cyber",
    descricao="Relatório pós-incidente; prazo e conteúdo mínimo não definidos.", obrigatoriedade="Mandatório", s=2, p=3,
    impacto="Esforço de documentação por incidente.", framework=ISO, controle="A.5.27 — Aprendizado com incidentes de segurança da informação", associacao="Correlata",
    acao="Atender", responsavel="Segurança/Cyber")

add(chave="d02_contr_logs", doc="D02", secao="1. SERVIÇOS DE SOC — 1.3 × 1.6", localizador=f"{S1} · itens 1.3 e 1.6",
    evidencia="A: " + q("deverão ser retidos por no mínimo 12 (doze) meses") + " · B: " + q("Para fins de auditoria, os logs deverão ser mantidos por 5 (cinco) anos."),
    tipo="Contradição", dominio="Infraestrutura/Cloud / Regulatório/Compliance",
    descricao="Dois prazos de retenção para os mesmos logs. Só se conciliam se 12 meses forem de retenção online e 5 anos de arquivamento, o que não está escrito (o QT-03 fala em 'online por no mínimo 12 meses'). Também se tipifica como Ambiguidade. O armazenamento por 5 anos multiplica o custo e ultrapassa a vigência de 36 meses.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Custo de armazenamento até cerca de 5 vezes maior; obrigação além do prazo contratual.",
    framework=ISO, controle="A.8.15 — Registro de eventos (logging)", associacao="Direta",
    relacionados=["d02_ret12", "d04_qt03", "d03_migracao", "d02_logs_pos"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="Confirmam que a retenção é de 12 meses online (pesquisável no SIEM) e de 5 anos em arquivamento? A retenção de 5 anos vale para todos os logs coletados ou só para os de segurança?",
    responsavel="Pré-venda/Arquitetura")

add(chave="d02_logs_pos", doc="D02", secao="1. SERVIÇOS DE SOC — 1.6", localizador=f"{S1} · item 1.6",
    evidencia="Não localizado · " + q("Para fins de auditoria, os logs deverão ser mantidos por 5 (cinco) anos."), tipo="Lacuna", dominio="Jurídico/Contratual / Privacidade/Proteção de Dados",
    descricao="Os logs devem durar 5 anos, mas o contrato tem 36 meses e o Anexo III cobre só a vigência. Não há regra para devolução dos logs ao Banco, custódia após o término ou eliminação.",
    obrigatoriedade="Informativo", s=3, p=3, impacto="Custo de custódia pós-contrato ou de exportação não previsto; obrigação de eliminação de dados pessoais.",
    framework=LGPD, controle="Arts. 15 e 16 (término do tratamento e eliminação)", associacao="Correlata",
    relacionados=["d02_contr_logs", "d01_vigencia", "d01_lgpd"], acao="Esclarecer no Q&A",
    pergunta="Ao término do contrato, os logs ainda dentro do prazo de 5 anos devem ser exportados para o Banco (em que formato) ou mantidos pela Contratada (com que remuneração)?",
    responsavel="Jurídico")

add(chave="d02_sla15", doc="D02", secao="2. NÍVEIS DE SERVIÇO (SLA) — 2.1", localizador=f"{S2} · item 2.1",
    evidencia=q("Tempo máximo para início do tratamento de incidentes críticos: 15 (quinze) minutos."), tipo="SLA / KPI", dominio="Operação/Serviços / Segurança da Informação/Cyber",
    descricao="SLA de 15 minutos, 24x7. 'Início do tratamento' não é definido (alerta, triagem, contato com o cliente) e 'incidente crítico' depende da matriz do Contratante, não fornecida. Cada descumprimento gera multa de 10% do valor mensal.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Dimensionamento de turno; exposição a multa por ocorrência.",
    framework="ITIL 4", controle="Prática de gerenciamento de incidentes", associacao="Correlata",
    relacionados=["d02_matriz", "d01_multa"], acao="Esclarecer no Q&A",
    pergunta="Qual evento marca o início e o fim da contagem do SLA de 15 minutos (geração do alerta, triagem, comunicação ao Banco)?",
    responsavel="Delivery/Operação")

add(chave="d02_disp", doc="D02", secao="2. NÍVEIS DE SERVIÇO (SLA) — 2.2", localizador=f"{S2} · item 2.2",
    evidencia=q("Disponibilidade mínima mensal da plataforma SIEM: 99,9%."), tipo="SLA / KPI", dominio="Infraestrutura/Cloud",
    descricao="Cerca de 43 minutos de indisponibilidade por mês. Não exclui janelas de manutenção nem falhas do provedor de nuvem ou da conectividade do Banco.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Arquitetura redundante; multa por ocorrência.",
    framework="ISO/IEC 20000-1", controle="Gestão da disponibilidade do serviço (identificador a confirmar)", associacao="Correlata",
    relacionados=["d01_multa"], acao="Registrar premissa na proposta",
    pergunta="Janelas de manutenção programada e indisponibilidades causadas pelo Banco ou por sua conectividade serão excluídas do cálculo de disponibilidade?",
    responsavel="Pré-venda/Arquitetura")

add(chave="d02_relatorio", doc="D02", secao="2. NÍVEIS DE SERVIÇO (SLA) — 2.3", localizador=f"{S2} · item 2.3",
    evidencia=q("Relatório mensal de indicadores, a ser entregue até o 5º dia útil do mês subsequente."), tipo="SLA / KPI", dominio="Operação/Serviços",
    descricao="Entregável mensal com prazo; por estar na seção de SLA, o atraso pode gerar multa de 10%. Conteúdo do relatório não definido.",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Esforço de relatório; exposição a multa por atraso.",
    relacionados=["d02_sla_escopo"], acao="Atender", responsavel="Delivery/Operação")

add(chave="d02_matriz", doc="D02", secao="2. NÍVEIS DE SERVIÇO (SLA) — 2.4", localizador=f"{S2} · item 2.4",
    evidencia="Não localizado · " + q("A classificação de criticidade dos incidentes seguirá a matriz de classificação do Contratante."), tipo="Lacuna", dominio="Segurança da Informação/Cyber",
    descricao="Documento do cliente citado e não fornecido. Sem a matriz não se sabe quantos incidentes serão 'críticos' e, portanto, sujeitos ao SLA de 15 minutos; o cliente poderia alterá-la unilateralmente.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Volume de incidentes sob SLA crítico e exposição a multas indefinidos.",
    framework=ISO, controle="A.5.25 — Avaliação e decisão sobre eventos de segurança da informação", associacao="Direta",
    relacionados=["d02_sla15"], acao="Esclarecer no Q&A",
    pergunta="Favor disponibilizar a matriz de classificação de criticidade de incidentes do Contratante e informar se ela poderá ser alterada durante o contrato e com que aviso prévio.",
    responsavel="Segurança/Cyber", pendencia="matriz de classificação de incidentes do Contratante citada no Anexo I, 2.4, e não fornecida")

add(chave="d02_sla_escopo", doc="D02", secao="2. NÍVEIS DE SERVIÇO (SLA) × RFP 7.4", localizador=f"D01 {P4}, item 7.4 · {S2} e {S3}",
    evidencia="A: " + q("qualquer nível de serviço (SLA) previsto no Anexo I") + " · B: " + q("revogação dos acessos de colaboradores desligados em até 24 (vinte e quatro) horas"),
    tipo="Ambiguidade", dominio="Jurídico/Contratual / Operação/Serviços",
    descricao="A multa do 7.4 alcança 'qualquer' SLA do Anexo I, mas o Anexo I tem prazos também fora da seção 2 (revogação em 24 h, recertificação trimestral, retenção de logs). Não há metodologia nem período de apuração. Se cada desligamento não revogado em 24 h for 'ocorrência', a exposição cresce com o turnover.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Base de incidência das multas indefinida.",
    relacionados=["d01_multa", "d02_revog", "d02_relatorio"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="Quais indicadores do Anexo I são SLA para fins do item 7.4 da RFP (apenas os da seção 2 ou também os prazos das seções 1 e 3, como a revogação de acessos em 24 horas)? Qual a metodologia e o período de apuração de cada um?",
    responsavel="Delivery/Operação")

add(chave="d02_iam_ciclo", doc="D02", secao="3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.1", localizador=f"{S3} · item 3.1",
    evidencia=q("Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"), tipo="Requisito funcional / de serviço", dominio="Segurança da Informação/Cyber",
    descricao="Ciclo de vida das identidades (joiner/mover/leaver).", obrigatoriedade="Mandatório", s=3, p=3,
    impacto="Operação de IAM e integrações com sistemas-alvo.", framework=ISO, controle="A.5.16 — Gestão de identidades", associacao="Direta",
    relacionados=["d02_iam_ferr"], acao="Precificar", responsavel="Delivery/Operação")

add(chave="d02_iam_ferr", doc="D02", secao="3. GESTÃO DE IDENTIDADES E ACESSOS (IAM)", localizador=f"{S3} · itens 3.1 a 3.4",
    evidencia=q("Gestão do ciclo de vida das identidades"), tipo="Ambiguidade", dominio="Técnico/Arquitetura / Comercial/Preço", natureza="Inferida",
    descricao="Inferência: para o SOC o Anexo I diz que o proponente fornece o SIEM, mas para o IAM não diz se a Contratada fornece e licencia uma plataforma de governança de identidades ou só opera as ferramentas atuais (Active Directory e scripts internos, segundo a apresentação). Também não informa quantos sistemas-alvo devem ser integrados.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Diferença relevante de preço (licenças e implantação de IGA) e de prazo de transição.",
    relacionados=["d02_iam_ciclo", "d03_iam_atual"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="Para o IAM, a Contratada deve fornecer e licenciar uma plataforma de governança de identidades ou operar as ferramentas atuais do Banco (Active Directory e scripts internos)? Quantos e quais sistemas-alvo devem ser integrados ao ciclo de vida?",
    responsavel="Pré-venda/Arquitetura")

add(chave="d02_revog", doc="D02", secao="3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.1", localizador=f"{S3} · item 3.1",
    evidencia=q("revogação dos acessos de colaboradores desligados em até 24 (vinte e quatro) horas"), tipo="SLA / KPI", dominio="Segurança da Informação/Cyber",
    descricao="Prazo de revogação de 24 h, dependente de comunicação tempestiva do RH do Banco, que não consta das responsabilidades do Contratante (seção 6).",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Possível multa por desligamento não revogado a tempo.",
    framework=ISO, controle="A.5.18 — Direitos de acesso", associacao="Direta",
    relacionados=["d02_sla_escopo"], acao="Esclarecer no Q&A",
    pergunta="O prazo de 24 horas é contado a partir de qual evento (data do desligamento ou recebimento da comunicação do RH)? Há integração automática com o sistema de RH do Banco?",
    responsavel="Delivery/Operação")

add(chave="d02_mfa", doc="D02", secao="3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.2", localizador=f"{S3} · item 3.2",
    evidencia=q("Autenticação multifator (MFA) obrigatória para 100% dos usuários com acesso privilegiado."), tipo="Requisito não funcional", dominio="Segurança da Informação/Cyber",
    descricao="MFA para todos os privilegiados. Não informa quantos são nem se a solução de MFA existe ou deve ser fornecida.",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Possível licenciamento de MFA.",
    framework=ISO, controle="A.8.5 — Autenticação segura", associacao="Direta",
    acao="Esclarecer no Q&A",
    pergunta="Quantos usuários e contas com acesso privilegiado existem e a solução de MFA deve ser fornecida pela Contratada ou já existe no Banco?",
    responsavel="Pré-venda/Arquitetura")

add(chave="d02_recert", doc="D02", secao="3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.3", localizador=f"{S3} · item 3.3",
    evidencia=q("Revisão (recertificação) trimestral dos acessos concedidos."), tipo="Requisito funcional / de serviço", dominio="Segurança da Informação/Cyber",
    descricao="Campanhas trimestrais de recertificação; depende da aprovação dos gestores do Banco (dependência não registrada na seção 6).",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Esforço recorrente de coordenação de campanhas.",
    framework=ISO, controle="A.5.18 — Direitos de acesso", associacao="Direta",
    acao="Registrar premissa na proposta", responsavel="Delivery/Operação")

add(chave="d02_pam", doc="D02", secao="3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.4", localizador=f"{S3} · item 3.4",
    evidencia=q("É desejável que a solução contemple cofre de senhas para contas privilegiadas (PAM)."), tipo="Oportunidade / diferencial", dominio="Segurança da Informação/Cyber",
    descricao="Item desejável; a apresentação confirma que o Banco não tem PAM. Oferecer PAM como opcional pode pontuar em 'Ferramentas e tecnologia'.",
    obrigatoriedade="Desejável", framework=ISO, controle="A.8.2 — Direitos de acesso privilegiado", associacao="Direta",
    relacionados=["d03_sem_pam", "d01_crit_ferr"], acao="Precificar", responsavel="Pré-venda/Arquitetura")

add(chave="d02_transicao60", doc="D02", secao="4. TRANSIÇÃO — 4.1", localizador=f"{S4} · item 4.1",
    evidencia=q("A transição dos serviços deverá ser concluída em até 60 (sessenta) dias corridos a partir da assinatura do contrato."), tipo="Prazo / marco", dominio="Transição/Implantação",
    descricao="Prazo de transição de 60 dias, contraditório com os 30 dias da RFP (3.2).", obrigatoriedade="Mandatório", s=4, p=3,
    impacto="Planejamento e custo da transição.", framework="ITIL 4", controle="Transição de serviços / gestão de implantação (identificador a confirmar)", associacao="Correlata",
    relacionados=["d02_contr_transicao"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A", responsavel="Delivery/Operação")

add(chave="d02_contr_transicao", doc="D02", secao="4. TRANSIÇÃO — 4.1 × RFP 3.2", localizador=f"A: D01 {P1}, item 3.2 · B: {S4} · item 4.1",
    evidencia="A: " + q("concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato") + " · B: " + q("concluída em até 60 (sessenta) dias corridos a partir da assinatura do contrato"),
    tipo="Contradição", dominio="Transição/Implantação",
    descricao="Prazos de transição incompatíveis (30 × 60 dias). A diferença altera equipe de implantação, duração da operação paralela sem custo (4.2) e o Plano de transição pontuado (10 pontos). Sem cláusula de precedência.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Custo de até 30 dias de operação paralela; risco de multa se o prazo menor prevalecer.",
    relacionados=["d01_transicao", "d02_transicao60", "d01_precedencia", "d03_risco_transicao"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="O prazo de conclusão da transição é de 30 dias (RFP, item 3.2) ou de 60 dias (Anexo I, item 4.1) contados da assinatura? Qual documento prevalece?",
    responsavel="Delivery/Operação")

add(chave="d02_paralelo", doc="D02", secao="4. TRANSIÇÃO — 4.2", localizador=f"{S4} · item 4.2",
    evidencia=q("Durante a transição, o proponente deverá operar em paralelo com o fornecedor atual"), tipo="Requisito funcional / de serviço", dominio="Transição/Implantação",
    descricao="Operação paralela com o incumbente. O Banco não assume a obrigação de garantir a cooperação do fornecedor atual (acesso a regras, playbooks, logs), e o SIEM legado se encerra em 31/01/2027.",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Dependência de terceiro fora do controle do proponente.",
    relacionados=["d03_siem_legado", "d03_risco_transicao"], acao="Esclarecer no Q&A",
    pergunta="O Banco garantirá contratualmente a cooperação do fornecedor atual durante a transição (repasse de regras de correlação, playbooks, inventário de fontes e acesso aos logs)?",
    responsavel="Delivery/Operação")

add(chave="d02_paralelo_custo", doc="D02", secao="4. TRANSIÇÃO — 4.2", localizador=f"{S4} · item 4.2",
    evidencia=q("sem custo adicional para o Contratante"), tipo="Restrição", dominio="Comercial/Preço",
    descricao="O custo da operação paralela (30 ou 60 dias) deve ser absorvido no preço mensal.", obrigatoriedade="Mandatório", s=3, p=3,
    impacto="Custo de transição embutido no preço, sem remuneração própria.", relacionados=["d02_contr_transicao"],
    acao="Precificar", responsavel="Pricing/Financeiro")

add(chave="d02_cissp", doc="D02", secao="5. EQUIPE — 5.1", localizador=f"{S5} · item 5.1",
    evidencia=q("O serviço deverá contar com coordenador com certificação CISSP, dedicado exclusivamente ao contrato."), tipo="Restrição", dominio="Pessoas/Equipe",
    descricao="Coordenador CISSP com dedicação exclusiva; custo integral alocado ao contrato.", obrigatoriedade="Mandatório", s=3, p=3,
    impacto="Custo fixo de um profissional sênior dedicado.", relacionados=["d01_equipe_cert", "d04_qt06"],
    acao="Precificar", responsavel="RH/Staffing")

add(chave="d02_n1", doc="D02", secao="5. EQUIPE — 5.2", localizador=f"{S5} · item 5.2",
    evidencia=q("Os analistas de nível 1 deverão atuar presencialmente na sede do Contratante, em São Paulo/SP, em horário comercial."), tipo="Restrição", dominio="Pessoas/Equipe / Operação/Serviços",
    descricao="Presença física de N1 em horário comercial. Alterado pela resposta 6 do Q&A, que permite atuação remota em território nacional; a prevalência depende da ordem de precedência, não definida. O item não diz onde atuam os N1 fora do horário comercial.",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Custo de alocação presencial em São Paulo, se mantido.",
    relacionados=["d04_q6", "d01_precedencia"], vigencia="Alterado", acao="Registrar premissa na proposta", responsavel="RH/Staffing")

add(chave="d02_vpn", doc="D02", secao="6. RESPONSABILIDADES DO CONTRATANTE — 6.1", localizador=f"{S6} · item 6.1",
    evidencia=q("Disponibilizar acesso remoto seguro (VPN) aos ambientes monitorados."), tipo="Responsabilidade / dependência do cliente", dominio="Infraestrutura/Cloud",
    descricao="Conectividade a cargo do Banco; não define prazo de disponibilização nem capacidade.", obrigatoriedade="Mandatório", s=2, p=3,
    impacto="Atraso na VPN atrasa a transição.", acao="Registrar premissa na proposta", responsavel="Pré-venda/Arquitetura")

add(chave="d02_doc", doc="D02", secao="6. RESPONSABILIDADES DO CONTRATANTE — 6.2", localizador=f"{S6} · item 6.2",
    evidencia=q("Disponibilizar a documentação técnica do ambiente em até 10 (dez) dias após a assinatura do contrato."), tipo="Responsabilidade / dependência do cliente", dominio="Transição/Implantação",
    descricao="Documentação só até o 10º dia após a assinatura: com transição de 30 dias, sobram 20 dias de implantação com informação completa. Não há previsão de prorrogação da transição em caso de atraso do Banco.",
    obrigatoriedade="Mandatório", s=3, p=3, impacto="Compressão do prazo útil de transição.",
    relacionados=["d03_risco_transicao"], acao="Registrar premissa na proposta",
    pergunta="Em caso de atraso na entrega da documentação técnica (6.2) ou do acesso VPN (6.1), o prazo de transição será prorrogado na mesma proporção?",
    responsavel="Delivery/Operação")

# =========================================================== D03 — Apresentação (PPTX)
add(chave="d03_inv", doc="D03", secao="Apresentação inteira (slides 1 a 5 e notas)", localizador="slides 1–5",
    evidencia=q("Workshop com proponentes — RFP nº 2026-017 — 22/10/2026"), tipo="Registro de cobertura", dominio="Administrativo do processo",
    descricao="Inventário: PowerPoint de 5 slides do workshop de 22/10/2026, versão não informada; sem slides ocultos; notas do apresentador no slide 5 (lidas e analisadas). A força vinculante da apresentação não é definida (ver Lacuna de precedência).",
    framework="—", controle="—", associacao="—", relacionados=["d01_precedencia"], responsavel="Bid Manager")

add(chave="d03_contr_usuarios", doc="D03", secao='Slide 2 — "Números do ambiente" × RFP 2.1', localizador=f'A: D01 {P1}, item 2.1 · B: slide 2 — "Números do ambiente"',
    evidencia="A: " + q("abrangendo aproximadamente 4.500 colaboradores") + " · B: " + q("6.200 usuários ativos"),
    tipo="Contradição", dominio="Técnico/Arquitetura / Comercial/Preço",
    descricao="Quantitativos de usuários divergentes (diferença de cerca de 38%). Podem medir coisas distintas (colaboradores × contas ativas, incluindo terceiros e contas de serviço), mas nenhum documento explica. O lado A foi alterado pelo Q&A (5.000), e a divergência continua (ver contradição no D04).",
    obrigatoriedade="Informativo", s=4, p=3, impacto="Subdimensionamento de licenças e esforço de IAM e SOC.",
    relacionados=["d01_usuarios", "d04_contr_usuarios"], vigencia="Alterado", acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura")

add(chave="d03_servidores", doc="D03", secao='Slide 2 — "Números do ambiente"', localizador='slide 2 — "Números do ambiente"',
    evidencia=q("850 servidores (70% Windows, 30% Linux)"), tipo="Dado de dimensionamento", dominio="Infraestrutura/Cloud",
    descricao="Base de fontes de log de servidores; única volumetria de ativos fornecida.", obrigatoriedade="Informativo", s=2, p=3,
    impacto="Insumo para estimar volume de logs e conectores.", relacionados=["d02_integracao"], acao="Precificar", responsavel="Pré-venda/Arquitetura")

add(chave="d03_dcs", doc="D03", secao='Slide 2 — "Números do ambiente"', localizador='slide 2 — "Números do ambiente"',
    evidencia=q("2 data centers próprios (São Paulo e Campinas)"), tipo="Dado de dimensionamento", dominio="Infraestrutura/Cloud",
    descricao="Duas localidades para coletores de log; não informa se há atuação presencial em Campinas.", obrigatoriedade="Informativo", s=2, p=3,
    impacto="Coletores e conectividade em dois sites.", acao="Precificar", responsavel="Pré-venda/Arquitetura")

add(chave="d03_nuvens", doc="D03", secao='Slide 2 — "Números do ambiente"', localizador='slide 2 — "Números do ambiente"',
    evidencia="Não localizado · " + q("Workloads em 2 nuvens públicas"), tipo="Lacuna", dominio="Infraestrutura/Cloud",
    descricao="Os provedores, a quantidade de contas/assinaturas e os serviços em nuvem a monitorar não são identificados.",
    obrigatoriedade="Informativo", s=3, p=3, impacto="Conectores e volume de logs de nuvem indefinidos.",
    relacionados=["d02_integracao"], acao="Esclarecer no Q&A",
    pergunta="Quais são os provedores de nuvem pública, quantas contas/assinaturas existem e quais serviços devem ser monitorados pelo SIEM?",
    responsavel="Pré-venda/Arquitetura")

add(chave="d03_siem_legado", doc="D03", secao='Slide 3 — "Ferramentas atuais"', localizador='slide 3 — "Ferramentas atuais"',
    evidencia=q("SIEM legado — contrato encerra em 31/01/2027, sem possibilidade de prorrogação"), tipo="Premissa do cliente", dominio="Transição/Implantação",
    descricao="Data rígida de fim do SIEM atual, véspera do início previsto dos serviços (01/02/2027). Limita a operação paralela e a extração de logs históricos.",
    obrigatoriedade="Informativo", s=4, p=3, impacto="Janela fixa para a nova plataforma estar operando.",
    relacionados=["d01_inicio", "d03_risco_transicao"], acao="Mitigar", responsavel="Delivery/Operação")

add(chave="d03_iam_atual", doc="D03", secao='Slide 3 — "Ferramentas atuais"', localizador='slide 3 — "Ferramentas atuais"',
    evidencia=q("IAM: Active Directory + scripts internos"), tipo="Dado de dimensionamento", dominio="Técnico/Arquitetura",
    descricao="Maturidade baixa de IAM (sem plataforma de governança). Sustenta a dúvida sobre quem fornece a ferramenta de IAM.",
    obrigatoriedade="Informativo", s=3, p=3, impacto="Esforço de automação do ciclo de vida e de recertificação.",
    relacionados=["d02_iam_ferr"], acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura")

add(chave="d03_sem_pam", doc="D03", secao='Slide 3 — "Ferramentas atuais"', localizador='slide 3 — "Ferramentas atuais"',
    evidencia=q("Não há solução de PAM"), tipo="Oportunidade / diferencial", dominio="Segurança da Informação/Cyber",
    descricao="Ausência de PAM confirma a oportunidade do item desejável 3.4 do Anexo I.", obrigatoriedade="Informativo",
    framework=ISO, controle="A.8.2 — Direitos de acesso privilegiado", associacao="Correlata",
    relacionados=["d02_pam"], acao="Precificar", responsavel="Pré-venda/Arquitetura")

add(chave="d03_alertas", doc="D03", secao='Slide 4 — "Desafios"', localizador='slide 4 — "Desafios"',
    evidencia=q("Cerca de 1.200 alertas por dia") + " · " + q("70% de falsos positivos"), tipo="Dado de dimensionamento", dominio="Operação/Serviços",
    descricao="Volume de alertas para dimensionar N1 (cerca de 50 por hora), com alto ruído. Única volumetria operacional disponível, já que o EPS foi recusado.",
    obrigatoriedade="Informativo", s=3, p=3, impacto="Dimensionamento de analistas.", relacionados=["d04_q3"],
    acao="Precificar", responsavel="Delivery/Operação")

add(chave="d03_meta_fp", doc="D03", secao='Slide 4 — "Desafios"', localizador='slide 4 — "Desafios"',
    evidencia=q("Meta: reduzir os falsos positivos para 10% no primeiro trimestre de operação"), tipo="Ambiguidade", dominio="Operação/Serviços",
    descricao="Meta agressiva (de 70% para 10% em três meses) que não consta do Anexo I. Não está claro se é SLA sujeito à multa do 7.4, critério de avaliação ou expectativa; não há definição de falso positivo nem linha de base.",
    obrigatoriedade="Desejável", s=4, p=3, impacto="Se contratual, exposição a multas no primeiro trimestre; exige esforço intensivo de tuning.",
    framework="NIST CSF 2.0", controle="DE.AE — Análise de eventos adversos", associacao="Correlata",
    relacionados=["d01_multa"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="A meta de reduzir falsos positivos para 10% no primeiro trimestre é obrigação contratual (SLA sujeito ao item 7.4) ou expectativa? Como será medida a taxa de falsos positivos e qual a linha de base?",
    responsavel="Delivery/Operação")

add(chave="d03_migracao", doc="D03", secao='Slide 5 — "Expectativas para o novo serviço"', localizador='slide 5 — "Expectativas para o novo serviço"',
    evidencia=q("Migração de 24 meses de logs históricos do SIEM legado para a nova plataforma"), tipo="Ambiguidade", dominio="Transição/Implantação / Infraestrutura/Cloud",
    descricao="Escopo de migração que não está no RFP nem no Anexo I. Não informa volume, formato nem se o SIEM legado (encerrado em 31/01/2027) permitirá a extração. 24 meses de histórico excedem a retenção mínima de 12 meses do Anexo I, 1.3.",
    obrigatoriedade="Desejável", s=4, p=3, impacto="Esforço e armazenamento de migração não previstos; dependência do fornecedor atual.",
    framework=ISO, controle="A.8.15 — Registro de eventos (logging)", associacao="Correlata",
    relacionados=["d02_contr_logs", "d03_siem_legado", "d03_risco_transicao"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="A migração de 24 meses de logs históricos do SIEM legado integra o escopo contratado? Qual o volume (TB), formato e forma de acesso ao SIEM legado para extração antes de 31/01/2027?",
    responsavel="Pré-venda/Arquitetura")

add(chave="d03_risco_transicao", doc="D03", secao="Risco combinado — transição", localizador=f'slide 3 — "Ferramentas atuais" · D01 {P1}, itens 3.1 e 3.2 · D01 {P4}, item 7.4',
    evidencia=q("SIEM legado — contrato encerra em 31/01/2027, sem possibilidade de prorrogação") + " · " + q("Início previsto dos serviços 01/02/2027") + " · " + q("multa de 10% (dez por cento) do valor mensal do contrato, por ocorrência"),
    tipo="Risco para o proponente", dominio="Transição/Implantação / Jurídico/Contratual", natureza="Inferida",
    descricao="Risco combinado: o SIEM legado acaba em 31/01/2027 sem prorrogação; a transição é de 30 ou 60 dias a partir de uma assinatura sem data; o Banco tem até 10 dias para entregar a documentação; há operação paralela sem custo, migração de 24 meses de logs e multa de 10% por ocorrência sem teto nem carência. Probabilidade 4: com propostas em 27/11/2026 (Q&A nº 1), concluir 60 dias de transição até 31/01/2027 exigiria assinar até 02/12/2026, cinco dias após a entrega; mesmo com 30 dias, a assinatura teria de ocorrer até 01/01/2027. Os itens componentes mantêm sua severidade própria.",
    obrigatoriedade="Informativo", s=5, p=4, impacto="Lacuna de monitoramento na virada, multas por ocorrência desde o início e responsabilidade ilimitada por incidentes no período.",
    relacionados=["d01_transicao", "d02_transicao60", "d02_contr_transicao", "d01_inicio", "d01_assinatura", "d03_siem_legado", "d02_doc", "d02_paralelo", "d03_migracao", "d01_multa", "d04_q1", "d04_q4"],
    acao="Avaliar Go/No-Go",
    pergunta="Considerando o fim do contrato do SIEM legado em 31/01/2027 sem prorrogação, os SLAs e as multas do item 7.4 serão aplicados durante a transição, ou haverá período de operação assistida sem multas até a conclusão da transição?",
    responsavel="Bid Manager")

add(chave="d03_visao", doc="D03", secao='Slide 5 — "Expectativas para o novo serviço"', localizador='slide 5 — "Expectativas para o novo serviço"',
    evidencia=q("Visão unificada de riscos para a diretoria"), tipo="Ambiguidade", dominio="Segurança da Informação/Cyber / Dados/Analytics",
    descricao="Expectativa sem definição de entregável (dashboard, relatório executivo), abrangência (SOC, IAM, riscos corporativos) ou periodicidade; não consta do Anexo I.",
    obrigatoriedade="Desejável", s=3, p=3, impacto="Possível escopo adicional de BI e relatórios executivos.",
    vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="A 'visão unificada de riscos para a diretoria' é entregável contratado? Qual a abrangência (apenas SOC e IAM ou riscos corporativos), o formato e a periodicidade?",
    responsavel="Pré-venda/Arquitetura")

add(chave="d03_subsid", doc="D03", secao='Slide 5 — notas do apresentador × RFP 2.1', localizador=f'A: D01 {P1}, item 2.1 · B: slide 5 — notas do apresentador',
    evidencia="A: " + q("abrangendo aproximadamente 4.500 colaboradores") + " · B: " + q("as subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários adicionais) também deverão ser incluídas no escopo."),
    tipo="Contradição", dominio="Comercial/Preço / Jurídico/Contratual",
    descricao="Ampliação de escopo escrita só nas notas do apresentador (não exibidas no slide) e ausente do RFP, do Anexo I e do Q&A. As subsidiárias são outras pessoas jurídicas: não se sabe quem contrata, quem é controlador dos dados, se o Anexo III (que fala só dos dados do Banco) as cobre nem se seus ambientes entram no SOC.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Cerca de 900 usuários e ambientes adicionais não precificados; risco de disputa de escopo.",
    relacionados=["d01_usuarios", "d04_contr_usuarios", "d04_q5"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="As subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários), citadas nas notas do slide 5 do workshop, integram o escopo? Se sim, serão contratantes ou beneficiárias, e seus ambientes (SOC e IAM) estão incluídos nos quantitativos e na declaração do Anexo III?",
    responsavel="Bid Manager")

# =========================================================== D04 — Q&A e questionário (XLSX)
def qa(cel, n):
    return f'{QA} · {cel} · Pergunta nº {n} · Rodada 1 (12/11/2026)'

add(chave="d04_inv", doc="D04", secao="Planilha inteira (abas Instruções, Q&A Rodada 1, Questionário Técnico e Pesos)", localizador='abas "Instruções", "Q&A Rodada 1", "Questionário Técnico" e "Pesos" (oculta)',
    evidencia=q("Questionário Técnico e Respostas aos Esclarecimentos — RFP nº 2026-017"), tipo="Registro de cobertura", dominio="Administrativo do processo",
    descricao="Inventário: Excel com 4 abas; Q&A Rodada 1 com 6 perguntas respondidas em 12/11/2026; questionário QT-01 a QT-06; aba 'Pesos' OCULTA (lida e analisada). Primeiro arquivo enviado pelo usuário, processado por último (D04) para confrontar as respostas com os documentos originais.",
    framework="—", controle="—", associacao="—", responsavel="Bid Manager")

add(chave="d04_instrucoes", doc="D04", secao="Instruções", localizador='aba "Instruções" · A3',
    evidencia=q("Questionários incompletos serão desclassificados."), tipo="Critério eliminatório / de habilitação", dominio="Administrativo do processo",
    descricao="Consequência eliminatória que o RFP (4.4) não menciona. Probabilidade 5: a desclassificação decorre diretamente do texto se o questionário não for preenchido integralmente.",
    obrigatoriedade="Mandatório", s=5, p=5, impacto="Desclassificação.", relacionados=["d01_questionario", "d04_instr_amb"],
    acao="Atender", responsavel="Pré-venda/Arquitetura")

add(chave="d04_instr_amb", doc="D04", secao="Instruções", localizador='aba "Instruções" · A3',
    evidencia=q("O preenchimento de todas as abas deste arquivo é obrigatório."), tipo="Ambiguidade", dominio="Administrativo do processo",
    descricao="'Todas as abas' incluiria a aba de Q&A e a aba oculta 'Pesos', que não têm campos de resposta. Não está claro se a coluna 'Comentários' é obrigatória nem se 'Parcial' conta como resposta completa. Erro de interpretação leva a desclassificação.",
    obrigatoriedade="Mandatório", s=5, p=3, impacto="Risco de desclassificação por interpretação divergente.",
    relacionados=["d04_instrucoes"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="Confirmam que apenas a aba 'Questionário Técnico' (colunas D e E) deve ser preenchida? A coluna 'Comentários' é obrigatória em todos os itens?",
    responsavel="Bid Manager")

add(chave="d04_q1", doc="D04", secao="Q&A Rodada 1 — Pergunta 1 (RFP, item 3.1)", localizador=qa("E2", 1),
    evidencia=q("A data de entrega das propostas fica prorrogada para 27/11/2026, até as 18h."), tipo="Prazo / marco", dominio="Administrativo do processo",
    descricao="Altera o prazo de entrega do RFP (20/11/2026). Demais datas do cronograma não foram alteradas.",
    obrigatoriedade="Mandatório", s=5, p=3, impacto="Entrega fora do prazo exclui o proponente.",
    relacionados=["d01_entrega"], acao="Atender", responsavel="Bid Manager")

add(chave="d04_q2", doc="D04", secao="Q&A Rodada 1 — Pergunta 2 (RFP, item 5.1 c)", localizador=qa("E3", 2),
    evidencia=q("Não. O SOC deverá estar localizado em território nacional."), tipo="Restrição", dominio="Operação/Serviços",
    descricao="Confirma o critério 5.1 c (sem alterá-lo). Impede SOC offshore e modelos follow-the-sun com equipes no exterior.",
    obrigatoriedade="Mandatório", s=4, p=3, impacto="Toda a operação do SOC precisa estar no Brasil.",
    relacionados=["d01_hab_c", "d04_q6"], acao="Atender", responsavel="Delivery/Operação")

add(chave="d04_q3", doc="D04", secao="Q&A Rodada 1 — Pergunta 3 (Anexo I, item 1.4)", localizador=qa("E4", 3),
    evidencia=q("A volumetria será informada somente ao proponente vencedor."), tipo="Lacuna", dominio="Técnico/Arquitetura / Comercial/Preço",
    descricao="O cliente recusou formalmente informar o EPS, principal base de licenciamento e de capacidade do SIEM. Probabilidade 5: informação indispensável ao preço recusada formalmente pelo cliente na resposta nº 3. Só há dados indiretos (850 servidores, cerca de 1.200 alertas por dia).",
    obrigatoriedade="Informativo", s=4, p=5, impacto="Preço do SIEM e da infraestrutura sem base; risco de subdimensionamento sem direito a reequilíbrio.",
    relacionados=["d02_integracao", "d02_siem", "d03_alertas", "d03_servidores"], acao="Registrar premissa na proposta",
    pergunta="Na impossibilidade de informar o EPS, o Banco aceita que a proposta adote uma volumetria de referência declarada pelo proponente, com repactuação do preço se a volumetria real a exceder? Alternativamente, pode informar o volume diário de logs (GB/dia) e o número de fontes por tipo?",
    responsavel="Pré-venda/Arquitetura")

add(chave="d04_q4", doc="D04", secao="Q&A Rodada 1 — Pergunta 4 (RFP, item 7.4)", localizador=qa("E5", 4),
    evidencia=q("As condições do item 7 permanecem inalteradas."), tipo="Risco para o proponente", dominio="Jurídico/Contratual",
    descricao="Perguntado sobre limite das multas, o cliente manteve todo o item 7: multas sem teto (7.4), responsabilidade ilimitada (7.5), vedação de subcontratação (7.7) e pagamento em 60 dias (7.3). Sinaliza baixa disposição de negociar. Probabilidade 4: recusa formal registrada na resposta nº 4.",
    obrigatoriedade="Informativo", s=5, p=4, impacto="Exposição financeira e jurídica ilimitada mantida; exceções na proposta podem ser recusadas.",
    relacionados=["d01_multa", "d01_resp", "d01_subcontrat", "d03_risco_transicao"], vigencia="Vigente", acao="Avaliar Go/No-Go",
    responsavel="Jurídico")

add(chave="d04_q5", doc="D04", secao="Q&A Rodada 1 — Pergunta 5 (RFP, item 2.1)", localizador=qa("E6", 5),
    evidencia=q("Considerar 5.000 usuários."), tipo="Dado de dimensionamento", dominio="Técnico/Arquitetura / Comercial/Preço",
    descricao="Altera o quantitativo do RFP (4.500) para dimensionamento. Não esclarece se inclui as subsidiárias nem terceiros.",
    obrigatoriedade="Informativo", s=4, p=3, impacto="Nova base de preço por usuário.",
    relacionados=["d01_usuarios", "d04_contr_usuarios"], acao="Precificar", responsavel="Pricing/Financeiro")

add(chave="d04_contr_usuarios", doc="D04", secao="Q&A Rodada 1 — Pergunta 5 × Apresentação, slides 2 e 5", localizador=f'A: {qa("E6", 5)} · B: D03 slide 2 — "Números do ambiente" e slide 5 — notas do apresentador',
    evidencia="A: " + q("Considerar 5.000 usuários.") + " · B: " + q("6.200 usuários ativos") + " · " + q("cerca de 900 usuários adicionais"),
    tipo="Contradição", dominio="Técnico/Arquitetura / Comercial/Preço",
    descricao="Mesmo após o Q&A, o número de usuários diverge: 5.000 (Q&A) × 6.200 ativos (workshop) × 7.100 se somadas as subsidiárias. Sem precedência definida e sem mecanismo de ajuste de preço por volume.",
    obrigatoriedade="Informativo", s=4, p=3, impacto="Diferença de até cerca de 42% na base de usuários.",
    relacionados=["d04_q5", "d03_contr_usuarios", "d03_subsid", "d01_usuarios", "d01_precedencia"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="A resposta 5 do Q&A indica 5.000 usuários, mas a apresentação do workshop indica 6.200 usuários ativos e mais cerca de 900 das subsidiárias. Qual quantitativo deve ser usado para SOC e IAM, e o preço será ajustado se o número real exceder o informado?",
    responsavel="Pré-venda/Arquitetura")

add(chave="d04_q6", doc="D04", secao="Q&A Rodada 1 — Pergunta 6 (Anexo I, item 5.2)", localizador=qa("E7", 6),
    evidencia=q("Sim, desde que em território nacional."), tipo="Restrição", dominio="Pessoas/Equipe",
    descricao="Altera o Anexo I, 5.2: analistas N1 podem atuar remotamente no Brasil. Reduz custo de alocação presencial.",
    obrigatoriedade="Mandatório", s=2, p=3, impacto="Flexibiliza o modelo de equipe.",
    relacionados=["d02_n1", "d04_q2"], acao="Atender", responsavel="RH/Staffing")

def qt(chave, cel, texto, obrig, peso, pcel, tipo, s, desc, rel, fw=None, ctrl=None, assoc=None, perg="—", resp="Pré-venda/Arquitetura", vig="Vigente", acao="Atender"):
    add(chave=chave, doc="D04", secao=f"Questionário Técnico — {chave[-4:].upper().replace('QT0', 'QT-0')}",
        localizador=f'{QT} · linha {cel[1:]} (ID {chave[-4:].upper().replace("QT0", "QT-0")}) · aba "Pesos" (oculta) · {pcel}',
        evidencia=q(texto) + f" · Obrigatório: {obrig} · Peso: {peso}", tipo=tipo, dominio="Administrativo do processo / Segurança da Informação/Cyber",
        descricao=desc, obrigatoriedade="Mandatório" if obrig == "Sim" else "Desejável", s=s, p=3,
        impacto=f"Item do questionário com peso {peso} (aba oculta); afeta a Nota Técnica.",
        framework=fw or "—", controle=ctrl or "—", associacao=assoc or "Não aplicável",
        relacionados=rel, vigencia=vig, acao=acao, pergunta=perg, responsavel=resp)

qt("d04_qt01", "B2", "Possui certificação ISO/IEC 27001 com escopo que inclua os serviços de SOC?", "Sim", 3, "B2", "Critério de avaliação / pontuação", 3,
   "Repete o critério de habilitação 5.1 a) no questionário, com peso 3.", ["d01_hab_a"], ISO, "Cláusulas 4 a 10 (requisitos do SGSI) — certificação", "Direta", vig="Duplicado", resp="Compliance")
qt("d04_qt02", "B3", "Oferece integração nativa com plataforma SOAR?", "Não", 1, "B3", "Critério de avaliação / pontuação", 3,
   "SOAR não consta do RFP nem do Anexo I. Embora não obrigatório, responder 'Não atende' custa 2 pontos pela regra da aba oculta 'Pesos'.", ["d04_pesos", "d01_crit_ferr"],
   "NIST CSF 2.0", "Função RS (Respond) — automação da resposta (identificador a confirmar)", "Correlata",
   perg="A integração com SOAR (QT-02) passa a fazer parte do escopo a ser precificado ou apenas da pontuação? Há plataforma SOAR existente no Banco?", acao="Esclarecer no Q&A")
qt("d04_qt03", "B4", "Retém os logs online por no mínimo 12 meses?", "Sim", 2, "B4", "Critério de avaliação / pontuação", 3,
   "Introduz o qualificador 'online', que não está no Anexo I (1.3), e reforça a leitura '12 meses online + 5 anos de arquivo' da contradição de retenção.", ["d02_contr_logs"],
   ISO, "A.8.15 — Registro de eventos (logging)", "Direta")
qt("d04_qt04", "B5", "Atende aos requisitos da Resolução CMN nº 4.893/2021?", "Sim", 3, "B5", "Critério de avaliação / pontuação", 4,
   "Pergunta ampla: a Resolução se dirige às instituições financeiras e o RFP não diz quais requisitos o prestador deve evidenciar. Peso 3 (máximo). Resposta afirmativa sem lastro pode gerar obrigação contratual.", ["d01_cmn"],
   CMN, "Política de segurança cibernética e contratação de serviços (identificador a confirmar)", "Direta",
   perg="Quais requisitos da Resolução CMN nº 4.893/2021 o Banco espera que o proponente evidencie no QT-04 (por exemplo, política de segurança cibernética própria, cláusulas de contratação de nuvem, localização de dados, continuidade) e com quais documentos?",
   resp="Compliance", acao="Esclarecer no Q&A")
qt("d04_qt05", "B6", "Oferece serviço de threat intelligence?", "Não", 2, "B6", "Critério de avaliação / pontuação", 3,
   "Threat intelligence não consta do RFP nem do Anexo I. Não obrigatório, mas 'Não atende' custa 2 pontos pela aba oculta 'Pesos'. Feeds de terceiros podem esbarrar na vedação de subcontratação (7.7).", ["d04_pesos", "d02_amb_subcontrat"],
   ISO, "A.5.7 — Inteligência de ameaças", "Direta", resp="Segurança/Cyber")
qt("d04_qt06", "B7", "Possui equipe com certificações reconhecidas pelo mercado?", "Sim", 2, "B7", "Critério de avaliação / pontuação", 3,
   "Genérico como o item 5.2 do RFP: não define quais certificações nem quantos profissionais.", ["d01_equipe_cert", "d02_cissp"],
   ISO, "Cláusula 7.2 — Competência", "Correlata", resp="RH/Staffing")

add(chave="d04_pesos", doc="D04", secao='Pesos (aba oculta)', localizador='aba "Pesos" (oculta) · A9',
    evidencia=q("Requisitos não obrigatórios respondidos como 'Não atende' reduzem a Nota Técnica em 2 (dois) pontos cada."), tipo="Critério de avaliação / pontuação", dominio="Administrativo do processo",
    descricao="Regra de pontuação escondida numa aba oculta e ausente do item 6 do RFP. Itens não obrigatórios (QT-02 SOAR e QT-05 threat intelligence) passam a ser, na prática, penalizados: até 4 pontos perdidos, perto do corte de 70% do item 6.3. Os pesos das linhas 2 a 7 (3, 1, 2, 3, 2, 2) não têm uso descrito.",
    obrigatoriedade="Informativo", s=4, p=3, impacto="Até 4 pontos a menos na Nota Técnica; risco de cair abaixo do corte.",
    relacionados=["d04_qt02", "d04_qt05", "d01_corte", "d04_contr_pontuacao"], acao="Esclarecer no Q&A", responsavel="Bid Manager")

add(chave="d04_contr_pontuacao", doc="D04", secao="Pesos (aba oculta) × RFP 6.2", localizador=f'A: D01 {P3}, item 6.2 · B: aba "Pesos" (oculta) · A1:B9',
    evidencia="A: " + q("A Nota Técnica, de no máximo 60 (sessenta) pontos, será atribuída conforme os critérios abaixo") + " · B: " + q("reduzem a Nota Técnica em 2 (dois) pontos cada"),
    tipo="Contradição", dominio="Administrativo do processo",
    descricao="O RFP diz que a Nota Técnica é atribuída só pelos quatro critérios do 6.2, mas a aba oculta do questionário prevê pesos por item e descontos diretos na Nota Técnica. Não se sabe em qual critério os pesos entram, como se trata 'Parcial' nem o efeito de 'Não atende' em item obrigatório.",
    obrigatoriedade="Informativo", s=4, p=3, impacto="Regra de pontuação não transparente; risco de desclassificação pelo corte de 70%.",
    relacionados=["d01_contr_pontos", "d01_corte", "d04_pesos"], vigencia="Em esclarecimento", acao="Esclarecer no Q&A",
    pergunta="A aba oculta 'Pesos' do questionário prevê pesos por item e desconto de 2 pontos por requisito não obrigatório respondido 'Não atende', o que não consta do item 6.2 da RFP. Esses pesos e descontos serão aplicados? Em qual critério do item 6.2 e com que efeito sobre o corte do item 6.3? Como serão tratadas as respostas 'Parcial' e 'Não atende' em requisitos obrigatórios?",
    responsavel="Bid Manager")

data = {
    "processo": "RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Serviços Gerenciados de SOC e IAM",
    "documentos": [
        {"codigo": "D01", "arquivo": "RFP-2026-017_Servicos_SOC_IAM.pdf", "tipo": "RFP (documento principal, com Anexo III digitalizado na p. 6)", "versao": "Versão 1.0 — 15/10/2026", "situacao": "processado"},
        {"codigo": "D02", "arquivo": "Anexo_I_Especificacao_Tecnica.docx", "tipo": "Anexo técnico", "versao": "Versão 1.0 — 15/10/2026", "situacao": "processado"},
        {"codigo": "D03", "arquivo": "Apresentacao_Ambiente_Atual.pptx", "tipo": "Apresentação do workshop", "versao": "22/10/2026 (versão não informada)", "situacao": "processado"},
        {"codigo": "D04", "arquivo": "QA_Rodada1_e_Questionario.xlsx", "tipo": "Q&A e questionário técnico", "versao": "Q&A Rodada 1 — 12/11/2026", "situacao": "processado"},
    ],
    "itens": itens,
    "status": {"final": True},
}
out = Path(__file__).with_name("itens.json")
out.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(itens), "itens ->", out)
