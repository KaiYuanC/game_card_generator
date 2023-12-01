from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import math

FILENAME = "/Users/kaiyuanchi/Dev/card_strings.py"

def format_front(front):
    x, y, z = int(front[1]), int(front[3]), int(front[5])
    return f'======= {x} | {y} | {z} ======='


def parse_cards(filename):
    with open(filename, "r") as f:
        cards = set(f.readlines())
    cards = [line.strip() for line in cards]
    cards_tuples = [(format_front(line[:7]), line) for line in cards]
    return cards_tuples

def chunks(lst, n):
    # Yield successive n-sized chunks from lst.
    for i in range(0, len(lst), n):
        yield lst[i : i + n]

def format_data(cards):
    data = []
    chunked_cards = list(chunks(cards, 16))
    for chunk in chunked_cards:
        front = [item[0] for item in chunk]
        back = [item[1] for item in chunk]

        front_rows = list(chunks(front, 4))
        back_rows = list(chunks(back, 4))
        # reversed rows so the front and back match when printing double sided
        back_rows = [reversed(row) for row in back_rows]
        data.extend(front_rows)
        data.extend(back_rows)
    return data


def generate_card_pdf(cards):
    doc = SimpleDocTemplate(
        "cards.pdf",
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=18,
        bottomMargin=18,
    )
    elements = []

    data = format_data(cards)

    backgroun_color = customColor = colors.Color(red=(173.0/255),green=(216.0/255),blue=(230.0/255))
    style = TableStyle(
        [
            ("GRID", (0, 0), (-1, -1), 4, colors.black),
            ('FONTSIZE', (0,0), (-1,-1), 20),
            ('ALIGNMENT',(0,0),(-1,-1),'CENTER'),
            ('TEXTCOLOR',(0,0),(-1,-1),colors.blue),
            ('BACKGROUND',(0,0),(-1,-1),backgroun_color),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]
    )

    # Configure style and word wrap
    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = "CJK"
    data2 = [[Paragraph(cell, s) for cell in row] for row in data]
    t = Table(
        data2,
        colWidths=[140, 140, 140, 140],
        rowHeights=[180 for _ in range(math.ceil(len(cards)/4) * 2)],
    )
    t.setStyle(style)

    elements.append(t)
    doc.build(elements)

def main() -> None:
    cards = parse_cards(FILENAME)
    print(len(cards))
    generate_card_pdf(cards)


if __name__ == "__main__":
    main()
