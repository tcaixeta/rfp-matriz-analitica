#!/usr/bin/env python3
"""Gera itens.json da matriz RFP 2026-017. Uso: gen_itens.py <estagio 1-4> <saida.json>"""
import json
import sys

ISO = "ISO/IEC 27001:2022"
CC = "Código Civil (Lei 10.406/2002)"
LGPD = "LGPD (Lei 13.709/2018)"
CMN = "Resolução CMN nº 4.893/2021 (citada pelo cliente)"
ITIL = "ITIL 4"
NIST = "NIST CSF 2.0"
APMP = "APMP Body of Knowledge"

itens = []


def I(chave, doc, secao, loc, evid, tipo, dominio, desc, **kw):
    d = dict(chave=chave, doc=doc, secao=secao, localizador=loc, evidencia=evid, tipo=tipo,
             dominio=dominio, descricao=desc)
    rel = kw.pop("rel", None)
    if rel:
        d["relacionados"] = rel
    d.update(kw)
    if d["tipo"] not in ("Registro de cobertura", "Oportunidade / diferencial") and "associacao" not in d:
        d["framework"], d["controle"], d["associacao"] = "—", "—", "Não aplicável"
    itens.append(d)


P2 = "p. 2 (impressa: 1)"
P3 = "p. 3 (impressa: 2)"
P4 = "p. 4 (impressa: 3)"
P5 = "p. 5 (impressa: 4)"
P6 = "p. 6 (impressa: 5) (OCR)"

# =============================================================== D01 — RFP
I("d01_inv", "D01", "Inventário do documento", "p. 1 a p. 6",
  '"Solicitação de Proposta (RFP) nº 2026-017"', "Registro de cobertura", "Administrativo do processo",
  "PDF de 6 páginas físicas (capa sem número + páginas impressas 1 a 5), versão 1.0 de 15/10/2026, processado integralmente. "
  "A p. 6 (impressa: 5) não tem camada de texto: o conteúdo em imagem foi lido visualmente ({d01_ocr}).")
I("d01_ocr", "D01", "Anexo III — Declaração de Localização de Dados", P6,
  '"ANEXO III — DECLARAÇÃO DE LOCALIZAÇÃO DE DADOS"', "Registro de cobertura", "Administrativo do processo",
  "Página digitalizada (0 caracteres de texto extraível, imagem em metade da página). Lida por OCR visual e transcrita em "
  "extracao/D01_p6_ocr.md; conteúdo analisado em {d01_anexo3_decl} e {d01_anexo3_dados}. O corpo da RFP não menciona o Anexo III.")
I("d01_regime", "D01", "1. Apresentação, item 1.2", P2,
  '"O Banco é instituição financeira autorizada a funcionar pelo Banco Central do Brasil e está sujeito à Resolução CMN nº 4.893/2021"',
  "Registro de cobertura", "Regulatório/Compliance",
  "Regime identificado: contratação privada (RFP de sociedade anônima, envio pelo portal de fornecedores do Banco, sem referência a licitação "
  "ou a lei de contratações públicas) em setor regulado (instituição financeira supervisionada pelo Banco Central). A Lei 14.133/2021 não se aplica. "
  "Associações jurídicas usam o Código Civil; regulatórias, a Resolução CMN nº 4.893/2021 citada pelo cliente e a LGPD.")
I("d01_precedencia", "D01", "Documento inteiro (RFP, Anexo I, apresentação e Q&A)", "p. 1 a p. 6",
  'Não localizado · "As especificações técnicas detalhadas constam do Anexo I — Especificação Técnica."',
  "Lacuna", "Jurídico/Contratual",
  "Nenhum dos quatro documentos define ordem de precedência entre RFP, Anexo I, apresentação do workshop e respostas do Q&A. Há divergências "
  "materiais entre eles: transição ({d02_contr_transicao}), base de usuários ({d03_contr_usuarios}, {d04_contr_usuarios}), localização de dados "
  "({d02_contr_nuvem}), retenção de logs ({d02_contr_retencao}) e pontuação ({d04_pesos_regra}). Não se presume que o Q&A prevaleça por ser mais recente. "
  "Associação de boa prática: a verificação da hierarquia documental é etapa usual de análise de propostas.",
  s=4, p=3, impacto="Sem regra de precedência o proponente não sabe qual prazo, volumetria e escopo são vinculantes; risco de precificar e se comprometer com a versão errada.",
  framework=APMP, controle="Análise de conformidade e hierarquia de documentos da RFP (identificador a confirmar)", associacao="Boa prática",
  rel=["d02_contr_transicao", "d03_contr_usuarios", "d04_contr_usuarios", "d02_contr_nuvem", "d02_contr_retencao", "d04_pesos_regra"],
  acao="Esclarecer no Q&A", responsavel="Jurídico",
  pergunta="Solicitamos informar a ordem de precedência entre a RFP, o Anexo I, a apresentação do workshop de 22/10/2026 e as respostas do Q&A, "
  "inclusive se as respostas do Q&A alteram formalmente a RFP e seus anexos e se o conteúdo da apresentação (inclusive notas) integra o escopo contratual.")
I("d01_cmn", "D01", "1. Apresentação, item 1.2", P2,
  '"está sujeito à Resolução CMN nº 4.893/2021, que dispõe sobre a política de segurança cibernética e sobre os requisitos para a contratação de serviços de processamento e armazenamento de dados e de computação em nuvem"',
  "Requisito implícito", "Regulatório/Compliance",
  "Inferido: como o Banco está sujeito à resolução, a contratação de SOC e SIEM (inclusive em nuvem, {d02_siem}) precisa permitir ao Banco cumprir as "
  "exigências para serviços de processamento e armazenamento de dados (cláusulas contratuais, acesso do regulador, comunicação ao Banco Central, "
  "localização de dados). A RFP não detalha quais obrigações serão repassadas à Contratada; o questionário pede declaração genérica ({d04_qt04}).",
  obrigatoriedade="Mandatório", natureza="Inferida", s=3, p=3,
  impacto="Obrigações regulatórias não precificadas (auditorias, relatórios ao regulador, restrições de nuvem).",
  framework=CMN, controle="Requisitos para contratação de serviços de processamento e armazenamento de dados e de computação em nuvem (identificador a confirmar)",
  associacao="Direta", rel=["d04_qt04", "d02_contr_nuvem"], acao="Esclarecer no Q&A", responsavel="Compliance",
  pergunta="Quais obrigações decorrentes da Resolução CMN nº 4.893/2021 serão exigidas contratualmente da Contratada (cláusulas obrigatórias, acesso do "
  "Banco Central, continuidade, notificação de incidentes, localização de dados) e em que documento estarão previstas?")
I("d01_objeto_soc", "D01", "2. Objeto, item 2.1", P2,
  '"serviços gerenciados de Centro de Operações de Segurança (SOC), em regime 24x7x365"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber / Operação/Serviços",
  "Objeto: SOC gerenciado em regime ininterrupto. Detalhado no Anexo I, seção 1 ({d02_monitoramento}).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Define a escala de turnos 24x7 e o dimensionamento da equipe do SOC.",
  framework=ISO, controle="A.8.16 Atividades de monitoramento", associacao="Correlata", acao="Precificar", responsavel="Delivery/Operação")
I("d01_objeto_iam", "D01", "2. Objeto, item 2.1", P2, '"gestão de identidades e acessos (IAM)"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Objeto inclui serviço de IAM. O Anexo I (seção 3) descreve processos, mas não diz se a plataforma de IAM é fornecida pelo proponente ({d02_lac_ferramenta_iam}).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Escopo de IAM entra no preço; ferramenta indefinida.",
  framework=ISO, controle="A.5.16 Gestão de identidade", associacao="Correlata", rel=["d02_lac_ferramenta_iam"],
  acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d01_usuarios", "D01", "2. Objeto, item 2.1", P2, '"abrangendo aproximadamente 4.500 colaboradores"',
  "Dado de dimensionamento", "Comercial/Preço",
  "Base de dimensionamento do objeto. Alterada pelo Q&A nº 5 para 5.000 usuários ({d04_qa5}) e divergente da apresentação (6.200 usuários ativos, "
  "mais cerca de 900 das subsidiárias: {d03_contr_usuarios}, {d03_subsidiarias}).",
  s=3, p=3, impacto="Base de preço de IAM, MFA e volume de eventos do SOC.", vigencia="Alterado",
  rel=["d04_qa5", "d03_contr_usuarios", "d03_subsidiarias"], acao="Registrar premissa na proposta", responsavel="Pricing/Financeiro")
I("d01_workshop", "D01", "3. Cronograma do processo, item 3.1", P2, '"Workshop de apresentação do ambiente 22/10/2026"',
  "Prazo / marco", "Administrativo do processo",
  "Workshop de apresentação do ambiente; o material correspondente foi recebido ({d03_inv}). A RFP não diz se a participação é obrigatória.",
  s=2, p=3, impacto="Perda de informações de ambiente dadas apenas no workshop (ex.: subsidiárias nas notas).", rel=["d03_inv"],
  acao="Atender", responsavel="Bid Manager")
I("d01_prazo_perguntas", "D01", "3. Cronograma do processo, item 3.1", P2, '"Prazo final para envio de perguntas 05/11/2026"',
  "Prazo / marco", "Administrativo do processo",
  "Data-limite para submeter perguntas. As respostas da Rodada 1 ({d04_inv}) deixam lacunas relevantes; a RFP não prevê nova rodada.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Lacunas que não puderem ser esclarecidas viram premissas e ressalvas na proposta.",
  acao="Esclarecer no Q&A", responsavel="Bid Manager",
  pergunta="Haverá nova rodada de perguntas após a divulgação das respostas da Rodada 1 e a prorrogação da entrega para 27/11/2026? Em caso positivo, qual o prazo?")
I("d01_respostas", "D01", "3. Cronograma do processo, item 3.1", P2, '"Divulgação das respostas 12/11/2026"',
  "Prazo / marco", "Administrativo do processo",
  "Respostas divulgadas na data prevista (Q&A Rodada 1 datado de 12/11/2026). Restam 15 dias até a entrega prorrogada ({d04_qa1}) para incorporar as respostas.",
  s=2, p=3, impacto="Janela curta entre respostas e entrega.", rel=["d04_qa1"], acao="Nenhuma (informativo)", responsavel="Bid Manager")
I("d01_entrega", "D01", "3. Cronograma do processo, item 3.1", P2, '"Entrega das propostas 20/11/2026, até as 18h"',
  "Prazo / marco", "Administrativo do processo",
  "Prazo original de entrega, prorrogado para 27/11/2026, até as 18h, pelo Q&A nº 1 ({d04_qa1}). Proposta fora do prazo não participa do processo (inferência).",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Perda do prazo exclui o proponente.", vigencia="Alterado", rel=["d04_qa1"],
  acao="Atender", responsavel="Bid Manager")
I("d01_inicio", "D01", "3. Cronograma do processo, item 3.1", P2, '"Início previsto dos serviços 01/02/2027"',
  "Prazo / marco", "Transição/Implantação",
  "Coincide com o dia seguinte ao fim do contrato do SIEM legado (31/01/2027, sem prorrogação: {d03_siem_legado}). Ver risco combinado {d03_risco_transicao}.",
  s=3, p=3, impacto="Define a data em que SLAs e multas passam a valer.", rel=["d03_siem_legado", "d03_risco_transicao"],
  acao="Registrar premissa na proposta", responsavel="Delivery/Operação")
