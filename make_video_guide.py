from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

doc = SimpleDocTemplate(
    "C:/Users/heywi/Desktop/wilder_screenkeys_video_guide.pdf",
    pagesize=letter,
    leftMargin=0.75*inch,
    rightMargin=0.75*inch,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch
)

styles = getSampleStyleSheet()
story = []

heading = ParagraphStyle('heading', parent=styles['Title'], fontSize=22, spaceAfter=6)
subhead = ParagraphStyle('subhead', parent=styles['Heading2'], fontSize=13, spaceBefore=14, spaceAfter=4, textColor=colors.HexColor('#3a6e1f'))
body = ParagraphStyle('body', parent=styles['Normal'], fontSize=11, spaceAfter=4, leading=16)
note = ParagraphStyle('note', parent=styles['Normal'], fontSize=10, textColor=colors.HexColor('#666666'), spaceAfter=4, leading=14)

story.append(Paragraph("Wilder Screen Keys", heading))
story.append(Paragraph("Demo Video — Shot Guide", styles['Heading2']))
story.append(Spacer(1, 0.15*inch))
story.append(Paragraph("Keep this next to your monitor while recording. One take is just practice — do it three times if you need to.", note))
story.append(Spacer(1, 0.1*inch))

# Before you record
story.append(Paragraph("Before You Record", subhead))
items = [
    "Log into the <b>demo</b> account",
    "Copy the ScreenKeys build folder to C:\\Wilder\\Demo\\",
    "Run wilder_screen_keys.exe — confirm it appears in the tray",
    "Open Chrome/Edge — navigate to <b>wildercode.com</b>",
    "Set browser to <b>125% zoom</b> (Ctrl + scroll)",
    "Go <b>full screen</b> (F11)",
    "Press <b>Win + G</b> to open Xbox Game Bar — test the record button",
    "Clean desktop — hide taskbar, close all other windows",
]
for item in items:
    story.append(Paragraph(f"&#9633;  {item}", body))

story.append(Spacer(1, 0.15*inch))

# Shot list
story.append(Paragraph("Shot List", subhead))

shots = [
    ["Time", "Shot", "Notes"],
    ["0:00–0:04", "Black screen\nWilder W logo fades in, holds", "Logo sting — added in editing"],
    ["0:04–0:06", "Fade to desktop\nGrey tray icon visible", "Show icon clearly — zoom if needed"],
    ["0:06–0:10", "Press Caps Lock\nIcon turns green", "Slow deliberate keypress"],
    ["0:10–0:18", "Cursor glides from centre\nup to nav — lands on Pricing", "Smooth, unhurried movement"],
    ["0:18–0:24", "Tap Space\nPricing page loads", "Clean single tap"],
    ["0:24–0:32", "Arrow keys scroll\ndown the page", "Let it breathe — slow scroll"],
    ["0:32–0:40", "Glide to Buy button\nTap Space — left click", "Hero moment — take your time"],
    ["0:40–0:50", "Hold Space while moving\nPrecision slow-down", "Show the contrast clearly"],
    ["0:50–0:54", "Press Caps Lock\nIcon turns grey", "Clean toggle off"],
    ["0:54–1:00", "Black screen\nWilder W fades in\nwildercode.com beneath", "Added in editing"],
]

table = Table(shots, colWidths=[0.9*inch, 2.4*inch, 3.0*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3a6e1f')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('FONTSIZE', (0, 1), (-1, -1), 9),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#f5f9f0'), colors.white]),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('PADDING', (0, 0), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
]))
story.append(table)

story.append(Spacer(1, 0.15*inch))

# After recording
story.append(Paragraph("After Recording", subhead))
after = [
    "File saves automatically to Videos\\Captures on the demo account",
    "Copy the file to a USB drive or shared folder to edit on your main account",
    "In Clipchamp: add the Wilder W logo sting at start and end (black background, fade in/out)",
    "Export at 1080p minimum",
]
for item in after:
    story.append(Paragraph(f"&#9633;  {item}", body))

story.append(Spacer(1, 0.15*inch))
story.append(Paragraph("Remember: the first take is just practice. Nobody sees it. Move the cursor, tell the story.", note))

doc.build(story)
print("PDF created: C:/Users/heywi/Desktop/wilder_screenkeys_video_guide.pdf")
