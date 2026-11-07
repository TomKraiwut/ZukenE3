# -*- coding: utf-8 -*-
"""Lesson 04: สร้าง Model ของตู้ -- from 02_Quicktour/04_Panel_Model/E3_04_Panel_Model_StepByStep.pptx
(drafted by pptx_to_chapter.py, finished by hand)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "สร้าง New Model จากแท็บ Model ใน Database Editor",
    "ตั้ง Model name / Model type และขนาด X / Y / Z ใน Model Properties",
    "ใส่ Mounting Description ให้ตรงกับ Slot description ของราง (เช่น TS 35 mm)",
    "ใช้เมนู Insert: Slot, Model View และ STEP model",
    "ปิด E³.dbe โดยไม่บันทึก และรู้ว่า Save to Database มีผลกับใครบ้าง",
]

BODY = f'''
<p class="lead" style="max-width:46em;">Model + Slot = วางลงตู้ได้ — ทีละขั้น รวม 6 ขั้น ใน <strong>Database Editor</strong>
สร้างภาพของอุปกรณ์สำหรับแบบตู้ ตั้งขนาดจริงและ Mounting Description ให้อุปกรณ์ snap เข้าราง Mount ในบทที่ 02 ใช้เวลาประมาณ 45 นาที</p>

<h2>ภาพรวม: Model + Slot = วางลงตู้ได้</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>แท็บ Model</td><td>tree ของ Model ใน Database</td></tr>
<tr><td>02</td><td>New Model</td><td>แผ่นวาด Model เปล่า</td></tr>
<tr><td>03</td><td>Model Properties</td><td>ชื่อ ชนิด หน่วย</td></tr>
<tr><td>04</td><td>Shape</td><td>Mounting description · ขนาด X/Y/Z</td></tr>
<tr><td>05</td><td>Insert Slot</td><td>จุด / เส้น / พื้นที่สำหรับติดตั้ง</td></tr>
<tr><td>06</td><td>ปิดโดยไม่บันทึก</td><td>บันทึกจริงเมื่อพร้อม</td></tr>
</table>
<div class="tip"><strong>สิ่งที่ต้องมี:</strong> ผ่านบทที่ 02–03 · license Database Editor + E³.panel · ขนาดจริงจาก datasheet ของอุปกรณ์</div>
<div class="tip"><strong>เชื่อมกับบทที่ 02:</strong> Mounting description ของ Model (เช่น TS 35 mm) ต้องตรงกับ Slot description ของราง Mount ในตู้</div>

<h2>ขั้นที่ 1: New Model</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-01.jpg", "ขั้นที่ 1: New Model"),
    step_list([
        'แท็บ <strong>Model</strong>',
        'คลิกขวาที่โฟลเดอร์ เช่น <strong>Electric</strong>',
        '<strong>New Model</strong>',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> เปิด E³.dbe จาก Tools → Start Database Editor (บทที่ 03) แล้วขยายหน้าต่างให้เต็มจอ</div>

<h2>ขั้นที่ 2: แผ่นวาด Model</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-02.jpg", "ขั้นที่ 2: แผ่นวาด Model"),
    step_list([
        'จุดกลางแผ่นคือ <strong>Origin</strong> ของ Model',
        '<strong>NewModel1</strong> อยู่ในโฟลเดอร์ Model ของ In use...',
        'วาดรูปด้านหน้าด้วยเครื่องมือ Graphic หรือ <strong>Insert → STEP model</strong>',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> Model ใช้หน่วยมิลลิเมตร ขนาดต้องตรงอุปกรณ์จริง เพราะใช้ตรวจการชนในตู้</div>

<h2>ขั้นที่ 3: Model Properties</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-03.jpg", "ขั้นที่ 3: Model Properties"),
    step_list([
        '<strong>Model name</strong>',
        '<strong>Model type</strong> = Device',
        'แท็บ Shape: <strong>Mounting Description</strong> = TS 35 mm',
        'เลือก / พิมพ์แล้วกด <strong>Add</strong>',
        '<strong>Size X / Y / Z</strong>',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> อุปกรณ์จะ snap เข้าราง Mount ที่มี Slot description ตรงกับ Mounting Description นี้</div>

<h2>ขั้นที่ 4: เมนู Insert ของ Model</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-04.jpg", "ขั้นที่ 4: เมนู Insert ของ Model"),
    step_list([
        '<strong>Slot...</strong> จุดติดตั้ง',
        '<strong>Model View</strong> มุมมอง Back / Right / Left / Top / Bottom',
        '<strong>STEP model...</strong> นำเข้าไฟล์ 3D',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> เมนู Insert ใช้ได้เมื่อมี Model เปิดอยู่</div>

<h2>ขั้นที่ 5: Insert Slot</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-05.jpg", "ขั้นที่ 5: Insert Slot"),
    step_list([
        '<strong>Type</strong> ชนิด Slot',
        '<strong>Description</strong> เช่น Rail type 100 / TS 35 mm',
        '<strong>Name</strong> ชื่อ Slot',
        '<strong>Point / Line / Area</strong>',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> Point = จุดยึด · Line = แนวราง · Area = พื้นที่ติดตั้ง</div>

<h2>ขั้นที่ 6: ปิด E³.dbe</h2>
{side_by_side(
    screenshot("assets/images/lessons/04-06.jpg", "ขั้นที่ 6: ปิด E³.dbe"),
    step_list([
        '<strong>No</strong> = ไม่บันทึก (ใช้ตอนฝึก)',
        '<strong>Save to Database</strong> = บันทึกลงฐานข้อมูลจริง',
    ])
)}
<div class="note"><strong>ระวัง:</strong> Save to Database เขียนทับฐานข้อมูลที่ทุกคนใช้ร่วมกัน สำรอง .mdb ก่อนเสมอ</div>

<h2>ไฟล์ที่ใช้ในบทนี้</h2>
<table>
<tr><th>ไฟล์</th><th>มาจากไหน</th><th>ใช้ทำอะไร</th></tr>
<tr><td>ฐานข้อมูลสำหรับฝึก (<code>.mdb</code>)</td><td>สำเนาเดียวกับบทที่ 03 — สำรองไฟล์ก่อนเสมอ</td><td>สร้าง Model ใหม่ในแท็บ Model (ฝึกแล้วปิดโดยไม่บันทึก)</td></tr>
<tr><td>datasheet ของอุปกรณ์</td><td>ผู้ผลิตอุปกรณ์</td><td>ขนาดจริง X / Y / Z และชนิดรางที่ติดตั้ง</td></tr>
</table>

<h2>Checklist ท้ายบท</h2>
<table>
<tr><th>ข้อ</th><th>สิ่งที่ต้องทำได้</th></tr>
<tr><td>1</td><td>สร้าง New Model จากแท็บ Model ได้</td></tr>
<tr><td>2</td><td>ตั้งชื่อและชนิดใน Model Properties ได้</td></tr>
<tr><td>3</td><td>ใส่ Mounting Description ให้ตรงกับรางได้</td></tr>
<tr><td>4</td><td>ใส่ขนาด X / Y / Z ได้</td></tr>
<tr><td>5</td><td>เปิด Insert Slot และเลือกชนิดได้</td></tr>
<tr><td>6</td><td>ปิด E³.dbe โดยไม่บันทึกได้</td></tr>
</table>
<div class="tip"><strong>ครบทุกข้อ:</strong> ทวนบทที่ 02: วาง Component ที่มี Model ลงรางในตู้</div>

<h2>ปัญหาที่พบบ่อย และวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>ไม่เห็น tree ของ Model</td><td>ขยายหน้าต่าง E³.dbe ให้เต็มจอ แล้วเลือกแท็บ Model</td></tr>
<tr><td>เมนู Insert กดไม่ได้</td><td>ต้องมี Model เปิดอยู่ก่อน (ขั้นที่ 1–2)</td></tr>
<tr><td>วางอุปกรณ์ในตู้แล้วไม่ snap เข้าราง</td><td>Mounting Description ของ Model ต้องตรงกับ Slot description ของราง Mount (เช่น TS 35 mm)</td></tr>
<tr><td>อุปกรณ์ในตู้ขนาดไม่ตรงของจริง</td><td>Model ใช้หน่วยมิลลิเมตร ใส่ Size X / Y / Z จาก datasheet</td></tr>
<tr><td>ปิด E³.dbe แล้วถามบันทึก</td><td>No = ไม่บันทึก (ตอนฝึก) · Save to Database = เขียนลงฐานข้อมูลจริงที่ทุกคนใช้</td></tr>
</table>
'''