I("d01_transicao30", "D01", "3. Cronograma do processo, item 3.2", P2,
  '"A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato."',
  "Prazo / marco", "Transição/Implantação",
  "Prazo de transição de 30 dias corridos, contraditório com os 60 dias do Anexo I ({d02_contr_transicao}). Prazo curto para provisionar SIEM, integrar fontes, "
  "migrar logs e assumir IAM.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Equipe de transição maior e risco de atraso na entrada em operação.",
  framework=ITIL, controle="Cadeia de valor de serviço — atividade Design e transição", associacao="Correlata",
  vigencia="Em esclarecimento", rel=["d02_contr_transicao", "d03_risco_transicao"], acao="Esclarecer no Q&A", responsavel="Delivery/Operação")
I("d01_lac_assinatura", "D01", "3. Cronograma do processo, itens 3.1 e 3.2", P2,
  'Não localizado · "a partir da assinatura do contrato"', "Lacuna", "Transição/Implantação",
  "O cronograma não informa data de resultado nem de assinatura do contrato. Como a transição conta da assinatura e o início dos serviços está previsto para "
  "01/02/2027, não se sabe se a transição ocorre antes dessa data (em paralelo com o fornecedor atual, {d02_paralelo}) ou depois, com o SIEM legado já encerrado.",
  s=3, p=3, impacto="Sem a data, não é possível planejar a transição nem a operação paralela.",
  rel=["d02_paralelo", "d03_siem_legado"], acao="Esclarecer no Q&A", responsavel="Bid Manager",
  pergunta="Qual a data prevista para divulgação do resultado e para assinatura do contrato? A transição deve estar concluída até 01/02/2027 ou começa nessa data?")
I("d01_idioma", "D01", "4. Instruções para apresentação da proposta, item 4.1", P3,
  '"A proposta deverá ser redigida em língua portuguesa"', "Instrução de resposta", "Administrativo do processo",
  "Idioma obrigatório. Não diz se documentos de fabricantes e certificados em inglês precisam de tradução.",
  obrigatoriedade="Mandatório", s=2, p=3, impacto="Custo de tradução de anexos técnicos, se exigida.", acao="Atender", responsavel="Bid Manager")
I("d01_portal", "D01", "4. Instruções para apresentação da proposta, item 4.1", P3,
  '"enviada exclusivamente pelo portal de fornecedores do Banco"', "Instrução de resposta", "Administrativo do processo",
  "Canal único de entrega. Não informa endereço do portal, exigência e prazo de cadastro prévio, formatos e tamanho de arquivos.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Cadastro tardio ou arquivo recusado pode impedir a entrega.",
  acao="Esclarecer no Q&A", responsavel="Bid Manager",
  pergunta="Favor informar o endereço do portal de fornecedores, se há cadastro prévio obrigatório (e com que antecedência) e os formatos e limites de tamanho de arquivo aceitos.")
I("d01_paginas", "D01", "4. Instruções para apresentação da proposta, item 4.2", P3,
  '"A proposta técnica deverá ter no máximo 40 (quarenta) páginas, excluídos os anexos."', "Instrução de resposta", "Administrativo do processo",
  "Limite de páginas sem padrão de formatação nem consequência do excesso. Não está claro se conteúdo em anexos é considerado na avaliação técnica.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Restringe a demonstração de metodologia e plano de transição, que somam 30 pontos.",
  acao="Esclarecer no Q&A", responsavel="Bid Manager",
  pergunta="Qual a consequência de exceder 40 páginas? Há padrão de formatação (fonte, margens, tamanho de página)? Conteúdo apresentado em anexos será considerado na avaliação técnica?")
I("d01_planilha_precos", "D01", "4. Instruções para apresentação da proposta, item 4.3", P3,
  '"A proposta comercial deverá ser apresentada conforme a planilha modelo do Anexo IV — Planilha de Preços."',
  "Instrução de resposta", "Comercial/Preço",
  "Formato obrigatório da proposta comercial; o Anexo IV não foi fornecido ({d01_lac_anexo4}).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Proposta comercial fora do modelo pode ser recusada.", rel=["d01_lac_anexo4"],
  acao="Atender", responsavel="Pricing/Financeiro")
I("d01_lac_anexo4", "D01", "4. Instruções para apresentação da proposta, item 4.3", P3,
  'Não localizado · "conforme a planilha modelo do Anexo IV — Planilha de Preços"', "Lacuna", "Comercial/Preço",
  "Documento citado pelo cliente e não fornecido (não está no pacote nem na lista do usuário). Sem ele não se conhece a estrutura de preço exigida "
  "(por usuário, por EPS, valor fixo mensal, transição), que também é a base da multa de 10% do valor mensal. A numeração dos anexos salta do Anexo I para o "
  "Anexo III (p. 6), sem menção a um Anexo II.",
  s=4, p=3, impacto="Impede montar a proposta comercial no formato exigido e simular a Nota de Preço.",
  rel=["d01_planilha_precos", "d01_lac_formula_preco"], acao="Esclarecer no Q&A", responsavel="Pricing/Financeiro",
  pendencia="Anexo IV — Planilha de Preços citado pelo cliente e não fornecido",
  pergunta="Solicitamos o envio do Anexo IV — Planilha de Preços (modelo editável). Pedimos também confirmar se existe um Anexo II e, em caso positivo, enviá-lo.")
I("d01_questionario", "D01", "4. Instruções para apresentação da proposta, item 4.4", P3,
  '"O questionário técnico (planilha anexa) deverá ser integralmente preenchido."', "Instrução de resposta", "Administrativo do processo",
  "A RFP não prevê sanção; a planilha recebida prevê desclassificação de questionário incompleto e exige o preenchimento de todas as abas ({d04_instr_desclass}, {d04_amb_todas_abas}).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Questionário incompleto leva à desclassificação (ver planilha).",
  rel=["d04_instr_desclass", "d04_amb_todas_abas"], acao="Atender", responsavel="Pré-venda/Arquitetura")
I("d01_iso", "D01", "5. Critérios de habilitação, item 5.1 a", P3,
  '"certificado ISO/IEC 27001 vigente, emitido por organismo acreditado, cujo escopo inclua os serviços de SOC"',
  "Critério eliminatório / de habilitação", "Segurança da Informação/Cyber",
  "Probabilidade 5: o item 5.1 determina a inabilitação de quem não apresentar o certificado; o efeito decorre do texto. Não se diz se vale certificado de "
  "empresa do mesmo grupo nem escopo em extensão.",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação.", framework=ISO,
  controle="Certificação do SGSI — requisitos das cláusulas 4 a 10", associacao="Direta", rel=["d04_qt01"],
  acao="Avaliar Go/No-Go", responsavel="Compliance",
  pergunta="O certificado ISO/IEC 27001 pode estar em nome de empresa do mesmo grupo econômico do proponente? Será aceito certificado cujo escopo inclua o SOC em processo de extensão, com auditoria agendada?")
I("d01_atestados", "D01", "5. Critérios de habilitação, item 5.1 b", P3,
  '"no mínimo 3 (três) atestados de capacidade técnica de prestação de serviços de SOC para instituições financeiras, com ambiente de no mínimo 2.000 usuários"',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Probabilidade 5: a falta dos atestados leva à inabilitação expressa no item 5.1.",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação.", rel=["d01_amb_atestados"],
  acao="Avaliar Go/No-Go", responsavel="Bid Manager")
I("d01_amb_atestados", "D01", "5. Critérios de habilitação, item 5.1 b", P3, '"com ambiente de no mínimo 2.000 usuários"',
  "Ambiguidade", "Administrativo do processo",
  "Não está claro se cada atestado deve comprovar 2.000 usuários ou se podem ser somados; se contratos em andamento valem; e se seguradoras, cooperativas "
  "e instituições de pagamento contam como instituições financeiras. A leitura errada leva à inabilitação.",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Risco de inabilitação por interpretação divergente.", rel=["d01_atestados"],
  acao="Esclarecer no Q&A", responsavel="Bid Manager",
  pergunta="Cada um dos 3 atestados deve comprovar ambiente de no mínimo 2.000 usuários, ou é admitida a soma? São aceitos atestados de contratos em andamento? "
  "Seguradoras, cooperativas de crédito e instituições de pagamento são consideradas instituições financeiras para este fim?")
I("d01_soc_nacional", "D01", "5. Critérios de habilitação, item 5.1 c", P3,
  '"comprovação de que o SOC está localizado em território nacional"', "Critério eliminatório / de habilitação", "Operação/Serviços",
  "Probabilidade 5: inabilitação expressa no item 5.1; confirmada pelo Q&A nº 2 ({d04_qa2}). Não se diz qual documento comprova a localização.",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação.", rel=["d04_qa2"],
  acao="Atender", responsavel="Bid Manager",
  pergunta="Qual documento será aceito como comprovação da localização do SOC em território nacional (endereço, contrato de locação, declaração)?")
I("d01_equipe_cert", "D01", "5. Critérios de habilitação, item 5.2", P3,
  '"O proponente deverá possuir equipe técnica devidamente certificada."', "Ambiguidade", "Pessoas/Equipe",
  "Item na seção de habilitação, mas fora da lista do 5.1 que define a inabilitação. Não diz quais certificações, quantos profissionais nem como comprovar. "
  "O Anexo I exige CISSP só do coordenador ({d02_cissp}) e o questionário fala em certificações reconhecidas pelo mercado ({d04_qt06}). "
  "Se for tratado como habilitação, a falta de comprovação pode inabilitar.",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Possível inabilitação e perda de pontos no critério Qualificação da equipe (20 pontos).",
  framework=ISO, controle="Cláusula 7.2 Competência", associacao="Correlata", rel=["d02_cissp", "d04_qt06", "d01_crit_equipe"],
  acao="Esclarecer no Q&A", responsavel="RH/Staffing",
  pergunta="O item 5.2 é critério de habilitação? Quais certificações, para quais perfis, em que quantidade e com que documentos devem ser comprovadas na proposta?")
I("d01_nota_final", "D01", "6. Critérios de avaliação, item 6.1", P4,
  '"A nota final será composta pela Nota Técnica (peso de 60%) e pela Nota de Preço (peso de 40%)."',
  "Critério de avaliação / pontuação", "Comercial/Preço",
  "Técnica e preço com pesos 60/40; a fórmula da Nota de Preço não é informada ({d01_lac_formula_preco}).",
  s=3, p=3, impacto="Orienta a estratégia de preço versus investimento técnico.", rel=["d01_lac_formula_preco"],
  acao="Nenhuma (informativo)", responsavel="Pricing/Financeiro")
I("d01_lac_formula_preco", "D01", "6. Critérios de avaliação, item 6.1", P4,
  'Não localizado · "pela Nota de Preço (peso de 40%)"', "Lacuna", "Comercial/Preço",
  "Não há fórmula da Nota de Preço (proporcional ao menor preço, faixas, preço de referência) nem critério de inexequibilidade.",
  s=4, p=3, impacto="Impede simular o equilíbrio entre preço e nota técnica, que define 40% da nota final.",
  acao="Esclarecer no Q&A", responsavel="Pricing/Financeiro",
  pergunta="Qual a fórmula de cálculo da Nota de Preço? Há preço máximo de referência ou critério de inexequibilidade?")
I("d01_crit_metod", "D01", "6. Critérios de avaliação, item 6.2", P4, '"Metodologia de operação do SOC 20"',
  "Critério de avaliação / pontuação", "Operação/Serviços",
  "Critério de maior peso, empatado com Qualificação da equipe (20 de 60 pontos declarados).", s=4, p=3,
  impacto="Um terço da Nota Técnica.", framework=ITIL, controle="Prática de gerenciamento de incidentes", associacao="Correlata",
  rel=["d01_contr_pontos"], acao="Atender", responsavel="Pré-venda/Arquitetura")
