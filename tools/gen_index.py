# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_site import (SECTIONS, QUIZ_PAGES, page_html, write, chapter_filename, chapter_numbers,
                      chapter_title, chapter_label, HUB_CARD_DESC, GAME_PAGE, GAME_TITLE)


def quiz_card(page, badge, desc):
    return f'''        <div class="card-grid">
          <a href="{page}" class="card">
            <div class="icon number">{badge}</div>
            <h3>{QUIZ_PAGES[page]["title"]}</h3>
            <p>{desc}</p>
          </a>
        </div>'''


def cards(section):
    out = []
    for n, i in enumerate(chapter_numbers(section)):
        out.append(f'''          <a href="{chapter_filename(section, i)}" class="card">
            <div class="icon number">{chapter_label(section, i)}</div>
            <h3>{chapter_title(section, i)}</h3>
            <p>{HUB_CARD_DESC[section][n]}</p>
          </a>''')
    return "\n".join(out)


BODY = f"""        <section id="banner">
          <h1>เรียนรู้ Zuken E³.series</h1>
          <p class="tagline">ชุดสอน Step by Step บน E³.series ภาษาไทย</p>
          <p class="intro">
            ลงมือทำทีละบท ตั้งแต่รู้จักหน้าจอ, เขียนวงจรไฟฟ้าด้วย E³.schematic, วางอุปกรณ์ในตู้ด้วย E³.panel
            ไปจนถึงสร้าง Symbol, Component และ Model เองใน Database Editor — ทุกบทมีภาพหน้าจอจริงพร้อมเลขกำกับ
            บนโปรเจกต์ตัวอย่าง Cooling water pump ที่มากับโปรแกรม
          </p>
        </section>

        <h2>เริ่มที่นี่</h2>
{quiz_card("pre-test.html", "ก่อน", "แบบทดสอบ 20 ข้อ และความคาดหวังต่อการเรียน ประมาณ 15 นาที — ใช้เทียบคะแนนกับหลังเรียน")}

        <h2>{SECTIONS["lessons"]["label"]}</h2>
        <p>ทุกบทใช้สำเนาของโปรเจกต์ตัวอย่าง <code>Cooling water pump.e3s</code> ที่มากับโปรแกรม
        (คัดลอกมาไว้ในโฟลเดอร์ของตัวเองก่อนเปิด) — บท 02 ทำต่อจากผลของบท 01 ส่วนบท 03–04 ทำใน Database Editor บนสำเนาฐานข้อมูล</p>
        <div class="card-grid">
{cards("lessons")}
        </div>

        <h2>{SECTIONS["lab"]["label"]}</h2>
        <p>ฝึกวงจรควบคุมมอเตอร์ทีละด่าน: เล่นด่านในเกมให้ผ่านก่อน แล้วเขียนแบบวงจรเดียวกันใน E³.series 2027 —
        Lab 00 เตรียม Database ของตัวเอง แล้วต่อด้วย Lab 01–06</p>
        <div class="card-grid">
          <a href="{GAME_PAGE}" class="card">
            <div class="icon number">▶</div>
            <h3>{GAME_TITLE}</h3>
            <p>ต่อวงจรควบคุมมอเตอร์ 10 ด่าน เล่นในเบราว์เซอร์ได้ทันที หรือดาวน์โหลดไปเล่นแบบออฟไลน์บน Windows</p>
          </a>
{cards("lab")}
        </div>

        <h2>เรียนจบแล้ว</h2>
{quiz_card("post-test.html", "หลัง", "แบบทดสอบ 20 ข้อชุดเดียวกับก่อนเรียน และประเมินการเรียน (Feedback) — ผลสอบส่งให้ทางอีเมล")}"""

