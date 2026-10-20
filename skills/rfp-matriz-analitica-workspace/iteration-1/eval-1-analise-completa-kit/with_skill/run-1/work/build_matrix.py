#!/usr/bin/env python3
"""Gera a matriz analítica da RFP 2026-017 a partir das linhas definidas abaixo."""
import re
import sys
from pathlib import Path

OUT = Path(sys.argv[1])

DOCS = {
    "D01": ("RFP-2026-017_Servicos_SOC_IAM.pdf", "v1.0 — 15/10/2026", "RFP"),
    "D02": ("Anexo_I_Especificacao_Tecnica.docx", "v1.0 — 15/10/2026", "Anexo técnico"),
    "D03": ("Apresentacao_Ambiente_Atual.pptx", "22/10/2026", "Apresentação (workshop)"),
    "D04": ("QA_Rodada1_e_Questionario.xlsx", "12/11/2026 (Q&A Rodada 1)", "Q&A e questionário"),
}
SEV = {1: "Insignificante", 2: "Menor", 3: "Moderada", 4: "Maior", 5: "Severa"}
PROB = {1: "Remota", 2: "Improvável", 3: "Possível", 4: "Provável", 5: "Quase certa"}

ROWS = []
CUR = {"doc": None}


def doc(code):
    CUR["doc"] = code


def R(key, sec, loc, ev, tipo, dom, desc, obr="Informativo", nat="Explícita", S=None, P=None, imp="—",
      fw="—", ctrl="—", assoc="Não aplicável", rel=(), status="Vigente", acao="Nenhuma (informativo)",
      perg="—", resp="Bid Manager"):
    if tipo in ("Registro de cobertura",):
        assoc = "—"
    if S is not None and P is not None and P != 3:
        assert "robabilidade" in desc, key
    ROWS.append(dict(key=key, doc=CUR["doc"], sec=sec, loc=loc, ev=ev, tipo=tipo, dom=dom, desc=desc, obr=obr,
                     nat=nat, S=S, P=P, imp=imp, fw=fw, ctrl=ctrl, assoc=assoc, rel=list(rel), status=status,
                     acao=acao, perg=perg, resp=resp))


# =============================================================================== D01
doc("D01")
R("d01_inv", "Inventário do documento", "p. 1–6 (6 páginas físicas; impressas 1–5 a partir da p. 2)",
  '"Solicitação de Proposta (RFP) nº 2026-017 [...] Versão 1.0 — 15/10/2026"',
  "Registro de cobertura", "Administrativo do processo",
  "Documento lido integralmente: p. 1 a 5 por extração de texto e p. 6 (impressa: 5) por leitura visual da imagem, pois a página é digitalização sem camada de texto (Anexo III — Declaração de Localização de Dados), analisada em {d01_anexo3} e {d01_dados_br} com localizador marcado (OCR). A numeração impressa é a física menos 1 (capa sem número). Cabeçalho repetido em todas as páginas desconsiderado.",
  imp="Cobertura integral; nenhuma pendência de leitura", rel=["d01_anexo3", "d01_dados_br"])
R("d01_regime", "1. APRESENTAÇÃO — 1.2", "p. 2 (impressa: 1)",
  '"O Banco é instituição financeira autorizada a funcionar pelo Banco Central do Brasil e está sujeito à Resolução CMN nº 4.893/2021"',
  "Registro de cobertura", "Regulatório/Compliance",
  "Regime identificado: contratação privada (sociedade anônima; RFP com entrega por portal de fornecedores do próprio Banco; nenhuma menção a licitação, edital ou modalidade pública) em setor regulado (instituição financeira supervisionada pelo Banco Central do Brasil, sujeita à Resolução CMN nº 4.893/2021). A Lei 14.133/2021 não se aplica. As associações jurídicas desta matriz usam Código Civil, LGPD e a Resolução CMN nº 4.893/2021 citada pelo cliente.",
  imp="Define a legislação aplicável à análise", rel=["d01_4893"], resp="Jurídico")