I("d01_crit_equipe", "D01", "6. Critérios de avaliação, item 6.2", P4, '"Qualificação da equipe 20"',
  "Critério de avaliação / pontuação", "Pessoas/Equipe",
  "20 pontos sem critério objetivo de qualificação; ligado à exigência vaga de equipe certificada ({d01_equipe_cert}).", s=4, p=3,
  impacto="Um terço da Nota Técnica.", rel=["d01_equipe_cert", "d01_contr_pontos"], acao="Atender", responsavel="RH/Staffing")
I("d01_crit_ferr", "D01", "6. Critérios de avaliação, item 6.2", P4, '"Ferramentas e tecnologia 15"',
  "Critério de avaliação / pontuação", "Técnico/Arquitetura", "15 pontos para ferramentas (SIEM, IAM, PAM, SOAR).", s=3, p=3,
  impacto="Um quarto da Nota Técnica.", rel=["d01_contr_pontos"], acao="Atender", responsavel="Pré-venda/Arquitetura")
I("d01_crit_trans", "D01", "6. Critérios de avaliação, item 6.2", P4, '"Plano de transição 10"',
  "Critério de avaliação / pontuação", "Transição/Implantação",
  "10 pontos para o plano de transição, cujo prazo é contraditório (30 ou 60 dias, {d02_contr_transicao}).", s=3, p=3,
  impacto="Plano feito sobre o prazo errado perde pontos.", rel=["d02_contr_transicao", "d01_contr_pontos"], acao="Atender", responsavel="Delivery/Operação")
I("d01_lac_subcriterios", "D01", "6. Critérios de avaliação, item 6.2", P4,
  'Não localizado · "será atribuída conforme os critérios abaixo"', "Lacuna", "Administrativo do processo",
  "Não há subcritérios, evidências esperadas nem escala de notas por critério técnico.", s=3, p=3,
  impacto="Dificulta direcionar a proposta técnica de 40 páginas para os pontos avaliados.",
  acao="Esclarecer no Q&A", responsavel="Bid Manager",
  pergunta="Quais subcritérios, evidências esperadas e escala de notas serão usados em cada critério técnico do item 6.2?")
I("d01_contr_pontos", "D01", "6. Critérios de avaliação, item 6.2", "A: p. 4 (impressa: 3), item 6.2 · B: p. 4 (impressa: 3), tabela do item 6.2",
  'A: "A Nota Técnica, de no máximo 60 (sessenta) pontos" · B: "Metodologia de operação do SOC 20 [...] Qualificação da equipe 20 [...] Ferramentas e tecnologia 15 [...] Plano de transição 10"',
  "Contradição", "Administrativo do processo",
  "Os critérios somam 65 pontos, mas a Nota Técnica tem máximo de 60. Afeta o corte de 70% do item 6.3 (42 ou 45,5 pontos) e o peso relativo de cada critério; "
  "a dedução da aba oculta Pesos ({d04_pesos_regra}) agrava a incerteza.",
  s=4, p=3, impacto="Incerteza sobre a nota mínima para não ser desclassificado e sobre onde investir esforço técnico.",
  rel=["d01_crit_metod", "d01_crit_equipe", "d01_crit_ferr", "d01_crit_trans", "d01_corte70", "d04_pesos_regra"],
  acao="Esclarecer no Q&A", responsavel="Bid Manager",
  pergunta="Os critérios do item 6.2 somam 65 pontos, mas a Nota Técnica máxima é de 60. Qual a pontuação correta de cada critério e qual a nota mínima exigida no item 6.3?")
I("d01_corte70", "D01", "6. Critérios de avaliação, item 6.3", P4,
  '"Serão desclassificadas as propostas com Nota Técnica inferior a 70% (setenta por cento) da pontuação máxima."',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Nota de corte técnica. A desclassificação depende da nota atribuída, por isso a probabilidade fica em 3. A base (60 ou 65 pontos) é incerta ({d01_contr_pontos}).",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Desclassificação.", rel=["d01_contr_pontos", "d04_pesos_regra"],
  acao="Mitigar", responsavel="Bid Manager")
I("d01_desempate", "D01", "6. Critérios de avaliação, item 6.4", P4,
  '"Em caso de empate na nota final, prevalecerá a proposta de menor preço."', "Critério de avaliação / pontuação", "Comercial/Preço",
  "Desempate por menor preço. Probabilidade 2: empate exato na nota final é pouco provável.", s=2, p=2,
  impacto="Reforça o peso do preço apenas em caso de empate.", acao="Nenhuma (informativo)", responsavel="Pricing/Financeiro")
I("d01_vigencia", "D01", "7. Condições comerciais e contratuais, item 7.1", P5,
  '"O contrato terá vigência de 36 (trinta e seis) meses, prorrogável por iguais períodos mediante acordo entre as partes."',
  "Obrigação contratual", "Jurídico/Contratual / Comercial/Preço",
  "Horizonte de 36 meses para amortizar transição, operação paralela sem custo e plataformas. Não há cláusula de rescisão antecipada nem de devolução de dados ao término.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Base da amortização dos investimentos iniciais.",
  acao="Precificar", responsavel="Pricing/Financeiro")
I("d01_reajuste", "D01", "7. Condições comerciais e contratuais, item 7.2", P5,
  '"Os preços serão reajustados anualmente pela variação do IPCA."', "Obrigação contratual", "Financeiro",
  "Não informa a data-base do reajuste. O principal custo (pessoal) é reajustado por convenção coletiva, que pode divergir do IPCA.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Possível perda de margem ao longo de 36 meses.",
  acao="Esclarecer no Q&A", responsavel="Pricing/Financeiro",
  pergunta="Qual a data-base do reajuste pelo IPCA: data de apresentação da proposta ou data de assinatura do contrato?")
I("d01_pagamento", "D01", "7. Condições comerciais e contratuais, item 7.3", P5,
  '"O pagamento será efetuado em até 60 (sessenta) dias após o aceite da nota fiscal."', "Obrigação contratual", "Financeiro",
  "Probabilidade 5: o prazo de 60 dias é explícito e gera custo financeiro certo de capital de giro. O prazo para aceite da nota não é definido e pode estender o recebimento.",
  obrigatoriedade="Mandatório", s=3, p=5, impacto="Custo financeiro a incluir no preço.",
  acao="Precificar", responsavel="Pricing/Financeiro",
  pergunta="Qual o prazo máximo para o aceite da nota fiscal após sua emissão? Há juros ou correção em caso de atraso no pagamento?")
I("d01_multa", "D01", "7. Condições comerciais e contratuais, item 7.4", P5,
  '"multa de 10% (dez por cento) do valor mensal do contrato, por ocorrência"', "Penalidade / multa / glosa", "Jurídico/Contratual / Financeiro",
  "Multa por ocorrência em qualquer SLA do Anexo I, sem teto, sem gradação por gravidade e sem carência. Três ocorrências no mês equivalem a 30% da fatura mensal. "
  "Probabilidade 4: o texto prevê aplicação a cada ocorrência, o volume de cerca de 1.200 alertas por dia ({d03_alertas}) torna frequentes os eventos sujeitos ao "
  "SLA de 15 minutos, e o Q&A nº 4 recusou limitar as multas ({d04_risco_juridico}).",
  obrigatoriedade="Mandatório", s=5, p=4, impacto="Exposição financeira sem limite, que pode superar a margem do contrato.",
  framework=CC, controle="Cláusula penal — art. 412", associacao="Correlata",
  rel=["d01_amb_ocorrencia", "d04_risco_juridico", "d02_sla_15min", "d02_sla_disp", "d02_relatorio_mensal"],
  acao="Propor exceção/ressalva", responsavel="Jurídico",
  pergunta="Será admitida gradação da multa por severidade do SLA, limite mensal e global das multas (percentual da fatura mensal) e carência durante a estabilização pós-transição?")
I("d01_amb_ocorrencia", "D01", "7. Condições comerciais e contratuais, item 7.4", P5,
  '"O descumprimento de qualquer nível de serviço (SLA) previsto no Anexo I sujeitará a Contratada a multa"', "Ambiguidade", "Jurídico/Contratual",
  "Não define 'ocorrência' (cada incidente fora de 15 minutos, cada mês abaixo de 99,9%, cada relatório atrasado), nem se prazos fora da seção de SLA do Anexo I "
  "(revogação em 24 horas, recertificação trimestral) sujeitam à multa, nem a base do 'valor mensal do contrato'.",
  s=4, p=3, impacto="A diferença entre interpretações multiplica a exposição a multas.",
  rel=["d01_multa", "d02_revogacao24h", "d02_relatorio_mensal"], acao="Esclarecer no Q&A", responsavel="Jurídico",
  pergunta="O que constitui 'ocorrência' para fins do item 7.4 em cada SLA do Anexo I? Os prazos dos itens 3.1 e 3.3 do Anexo I são SLAs sujeitos a multa? Qual a base do 'valor mensal do contrato'?")
I("d01_resp_ilimitada", "D01", "7. Condições comerciais e contratuais, item 7.5", P5,
  '"A Contratada responderá de forma integral e ilimitada por quaisquer danos decorrentes de incidentes de segurança ocorridos no ambiente do Contratante."',
  "Obrigação contratual", "Jurídico/Contratual",
  "Responsabilidade sem limite e sem exigência de culpa ou nexo com falha da Contratada: abrange qualquer incidente no ambiente do Banco, inclusive não causado "
  "nem detectável pelo SOC, e danos indiretos. O Q&A nº 4 manteve todo o item 7 ({d04_risco_juridico}).",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Exposição jurídica e financeira ilimitada.",
  framework=CC, controle="Perdas e danos — arts. 402 e 403", associacao="Correlata", rel=["d04_risco_juridico", "d01_seguro"],
  acao="Propor exceção/ressalva", responsavel="Jurídico",
  pergunta="Será admitida limitação de responsabilidade da Contratada (por exemplo, ao valor anual do contrato), exclusão de danos indiretos e lucros cessantes e restrição a danos comprovadamente causados por culpa ou dolo da Contratada?")
I("d01_seguro", "D01", "7. Condições comerciais e contratuais, item 7.6", P5,
  '"seguro de responsabilidade civil cibernética em valor compatível com os riscos do contrato"', "Obrigação contratual", "Jurídico/Contratual / Financeiro",
  "Valor segurado não definido; com responsabilidade ilimitada ({d01_resp_ilimitada}) não há referência objetiva de 'valor compatível'. Não diz quando a apólice deve ser apresentada.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Custo de prêmio incerto.", rel=["d01_resp_ilimitada"],
  acao="Esclarecer no Q&A", responsavel="Jurídico",
  pergunta="Qual o valor mínimo de cobertura do seguro de responsabilidade civil cibernética e em que momento a apólice deve ser apresentada?")
I("d01_subcontratacao", "D01", "7. Condições comerciais e contratuais, item 7.7", P5,
  '"É vedada a subcontratação, total ou parcial, do objeto deste contrato."', "Restrição", "Jurídico/Contratual",
  "A vedação total pode alcançar componentes usuais do serviço: SIEM em nuvem pública ({d02_siem}), licenças e suporte de fabricantes, threat intelligence "
  "({d04_qt05}), exportação de logs do SIEM legado. Registrado como Restrição; há também ambiguidade sobre o que é subcontratação.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Pode inviabilizar o modelo de entrega com parceiros e plataformas SaaS.",
  framework=ISO, controle="A.5.19 Segurança da informação nas relações com fornecedores", associacao="Correlata",
  rel=["d02_siem", "d04_qt05"], acao="Esclarecer no Q&A", responsavel="Jurídico",
  pergunta="A contratação de serviços de nuvem pública, licenças de software (SaaS), suporte de fabricantes e feeds de threat intelligence é considerada subcontratação vedada pelo item 7.7?")
