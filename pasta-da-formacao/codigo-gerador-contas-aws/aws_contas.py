

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER

doc = SimpleDocTemplate(
    "AWS_Contas_Senhas.pdf",
    pagesize=A4,
    leftMargin=15*mm,
    rightMargin=15*mm,
    topMargin=15*mm,
    bottomMargin=15*mm
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('Title', parent=styles['Normal'],
    fontSize=14, fontName='Helvetica-Bold',
    textColor=colors.HexColor('#FF9900'),
    alignment=TA_CENTER, spaceAfter=6)

section_style = ParagraphStyle('Section', parent=styles['Normal'],
    fontSize=10, fontName='Helvetica-Bold',
    textColor=colors.HexColor('#232F3E'),
    spaceAfter=4, spaceBefore=8)

warning_style = ParagraphStyle('Warning', parent=styles['Normal'],
    fontSize=9, fontName='Helvetica-Bold',
    textColor=colors.HexColor('#CC0000'),
    spaceAfter=3)

normal_style = ParagraphStyle('Normal2', parent=styles['Normal'],
    fontSize=8.5, fontName='Helvetica',
    textColor=colors.HexColor('#222222'),
    spaceAfter=2, leftIndent=8)

arrow_style = ParagraphStyle('Arrow', parent=styles['Normal'],
    fontSize=8.5, fontName='Helvetica',
    textColor=colors.HexColor('#333333'),
    spaceAfter=2, leftIndent=16)

sub_style = ParagraphStyle('Sub', parent=styles['Normal'],
    fontSize=8.5, fontName='Helvetica',
    textColor=colors.HexColor('#444444'),
    spaceAfter=2, leftIndent=30)

label_style = ParagraphStyle('Label', parent=styles['Normal'],
    fontSize=8, fontName='Helvetica-Bold',
    textColor=colors.HexColor('#FF9900'),
    spaceAfter=2)

code_style = ParagraphStyle('Code', parent=styles['Normal'],
    fontSize=8.5, fontName='Courier',
    textColor=colors.HexColor('#003087'),
    backColor=colors.HexColor('#F5F5F5'),
    spaceAfter=3, leftIndent=8)

story = []

# Header with AWS orange bar
story.append(Paragraph("&#9729; AWS — Controle de Contas e Senhas", title_style))
story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#FF9900')))
story.append(Spacer(1, 6))

# ATENÇÃO block
atencao_data = [
    [Paragraph("⚠  ATENCAO — Antes de encerrar a conta:", warning_style)],
    [Paragraph("→ Criar a nova conta e fazer as transferencias.", arrow_style)],
    [Paragraph("→ Assistir o video: <i>Cadastrando uma Conta na AWS</i>", arrow_style)],
    [Paragraph("→ Criar as transferencias das regras e autorizacoes do novo usuario:", arrow_style)],
    [Paragraph("  - Criar o controle de aviso de custo", sub_style)],
    [Paragraph("  - Criar a autenticacao de dois fatores", sub_style)],
    [Paragraph("  - Criar os Security Group", sub_style)],
    [Paragraph("  - Criar as Roles", sub_style)],
    [Paragraph("  - Criar as Policies", sub_style)],
    [Paragraph("  - Criar os Users", sub_style)],
    [Paragraph("  - Criar o  --profile bia", sub_style)],
    [Paragraph("  - Criar o Iam group SAM_PERMISSION", sub_style)],
    [Paragraph("  - Criar as VPC: aws-modulo-1-vpc-visual / aws-modulo-1-vpc-manual", sub_style)],
    [Paragraph("  - Outros", sub_style)],
]

atencao_table = Table(atencao_data, colWidths=[175*mm])
atencao_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF8F0')),
    ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#FF9900')),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.HexColor('#FFF8F0'), colors.HexColor('#FFFFFF')]),
]))
story.append(atencao_table)
story.append(Spacer(1, 6))

# Encerramento
encerr_data = [
    [Paragraph("→ Matar todos os processos criados da conta antiga — Desalocando tudo e CANCELA conta.", warning_style)],
]
encerr_table = Table(encerr_data, colWidths=[175*mm])
encerr_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF0F0')),
    ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#CC0000')),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(encerr_table)
story.append(Spacer(1, 6))

# Login info
login_data = [
    [Paragraph("&#128274;  Abrir as Contas:", section_style),
     Paragraph("Login: e-mail  +  Senha: <b>Masterkey#101624</b>  +  Authenticator Code MFA", code_style)],
]
login_table = Table(login_data, colWidths=[45*mm, 130*mm])
login_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EAF4FB')),
    ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#0073BB')),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(login_table)
story.append(Spacer(1, 8))

# Accounts table
story.append(Paragraph("&#128196;  Contas Cadastradas", section_style))

header = [
    Paragraph("Nome da Conta", label_style),
    Paragraph("Usuario Root", label_style),
    Paragraph("Cartao", label_style),
    Paragraph("Cadastro / Venc.", label_style),
    Paragraph("Status", label_style),
]

ps = ParagraphStyle('td', fontSize=8, fontName='Helvetica', textColor=colors.HexColor('#222222'))
ps_mono = ParagraphStyle('mono', fontSize=7.5, fontName='Courier', textColor=colors.HexColor('#003087'))
ps_status = ParagraphStyle('status', fontSize=7.5, fontName='Helvetica-Bold')

def status_color(s):
    if 'ativa' in s: return colors.HexColor('#1D8348')
    if 'cancelada' in s: return colors.HexColor('#CC0000')
    if 'vencida' in s: return colors.HexColor('#B7950B')
    return colors.HexColor('#555555')