# game level -> lab page (None = no lab yet)
GAME_LEVELS = [
    ("ไฟดวงแรก", "ห้องเก็บอะไหล่", "เปิดสวิตช์แล้วหลอดไฟติด ปิดสวิตช์แล้วหลอดไฟดับ", 1),
    ("มอเตอร์ตัวแรก", "สายพานลำเลียง ไลน์บรรจุ", "กด START ค้าง มอเตอร์หมุนเดินหน้า ปล่อยแล้วหยุด", 2),
    ("กดครั้งเดียวค้าง", "ปั๊มน้ำหล่อเย็น", "กด START แล้วปล่อย มอเตอร์ยังหมุนค้าง กด STOP แล้วหยุด", 3),
    ("กันมอเตอร์ไหม้", "พัดลมระบายอากาศ", "START/STOP เดินค้าง OL ทริปแล้วมอเตอร์หยุด ไฟเขียวตอนทำงาน ไฟแดงตอน OL ทริป", 4),
    ("เดินทีละนิด", "เครื่องตัดแผ่นเหล็ก", "START เดินค้าง STOP หยุด JOG เดินเฉพาะตอนกดค้าง", 5),
    ("สั่งได้สองจุด", "ลิฟต์ขนของ", "START ตัวไหนก็เดินค้างได้ STOP ตัวไหนก็หยุดได้", None),
    ("เดินหน้า-ถอยหลัง", "ประตูม้วนคลังสินค้า", "FWD เดินหน้าค้าง REV ถอยหลังค้าง กดสลับขณะหมุนต้องไม่ลัดวงจร", 6),
    ("ตู้ที่มีปัญหา", "ตู้ปั๊มน้ำทิ้ง งานซ่อม", "ซ่อมจนกด START แล้วมอเตอร์เดินหน้าค้าง กด STOP แล้วหยุด", None),
    ("เดินตามลำดับ", "สายพานสองตอน", "START แล้ว M1 เดินทันที M2 เดินตามเมื่อครบ 3 วินาที STOP หยุดทั้งคู่", None),
    ("สตาร์-เดลต้า", "ปั๊มน้ำดิบขนาดใหญ่", "START ออกตัวแบบสตาร์ ครบ 3 วินาทีสลับเป็นเดลต้า STOP หยุด", None),
]


def game_body():
    rows = []
    for n, (name, place, goal, lab) in enumerate(GAME_LEVELS, 1):
        lab_html = (f'<a href="{chapter_filename("lab", lab)}">Lab {lab:02d}</a>' if lab is not None else "—")
        rows.append(f"<tr><td>{n}</td><td><strong>{name}</strong><br>{place}</td><td>{goal}</td><td>{lab_html}</td></tr>")
    rows_html = "\n".join(rows)
    return f"""        <h1>{GAME_TITLE}</h1>
        <p class="lead" style="max-width:46em;">เกมต่อวงจรควบคุมมอเตอร์ 10 ด่าน ใช้เป็นแบบทดสอบก่อนเข้า Lab:
        ลากอุปกรณ์ลงแผง ต่อสาย แล้วกดทดสอบว่าวงจรทำงานตามโจทย์หรือไม่ — แต่ละ Lab ใน E³ คือวงจรของด่านนั้น</p>

        <p>
          <a class="download-btn" href="assets/game/MotorControlLab.html" target="_blank" rel="noopener">▶ เล่นในเบราว์เซอร์</a>
          &nbsp;
          <a class="download-btn" href="assets/game/MotorControlLab.zip" download>⬇ ดาวน์โหลดสำหรับ Windows (.zip)</a>
        </p>

        <div class="tip"><strong>เล่นในเบราว์เซอร์:</strong> เปิดได้ทั้ง Chrome และ Edge บนคอมพิวเตอร์ ดาว คะแนน และวงจรที่ต่อไว้
        เก็บไว้ในเบราว์เซอร์ของเครื่องนั้น ถ้าจะเริ่มใหม่ให้กดปุ่ม "ล้างความคืบหน้า" ในหน้าแรกของเกม</div>
        <div class="note"><strong>ไฟล์สำหรับ Windows:</strong> แตกไฟล์ zip ก่อน แล้วดับเบิลคลิก <code>MotorControlLab.exe</code>
        (Windows 10/11 64 บิต ไม่ต้องติดตั้ง และไม่ต้องต่ออินเทอร์เน็ต) ครั้งแรก Windows อาจขึ้นหน้าต่าง "Windows protected your PC"
        เพราะไฟล์ไม่ได้ลงลายเซ็นดิจิทัล ให้กด More info แล้วกด Run anyway — ถ้าเครื่องไหนเปิด exe ไม่ได้ ให้เปิด
        <code>MotorControlLab.html</code> ในโฟลเดอร์เดียวกันแทน</div>

        <h2>ด่านในเกม และ Lab ที่คู่กัน</h2>
        <table>
        <tr><th>ด่าน</th><th>ชื่อด่าน / สถานที่</th><th>โจทย์</th><th>Lab ใน E³</th></tr>
{rows_html}
        </table>
        <p>ด่าน 6 และ 8–10 ยังไม่มี Lab ใน E³ — เล่นในเกมเพื่อฝึกอ่านวงจรได้เลย</p>

        <div class="page-nav">
          <a href="index.html">← กลับหน้าแรก</a>
          <a href="{chapter_filename("lab", 0)}">เริ่ม Lab 00. {chapter_title("lab", 0)} →</a>
        </div>"""


if __name__ == "__main__":
    write("index.html", page_html("หน้าแรก", BODY, active_top="index"))
    write(GAME_PAGE, page_html(GAME_TITLE, game_body(), expand_section="lab", active_top=GAME_PAGE))
