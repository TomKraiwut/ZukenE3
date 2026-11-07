# -*- coding: utf-8 -*-
"""Lesson 03: สร้าง Symbol และ Component -- from 02_Quicktour/03_Symbol_Component/E3_03_Symbol_Component_StepByStep.pptx
(drafted by pptx_to_chapter.py, finished by hand)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "เปิด Database Editor (E³.dbe) จากโปรเจกต์ และหา tree ของ Symbol / Component",
    "สร้าง Symbol คอยล์ใหม่ วาดกราฟิก วาง Node แล้วตั้ง Name / Type / Class",
    "สร้าง Component ใหม่ด้วย Component Wizard โดยตั้งต้นจากตัวที่มีอยู่ (Make new copy)",
    "ดู Component Properties และ Pin Assignment ที่ผูกเลขขากับ Symbol",
    "บอกได้ว่าเมื่อไรควร Save To Database และต้องสำรองฐานข้อมูลก่อน",
]

BODY = f'''
<p class="lead" style="max-width:46em;">Symbol + เลขขา + ข้อมูล = Component — ทีละขั้น รวม 9 ขั้น ใน <strong>Database Editor</strong>
สร้าง Symbol คอยล์ G01Y001B แล้วสร้าง Component GHR15511201R003 โดยตั้งต้นจาก 3RT10151AB01 ใช้เวลาประมาณ 1.5 ชั่วโมง</p>

<h2>ภาพรวม: Symbol + เลขขา + ข้อมูล = Component</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>เปิด Database Editor</td><td>Tools → Start Database Editor</td></tr>
<tr><td>02</td><td>New Symbol</td><td>วาดกราฟิก วางขา (Node)</td></tr>
<tr><td>03</td><td>Symbol Properties</td><td>ชื่อ Type Class</td></tr>
<tr><td>04</td><td>Component Wizard</td><td>ตั้งต้นจาก Component เดิม</td></tr>
<tr><td>05</td><td>แก้ Component</td><td>Pins · Pin Assignment</td></tr>
<tr><td>06</td><td>Save To Database</td><td>บันทึกเมื่อพร้อมเท่านั้น</td></tr>
</table>
<div class="tip"><strong>สิ่งที่ต้องมี:</strong> ผ่านบทที่ 00–01 · license Database Editor · ฐานข้อมูลสำหรับฝึก (สำรองไฟล์ .mdb ก่อนเสมอ)</div>
<div class="note"><strong>ระวัง:</strong> Save To Database เขียนลงฐานข้อมูลที่ใช้งานอยู่ทันที ทุกคนที่ใช้ฐานข้อมูลเดียวกันเห็นการแก้ไข ฝึกบนสำเนาฐานข้อมูลเท่านั้น</div>

<h2>ขั้นที่ 1: เปิด Database Editor</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-01.jpg", "ขั้นที่ 1: เปิด Database Editor"),
    step_list([
        'ในหน้าต่างโปรเจกต์ เมนู <strong>Tools</strong>',
        '<strong>Start Database Editor</strong>',
        'E³.dbe เปิดเป็นหน้าต่างใหม่ <strong>In use...</strong>',
        'แท็บ <strong>Comp / Symbol / Misc / Model</strong>',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> E³.dbe เป็นอีกโปรแกรมหนึ่ง ปิดแล้วกลับไปที่หน้าต่างโปรเจกต์ได้เลย · ขยายหน้าต่างให้เต็มจอเพื่อให้เห็น tree</div>

<h2>ขั้นที่ 2: สร้าง Symbol ใหม่</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-02.jpg", "ขั้นที่ 2: สร้าง Symbol ใหม่"),
    step_list([
        'แท็บ Symbol คลิกขวาที่โฟลเดอร์ใน tree',
        '<strong>New Symbol</strong>',
        'แผ่นวาด Symbol เปิดขึ้น <strong>วงกลมกากบาท</strong> คือจุด Origin',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> เมนูเดียวกันมี New Component และ New Model (บทที่ 04)</div>

<h2>ขั้นที่ 3: วาดกราฟิกและวางขา (Node)</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-03.jpg", "ขั้นที่ 3: วาดกราฟิกและวางขา (Node)"),
    step_list([
        'เลือกชนิด Node จาก list',
        '<strong>from top / from bottom</strong> = ทิศที่สายเข้า',
        'วาดสี่เหลี่ยมคอยล์ด้วยเครื่องมือ Graphic บน grid',
        'คลิกวาง Node ที่ขอบบน และขอบล่าง',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> ลำดับการวางขาสำคัญ ใช้จับคู่กับเลขขาของ Component · เปิด Grid ก่อนวาด</div>

<h2>ขั้นที่ 4: Symbol Properties</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-04.jpg", "ขั้นที่ 4: Symbol Properties"),
    step_list([
        'คลิกขวาที่ Symbol ใหม่ใน tree',
        '<strong>Properties...</strong>',
        '<strong>Name</strong> = G01Y001B (ตั้งตาม IEC 617)',
        '<strong>Type</strong> Normal',
        '<strong>Class</strong> = Coil',
    ])
)}
<div class="tip"><strong>ทำซ้ำ:</strong> ตั้ง Origin และพื้นที่ของ Symbol ก่อน Save To Database · ฝั่งโปรเจกต์กด F5 ที่ Database เพื่อเห็น Symbol ใหม่</div>

<h2>ขั้นที่ 5: New Component จากตัวที่มีอยู่</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-05.jpg", "ขั้นที่ 5: New Component จากตัวที่มีอยู่"),
    step_list([
        'ค้นหา <strong>3RT10151AB01</strong> แล้วคลิกขวา',
        '<strong>New Component</strong>',
        '<strong>Name</strong> = GHR15511201R003',
        'ใช้ Attribute และโครงสร้างของ 3RT10151AB01',
        '<strong>Standard device</strong>',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> Component Wizard มี 4 หน้า: Identification → Properties → Structure → Complete</div>

<h2>ขั้นที่ 6: Properties และ Structure</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-06.jpg", "ขั้นที่ 6: Properties และ Structure"),
    step_list([
        'แก้ Attribute เช่น Article number, Description, Supplier',
        'ติ๊ก <strong>Make new copy</strong>',
        'Preview แสดง Symbol / Model ในโครงสร้างเดิม',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> Make new copy ทำให้แก้โครงสร้างได้ โดยไม่กระทบ Component อื่นที่ใช้โครงสร้างเดียวกัน</div>

<h2>ขั้นที่ 7: Complete → แก้แบบกราฟิก</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-07.jpg", "ขั้นที่ 7: Complete → แก้แบบกราฟิก"),
    step_list([
        '<strong>Edit component graphically</strong>',
        'ยังไม่เลือก Save to database',
        '<strong>Finish</strong>',
        'Symbol 1–4 ของ Component เรียงตามลำดับ',
        'Model สำหรับแบบตู้',
    ])
)}
<div class="tip"><strong>ทำต่อ:</strong> กด L โหลด component-editor.vis ให้ดูง่าย แล้วลบ / เพิ่ม Symbol ตามอุปกรณ์จริง</div>

<h2>ขั้นที่ 8: Component Properties และ Pin Assignment</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-08.jpg", "ขั้นที่ 8: Component Properties และ Pin Assignment"),
    step_list([
        'คลิกขวา Component ใน tree → <strong>Properties</strong>',
        'Attribute ของ Component',
        'แท็บ <strong>Pin Assignment</strong> Symbol ในโครงสร้าง',
        'ผูกชื่อขา A1/A2, 1–6, 13/14 กับ Symbol',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> Order Definition กำหนดลำดับ Symbol · Master/Slave Assignment ทำให้มี Cross-reference</div>

<h2>ขั้นที่ 9: Save To Database (เมื่อพร้อม)</h2>
{side_by_side(
    screenshot("assets/images/lessons/03-09.jpg", "ขั้นที่ 9: Save To Database (เมื่อพร้อม)"),
    step_list([
        'คลิกขวา Symbol / Component ใน tree → <strong>Save To Database</strong>',
        'ตรวจชื่อ Class เลขขา และ Model ให้ครบก่อนบันทึก',
        'ฝั่งโปรเจกต์กด <strong>F5</strong> ที่ Database Window',
    ])
)}
<div class="note"><strong>ระวัง:</strong> บันทึกลงฐานข้อมูลที่เปิดอยู่ทันที และย้อนไม่ได้ด้วย Undo · สำรอง .mdb ก่อน และฝึกบนสำเนา</div>

<h2>ไฟล์ที่ใช้ในบทนี้</h2>
<table>
<tr><th>ไฟล์</th><th>มาจากไหน</th><th>ใช้ทำอะไร</th></tr>
<tr><td>โปรเจกต์ <code>.e3s</code> ที่เปิดอยู่</td><td>สำเนาจากบทที่ 00–01</td><td>เปิด Database Editor จาก Tools → Start Database Editor</td></tr>
<tr><td>ฐานข้อมูลสำหรับฝึก (<code>.mdb</code>)</td><td>สำเนาของฐานข้อมูลที่ใช้งาน — สำรองไฟล์ก่อนเสมอ</td><td>สร้าง Symbol / Component ใหม่ (Save To Database เขียนลงไฟล์นี้)</td></tr>
</table>

<h2>Checklist ท้ายบท</h2>
<table>
<tr><th>ข้อ</th><th>สิ่งที่ต้องทำได้</th></tr>
<tr><td>1</td><td>เปิด Database Editor และหา tree ของ Symbol ได้</td></tr>
<tr><td>2</td><td>สร้าง New Symbol และวาง Node ได้</td></tr>
<tr><td>3</td><td>ตั้งชื่อ / Class ใน Symbol Properties ได้</td></tr>
<tr><td>4</td><td>ใช้ Component Wizard ตั้งต้นจากตัวเดิมได้</td></tr>
<tr><td>5</td><td>อธิบายความต่าง Use current / Make new copy ได้</td></tr>
<tr><td>6</td><td>ดู Pin Assignment ได้</td></tr>
<tr><td>7</td><td>บอกได้ว่าเมื่อไรควร Save To Database</td></tr>
</table>
<div class="tip"><strong>ครบทุกข้อ:</strong> ไปต่อบทที่ 04: สร้าง Model ของอุปกรณ์สำหรับแบบตู้</div>

<h2>ปัญหาที่พบบ่อย และวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>ไม่เห็น tree ของ Symbol</td><td>ขยายหน้าต่าง E³.dbe ให้เต็มจอ หรือลากขยายช่อง Database Window</td></tr>
<tr><td>กด New แล้วได้หน้าต่าง E³.dbe ใหม่</td><td>ปิดหน้าต่างนั้น ใช้คลิกขวาใน tree → New Symbol / New Component</td></tr>
<tr><td>เมนู Insert กดไม่ได้</td><td>ต้องเปิด Symbol / Model อยู่ก่อน</td></tr>
<tr><td>โปรเจกต์ไม่เห็น Symbol ใหม่</td><td>Save To Database แล้วกด F5 ที่ Database Window ของโปรเจกต์</td></tr>
<tr><td>แก้ Component แล้วกระทบตัวอื่น</td><td>ใช้ Make new copy ใน Structure ของ Wizard</td></tr>
<tr><td>ปิด E³.dbe แล้วถามบันทึก</td><td>No = ไม่บันทึก · Save to Database = เขียนลงฐานข้อมูลจริง</td></tr>
</table>
'''