accounts = [
    ("aws-edvaldojose-c1-2024", "edvaldojose003@gmail.com", "cartao edv", "Abr/2023 - Dez/2024", "[c1] free-tier-vencida*"),
    ("aws-edvaldojose-c2-2025", "edvaldojose.aws@gmail.com", "cartao mae", "Jun/2024 - Jun/2025", "[c2] conta-ativa"),
    ("aws-edvaldojose-c3-2026", "dev.edvaldojose@gmail.com", "cartao mae", "Mar/2026 - Mar/202x", "[c3] conta-pad-ativa"),
    ("aws-edvaldojose-c4-ft-2026", "eddvdev@gmail.com", "cartao irma", "Mar/2026 - Mar/2027", "[c4] conta-pad-free-tier"),
    ("---", "---", "---", "---", "---"),
    ("aws-edvaldojose-c...", "edvaldojsnet@gmail.com", "cartao mae", "Abr/2025 - Abr/2026", "[ ]"),
    ("aws-edvaldojose-c...", "edvaldojose.dev@outlook.com", "cartao mae", "Abr/2026 - Abr/2027", "[ ]"),
    ("aws-edvaldojose-c...", "edvaldojose.dev@gmail.com", "cartao mae", "Abr/2024", "conta-cancelada []"),
]

table_data = [header]
row_colors = []
for i, (nome, email, cartao, datas, status) in enumerate(accounts):
    sc = status_color(status)
    sp = ParagraphStyle(f'st{i}', fontSize=7.5, fontName='Helvetica-Bold', textColor=sc)
    table_data.append([
        Paragraph(nome, ps_mono),
        Paragraph(email, ps_mono),
        Paragraph(cartao, ps),
        Paragraph(datas, ps),
        Paragraph(status, sp),
    ])

acc_table = Table(table_data, colWidths=[45*mm, 55*mm, 22*mm, 30*mm, 23*mm])
acc_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#232F3E')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 8),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#FFFFFF'), colors.HexColor('#F4F6F7')]),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#AAAAAA')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('LEFTPADDING', (0,0), (-1,-1), 5),
    ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(acc_table)
story.append(Spacer(1, 8))

# Modelo nova conta
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#FF9900')))
story.append(Spacer(1, 4))
story.append(Paragraph("&#9733;  Modelo para Nova Conta AWS (franquia anual de 750hs/mes) — formato: seuemail+c(x)", section_style))

model_header = [
    Paragraph("Usuario Root", label_style),
    Paragraph("Nome da Conta", label_style),
    Paragraph("Cartao", label_style),
    Paragraph("Cadastro / Venc.", label_style),
]
model_data = [
    model_header,
    [
        Paragraph("edvaldojose.aws+c3@gmail.com", ps_mono),
        Paragraph("aws-edvaldojose-c3-2026", ps_mono),
        Paragraph("edv", ps),
        Paragraph("mm-aaaa / mm-aaaa", ps),
    ]
]
model_table = Table(model_data, colWidths=[65*mm, 55*mm, 20*mm, 35*mm])
model_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#232F3E')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#FFF8F0')),
    ('BOX', (0,0), (-1,-1), 2, colors.HexColor('#FF9900')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#DDDDDD')),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(model_table)
story.append(Spacer(1, 8))

# Contas ativas
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#1D8348')))
story.append(Spacer(1, 4))
story.append(Paragraph("&#9989;  Contas Ativas da AWS", section_style))

ativas = [
    ("[aws-edvaldojose-c1-2024]", "Com creditos no valor de $300 ate agosto/2025."),
    ("[aws-edvaldojose-c2-2025]", "Com creditos de 750hs da free tier."),
    ("[aws-edvaldojose-c3-2026]", "Com creditos de U$xxx solicitado."),
    ("[aws-edvaldojose-c4-ft-2026]", "Com creditos de U$200 da nova free tier."),
]

ps_conta = ParagraphStyle('conta', fontSize=8.5, fontName='Courier-Bold', textColor=colors.HexColor('#0073BB'))
ps_desc = ParagraphStyle('desc', fontSize=8.5, fontName='Helvetica', textColor=colors.HexColor('#222222'))

ativas_data = [[Paragraph(c, ps_conta), Paragraph(d, ps_desc)] for c, d in ativas]
ativas_table = Table(ativas_data, colWidths=[65*mm, 110*mm])
ativas_table.setStyle(TableStyle([
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.HexColor('#F0FFF4'), colors.HexColor('#FFFFFF')]),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#1D8348')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(ativas_table)
story.append(Spacer(1, 6))

# Nova Freetier
story.append(Paragraph("&#128640;  Contas Novas usando a nova Freetier:", section_style))
freetier_data = [
    [Paragraph("[aws-edvaldojose-c3-2026]", ps_conta), Paragraph("edvaldojose.aws+c3@gmail.com", ps_mono)],
]
ft_table = Table(freetier_data, colWidths=[65*mm, 110*mm])
ft_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EAF4FB')),
    ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#0073BB')),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(ft_table)

# Footer
story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#AAAAAA')))
footer_style = ParagraphStyle('footer', fontSize=7, fontName='Helvetica', textColor=colors.HexColor('#888888'), alignment=TA_CENTER)
story.append(Paragraph("Documento confidencial — AWS Account Manager | Gerado automaticamente", footer_style))

doc.build(story)
print("PDF criado com sucesso!")
