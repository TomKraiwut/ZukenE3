# -*- coding: utf-8 -*-
"""Motor Control Lab chapters (lab/00.html .. lab/06.html) from the Lab Step-by-Step decks.

    python -X utf8 deck_to_lab.py <deck.pptx> <deck.pdf> <NN>

Text comes from the .pptx (keeps Thai spacing), pictures from the PDF export of the same deck: the crop of every
picture slide is the union of its pictures, callout circles, leader lines and labels lying on the pictures, taken from
the shape geometry in the .pptx. Writes assets/images/lab/NN-kk.jpg and tools/chapters/lab_NN.py (overwritten --
objectives, lead text and game level come from LAB_META below, so edit those here, not in the generated file).

Slide types: 1 = cover (skipped) · "ภาพรวม..." = overview cards -> table · slide with a picture = screenshot + numbered
legend + note boxes · "Thank you" = skipped · anything else = table (problems / precautions)."""
import io
import os
import re
import sys

import pymupdf
from PIL import Image, ImageDraw
from pptx.util import Emu

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from pptx_to_chapter import (Presentation, shapes_of, body_boxes, title_kicker, plain, rich, esc, label_split,
                             note_html, grid_slide, cm)

SCALE = 2.6
MAX_W = 1600
PAD_CM = 0.25
FRAME_TOP = 3.4 / 2.54 * 72      # below the title
FRAME_BOTTOM = 17.4 / 2.54 * 72  # above the footer line

