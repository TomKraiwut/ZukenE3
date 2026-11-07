# -*- coding: utf-8 -*-
"""Lesson 01: วงจรไฟฟ้า E3.schematic -- from 02_Quicktour/01_Schematic/E3_01_Schematic_StepByStep.pptx
(drafted by pptx_to_chapter.py, finished by hand)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "เพิ่ม Sheet ใหม่พร้อม =A1 / +S1.MP และ Format แล้วใส่หัวกระดาษจาก Translation Table",
    "เปิด Device Properties ของมอเตอร์ และเปลี่ยน Component จาก list ที่ใช้กับ Symbol นั้นได้",
    "Copy / Paste วงจรปั๊ม แล้วอ่าน Messages ว่าระบบตั้งชื่ออุปกรณ์ใหม่ให้อย่างไร",
    "ค้นหาด้วย Search (F3) และ Jump ไปยังมุมมองอื่นของอุปกรณ์",
    "อธิบายว่า Terminal Plan อัปเดตตามวงจร และส่งออกแบบเป็น PDF",
]

BODY = f'''
<p class="lead" style="max-width:46em;">เขียนวงจรไฟฟ้าด้วย <strong>E³.schematic</strong> บนข้อมูลชุดเดียว — ทีละขั้น รวม 11 ขั้น
เพิ่ม Sheet ผูก Component คัดลอกวงจรปั๊มตัวที่ 2 เป็นปั๊มตัวที่ 3 ค้นหา ดู Terminal Plan แล้วส่งออก PDF ใช้เวลาประมาณ 1.5 ชั่วโมง</p>

<h2>ภาพรวม: เขียนวงจรด้วยข้อมูลชุดเดียว</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>เพิ่ม Sheet</td><td>New Sheet · หัวกระดาษจาก Translation Table</td></tr>
<tr><td>02</td><td>ผูก Component</td><td>Device Properties เลือก Component ที่ใช้ได้</td></tr>
<tr><td>03</td><td>คัดลอกวงจร</td><td>Copy / Paste ชื่ออุปกรณ์ไม่ซ้ำเอง</td></tr>
<tr><td>04</td><td>ค้นหาและกระโดด</td><td>F3 Search · Jump ไป tree / Variant</td></tr>
<tr><td>05</td><td>Terminal Plan</td><td>แผนขั้วต่ออัปเดตตามวงจร</td></tr>
<tr><td>06</td><td>ส่งออก PDF</td><td>File → Export → PDF</td></tr>
</table>
<div class="tip"><strong>สิ่งที่ต้องมี:</strong> ผ่านบทที่ 00 หน้าจอและพื้นฐาน · สำเนา <code>Cooling water pump.e3s</code> ของตัวเอง · license E³.schematic (Export PDF ต้องมี license)</div>
<div class="note"><strong>ไฟล์ฝึก:</strong> คัดลอก <code>Cooling water pump.e3s</code> จาก <code>C:\\Users\\Public\\Documents\\Zuken\\E3.series_&lt;เวอร์ชัน&gt;\\data\\Pumpe</code> มาไว้ในโฟลเดอร์ของตัวเองก่อนเปิด (เช่น <code>Cooling water pump_01.e3s</code>)</div>

<h2>ขั้นที่ 1: เพิ่ม Sheet ใหม่</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-01.jpg", "ขั้นที่ 1: เพิ่ม Sheet ใหม่"),
    step_list([
        'คลิกขวาที่ <strong>Sheet 8</strong> ใน Project Window',
        'เลือก <strong>New Sheet...</strong>',
        '<strong>Name</strong> = 7',
        '<strong>=A1</strong> และ <strong>+S1.MP</strong>',
        '<strong>Format</strong> = DINA3_Electric',
        '<strong>Insert before</strong> แล้วกด OK',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> =A1 คือ Higher level assignment (ระบบ) · +S1.MP คือ Location (ตำแหน่งติดตั้ง) ใช้กับอุปกรณ์ทุกตัวบนแผ่นนี้</div>

<h2>ขั้นที่ 2: หัวกระดาษจาก Translation Table</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-02.jpg", "ขั้นที่ 2: หัวกระดาษจาก Translation Table"),
    step_list([
        'คลิกขวา Sheet 7 → <strong>Sheet Properties</strong> คลิกช่อง Entry ของ Name (1) แล้วกด <strong>...</strong>',
        'พิมพ์คำค้นในแถวกรอง เช่น <strong>power supply*</strong>',
        'เลือก <strong>Power supply</strong> แล้วกด OK',
        'ทำซ้ำกับ Name (2) = <strong>main switch</strong>',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> ข้อความจาก Translation Table แปลภาษาได้อัตโนมัติ (สูงสุด 5 ภาษา) · * ใช้แทนตัวอักษรใดก็ได้</div>

<h2>ขั้นที่ 3: ตรวจ Sheet ใหม่และหัวกระดาษ</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-03.jpg", "ขั้นที่ 3: ตรวจ Sheet ใหม่และหัวกระดาษ"),
    step_list([
        '<strong>7 =A1 +S1.MP</strong> อยู่ในโฟลเดอร์ 03-circuit diagram',
        'หัวกระดาษแสดง <strong>Power supply / main switch</strong>',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> แก้ Sheet Properties ภายหลังได้เสมอ หัวกระดาษเปลี่ยนตามทันที</div>

<h2>ขั้นที่ 4: Device Properties ของมอเตอร์</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-04.jpg", "ขั้นที่ 4: Device Properties ของมอเตอร์"),
    step_list([
        'คลิกขวาที่มอเตอร์ <strong>-M2</strong> บน Sheet 9',
        'เลือก <strong>Device Properties...</strong>',
        '<strong>Device designation</strong> -M2 =A1 +Tank1',
        '<strong>Component</strong> = K21R-160-L8',
        '<strong>Function</strong> = pump 2 (ติ๊กให้แสดงบนแบบ)',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> Device = Component ที่อยู่ในโปรเจกต์แล้ว · แก้ชื่อที่นี่ ทุก Sheet และแบบตู้เปลี่ยนตาม</div>

<h2>ขั้นที่ 5: เปลี่ยน Component (แสดงเฉพาะตัวที่ใช้ได้)</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-05.jpg", "ขั้นที่ 5: เปลี่ยน Component (แสดงเฉพาะตัวที่ใช้ได้)"),
    step_list([
        'กดลูกศรของช่อง <strong>Component</strong>',
        'list แสดงเฉพาะ Component ที่ใช้กับ Symbol นี้ได้ เช่น K21R-132-M4, K21R-160-M6',
        'เลือกแล้วกด <strong>OK</strong> (ในบทเรียนนี้กด Cancel)',
    ])
)}
<div class="tip"><strong>ข้อดีของการทำงานแบบอิง Component:</strong> ระบบตรวจเลขขาตั้งแต่ต้น ใช้หน้าสัมผัสเกินจำนวนที่อุปกรณ์มีจริงไม่ได้</div>

<h2>ขั้นที่ 6: เลือกวงจรปั๊ม 2 แล้ว Copy</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-06.jpg", "ขั้นที่ 6: เลือกวงจรปั๊ม 2 แล้ว Copy"),
    step_list([
        'ลากกรอบจากมุมบนซ้ายของวงจรปั๊มตัวที่ 2',
        'ปล่อยที่มุมล่างขวา ชิ้นที่เลือกเป็นสีไฮไลต์',
        'คลิกขวาที่ชิ้นที่เลือก → <strong>Copy</strong> (Ctrl+C)',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> ลากกรอบจากพื้นที่ว่าง ถ้าเริ่มบน Symbol จะกลายเป็นการย้าย Symbol</div>

<h2>ขั้นที่ 7: Paste แล้วระบบตั้งชื่อใหม่ให้เอง</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-07.jpg", "ขั้นที่ 7: Paste แล้วระบบตั้งชื่อใหม่ให้เอง"),
    step_list([
        '<strong>Edit → Paste</strong> แล้วคลิกวางในที่ว่างของแผ่น',
        'Messages แจ้งชื่อที่เปลี่ยน เช่น <strong>-M2 → -M3</strong>, -Q4 → -Q6, -W2 → -W5',
        'ได้วงจรปั๊มตัวที่ 3 ที่ชื่อไม่ซ้ำ',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> E³ ไม่ยอมให้ชื่ออุปกรณ์ซ้ำในโปรเจกต์ · อุปกรณ์ใหม่ (-Q6, -Q7) จะรอวางในแบบตู้ (บทที่ 02)</div>

<h2>ขั้นที่ 8: ค้นหาด้วย Search (F3)</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-08.jpg", "ขั้นที่ 8: ค้นหาด้วย Search (F3)"),
    step_list([
        '<strong>Edit → Search (F3)</strong> Type = <strong>Signal</strong>',
        '<strong>Value</strong> = L1',
        'กด <strong>OK</strong>',
        'ผลอยู่ในแท็บ <strong>Results</strong> คลิก [Jump] เพื่อไปยังจุดนั้น',
    ])
)}
<div class="tip"><strong>ทำซ้ำ:</strong> Shift+F3 หรือ Edit → Reset Highlight ล้างสีไฮไลต์หลังค้นหา</div>

<h2>ขั้นที่ 9: Jump ไปยังมุมมองอื่นของอุปกรณ์</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-09.jpg", "ขั้นที่ 9: Jump ไปยังมุมมองอื่นของอุปกรณ์"),
    step_list([
        'คลิกขวาที่อุปกรณ์ → <strong>Jump</strong>',
        'เลือกปลายทาง เช่น Device Tree, Device Table หรือ <strong>Variant/Option Tree</strong>',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> มอเตอร์ -M2 เป็นของ Option 'Additional pump 1' ปิด Option นี้แล้วอุปกรณ์ทั้งชุดจะซ่อนทั้งวงจรและตู้</div>

<h2>ขั้นที่ 10: Terminal Plan อัปเดตตามวงจร</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-10.jpg", "ขั้นที่ 10: Terminal Plan อัปเดตตามวงจร"),
    step_list([
        'Sheet 32 ในโฟลเดอร์ 04-Terminal Plan คือแผนขั้วต่อ <strong>-XT2</strong>',
        'ทุกแถวคือขั้วจริง ปลายสายสองฝั่งมาจากวงจร',
        'สร้างแผนใหม่: <strong>Insert → Terminal Plan...</strong>',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> แก้เลขขั้วในวงจร แผนเปลี่ยนตาม · ลากเรียงขั้วในแผน วงจรเปลี่ยนตาม</div>

<h2>ขั้นที่ 11: ส่งออก PDF</h2>
{side_by_side(
    screenshot("assets/images/lessons/01-11.jpg", "ขั้นที่ 11: ส่งออก PDF"),
    step_list([
        '<strong>File</strong>',
        '<strong>Export</strong>',
        '<strong>PDF...</strong>',
        'Export Range: <strong>All</strong> / Current sheet / Sheets',
        'ตั้งชื่อไฟล์แล้วกด <strong>Save</strong>',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> ต้องมี license Export PDF · Cross-reference ใน PDF คลิกได้</div>

<h2>ไฟล์ที่ใช้ในบทนี้</h2>
<table>
<tr><th>ไฟล์</th><th>มาจากไหน</th><th>ใช้ทำอะไร</th></tr>
<tr><td><code>Cooling water pump_01.e3s</code></td><td>สำเนาใหม่ของโปรเจกต์ตัวอย่าง <code>data\\Pumpe\\Cooling water pump.e3s</code></td><td>ฝึกขั้นที่ 1–11</td></tr>
<tr><td>ไฟล์เดียวกันหลังจบบท</td><td>มี Sheet 7 และวงจรปั๊มตัวที่ 3 (-M3, -Q6, -Q7 …)</td><td>ใช้ต่อในบทที่ 02 (วาง -Q6 / -Q7 ลงตู้)</td></tr>
<tr><td>ไฟล์ PDF</td><td>ขั้นที่ 11 File → Export → PDF</td><td>แบบสำหรับส่งต่อ Cross-reference คลิกได้</td></tr>
</table>

<h2>Checklist ท้ายบท</h2>
<table>
<tr><th>ข้อ</th><th>สิ่งที่ต้องทำได้</th></tr>
<tr><td>1</td><td>เพิ่ม Sheet พร้อม =HLA / +Location และ Format ได้</td></tr>
<tr><td>2</td><td>ใส่หัวกระดาษจาก Translation Table ได้</td></tr>
<tr><td>3</td><td>เปิด Device Properties และเปลี่ยน Component ได้</td></tr>
<tr><td>4</td><td>Copy / Paste วงจร และอ่าน Messages การเปลี่ยนชื่อได้</td></tr>
<tr><td>5</td><td>ค้นหาด้วย F3 และ Jump ไปยังผลลัพธ์ได้</td></tr>
<tr><td>6</td><td>อธิบายว่า Terminal Plan อัปเดตตามวงจรได้</td></tr>
<tr><td>7</td><td>ส่งออก PDF ได้</td></tr>
</table>
<div class="tip"><strong>ครบทุกข้อ:</strong> ไปต่อบทที่ 02: วางอุปกรณ์ในตู้ด้วย E³.panel</div>

<h2>ปัญหาที่พบบ่อย และวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>Sheet ใหม่ไปอยู่ผิดโฟลเดอร์</td><td>Sheet Properties → Document Type ต้องเป็น 03-circuit diagram</td></tr>
<tr><td>ข้อความหัวกระดาษยาวเกิน 30 ตัวอักษร</td><td>ใช้ข้อความจาก Translation Table แทนการพิมพ์ยาว ๆ</td></tr>
<tr><td>Format ของแผ่นเปลี่ยนเป็นข้อความแปลก ๆ</td><td>เลือก Format ใหม่จาก list (DINA3_Electric) ก่อนกด OK</td></tr>
<tr><td>Paste แล้วได้ข้อความแทนวงจร</td><td>Clipboard มีข้อความจากโปรแกรมอื่น ใช้คลิกขวา → Copy ใน E³ ใหม่ แล้ว Edit → Paste</td></tr>
<tr><td>Component ที่ต้องการไม่อยู่ใน list</td><td>list แสดงเฉพาะตัวที่ใช้กับ Symbol นั้นได้ ต้องสร้าง Component ใหม่ (บทที่ 03)</td></tr>
<tr><td>ไฮไลต์จากการค้นหาไม่หาย</td><td>Shift+F3 หรือ Edit → Reset Highlight</td></tr>
</table>
'''
