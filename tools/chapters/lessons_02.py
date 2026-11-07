# -*- coding: utf-8 -*-
"""Lesson 02: ออกแบบตู้ E3.panel -- from 02_Quicktour/02_Panel/E3_02_Panel_StepByStep.pptx
(drafted by pptx_to_chapter.py, finished by hand)"""
from gen_site import screenshot, step_list, side_by_side

OBJECTIVES = [
    "เปิดแบบตู้ และบอกได้ว่า Mounting rail / Cable duct / พื้นที่สีแดงคืออะไร",
    "หาอุปกรณ์ที่ยังไม่วางในแท็บ Panel - Not Placed แล้ววางลงรางที่ถูกต้อง",
    "เพิ่ม Cable Duct และราง Mount (TS 35 mm) และอธิบายหน้าที่ของ Slot description",
    "สั่ง Panel Autoconnect ให้เดินสายตามราง แล้วดูตู้แบบ 3D",
    "ส่งออก Wiring list จากแบบตู้เป็น Excel",
]

BODY = f'''
<p class="lead" style="max-width:46em;">ตู้คืออีกมุมมองของวงจรเดียวกัน — ทีละขั้น รวม 10 ขั้น ใน <strong>E³.panel</strong>
วางอุปกรณ์ -Q6 ที่ได้จากปั๊มตัวที่ 3 ในบทที่ 01 ลงราง เพิ่มราง เดินสายอัตโนมัติ ดูตู้ 3D และส่งออก Wiring list ใช้เวลาประมาณ 1 ชั่วโมง</p>

<h2>ภาพรวม: ตู้คืออีกมุมมองของวงจรเดียวกัน</h2>
<table>
<tr><th>ลำดับ</th><th>หัวข้อ</th><th>ทำอะไร</th></tr>
<tr><td>01</td><td>แบบตู้ 2D</td><td>Sheet 6 ในโฟลเดอร์ 02-Panel</td></tr>
<tr><td>02</td><td>Placed / Not Placed</td><td>อุปกรณ์จากวงจรที่รอวาง</td></tr>
<tr><td>03</td><td>วางลงราง</td><td>ระบบไฮไลต์รางที่ติดตั้งได้</td></tr>
<tr><td>04</td><td>ราง Mount / Cable Duct</td><td>Slot TS 35 mm · ความจุราง</td></tr>
<tr><td>05</td><td>Autoconnect</td><td>เดินสายตามรางอัตโนมัติ</td></tr>
<tr><td>06</td><td>ตู้ 3D + Wiring list</td><td>Panel toolbar · Add-ons Excel</td></tr>
</table>
<div class="tip"><strong>สิ่งที่ต้องมี:</strong> ผ่านบทที่ 01 (มี -Q6 / -Q7 จากปั๊มตัวที่ 3) · license E³.panel · เมาส์ 3 ปุ่มสำหรับหมุนมุมมอง 3D</div>
<div class="tip"><strong>ข้อมูลชุดเดียว:</strong> เปลี่ยนชื่ออุปกรณ์ในวงจร ชื่อในตู้เปลี่ยนตาม · อุปกรณ์ที่เพิ่มในวงจรจะรอใน Panel - Not Placed</div>

<h2>ขั้นที่ 1: เปิดแบบตู้ Sheet 6</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-01.jpg", "ขั้นที่ 1: เปิดแบบตู้ Sheet 6"),
    step_list([
        '<strong>พื้นที่สีแดง</strong> = ความร้อนสูญเสีย (Level 200) ปิดได้ด้วยคีย์ L',
        '<strong>Mounting rail</strong> รางจับอุปกรณ์ (สีเหลือง)',
        '<strong>Cable duct</strong> รางเดินสาย สายในตู้เดินผ่านรางนี้',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> เปิด Sheet 6 จากโฟลเดอร์ 02-Panel · ซูมด้วย Ctrl + ล้อเมาส์</div>

<h2>ขั้นที่ 2: แท็บ Panel - Placed และ Not Placed</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-02.jpg", "ขั้นที่ 2: แท็บ Panel - Placed และ Not Placed"),
    step_list([
        'แท็บ <strong>Panel - Placed</strong> (ไอคอนสีเขียว)',
        'อุปกรณ์ที่อยู่ในตู้แล้ว',
        'แท็บ <strong>Panel - Not Placed</strong> (สีเหลือง)',
        '<strong>-Q6 / -Q7</strong> จากปั๊มตัวที่ 3 ในบทที่ 01 รอวาง',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> อุปกรณ์ที่เพิ่มในวงจรจะไม่อยู่ในตู้เอง ต้องวางลงตู้จากแท็บ Not Placed</div>

<h2>ขั้นที่ 3: วาง -Q6 ลงราง</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-03.jpg", "ขั้นที่ 3: วาง -Q6 ลงราง"),
    step_list([
        'คลิกขวาที่ <strong>-Q6</strong> (Preview แสดงรูปอุปกรณ์)',
        'เลือก <strong>Place</strong>',
        'รางที่ติดตั้งได้เป็น<strong>สีชมพู</strong> คลิกวางบนราง',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> อุปกรณ์ snap เข้าราง วางซ้อนกันหรือวางบน Cable duct ไม่ได้ · ตรวจจาก Slot Description ของราง</div>

<h2>ขั้นที่ 4: ผลการวาง</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-04.jpg", "ขั้นที่ 4: ผลการวาง"),
    step_list([
        '<strong>-Q6</strong> อยู่บนรางแล้ว (3RT10251BB40)',
        'Not Placed เหลือเฉพาะ <strong>-Q7</strong>',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> Status bar ล่างจอแจ้ง Component และตำแหน่งที่วาง</div>

<h2>ขั้นที่ 5: เพิ่ม Cable Duct</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-05.jpg", "ขั้นที่ 5: เพิ่ม Cable Duct"),
    step_list([
        '<strong>Insert → Mount...</strong> (ราง)',
        '<strong>Insert → Cable Duct...</strong>',
        '<strong>Height</strong> ความสูงราง',
        '<strong>Width</strong> ความกว้างราง (Quicktour ใช้ 25 mm)',
        '<strong>Fill limit</strong> ความจุสาย (ค่าจาก Settings 70%)',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> ไม่ติ๊ก Length แล้วลากความยาวเอง · จุดวงกลมเล็กปรากฏเมื่อรางเชื่อมกัน</div>

<h2>ขั้นที่ 6: เพิ่ม Mount (TS 35 mm)</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-06.jpg", "ขั้นที่ 6: เพิ่ม Mount (TS 35 mm)"),
    step_list([
        '<strong>Slot description</strong> = TS 35 mm',
        '<strong>Height</strong> 7.5 mm',
        '<strong>Width</strong> 35 mm',
    ])
)}
<div class="note"><strong>ข้อควรจำ:</strong> ระบบใช้ Slot description ตรวจว่าอุปกรณ์ตัวไหนติดตั้งบนรางนี้ได้ (Model ต้องมีค่าเดียวกัน บทที่ 04)</div>

<h2>ขั้นที่ 7: Logic Lines และ Panel Autoconnect</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-07.jpg", "ขั้นที่ 7: Logic Lines และ Panel Autoconnect"),
    step_list([
        '<strong>View → Logic Lines</strong>',
        '<strong>Cores On Panel</strong> แสดงเส้นประของสายที่ต้องเดิน',
        'คลิกขวาที่อุปกรณ์ (หรือ Ctrl+A) → <strong>Panel Autoconnect</strong>',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> ระบบหาเส้นทางสั้นที่สุดผ่าน Cable duct ตามความจุราง · สายที่เดินไม่ได้แจ้งใน Output Window → Results</div>

<h2>ขั้นที่ 8: สลับเป็นมุมมอง 3D</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-08.jpg", "ขั้นที่ 8: สลับเป็นมุมมอง 3D"),
    step_list([
        'Panel toolbar → ปุ่ม <strong>3D</strong> (แสดง Sheet แบบ 3D)',
        '3D View toolbar → <strong>Isometric</strong>',
        'ตู้ทั้งแผ่นแสดงแบบ 3D',
    ])
)}
<div class="tip"><strong>เปิด toolbar:</strong> คลิกขวาบนแถบ toolbar แล้วติ๊ก Panel และ 3D View (ค่าเริ่มต้นปิดอยู่)</div>

<h2>ขั้นที่ 9: ดูตู้ 3D</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-09.jpg", "ขั้นที่ 9: ดูตู้ 3D"),
    step_list([
        'อุปกรณ์อยู่บนแผ่นติดตั้งในตู้ตามตำแหน่งจริง',
        '<strong>ลากปุ่มซ้าย</strong> หมุน · <strong>ลากปุ่มขวา</strong> เลื่อน · <strong>หมุนล้อ</strong> ซูม',
        '<strong>Shift + ลูกศร</strong> พับผนัง / ประตู (Pivot)',
    ])
)}
<div class="note"><strong>หมายเหตุ:</strong> คลิกขวาที่อุปกรณ์ → Transparency in 3D ทำให้มองทะลุได้</div>

<h2>ขั้นที่ 10: Wiring List จากแบบตู้</h2>
{side_by_side(
    screenshot("assets/images/lessons/02-10.jpg", "ขั้นที่ 10: Wiring List จากแบบตู้"),
    step_list([
        '<strong>Add-ons</strong>',
        '<strong>EXCEL Documents</strong>',
        '<strong>Wiring list from Panel</strong>',
    ])
)}
<div class="tip"><strong>ผลลัพธ์:</strong> Excel แสดง From / To เลขสาย ชนิด สี ขนาดหน้าตัด ความยาว และเส้นทางเดินสาย</div>

<h2>ไฟล์ที่ใช้ในบทนี้</h2>
<table>
<tr><th>ไฟล์</th><th>มาจากไหน</th><th>ใช้ทำอะไร</th></tr>
<tr><td><code>Cooling water pump_01.e3s</code></td><td>ไฟล์ที่ทำเสร็จจากบทที่ 01 (มี -Q6 / -Q7 ของปั๊มตัวที่ 3)</td><td>ฝึกขั้นที่ 1–10 บน Sheet 6 โฟลเดอร์ 02-Panel</td></tr>
<tr><td>Wiring list (Excel)</td><td>ขั้นที่ 10 Add-ons → EXCEL Documents</td><td>รายการสาย From / To ความยาว และเส้นทาง</td></tr>
</table>

<h2>Checklist ท้ายบท</h2>
<table>
<tr><th>ข้อ</th><th>สิ่งที่ต้องทำได้</th></tr>
<tr><td>1</td><td>เปิดแบบตู้และบอกได้ว่า Rail / Duct / พื้นที่สีแดงคืออะไร</td></tr>
<tr><td>2</td><td>หาอุปกรณ์ที่ยังไม่วางในแท็บ Not Placed ได้</td></tr>
<tr><td>3</td><td>วางอุปกรณ์ลงรางที่ถูกต้องได้</td></tr>
<tr><td>4</td><td>อธิบาย Slot description (TS 35 mm) ได้</td></tr>
<tr><td>5</td><td>สั่ง Panel Autoconnect ได้</td></tr>
<tr><td>6</td><td>สลับ 2D / 3D และหมุนมุมมองได้</td></tr>
<tr><td>7</td><td>ส่งออก Wiring list ได้</td></tr>
</table>
<div class="tip"><strong>ครบทุกข้อ:</strong> ไปต่อบทที่ 03: สร้าง Symbol และ Component เองใน Database Editor</div>

<h2>ปัญหาที่พบบ่อย และวิธีแก้</h2>
<table>
<tr><th>อาการ</th><th>วิธีแก้</th></tr>
<tr><td>ไม่เห็นปุ่ม 3D</td><td>คลิกขวาบนแถบ toolbar → ติ๊ก Panel และ 3D View</td></tr>
<tr><td>วางอุปกรณ์แล้วไม่ติดราง</td><td>Slot description ของรางกับ Model ต้องตรงกัน (เช่น TS 35 mm)</td></tr>
<tr><td>อุปกรณ์ใหม่ไม่อยู่ในตู้</td><td>ดูแท็บ Panel - Not Placed แล้วสั่ง Place</td></tr>
<tr><td>พื้นที่สีแดงบังอุปกรณ์</td><td>กด L แล้วปิด Level 200</td></tr>
<tr><td>Autoconnect เดินสายไม่ได้</td><td>ตรวจ Output Window → Results · รางเต็ม (Fill limit) หรือไม่มีรางเชื่อม</td></tr>
<tr><td>toolbar ที่เปิดเพิ่มติดไปครั้งหน้า</td><td>View → Workspace Configurations → Restore หรือปิด toolbar เองก่อนออก</td></tr>
</table>
'''