# game level (MotorControlLab.html) per lab, objectives and the lead paragraph of each page
LAB_META = {
    0: dict(level=None,
            lead="ก่อนเริ่ม Lab แรก ให้ E³ ใช้ Database ของผู้เรียนเองที่อยู่ในเครื่อง (ไม่ใช่ไฟล์บน Google Drive หรือ "
                 "ไดรฟ์ที่แชร์) และรู้วิธี Backup Database กับโปรเจกต์ .e3s ไว้ก่อนลงมือ",
            objectives=["Copy Database ของคอร์สไปไว้ในโฟลเดอร์งานของตัวเอง",
                        "เพิ่ม Database ด้วย Configure Databases (Data Link → Access Database Engine 16.0) แล้วเลือกใช้",
                        "Backup Database และใช้ Compact and Repair ใน Microsoft Access",
                        "Backup โปรเจกต์ .e3s ก่อนแก้งานใหญ่"]),
    1: dict(level=1,
            lead="Lab แรกบน E³.schematic: จากโปรเจกต์เปล่าไปถึงวงจรสวิตช์กับหลอดไฟหนึ่งดวง "
                 "ได้ฝึกวาง Component, Signal reference, Connection, ใส่สายและป้ายสาย",
            objectives=["สร้างโปรเจกต์ใหม่ ตั้ง Sheet A4 และ Title block",
                        "วาง Component, Signal reference และต่อ Connection",
                        "ตั้งชื่อ Signal (L1 / N) ใส่สาย H07V-K 1.5 mm² และให้ป้ายสายแสดงขนาดกับสี",
                        "ใช้ Device window ดู Placement, Jump และ Highlight"]),
    2: dict(level=2,
            lead="วงจรกำลัง 3 เฟส (Sheet 1) กับวงจรควบคุม (Sheet 2) ของมอเตอร์ตัวแรก: กด START ค้างมอเตอร์หมุน ปล่อยแล้วหยุด",
            objectives=["แยกวงจรกำลังและวงจรควบคุมเป็น 2 Sheet ขนาด A3",
                        "ใช้ Signal reference, Autoconnect และ Multi-Connection ต่อ L1 L2 L3 N",
                        "วาง Contactor -K1, Motor -M1, Push Button -S1 และ Coil ของ -K1",
                        "ซ่อน/แสดงเส้นนำสีเทาด้วย View → Levels และไฟล์ .vis"]),
    3: dict(level=3,
            lead="ต่อจาก Lab 02: เพิ่ม Terminal, ปุ่ม STOP และหน้าสัมผัสจับค้าง (Self-holding) "
                 "ให้กด START ครั้งเดียวแล้วมอเตอร์หมุนค้างจนกด STOP",
            objectives=["วาง Terminal บนจุดต่อ bus และซ่อนข้อความ Terminal ด้วย Symbol Properties",
                        "ใส่สายวงจรกำลัง 1.5-BK และสายวงจรควบคุม 1.5-RD / N 1.5-BU ตาม IEC 60204-1",
                        "วาง Push Button NC และหน้าสัมผัส NO 13-14 ของ -K1 เป็นวงจรจับค้าง",
                        "ใช้ Angle connection ที่จุดต่อเส้นกิ่ง"]),
    4: dict(level=4,
            lead="ต่อจาก Lab 03: เพิ่ม Overload relay -F1 กันมอเตอร์ไหม้ พร้อมไฟเขียว RUN และไฟแดง TRIP",
            objectives=["แทรก Overload relay บนสายกำลัง 3 เส้นแล้วใส่สายใหม่",
                        "แทรกหน้าสัมผัส NC 95-96 ก่อน STOP และใช้ NO 97-98 สั่งไฟ TRIP",
                        "เปลี่ยนเลขสาย (F2 / Wire Properties) ให้เรียงตามแบบ",
                        "ตรวจแบบแล้วทดสอบตามโจทย์"]),
    5: dict(level=5,
            lead="ต่อจาก Lab 03: เพิ่มปุ่ม JOG ให้มอเตอร์เดินทีละนิดเฉพาะตอนกดค้าง ขณะที่ START ยังเดินค้างได้ตามเดิม",
            objectives=["วาง Push Button NO NC เป็นอุปกรณ์ตัวเดียว (-S3 JOG) แล้ววาง NC 3-4 จาก Device tree",
                        "ต่อ Connection และ Angle connection ของวงจร JOG",
                        "เปลี่ยนเลขสายเป็น 2 หลัก และซ่อนป้ายสายที่ซ้อนกัน"]),
    6: dict(level=7,
            lead="ต่อจาก Lab 03: เพิ่ม -K2 กลับทางหมุนมอเตอร์ (สลับเฟส) และ Interlock กันคอนแทคเตอร์ทั้งสองตัวดึงพร้อมกัน",
            objectives=["วาง -K2 และต่อวงจรกำลังแบบสลับเฟส",
                        "ใช้ NC 21-22 ของคอนแทคเตอร์อีกตัวเป็น Interlock ในวงจรควบคุม",
                        "ต่อ Connection และ Angle connection ฝั่ง REV แล้วตรวจแบบ"]),
}


def emu_pt(v):
    return (v or 0) / 12700.0


def rect_of(sh):
    return pymupdf.Rect(emu_pt(sh.left), emu_pt(sh.top), emu_pt(sh.left + sh.width), emu_pt(sh.top + sh.height))


def is_oval(sh):
    return "Oval" in sh.name and re.fullmatch(r"\d{1,2}", plain(sh) if sh.has_text_frame else "") is not None


def legend_pairs(slide):
    """{n: text box} for callout circles that have their legend text right next to them."""
    boxes = [sh for sh in shapes_of(slide) if sh.has_text_frame and sh.text_frame.text.strip()]
    ovals = [sh for sh in boxes if is_oval(sh)]
    texts = [sh for sh in boxes if not is_oval(sh) and not sh.name.startswith(("Title", "Text Placeholder",
                                                                               "Footer", "Slide Number"))]
    out = {}
    for ov in ovals:
        for sh in texts:
            if abs(cm(sh.top) - cm(ov.top)) <= 0.35 and 0.3 <= cm(sh.left) - cm(ov.left) <= 1.6:
                out[ov.shape_id] = (int(plain(ov)), sh)
                break
    return out