I("d01_confidencialidade", "D01", "7. Condições comerciais e contratuais, item 7.8", P5,
  '"As obrigações de confidencialidade vigorarão por 5 (cinco) anos após o término do contrato."', "Obrigação contratual", "Jurídico/Contratual",
  "Prazo de confidencialidade pós-contratual definido.", obrigatoriedade="Mandatório", s=2, p=3,
  impacto="Obrigação de longo prazo, usual.", framework=ISO, controle="A.6.6 Acordos de confidencialidade ou de não divulgação",
  associacao="Direta", acao="Atender", responsavel="Jurídico")
I("d01_anexo3_decl", "D01", "Anexo III — Declaração de Localização de Dados", P6,
  '"Esta declaração deverá ser entregue assinada pelo representante legal do proponente junto com a proposta, sob pena de inabilitação."',
  "Critério eliminatório / de habilitação", "Administrativo do processo / Regulatório/Compliance",
  "Probabilidade 5: a inabilitação está expressa. A exigência só aparece no anexo escaneado da última página: não consta do item 5.1 nem das instruções do item 4, "
  "o que aumenta o risco de omissão. O modelo traz data 'de 2026'.",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação.", rel=["d01_ocr", "d01_anexo3_dados"],
  acao="Atender", responsavel="Jurídico")
I("d01_anexo3_dados", "D01", "Anexo III — Declaração de Localização de Dados", P6,
  '"todos os dados do Banco Horizonte Fictício S.A., incluindo os registros (logs) de segurança, serão armazenados e processados exclusivamente em território nacional"',
  "Restrição", "Infraestrutura/Cloud / Privacidade/Proteção de Dados",
  "Ao assinar, o proponente se obriga a manter dados e logs exclusivamente no Brasil durante toda a vigência: restringe nuvem e região do SIEM, backups, "
  "ferramentas SaaS e suporte de fabricante a partir do exterior. Conflita com a região de livre escolha do Anexo I ({d02_contr_nuvem}).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Limita a oferta de SIEM SaaS e pode encarecer a plataforma.",
  framework=LGPD, controle="Transferência internacional de dados — art. 33", associacao="Correlata",
  rel=["d02_contr_nuvem", "d01_anexo3_decl"], acao="Precificar", responsavel="Pré-venda/Arquitetura")

# =============================================================== D02 — Anexo I
S1 = "§ 1. Serviços de SOC"
S2 = "§ 2. Níveis de serviço (SLA)"
S3 = "§ 3. Gestão de identidades e acessos (IAM)"
I("d02_inv", "D02", "Inventário do documento", "§ início do documento a § 6",
  '"RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Versão 1.0 — 15/10/2026"', "Registro de cobertura", "Administrativo do processo",
  "Documento Word com 6 seções numeradas (22 parágrafos, sem tabelas), versão 1.0 de 15/10/2026, processado integralmente. Sem marcas de revisão nem "
  "comentários sinalizados. Localizador por seção e item; sem número de página.")
I("d02_monitoramento", "D02", S1 + ", item 1.1", S1 + ", item 1.1",
  '"O proponente deverá prestar serviço de monitoramento contínuo de eventos de segurança, em regime 24x7x365."',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Repete o objeto da RFP ({d01_objeto_soc}).", obrigatoriedade="Mandatório", s=3, p=3,
  impacto="Turnos 24x7.", framework=ISO + " · " + NIST, controle="A.8.16 Atividades de monitoramento · DE.CM Monitoramento contínuo",
  associacao="Direta", vigencia="Duplicado", rel=["d01_objeto_soc"], acao="Precificar", responsavel="Delivery/Operação")
I("d02_siem", "D02", S1 + ", item 1.2", S1 + ", item 1.2", '"O proponente deverá fornecer a solução de SIEM"',
  "Requisito funcional / de serviço", "Técnico/Arquitetura / Infraestrutura/Cloud",
  "O proponente arca com plataforma, licenças e infraestrutura do SIEM; o custo depende da volumetria que o Banco recusou informar ({d04_lac_eps}) e da retenção "
  "({d02_contr_retencao}). Não diz se licenças e dados ficam com o Banco ao término.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Principal componente de custo de tecnologia do SOC.",
  framework=ISO, controle="A.8.16 Atividades de monitoramento", associacao="Correlata",
  rel=["d04_lac_eps", "d02_contr_retencao", "d02_contr_nuvem"], acao="Precificar", responsavel="Pré-venda/Arquitetura",
  pergunta="Ao término do contrato, a plataforma SIEM, as licenças e os logs armazenados serão transferidos ao Banco ou ao novo fornecedor? Em que formato?")
I("d02_contr_nuvem", "D02", S1 + ", item 1.2 × Anexo III da RFP", "A: D02 " + S1 + ", item 1.2 · B: D01 p. 6 (impressa: 5) (OCR)",
  'A: "podendo esta ser disponibilizada em nuvem pública, em região de livre escolha do proponente" · B: "serão armazenados e processados exclusivamente em território nacional"',
  "Contradição", "Infraestrutura/Cloud / Regulatório/Compliance",
  "O Anexo I admite SIEM em nuvem pública em qualquer região, mas a declaração do Anexo III, exigida sob pena de inabilitação, obriga armazenar e processar dados "
  "e logs só no Brasil. A Resolução CMN nº 4.893/2021 ({d01_cmn}) também trata de nuvem. Região no exterior torna a declaração falsa; restringir ao Brasil muda custo e oferta de SIEM SaaS.",
  s=4, p=3, impacto="Escolha errada de arquitetura gera descumprimento contratual ou proposta mais cara.",
  framework=ISO, controle="A.5.23 Segurança da informação para uso de serviços em nuvem", associacao="Correlata",
  rel=["d02_siem", "d01_anexo3_dados", "d01_cmn"], acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura",
  pergunta="O SIEM em nuvem pública pode ser hospedado em região fora do Brasil, conforme o item 1.2 do Anexo I, ou deve observar a declaração do Anexo III "
  "(armazenamento e processamento exclusivamente em território nacional)? A restrição alcança backups, réplicas de recuperação de desastre e suporte do fabricante a partir do exterior?")