R("d01_4893", "1. APRESENTAÇÃO — 1.2", "p. 2 (impressa: 1)",
  '"está sujeito à Resolução CMN nº 4.893/2021, que dispõe sobre a política de segurança cibernética e sobre os requisitos para a contratação de serviços de processamento e armazenamento de dados e de computação em nuvem"',
  "Requisito implícito", "Regulatório/Compliance",
  "Inferência: como o proponente fornecerá o SIEM, inclusive em nuvem (Anexo I 1.2, {d02_12}), e tratará logs do Banco, a contratação tende a enquadrar-se como serviço de processamento e armazenamento de dados ou de computação em nuvem sujeito à Resolução citada. O proponente terá de aceitar as obrigações contratuais dela decorrentes (conteúdo exato a confirmar; por exemplo, acesso do regulador a informações, comunicação de incidentes, continuidade e saída) e responder ao QT-04 ({d04_qt04}). A RFP não detalha quais obrigações serão impostas.",
  obr="Mandatório", nat="Inferida", S=4, P=3,
  imp="Cláusulas regulatórias adicionais e custos de conformidade (auditorias, relatórios, localização de dados) não dimensionados no preço",
  fw="Resolução CMN nº 4.893/2021", ctrl="Requisitos para contratação de processamento, armazenamento de dados e computação em nuvem (identificador a confirmar)",
  assoc="Direta", rel=["d02_contr_regiao", "d04_qt04"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Quais obrigações decorrentes da Resolução CMN nº 4.893/2021 serão incluídas no contrato (por exemplo, acesso do Banco Central a informações, notificação de incidentes, plano de continuidade e de saída)? Favor disponibilizar as cláusulas-padrão.",
  resp="Compliance")
R("d01_preced", "Documento inteiro (gatilho: 2. OBJETO — 2.2)", "p. 2–6 (todo o documento); gatilho em p. 2 (impressa: 1)",
  'Não localizado. Trecho que gera a necessidade: "As especificações técnicas detalhadas constam do Anexo I — Especificação Técnica."',
  "Lacuna", "Jurídico/Contratual / Administrativo do processo",
  "A RFP não define ordem de precedência entre RFP, Anexo I, Anexo III, material do workshop e respostas do Q&A, nem declara se as respostas do Q&A e o material do workshop integram o contrato. Há conflitos entre esses documentos (transição 30 × 60 dias, {d02_transc}; usuários 4.500 × 5.000 × 6.200, {d04_contr_users}; nuvem em região livre × dados no Brasil, {d02_contr_regiao}; N1 presencial × remoto, {d04_q6}). Não se presume que o Q&A prevaleça por ser mais recente.",
  S=4, P=3,
  imp="Sem precedência, o proponente não sabe qual versão precificar e pode ter exigida cumulativamente a versão mais onerosa em disputa contratual",
  fw="Código Civil (Lei 10.406/2002)", ctrl="Art. 113 (interpretação dos negócios jurídicos conforme a boa-fé)", assoc="Correlata",
  rel=["d02_transc", "d03_contr_users", "d04_contr_users", "d02_contr_regiao", "d02_52", "d04_q6"], status="Em esclarecimento",
  acao="Esclarecer no Q&A",
  perg="Qual a ordem de precedência entre a RFP, o Anexo I, o Anexo III, a apresentação do workshop de 22/10/2026 e as respostas do Q&A (Rodada 1)? As respostas do Q&A e o conteúdo do workshop, inclusive notas, integram o contrato?",
  resp="Jurídico")
R("d01_soc", "2. OBJETO — 2.1", "p. 2 (impressa: 1)",
  '"prestação de serviços gerenciados de Centro de Operações de Segurança (SOC), em regime 24x7x365"',
  "Requisito funcional / de serviço", "Operação/Serviços / Segurança da Informação/Cyber",
  "Objeto principal: SOC gerenciado com operação ininterrupta. Detalhado no Anexo I 1.1 ({d02_11}).",
  obr="Mandatório", S=3, P=3,
  imp="Define escala mínima de turnos 24x7 e o custo recorrente de pessoal",
  fw="NIST CSF 2.0", ctrl="DE.CM — Monitoramento contínuo", assoc="Direta", rel=["d02_11"], acao="Precificar",
  resp="Delivery/Operação")
R("d01_iam", "2. OBJETO — 2.1", "p. 2 (impressa: 1)",
  '"e de gestão de identidades e acessos (IAM)"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Segundo componente do objeto. O Anexo I (seção 3) lista atividades, mas não define se o proponente fornece a plataforma de IAM/IGA nem os sistemas-alvo ({d02_iam_lac}).",
  obr="Mandatório", S=3, P=3, imp="Componente de escopo com implantação e operação a precificar",
  fw="ISO/IEC 27001:2022", ctrl="A.5.16 Gestão de identidade", assoc="Direta", rel=["d02_iam_lac"], acao="Precificar",
  resp="Pré-venda/Arquitetura")
R("d01_users", "2. OBJETO — 2.1", "p. 2 (impressa: 1)",
  '"abrangendo aproximadamente 4.500 colaboradores"',
  "Dado de dimensionamento", "Comercial/Preço / Operação/Serviços",
  "Base de dimensionamento original. Divergente da apresentação (6.200 usuários ativos, {d03_contr_users}; cerca de 900 usuários das subsidiárias nas notas, {d03_subsid}) e alterada pelo Q&A nº 5 para 5.000 usuários ({d04_q5}). Colaboradores pode não equivaler a usuários (terceiros, contas de serviço).",
  S=3, P=3, imp="Volumetria de identidades é base de preço do IAM e de licenças por usuário",
  rel=["d03_contr_users", "d04_q5", "d04_contr_users"], status="Alterado", acao="Esclarecer no Q&A",
  resp="Pricing/Financeiro")
R("d01_workshop", "3. CRONOGRAMA DO PROCESSO — 3.1", "p. 2 (impressa: 1)",
  '"Workshop de apresentação do ambiente 22/10/2026"',
  "Prazo / marco", "Administrativo do processo",
  "Marco cumprido; o material do workshop é o D03. Probabilidade 2: marco já realizado, impacto residual apenas sobre o caráter vinculante do material ({d01_preced}).",
  S=2, P=2, imp="Fonte de dados de ambiente (D03) com valor contratual indefinido", rel=["d03_inv", "d01_preced"],
  resp="Bid Manager")
R("d01_perguntas", "3. CRONOGRAMA DO PROCESSO — 3.1", "p. 2 (impressa: 1)",
  '"Prazo final para envio de perguntas 05/11/2026"',
  "Prazo / marco", "Administrativo do processo",
  "Única janela de perguntas prevista no cronograma. Risco de não haver canal para os esclarecimentos desta matriz tratado em {d04_risk_qa}.",
  obr="Mandatório", S=3, P=3, imp="Dúvidas após essa data podem ficar sem resposta formal", rel=["d04_risk_qa"],
  acao="Atender", resp="Bid Manager")
R("d01_respostas", "3. CRONOGRAMA DO PROCESSO — 3.1", "p. 2 (impressa: 1)",
  '"Divulgação das respostas 12/11/2026"',
  "Prazo / marco", "Administrativo do processo",
  "Cumprido: o Q&A Rodada 1 (D04) é datado de 12/11/2026. Probabilidade 2: marco já cumprido. Restam 15 dias corridos entre as respostas e a nova data de entrega (27/11/2026).",
  S=2, P=2, imp="Janela curta para incorporar as respostas à proposta", rel=["d04_q1"], resp="Bid Manager")
R("d01_entrega", "3. CRONOGRAMA DO PROCESSO — 3.1", "p. 2 (impressa: 1)",
  '"Entrega das propostas 20/11/2026, até as 18h"',
  "Prazo / marco", "Administrativo do processo",
  "Prazo original, prorrogado para 27/11/2026, 18h, pelo Q&A nº 1 ({d04_q1}). Probabilidade 2: data clara; o impacto só ocorre por falha de controle interno ou se a RFP prevalecer sobre o Q&A ({d01_preced}). Associação de boa prática: controle de prazos de submissão.",
  obr="Mandatório", S=5, P=2, imp="Proposta intempestiva não é recebida (exclusão do processo)",
  fw="APMP Body of Knowledge", ctrl="Gestão do cronograma da proposta (identificador a confirmar)", assoc="Boa prática",
  rel=["d04_q1", "d01_preced"], status="Alterado", acao="Atender", resp="Bid Manager")
R("d01_inicio", "3. CRONOGRAMA DO PROCESSO — 3.1", "p. 2 (impressa: 1)",
  '"Início previsto dos serviços 01/02/2027"',
  "Prazo / marco", "Transição/Implantação",
  "Não está claro se 01/02/2027 é o início da operação plena (após a transição) ou o início da transição. Coincide com o dia seguinte ao fim do contrato do SIEM legado ({d03_siem_fim}). Risco combinado em {d03_risk_trans}.",
  obr="Mandatório", S=3, P=3, imp="Define a data em que o serviço precisa estar operando e sujeito a SLA",
  rel=["d01_trans30", "d01_lac_assin", "d03_risk_trans"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A data de 01/02/2027 corresponde ao início da operação plena (após a transição) ou ao início da transição?",
  resp="Delivery/Operação")
R("d01_trans30", "3. CRONOGRAMA DO PROCESSO — 3.2", "p. 2 (impressa: 1)",
  '"A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato."',
  "Prazo / marco", "Transição/Implantação",
  "Prazo de transição contado da assinatura. Contradiz o Anexo I 4.1, que fixa 60 dias ({d02_transc}).",
  obr="Mandatório", S=4, P=3,
  imp="Prazo define tamanho da equipe de implantação, custo da operação em paralelo e exposição a multas desde o início",
  fw="ISO/IEC 20000-1", ctrl="Transição de serviços novos ou alterados (identificador a confirmar)", assoc="Correlata",
  rel=["d02_41", "d02_transc", "d03_risk_trans"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  resp="Delivery/Operação")
R("d01_lac_assin", "3. CRONOGRAMA DO PROCESSO — 3.1 e 3.2", "p. 2 (impressa: 1)",
  'Não localizado. Trecho que gera a necessidade: "deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato"',
  "Lacuna", "Transição/Implantação / Gestão de Projetos",
  "O cronograma não traz data de adjudicação nem de assinatura. Como a transição conta da assinatura e o início previsto é 01/02/2027, a janela real não é calculável; para 30 dias de transição terminando em 31/01/2027, a assinatura teria de ocorrer até 01/01/2027. Associação de boa prática: planejamento de cronograma do projeto.",
  S=4, P=3, imp="Impede planejar a mobilização e avaliar a exequibilidade do prazo de transição",
  fw="PMBOK Guide (7ª edição)", ctrl="Domínio de desempenho de Planejamento (identificador a confirmar)", assoc="Boa prática",
  rel=["d01_trans30", "d03_risk_trans"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Qual a data prevista de adjudicação e de assinatura do contrato? Se a assinatura ocorrer após 01/01/2027, o prazo de transição e a data de início de 01/02/2027 serão ajustados?",
  resp="Bid Manager")
R("d01_idioma", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.1", "p. 3 (impressa: 2)",
  '"A proposta deverá ser redigida em língua portuguesa"',
  "Instrução de resposta", "Administrativo do processo",
  "Idioma obrigatório. Documentos de fabricantes em inglês (datasheets, certificados) podem exigir tradução. Probabilidade 2: instrução clara, impacto só por descuido.",
  obr="Mandatório", S=2, P=2, imp="Custo e prazo de tradução de anexos técnicos", acao="Atender", resp="Bid Manager")
R("d01_portal", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.1", "p. 3 (impressa: 2)",
  '"enviada exclusivamente pelo portal de fornecedores do Banco"',
  "Instrução de resposta", "Administrativo do processo",
  "Canal único de entrega. A RFP não informa endereço do portal, exigência e prazo de cadastro, limites de tamanho e formato de arquivo nem forma de assinatura. Probabilidade 2: canal definido; impacto só em caso de falha de cadastro ou de envio.",
  obr="Mandatório", S=4, P=2, imp="Falha de cadastro ou de upload impede a entrega", acao="Esclarecer no Q&A",
  perg="Qual o endereço do portal de fornecedores? Há cadastro prévio exigido e com que antecedência? Quais os limites de tamanho e formato de arquivos e a forma de assinatura dos documentos?",
  resp="Bid Manager")
R("d01_40pag", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.2", "p. 3 (impressa: 2)",
  '"A proposta técnica deverá ter no máximo 40 (quarenta) páginas, excluídos os anexos."',
  "Instrução de resposta", "Administrativo do processo",
  "Consequência do excesso não definida (desclassificação, desconsideração das páginas excedentes ou perda de pontos), nem o que conta como anexo. Os critérios técnicos de 6.2 precisam ser atendidos dentro desse limite.",
  obr="Mandatório", S=3, P=3, imp="Risco de conteúdo desconsiderado e perda de pontuação técnica", acao="Esclarecer no Q&A",
  perg="Qual a consequência de exceder 40 páginas? Currículos, certificados, atestados e o questionário técnico contam como anexos excluídos do limite?",
  resp="Bid Manager")
R("d01_anexo4", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.3", "p. 3 (impressa: 2)",
  'Não localizado. Trecho que gera a necessidade: "A proposta comercial deverá ser apresentada conforme a planilha modelo do Anexo IV — Planilha de Preços."',
  "Lacuna", "Comercial/Preço",
  "Anexo IV citado e não fornecido no pacote. Sem ele não se conhece a estrutura de preço exigida (itens, unidades, preço fixo × variável por usuário ou EPS, separação SOC × IAM × transição), o que afeta a precificação e a Nota de Preço ({d01_lac_preco}). Associação de boa prática: conformidade da proposta comercial ao modelo do cliente.",
  obr="Mandatório", S=4, P=3, imp="Impede montar a proposta comercial no formato exigido; risco de proposta desconforme",
  fw="APMP Body of Knowledge", ctrl="Conformidade da proposta ao modelo exigido (identificador a confirmar)", assoc="Boa prática",
  rel=["d01_lac_preco", "d01_anexo2"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Favor disponibilizar o Anexo IV — Planilha de Preços. A planilha prevê preço fixo mensal ou componentes variáveis (por usuário, por EPS, por volume de armazenamento)?",
  resp="Pricing/Financeiro")
R("d01_anexo2", "Estrutura de anexos (2.2, 4.3 e Anexo III)", "p. 2 (impressa: 1) · p. 3 (impressa: 2) · p. 6 (impressa: 5) (OCR)",
  'Não localizado. Trechos: "constam do Anexo I — Especificação Técnica" · "ANEXO III — DECLARAÇÃO DE LOCALIZAÇÃO DE DADOS" · "planilha modelo do Anexo IV — Planilha de Preços"',
  "Lacuna", "Administrativo do processo / Jurídico/Contratual",
  "Inferência: a RFP cita os Anexos I, III e IV, mas nenhum trecho cita ou fornece o Anexo II, e o pacote não traz minuta de contrato (rescisão, garantias, limitação de responsabilidade, foro). A falha na sequência sugere anexo não divulgado; não há prova de que exista.",
  nat="Inferida", S=3, P=3, imp="Condições contratuais e documentos de resposta podem ser desconhecidos na precificação",
  rel=["d01_anexo4"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Existe um Anexo II desta RFP? Em caso afirmativo, favor disponibilizá-lo. Há minuta de contrato a ser assinada pelo vencedor? Favor disponibilizá-la.",
  resp="Bid Manager")
R("d01_qt", "4. INSTRUÇÕES PARA APRESENTAÇÃO DA PROPOSTA — 4.4", "p. 3 (impressa: 2)",
  '"O questionário técnico (planilha anexa) deverá ser integralmente preenchido."',
  "Instrução de resposta", "Administrativo do processo",
  "A RFP não prevê sanção; a planilha (D04, aba Instruções) acrescenta desclassificação para questionário incompleto ({d04_instr}).",
  obr="Mandatório", S=3, P=3, imp="Preenchimento incompleto expõe à desclassificação prevista no D04", rel=["d04_instr"],
  acao="Atender", resp="Pré-venda/Arquitetura")
R("d01_iso", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 a)", "p. 3 (impressa: 2)",
  '"Serão inabilitados os proponentes que não apresentarem: a) certificado ISO/IEC 27001 vigente, emitido por organismo acreditado, cujo escopo inclua os serviços de SOC"',
  "Critério eliminatório / de habilitação", "Segurança da Informação/Cyber / Administrativo do processo",
  "Certificado vigente com escopo que inclua SOC; IAM não é exigido no escopo. Organismo acreditado não especifica o acreditador. Repetido no QT-01 ({d04_qt01}). Probabilidade 5: a inabilitação decorre diretamente do texto para quem não apresentar o certificado.",
  obr="Mandatório", S=5, P=5, imp="Inabilitação",
  fw="ISO/IEC 27001:2022", ctrl="Certificação do SGSI (cláusulas 4 a 10)", assoc="Direta", rel=["d04_qt01"],
  acao="Atender",
  perg="Serão aceitos certificados emitidos por organismos acreditados por membros do IAF, além da Cgcre/Inmetro? O escopo deve mencionar expressamente SOC ou basta abranger serviços gerenciados de segurança?",
  resp="Compliance")
R("d01_atest", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 b)", "p. 3 (impressa: 2)",
  '"b) no mínimo 3 (três) atestados de capacidade técnica de prestação de serviços de SOC para instituições financeiras, com ambiente de no mínimo 2.000 usuários"',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Três atestados de SOC em instituições financeiras; nada é exigido para IAM. Ambiguidades em {d01_atest_amb}. Probabilidade 5: a inabilitação decorre diretamente do texto.",
  obr="Mandatório", S=5, P=5, imp="Inabilitação", rel=["d01_atest_amb"], acao="Atender", resp="Bid Manager")
R("d01_atest_amb", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 b)", "p. 3 (impressa: 2)",
  '"para instituições financeiras, com ambiente de no mínimo 2.000 usuários"',
  "Ambiguidade", "Administrativo do processo",
  "Não está claro: (i) se seguradoras, cooperativas de crédito e instituições de pagamento contam como instituições financeiras; (ii) se os 2.000 usuários valem por atestado ou somados; (iii) se usuários significa colaboradores, identidades ou ativos monitorados; (iv) se os atestados devem ser de clientes distintos e se contratos em execução valem. A diferença entre leituras pode inabilitar o proponente.",
  obr="Mandatório", S=5, P=3, imp="Atestados válidos numa leitura podem ser recusados em outra: risco de inabilitação",
  rel=["d01_atest"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="(i) Seguradoras, cooperativas de crédito, instituições de pagamento e demais entidades autorizadas pelo Banco Central contam como instituições financeiras? (ii) O mínimo de 2.000 usuários se aplica a cada atestado? (iii) Usuários refere-se a colaboradores do cliente atestante ou a identidades monitoradas? (iv) Os três atestados devem ser de clientes distintos e contratos em execução são aceitos?",
  resp="Bid Manager")
R("d01_soc_br", "5. CRITÉRIOS DE HABILITAÇÃO — 5.1 c)", "p. 3 (impressa: 2)",
  '"c) comprovação de que o SOC está localizado em território nacional"',
  "Critério eliminatório / de habilitação", "Operação/Serviços / Regulatório/Compliance",
  "Confirmado pelo Q&A nº 2 ({d04_q2}). A RFP não diz qual documento comprova a localização. Trata do centro de operação; a localização dos dados e logs está no Anexo III ({d01_dados_br}). Probabilidade 5: a inabilitação decorre diretamente do texto.",
  obr="Mandatório", S=5, P=5, imp="Inabilitação; impede operação a partir de SOC no exterior (inclusive modelo follow-the-sun)",
  fw="Resolução CMN nº 4.893/2021", ctrl="Contratação de serviços com processamento no exterior (identificador a confirmar)", assoc="Correlata",
  rel=["d04_q2", "d01_dados_br"], acao="Atender",
  perg="Que documento será aceito como comprovação da localização do SOC (declaração, contrato de locação, visita técnica)?",
  resp="Compliance")
R("d01_equipe_cert", "5. CRITÉRIOS DE HABILITAÇÃO — 5.2", "p. 3 (impressa: 2)",
  '"O proponente deverá possuir equipe técnica devidamente certificada."',
  "Ambiguidade", "Pessoas/Equipe",
  "Não define quais certificações, para quais perfis, em que quantidade, nem a forma de comprovação; também não diz se é condição de habilitação (está na seção 5, mas fora da lista de inabilitação do 5.1). Relaciona-se ao CISSP do coordenador ({d02_51}), ao QT-06 ({d04_qt06}) e ao critério Qualificação da equipe ({d01_c_equipe}).",
  obr="Mandatório", S=5, P=3, imp="Se lido como habilitação, comprovação julgada insuficiente leva à inabilitação; afeta também o custo da equipe",
  fw="ISO/IEC 27001:2022", ctrl="A.6.3 Conscientização, educação e treinamento em segurança da informação", assoc="Correlata",
  rel=["d02_51", "d04_qt06", "d01_c_equipe"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Quais certificações e em que quantidade são exigidas por perfil (N1, N2, N3, coordenação, IAM)? A exigência do item 5.2 é condição de habilitação ou apenas de pontuação? Em que momento e por qual documento deve ser comprovada?",
  resp="RH/Staffing")
R("d01_nota", "6. CRITÉRIOS DE AVALIAÇÃO — 6.1", "p. 4 (impressa: 3)",
  '"A nota final será composta pela Nota Técnica (peso de 60%) e pela Nota de Preço (peso de 40%)."',
  "Critério de avaliação / pontuação", "Comercial/Preço / Administrativo do processo",
  "Técnica e preço com pesos 60/40. A fórmula da Nota de Preço não é informada ({d01_lac_preco}).",
  obr="Informativo", S=3, P=3, imp="Peso técnico relevante; sem a fórmula de preço não se simula a nota final",
  rel=["d01_lac_preco"], acao="Atender", resp="Bid Manager")
R("d01_lac_preco", "6. CRITÉRIOS DE AVALIAÇÃO — 6.1", "p. 4 (impressa: 3)",
  'Não localizado. Trecho que gera a necessidade: "pela Nota de Preço (peso de 40%)"',
  "Lacuna", "Comercial/Preço",
  "A RFP não define como a Nota de Preço é calculada (proporção ao menor preço, faixas, preço de referência), nem se há preço máximo aceitável ou critério de inexequibilidade.",
  S=4, P=3, imp="Impede simular a nota final e calibrar a estratégia de preço",
  rel=["d01_nota", "d01_anexo4"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Qual a fórmula de cálculo da Nota de Preço? Há preço máximo aceitável ou critério de preço inexequível?",
  resp="Pricing/Financeiro")
R("d01_c_metod", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", "p. 4 (impressa: 3)",
  '"Metodologia de operação do SOC 20"',
  "Critério de avaliação / pontuação", "Operação/Serviços",
  "Maior peso, empatado com equipe. Sem subcritérios publicados ({d01_lac_subcrit}).",
  obr="Informativo", S=3, P=3, imp="Perda moderada de pontuação técnica",
  fw="NIST CSF 2.0", ctrl="Funções DE (Detectar) e RS (Responder)", assoc="Correlata", rel=["d01_lac_subcrit"],
  acao="Atender", resp="Pré-venda/Arquitetura")
R("d01_c_equipe", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", "p. 4 (impressa: 3)",
  '"Qualificação da equipe 20"',
  "Critério de avaliação / pontuação", "Pessoas/Equipe",
  "Sem subcritérios; ligado à exigência vaga de equipe certificada ({d01_equipe_cert}).",
  obr="Informativo", S=3, P=3, imp="Perda moderada de pontuação técnica", rel=["d01_equipe_cert", "d01_lac_subcrit"],
  acao="Atender", resp="RH/Staffing")
R("d01_c_ferr", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", "p. 4 (impressa: 3)",
  '"Ferramentas e tecnologia 15"',
  "Critério de avaliação / pontuação", "Técnico/Arquitetura",
  "Sem subcritérios. Itens não exigidos no Anexo I (PAM desejável, SOAR, threat intelligence) podem pesar aqui ({d03_pam}).",
  obr="Informativo", S=3, P=3, imp="Perda moderada de pontuação técnica", rel=["d01_lac_subcrit", "d03_pam"],
  acao="Atender", resp="Pré-venda/Arquitetura")
R("d01_c_trans", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", "p. 4 (impressa: 3)",
  '"Plano de transição 10"',
  "Critério de avaliação / pontuação", "Transição/Implantação",
  "Sem subcritérios; o plano terá de se basear num prazo indefinido (30 × 60 dias, {d02_transc}).",
  obr="Informativo", S=3, P=3, imp="Perda moderada de pontuação técnica", rel=["d02_transc", "d01_lac_subcrit"],
  acao="Atender", resp="Delivery/Operação")
R("d01_lac_subcrit", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", "p. 4 (impressa: 3)",
  'Não localizado. Trecho que gera a necessidade: "será atribuída conforme os critérios abaixo"',
  "Lacuna", "Administrativo do processo",
  "Não há subcritérios, evidências esperadas nem escala de notas para cada critério, o que torna a avaliação subjetiva e dificulta mirar o mínimo de 70% (6.3).",
  S=3, P=3, imp="Dificulta direcionar o conteúdo da proposta técnica às notas", rel=["d01_desclass"],
  status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Quais subcritérios, evidências esperadas e escala de notas serão usados em cada critério do item 6.2?",
  resp="Bid Manager")
R("d01_contr_60_65", "6. CRITÉRIOS DE AVALIAÇÃO — 6.2", "p. 4 (impressa: 3) — texto do 6.2 · p. 4 (impressa: 3) — tabela do 6.2",
  'A: "A Nota Técnica, de no máximo 60 (sessenta) pontos" · B: "Metodologia de operação do SOC 20 [...] Qualificação da equipe 20 [...] Ferramentas e tecnologia 15 [...] Plano de transição 10" (soma = 65)',
  "Contradição", "Administrativo do processo",
  "O teto de 60 pontos é incompatível com a soma dos critérios (65). Leituras possíveis: normalização para 60, corte em 60 ou erro em algum peso. Afeta o mínimo de 70% do 6.3 (42 pontos sobre 60 ou 45,5 sobre 65) e a conversão para o peso de 60% da nota final. A aba oculta Pesos acrescenta deduções não previstas ({d04_contr_pesos}).",
  S=4, P=3, imp="Incerteza sobre o mínimo técnico e sobre onde concentrar esforço na proposta técnica",
  rel=["d01_desclass", "d04_contr_pesos"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A soma dos critérios do item 6.2 é 65 pontos, mas a Nota Técnica máxima é 60. Qual o valor correto de cada critério e como será calculado o mínimo de 70% do item 6.3?",
  resp="Bid Manager")
R("d01_desclass", "6. CRITÉRIOS DE AVALIAÇÃO — 6.3", "p. 4 (impressa: 3)",
  '"Serão desclassificadas as propostas com Nota Técnica inferior a 70% (setenta por cento) da pontuação máxima."',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Corte técnico com base de cálculo incerta (60 × 65, {d01_contr_60_65}) e sujeito às deduções ocultas da aba Pesos ({d04_pesos_a9}). Probabilidade mantida em 3: o atingimento depende de avaliação sem subcritérios publicados; o texto não indica se a proposta ficará abaixo do corte.",
  obr="Mandatório", S=5, P=3, imp="Desclassificação",
  rel=["d01_contr_60_65", "d04_pesos_a9", "d01_lac_subcrit"], acao="Mitigar", resp="Bid Manager")
R("d01_empate", "6. CRITÉRIOS DE AVALIAÇÃO — 6.4", "p. 4 (impressa: 3)",
  '"Em caso de empate na nota final, prevalecerá a proposta de menor preço."',
  "Critério de avaliação / pontuação", "Comercial/Preço",
  "Desempate por preço. Probabilidade 2: empate exato na nota final é pouco provável com notas fracionárias.",
  S=2, P=2, imp="Reforça o peso do preço apenas em caso de empate", resp="Pricing/Financeiro")
R("d01_vig", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.1", "p. 5 (impressa: 4)",
  '"O contrato terá vigência de 36 (trinta e seis) meses, prorrogável por iguais períodos mediante acordo entre as partes."',
  "Obrigação contratual", "Jurídico/Contratual / Comercial/Preço",
  "Prazo para amortizar implantação do SIEM e do IAM e licenças. Prorrogação depende de acordo, sem garantia de renovação. Inferior aos 5 anos de guarda de logs ({d02_16}).",
  S=2, P=3, imp="Define o período de amortização dos investimentos iniciais", rel=["d02_16", "d02_lac_saida"],
  acao="Precificar", resp="Pricing/Financeiro")
R("d01_reaj", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.2", "p. 5 (impressa: 4)",
  '"Os preços serão reajustados anualmente pela variação do IPCA."',
  "Obrigação contratual", "Comercial/Preço",
  "Data-base do reajuste (proposta ou assinatura) não informada; custos atrelados a câmbio (licenças, nuvem) não acompanham o IPCA.",
  S=2, P=3, imp="Descasamento entre custos em moeda estrangeira e o índice de reajuste", acao="Esclarecer no Q&A",
  perg="Qual a data-base do reajuste anual pelo IPCA: data de entrega da proposta ou data de assinatura do contrato?",
  resp="Pricing/Financeiro")
R("d01_pgto", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.3", "p. 5 (impressa: 4)",
  '"O pagamento será efetuado em até 60 (sessenta) dias após o aceite da nota fiscal."',
  "Obrigação contratual", "Financeiro",
  "Prazo longo e contado do aceite, cujo prazo não é definido. Probabilidade 4: o próprio texto fixa até 60 dias após um aceite sem prazo, o que implica financiar mais de dois meses de operação.",
  obr="Mandatório", S=3, P=4, imp="Custo financeiro de capital de giro a incluir no preço", acao="Precificar",
  perg="Qual o prazo para o aceite da nota fiscal após sua emissão? Há atualização monetária ou juros em caso de atraso no pagamento?",
  resp="Pricing/Financeiro")
R("d01_multa", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.4", "p. 5 (impressa: 4)",
  '"O descumprimento de qualquer nível de serviço (SLA) previsto no Anexo I sujeitará a Contratada a multa de 10% (dez por cento) do valor mensal do contrato, por ocorrência."',
  "Penalidade / multa / glosa", "Jurídico/Contratual / Financeiro",
  "Multa por ocorrência, sem teto, sem gradação por gravidade e sem período de estabilização: 10 ocorrências num mês consomem 100% do faturamento mensal. Alcança qualquer SLA do Anexo I, inclusive atraso do relatório mensal ({d02_23}); alcance exato em {d02_sla_scope}. Probabilidade 4: a multa incide automaticamente a cada ocorrência e o Banco manteve o item 7 inalterado quando perguntado sobre limite (Q&A nº 4, {d04_q4}).",
  obr="Mandatório", S=5, P=4, imp="Exposição financeira ilimitada, que pode superar a receita mensal",
  fw="Código Civil (Lei 10.406/2002)", ctrl="Art. 412 (valor da cláusula penal limitado ao da obrigação principal)", assoc="Correlata",
  rel=["d04_q4", "d04_q4", "d02_sla_scope", "d02_21", "d02_22", "d02_23"], acao="Propor exceção/ressalva",
  perg="Considerando o Q&A nº 4, o Banco aceitaria limite agregado de multas (por exemplo, percentual do valor mensal), gradação por criticidade do SLA e período inicial de estabilização sem multas?",
  resp="Jurídico")
R("d01_resp_ilim", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.5", "p. 5 (impressa: 4)",
  '"A Contratada responderá de forma integral e ilimitada por quaisquer danos decorrentes de incidentes de segurança ocorridos no ambiente do Contratante."',
  "Obrigação contratual", "Jurídico/Contratual",
  "Responsabilidade por quaisquer danos de incidentes ocorridos no ambiente do Banco, sem exigir culpa ou nexo com a atuação da Contratada e sem exclusão de danos indiretos ou lucros cessantes. Mantida pelo Q&A nº 4 ({d04_q4}). Probabilidade 3: os documentos não indicam frequência de incidentes com dano.",
  obr="Mandatório", S=5, P=3, imp="Exposição jurídica e financeira ilimitada; pode tornar o risco não segurável e não precificável",
  fw="Código Civil (Lei 10.406/2002)", ctrl="Art. 944 (indenização medida pela extensão do dano)", assoc="Correlata",
  rel=["d04_q4", "d04_q4", "d01_seguro", "d02_15a"], acao="Propor exceção/ressalva",
  perg="O Banco aceita limitar a responsabilidade da Contratada a danos diretos causados por sua culpa comprovada, com teto (por exemplo, valor anual do contrato) e exclusão de lucros cessantes e danos indiretos?",
  resp="Jurídico")
R("d01_seguro", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.6", "p. 5 (impressa: 4)",
  '"A Contratada deverá manter seguro de responsabilidade civil cibernética em valor compatível com os riscos do contrato."',
  "Ambiguidade", "Jurídico/Contratual / Financeiro",
  "Valor segurado indefinido; com responsabilidade ilimitada (7.5) nenhum valor é objetivamente compatível. Não informa coberturas mínimas nem quando a apólice deve ser apresentada.",
  obr="Mandatório", S=4, P=3, imp="Custo do seguro não estimável; risco de o valor contratado ser contestado",
  fw="ISO 31000", ctrl="Tratamento de riscos — compartilhamento por seguro (identificador a confirmar)", assoc="Correlata",
  rel=["d01_resp_ilim", "d04_q4"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Qual o valor mínimo de cobertura e quais coberturas mínimas são exigidas na apólice de responsabilidade civil cibernética? Ela deve ser apresentada com a proposta ou na assinatura do contrato?",
  resp="Jurídico")
R("d01_subcont", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.7", "p. 5 (impressa: 4)",
  '"É vedada a subcontratação, total ou parcial, do objeto deste contrato."',
  "Restrição", "Jurídico/Contratual",
  "Vedação total, sem exceção para fornecedores de tecnologia. Pode conflitar com SIEM em nuvem pública de terceiro, feeds de threat intelligence e integração com SOAR ({d02_subcont_amb}).",
  obr="Mandatório", S=4, P=3, imp="Pode impedir modelos de entrega com parceiros e provedores de nuvem; risco de descumprimento contratual",
  fw="ISO/IEC 27001:2022", ctrl="A.5.19 Segurança da informação nas relações com fornecedores", assoc="Correlata",
  rel=["d02_subcont_amb"], status="Em esclarecimento", acao="Esclarecer no Q&A", resp="Jurídico")
R("d01_conf", "7. CONDIÇÕES COMERCIAIS E CONTRATUAIS — 7.8", "p. 5 (impressa: 4)",
  '"As obrigações de confidencialidade vigorarão por 5 (cinco) anos após o término do contrato."',
  "Obrigação contratual", "Jurídico/Contratual",
  "Sobrevivência de 5 anos após o término.",
  obr="Mandatório", S=2, P=3, imp="Obrigação pós-contratual de controle de informação",
  fw="ISO/IEC 27001:2022", ctrl="A.6.6 Acordos de confidencialidade ou de não divulgação", assoc="Direta",
  acao="Atender", resp="Jurídico")
R("d01_anexo3", "Anexo III — Declaração de Localização de Dados", "p. 6 (impressa: 5) (OCR)",
  '"Esta declaração deverá ser entregue assinada pelo representante legal do proponente junto com a proposta, sob pena de inabilitação."',
  "Critério eliminatório / de habilitação", "Administrativo do processo / Regulatório/Compliance",
  "Página digitalizada sem camada de texto, lida visualmente. Declaração obrigatória de habilitação que não consta da lista do item 5.1. Probabilidade 5: a ausência da declaração leva à inabilitação por texto expresso.",
  obr="Mandatório", S=5, P=5, imp="Inabilitação; a declaração vincula a arquitetura a dados no Brasil",
  rel=["d01_dados_br", "d02_contr_regiao"], acao="Atender", resp="Jurídico")
R("d01_dados_br", "Anexo III — Declaração de Localização de Dados", "p. 6 (impressa: 5) (OCR)",
  '"todos os dados do Banco Horizonte Fictício S.A., incluindo os registros (logs) de segurança, serão armazenados e processados exclusivamente em território nacional, durante toda a vigência do contrato"',
  "Restrição", "Infraestrutura/Cloud / Regulatório/Compliance",
  "Restringe a arquitetura do SIEM, backups, réplicas de recuperação de desastres e ferramentas SaaS de apoio (threat intelligence, SOAR, chamados). Contradiz a liberdade de região do Anexo I 1.2 ({d02_contr_regiao}). Cobre só a vigência e só dados do Banco, embora o Anexo I exija guarda de logs por 5 anos ({d02_16}) e as notas do workshop incluam subsidiárias ({d03_subsid}).",
  obr="Mandatório", S=4, P=3, imp="Limita provedores e regiões de nuvem e ferramentas; descumprimento após declaração assinada gera inadimplemento",
  fw="LGPD (Lei 13.709/2018)", ctrl="Art. 33 (transferência internacional de dados)", assoc="Correlata",
  rel=["d02_contr_regiao", "d02_12", "d02_16", "d03_subsid"], acao="Atender", resp="Pré-venda/Arquitetura")

# =============================================================================== D02
doc("D02")
R("d02_inv", "Inventário do documento", "§ documento inteiro (cabeçalho e seções 1 a 6)",
  '"RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Versão 1.0 — 15/10/2026"',
  "Registro de cobertura", "Administrativo do processo",
  "22 parágrafos, sem tabelas, sem marcas de revisão nem comentários; lido integralmente. Word sem paginação fixa: localizador por seção e item.",
  imp="Cobertura integral; nenhuma pendência de leitura")
R("d02_11", "1. SERVIÇOS DE SOC — 1.1", "§ 1. SERVIÇOS DE SOC — item 1.1",
  '"O proponente deverá prestar serviço de monitoramento contínuo de eventos de segurança, em regime 24x7x365."',
  "Requisito funcional / de serviço", "Operação/Serviços / Segurança da Informação/Cyber",
  "Coerente com a RFP 2.1 ({d01_soc}). Fontes de eventos não definidas ({d02_14}).",
  obr="Mandatório", S=3, P=3, imp="Base do dimensionamento de turnos",
  fw="ISO/IEC 27001:2022", ctrl="A.8.16 Atividades de monitoramento", assoc="Direta", rel=["d01_soc", "d02_14"],
  acao="Precificar", resp="Delivery/Operação")
R("d02_12", "1. SERVIÇOS DE SOC — 1.2", "§ 1. SERVIÇOS DE SOC — item 1.2",
  '"O proponente deverá fornecer a solução de SIEM"',
  "Requisito funcional / de serviço", "Técnico/Arquitetura / Infraestrutura/Cloud",
  "O proponente fornece a plataforma (licenças, infraestrutura, armazenamento). O custo depende de EPS e retenção, não informados ({d04_q3}). Não define propriedade das licenças e dos dados ao término ({d02_lac_saida}).",
  obr="Mandatório", S=4, P=3, imp="Principal custo de tecnologia, sem base de volumetria",
  fw="ISO/IEC 27001:2022", ctrl="A.8.15 Registro de logs", assoc="Correlata", rel=["d04_q3", "d02_lac_saida", "d02_contr_regiao"],
  acao="Precificar", resp="Pré-venda/Arquitetura")
R("d02_contr_regiao", "1. SERVIÇOS DE SOC — 1.2 × Anexo III", "§ 1. SERVIÇOS DE SOC — item 1.2 (D02) · p. 6 (impressa: 5) (OCR) (D01)",
  'A: "podendo esta ser disponibilizada em nuvem pública, em região de livre escolha do proponente" · B: "serão armazenados e processados exclusivamente em território nacional"',
  "Contradição", "Infraestrutura/Cloud / Regulatório/Compliance",
  "O Anexo I permite região de nuvem de livre escolha; o Anexo III exige, sob pena de inabilitação, declaração de que dados e logs ficam exclusivamente no Brasil. Quem adotar região no exterior com base no Anexo I fica impedido de firmar a declaração. A Resolução CMN nº 4.893/2021, a que o Banco se declara sujeito ({d01_4893}), também condiciona a contratação de processamento, armazenamento e nuvem. O Q&A nº 2 trata só do local do SOC, não dos dados ({d04_q2}).",
  obr="Mandatório", S=5, P=3, imp="Arquitetura e preço errados levam à inabilitação ou a refazer a solução",
  fw="Resolução CMN nº 4.893/2021", ctrl="Contratação de processamento, armazenamento de dados e computação em nuvem (identificador a confirmar)", assoc="Direta",
  rel=["d01_dados_br", "d01_anexo3", "d04_q2", "d01_4893"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O Anexo I, item 1.2, permite nuvem pública em região de livre escolha, mas o Anexo III exige dados e logs exclusivamente em território nacional. Confirmam que o SIEM em nuvem deve usar apenas regiões no Brasil, inclusive para backup, réplica de recuperação de desastres e ferramentas SaaS de apoio?",
  resp="Pré-venda/Arquitetura")
R("d02_subcont_amb", "1. SERVIÇOS DE SOC — 1.2 × RFP 7.7", "§ 1. SERVIÇOS DE SOC — item 1.2 (D02) · p. 5 (impressa: 4) — 7.7 (D01)",
  '"podendo esta ser disponibilizada em nuvem pública" · "É vedada a subcontratação, total ou parcial, do objeto deste contrato."',
  "Ambiguidade", "Jurídico/Contratual / Infraestrutura/Cloud",
  "Não está claro se usar provedor de nuvem pública, SIEM em modelo SaaS de fabricante, feeds de threat intelligence (QT-05) ou SOAR (QT-02) de terceiros configura a subcontratação vedada.",
  obr="Mandatório", S=4, P=3, imp="Leitura restritiva pode inviabilizar a arquitetura em nuvem e serviços de terceiros",
  rel=["d01_subcont", "d04_qt02", "d04_qt05"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A contratação, pelo proponente, de provedor de nuvem pública, de SIEM em modelo SaaS, de licenças de software e de feeds de threat intelligence configura subcontratação vedada pelo item 7.7 da RFP?",
  resp="Jurídico")
R("d02_13", "1. SERVIÇOS DE SOC — 1.3", "§ 1. SERVIÇOS DE SOC — item 1.3",
  '"Os registros (logs) de segurança deverão ser retidos por no mínimo 12 (doze) meses."',
  "Requisito não funcional", "Técnico/Arquitetura",
  "Retenção mínima; em conflito com o item 1.6 ({d02_contr_logs}). O QT-03 fala em 12 meses online ({d04_qt03}).",
  obr="Mandatório", S=3, P=3, imp="Custo de armazenamento proporcional ao EPS",
  fw="ISO/IEC 27001:2022", ctrl="A.8.15 Registro de logs", assoc="Direta", rel=["d02_contr_logs", "d04_qt03"],
  status="Em esclarecimento", acao="Precificar", resp="Pré-venda/Arquitetura")
R("d02_14", "1. SERVIÇOS DE SOC — 1.4", "§ 1. SERVIÇOS DE SOC — item 1.4",
  '"O SIEM deverá ser integrado a todos os ativos relevantes do Contratante."',
  "Ambiguidade", "Técnico/Arquitetura",
  "Ativos relevantes não é definido e não há inventário de fontes de log (só 850 servidores, 2 data centers e 2 nuvens na apresentação, {d03_servers}); o Banco recusou informar o EPS ({d04_q3}). Esforço de integração (conectores, parsers customizados) e licenciamento ficam indeterminados.",
  obr="Mandatório", S=4, P=3, imp="Escopo de integração aberto, sem remuneração por fontes adicionais",
  fw="ISO/IEC 27001:2022", ctrl="A.5.9 Inventário de informações e outros ativos associados", assoc="Correlata",
  rel=["d04_q3", "d03_servers", "d03_cloud"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Quais são os ativos relevantes a integrar ao SIEM (tipos e quantidades: servidores, estações, firewalls, ativos de rede, aplicações, contas de nuvem)? Integrações de aplicações legadas sem conector padrão estão no escopo?",
  resp="Pré-venda/Arquitetura")
R("d02_15a", "1. SERVIÇOS DE SOC — 1.5", "§ 1. SERVIÇOS DE SOC — item 1.5",
  '"O serviço deverá contemplar resposta a incidentes, incluindo contenção, erradicação"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Contenção e erradicação pressupõem atuação no ambiente do Banco; não define se é remota ou presencial, os níveis de autorização (isolar host, bloquear conta) nem se inclui recuperação. Combinada com a responsabilidade ilimitada ({d01_resp_ilim}), a atuação direta amplia a exposição.",
  obr="Mandatório", S=3, P=3, imp="Esforço de resposta e exposição por ações no ambiente do cliente",
  fw="ISO/IEC 27001:2022", ctrl="A.5.26 Resposta a incidentes de segurança da informação", assoc="Direta",
  rel=["d01_resp_ilim"], acao="Esclarecer no Q&A",
  perg="As ações de contenção e erradicação serão executadas diretamente pela Contratada ou pelas equipes do Banco sob orientação? Há atendimento presencial a incidentes? A recuperação está no escopo?",
  resp="Segurança/Cyber")
R("d02_15b", "1. SERVIÇOS DE SOC — 1.5", "§ 1. SERVIÇOS DE SOC — item 1.5",
  '"e elaboração de relatório pós-incidente"',
  "Entregável", "Segurança da Informação/Cyber",
  "Prazo, formato e destinatários do relatório não definidos.",
  obr="Mandatório", S=2, P=3, imp="Esforço de análise e documentação por incidente",
  fw="ISO/IEC 27001:2022", ctrl="A.5.27 Aprendizado com incidentes de segurança da informação", assoc="Direta",
  acao="Atender", resp="Segurança/Cyber")
R("d02_16", "1. SERVIÇOS DE SOC — 1.6", "§ 1. SERVIÇOS DE SOC — item 1.6",
  '"Para fins de auditoria, os logs deverão ser mantidos por 5 (cinco) anos."',
  "Requisito não funcional", "Técnico/Arquitetura / Regulatório/Compliance",
  "Guarda de 5 anos excede a vigência de 36 meses (RFP 7.1): não se sabe quem guarda os logs após o término ({d02_lac_saida}).",
  obr="Mandatório", S=4, P=3, imp="Custo de armazenamento de longo prazo e obrigação que ultrapassa o contrato",
  fw="ISO/IEC 27001:2022", ctrl="A.5.33 Proteção de registros", assoc="Direta",
  rel=["d02_contr_logs", "d02_lac_saida", "d01_vig"], status="Em esclarecimento", acao="Precificar",
  resp="Pré-venda/Arquitetura")
R("d02_contr_logs", "1. SERVIÇOS DE SOC — 1.3 × 1.6", "§ 1. SERVIÇOS DE SOC — item 1.3 · § 1. SERVIÇOS DE SOC — item 1.6",
  'A: "Os registros (logs) de segurança deverão ser retidos por no mínimo 12 (doze) meses." · B: "Para fins de auditoria, os logs deverão ser mantidos por 5 (cinco) anos."',
  "Contradição", "Técnico/Arquitetura",
  "Prazos incompatíveis na mesma seção. Leitura conciliadora possível (12 meses online pesquisáveis + 5 anos em arquivo), sugerida pelo QT-03, mas não declarada. A diferença de custo entre 12 e 60 meses de armazenamento é relevante e depende do EPS, não informado. A migração de 24 meses de logs históricos ({d03_migr}) agrava a conta.",
  obr="Mandatório", S=4, P=3, imp="Diferença relevante no custo de armazenamento do SIEM",
  rel=["d02_13", "d02_16", "d04_qt03", "d03_migr"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Os itens 1.3 (12 meses) e 1.6 (5 anos) do Anexo I devem ser lidos como 12 meses de retenção online pesquisável e 5 anos de arquivamento? Os 5 anos contam inclusive após o fim do contrato? O arquivamento pode ser feito em armazenamento do próprio Banco?",
  resp="Pré-venda/Arquitetura")
R("d02_lgpd", "1. SERVIÇOS DE SOC — 1.3 e 1.6 · 3. IAM — 3.1", "§ 1. SERVIÇOS DE SOC — itens 1.3 e 1.6 · § 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — item 3.1",
  '"Os registros (logs) de segurança deverão ser retidos" · "Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"',
  "Requisito implícito", "Privacidade/Proteção de Dados",
  "Inferência: logs de segurança (usuário, IP, acessos) e dados do ciclo de vida de colaboradores são dados pessoais; ao tratá-los por conta do Banco, o proponente atua como operador (LGPD art. 5º, VII), deve seguir as instruções do controlador (art. 39) e adotar medidas de segurança (art. 46). Nenhum documento trata de LGPD, acordo de tratamento, papéis ou prazos de comunicação de incidentes com dados pessoais.",
  obr="Mandatório", nat="Inferida", S=4, P=3, imp="Obrigações e responsabilidade (art. 42) não delimitadas; custos de conformidade não previstos",
  fw="LGPD (Lei 13.709/2018)", ctrl="Art. 5º, VII · Art. 39 · Art. 46", assoc="Direta",
  rel=["d01_resp_ilim", "d01_dados_br"], acao="Registrar premissa na proposta",
  perg="O Banco prevê acordo de tratamento de dados pessoais (papéis de controlador e operador, instruções, prazos de notificação de incidentes)? Favor disponibilizar a minuta.",
  resp="Compliance")
R("d02_lac_saida", "1. SERVIÇOS DE SOC — 1.2 e 1.6 × RFP 7.1", "§ 1. SERVIÇOS DE SOC — itens 1.2 e 1.6 (D02) · p. 5 (impressa: 4) — 7.1 (D01)",
  'Não localizado. Trechos: "O proponente deverá fornecer a solução de SIEM" · "os logs deverão ser mantidos por 5 (cinco) anos" · "O contrato terá vigência de 36 (trinta e seis) meses"',
  "Lacuna", "Jurídico/Contratual / Continuidade",
  "Não há regras de encerramento: devolução ou migração dos logs e do conteúdo do SIEM, propriedade das licenças, guarda dos logs pelos 2 anos restantes do período de 5 anos e apoio ao próximo fornecedor.",
  S=3, P=3, imp="Obrigações de saída não precificadas e possível guarda de logs sem remuneração",
  fw="ISO/IEC 27001:2022", ctrl="A.5.20 Tratamento da segurança da informação nos acordos com fornecedores", assoc="Correlata",
  rel=["d02_12", "d02_16", "d01_vig"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Ao término do contrato, a Contratada deverá exportar e entregar ao Banco os logs e o conteúdo do SIEM? Em que formato e prazo? A guarda dos logs após o término cabe a quem e será remunerada?",
  resp="Jurídico")
R("d02_21", "2. NÍVEIS DE SERVIÇO (SLA) — 2.1", "§ 2. NÍVEIS DE SERVIÇO (SLA) — item 2.1",
  '"Tempo máximo para início do tratamento de incidentes críticos: 15 (quinze) minutos."',
  "SLA / KPI", "Operação/Serviços",
  "Início do tratamento não é definido (reconhecimento, abertura de chamado ou primeira ação) e depende da classificação de criticidade pelo Banco ({d02_24}). Não há SLA para outras severidades nem para contenção ou resolução. Cada descumprimento sujeita a multa de 10% ({d01_multa}).",
  obr="Mandatório", S=4, P=3, imp="Exige analistas disponíveis 24x7 com resposta imediata; cada falha gera multa",
  fw="ITIL 4", ctrl="Prática Gerenciamento de incidentes", assoc="Direta", rel=["d02_24", "d01_multa"],
  status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O que caracteriza o início do tratamento no SLA de 15 minutos (reconhecimento, abertura de chamado, primeira ação de contenção)? A contagem começa na geração do alerta pelo SIEM ou na sua classificação como crítico?",
  resp="Delivery/Operação")
R("d02_22", "2. NÍVEIS DE SERVIÇO (SLA) — 2.2", "§ 2. NÍVEIS DE SERVIÇO (SLA) — item 2.2",
  '"Disponibilidade mínima mensal da plataforma SIEM: 99,9%."',
  "SLA / KPI", "Infraestrutura/Cloud",
  "99,9% mensal equivale a cerca de 43 minutos de indisponibilidade em 30 dias. Não define método de medição, exclusão de manutenções programadas nem tratamento de falhas do provedor de nuvem.",
  obr="Mandatório", S=3, P=3, imp="Exige arquitetura redundante; falhas geram multa",
  fw="ITIL 4", ctrl="Prática Gerenciamento de disponibilidade", assoc="Direta", rel=["d01_multa"],
  status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Janelas de manutenção programada são excluídas do cálculo de disponibilidade do SIEM? Qual a fonte e o método de medição?",
  resp="Pré-venda/Arquitetura")
R("d02_23", "2. NÍVEIS DE SERVIÇO (SLA) — 2.3", "§ 2. NÍVEIS DE SERVIÇO (SLA) — item 2.3",
  '"Relatório mensal de indicadores, a ser entregue até o 5º dia útil do mês subsequente."',
  "SLA / KPI", "Operação/Serviços",
  "Indicadores do relatório não definidos. Por estar na seção de SLA, atraso pode gerar multa de 10% do valor mensal ({d01_multa}).",
  obr="Mandatório", S=2, P=3, imp="Prazo curto para consolidação mensal com risco de multa desproporcional",
  fw="ITIL 4", ctrl="Prática Gerenciamento de nível de serviço", assoc="Direta", rel=["d01_multa"],
  acao="Atender", resp="Delivery/Operação")
R("d02_24", "2. NÍVEIS DE SERVIÇO (SLA) — 2.4", "§ 2. NÍVEIS DE SERVIÇO (SLA) — item 2.4",
  'Não localizado. Trecho que gera a necessidade: "A classificação de criticidade dos incidentes seguirá a matriz de classificação do Contratante."',
  "Lacuna", "Segurança da Informação/Cyber / Operação/Serviços",
  "Matriz citada e não fornecida. Sem ela não se sabe que parcela dos cerca de 1.200 alertas por dia ({d03_alertas}) vira incidente crítico sujeito ao SLA de 15 minutos, o que define o dimensionamento da equipe e a exposição a multas.",
  obr="Mandatório", S=4, P=3, imp="Impede dimensionar a equipe e estimar a exposição a multas do SLA 2.1",
  fw="ISO/IEC 27001:2022", ctrl="A.5.25 Avaliação e decisão sobre eventos de segurança da informação", assoc="Direta",
  rel=["d02_21", "d03_alertas"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Favor disponibilizar a matriz de classificação de criticidade de incidentes do Banco e o volume histórico mensal de incidentes por criticidade.",
  resp="Segurança/Cyber")
R("d02_iam_lac", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM)", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — itens 3.1 a 3.4",
  'Não localizado. Trecho que gera a necessidade: "Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"',
  "Lacuna", "Técnico/Arquitetura / Segurança da Informação/Cyber",
  "A seção 3 não diz se o proponente fornece a plataforma de IAM/IGA (como faz com o SIEM em 1.2) ou opera ferramentas do Banco; não lista sistemas-alvo, fonte autoritativa (RH) nem número de aplicações. O ambiente atual é Active Directory com scripts internos ({d03_iam_atual}). A seção 6 não atribui ao Banco a integração com o RH.",
  obr="Mandatório", S=4, P=3, imp="Escopo de IAM impossível de precificar com precisão (ferramenta, integrações, esforço)",
  rel=["d01_iam", "d03_iam_atual", "d03_pam"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O proponente deve fornecer a plataforma de IAM/IGA ou operar ferramentas do Banco? Quantos e quais sistemas-alvo devem ser integrados ao ciclo de vida, e qual sistema de RH será a fonte autoritativa?",
  resp="Pré-venda/Arquitetura")
R("d02_31a", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.1", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — item 3.1",
  '"Gestão do ciclo de vida das identidades (admissão, movimentação e desligamento)"',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Processos de admissão, movimentação e desligamento; volume depende da base de usuários, divergente entre documentos ({d04_contr_users}).",
  obr="Mandatório", S=3, P=3, imp="Esforço operacional proporcional ao número de identidades e de sistemas-alvo",
  fw="ISO/IEC 27001:2022", ctrl="A.5.16 Gestão de identidade", assoc="Direta", rel=["d02_iam_lac", "d04_contr_users"],
  acao="Precificar", resp="Delivery/Operação")
R("d02_31b", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.1", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — item 3.1",
  '"com revogação dos acessos de colaboradores desligados em até 24 (vinte e quatro) horas"',
  "SLA / KPI", "Segurança da Informação/Cyber",
  "Depende de o Banco comunicar o desligamento a tempo; o marco inicial da contagem não é definido. Pode ser tratado como SLA para a multa do 7.4 ({d02_sla_scope}).",
  obr="Mandatório", S=3, P=3, imp="Prazo dependente de terceiros, com possível multa",
  fw="ISO/IEC 27001:2022", ctrl="A.5.18 Direitos de acesso", assoc="Direta", rel=["d02_sla_scope"],
  acao="Esclarecer no Q&A",
  perg="A contagem das 24 horas para revogação começa no registro do desligamento no sistema de RH ou na comunicação formal à Contratada?",
  resp="Delivery/Operação")
R("d02_sla_scope", "RFP 7.4 × Anexo I seções 1, 3 e 4", "p. 5 (impressa: 4) — 7.4 (D01) · § 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — item 3.1 (D02)",
  '"qualquer nível de serviço (SLA) previsto no Anexo I" · "com revogação dos acessos de colaboradores desligados em até 24 (vinte e quatro) horas"',
  "Ambiguidade", "Jurídico/Contratual / Operação/Serviços",
  "O Anexo I agrupa SLAs na seção 2, mas contém outros prazos mensuráveis (revogação em 24 h, 3.1; recertificação trimestral, 3.3; transição, 4.1; retenção de logs, 1.3). Não está claro quais são níveis de serviço para a multa de 10% por ocorrência.",
  obr="Mandatório", S=4, P=3, imp="Base de incidência da multa sem teto pode ser muito maior que a seção 2",
  rel=["d01_multa", "d02_31b", "d02_33", "d02_41"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Quais itens do Anexo I são considerados níveis de serviço para a multa do item 7.4 da RFP: apenas os da seção 2 ou também os prazos das seções 1, 3 e 4?",
  resp="Jurídico")
R("d02_32", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.2", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — item 3.2",
  '"Autenticação multifator (MFA) obrigatória para 100% dos usuários com acesso privilegiado."',
  "Requisito não funcional", "Segurança da Informação/Cyber",
  "Não informa quem fornece a solução de MFA nem quantos usuários privilegiados existem.",
  obr="Mandatório", S=3, P=3, imp="Possível custo de licenças e implantação de MFA",
  fw="ISO/IEC 27001:2022", ctrl="A.8.5 Autenticação segura", assoc="Direta", acao="Esclarecer no Q&A",
  perg="Quantos usuários privilegiados existem e o Banco já possui solução de MFA licenciada?",
  resp="Segurança/Cyber")
R("d02_33", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.3", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — item 3.3",
  '"Revisão (recertificação) trimestral dos acessos concedidos."',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Quatro ciclos por ano; sem ferramenta de IGA no ambiente atual ({d03_iam_atual}), o esforço manual é alto.",
  obr="Mandatório", S=2, P=3, imp="Esforço recorrente de campanhas de recertificação",
  fw="ISO/IEC 27001:2022", ctrl="A.5.18 Direitos de acesso", assoc="Direta", rel=["d03_iam_atual"],
  acao="Precificar", resp="Delivery/Operação")
R("d02_34", "3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — 3.4", "§ 3. GESTÃO DE IDENTIDADES E ACESSOS (IAM) — item 3.4",
  '"É desejável que a solução contemple cofre de senhas para contas privilegiadas (PAM)."',
  "Requisito funcional / de serviço", "Segurança da Informação/Cyber",
  "Desejável, sem indicação de pontuação. Oportunidade em {d03_pam}.",
  obr="Desejável", S=2, P=3, imp="Custo opcional que pode render pontos em Ferramentas e tecnologia",
  fw="ISO/IEC 27001:2022", ctrl="A.8.2 Direitos de acesso privilegiados", assoc="Direta", rel=["d03_pam"],
  acao="Precificar", resp="Pré-venda/Arquitetura")
R("d02_41", "4. TRANSIÇÃO — 4.1", "§ 4. TRANSIÇÃO — item 4.1",
  '"A transição dos serviços deverá ser concluída em até 60 (sessenta) dias corridos a partir da assinatura do contrato."',
  "Prazo / marco", "Transição/Implantação",
  "Diverge da RFP 3.2 (30 dias), ver {d02_transc}.",
  obr="Mandatório", S=4, P=3, imp="Prazo de transição define equipe e custo de implantação",
  rel=["d02_transc", "d01_trans30"], status="Em esclarecimento", acao="Esclarecer no Q&A", resp="Delivery/Operação")
R("d02_transc", "RFP 3.2 × Anexo I 4.1", "p. 2 (impressa: 1) — 3.2 (D01) · § 4. TRANSIÇÃO — item 4.1 (D02)",
  'A: "A transição dos serviços deverá ser concluída em até 30 (trinta) dias corridos a partir da assinatura do contrato." · B: "A transição dos serviços deverá ser concluída em até 60 (sessenta) dias corridos a partir da assinatura do contrato."',
  "Contradição", "Transição/Implantação",
  "Mesma obrigação com prazos diferentes, sem cláusula de precedência ({d01_preced}). A diferença de 30 dias altera a equipe de implantação, o custo da operação em paralelo (4.2) e o risco de não concluir antes do fim do SIEM legado em 31/01/2027 ({d03_siem_fim}).",
  obr="Mandatório", S=4, P=3, imp="Diferença de esforço e custo de transição; risco de descumprimento de prazo",
  fw="ISO/IEC 20000-1", ctrl="Transição de serviços novos ou alterados (identificador a confirmar)", assoc="Correlata",
  rel=["d01_trans30", "d02_41", "d01_preced", "d03_risk_trans"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A RFP (item 3.2) fixa a transição em 30 dias e o Anexo I (item 4.1) em 60 dias corridos a partir da assinatura do contrato. Qual prazo prevalece?",
  resp="Delivery/Operação")
R("d02_42", "4. TRANSIÇÃO — 4.2", "§ 4. TRANSIÇÃO — item 4.2",
  '"Durante a transição, o proponente deverá operar em paralelo com o fornecedor atual, sem custo adicional para o Contratante."',
  "Restrição", "Transição/Implantação / Comercial/Preço",
  "Probabilidade 5: o custo da operação em paralelo é exigido expressamente e não pode ser cobrado à parte. A duração do paralelo depende do prazo de transição (30 ou 60 dias) e é limitada na prática pelo fim do SIEM legado em 31/01/2027 ({d03_siem_fim}).",
  obr="Mandatório", S=3, P=5, imp="Custo de operação dupla absorvido no preço",
  rel=["d02_transc", "d03_siem_fim", "d03_risk_trans"], acao="Precificar", resp="Pricing/Financeiro")
R("d02_51", "5. EQUIPE — 5.1", "§ 5. EQUIPE — item 5.1",
  '"O serviço deverá contar com coordenador com certificação CISSP, dedicado exclusivamente ao contrato."',
  "Restrição", "Pessoas/Equipe",
  "Probabilidade 5: o custo de um coordenador CISSP em dedicação exclusiva por 36 meses é exigido expressamente. Não diz se o coordenador cobre também o IAM nem quando deve ser comprovado.",
  obr="Mandatório", S=3, P=5, imp="Custo fixo de pessoal dedicado",
  rel=["d01_equipe_cert"], acao="Precificar", resp="RH/Staffing")
R("d02_52", "5. EQUIPE — 5.2", "§ 5. EQUIPE — item 5.2",
  '"Os analistas de nível 1 deverão atuar presencialmente na sede do Contratante, em São Paulo/SP, em horário comercial."',
  "Restrição", "Pessoas/Equipe",
  "Alterado pelo Q&A nº 6 ({d04_q6}): N1 pode atuar remotamente no Brasil. Sem precedência definida ({d01_preced}). O texto original não explicava como N1 presencial em horário comercial se combina com o regime 24x7.",
  obr="Mandatório", S=3, P=3, imp="Custo de presença física em São Paulo, se prevalecer o texto original",
  rel=["d04_q6", "d01_preced"], status="Alterado", acao="Registrar premissa na proposta", resp="RH/Staffing")
R("d02_61", "6. RESPONSABILIDADES DO CONTRATANTE — 6.1", "§ 6. RESPONSABILIDADES DO CONTRATANTE — item 6.1",
  '"Disponibilizar acesso remoto seguro (VPN) aos ambientes monitorados."',
  "Responsabilidade / dependência do cliente", "Infraestrutura/Cloud",
  "Dependência para operação remota, inclusive do N1 remoto admitido no Q&A nº 6.",
  S=2, P=3, imp="Atraso no acesso compromete a transição",
  fw="ISO/IEC 27001:2022", ctrl="A.6.7 Trabalho remoto", assoc="Correlata", rel=["d04_q6"],
  acao="Registrar premissa na proposta", resp="Delivery/Operação")
R("d02_62", "6. RESPONSABILIDADES DO CONTRATANTE — 6.2", "§ 6. RESPONSABILIDADES DO CONTRATANTE — item 6.2",
  '"Disponibilizar a documentação técnica do ambiente em até 10 (dez) dias após a assinatura do contrato."',
  "Responsabilidade / dependência do cliente", "Transição/Implantação",
  "Com transição de 30 dias (RFP 3.2), um terço do prazo passa antes de o proponente receber a documentação. Faltam outras dependências do Banco: acesso ao SIEM legado para migração de logs ({d03_migr}), integração com RH e pontos focais.",
  S=3, P=3, imp="Reduz o tempo útil de transição",
  rel=["d01_trans30", "d03_risk_trans", "d03_migr"], acao="Registrar premissa na proposta", resp="Delivery/Operação")

# =============================================================================== D03
doc("D03")
R("d03_inv", "Inventário do documento", "slides 1–5 · slide 5 — notas do apresentador",
  '"Workshop com proponentes — RFP nº 2026-017 — 22/10/2026"',
  "Registro de cobertura", "Administrativo do processo",
  "5 slides lidos, incluindo as notas do apresentador do slide 5 (conteúdo não exibido nos slides). Nenhum slide oculto. O caráter vinculante do material do workshop não está definido ({d01_preced}).",
  imp="Cobertura integral; nenhuma pendência de leitura", rel=["d01_preced"])
R("d03_users", "Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"6.200 usuários ativos"',
  "Dado de dimensionamento", "Comercial/Preço / Operação/Serviços",
  "Diverge da RFP 2.1 ({d03_contr_users}).",
  S=3, P=3, imp="Base de identidades e de licenças por usuário", rel=["d03_contr_users"],
  status="Em esclarecimento", acao="Esclarecer no Q&A", resp="Pricing/Financeiro")
R("d03_contr_users", "RFP 2.1 × slide 2", 'p. 2 (impressa: 1) — 2.1 (D01) · slide 2 — "Números do ambiente" (D03)',
  'A: "abrangendo aproximadamente 4.500 colaboradores" · B: "6.200 usuários ativos"',
  "Contradição", "Comercial/Preço / Operação/Serviços",
  "Diferença de 1.700 usuários (38%). Colaboradores × usuários ativos pode explicar parte (terceiros, contas de serviço), mas a base de preço fica indefinida. Ver subsidiárias ({d03_subsid}) e Q&A nº 5 ({d04_contr_users}).",
  S=4, P=3, imp="Subdimensionamento do IAM e de licenças por usuário",
  rel=["d01_users", "d03_users", "d03_subsid", "d04_contr_users"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="Os 6.200 usuários ativos citados na apresentação incluem terceiros e contas de serviço? Qual número deve ser usado para o IAM e para licenças do SIEM?",
  resp="Pricing/Financeiro")
R("d03_servers", "Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"850 servidores (70% Windows, 30% Linux)"',
  "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Única volumetria de ativos; não há quantidades de estações, ativos de rede e de segurança, aplicações nem EPS ({d04_q3}).",
  S=2, P=3, imp="Base parcial para estimar fontes de log", rel=["d02_14", "d04_q3"], acao="Precificar",
  resp="Pré-venda/Arquitetura")
R("d03_dc", "Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"2 data centers próprios (São Paulo e Campinas)"',
  "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Duas localidades para coletores de logs e eventual atuação presencial.",
  S=2, P=3, imp="Coletores e conectividade em dois sites", acao="Precificar", resp="Pré-venda/Arquitetura")
R("d03_cloud", "Números do ambiente", 'slide 2 — "Números do ambiente"',
  '"Workloads em 2 nuvens públicas"',
  "Dado de dimensionamento", "Infraestrutura/Cloud",
  "Não identifica os provedores nem o volume de contas e workloads; a integração de logs de nuvem depende disso.",
  S=3, P=3, imp="Esforço de integração de nuvem indeterminado", rel=["d02_14"], acao="Esclarecer no Q&A",
  perg="Quais provedores de nuvem pública são usados e quantas contas, assinaturas ou projetos devem ser integrados ao SIEM?",
  resp="Pré-venda/Arquitetura")
R("d03_siem_fim", "Ferramentas atuais", 'slide 3 — "Ferramentas atuais"',
  '"SIEM legado — contrato encerra em 31/01/2027, sem possibilidade de prorrogação"',
  "Premissa do cliente", "Transição/Implantação",
  "Data-limite rígida: após 31/01/2027 não há SIEM legado. Limita a operação em paralelo (Anexo I 4.2) e a extração dos 24 meses de logs históricos ({d03_migr}).",
  S=4, P=3, imp="Qualquer atraso de transição deixa o Banco sem SIEM", rel=["d03_risk_trans", "d02_42", "d03_migr"],
  acao="Registrar premissa na proposta", resp="Delivery/Operação")
R("d03_risk_trans", "Risco combinado de transição", 'slide 3 — "Ferramentas atuais" (D03) · p. 2 (impressa: 1) — 3.1 e 3.2 (D01) · § 4 e § 6.2 (D02)',
  '"SIEM legado — contrato encerra em 31/01/2027, sem possibilidade de prorrogação" · "Início previsto dos serviços 01/02/2027" · "em até 30 (trinta) dias corridos a partir da assinatura do contrato" · "operar em paralelo com o fornecedor atual, sem custo adicional"',
  "Risco para o proponente", "Transição/Implantação",
  "Combinação: SIEM legado termina em 31/01/2027 sem prorrogação; início dos serviços em 01/02/2027; transição de 30 dias (RFP) ou 60 dias (Anexo I) contada de assinatura sem data definida; documentação do ambiente só até 10 dias após a assinatura; paralelo sem custo; migração de 24 meses de logs do SIEM legado; EPS não informado; multa de 10% por ocorrência sem teto e responsabilidade ilimitada desde o início. Se a transição atrasar, o Banco fica sem SIEM e o proponente fica exposto a multas e danos sem limite. Probabilidade 4: o cronograma deixa cerca de 6 semanas entre a entrega das propostas (20/11/2026) e a data-limite de assinatura para 30 dias de transição (01/01/2027), e o fim do SIEM legado é declarado improrrogável; a prorrogação da entrega para 27/11/2026 ({d04_q1}) encurtou essa janela sem mover o início.",
  obr="Mandatório", nat="Inferida", S=5, P=4,
  imp="Exposição a multas e responsabilidade sem limite desde o primeiro dia; possível operação sem ferramenta; equipe de transição ampliada",
  fw="ISO/IEC 27001:2022", ctrl="A.5.30 Prontidão de TIC para continuidade de negócios", assoc="Correlata",
  rel=["d01_inicio", "d01_trans30", "d01_lac_assin", "d02_41", "d02_transc", "d02_42", "d02_62", "d03_siem_fim", "d03_migr", "d01_multa", "d01_resp_ilim", "d04_q3", "d04_q1"],
  acao="Mitigar",
  perg="Considerando o fim do SIEM legado em 31/01/2027 sem prorrogação, qual a data prevista de assinatura? O Banco aceita período de estabilização sem multas e plano de contingência caso a assinatura ocorra após 01/01/2027?",
  resp="Delivery/Operação")
R("d03_iam_atual", "Ferramentas atuais", 'slide 3 — "Ferramentas atuais"',
  '"IAM: Active Directory + scripts internos"',
  "Dado de dimensionamento", "Técnico/Arquitetura / Segurança da Informação/Cyber",
  "Sem ferramenta de IGA: ciclo de vida (Anexo I 3.1) e recertificação (3.3) exigirão implantar ferramenta ou automações, sem que se diga quem fornece ({d02_iam_lac}).",
  S=3, P=3, imp="Esforço de implantação de IAM maior que uma operação assistida", rel=["d02_iam_lac", "d02_33"],
  acao="Precificar", resp="Pré-venda/Arquitetura")
R("d03_pam", "Ferramentas atuais", 'slide 3 — "Ferramentas atuais"',
  '"Não há solução de PAM"',
  "Oportunidade / diferencial", "Segurança da Informação/Cyber",
  "PAM é desejável no Anexo I 3.4 ({d02_34}) e inexistente no ambiente: oferecê-lo pode diferenciar a proposta no critério Ferramentas e tecnologia (15 pontos, {d01_c_ferr}).",
  obr="Desejável", imp="Ganho potencial de pontuação técnica",
  fw="ISO/IEC 27001:2022", ctrl="A.8.2 Direitos de acesso privilegiados", assoc="Direta", rel=["d02_34", "d01_c_ferr"],
  acao="Precificar", resp="Pré-venda/Arquitetura")
R("d03_alertas", "Desafios", 'slide 4 — "Desafios"',
  '"Cerca de 1.200 alertas por dia" · "70% de falsos positivos"',
  "Dado de dimensionamento", "Operação/Serviços",
  "Cerca de 36.000 alertas por mês, dos quais cerca de 840 por dia seriam falsos positivos. Única métrica de volume operacional; não há EPS nem volume de incidentes por criticidade ({d02_24}).",
  S=3, P=3, imp="Base para dimensionar analistas N1 e N2", rel=["d02_24", "d03_meta_fp"], acao="Precificar",
  resp="Delivery/Operação")
R("d03_meta_fp", "Desafios", 'slide 4 — "Desafios"',
  '"Meta: reduzir os falsos positivos para 10% no primeiro trimestre de operação"',
  "Ambiguidade", "Operação/Serviços",
  "Meta ausente da RFP e do Anexo I; não está claro se é SLA/KPI contratual (sujeito à multa de 7.4), critério de avaliação ou expectativa. Reduzir de 70% para 10% em 3 meses, no mesmo período da transição e com ferramenta nova, é meta agressiva; a base de medição não é definida.",
  S=4, P=3, imp="Se contratual, gera risco de multa e exige esforço intenso de tuning no início",
  fw="ITIL 4", ctrl="Prática Melhoria contínua", assoc="Correlata", rel=["d03_alertas", "d01_multa"],
  status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A meta de reduzir falsos positivos para 10% no primeiro trimestre é obrigação contratual (SLA/KPI sujeito a multa) ou expectativa? Como será medida a taxa de falsos positivos?",
  resp="Segurança/Cyber")
R("d03_migr", "Expectativas para o novo serviço", 'slide 5 — "Expectativas para o novo serviço"',
  '"Migração de 24 meses de logs históricos do SIEM legado para a nova plataforma"',
  "Ambiguidade", "Transição/Implantação / Técnico/Arquitetura",
  "Ampliação de escopo ausente da RFP e do Anexo I, apresentada como expectativa. Exige extrair dados do SIEM legado (que termina em 31/01/2027) e armazenar 24 meses adicionais, o dobro da retenção do item 1.3. Volume, formato e cooperação do fornecedor atual não informados.",
  S=4, P=3, imp="Custo de migração e armazenamento não previsto; dependência do fornecedor atual",
  rel=["d03_siem_fim", "d02_contr_logs", "d03_risk_trans", "d02_62"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A migração de 24 meses de logs históricos do SIEM legado faz parte do escopo obrigatório? Qual o volume (TB) e o formato? O Banco garantirá acesso e colaboração do fornecedor atual para a extração antes de 31/01/2027?",
  resp="Pré-venda/Arquitetura")
R("d03_visao", "Expectativas para o novo serviço", 'slide 5 — "Expectativas para o novo serviço"',
  '"Visão unificada de riscos para a diretoria"',
  "Ambiguidade", "Operação/Serviços / Dados/Analytics",
  "Entregável não descrito (painel, relatório executivo ou ferramenta de GRC), sem frequência nem fontes; pode ampliar o escopo para gestão de riscos além de SOC e IAM.",
  S=3, P=3, imp="Possível escopo adicional de reporte e ferramenta",
  fw="ISO 31000", ctrl="Registro e relato de riscos (identificador a confirmar)", assoc="Correlata",
  status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O que se espera da visão unificada de riscos para a diretoria: painel do SIEM, relatório executivo periódico ou ferramenta de GRC? Está no escopo obrigatório?",
  resp="Pré-venda/Arquitetura")
R("d03_subsid", "Expectativas para o novo serviço — notas", "slide 5 — notas do apresentador (D03) · p. 2 (impressa: 1) — 2.1 (D01)",
  'A: "abrangendo aproximadamente 4.500 colaboradores" · B: "as subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários adicionais) também deverão ser incluídas no escopo"',
  "Contradição", "Comercial/Preço / Jurídico/Contratual",
  "Ampliação de escopo só nas notas do apresentador (não exibidas nos slides): duas subsidiárias e cerca de 900 usuários. A RFP descreve o objeto para o Banco; contratante, faturamento, declaração do Anexo III (só dados do Banco) e regulação aplicável às subsidiárias não são tratados. Não se sabe se o conteúdo foi comunicado verbalmente no workshop.",
  S=4, P=3, imp="Escopo e entidades contratantes indefinidos; possível subprecificação",
  rel=["d01_users", "d03_contr_users", "d04_contr_users", "d01_dados_br"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="As subsidiárias Horizonte Seguros e Horizonte Investimentos (cerca de 900 usuários), mencionadas nas notas da apresentação do workshop, fazem parte do escopo? Em caso afirmativo, serão contratantes no mesmo contrato e o Anexo III e a Resolução CMN nº 4.893/2021 se aplicam a elas?",
  resp="Bid Manager")

# =============================================================================== D04
doc("D04")
R("d04_inv", "Inventário do documento", 'abas "Instruções", "Q&A Rodada 1", "Questionário Técnico" e "Pesos" (OCULTA)',
  '"Questionário Técnico e Respostas aos Esclarecimentos — RFP nº 2026-017"',
  "Registro de cobertura", "Administrativo do processo",
  "Quatro abas lidas, inclusive a aba oculta Pesos (A1:B9), que contém pesos e regra de dedução não publicados na RFP. Sem linhas ou colunas ocultas nas abas.",
  imp="Cobertura integral; nenhuma pendência de leitura", rel=["d04_pesos", "d04_pesos_a9"])
R("d04_instr", "Instruções", 'aba "Instruções" · A3',
  '"O preenchimento de todas as abas deste arquivo é obrigatório. Questionários incompletos serão desclassificados."',
  "Critério eliminatório / de habilitação", "Administrativo do processo",
  "Agrava a RFP 4.4 ({d01_qt}), que não previa sanção. Probabilidade 5: a desclassificação decorre diretamente do texto para questionário incompleto.",
  obr="Mandatório", S=5, P=5, imp="Desclassificação", rel=["d01_qt", "d04_instr_amb"], acao="Atender",
  resp="Pré-venda/Arquitetura")
R("d04_instr_amb", "Instruções", 'aba "Instruções" · A3',
  '"O preenchimento de todas as abas deste arquivo é obrigatório."',
  "Ambiguidade", "Administrativo do processo",
  "Literalmente, todas as abas inclui Q&A Rodada 1 (respostas do próprio Banco) e a aba oculta Pesos, sem campos para o proponente. Também não define se Parcial ou Comentários vazios tornam o questionário incompleto. Probabilidade 2: é improvável que o Banco exija preencher abas de sua autoria, mas a sanção é desclassificação.",
  obr="Mandatório", S=5, P=2, imp="Leitura literal pode levar à desclassificação",
  rel=["d04_instr"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A exigência de preencher todas as abas refere-se apenas à aba Questionário Técnico? A coluna Comentários é de preenchimento obrigatório?",
  resp="Bid Manager")
R("d04_risk_qa", "Q&A Rodada 1 × cronograma", 'aba "Q&A Rodada 1" · B2:B7 (D04) · p. 2 (impressa: 1) — 3.1 (D01)',
  '"12/11/2026" · "Prazo final para envio de perguntas 05/11/2026"',
  "Risco para o proponente", "Administrativo do processo",
  "O cronograma prevê uma única rodada de perguntas, encerrada em 05/11/2026; as respostas são de 12/11/2026 e duas foram evasivas (nº 3 e nº 4). As contradições e lacunas desta matriz (transição, usuários, região de dados, pontuação 60 × 65, Anexo IV, matriz de criticidade, aba Pesos) podem ficar sem canal formal antes da entrega em 27/11/2026. Probabilidade 4: o prazo final de perguntas está expresso e já transcorrido na data do Q&A, sem previsão de nova rodada. Associação de boa prática: gestão de esclarecimentos no processo de proposta.",
  nat="Inferida", S=4, P=4, imp="Proposta terá de ser precificada com premissas e ressalvas, com risco de desconformidade",
  fw="APMP Body of Knowledge", ctrl="Gestão de perguntas e esclarecimentos (identificador a confirmar)", assoc="Boa prática",
  rel=["d01_perguntas", "d01_preced", "d04_q3", "d04_q4"], acao="Mitigar",
  perg="O Banco aceitará uma segunda rodada de esclarecimentos, considerando a prorrogação da entrega para 27/11/2026 e as divergências entre RFP, Anexo I e apresentação?",
  resp="Bid Manager")
R("d04_q1", "Q&A Rodada 1 — pergunta nº 1 (RFP, item 3.1)", 'aba "Q&A Rodada 1" · E2 (nº 1, 12/11/2026)',
  '"A data de entrega das propostas fica prorrogada para 27/11/2026, até as 18h."',
  "Prazo / marco", "Administrativo do processo",
  "Altera a RFP 3.1 ({d01_entrega}). As demais datas (início em 01/02/2027) não mudaram, o que encurta a janela até o início ({d03_risk_trans}). Probabilidade 2: data clara; impacto só por falha de controle ou disputa de precedência.",
  obr="Mandatório", S=5, P=2, imp="Proposta intempestiva não é recebida",
  rel=["d01_entrega", "d03_risk_trans"], acao="Atender", resp="Bid Manager")
R("d04_q2", "Q&A Rodada 1 — pergunta nº 2 (RFP, item 5.1 c)", 'aba "Q&A Rodada 1" · E3 (nº 2, 12/11/2026)',
  '"Não. O SOC deverá estar localizado em território nacional."',
  "Critério eliminatório / de habilitação", "Operação/Serviços / Regulatório/Compliance",
  "Confirma a RFP 5.1 c ({d01_soc_br}). Trata do local de operação do SOC; não esclarece o local dos dados do SIEM em nuvem ({d02_contr_regiao}). Probabilidade 5: inabilitação expressa na RFP para SOC fora do país.",
  obr="Mandatório", S=5, P=5, imp="Inabilitação de SOC no exterior",
  rel=["d01_soc_br", "d02_contr_regiao"], status="Duplicado", acao="Atender", resp="Compliance")
R("d04_q3", "Q&A Rodada 1 — pergunta nº 3 (Anexo I, item 1.4)", 'aba "Q&A Rodada 1" · E4 (nº 3, 12/11/2026)',
  'Não localizado (volumetria de EPS). Resposta: "A volumetria será informada somente ao proponente vencedor."',
  "Lacuna", "Técnico/Arquitetura / Comercial/Preço",
  "EPS é a principal base de licenciamento e armazenamento do SIEM (1.2), da retenção de 12 meses e 5 anos (1.3 e 1.6) e do esforço de integração (1.4). Únicas referências: 850 servidores, 2 data centers, 2 nuvens e cerca de 1.200 alertas por dia ({d03_servers}, {d03_alertas}). Probabilidade 5: informação indispensável ao preço formalmente recusada pelo cliente.",
  obr="Mandatório", S=4, P=5, imp="Preço do SIEM e do armazenamento só pode ser estimado; risco de subprecificação ou de proposta não competitiva",
  rel=["d02_12", "d02_14", "d02_contr_logs", "d03_servers", "d03_alertas"], acao="Registrar premissa na proposta",
  perg="Na impossibilidade de informar o EPS, o Banco aceita que a proposta adote volumetria de referência (EPS e GB/dia) como premissa, com revisão de preço se a volumetria real for superior?",
  resp="Pricing/Financeiro")
R("d04_q4", "Q&A Rodada 1 — pergunta nº 4 (RFP, item 7.4)", 'aba "Q&A Rodada 1" · E5 (nº 4, 12/11/2026)',
  '"As condições do item 7 permanecem inalteradas."',
  "Risco para o proponente", "Jurídico/Contratual / Financeiro",
  "Combinação: multa de 10% do valor mensal por ocorrência sem teto (7.4, {d01_multa}), aplicável a qualquer SLA do Anexo I ({d02_sla_scope}); responsabilidade integral e ilimitada por quaisquer danos de incidentes (7.5, {d01_resp_ilim}); seguro de valor indefinido (7.6, {d01_seguro}); pagamento em até 60 dias (7.3, {d01_pgto}). Perguntado sobre limite das multas, o Banco não respondeu objetivamente e manteve todo o item 7. Probabilidade 4: recusa documentada de alterar o item 7 e multa automática por ocorrência.",
  obr="Mandatório", nat="Inferida", S=5, P=4, imp="Exposição financeira e jurídica ilimitada; risco pode não ser segurável nem precificável",
  fw="ISO 31000", ctrl="Avaliação e tratamento de riscos (identificador a confirmar)", assoc="Correlata",
  rel=["d01_multa", "d01_resp_ilim", "d01_seguro", "d01_pgto", "d02_sla_scope"], acao="Avaliar Go/No-Go",
  perg="O Banco admite que a proposta apresente ressalvas ao item 7 (teto de multas e de responsabilidade) sem que isso cause desclassificação?",
  resp="Jurídico")
R("d04_q5", "Q&A Rodada 1 — pergunta nº 5 (RFP, item 2.1)", 'aba "Q&A Rodada 1" · E6 (nº 5, 12/11/2026)',
  '"Considerar 5.000 usuários."',
  "Dado de dimensionamento", "Comercial/Preço",
  "Altera a base da RFP 2.1 (4.500, {d01_users}); continua divergente da apresentação ({d04_contr_users}).",
  S=3, P=3, imp="Nova base de preço para IAM e licenças por usuário",
  rel=["d01_users", "d04_contr_users"], status="Em esclarecimento", acao="Esclarecer no Q&A", resp="Pricing/Financeiro")
R("d04_contr_users", "Q&A nº 5 × apresentação", 'aba "Q&A Rodada 1" · E6 (D04) · slide 2 — "Números do ambiente" e slide 5 — notas do apresentador (D03)',
  'A: "Considerar 5.000 usuários." · B: "6.200 usuários ativos" · "(cerca de 900 usuários adicionais)"',
  "Contradição", "Comercial/Preço",
  "Quatro números para a mesma base: 4.500 (RFP), 5.000 (Q&A), 6.200 (apresentação) e 7.100 (6.200 mais 900 das subsidiárias). Entre 5.000 e 7.100 a diferença é de 42%. Se o preço usar 5.000 e o contrato não limitar o escopo a esse número, o proponente absorve até 2.100 identidades.",
  S=4, P=3, imp="Subprecificação do IAM e de licenças por usuário",
  rel=["d01_users", "d03_contr_users", "d03_subsid", "d04_q5"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="O Q&A nº 5 indica 5.000 usuários; a apresentação indica 6.200 usuários ativos mais cerca de 900 das subsidiárias. O contrato limitará o escopo a 5.000 usuários, com aditivo para excedentes? As subsidiárias estão incluídas nos 5.000?",
  resp="Pricing/Financeiro")
R("d04_q6", "Q&A Rodada 1 — pergunta nº 6 (Anexo I, item 5.2)", 'aba "Q&A Rodada 1" · E7 (nº 6, 12/11/2026)',
  '"Sim, desde que em território nacional."',
  "Restrição", "Pessoas/Equipe",
  "Altera o Anexo I 5.2 ({d02_52}): N1 pode atuar remotamente no Brasil, o que reduz custo de presença em São Paulo. Sem precedência definida ({d01_preced}), convém registrar a resposta como premissa.",
  obr="Mandatório", S=2, P=3, imp="Redução de custo de alocação, condicionada à precedência do Q&A",
  rel=["d02_52", "d01_preced"], acao="Registrar premissa na proposta", resp="RH/Staffing")
R("d04_qt01", "Questionário Técnico — QT-01", 'aba "Questionário Técnico" · B2:C2 (QT-01)',
  '"Possui certificação ISO/IEC 27001 com escopo que inclua os serviços de SOC?" · Obrigatório: "Sim"',
  "Critério de avaliação / pontuação", "Segurança da Informação/Cyber",
  "Repete a RFP 5.1 a ({d01_iso}). Peso 3 na aba oculta Pesos.",
  obr="Mandatório", S=3, P=3, imp="Pontuação do questionário (peso 3)",
  fw="ISO/IEC 27001:2022", ctrl="Certificação do SGSI (cláusulas 4 a 10)", assoc="Direta",
  rel=["d01_iso", "d04_pesos"], status="Duplicado", acao="Atender", resp="Compliance")
R("d04_qt02", "Questionário Técnico — QT-02", 'aba "Questionário Técnico" · B3:C3 (QT-02)',
  '"Oferece integração nativa com plataforma SOAR?" · Obrigatório: "Não"',
  "Critério de avaliação / pontuação", "Técnico/Arquitetura",
  "Ausente do Anexo I. Embora não obrigatório, Não atende reduz a Nota Técnica em 2 pontos pela regra oculta ({d04_pesos_a9}). SOAR de terceiro pode esbarrar na vedação de subcontratação ({d02_subcont_amb}).",
  obr="Desejável", S=3, P=3, imp="Perda de 2 pontos técnicos se não ofertado",
  rel=["d04_pesos_a9", "d02_subcont_amb"], acao="Precificar", resp="Pré-venda/Arquitetura")
R("d04_qt03", "Questionário Técnico — QT-03", 'aba "Questionário Técnico" · B4:C4 (QT-03)',
  '"Retém os logs online por no mínimo 12 meses?" · Obrigatório: "Sim"',
  "Critério de avaliação / pontuação", "Técnico/Arquitetura",
  "Sugere que os 12 meses do Anexo I 1.3 são de retenção online, sem tratar dos 5 anos do item 1.6 ({d02_contr_logs}).",
  obr="Mandatório", S=3, P=3, imp="Pontuação do questionário (peso 2)",
  fw="ISO/IEC 27001:2022", ctrl="A.8.15 Registro de logs", assoc="Direta", rel=["d02_contr_logs", "d02_13"],
  acao="Atender", resp="Pré-venda/Arquitetura")
R("d04_qt04", "Questionário Técnico — QT-04", 'aba "Questionário Técnico" · B5:C5 (QT-04)',
  '"Atende aos requisitos da Resolução CMN nº 4.893/2021?" · Obrigatório: "Sim"',
  "Critério de avaliação / pontuação", "Regulatório/Compliance",
  "A Resolução dirige-se à instituição financeira; não está claro o que o proponente deve demonstrar para responder Atende (cláusulas contratuais, localização de dados, relatórios ao Banco). Peso 3, o maior do questionário.",
  obr="Mandatório", S=3, P=3, imp="Resposta sem critério objetivo em item de peso máximo",
  fw="Resolução CMN nº 4.893/2021", ctrl="Requisitos para prestadores de serviços de processamento, armazenamento e nuvem (identificador a confirmar)", assoc="Direta",
  rel=["d01_4893", "d04_pesos"], acao="Esclarecer no Q&A",
  perg="Para o QT-04, quais requisitos da Resolução CMN nº 4.893/2021 o proponente deve demonstrar e com que evidências?",
  resp="Compliance")
R("d04_qt05", "Questionário Técnico — QT-05", 'aba "Questionário Técnico" · B6:C6 (QT-05)',
  '"Oferece serviço de threat intelligence?" · Obrigatório: "Não"',
  "Critério de avaliação / pontuação", "Segurança da Informação/Cyber",
  "Ausente do Anexo I. Não atende custa 2 pontos pela regra oculta ({d04_pesos_a9}). Feeds de terceiros podem esbarrar na vedação de subcontratação ({d02_subcont_amb}).",
  obr="Desejável", S=3, P=3, imp="Perda de 2 pontos técnicos se não ofertado",
  fw="ISO/IEC 27001:2022", ctrl="A.5.7 Inteligência de ameaças", assoc="Direta", rel=["d04_pesos_a9", "d02_subcont_amb"],
  acao="Precificar", resp="Segurança/Cyber")
R("d04_qt06", "Questionário Técnico — QT-06", 'aba "Questionário Técnico" · B7:C7 (QT-06)',
  '"Possui equipe com certificações reconhecidas pelo mercado?" · Obrigatório: "Sim"',
  "Critério de avaliação / pontuação", "Pessoas/Equipe",
  "Tão vago quanto a RFP 5.2 ({d01_equipe_cert}): não define certificações nem quantidade.",
  obr="Mandatório", S=3, P=3, imp="Pontuação do questionário (peso 2) com critério subjetivo",
  rel=["d01_equipe_cert", "d04_pesos"], acao="Esclarecer no Q&A",
  perg="Quais certificações são consideradas reconhecidas pelo mercado para o QT-06 e quantos profissionais certificados são esperados?",
  resp="RH/Staffing")
R("d04_pesos", "Pesos (aba oculta)", 'aba "Pesos" (OCULTA) · A1:B7',
  '"QT-01" "3" · "QT-02" "1" · "QT-03" "2" · "QT-04" "3" · "QT-05" "2" · "QT-06" "2"',
  "Critério de avaliação / pontuação", "Administrativo do processo",
  "Pesos não divulgados na RFP nem nas abas visíveis; a RFP (6.2) não prevê pontuação do questionário. Não se sabe como os pesos entram na Nota Técnica.",
  S=4, P=3, imp="Critério de julgamento oculto que pode alterar a Nota Técnica",
  rel=["d04_contr_pesos", "d04_pesos_a9"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A aba oculta Pesos atribui pesos às questões QT-01 a QT-06. Como esses pesos compõem a Nota Técnica e em qual critério do item 6.2 se inserem?",
  resp="Bid Manager")
R("d04_pesos_a9", "Pesos (aba oculta)", 'aba "Pesos" (OCULTA) · A9',
  '"Requisitos não obrigatórios respondidos como \'Não atende\' reduzem a Nota Técnica em 2 (dois) pontos cada."',
  "Critério de avaliação / pontuação", "Administrativo do processo",
  "Regra oculta: QT-02 e QT-05 (não obrigatórios) custam 2 pontos cada se respondidos Não atende, até 4 pontos (6,7% de 60), aproximando a proposta do corte de 70% ({d01_desclass}). Torna itens não obrigatórios obrigatórios na prática. Não define o efeito de Parcial nem de Não atende em itens obrigatórios. Probabilidade 4: a dedução é automática por item, por texto expresso.",
  obr="Mandatório", S=4, P=4, imp="Perda de pontuação não prevista na RFP; risco de ficar abaixo do mínimo técnico",
  rel=["d04_qt02", "d04_qt05", "d01_desclass", "d04_contr_pesos"], acao="Precificar",
  perg="A regra da aba Pesos (dedução de 2 pontos por requisito não obrigatório respondido Não atende) está em vigor, embora não conste da RFP? Qual o efeito de respostas Parcial?",
  resp="Bid Manager")
R("d04_contr_pesos", "RFP 6.2 × aba Pesos", 'p. 4 (impressa: 3) — 6.2 (D01) · aba "Pesos" (OCULTA) · A9 (D04)',
  'A: "A Nota Técnica, de no máximo 60 (sessenta) pontos, será atribuída conforme os critérios abaixo" · B: "Requisitos não obrigatórios respondidos como \'Não atende\' reduzem a Nota Técnica em 2 (dois) pontos cada."',
  "Contradição", "Administrativo do processo",
  "A RFP limita a Nota Técnica aos quatro critérios do 6.2; a aba oculta cria pesos e deduções adicionais não publicados. Critério de julgamento não divulgado aos proponentes; soma-se à incoerência 60 × 65 ({d01_contr_60_65}).",
  S=4, P=3, imp="Nota técnica calculada por regra que o proponente não deveria conhecer; base de questionamento do resultado",
  rel=["d01_contr_60_65", "d04_pesos", "d04_pesos_a9"], status="Em esclarecimento", acao="Esclarecer no Q&A",
  perg="A Nota Técnica é composta apenas pelos critérios do item 6.2 da RFP ou também pelos pesos e deduções da aba Pesos do questionário? Favor publicar a regra completa.",
  resp="Bid Manager")


# =============================================================================== montagem
def band(score, s):
    b = "Baixa" if score <= 4 else "Média" if score <= 9 else "Alta" if score <= 15 else "Crítica"
    if s == 5 and b in ("Baixa", "Média"):
        b = "Alta"
    return b


counters = {}
ids = {}
for r in ROWS:
    counters[r["doc"]] = counters.get(r["doc"], 0) + 1
    rid = f'{r["doc"]}-{counters[r["doc"]]:03d}'
    assert r["key"] not in ids, r["key"]
    ids[r["key"]] = rid
    r["id"] = rid


def sub(text):
    def rep(m):
        k = m.group(1)
        if k not in ids:
            raise KeyError(k)
        return ids[k]
    return re.sub(r"\{(\w+)\}", rep, text)


COLS = ["ID", "Documento", "Versão/Data", "Seção/Cláusula", "Localizador", "Evidência", "Tipo de item",
        "Domínio", "Descrição analítica", "Obrigatoriedade", "Natureza da evidência", "Severidade",
        "Probabilidade", "Criticidade", "Impacto para o proponente", "Framework/Referência",
        "Controle/Cláusula", "Tipo de associação", "IDs relacionados", "Status de vigência",
        "Ação recomendada", "Pergunta de esclarecimento", "Responsável interno sugerido"]


def clean(x):
    x = sub(str(x)).replace("|", "/").replace("\n", " ").strip()
    return x if x else "—"


lines = []
for r in ROWS:
    name, ver, _ = DOCS[r["doc"]]
    if r["S"] is None:
        sev = prob = crit = "—"
    else:
        s, p = r["S"], r["P"]
        sev, prob = f"{s} · {SEV[s]}", f"{p} · {PROB[p]}"
        crit = f"{s * p} · {band(s * p, s)}"
    rel = " · ".join(dict.fromkeys(ids[k] for k in r["rel"])) if r["rel"] else "—"
    cells = [r["id"], name, ver, r["sec"], r["loc"], r["ev"], r["tipo"], r["dom"], r["desc"], r["obr"], r["nat"],
             sev, prob, crit, r["imp"], r["fw"], r["ctrl"], r["assoc"], rel, r["status"], r["acao"], r["perg"],
             r["resp"]]
    lines.append("| " + " | ".join(clean(c) for c in cells) + " |")

last = ROWS[-1]["id"]
pend = [ids["d01_anexo4"] + " (Anexo IV — Planilha de Preços, citado e não fornecido)",
        ids["d01_anexo2"] + " (Anexo II — inferido, não fornecido)",
        ids["d02_24"] + " (matriz de classificação de criticidade do Contratante, citada e não fornecida)"]

out = []
out.append("# RFP nº 2026-017 — Matriz Analítica")
out.append("")
out.append("Banco Horizonte Fictício S.A. · Serviços gerenciados de SOC e IAM · Valor estimado do contrato: não informado (severidade avaliada pelo critério qualitativo)")
out.append("")
out.append("## Documentos")
out.append("")
out.append("| Código | Arquivo | Tipo | Versão/Data |")
out.append("|---|---|---|---|")
for code, (name, ver, tipo) in DOCS.items():
    out.append(f"| {code} | {name} | {tipo} | {ver} |")
out.append("")
out.append("## Matriz")
out.append("")
out.append("| " + " | ".join(COLS) + " |")
out.append("|" + "---|" * len(COLS))
out.extend(lines)
out.append("")
out.append("## Status")
out.append("")
out.append("✅ STATUS: ANÁLISE CONCLUÍDA")
out.append(f"Documentos processados: 4 de 4 · Total de itens: {len(ROWS)} (de D01-001 a {last})")
out.append("Pendências de cobertura: " + " · ".join(pend) + " · nenhuma pendência de leitura (p. 6 do D01 lida por OCR; aba oculta e notas de slide analisadas)")
out.append('Não é necessário enviar "continuar".')
OUT.write_text("\n".join(out) + "\n", encoding="utf-8")

# resumo por documento para o chat
from collections import Counter
for code in DOCS:
    rs = [r for r in ROWS if r["doc"] == code]
    print(code, len(rs), rs[0]["id"], rs[-1]["id"])
crit = Counter(band(r["S"] * r["P"], r["S"]) for r in ROWS if r["S"] is not None)
print("crit", dict(crit), "total", len(ROWS))
for k in ("d01_anexo2", "d01_anexo4", "d02_24"):
    print(k, ids[k])