def picture_slide(slide, page, nn, seq, title):
    allsh = shapes_of(slide)
    pics = [sh for sh in allsh if sh.shape_type == 13]
    legend = legend_pairs(slide)
    legend_text_ids = {t.shape_id for _, t in legend.values()}
    pic_union = rect_of(pics[0])
    for p in pics[1:]:
        pic_union |= rect_of(p)
    crop = pymupdf.Rect(pic_union)
    notes, blank = [], []                               # blank = slide parts outside the picture, painted white
    for sh in allsh:
        if sh.name.startswith(("Title", "Text Placeholder", "Footer", "Slide Number")) or sh.shape_type == 13:
            continue
        r = rect_of(sh)
        if sh.shape_id in legend or sh.shape_id in legend_text_ids:
            blank.append(r)
        elif sh.shape_type == 1 and not (sh.has_text_frame and sh.text_frame.text.strip())                 and not pic_union.contains(pymupdf.Point((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2)):
            blank.append(r)                             # grey box behind a note
        if is_oval(sh) and sh.shape_id not in legend:
            crop |= r                                   # callout on the picture
        elif sh.shape_type == 9:                        # leader line
            if r.intersects(pic_union) or pic_union.contains(r.tl):
                crop |= r
        elif sh.has_text_frame and sh.text_frame.text.strip() and sh.shape_id not in legend_text_ids and not is_oval(sh):
            c = pymupdf.Point((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2)
            if pic_union.contains(c):
                crop |= r                               # label printed on the picture ("ก่อน" / "หลัง")
            else:
                ls = label_split(sh)
                notes.append((cm(sh.top), cm(sh.left), ls if ls else None, sh))
                blank.append(r)
    pad = PAD_CM / 2.54 * 72
    crop = pymupdf.Rect(crop.x0 - pad, max(crop.y0 - pad, FRAME_TOP), crop.x1 + pad, min(crop.y1 + pad, FRAME_BOTTOM))
    crop &= page.rect
    rel = f"assets/images/lab/{nn:02d}-{seq:02d}.jpg"
    pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), clip=crop)
    im = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
    dr = ImageDraw.Draw(im)
    for b in blank:
        on_pic = (pymupdf.Rect(b) & pic_union).get_area() if b.intersects(pic_union) else 0
        if on_pic > 0.1 * b.get_area():                 # never paint over the screenshot itself
            continue
        b = pymupdf.Rect(b.x0 - 2, b.y0 - 2, b.x1 + 2, b.y1 + 2) & crop
        if not b.is_empty:
            dr.rectangle([(b.x0 - crop.x0) * SCALE, (b.y0 - crop.y0) * SCALE,
                          (b.x1 - crop.x0) * SCALE, (b.y1 - crop.y0) * SCALE], fill="white")
    if im.width > MAX_W:
        im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
    path = os.path.join(ROOT, *rel.split("/"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path, "JPEG", quality=84, optimize=True)

    alt = esc(title)
    items = [rich(t) for _, (n, t) in sorted(legend.items(), key=lambda kv: kv[1][0])]
    shot = f'screenshot("{rel}", "{alt}")'
    out = [f"<h2>{alt}</h2>"]
    if items:
        lst = ",\n".join(f"        '{t}'" for t in items)
        out += ["{side_by_side(", f"    {shot},", "    step_list([", lst + ",", "    ])", ")}"]
    else:
        out.append("{" + shot + "}")
    for _, _, ls, sh in sorted(notes, key=lambda n: (n[0], n[1])):
        if ls and ls[0].strip().startswith("โจทย์จากเกม"):
            out.append(f'<div class="tip"><strong>{ls[0].strip()}:</strong> {ls[1]} '
                       f'<a href="game.html">เล่นด่านนี้ในเกม →</a></div>')
        elif ls:
            out.append(note_html(*ls))
        else:
            out.append(f'<div class="tip">{rich(sh)}</div>')
    return "\n".join(out)


def overview(slide, title):
    boxes = body_boxes(slide)
    used, cards = set(), []
    for sh in boxes:
        if re.fullmatch(r"\d{2}", plain(sh)):
            x, y = cm(sh.left), cm(sh.top)
            near = sorted([b for b in boxes if 1.0 <= cm(b.left) - x <= 2.0 and -0.3 <= cm(b.top) - y <= 1.6],
                          key=lambda b: cm(b.top))
            if len(near) >= 2:
                cards.append((plain(sh), rich(near[0]), rich(near[1])))
                used |= {id(sh), id(near[0]), id(near[1])}
    cards.sort()
    need, extra = [], []
    for sh in boxes:
        if plain(sh) == "สิ่งที่ต้องมี":
            used.add(id(sh))
            for b in boxes:
                if abs(cm(b.left) - cm(sh.left)) < 0.3 and 0.3 < cm(b.top) - cm(sh.top) < 2.5:
                    need = [esc(p.text) for p in b.text_frame.paragraphs if p.text.strip()]
                    used.add(id(b))
    rest = sorted([b for b in boxes if id(b) not in used], key=lambda b: (cm(b.top), cm(b.left)))
    for b in rest:
        ls = label_split(b)
        extra.append(note_html(*ls) if ls else None)
    stats = [rich(b) for b, e in zip(rest, extra) if e is None]
    out = [f"<h2>{esc(title)}</h2>", "<table>", "<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>"]
    out += [f"<tr><td>{n}</td><td>{a}</td><td>{b}</td></tr>" for n, a, b in cards]
    out.append("</table>")
    if need:
        out.append(f'<div class="tip"><strong>สิ่งที่ต้องมี:</strong> {" · ".join(need)}</div>')
    if stats:
        out.append(f'<p>{" ".join(stats)}</p>')
    out += [e for e in extra if e]
    return "\n".join(out)


def main():
    deck, pdf, nn = sys.argv[1], sys.argv[2], int(sys.argv[3])
    prs, doc = Presentation(deck), pymupdf.open(pdf)
    meta = LAB_META[nn]
    parts, seq, cover = [], 0, ""
    for pno, slide in enumerate(prs.slides, 1):
        title, _ = title_kicker(slide)
        if pno == 1:
            cover = title
            continue
        if title.lower().startswith("thank you"):
            continue
        parts.append(f"<!-- slide {pno} -->")
        if title.startswith("ภาพรวม"):
            parts.append(overview(slide, title))
        elif any(sh.shape_type == 13 for sh in shapes_of(slide)):
            seq += 1
            parts.append(picture_slide(slide, doc[pno - 1], nn, seq, title))
        else:
            parts.append(grid_slide(slide, title))
        parts.append("")
    lead = f'<p class="lead" style="max-width:46em;">{meta["lead"]}</p>'
    if meta["level"]:
        lead += (f'\n<div class="note"><strong>ด่านในเกม:</strong> Lab นี้ตรงกับด่าน {meta["level"]} ของเกม Motor Control Lab '
                 f'— ลองต่อวงจรในเกมก่อน แล้วค่อยเขียนแบบเดียวกันใน E³ <a href="game.html">ไปหน้าเกม →</a></div>')
    objs = ",\n".join(f'    "{o}"' for o in meta["objectives"])
    src = (f'# -*- coding: utf-8 -*-\n"""GENERATED by deck_to_lab.py from {os.path.basename(deck)} ({esc(cover)}) -- '
           f'do not edit by hand: change the deck or LAB_META and run it again."""\n'
           "from gen_site import screenshot, step_list, side_by_side\n\n"
           f"OBJECTIVES = [\n{objs},\n]\n\nBODY = f'''\n{lead}\n\n" + "\n".join(parts) + "'''\n")
    out = os.path.join(HERE, "chapters", f"lab_{nn:02d}.py")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(src)
    print(f"wrote {out} - {seq} pictures")


if __name__ == "__main__":
    main()