I("d02_retencao12", "D02", S1 + ", item 1.3", S1 + ", item 1.3",
  '"Os registros (logs) de segurança deverão ser retidos por no mínimo 12 (doze) meses."', "Requisito não funcional", "Segurança da Informação/Cyber",
  "Retenção mínima de 12 meses, contraditória com os 5 anos do item 1.6 ({d02_contr_retencao}).", obrigatoriedade="Mandatório", s=3, p=3,
  impacto="Custo de armazenamento.", framework=ISO, controle="A.8.15 Registro de logs", associacao="Direta",
  vigencia="Em esclarecimento", rel=["d02_contr_retencao"], acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura")
I("d02_lgpd_operador", "D02", S1 + ", itens 1.3 e 3.1", S1 + ", item 1.3",
  '"Os registros (logs) de segurança deverão ser retidos por no mínimo 12 (doze) meses."', "Requisito implícito", "Privacidade/Proteção de Dados",
  "Inferido: logs de segurança contêm dados pessoais (usuários, IPs, atividades de milhares de colaboradores) e o IAM trata dados cadastrais e de RH. Ao coletar, "
  "reter e analisar esses dados em nome do Banco, o proponente atua como operador na LGPD. A RFP não traz cláusula de proteção de dados nem acordo de tratamento.",
  obrigatoriedade="Mandatório", natureza="Inferida", s=3, p=3, impacto="Obrigações de operador (segurança, notificação, eliminação) a precificar e contratar.",
  framework=LGPD, controle="Operador — art. 39 (tratamento segundo as instruções do controlador)", associacao="Direta",
  acao="Registrar premissa na proposta", responsavel="Compliance",
  pergunta="O Banco celebrará acordo de tratamento de dados pessoais com a Contratada? Quais obrigações de operador (prazo de notificação de incidentes, eliminação de dados ao fim do contrato) serão exigidas?")
I("d02_integracao_ativos", "D02", S1 + ", item 1.4", S1 + ", item 1.4",
  '"O SIEM deverá ser integrado a todos os ativos relevantes do Contratante."', "Ambiguidade", "Técnico/Arquitetura",
  "'Ativos relevantes' não é definido nem quantificado. O ambiente tem 850 servidores, 2 data centers e 2 nuvens públicas ({d03_servidores}, {d03_nuvens}); "
  "o Banco recusou informar o EPS ({d04_lac_eps}). O número de fontes define esforço de integração e licenciamento.",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Escopo de integração aberto: risco de subdimensionar conectores e ingestão.",
  rel=["d03_servidores", "d03_nuvens", "d04_lac_eps"], acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura",
  pergunta="Quais ativos são considerados relevantes para integração ao SIEM? Solicitamos o quantitativo por tipo de fonte (servidores, estações, rede, segurança, aplicações, nuvem, bancos de dados).")
I("d02_resposta", "D02", S1 + ", item 1.5", S1 + ", item 1.5",
  '"O serviço deverá contemplar resposta a incidentes, incluindo contenção, erradicação"', "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Contenção e erradicação exigem atuação no ambiente do Banco (bloqueios, isolamento, alteração de regras). Não define se a execução é remota ou presencial, com "
  "que privilégios e com que aprovação; somada à responsabilidade ilimitada ({d01_resp_ilimitada}), a atuação direta amplia a exposição.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Esforço de resposta e exposição jurídica por ações no ambiente do cliente.",
  framework=NIST + " · " + ISO, controle="RS.MI Mitigação de incidentes · A.5.26 Resposta a incidentes de segurança da informação", associacao="Direta",
  rel=["d01_resp_ilimitada"], acao="Esclarecer no Q&A", responsavel="Segurança/Cyber",
  pergunta="As ações de contenção e erradicação serão executadas pela Contratada diretamente nos ativos do Banco ou recomendadas para execução pelas equipes do Banco? Há necessidade de atendimento presencial?")
I("d02_relatorio_pos", "D02", S1 + ", item 1.5", S1 + ", item 1.5", '"elaboração de relatório pós-incidente"',
  "Entregável", "Segurança da Informação/Cyber", "Relatório por incidente; modelo e prazo de entrega não definidos.",
  obrigatoriedade="Mandatório", s=2, p=3, impacto="Esforço recorrente por incidente.",
  framework=ISO, controle="A.5.27 Aprendizado com incidentes de segurança da informação", associacao="Direta",
  acao="Atender", responsavel="Segurança/Cyber")
I("d02_retencao5a", "D02", S1 + ", item 1.6", S1 + ", item 1.6",
  '"Para fins de auditoria, os logs deverão ser mantidos por 5 (cinco) anos."', "Requisito não funcional", "Segurança da Informação/Cyber / Regulatório/Compliance",
  "Retenção de 5 anos, contraditória com os 12 meses do item 1.3 ({d02_contr_retencao}).", obrigatoriedade="Mandatório", s=3, p=3,
  impacto="Custo de armazenamento de longo prazo.", framework=ISO, controle="A.8.15 Registro de logs", associacao="Direta",
  vigencia="Em esclarecimento", rel=["d02_contr_retencao"], acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura")
I("d02_contr_retencao", "D02", S1 + ", itens 1.3 e 1.6", "A: D02 " + S1 + ", item 1.3 · B: D02 " + S1 + ", item 1.6",
  'A: "deverão ser retidos por no mínimo 12 (doze) meses" · B: "os logs deverão ser mantidos por 5 (cinco) anos"', "Contradição", "Técnico/Arquitetura",
  "Retenção de 12 meses e de 5 anos para os mesmos logs. Pode ser 12 meses online e 5 anos em arquivo (o questionário fala em retenção online, {d04_qt03}), mas isso "
  "não está escrito. Também não se diz se os 24 meses de logs históricos a migrar ({d03_migracao}) entram nessa retenção. A diferença de armazenamento é material.",
  s=4, p=3, impacto="Diferença de até 5 vezes no volume armazenado.",
  rel=["d02_retencao12", "d02_retencao5a", "d04_qt03", "d03_migracao"], acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura",
  pergunta="Os logs devem ser retidos por 12 meses em base online pesquisável e por 5 anos em arquivo? Em que formato e com que prazo de recuperação os logs arquivados "
  "devem ser disponibilizados? A retenção de 5 anos vale também para os logs históricos migrados do SIEM legado?")
I("d02_sla_15min", "D02", S2 + ", item 2.1", S2 + ", item 2.1",
  '"Tempo máximo para início do tratamento de incidentes críticos: 15 (quinze) minutos."', "SLA / KPI", "Operação/Serviços",
  "Sujeito à multa de 10% por ocorrência ({d01_multa}). Não define 'início do tratamento', forma de medição nem o que é incidente crítico, que depende da matriz do Contratante ({d02_lac_matriz}).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Dimensionamento de analistas 24x7 e exposição a multas.",
  framework=ITIL, controle="Prática de gerenciamento de nível de serviço", associacao="Correlata",
  rel=["d01_multa", "d02_lac_matriz"], acao="Esclarecer no Q&A", responsavel="Delivery/Operação",
  pergunta="Como é medido o início do tratamento (a partir do alerta no SIEM, da abertura do chamado ou da classificação do incidente) e qual ferramenta é a fonte oficial da medição?")
I("d02_sla_disp", "D02", S2 + ", item 2.2", S2 + ", item 2.2",
  '"Disponibilidade mínima mensal da plataforma SIEM: 99,9%."', "SLA / KPI", "Infraestrutura/Cloud",
  "99,9% mensal admite cerca de 43 minutos de indisponibilidade por mês. Não define manutenção programada, exclusões (falha do provedor de nuvem ou da rede do Banco) "
  "nem método de medição. Sujeito à multa por ocorrência ({d01_multa}).",
  obrigatoriedade="Mandatório", s=4, p=3, impacto="Exige arquitetura redundante e expõe a multas.",
  framework=ITIL, controle="Prática de gerenciamento de disponibilidade", associacao="Direta", rel=["d01_multa"],
  acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura",
  pergunta="Janelas de manutenção programada e indisponibilidades causadas pelo provedor de nuvem ou pela rede do Banco são excluídas do cálculo de disponibilidade? Qual o método de medição?")
I("d02_relatorio_mensal", "D02", S2 + ", item 2.3", S2 + ", item 2.3",
  '"Relatório mensal de indicadores, a ser entregue até o 5º dia útil do mês subsequente."', "SLA / KPI", "Operação/Serviços",
  "Por estar na seção de SLA, o atraso pode ser tratado como descumprimento sujeito à multa de 10% ({d01_multa}), desproporcional ao item. Indicadores do relatório não especificados. Também é um entregável.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Multa desproporcional por atraso de relatório.",
  rel=["d01_multa", "d01_amb_ocorrencia"], acao="Esclarecer no Q&A", responsavel="Delivery/Operação",
  pergunta="Quais indicadores devem compor o relatório mensal? O atraso na entrega do relatório está sujeito à multa do item 7.4 da RFP?")
I("d02_lac_matriz", "D02", S2 + ", item 2.4", S2 + ", item 2.4",
  'Não localizado · "A classificação de criticidade dos incidentes seguirá a matriz de classificação do Contratante."', "Lacuna", "Segurança da Informação/Cyber",
  "Documento citado pelo cliente e não fornecido. A matriz define quais incidentes são críticos e, portanto, sujeitos ao SLA de 15 minutos e à multa; sem ela não "
  "se dimensiona a equipe. Também não se diz se o Banco pode alterá-la durante o contrato.",
  s=4, p=3, impacto="SLA de 15 minutos sem base para dimensionamento.", rel=["d02_sla_15min"],
  framework=ISO, controle="A.5.25 Avaliação e decisão sobre eventos de segurança da informação", associacao="Correlata",
  acao="Esclarecer no Q&A", responsavel="Segurança/Cyber",
  pendencia="matriz de classificação de incidentes do Contratante citada e não fornecida",
  pergunta="Solicitamos a matriz de classificação de criticidade de incidentes do Contratante e a volumetria histórica de incidentes por nível. Alterações da matriz durante a vigência dependerão de acordo entre as partes?")
I("d02_iam_ciclo", "D02", S3 + ", item 3.1", S3 + ", item 3.1",
  '"Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"', "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Itens 3.1 a 3.3 não usam 'deverá', mas, em contraste com o 'desejável' do 3.4, foram tratados como mandatórios. Pressupõe integração com o sistema de RH "
  "(fonte autoritativa), não mencionada nas responsabilidades do Contratante.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Esforço de automação, partindo de AD e scripts ({d03_iam_atual}).",
  framework=ISO, controle="A.5.16 Gestão de identidade", associacao="Direta", rel=["d03_iam_atual", "d02_lac_ferramenta_iam"],
  acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d02_revogacao24h", "D02", S3 + ", item 3.1", S3 + ", item 3.1",
  '"com revogação dos acessos de colaboradores desligados em até 24 (vinte e quatro) horas"', "SLA / KPI", "Segurança da Informação/Cyber",
  "Prazo mensurável fora da seção de SLA; não está claro se sujeita à multa ({d01_amb_ocorrencia}). O cumprimento depende de o RH do Banco comunicar o desligamento, "
  "dependência não listada na seção 6.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Possível multa por atraso causado por terceiros.",
  framework=ISO, controle="A.5.18 Direitos de acesso", associacao="Direta", rel=["d01_amb_ocorrencia"],
  acao="Esclarecer no Q&A", responsavel="Delivery/Operação",
  pergunta="O prazo de 24 horas conta a partir de qual evento (registro do desligamento no sistema de RH ou comunicação formal à Contratada)? Haverá integração automática com o sistema de RH?")
I("d02_lac_ferramenta_iam", "D02", S3, S3,
  'Não localizado · "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM)"', "Lacuna", "Técnico/Arquitetura / Comercial/Preço",
  "O Anexo I descreve processos de IAM sem dizer se o proponente fornece plataforma de governança de identidades, MFA e PAM ou opera ferramentas do Banco. "
  "O ambiente atual é Active Directory com scripts e não há PAM ({d03_iam_atual}). Operar ou fornecer muda preço e prazo de transição.",
  s=4, p=3, impacto="Diferença material de preço (licenças, implantação) e de prazo.",
  rel=["d01_objeto_iam", "d03_iam_atual", "d02_pam"], acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura",
  pergunta="O proponente deve fornecer as plataformas de IAM (governança de identidades, MFA, PAM) e suas licenças, ou operará ferramentas adquiridas pelo Banco? Quais sistemas-alvo devem ser integrados ao ciclo de vida das identidades?")
I("d02_mfa", "D02", S3 + ", item 3.2", S3 + ", item 3.2",
  '"Autenticação multifator (MFA) obrigatória para 100% dos usuários com acesso privilegiado."', "Requisito não funcional", "Segurança da Informação/Cyber",
  "Número de usuários privilegiados e de sistemas cobertos não informado.", obrigatoriedade="Mandatório", s=3, p=3,
  impacto="Licenças e esforço de implantação de MFA.", framework=ISO, controle="A.8.5 Autenticação segura", associacao="Direta",
  acao="Esclarecer no Q&A", responsavel="Segurança/Cyber",
  pergunta="Qual o número de usuários e contas com acesso privilegiado e quais sistemas devem ter MFA?")
I("d02_recert", "D02", S3 + ", item 3.3", S3 + ", item 3.3", '"Revisão (recertificação) trimestral dos acessos concedidos."',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Esforço trimestral recorrente; escopo (todos os sistemas ou só críticos) e número de revisores não informados.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Esforço recorrente de operação.",
  framework=ISO, controle="A.5.18 Direitos de acesso", associacao="Direta", acao="Precificar", responsavel="Delivery/Operação")
I("d02_pam", "D02", S3 + ", item 3.4", S3 + ", item 3.4",
  '"É desejável que a solução contemple cofre de senhas para contas privilegiadas (PAM)."', "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Desejável, sem regra de pontuação na RFP; a regra da aba oculta Pesos deduz pontos de requisitos não obrigatórios respondidos 'Não atende' ({d04_pesos_regra}), "
  "embora o PAM não conste do questionário. O Banco não tem PAM hoje ({d03_pam_oport}).",
  obrigatoriedade="Desejável", s=3, p=3, impacto="Custo adicional de PAM versus possível ganho de pontuação.",
  framework=ISO, controle="A.8.2 Direitos de acesso privilegiado", associacao="Direta", rel=["d03_pam_oport", "d04_pesos_regra"],
  acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura",
  pergunta="A oferta de PAM (item 3.4 do Anexo I) será pontuada? Em qual critério do item 6.2 da RFP?")
I("d02_transicao60", "D02", "§ 4. Transição, item 4.1", "§ 4. Transição, item 4.1",
  '"A transição dos serviços deverá ser concluída em até 60 (sessenta) dias corridos a partir da assinatura do contrato."', "Prazo / marco", "Transição/Implantação",
  "Prazo de 60 dias, contraditório com os 30 dias da RFP ({d02_contr_transicao}).", obrigatoriedade="Mandatório", s=3, p=3,
  impacto="Base do plano de transição.", framework=ITIL, controle="Cadeia de valor de serviço — atividade Design e transição", associacao="Correlata",
  vigencia="Em esclarecimento", rel=["d02_contr_transicao"], acao="Esclarecer no Q&A", responsavel="Delivery/Operação")
I("d02_contr_transicao", "D02", "§ 4. Transição, item 4.1 × RFP item 3.2", "A: D01 p. 2 (impressa: 1), item 3.2 · B: D02 § 4. Transição, item 4.1",
  'A: "A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos" · B: "A transição dos serviços deverá ser concluída em até 60 (sessenta) dias corridos"',
  "Contradição", "Transição/Implantação",
  "RFP fixa 30 dias e Anexo I fixa 60 dias para a mesma transição, sem ordem de precedência ({d01_precedencia}). A diferença altera equipe de transição, custo da "
  "operação paralela ({d02_paralelo}) e o plano de transição pontuado (10 pontos). O Q&A Rodada 1 não tratou do tema.",
  s=4, p=3, impacto="Custo e risco de transição dobram entre as interpretações.",
  rel=["d01_transicao30", "d02_transicao60", "d01_precedencia", "d02_paralelo"], acao="Esclarecer no Q&A", responsavel="Delivery/Operação",
  pergunta="A RFP (item 3.2) prevê 30 dias e o Anexo I (item 4.1) prevê 60 dias para a conclusão da transição. Qual prazo prevalece?")
I("d02_paralelo", "D02", "§ 4. Transição, item 4.2", "§ 4. Transição, item 4.2",
  '"Durante a transição, o proponente deverá operar em paralelo com o fornecedor atual, sem custo adicional para o Contratante."',
  "Obrigação contratual", "Transição/Implantação / Comercial/Preço",
  "Probabilidade 5: o custo da operação paralela é exigido explicitamente sem remuneração. Duração (30 ou 60 dias) e escopo do paralelo indefinidos. O SIEM legado "
  "termina em 31/01/2027 ({d03_siem_legado}): o paralelo só é possível se a transição ocorrer antes, o que depende da assinatura ({d01_lac_assinatura}). "
  "Não se sabe se o fornecedor atual é obrigado a cooperar.",
  obrigatoriedade="Mandatório", s=3, p=5, impacto="Custo certo, não remunerado, a amortizar no preço mensal.",
  rel=["d02_contr_transicao", "d03_siem_legado", "d01_lac_assinatura"], acao="Precificar", responsavel="Pricing/Financeiro",
  pergunta="O fornecedor atual tem obrigação contratual de cooperar com a transição (repasse de conhecimento, acesso ao SIEM legado e exportação de logs)? A operação paralela deve ocorrer antes de 01/02/2027?")
I("d02_cissp", "D02", "§ 5. Equipe, item 5.1", "§ 5. Equipe, item 5.1",
  '"O serviço deverá contar com coordenador com certificação CISSP, dedicado exclusivamente ao contrato."', "Restrição", "Pessoas/Equipe",
  "Custo integral de um profissional sênior dedicado. Não diz se é presencial nem se cobre também o IAM.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Custo fixo de pessoal.", framework=ISO, controle="Cláusula 7.2 Competência",
  associacao="Correlata", rel=["d01_equipe_cert"], acao="Precificar", responsavel="RH/Staffing")
I("d02_n1_presencial", "D02", "§ 5. Equipe, item 5.2", "§ 5. Equipe, item 5.2",
  '"Os analistas de nível 1 deverão atuar presencialmente na sede do Contratante, em São Paulo/SP, em horário comercial."', "Restrição", "Pessoas/Equipe",
  "Alterado pelo Q&A nº 6 ({d04_qa6}), que admite atuação remota no Brasil. Não está claro como fica o N1 fora do horário comercial no regime 24x7.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Custo de alocação presencial em São Paulo (reduzido pelo Q&A).",
  vigencia="Alterado", rel=["d04_qa6"], acao="Atender", responsavel="RH/Staffing")
I("d02_vpn", "D02", "§ 6. Responsabilidades do Contratante, item 6.1", "§ 6. Responsabilidades do Contratante, item 6.1",
  '"Disponibilizar acesso remoto seguro (VPN) aos ambientes monitorados."', "Responsabilidade / dependência do cliente", "Infraestrutura/Cloud",
  "Dependência do cliente para a operação remota; prazo de disponibilização não definido.", s=2, p=3,
  impacto="Atraso do Banco afeta a transição.", acao="Registrar premissa na proposta", responsavel="Delivery/Operação")
I("d02_documentacao", "D02", "§ 6. Responsabilidades do Contratante, item 6.2", "§ 6. Responsabilidades do Contratante, item 6.2",
  '"Disponibilizar a documentação técnica do ambiente em até 10 (dez) dias após a assinatura do contrato."',
  "Responsabilidade / dependência do cliente", "Transição/Implantação",
  "Com transição de 30 dias ({d01_transicao30}), um terço do prazo passa sem documentação do ambiente. Não há ajuste de prazo nem suspensão de SLA por atraso do Banco.",
  s=3, p=3, impacto="Comprime a transição.", rel=["d01_transicao30", "d03_risco_transicao"],
  acao="Registrar premissa na proposta", responsavel="Delivery/Operação",
  pergunta="Atrasos na entrega da documentação técnica ou do acesso VPN pelo Banco prorrogarão, na mesma proporção, o prazo de transição e suspenderão SLAs e multas?")

# =============================================================== D03 — Apresentação
SL2 = 'slide 2 — "Números do ambiente"'
SL3 = 'slide 3 — "Ferramentas atuais"'
SL4 = 'slide 4 — "Desafios"'
SL5 = 'slide 5 — "Expectativas para o novo serviço"'
I("d03_inv", "D03", "Inventário do documento", "slides 1 a 5",
  '"Workshop com proponentes — RFP nº 2026-017 — 22/10/2026"', "Registro de cobertura", "Administrativo do processo",
  "Apresentação de 5 slides do workshop de 22/10/2026, processada integralmente, inclusive as notas do apresentador do slide 5 (única nota). Nenhum slide oculto sinalizado.")
I("d03_usuarios", "D03", "Números do ambiente", SL2, '"6.200 usuários ativos"', "Dado de dimensionamento", "Comercial/Preço",
  "Base de usuários divergente da RFP e do Q&A ({d03_contr_usuarios}, {d04_contr_usuarios}).", s=3, p=3,
  impacto="Base de preço de IAM e volume de eventos.", rel=["d03_contr_usuarios", "d04_contr_usuarios"],
  acao="Precificar", responsavel="Pricing/Financeiro")
I("d03_contr_usuarios", "D03", "Números do ambiente × RFP item 2.1", "A: D01 p. 2 (impressa: 1), item 2.1 · B: D03 slide 2",
  'A: "abrangendo aproximadamente 4.500 colaboradores" · B: "6.200 usuários ativos"', "Contradição", "Comercial/Preço",
  "Diferença de 38% entre o objeto da RFP e o ambiente apresentado. 'Colaboradores' e 'usuários ativos' podem medir coisas diferentes (terceiros, contas de serviço), "
  "mas nenhum documento explica. O Q&A nº 5 indicou 5.000 ({d04_contr_usuarios}).",
  s=4, p=3, impacto="Licenças de IAM e MFA, volume de eventos e esforço de recertificação mudam em dezenas de por cento.",
  rel=["d01_usuarios", "d03_usuarios", "d04_contr_usuarios"], acao="Esclarecer no Q&A", responsavel="Pricing/Financeiro",
  pergunta="A RFP indica cerca de 4.500 colaboradores e a apresentação, 6.200 usuários ativos. Qual a composição dos 6.200 (colaboradores, terceiros, contas de serviço) e qual base deve ser usada para SOC e para IAM?")
I("d03_servidores", "D03", "Números do ambiente", SL2, '"850 servidores (70% Windows, 30% Linux)"', "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Principal referência de fontes de log de servidores; estações, rede e aplicações não informadas.", s=3, p=3,
  impacto="Base para estimar integração e ingestão do SIEM.", rel=["d02_integracao_ativos"], acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d03_dcs", "D03", "Números do ambiente", SL2, '"2 data centers próprios (São Paulo e Campinas)"', "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Duas localidades a integrar (coletores de log, conectividade).", s=2, p=3, impacto="Coletores e links em duas localidades.",
  acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d03_nuvens", "D03", "Números do ambiente", SL2, 'Não localizado · "Workloads em 2 nuvens públicas"', "Lacuna", "Infraestrutura/Cloud",
  "Provedores, serviços e volume de workloads em nuvem não identificados. Afetam conectores e ingestão no SIEM e devem respeitar a restrição de dados no Brasil ({d01_anexo3_dados}).",
  s=3, p=3, impacto="Escopo de monitoramento de nuvem indefinido.", rel=["d02_integracao_ativos", "d01_anexo3_dados"],
  acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura",
  pergunta="Quais provedores de nuvem pública e quais contas e serviços devem ser monitorados? Qual o volume aproximado de workloads?")
I("d03_siem_legado", "D03", "Ferramentas atuais", SL3, '"SIEM legado — contrato encerra em 31/01/2027, sem possibilidade de prorrogação"',
  "Prazo / marco", "Transição/Implantação",
  "Data-limite rígida do SIEM atual, coincidente com o início previsto dos serviços ({d01_inicio}). Informação dada só no workshop. Base do risco combinado {d03_risco_transicao}.",
  s=3, p=3, impacto="Sem margem para atraso na entrada em operação do novo SIEM.", rel=["d01_inicio", "d03_risco_transicao"],
  acao="Mitigar", responsavel="Delivery/Operação")
I("d03_risco_transicao", "D03", "Ferramentas atuais (risco combinado de transição)", SL3,
  '"contrato encerra em 31/01/2027, sem possibilidade de prorrogação"', "Risco para o proponente", "Transição/Implantação",
  "Risco combinado: transição de 30 ou 60 dias contada de assinatura sem data ({d01_transicao30}, {d02_transicao60}, {d01_lac_assinatura}); SIEM legado encerra em "
  "31/01/2027 sem prorrogação; documentação só até 10 dias após a assinatura ({d02_documentacao}); migração de 24 meses de logs dependente do legado ({d03_migracao}); "
  "operação paralela sem custo ({d02_paralelo}); multa de 10% por ocorrência sem teto desde o início ({d01_multa}). Probabilidade 4: a data do legado é expressamente "
  "improrrogável, a multa incide a cada ocorrência e o Q&A nº 4 manteve o item 7 sem limite.",
  natureza="Inferida", s=5, p=4,
  impacto="Multas desde o primeiro mês, custo de aceleração da transição e risco de perder os logs históricos se não forem exportados até 31/01/2027.",
  framework=ITIL, controle="Cadeia de valor de serviço — atividade Design e transição", associacao="Correlata",
  rel=["d01_transicao30", "d02_transicao60", "d01_lac_assinatura", "d03_siem_legado", "d02_documentacao", "d03_migracao", "d02_paralelo", "d01_multa", "d04_risco_juridico"],
  acao="Avaliar Go/No-Go", responsavel="Delivery/Operação",
  pergunta="Solicitamos carência na aplicação de SLAs e multas nos primeiros 90 dias de operação e confirmação de que o Banco garantirá acesso ao SIEM legado e a exportação dos logs históricos até 31/01/2027.")
I("d03_iam_atual", "D03", "Ferramentas atuais", SL3, '"IAM: Active Directory + scripts internos"', "Dado de dimensionamento", "Técnico/Arquitetura",
  "Sem plataforma de governança de identidades: ciclo de vida e recertificação ({d02_iam_ciclo}, {d02_recert}) partem de processos manuais e scripts. Ligado à lacuna sobre quem fornece a ferramenta ({d02_lac_ferramenta_iam}).",
  s=3, p=3, impacto="Maior esforço de implantação de IAM.", rel=["d02_iam_ciclo", "d02_recert", "d02_lac_ferramenta_iam"],
  acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d03_pam_oport", "D03", "Ferramentas atuais", SL3, '"Não há solução de PAM"', "Oportunidade / diferencial", "Segurança da Informação/Cyber",
  "O PAM é desejável no Anexo I ({d02_pam}) e o Banco não tem solução: oferta de PAM pode diferenciar a proposta, se for pontuada.",
  impacto="Possível ganho no critério Ferramentas e tecnologia.", framework=ISO, controle="A.8.2 Direitos de acesso privilegiado",
  associacao="Correlata", rel=["d02_pam"], acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d03_alertas", "D03", "Desafios", SL4, '"Cerca de 1.200 alertas por dia"', "Dado de dimensionamento", "Operação/Serviços",
  "Único indicador de volume fornecido; não substitui o EPS ({d04_lac_eps}). Base para dimensionar N1 e estimar a frequência de eventos sujeitos ao SLA de 15 minutos.",
  s=3, p=3, impacto="Dimensionamento da equipe de triagem.", rel=["d04_lac_eps", "d02_sla_15min"], acao="Precificar", responsavel="Delivery/Operação")
I("d03_fp70", "D03", "Desafios", SL4, '"70% de falsos positivos"', "Dado de dimensionamento", "Operação/Serviços",
  "Indica regras de correlação mal ajustadas no legado; exige esforço de ajuste na transição.", s=2, p=3,
  impacto="Esforço de tuning no início da operação.", rel=["d03_meta_fp"], acao="Precificar", responsavel="Delivery/Operação")
I("d03_meta_fp", "D03", "Desafios", SL4, '"Meta: reduzir os falsos positivos para 10% no primeiro trimestre de operação"', "Ambiguidade", "Operação/Serviços",
  "Meta agressiva (de 70% para 10% em 3 meses) apresentada só no workshop, sem previsão no Anexo I. Não está claro se é SLA contratual sujeito à multa do item 7.4, "
  "critério de avaliação ou expectativa, nem como falso positivo será medido.",
  s=4, p=3, impacto="Se vinculante, nova fonte de multas sem teto já no primeiro trimestre.", rel=["d03_fp70", "d01_multa"],
  acao="Esclarecer no Q&A", responsavel="Delivery/Operação",
  pergunta="A meta de reduzir falsos positivos para 10% no primeiro trimestre é obrigação contratual (SLA sujeito a multa) ou expectativa não vinculante? Como serão medidos os falsos positivos?")
I("d03_migracao", "D03", "Expectativas para o novo serviço", SL5, '"Migração de 24 meses de logs históricos do SIEM legado para a nova plataforma"',
  "Ambiguidade", "Técnico/Arquitetura / Transição/Implantação",
  "Escopo relevante ausente da RFP e do Anexo I: volume, formato de exportação, cooperação do fornecedor legado e prazo (antes de 31/01/2027) não informados. "
  "Implica reter ao menos 24 meses, acima dos 12 meses do item 1.3 ({d02_contr_retencao}). Registrado como Ambiguidade (e não como requisito) porque a vinculação contratual do workshop é incerta ({d01_precedencia}).",
  s=4, p=3, impacto="Custo de migração e armazenamento não previsto, com prazo rígido.",
  rel=["d02_contr_retencao", "d03_siem_legado", "d01_precedencia"], acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura",
  pergunta="A migração de 24 meses de logs históricos do SIEM legado faz parte do escopo contratual? Em caso positivo, qual o volume, o formato de exportação, quem exporta os dados do SIEM legado e qual o prazo?")
I("d03_visao_riscos", "D03", "Expectativas para o novo serviço", SL5, '"Visão unificada de riscos para a diretoria"', "Ambiguidade", "Segurança da Informação/Cyber",
  "Expectativa sem definição (painel, relatório ou ferramenta de gestão de riscos) e sem previsão no Anexo I.", s=3, p=3,
  impacto="Escopo de relatórios executivos indefinido.", acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura",
  pergunta="O que se espera da visão unificada de riscos para a diretoria: painel no SIEM, relatório periódico ou ferramenta de gestão de riscos? Com que periodicidade e conteúdo?")
I("d03_subsidiarias", "D03", "Expectativas para o novo serviço — notas do apresentador × RFP item 2.1",
  "A: D01 p. 2 (impressa: 1), item 2.1 · B: D03 slide 5 — notas do apresentador",
  'A: "abrangendo aproximadamente 4.500 colaboradores" · B: "as subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários adicionais) também deverão ser incluídas no escopo"',
  "Contradição", "Comercial/Preço / Jurídico/Contratual",
  "Ampliação de escopo escondida nas notas do apresentador: o objeto da RFP trata do Banco e de cerca de 4.500 colaboradores; as notas incluem duas subsidiárias com "
  "cerca de 900 usuários. Envolve outras pessoas jurídicas (parte contratante, controlador na LGPD, ambientes próprios) e, numa seguradora, possivelmente outra regulação. "
  "O Q&A nº 5 não esclarece se estão incluídas.",
  s=4, p=3, impacto="Escopo e preço até 20% maiores e possível contratação com múltiplas entidades.",
  rel=["d01_usuarios", "d01_objeto_iam", "d04_qa5", "d04_contr_usuarios"], acao="Esclarecer no Q&A", responsavel="Bid Manager",
  pergunta="As subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários), mencionadas no workshop, fazem parte do escopo? Em caso positivo, serão partes do contrato, e seus ambientes estão incluídos nos números apresentados?")

# =============================================================== D04 — Q&A e Questionário
QA = 'aba "Q&A Rodada 1"'
QT = 'aba "Questionário Técnico"'
I("d04_inv", "D04", "Inventário do documento", 'abas "Instruções", "Q&A Rodada 1", "Questionário Técnico" e "Pesos" (oculta)',
  '"Questionário Técnico e Respostas aos Esclarecimentos — RFP nº 2026-017"', "Registro de cobertura", "Administrativo do processo",
  "Planilha com 4 abas: Instruções; Q&A Rodada 1 (6 perguntas respondidas em 12/11/2026); Questionário Técnico (QT-01 a QT-06); Pesos, aba OCULTA analisada "
  "(pesos por questão e regra de dedução). Processada integralmente.")
I("d04_instr_desclass", "D04", "Instruções", 'aba "Instruções" · A3', '"Questionários incompletos serão desclassificados."',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Probabilidade 5: a desclassificação está expressa. Sanção ausente do item 4.4 da RFP ({d01_questionario}).",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Desclassificação.", rel=["d01_questionario", "d04_amb_todas_abas"],
  acao="Atender", responsavel="Pré-venda/Arquitetura")
I("d04_amb_todas_abas", "D04", "Instruções", 'aba "Instruções" · A3', '"O preenchimento de todas as abas deste arquivo é obrigatório."',
  "Ambiguidade", "Administrativo do processo",
  "O arquivo junta questionário e respostas do Q&A. Literalmente, 'todas as abas' inclui o Q&A Rodada 1 (já respondido pelo Banco) e a aba oculta Pesos, sem campo "
  "para o proponente. Somado à desclassificação de questionário incompleto, a dúvida pode levar à desclassificação. Não se diz se Comentários é obrigatório.",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Risco de desclassificação por preenchimento considerado incompleto.",
  rel=["d04_instr_desclass"], acao="Esclarecer no Q&A", responsavel="Pré-venda/Arquitetura",
  pergunta="Quais abas e colunas devem ser preenchidas pelo proponente? As abas Q&A Rodada 1 e Pesos exigem algum preenchimento? A coluna Comentários é obrigatória?")
I("d04_qa1", "D04", "Q&A Rodada 1, pergunta 1 (12/11/2026) — RFP item 3.1", QA + " · E2 (pergunta 1)",
  '"A data de entrega das propostas fica prorrogada para 27/11/2026, até as 18h."', "Prazo / marco", "Administrativo do processo",
  "Altera o prazo de entrega da RFP ({d01_entrega}). Não informa se outras datas do cronograma mudaram.",
  obrigatoriedade="Mandatório", s=5, p=3, impacto="Novo prazo de entrega; perda exclui o proponente.", rel=["d01_entrega"],
  acao="Atender", responsavel="Bid Manager")
I("d04_qa2", "D04", "Q&A Rodada 1, pergunta 2 (12/11/2026) — RFP item 5.1 c", QA + " · E3 (pergunta 2)",
  '"Não. O SOC deverá estar localizado em território nacional."', "Critério eliminatório / de habilitação", "Operação/Serviços",
  "Probabilidade 5: confirma o critério de inabilitação do item 5.1 c ({d01_soc_nacional}). Trata da localização do SOC, não dos dados: não resolve a contradição sobre a região do SIEM ({d02_contr_nuvem}).",
  obrigatoriedade="Mandatório", s=5, p=5, impacto="Inabilitação se o SOC não estiver no Brasil.", vigencia="Duplicado",
  rel=["d01_soc_nacional", "d02_contr_nuvem"], acao="Atender", responsavel="Bid Manager")
I("d04_lac_eps", "D04", "Q&A Rodada 1, pergunta 3 (12/11/2026) — Anexo I item 1.4", QA + " · E4 (pergunta 3)",
  'Não localizado · "A volumetria será informada somente ao proponente vencedor."', "Lacuna", "Comercial/Preço / Técnico/Arquitetura",
  "Probabilidade 5: o Banco recusou formalmente informar o EPS, indispensável para precificar licenciamento, ingestão e armazenamento do SIEM. As referências indiretas "
  "(1.200 alertas por dia, 850 servidores) não permitem estimar EPS com segurança. Será preciso precificar com premissa explícita e cláusula de revisão.",
  s=4, p=5, impacto="Preço do SIEM sem base: risco de subprecificação por 36 meses ou de perda na Nota de Preço.",
  rel=["d02_integracao_ativos", "d02_siem", "d03_alertas"], acao="Registrar premissa na proposta", responsavel="Pricing/Financeiro",
  pergunta="Diante da recusa em informar a volumetria, o Banco aceitará que a proposta adote um EPS de referência como premissa, com revisão de preço se a volumetria real medida após a contratação for superior?")
I("d04_risco_juridico", "D04", "Q&A Rodada 1, pergunta 4 (12/11/2026) — RFP item 7.4", QA + " · E5 (pergunta 4)",
  '"As condições do item 7 permanecem inalteradas."', "Risco para o proponente", "Jurídico/Contratual",
  "Risco combinado: o Banco recusou limitar as multas e manteve todo o item 7: multa de 10% por ocorrência sem teto ({d01_multa}), responsabilidade integral e ilimitada "
  "por qualquer incidente ({d01_resp_ilimitada}) e seguro sem valor definido ({d01_seguro}). A exposição não tem limite e o seguro não a cobre. "
  "Probabilidade 4: o cliente já recusou alterar o tema no Q&A.",
  natureza="Inferida", s=5, p=4, impacto="Exposição financeira e jurídica ilimitada; pode inviabilizar a participação ou exigir reserva de risco relevante no preço.",
  framework=CC, controle="Cláusula penal — art. 412 · Perdas e danos — arts. 402 e 403", associacao="Correlata",
  rel=["d01_multa", "d01_resp_ilimitada", "d01_seguro", "d01_amb_ocorrencia"], acao="Avaliar Go/No-Go", responsavel="Jurídico",
  pergunta="Reiteramos o pedido de limitação de multas e de responsabilidade. O Banco aceitará proposta com ressalva que estabeleça limite agregado (por exemplo, 100% do valor anual do contrato)?")
I("d04_qa5", "D04", "Q&A Rodada 1, pergunta 5 (12/11/2026) — RFP item 2.1", QA + " · E6 (pergunta 5)", '"Considerar 5.000 usuários."',
  "Dado de dimensionamento", "Comercial/Preço",
  "Altera a base de 4.500 colaboradores da RFP ({d01_usuarios}). Não diz se vale para SOC, IAM ou ambos, nem se inclui as subsidiárias ({d03_subsidiarias}).",
  s=3, p=3, impacto="Nova base oficial de dimensionamento.", rel=["d01_usuarios", "d04_contr_usuarios", "d03_subsidiarias"],
  acao="Precificar", responsavel="Pricing/Financeiro")
I("d04_contr_usuarios", "D04", "Q&A Rodada 1, pergunta 5 × apresentação", 'A: D04 aba "Q&A Rodada 1" · E6 (pergunta 5) · B: D03 slide 2 e slide 5 (notas)',
  'A: "Considerar 5.000 usuários." · B: "6.200 usuários ativos" · "cerca de 900 usuários adicionais"', "Contradição", "Comercial/Preço",
  "A resposta oficial (5.000) é inferior aos 6.200 usuários ativos do workshop, sem contar os cerca de 900 das subsidiárias (até 7.100). Sem ordem de precedência "
  "({d01_precedencia}), não se sabe se o Q&A prevalece. Diferença de até 42% na base.",
  s=4, p=3, impacto="Subdimensionamento de licenças e equipe se a base real for maior.",
  rel=["d04_qa5", "d03_contr_usuarios", "d03_subsidiarias", "d01_precedencia"], acao="Esclarecer no Q&A", responsavel="Pricing/Financeiro",
  pergunta="A resposta à pergunta 5 indica 5.000 usuários, mas o workshop indicou 6.200 usuários ativos e cerca de 900 usuários das subsidiárias. Qual número deve ser usado para SOC e para IAM, e o preço será revisto se a base real exceder o número informado?")
I("d04_qa6", "D04", "Q&A Rodada 1, pergunta 6 (12/11/2026) — Anexo I item 5.2", QA + " · E7 (pergunta 6)", '"Sim, desde que em território nacional."',
  "Restrição", "Pessoas/Equipe",
  "Altera o item 5.2 do Anexo I ({d02_n1_presencial}): o N1 pode atuar remotamente, no Brasil. Reduz custo de alocação presencial.",
  obrigatoriedade="Mandatório", s=2, p=3, impacto="Redução de custo de pessoal.", rel=["d02_n1_presencial"], acao="Atender", responsavel="RH/Staffing")
I("d04_risco_preco", "D04", "Q&A Rodada 1, pergunta 3 (risco combinado de precificação)", QA + " · E4 (pergunta 3)",
  '"A volumetria será informada somente ao proponente vencedor."', "Risco para o proponente", "Comercial/Preço",
  "Risco combinado: EPS recusado ({d04_lac_eps}); usuários entre 4.500 e 7.100 ({d04_contr_usuarios}, {d03_subsidiarias}); ativos relevantes indefinidos "
  "({d02_integracao_ativos}); retenção de 12 meses ou 5 anos ({d02_contr_retencao}); migração de logs sem volume ({d03_migracao}); planilha de preços não fornecida "
  "({d01_lac_anexo4}); fornecimento de plataforma de IAM indefinido ({d02_lac_ferramenta_iam}); contrato de 36 meses sem revisão por volume. "
  "Probabilidade 4: o Banco recusou formalmente a informação de volumetria.",
  natureza="Inferida", s=5, p=4, impacto="Preço subdimensionado (perda de margem em 36 meses) ou superdimensionado (perda na Nota de Preço, 40% da nota final).",
  rel=["d04_lac_eps", "d04_contr_usuarios", "d03_subsidiarias", "d02_integracao_ativos", "d02_contr_retencao", "d03_migracao", "d01_lac_anexo4", "d02_lac_ferramenta_iam"],
  acao="Registrar premissa na proposta", responsavel="Pricing/Financeiro",
  pergunta="O Banco aceitará cláusula de revisão de preço por faixas de volumetria (EPS, usuários e ativos integrados) medidas após a contratação?")
I("d04_qt01", "D04", "Questionário Técnico, QT-01", QT + ' · linha 2 (QT-01) · aba "Pesos" · B2',
  '"Possui certificação ISO/IEC 27001 com escopo que inclua os serviços de SOC?"', "Critério de avaliação / pontuação", "Segurança da Informação/Cyber",
  "Obrigatório; peso 3 na aba oculta Pesos. Repete o critério de habilitação 5.1 a ({d01_iso}).", obrigatoriedade="Mandatório", s=3, p=3,
  impacto="Pontuação e habilitação.", framework=ISO, controle="Certificação do SGSI — requisitos das cláusulas 4 a 10", associacao="Direta",
  vigencia="Duplicado", rel=["d01_iso"], acao="Atender", responsavel="Compliance")
I("d04_qt02", "D04", "Questionário Técnico, QT-02", QT + ' · linha 3 (QT-02) · aba "Pesos" · B3',
  '"Oferece integração nativa com plataforma SOAR?"', "Critério de avaliação / pontuação", "Técnico/Arquitetura",
  "Não obrigatório; peso 1. SOAR não é citado na RFP nem no Anexo I; pela regra oculta ({d04_pesos_regra}), responder 'Não atende' custa 2 pontos.",
  obrigatoriedade="Desejável", s=3, p=3, impacto="Perda de 2 pontos ou custo de SOAR.", rel=["d04_pesos_regra"],
  acao="Precificar", responsavel="Pré-venda/Arquitetura")
I("d04_qt03", "D04", "Questionário Técnico, QT-03", QT + ' · linha 4 (QT-03) · aba "Pesos" · B4',
  '"Retém os logs online por no mínimo 12 meses?"', "Critério de avaliação / pontuação", "Técnico/Arquitetura",
  "Obrigatório; peso 2. Introduz o qualificador 'online', ausente do Anexo I; sugere que os 5 anos do item 1.6 sejam em arquivo ({d02_contr_retencao}).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Define a camada de armazenamento online.", framework=ISO, controle="A.8.15 Registro de logs",
  associacao="Direta", rel=["d02_contr_retencao"], acao="Atender", responsavel="Pré-venda/Arquitetura")
I("d04_qt04", "D04", "Questionário Técnico, QT-04", QT + ' · linha 5 (QT-04) · aba "Pesos" · B5',
  '"Atende aos requisitos da Resolução CMN nº 4.893/2021?"', "Critério de avaliação / pontuação", "Regulatório/Compliance",
  "Obrigatório; peso 3. Pergunta genérica: a resolução se dirige à instituição financeira e não se diz quais requisitos a Contratada deve atender nem como comprovar ({d01_cmn}).",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Declaração genérica pode gerar obrigação contratual ampla.",
  framework=CMN, controle="Requisitos para contratação de serviços de processamento e armazenamento de dados e de computação em nuvem (identificador a confirmar)",
  associacao="Direta", rel=["d01_cmn"], acao="Esclarecer no Q&A", responsavel="Compliance",
  pergunta="Quais requisitos da Resolução CMN nº 4.893/2021 o proponente deve declarar atender na questão QT-04, e que evidências serão exigidas?")
I("d04_qt05", "D04", "Questionário Técnico, QT-05", QT + ' · linha 6 (QT-05) · aba "Pesos" · B6',
  '"Oferece serviço de threat intelligence?"', "Critério de avaliação / pontuação", "Segurança da Informação/Cyber",
  "Não obrigatório; peso 2; não citado no Anexo I. Pela regra oculta, 'Não atende' custa 2 pontos. Fornecimento por terceiro pode esbarrar na vedação de subcontratação ({d01_subcontratacao}).",
  obrigatoriedade="Desejável", s=3, p=3, impacto="Perda de 2 pontos ou custo de feeds de inteligência.",
  framework=ISO, controle="A.5.7 Inteligência de ameaças", associacao="Direta", rel=["d04_pesos_regra", "d01_subcontratacao"],
  acao="Precificar", responsavel="Segurança/Cyber")
I("d04_qt06", "D04", "Questionário Técnico, QT-06", QT + ' · linha 7 (QT-06) · aba "Pesos" · B7',
  '"Possui equipe com certificações reconhecidas pelo mercado?"', "Critério de avaliação / pontuação", "Pessoas/Equipe",
  "Obrigatório; peso 2. Tão vago quanto o item 5.2 da RFP ({d01_equipe_cert}): não diz quais certificações nem quantos profissionais.",
  obrigatoriedade="Mandatório", s=3, p=3, impacto="Resposta sem critério objetivo.", rel=["d01_equipe_cert"],
  acao="Esclarecer no Q&A", responsavel="RH/Staffing")
I("d04_pesos_uso", "D04", "Pesos (aba oculta)", 'aba "Pesos" (OCULTA) · A1:B7',
  'Não localizado · Pesos: "QT-01" = "3" · "QT-02" = "1" · "QT-03" = "2" · "QT-04" = "3" · "QT-05" = "2" · "QT-06" = "2"', "Lacuna", "Administrativo do processo",
  "A aba oculta atribui pesos às questões QT-01 a QT-06, mas nenhum documento diz como entram na Nota Técnica nem em qual critério do item 6.2. Não se sabe o efeito "
  "de 'Não atende' ou 'Parcial' em questão obrigatória.",
  s=3, p=3, impacto="Peso do questionário na nota desconhecido.", rel=["d04_pesos_regra", "d01_contr_pontos"],
  acao="Esclarecer no Q&A", responsavel="Bid Manager",
  pergunta="Como os pesos das questões do questionário técnico entram na Nota Técnica e em qual critério do item 6.2 da RFP? Qual o efeito de respostas 'Não atende' ou 'Parcial' em questões obrigatórias?")
I("d04_pesos_regra", "D04", "Pesos (aba oculta) × RFP item 6.2", 'A: D01 p. 4 (impressa: 3), item 6.2 · B: D04 aba "Pesos" (OCULTA) · A9',
  'A: "A Nota Técnica, de no máximo 60 (sessenta) pontos, será atribuída conforme os critérios abaixo" · B: "Requisitos não obrigatórios respondidos como \'Não atende\' reduzem a Nota Técnica em 2 (dois) pontos cada."',
  "Contradição", "Administrativo do processo",
  "Regra de pontuação escondida em aba oculta e ausente dos critérios do item 6.2. Penaliza requisitos não obrigatórios (QT-02 e QT-05): até 4 pontos, cerca de 7% da "
  "Nota Técnica, o que pode levar a proposta abaixo do corte de 70% ({d01_corte70}). Não se diz se 'Parcial' também desconta.",
  s=4, p=3, impacto="Perda de pontos não prevista na RFP e risco de desclassificação técnica.",
  rel=["d01_contr_pontos", "d01_corte70", "d04_qt02", "d04_qt05", "d04_pesos_uso", "d02_pam"], acao="Esclarecer no Q&A", responsavel="Bid Manager",
  pergunta="A regra de dedução de 2 pontos por requisito não obrigatório respondido 'Não atende', presente na aba Pesos, será aplicada? Ela se soma aos critérios do item 6.2 da RFP? Respostas 'Parcial' também sofrem dedução?")

DOCS = [
    dict(codigo="D01", arquivo="RFP-2026-017_Servicos_SOC_IAM.pdf", tipo="RFP", versao="Versão 1.0 — 15/10/2026"),
    dict(codigo="D02", arquivo="Anexo_I_Especificacao_Tecnica.docx", tipo="Anexo técnico", versao="Versão 1.0 — 15/10/2026"),
    dict(codigo="D03", arquivo="Apresentacao_Ambiente_Atual.pptx", tipo="Apresentação (workshop)", versao="22/10/2026"),
    dict(codigo="D04", arquivo="QA_Rodada1_e_Questionario.xlsx", tipo="Q&A e questionário técnico", versao="Q&A Rodada 1 — 12/11/2026"),
]
PROX = {1: "Anexo I — Especificação Técnica (D02), a partir do § 1",
        2: "Apresentação do Ambiente Atual (D03), a partir do slide 1",
        3: "Q&A Rodada 1 e Questionário (D04), a partir da aba Instruções"}

if __name__ == "__main__":
    stage, out = int(sys.argv[1]), sys.argv[2]
    docs = []
    for i, d in enumerate(DOCS, 1):
        d = dict(d)
        d["situacao"] = "processado" if i <= stage else "pendente"
        docs.append(d)
    keep = {d["codigo"] for d in docs if d["situacao"] == "processado"}
    status = {"final": True} if stage == 4 else {"final": False, "proximo": PROX[stage], "parte": stage, "concluidos": stage}
    data = {"processo": "RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Serviços Gerenciados de SOC e IAM",
            "documentos": docs, "itens": [it for it in itens if it["doc"] in keep], "status": status}
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f"estágio {stage}: {len(data['itens'])} itens")
