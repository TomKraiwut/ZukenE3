"""Schematics chapter content (schematic/01.html .. 10.html).

Ported verbatim from the original flat worksheet-01.html..worksheet-10.html —
no content was rewritten, only relocated into the generator pattern.
"""
import gen_site as gs

TITLE = {
    1: "บทที่ 1: Project &amp; UI Setup - Zuken E3.series Tutorial",
    2: "บทที่ 2: Placing &amp; Editing Devices - Zuken E3.series Tutorial",
    3: "บทที่ 3: Connecting &amp; Online Checks - Zuken E3.series Tutorial",
    4: "บทที่ 4: Fields &amp; Levels - Zuken E3.series Tutorial",
    5: "บทที่ 5: Signals &amp; Signal Tree - Zuken E3.series Tutorial",
    6: "บทที่ 6: Global Search &amp; Replace - Zuken E3.series Tutorial",
    7: "บทที่ 7: Terminals &amp; Terminal Plan - Zuken E3.series Tutorial",
    8: "บทที่ 8: Subcircuits - Zuken E3.series Tutorial",
    9: "บทที่ 9: DBE - สร้าง Symbol และ Component ใหม่ - Zuken E3.series Tutorial",
    10: "บทที่ 10: Database Sync &amp; Reporting - Zuken E3.series Tutorial",
}

BODY = {}

BODY[1] = '''    <h1>บทที่ 1: การใช้งานส่วนติดต่อผู้ใช้และการจัดการโครงการ (Project &amp; UI Setup)</h1>
    <p class="lead">จุดเริ่มต้นของทุกงานออกแบบ — รู้จักหน้าต่างหลัก จัดการโปรเจกต์อย่างปลอดภัย และเตรียมชีทแรกให้พร้อมวาดวงจร</p>

    <div class="objectives">
        <p>วัตถุประสงค์การเรียนรู้</p>
        <ol>
            <li>เพื่อระบุและเข้าถึงส่วนประกอบที่สำคัญทางโครงสร้างของหน้าต่างโปรแกรม เช่น Project Window, Database Window และ Preview Window ได้อย่างถูกต้อง</li>
            <li>เพื่อสร้าง เปิด และบันทึกโครงการ (Save / Save As) รวมถึงการจัดระเบียบหน้าต่าง Workspace และนำทางแบบย่อขยาย (Zoom / Panning) ได้อย่างถูกวิธีตามมาตรฐานความปลอดภัยข้อมูล</li>
            <li>เพื่อแทรกหน้าแผ่นงานเขียนแบบใหม่ (Insert Sheet) เลือกรูปแบบมาตรฐานแผ่นงาน (เช่น DINA3) และระบุขอบเขตตำแหน่งติดตั้ง (Location) ของแผ่นงานนั้นๆ</li>
        </ol>
    </div>

    <h2>1. หน้าต่างหลักของโปรแกรม</h2>
    <p>E3.series เปิดมาพร้อมหน้าต่างย่อยหลายบาน แต่ละบานทำหน้าที่ต่างกันชัดเจน:</p>
    <table>
        <tr><th>หน้าต่าง</th><th>หน้าที่</th></tr>
        <tr><td><strong>Project Window</strong></td><td>โครงสร้างโปรเจกต์แบบ Tree แสดงลำดับชั้นของ Sheet และ Symbol/Device ทั้งหมดในโปรเจกต์ — คลิกเพื่อกระโดด (Jump to) ไปยัง Object นั้นบนชีทได้ทันที</td></tr>
        <tr><td><strong>Database Window</strong></td><td>คลัง Symbol/Component ในฐานข้อมูลกลาง มีแท็บ Component/Symbol/Misc ให้ค้นหาและลากไปวางบนชีท</td></tr>
        <tr><td><strong>Preview Window</strong></td><td>แสดงชีททั้งแผ่นแบบย่อ มีกรอบสีขาวบอกพื้นที่ที่ Zoom อยู่ปัจจุบัน ใช้ลากกรอบเพื่อ Pan ไปจุดอื่นได้เร็วกว่าการเลื่อน Scrollbar</td></tr>
    </table>
    <p>ปิด/เปิดหน้าต่างเหล่านี้แบบ Auto Hide ได้เพื่อประหยัดพื้นที่จอ และบันทึกการจัดวางเป็น <strong>Workspace Configuration</strong> ของตัวเองได้ ถ้าใช้จอเล็กหรือสลับงานหลายแบบบ่อยๆ</p>

    <h2>2. จัดการโปรเจกต์และนำทางบนชีท</h2>
    <p>
        สร้างโปรเจกต์ใหม่ เปิดโปรเจกต์เดิม และปิดโปรเจกต์ได้จากเมนู Project ตามปกติ — สิ่งที่ต้องระวังคือ <strong>Save</strong>
        จะบันทึกทับไฟล์เดิมทันที ในขณะที่ <strong>Save As</strong> สร้างสำเนาใหม่ภายใต้ชื่อ/ตำแหน่งที่ระบุ ควรใช้ Save As
        ทุกครั้งที่จะทดลองแก้ไขแบบเสี่ยงๆ เพื่อไม่ให้ไฟล์ต้นฉบับเสียหาย
    </p>
    <table>
        <tr><th>คีย์ลัด</th><th>คำสั่ง</th></tr>
        <tr><td><code>Z</code> หรือ <code>O</code></td><td>Zoom เข้าพื้นที่ที่เลือก / กด <code>O</code> ซ้ำเพื่อกลับสู่ Overview เดิม</td></tr>
        <tr><td>Scroll wheel</td><td>Pan แนวตั้ง — กด <code>Shift</code> ค้างด้วยเพื่อ Pan แนวนอน</td></tr>
        <tr><td><code>Ctrl</code> + Scroll wheel</td><td>Dynamic Zoom โดยยึดตำแหน่งเคอร์เซอร์เป็นจุดศูนย์กลาง</td></tr>
        <tr><td><code>+</code> / <code>-</code></td><td>Incremental Zoom เข้า/ออกทีละขั้นตามค่าที่ตั้งไว้ใน Project Settings</td></tr>
        <tr><td><code>J</code></td><td>Adjust Zoom — โฟกัสอัตโนมัติไปที่ Object ที่เลือกอยู่</td></tr>
    </table>

    <div class="tip">
        <strong>Tip:</strong> ลากกรอบสีขาวใน Preview Window แทนการ Scroll ไปมาเวลาโปรเจกต์มีหลายสิบชีท จะนำทางได้เร็วกว่ามาก
        โดยเฉพาะเวลาต้องสลับดูหลายจุดในชีทเดียวกัน
    </div>

    <h2>3. แทรกชีทแรกและกำหนด Location</h2>
    <p>เริ่มงานจริงด้วยการแทรกชีทเขียนแบบ:</p>
    <ol class="steps">
        <li>Insert → Sheet (หรือคลิกขวาใน Project Window เลือก Insert Sheet)</li>
        <li>เลือก Sheet Format มาตรฐาน เช่น <strong>DINA3</strong> — ขนาดกระดาษกำหนดพื้นที่วาดและ Sheet Text ที่มากับ Template</li>
        <li>ตั้งชื่อ Sheet ให้สื่อความหมาย (เช่น ตามระบบย่อยที่จะออกแบบ)</li>
        <li>กำหนด <strong>Location</strong> (ตำแหน่งติดตั้งจริง) ที่ Sheet Header — Device ที่วางบนชีทนี้จะรับค่า Location นี้ไปอัตโนมัติถ้าไม่ได้ตั้งเอง</li>
    </ol>

    <p>
        Location เป็นส่วนหนึ่งของ <strong>Item Designation</strong> — รหัสประจำตัวของทุก Device ตามมาตรฐาน IEC 81346 / DIN 40719
        ที่จะใช้ตลอดทั้งเว็บนี้ ประกอบด้วย 4 ส่วน:
    </p>
    <table>
        <tr><th>สัญลักษณ์นำหน้า</th><th>ความหมาย</th></tr>
        <tr><td><code>=</code></td><td>Higher Level Assignment (HLA) — กลุ่ม/ระบบย่อยที่อุปกรณ์สังกัด</td></tr>
        <tr><td><code>+</code></td><td>Location — ตำแหน่งติดตั้งจริง เช่น ตู้คอนโทรลไหน (ตั้งที่ Sheet Header ในขั้นตอนนี้)</td></tr>
        <tr><td><code>-</code></td><td>Device Designation — หมายเลขอุปกรณ์ (ส่วนที่ใช้บ่อยที่สุด ถ้าใช้ตัวนี้ตัวเดียวสามารถละเครื่องหมาย <code>-</code> ได้ — แก้ไขในบทที่ 2)</td></tr>
        <tr><td><code>:</code></td><td>Pin Name — ชื่อขา/สายที่ต่อกับ Device นั้น</td></tr>
    </table>
    <p>ลำดับเต็มคือ <code>=HLA +Location -Device:Pin</code> เช่น <code>=K1+PANEL1-Q3:14</code> — ส่วน Field ที่ใช้แบ่งเขต HLA/Location ย่อยภายในชีทเดียว เรียนต่อในบทที่ 4</p>

    <div class="note">
        <strong>ข้อควรระวังด้านความปลอดภัยข้อมูล:</strong> ทำงานบนฐานข้อมูลกลาง (Shared Database) ผ่านการเชื่อมต่อที่ทีมกำหนดไว้เท่านั้น
        อย่าคัดลอกไฟล์ฐานข้อมูลมาแก้ไขนอกระบบ เพราะจะทำให้ Part/Symbol ที่ทีมอื่นใช้ไม่ตรงกับของคุณ และอย่าลืม Save As
        เก็บสำรองก่อนเริ่มแก้ไขโครงสร้างใหญ่ๆ ของโปรเจกต์
    </div>

    <h2>ตัวอย่างฝึกทำ</h2>
    <p><strong>โจทย์:</strong> เปิดโปรเจกต์ใหม่ แทรกชีท DINA3 หนึ่งแผ่น ตั้งชื่อและ Location ให้เรียบร้อย จากนั้นลองเปิด Database Window ค้นหา Symbol อะไรก็ได้ 1 ตัว แล้วใช้ Preview Window ซูมเข้าไปดูตำแหน่งกึ่งกลางชีท</p>
    <p><strong>คำถามฝึกคิด:</strong> ถ้าลืมกำหนด Location ที่ Sheet Header ตั้งแต่ตอนแทรกชีท จะเกิดผลอะไรตามมาเมื่อวาง Device หลายสิบตัวบนชีทนั้นไปแล้ว?</p>
    <div class="tip"><strong>เฉลย:</strong> Device ทุกตัวที่วางไปแล้วจะรับ Location ว่าง/ค่าเริ่มต้นจาก Sheet Header ไปด้วย ถ้ามาแก้ Location ของ Sheet ทีหลัง Device ที่ Location ตรงกับ Sheet จะเปลี่ยนตามอัตโนมัติ แต่ตัวที่เคยถูกแก้ Location มือเองแยกไว้ก่อนจะไม่เปลี่ยนตาม ทำให้ Item Designation ปนกันได้ — ตั้ง Location ให้ถูกตั้งแต่แรกจะปลอดภัยกว่าการไล่แก้ทีหลัง</div>

    <div class="page-nav">
        <a href="schematic.html">← กลับหน้ารวม Schematics</a>
        <a href="worksheet-02.html">ถัดไป: บทที่ 2 →</a>
    </div>'''

BODY[2] = '''    <h1>บทที่ 2: การวางอุปกรณ์และการแก้ไขคุณสมบัติแผงผัง (Placing &amp; Editing Devices)</h1>
    <p class="lead">จากฐานข้อมูลสู่ชีทจริง — ค้นหา วาง และปรับแต่งคุณสมบัติของ Device แต่ละตัวให้ตรงกับแบบ</p>

    <div class="objectives">
        <p>วัตถุประสงค์การเรียนรู้</p>
        <ol>
            <li>เพื่อค้นหาและลากวางอุปกรณ์ (Drag &amp; Drop) จากฐานข้อมูลส่วนกลางหรือจากตารางข้อมูลอุปกรณ์ (Component Table) ลงสู่แผ่นงานได้อย่างแม่นยำ</li>
            <li>เพื่อจัดวางสัญลักษณ์พินอุปกรณ์ทีละชิ้น (Place Objects One-by-One) และสามารถข้ามไปติดตั้งสัญลักษณ์ตัวถัดไปในอุปกรณ์ชุดเดียวกันได้ทันทีด้วยคีย์ลัด <code>N</code></li>
            <li>เพื่อแก้ไขและอัปเดตค่าคุณสมบัติอุปกรณ์ (Device Properties) เช่น การระบุรหัสประจำตัวอุปกรณ์ (Device Designation) และข้อมูลแอตทริบิวต์อื่นๆ ในระบบแบบ Object-Oriented</li>
        </ol>
    </div>

    <h2>1. ค้นหาและวางอุปกรณ์จากฐานข้อมูล</h2>
    <p>มีสองแหล่งหลักที่ดึง Symbol/Component มาวางบนชีทได้:</p>
    <table>
        <tr><th>แหล่ง</th><th>เหมาะกับ</th></tr>
        <tr><td><strong>Database Window</strong></td><td>ค้นหาด้วยเงื่อนไข (Search Criteria ต่อแท็บ Component/Symbol/Misc) แล้วลาก Drag &amp; Drop ลงชีทโดยตรง เหมาะเมื่อยังไม่รู้ว่าจะใช้ตัวไหนแน่ชัด</td></tr>
        <tr><td><strong>Component Table</strong></td><td>ตารางแสดง Component ที่ถูกใช้ในโปรเจกต์อยู่แล้ว วางซ้ำจากตารางนี้ได้เร็วกว่าค้นหาใหม่ทุกครั้ง เหมาะเมื่อต้องวาง Part เดิมซ้ำหลายจุด</td></tr>
    </table>
    <p>ถ้าต้องใช้ Component เดียวกันหลายตัวในคราวเดียว ใช้คำสั่ง <strong>Load Multiple Copies of Same Component</strong> แทนการลากทีละตัว จะประหยัดเวลาได้มากเมื่อวางอุปกรณ์ประเภทเดียวกันจำนวนมาก เช่น Terminal หรือ Relay รุ่นเดียวกันหลายสิบตัว</p>

    <h2>2. วางสัญลักษณ์ทีละชิ้นด้วย Place Objects One-by-One</h2>
    <p>
        อุปกรณ์บางชนิดประกอบด้วยหลาย Symbol ที่ต้องแยกไปวางคนละตำแหน่งบนชีท (เช่น รีเลย์ตัวเดียวที่มีทั้งขดลวดและหน้าสัมผัสหลายชุด)
        คำสั่ง <strong>Place Objects One-by-One</strong> ให้วางสัญลักษณ์เหล่านี้ทีละตัวแยกกัน โดยระบบจดจำว่ายังเหลือ Symbol
        ใดของอุปกรณ์ชุดเดียวกันที่ยังไม่ได้วาง
    </p>
    <ul>
        <li>Status Bar จะแสดงชื่อ Symbol ตัวที่กำลังจะวางอยู่เสมอ</li>
        <li>กดคีย์ลัด <code>N</code> เพื่อข้ามไปวาง Symbol ตัวถัดไปในอุปกรณ์ชุดเดียวกันได้ทันที โดยไม่ต้องเปิดคำสั่งใหม่</li>
        <li>กด <code>Esc</code> เพื่อยกเลิกคำสั่งกลางคัน — Symbol ที่วางไปแล้วจะยังคงอยู่บนชีท ไม่ถูกย้อนกลับ</li>
        <li>ใช้ไม่ได้กับ Cable Device และ Wire — ส่วน Connector Device จะถูกวางเป็นชุดสมบูรณ์ในโหมด E3.cable แต่แยกวางเป็นขาเดี่ยวๆ ได้ในโหมด E3.schematic</li>
    </ul>

    <div class="tip">
        <strong>Tip:</strong> เวลาวางรีเลย์ที่มีหน้าสัมผัสหลายชุดกระจายอยู่คนละชีท ใช้ <code>N</code> ไล่วางทีละชุดจนครบ
        แทนที่จะปิดคำสั่งแล้วเปิดใหม่ทุกครั้ง — เร็วกว่าและไม่พลาดหลุดขาไหนไป
    </div>

    <h2>3. แก้ไข Device Properties</h2>
    <p>
        เมื่อ Component ถูกวางลงชีทแล้วจะกลายเป็น <strong>Device</strong> — ดับเบิลคลิกเพื่อเปิด Properties Window ซึ่งแยกเป็นแท็บ:
    </p>
    <table>
        <tr><th>แท็บ</th><th>ใช้แก้อะไร</th></tr>
        <tr><td>Device Tab</td><td>Device Designation, Higher Level Assignment, Location — ค่าที่ประกอบเป็น Item Designation ของ Device นี้โดยเฉพาะ</td></tr>
        <tr><td>Attributes</td><td>ค่าคุณสมบัติเสริมอื่นๆ ที่ผูกกับ Device ตัวนี้ เช่น หมายเหตุ หรือแอตทริบิวต์ที่กำหนดเองของทีม</td></tr>
        <tr><td>Component Tab</td><td>ข้อมูลอ้างอิงจาก Component ต้นทางในฐานข้อมูล (Part Number, Manufacturer) — แก้ที่นี่คือแก้เฉพาะ Device ตัวนี้ ไม่กระทบ Component ต้นแบบในฐานข้อมูล</td></tr>
    </table>
    <p>
        เพราะ E3.series เป็นระบบ Object-Oriented การแก้ Device Properties ในโปรเจกต์จึงเป็นการแก้ "สำเนา" เท่านั้น
        Component ต้นแบบในฐานข้อมูลกลางจะไม่เปลี่ยนตาม เว้นแต่จะไปแก้ผ่าน Database Editor โดยตรง (ดูรายละเอียดในบทที่ 9)
    </p>

    <div class="note">
        <strong>ข้อควรระวัง:</strong> อย่าใช้วิธีแก้ Device Designation ซ้ำกันโดยไม่ตั้งใจ — ถ้า Device สองตัวได้ Item Designation
        ซ้ำกันในโปรเจกต์เดียว รายงาน BOM/Wire List จะสับสนว่าเป็นอุปกรณ์ตัวเดียวกัน ทั้งที่จริงเป็นคนละตัว
    </div>

    <h2>ตัวอย่างฝึกทำ</h2>
    <p><strong>โจทย์:</strong> ค้นหารีเลย์ 1 ตัวที่มีขดลวด + หน้าสัมผัส 2 ชุดจาก Database Window วางขดลวดที่ชีทแรก แล้วใช้ <code>N</code> ข้ามไปวางหน้าสัมผัสทั้งสองชุดที่ชีทถัดไป จากนั้นตั้ง Device Designation ให้ทั้งสามส่วนตรงกัน</p>
    <p><strong>คำถามฝึกคิด:</strong> ทำไม Component Table ถึงวางอุปกรณ์ซ้ำได้เร็วกว่า Database Window ทั้งที่ข้อมูลมาจากแหล่งเดียวกัน?</p>
    <div class="tip"><strong>เฉลย:</strong> Component Table กรองมาเฉพาะ Component ที่ถูกดึงเข้าโปรเจกต์แล้ว ไม่ต้องเสียเวลาพิมพ์ค้นหาใน Database Window ใหม่ทุกครั้ง เหมาะเมื่อรู้แน่ชัดว่าจะใช้ Part เดิมซ้ำ ส่วน Database Window เหมาะกับตอนที่ยังไม่รู้ว่าจะใช้ตัวไหน หรือกำลังหา Part ที่ยังไม่เคยใช้ในโปรเจกต์นี้</div>

    <div class="page-nav">
        <a href="worksheet-01.html">← ก่อนหน้า: บทที่ 1</a>
        <a href="worksheet-03.html">ถัดไป: บทที่ 3 →</a>
    </div>'''

BODY[3] = '''    <h1>บทที่ 3: การเชื่อมโยงวงจรไฟฟ้าและระบบควบคุมออนไลน์ (Connecting &amp; Online Checks)</h1>
    <p class="lead">ต่อวงจรให้เร็วด้วย Autoconnect และปล่อยให้ระบบช่วยจับข้อผิดพลาดให้แบบเรียลไทม์</p>

    <div class="objectives">
        <p>วัตถุประสงค์การเรียนรู้</p>
        <ol>
            <li>เพื่อสร้างเส้นเชื่อมโยงทางไฟฟ้า (Connect) ระหว่างพินอุปกรณ์ และใช้งานชุดเครื่องมือ Autoconnect ที่ช่วยร่นระยะการทำงานในแนวดิ่งและแนวราบ</li>
            <li>เพื่อประยุกต์ใช้ระบบตรวจสอบตรรกะแบบออนไลน์ (Online Checks) ในการป้องกันความผิดพลาดทางวิศวกรรมและการขัดกันของการกำหนดขนาดหน้าตัดสายไฟระหว่างทำงานจริง</li>
            <li>เพื่อทำการตัดแต่งและปลดการเชื่อมต่อ (Unconnect) สัญญาณไฟออกจากพิน โดยเลือกได้ว่าจะให้ตรรกะสัญญาณยังคงค้างอยู่ที่พิน หรือสั่งลบสัญญาณไปพร้อมกับการตัดสาย</li>
        </ol>
    </div>

    <h2>1. เชื่อมต่อพินด้วย Connect และ Autoconnect</h2>
    <table>
        <tr><th>คีย์ลัด/คำสั่ง</th><th>ใช้ทำอะไร</th></tr>
        <tr><td><code>C</code> — Insert Connection</td><td>ลากเส้นเชื่อมต่อทีละเส้นด้วยมือ กด Space หรือคลิกซ้ายเพื่อหักมุม</td></tr>
        <tr><td><code>Alt+C</code> — Insert Busbar Connection</td><td>เชื่อมต่อแบบ Busbar สำหรับจุดที่มีสายเข้าหลายเส้นรวมกัน</td></tr>
        <tr><td><code>B</code> — Insert Curve Connection</td><td>เส้นเชื่อมต่อแบบโค้ง</td></tr>
        <tr><td>Autoconnect Vertical / Horizontal</td><td>คลุมพินที่ต้องการด้วยกรอบสี่เหลี่ยม ระบบจะเชื่อมพินที่สอดคล้องกันในแนวตั้งหรือแนวนอนให้อัตโนมัติ ตามทิศทางการเชื่อมต่อ (Connection Direction) ของแต่ละพิน</td></tr>
        <tr><td>Multi-Connection</td><td>เชื่อมหลายเส้นพร้อมกันโดยเปลี่ยนทิศทางกลางทางได้ — เลือกเฉพาะพินฝั่งเริ่มต้นด้วยกรอบสี่เหลี่ยมก่อน</td></tr>
    </table>

    <div class="tip">
        <strong>Tip:</strong> ก่อนใช้ Autoconnect ให้เลือกเฉพาะพินที่ต้องการด้วยกรอบสี่เหลี่ยมให้แม่นยำ เพราะระบบจะพยายามเชื่อม
        "ทุกพินที่สอดคล้องกัน" ภายในกรอบนั้น ถ้าคลุมกว้างเกินไปอาจได้เส้นเชื่อมที่ไม่ตั้งใจปนมาด้วย
    </div>

    <h2>2. Online Checks: ตรวจตรรกะและขนาดหน้าตัดสายแบบเรียลไทม์</h2>
    <p>ระบบตรวจสอบสองเรื่องหลักทันทีที่คุณลงมือเชื่อมต่อ ไม่ต้องรอสั่ง Check Design:</p>
    <ul>
        <li>
            <strong>ตรรกะสัญญาณ (Signal Logic)</strong> — สัญญาณที่ระบบตั้งอัตโนมัติ (System-Generated เช่น <code>#1022</code>)
            จะถูกแทนที่ด้วยสัญญาณที่ผู้ใช้ตั้งเอง (User-Defined) เสมอเมื่อมาเจอกัน แต่ถ้าสัญญาณที่ผู้ใช้ตั้งเอง <em>สองชื่อ</em>
            มาชนกันบนเส้นเดียว ระบบจะปฏิเสธไม่ให้สร้าง Connection พร้อมแจ้งเตือนที่ Status Bar ทันที
        </li>
        <li>
            <strong>ขนาดหน้าตัดสาย (Cross-Section)</strong> — ทุกครั้งที่วางสาย/ตัวนำ ระบบตรวจ 3 อย่างพร้อมกัน: จำนวนสายสูงสุดที่พินรับได้,
            ขนาดหน้าตัดต้องอยู่ในช่วงที่กำหนดของ Model พินนั้น, และผลรวมสูงสุดที่อนุญาต — ถ้าเกินเงื่อนไขจะมีข้อความ Error ทันที
            (เงื่อนไขนี้ต้องมี Model ของอุปกรณ์ที่ระบุค่า Min/Max Cross-Section ไว้ก่อน)
        </li>
    </ul>

    <div class="note">
        <strong>ข้อควรรู้:</strong> Online Checks ช่วยจับข้อผิดพลาดตอนออกแบบ แต่ไม่ได้แทนที่คำสั่ง <strong>Check Design</strong>
        ทั้งหมด — Check Design ยังจำเป็นก่อนส่งออกรายงาน เพราะครอบคลุมการตรวจทั้งโปรเจกต์ ไม่ใช่แค่จุดที่กำลังแก้อยู่
    </div>

    <h2>3. Unconnect vs. Delete: ปลดสายโดยเก็บหรือลบสัญญาณ</h2>
    <p>การเอาเส้นเชื่อมต่อออกทำได้สองแบบ ให้ผลต่างกัน:</p>
    <table>
        <tr><th>คำสั่ง</th><th>ผลลัพธ์</th></tr>
        <tr><td><strong>Delete</strong> (<code>DEL</code>)</td><td>ลบเส้นเชื่อมต่อพร้อมสัญญาณทิ้งทั้งหมด รวมถึงที่พินทั้งสองฝั่งด้วย</td></tr>
        <tr><td><strong>Unconnect</strong></td><td>ลบเฉพาะเส้นกราฟิก แต่สัญญาณยังคงค้างอยู่ที่พินเดิม (เห็นเป็นเส้นประถ้าเปิดปุ่ม Signal Logic Lines) — เลือกได้อีกว่าจะให้ลบนิยามสัญญาณที่พินไปด้วยหรือไม่</td></tr>
    </table>
    <p>
        เลือก Unconnect เมื่อจะย้ายจุดเชื่อมต่อไปที่อื่นแต่ยังอยากให้ระบบจำสัญญาณเดิมไว้ (ลดโอกาสตั้งชื่อสัญญาณผิดซ้ำ)
        ส่วน Delete เหมาะเมื่อต้องการล้างทั้งเส้นและสัญญาณทิ้งจริงๆ เช่น ยกเลิกวงจรส่วนนั้นทั้งหมด
    </p>

    <h2>ตัวอย่างฝึกทำ</h2>
    <p><strong>โจทย์:</strong> วาง Symbol 4 ตัวเรียงแถวตรงกัน แล้วลองใช้ Autoconnect Horizontal คลุมทั้งแถวในครั้งเดียว เทียบเวลากับการลาก Insert Connection ทีละเส้นด้วยมือ</p>
    <p><strong>คำถามฝึกคิด:</strong> ทำไมระบบถึงปฏิเสธการเชื่อมต่อเมื่อสัญญาณ User-Defined สองชื่อมาชนกัน แต่กลับยอมให้ System-Generated ชนกับ User-Defined ได้โดยไม่มีปัญหา?</p>
    <div class="tip"><strong>เฉลย:</strong> System-Generated Signal (เช่น <code>#1022</code>) เป็นเพียงชื่อชั่วคราวที่ระบบตั้งให้เมื่อยังไม่มีใครกำหนด จึงถูกแทนที่ได้เสมอโดยไม่เสียข้อมูลที่มีความหมาย แต่ User-Defined Signal สองชื่อถือเป็นเจตนาของผู้ออกแบบทั้งคู่ ระบบจึงไม่กล้าตัดสินใจแทนว่าจะใช้ชื่อไหน เพราะอาจทำให้วงจรสองส่วนที่ควรแยกกันถูกรวมสัญญาณผิดโดยไม่ตั้งใจ</div>

    <div class="page-nav">
        <a href="worksheet-02.html">← ก่อนหน้า: บทที่ 2</a>
        <a href="worksheet-04.html">ถัดไป: บทที่ 4 →</a>
    </div>'''

BODY[4] = '''    <h1>บทที่ 4: การจัดสรรเขตข้อมูลแผงวงจร (Fields) และควบคุมการแสดงผลด้วยเลเยอร์ (Levels)</h1>
    <p class="lead">จัดระเบียบชีทที่มีอุปกรณ์จำนวนมากด้วย Field สำหรับกลุ่ม HLA/Location และ Level สำหรับคุมการแสดงผล</p>

    <div class="objectives">
        <p>วัตถุประสงค์การเรียนรู้</p>
        <ol>
            <li>เพื่อสร้างพื้นที่เขตข้อมูล (Field) บนหน้าแบบ เพื่อบังคับให้อุปกรณ์ที่วางอยู่ภายในเขตนี้ได้รับการสืบทอดรหัสกลุ่ม Higher-Level Assignment (HLA) และ Location จากแผ่นงานหรือเขต Field โดยอัตโนมัติ</li>
            <li>เพื่อแยกประเภทและจัดลำดับชั้นเอกสารระบบวงจร กราฟิก และข้อความประกอบแบบ ลงบนระบบชั้นเลเยอร์ (Levels) ต่างๆ ได้สูงสุด 256 ระดับ</li>
            <li>เพื่อตั้งค่าจำกัดการเข้าถึงแผ่นงานแบบอ่านอย่างเดียว (Read-Only Level) ให้กับข้อมูลรูปทรงกราฟิกเสรีและข้อความประกอบ เพื่อป้องกันพนักงานร่วมงานทำการแก้ไขข้อมูลโดยไม่ได้ตั้งใจ</li>
        </ol>
    </div>

    <h2>1. Field: เขตที่สืบทอด HLA/Location อัตโนมัติ</h2>
    <p>
        <strong>Field</strong> คือพื้นที่บนชีทที่ใช้รวม Device ที่มี HLA และ/หรือ Location เดียวกันเข้าไว้ในกรอบเดียวกัน
        เพื่อให้ผังวงจรอ่านง่ายขึ้นเวลามีหลายระบบย่อยอยู่บนชีทเดียว สร้างได้จาก <strong>Insert → Field</strong>
        และใช้กฎการวาง (Settings → Placement → Rules) ชุดเดียวกับที่ใช้กับ Sheet
    </p>
    <p>
        Device ใดก็ตามที่วางลงในเขต Field จะรับค่า HLA/Location ของ Field นั้นไปอัตโนมัติ เหมือนที่ Device รับค่าจาก
        Sheet Header ตามที่เรียนในบทที่ 1 — ต่างกันตรงที่ Field ใช้แบ่งเขตย่อยๆ <em>ภายใน</em> ชีทเดียวกันได้
        โดยไม่ต้องแยกไปคนละชีท
    </p>

    <div class="tip">
        <strong>Tip:</strong> ใช้ Field เมื่อชีทเดียวมีหลายระบบย่อยปนกัน (เช่น วงจรควบคุมมอเตอร์ 2 ตัวบนชีทเดียว) แทนที่จะแยกชีท
        เพิ่มโดยไม่จำเป็น — ลด HLA/Location ผิดพลาดจากการตั้งมือทีละ Device
    </div>

    <h2>2. Levels: จัดชั้นการแสดงผลได้สูงสุด 256 ระดับ</h2>
    <p>
        Object ทุกชนิดบนชีท (เส้นเชื่อมต่อ กราฟิก ข้อความ) วางอยู่บน Level ใดระดับหนึ่งเสมอ — เรียก Level Manager ด้วยคีย์ลัด
        <code>L</code> เพื่อสลับเปิด/ปิดการแสดงผลของแต่ละระดับ มีประโยชน์มากเวลาต้องพิมพ์เอกสารหลายภาษา หรือทำ Export
        ที่ต้องซ่อนบาง Layer ออกไป
    </p>
    <table>
        <tr><th>ประเภท Object</th><th>ตัวอย่างที่อยู่บน Level</th></tr>
        <tr><td>Symbol เต็มรูป</td><td>กราฟิก + ข้อความของ Symbol ทั้งชุด</td></tr>
        <tr><td>กราฟิกล้วน</td><td>ส่วนกราฟิกหรือบางส่วนของ Symbol</td></tr>
        <tr><td>Text Placeholder ของ Symbol</td><td>ช่องข้อความที่ผูกกับ Symbol</td></tr>
        <tr><td>Free Graphic / Free Text</td><td>รูปวาดหรือข้อความอิสระที่ไม่ผูกกับ Symbol</td></tr>
        <tr><td>เส้นเชื่อมต่อ</td><td>เส้น Connection กราฟิก (ไม่รวม Cable/Wire เดี่ยว)</td></tr>
    </table>
    <p>
        ปุ่มลัดในหน้าต่าง Level Manager ช่วยสลับมุมมองได้เร็ว: "Display all levels" / "Display only used levels" และบันทึก/โหลด
        ชุดค่า Level เป็นไฟล์ <code>*.vis</code> ได้ — ตั้งค่าแยกกันได้สำหรับ Print, Print Preview, PDF-Export และ WebView-Export
        (.svg) โดยค่าที่ตั้งจะใช้เฉพาะตอน Export นั้นๆ แล้วกลับไปใช้ค่า Level เดิมของโปรเจกต์ต่อ
    </p>

    <h2>3. Read-Only Level: ล็อกกราฟิกเสรีไม่ให้แก้โดยไม่ตั้งใจ</h2>
    <p>
        Level หมายเลข <strong>253</strong> ถูกจองไว้เป็น "Read-only Level" โดยเฉพาะ — Free Graphic หรือ Free Text ใดที่ย้ายไปอยู่บน
        Level นี้จะไม่สามารถถูกเลือกหรือแก้ไขได้อีก จนกว่าจะปิดโหมดนี้
    </p>
    <ol class="steps">
        <li>ย้าย Object ที่ต้องการล็อกไปยัง Level 253</li>
        <li>เปิด Tools → Settings → Graphic</li>
        <li>เปิดใช้งานตัวเลือก <strong>"Use read-only level"</strong> (มีปุ่มลัดให้เปิด/ปิดเร็วในหน้าเดียวกัน)</li>
    </ol>

    <div class="note">
        <strong>ข้อควรระวัง:</strong> Read-Only Level ป้องกันการแก้ "โดยไม่ตั้งใจ" เท่านั้น ไม่ใช่ระบบ Permission จริงจัง —
        ผู้ใช้ที่รู้วิธีปิด Settings ยังแก้ไขได้อยู่ เหมาะกับกันความผิดพลาดในทีมเดียวกัน ไม่ใช่ควบคุมสิทธิ์ข้ามทีม
    </div>

    <h2>ตัวอย่างฝึกทำ</h2>
    <p><strong>โจทย์:</strong> สร้าง Field บนชีทเดิม 1 กรอบ ตั้ง HLA ให้ต่างจาก Sheet Header แล้ววาง Device 2 ตัวลงในกรอบนั้น ตรวจสอบว่า Item Designation ของทั้งสองตัวสืบทอดค่าจาก Field ไม่ใช่จาก Sheet</p>
    <p><strong>คำถามฝึกคิด:</strong> ทำไมข้อความหมายเหตุ (Free Text) บนกรอบชื่อเรื่อง (Title Block) ของทุกชีทถึงมักถูกใส่ไว้บน Read-Only Level เสมอ?</p>
    <div class="tip"><strong>เฉลย:</strong> ข้อมูลใน Title Block เช่น ชื่อบริษัท เลขแบบ มาตรฐานที่ใช้ ต้องเหมือนกันทุกชีทในโปรเจกต์ ถ้าใครบังเอิญคลิกโดนแล้วขยับหรือแก้ข้อความผิด จะทำให้เอกสารทั้งชุดดูไม่เป็นมาตรฐานเดียวกัน การล็อกไว้ที่ Level 253 ป้องกันอุบัติเหตุแบบนี้โดยที่ยังเปิดดูข้อมูลได้ตามปกติ</div>

    <div class="page-nav">
        <a href="worksheet-03.html">← ก่อนหน้า: บทที่ 3</a>
        <a href="worksheet-05.html">ถัดไป: บทที่ 5 →</a>
    </div>'''

BODY[5] = '''    <h1>บทที่ 5: การจัดการตรรกะสัญญาณและการสืบค้นทางวิศวกรรม (Signals &amp; Signal Tree)</h1>
    <p class="lead">ตามรอยสัญญาณไฟฟ้าข้ามหลายสิบชีทได้โดยไม่หลุดจุดไหน ด้วย Signal Tree และ Signal Cross-Reference</p>

    <div class="objectives">
        <p>วัตถุประสงค์การเรียนรู้</p>
        <ol>
            <li>เพื่อวิเคราะห์ความแตกต่างและการเดินทางสืบทอดตรรกะสัญญาณระหว่างสัญญาณที่ระบบตั้งให้อัตโนมัติ (System-Generated Signals เช่น <code>#1022</code>) กับสัญญาณที่วิศวกรกำหนดเอง (User-Defined Signals)</li>
            <li>เพื่อใช้งานแผนผังโครงสร้างสัญญาณ (Signal Tree) ในการสืบค้น ไฮไลต์ระบุเส้นทาง และติดตามตรรกะสัญญาณไฟฟ้าทั้งหมดในแผ่นงานโปรเจกต์</li>
            <li>เพื่อเชื่อมโยงและนำทางสัญญาณข้ามหน้าแบบวงจร (Signal Cross-Reference / Sheet References) ผ่านกล่องข้อความอ้างอิงและตารางปลายทางแบบออนไลน์</li>
        </ol>
    </div>

    <h2>1. System-Generated vs. User-Defined Signals</h2>
    <p>
        ทุก Connection ที่สร้างขึ้นจะได้สัญญาณติดมาด้วยเสมอ ถ้าไม่มีใครตั้งชื่อ ระบบจะสร้าง <strong>System-Generated Signal</strong>
        ให้อัตโนมัติ (รูปแบบ <code>#1022</code>) — ถ้า Connection นั้นไปแตะพินที่มีสัญญาณอยู่แล้ว สัญญาณเดิมจะถูกส่งต่อมาให้
        แต่ถ้าพินยังว่าง สัญญาณจะถูกดึงมาจาก Connection แทน
    </p>
    <p>
        <strong>User-Defined Signal</strong> คือชื่อที่วิศวกรตั้งเอง เปลี่ยนชื่อได้ตลอดเวลา และมีสิทธิ์เหนือกว่า
        System-Generated เสมอเมื่อมาเจอกัน (ตามที่เรียนในบทที่ 3) — ตั้งชื่อได้ 3 จุด: Connection Properties,
        Symbol Properties หรือ Device Properties
    </p>

    <h2>2. Signal Tree: มองเห็นสัญญาณทั้งโปรเจกต์ในที่เดียว</h2>
    <p>
        Signal Tree คือ Tree View พิเศษที่รวมสัญญาณทั้งหมดของโปรเจกต์ไว้ที่เดียว แบ่งเป็นสัญญาณที่กำหนดล่วงหน้า
        (Predefined — โหลดจากไฟล์ XML ด้วยคำสั่ง "Load signal structure") และสัญญาณที่เกิดขึ้นจริงระหว่างออกแบบ
    </p>
    <table>
        <tr><th>ฟังก์ชัน</th><th>ใช้ทำอะไร</th></tr>
        <tr><td>Highlight / Highlight Conductor Logic Lines</td><td>ไฮไลต์ทุก Object ที่ใช้สัญญาณนี้ในโปรเจกต์ ผลลัพธ์ยังโผล่ใน Results Window ให้ดับเบิลคลิกกระโดดไปดูได้</td></tr>
        <tr><td>Place / Assign signal to selection</td><td>ลาก Signal จาก Tree ไปกำหนดให้ Object ที่เลือกไว้บนชีทได้โดยตรง (Drag &amp; Drop)</td></tr>
        <tr><td>Signal Format</td><td>ตั้งรูปแบบชื่อสัญญาณอัตโนมัติจาก Placeholder เช่น <code>&lt;.Sheet&gt;</code> (ชื่อชีท) หรือ <code>&lt;.GRID&gt;</code> (พิกัดกริดบนชีท)</td></tr>
        <tr><td>Signal Properties</td><td>เปลี่ยนชื่อสัญญาณหรือกำหนด Attribute เพิ่มเติม เช่น Connection Class Panel</td></tr>
    </table>
    <p>ยกเลิกการไฮไลต์ทั้งหมดได้เร็วๆ ด้วย <code>Shift+F6</code></p>

    <h2>3. Signal Cross-Reference: อ้างอิงสัญญาณข้ามชีท</h2>
    <p>
        เมื่อวงจรกระจายอยู่หลายสิบชีท ใช้สัญลักษณ์ Cross-Reference (แท็บ Misc ใน Database Window) เพื่อบอกว่าสัญญาณเส้นนี้
        "ไปโผล่ต่อที่ชีทไหน" — Symbol ต้นทาง (Source) กับปลายทาง (Destination) ต้องเป็นชนิดเดียวกันเสมอ มี 4 รูปแบบ:
    </p>
    <table>
        <tr><th>ชนิด</th><th>พฤติกรรม</th></tr>
        <tr><td>Point to Point (manual)</td><td>1 Source ต่อ 1 Destination กำหนดคู่กันเองผ่านเมนู "Sheet Reference..." (<code>Shift+R</code>)</td></tr>
        <tr><td>Star (manual)</td><td>1 Source อ้างถึงได้หลาย Destination กำหนดคู่กันเองผ่าน Sheet References เช่นกัน</td></tr>
        <tr><td>Auto Point to Point</td><td>ระบบจับคู่ Source-Destination อัตโนมัติทันทีที่สัญญาณชื่อเดียวกันปรากฏบนชีทลูกในโครงสร้างโปรเจกต์ — ใช้เมื่อสัญญาณวนเป็นลูป และสัญญาณออกจากชีทได้แค่ครั้งเดียว</td></tr>
        <tr><td>Auto Star</td><td>เหมือน Auto Point to Point แต่ 1 Source อ้างได้หลาย Destination พร้อมกัน</td></tr>
    </table>

    <div class="tip">
        <strong>Tip:</strong> เลือกแบบ Auto เมื่อโครงสร้างโปรเจกต์เป็นลำดับชั้นชัดเจน (Sheet ลูก-แม่) เพื่อลดงานจับคู่มือ
        ส่วนแบบ Manual (Point-to-Point/Star) เหมาะกับกรณีที่ต้องกำหนดปลายทางเองเพราะไม่ตรงตามลำดับชั้นปกติของโปรเจกต์
    </div>

    <h2>ตัวอย่างฝึกทำ</h2>
    <p><strong>โจทย์:</strong> สร้างสัญญาณ User-Defined ชื่อ <code>K1_COIL</code> บนชีท 1 แล้วต่อสัญญาณเดียวกันไปโผล่ที่ชีท 2 ด้วย Cross-Reference แบบ Auto Point to Point จากนั้นใช้ Signal Tree ค้นหาชื่อสัญญาณนี้และกด Highlight ดูผล</p>
    <p><strong>คำถามฝึกคิด:</strong> ทำไมโปรเจกต์ที่มีหลายชีทถึงควรใช้ Signal Cross-Reference แทนการไล่ดู Wire ทีละเส้นด้วยตา?</p>
    <div class="tip"><strong>เฉลย:</strong> เมื่อสัญญาณเดียวกันปรากฏในหลายชีท การไล่ตาดูทีละเส้นจะพลาดง่ายและช้ามากเมื่อโปรเจกต์ใหญ่ขึ้น Cross-Reference จะอัปเดตอัตโนมัติทุกครั้งที่แก้วงจร ทำให้มั่นใจได้ว่าเอกสารตรงกับแบบจริงเสมอ ไม่ต้องพึ่งความจำของผู้ออกแบบ</div>

    <div class="page-nav">
        <a href="worksheet-04.html">← ก่อนหน้า: บทที่ 4</a>
        <a href="worksheet-06.html">ถัดไป: บทที่ 6 →</a>
    </div>'''

BODY[6] = '''    <h1>บทที่ 6: การปรับปรุงแอตทริบิวต์ในวงกว้างอย่างรวดเร็ว (Global Search &amp; Replace)</h1>
    <p class="lead">แก้ข้อความหรือแอตทริบิวต์ทีละร้อยจุดในคลิกเดียว ด้วยฟีเจอร์ Search and Replace ที่เพิ่มเข้ามาใน E3.series 2026</p>

    <div class="objectives">
        <p>วัตถุประสงค์การเรียนรู้</p>
        <ol>
            <li>เพื่อใช้งานกล่องสืบค้นขั้นสูง ค้นหาข้อความเสรีหรือ Attributes ของอุปกรณ์ข้ามแผ่นงานได้อย่างถูกต้องและปลอดภัย</li>
            <li>เพื่อเรียกใช้งานคำสั่ง Search &amp; Replace (คีย์ลัด <code>Ctrl+H</code>) เพื่อปรับปรุง เปลี่ยนแปลง หรือล้างข้อมูลแอตทริบิวต์ของอุปกรณ์พร้อมกันทั้งโครงการ (Replace All) ในขั้นตอนเดียว</li>
            <li>เพื่อใช้ประโยชน์จากฟังก์ชันประสานคำค้นหา ที่ทำให้การระบุแอตทริบิวต์ของประเภท Component สามารถสืบค้นไปยังอุปกรณ์หรือตัว Device จริงที่ใช้ในแบบได้ทันที</li>
        </ol>
    </div>

    <h2>1. ค้นหาข้อความและ Attribute ข้ามแผ่นงาน</h2>
    <p>
        ค้นหาแบบพื้นฐานยังคงใช้ <code>F3</code> ได้เหมือนเดิม (ค้นข้อความ/ค่า Attribute ในโปรเจกต์) แต่ตั้งแต่ E3.series 2026
        ผลการค้นหานี้ <strong>แก้ไขต่อได้ทันที</strong> ด้วยคำสั่งใหม่ Search and Replace โดยไม่ต้องไล่เปิดทีละ Object เอง
    </p>
    <div class="note">
        <strong>ข้อควรรู้ก่อนค้นหา:</strong> ระบบจะไม่แสดงบาง Text/Attribute ที่ไม่ปลอดภัยต่อการแก้ไขแบบอัตโนมัติ:
        Text ประเภทระบบ (System text types) และ Text ที่ผูกกับ Attribute จะไม่ปรากฏในรายการค้นหา ส่วน Attribute
        จะแสดงเฉพาะประเภท <code>String</code> ที่เจ้าของสามารถเปลี่ยนค่าได้เท่านั้น — Attribute ของระบบ หรือที่แก้ได้เฉพาะผ่าน
        Script จะถูกกันออกไปโดยอัตโนมัติ
    </div>

    <h2>2. Search and Replace (Ctrl+H) — แก้ทั้งโปรเจกต์ในขั้นตอนเดียว</h2>
    <p>เรียกใช้ได้จากเมนู Edit, Toolbar "Display" หรือคีย์ลัด <code>Ctrl+H</code> โดยตรง</p>
    <ol class="steps">
        <li>เลือกก่อนว่าจะค้นหา <strong>Text</strong> หรือ <strong>Attribute</strong></li>
        <li>เลือก Type(s) ที่ต้องการ: ทั้งหมด (<code>&lt;All&gt;</code>), บางประเภท หรือประเภทเดียว</li>
        <li>กรอกคำค้นหาใน <strong>Find what</strong> — เลือกจากรายการที่ระบบเสนอให้ (ไม่รองรับ Wildcard)</li>
        <li>กรอกค่าที่ต้องการแทนที่ใน <strong>Replace with</strong></li>
        <li>ตรวจสีในหน้าต่าง Output: ค่าสีน้ำเงินคือแก้ได้จริง ค่าสีดำคือแก้ไม่ได้ (ล็อกอยู่หรือเป็นชนิด Object ที่ระบบห้ามแก้)</li>
        <li>สั่ง Replace All เมื่อมั่นใจแล้วว่าผลลัพธ์ตรงตามต้องการ</li>
    </ol>

    <div class="note">
        <strong>ข้อควรระวัง:</strong> Object บางชนิดถูกล็อกไว้ไม่ให้ Replace ได้แม้จะเจอในผลค้นหา ได้แก่ Component/Component
        Pin, Cable, Symbol/Symbol Pin, Wire, Slot, Contour, Functional Unit/Port, State และ Bundle — เห็นในผลค้นหาได้
        แต่แก้ไม่ได้ผ่านคำสั่งนี้ ต้องไปแก้ที่ Database Editor โดยตรง (บทที่ 9)
    </div>

    <h2>3. ค้นหา Attribute ของ Component แล้วเจอ Device จริงในแบบทันที</h2>
    <p>
        ตั้งแต่ 2026 การค้นหา Attribute ที่มีเจ้าของเป็น <strong>Component, Cable Type หรือ Model</strong> จะดึงผลลัพธ์ครอบคลุมไปถึง
        <strong>Device</strong> ทุกตัวที่มี Attribute นั้นด้วย ไม่ใช่แค่ Component ต้นแบบในฐานข้อมูล — มีประโยชน์มากเวลาจะเช็คว่า
        ค่า Attribute ของ Device ตัวใดตัวหนึ่งในแบบถูกแก้ให้ต่างจากค่ามาตรฐานของ Component หรือไม่
    </p>

    <div class="tip">
        <strong>Tip:</strong> ใช้ฟีเจอร์นี้ตรวจ QA ก่อนปิดงาน — ค้นหา Attribute เช่น "Manufacturer" ของ Component ต้นแบบ
        แล้วดูว่ามี Device ตัวไหนในแบบที่ค่าเพี้ยนไปจากมาตรฐานบ้าง โดยไม่ต้องไล่เปิดทีละตัว
    </div>

    <h2>ตัวอย่างฝึกทำ</h2>
    <p><strong>โจทย์:</strong> ค้นหา Attribute ชื่อ "Manufacturer" แบบ <code>&lt;All&gt;</code> Type ในโปรเจกต์ตัวอย่าง แล้วลอง Replace ค่าที่ผิดให้ถูกต้องทั้งหมดในคำสั่งเดียว</p>
    <p><strong>คำถามฝึกคิด:</strong> ทำไม Search and Replace ถึงไม่รองรับ Wildcard (เช่น <code>*</code> หรือ <code>?</code>) ทั้งที่โปรแกรมค้นหาทั่วไปมักมีให้ใช้?</p>
    <div class="tip"><strong>เฉลย:</strong> เพราะคำสั่งนี้ทำ Replace All ทั่วทั้งโปรเจกต์ในขั้นตอนเดียว ถ้าใช้ Wildcard ผิดพลาดอาจกวาดแก้ Text/Attribute ที่ไม่ได้ตั้งใจจำนวนมากพร้อมกัน โดยไม่มีขั้นตอนยืนยันทีละรายการ — การบังคับให้เลือกคำค้นหาที่ตรงเป๊ะจากรายการที่ระบบเสนอ ช่วยลดความเสี่ยงที่จะ Replace ผิดเป้าไปทั้งโปรเจกต์</div>

    <div class="page-nav">
        <a href="worksheet-05.html">← ก่อนหน้า: บทที่ 5</a>
        <a href="worksheet-07.html">ถัดไป: บทที่ 7 →</a>
    </div>'''

BODY[7] = '''    <h1>บทที่ 7: การเขียนบล็อกขั้วต่อสายไฟและการคำนวณผังออนไลน์ (Terminals &amp; Terminal Plan)</h1>
    <p class="lead">จาก Terminal Strip บนชีท สู่ตารางขั้วต่อที่คำนวณปลายทางในตู้/นอกตู้ให้อัตโนมัติ</p>

    <div class="objectives">
        <p>วัตถุประสงค์การเรียนรู้</p>
        <ol>
            <li>เพื่อกำหนด สร้าง และจัดสรรขั้วต่อสายไฟ (Terminal Block) ควบคุมความปลอดภัยของระบบจัดเรียงพินและการต่อสายเคเบิลสะพานไฟ (Jumper)</li>
            <li>เพื่อสร้างแผ่นงานแผนผังตารางขั้วสายไฟออนไลน์ (Online Terminal Plan) ที่จะคำนวณเป้าหมายปลายทางการต่อเชื่อมทั้งภายใน (Internal Target) และภายนอก (External Target) ตู้โดยอัตโนมัติ</li>
            <li>เพื่อใช้งานคำสั่งสะพานเชื่อมขั้วไฟแบบกราฟิกและตรรกะจัมเปอร์ (Jumper Symbols / Jumper for Terminal) และสร้างรายงานออกมาบนเทอร์มินอลแพลนจริง</li>
        </ol>
    </div>

    <h2>1. Terminal Block: ขั้วต่อและความปลอดภัยของการจัดเรียงพิน</h2>
    <p>
        ทบทวนจากบทที่ 1: <strong>Terminal</strong> เป็น Component ชนิดพิเศษ วางจาก Database Window ครั้งแรกจะสร้าง Device
        ชนิด <strong>Terminal Strip</strong> ให้อัตโนมัติ วาง Terminal ชนิดเดียวกันซ้ำจะเข้า Strip เดิม ส่วนชนิดต่างกันจะแยก
        Strip ใหม่ให้เอง ระบบตรวจจำนวนสายที่เข้าขั้วและ Cross-Section ให้ตลอดเวลาตามที่เรียนในบทที่ 3 (Online Checks)
    </p>
    <p>
        <strong>Jumper</strong> คือสายสะพานไฟเชื่อมระหว่างขั้วต่อสองขั้วขึ้นไปในสตริปเดียวกัน ใช้เมื่อต้องกระจายไฟเส้นเดียวไปหลายขั้ว
        (เช่น กระจายไฟบวกไปหลายวงจรจากขั้วต้นทางเดียว) — นิยาม Jumper ได้สองแบบ: <em>วาดเส้นเชื่อมต่อกราฟิก</em> ระหว่างขั้วในสตริป
        เดียวกันโดยตรง หรือกำหนดผ่าน <em>Attribute "Jumper for Terminal"</em> บนพิน โดยไม่ต้องวาดเส้นกราฟิกเลย
    </p>

    <h2>2. Online Terminal Plan: อีกมุมมองหนึ่งของ Schematic</h2>
    <p>
        Terminal Plan ไม่ใช่เอกสารแยกต่างหาก แต่เป็น "อีกมุมมอง" ของวงจรเดียวกัน — แก้ที่ Terminal Plan จะอัปเดตกลับไปที่
        Schematic ทันที และกลับกัน สร้างได้ครั้งเดียวจากเมนูหลัก, Toolbar Placement หรือคลิกขวาที่ Terminal Strip ใน Device Tree
    </p>
    <ol class="steps">
        <li>เลือกชื่อ Sheet, Sheet Format และ Table Symbol ที่จะใช้แสดงผล</li>
        <li>เลือก Sorting Criteria: เรียงตามลำดับใน Device Tree (None), ตามหมายเลขขั้ว (Pin Name), ตามการจัดกลุ่ม Jumper/Cable (Cable or Jumper), ตามพิกัดการวางจริงบนแบบ (Placement) หรือกำหนดลำดับเองด้วยไฟล์ Sort (<code>*.def</code>)</li>
        <li>ตั้งค่า Internal/External Definition — กำหนดว่า Device ปลายทางจะนับเป็น "Internal" (ในตู้เดียวกับ Terminal Strip) หรือ "External" (นอกตู้) โดยเทียบจาก Assignment เท่านั้น, Location เท่านั้น หรือทั้งคู่ต้องตรงกัน</li>
        <li>สั่ง Generate — Internal/External Target ทุกช่องคำนวณให้อัตโนมัติจากผังจริง ไม่ต้องกรอกมือ</li>
    </ol>
    <p>
        ตัวเลือกจัดรูปแบบที่ใช้บ่อย ได้แก่ <strong>Autocompress</strong> (ย่อจำนวนแถวให้กระชับที่สุด), <strong>Combine same pin
        names</strong> (รวมทุกเส้นที่ต่อขั้วชื่อเดียวกันไว้แถวเดียว) และ <strong>Only user-defined signals</strong> (ซ่อนสัญญาณ
        System-Generated ที่ขึ้นต้นด้วย <code>#</code> ไม่ให้รกตาราง)
    </p>

    <div class="note">
        <strong>ข้อควรรู้:</strong> ถ้า Model ของ Terminal ถูกวางลงบน Panel Sheet แล้ว (เรียนต่อในหน้า Panel) จะ "ย้ายแถว"
        โดยตรงในหน้า Terminal Plan หรือ Device Tree ไม่ได้อีก — ต้องย้ายตำแหน่ง Model บน Panel เท่านั้น แล้วลำดับใน
        Terminal Plan/Device Tree จะตามไปเอง
    </div>

    <h2>3. Jumper และรายงานเทอร์มินอลแพลน</h2>
    <p>ระบบตีความ Jumper ในผังได้หลายแบบ เลือกตั้งค่าตามลักษณะงานจริง:</p>
    <table>
        <tr><th>โหมด</th><th>พฤติกรรม</th></tr>
        <tr><td>Jumpers by Connections</td><td>ขั้วที่มีเส้นเชื่อมต่อถึงกันจริงในผัง จะแสดงเป็น Jumper อัตโนมัติ</td></tr>
        <tr><td>In Line</td><td>รวมทุกพินที่เชื่อมกันแบบกราฟิก (รวมถึงพินสมมูลข้ามกัน) เป็นแถวเดียว มองเป็นบล็อก Jumper รวด</td></tr>
        <tr><td>Jumpers by Attributes</td><td>กำหนด Jumper ผ่าน Attribute "Jumper for Terminal" บนตัวนำ โดยไม่ต้องมีเส้นกราฟิก</td></tr>
        <tr><td>No Jumpers</td><td>ปิดการแสดงผล Jumper ทั้งหมดในแพลนนี้</td></tr>
    </table>
    <p>
        แก้ไขค่าตรงๆ ในตาราง Terminal Plan ได้เลย เช่น หมายเลขขั้ว สัญญาณ หรือชื่อ Device ปลายทาง ผ่านเมนู Properties —
        ค่าจะอัปเดตกลับไปที่ Schematic ทันที ทำให้ Terminal Plan ใช้เป็นทั้งเครื่องมือแก้ไขและรายงานสำหรับส่งช่างเดินสายจริงได้ในตัว
        (ต่อยอดการส่งออกเป็น PDF/Excel ในบทที่ 10)
    </p>

    <h2>ตัวอย่างฝึกทำ</h2>
    <p><strong>โจทย์:</strong> สร้าง Terminal Strip 6 ขั้วจาก Schematic ต่อ Jumper แบบ Jumpers by Connections เชื่อม 3 ขั้วแรกเข้าด้วยกัน แล้ว Generate Terminal Plan โดยตั้ง Sorting Criteria เป็น Pin Name และเปิด Autocompress</p>
    <p><strong>คำถามฝึกคิด:</strong> ทำไม Internal/External Target ในตาราง Terminal Plan ถึงคำนวณจาก Assignment/Location แทนที่จะให้ผู้ใช้พิมพ์ระบุเองตรงๆ?</p>
    <div class="tip"><strong>เฉลย:</strong> เพราะ Assignment/Location ของทุก Device ถูกกำหนดไว้แล้วตั้งแต่ขั้นตอนวางวงจร (บทที่ 1 และ 4) การให้ระบบคำนวณ Internal/External จากค่านี้โดยตรงทำให้ตาราง Terminal Plan อัปเดตอัตโนมัติทุกครั้งที่แก้ผัง ไม่มีความเสี่ยงที่ตัวเลขในรายงานจะไม่ตรงกับแบบจริง ต่างจากการพิมพ์มือที่ต้องมาคอยแก้ตามทุกครั้งที่ผังเปลี่ยน</div>

    <div class="page-nav">
        <a href="worksheet-06.html">← ก่อนหน้า: บทที่ 6</a>
        <a href="worksheet-08.html">ถัดไป: บทที่ 8 →</a>
    </div>'''

BODY[8] = '''    <h1>บทที่ 8: การจัดการวงจรย่อยและโมดูลโครงสร้างใช้ซ้ำ (Subcircuits)</h1>
    <p class="lead">แปลงวงจรที่ใช้บ่อยให้กลายเป็นโมดูลสำเร็จรูป วางซ้ำได้ในขั้นตอนเดียวทุกโปรเจกต์</p>

    <div class="objectives">
        <p>วัตถุประสงค์การเรียนรู้</p>
        <ol>
            <li>เพื่อกำหนดพิกัดจุดกำเนิดพิกัดต้นฉบับ (Origin for subcircuit) ให้กับแผงวงจรส่วนที่ใช้งานบ่อย เพื่อจัดเตรียมโครงสร้างให้ระบบนำกลับมาผลิตซ้ำได้</li>
            <li>เพื่อทำการส่งออกแผงวงจรชุดดังกล่าว ออกไปเป็นไฟล์ภายนอกรูปแบบไฟล์ <code>.e3p</code> (Subcircuit File)</li>
            <li>เพื่อบันทึกและนำเข้าโครงสร้างวงจรย่อย <code>.e3p</code> กลับเข้ามาจัดเก็บไว้ในฐานข้อมูล Component Database เพื่อให้วิศวกรสามารถเลือกวางวงจรสมบูรณ์ได้แบบขั้นตอนเดียว (Place Database Subcircuit)</li>
        </ol>
    </div>

    <p>
        <strong>Subcircuit</strong> คือส่วนหนึ่งของแบบ (ครอบคลุมได้ตั้งแต่พื้นที่ที่เลือกไว้ ไปจนถึงทั้งชีท) ที่นำไปใช้ซ้ำได้สองทาง:
        ส่งออก/นำเข้าเป็นไฟล์ภายนอกนามสกุล <code>.e3p</code> หรือบันทึกลงฐานข้อมูลกลางเป็น Component ชนิด "Subcircuit" ถาวร
    </p>

    <h2>1. กำหนด Origin ก่อนแปลงเป็นวงจรใช้ซ้ำ</h2>
    <p>
        ก่อน Export ทุกครั้ง ควรกำหนด <strong>Origin</strong> (จุดอ้างอิงของ Subcircuit) ไว้ก่อน — จุดนี้คือตำแหน่งที่ Subcircuit
        จะ "เกาะติดเคอร์เซอร์" เวลานำกลับมา Import ใหม่ในโปรเจกต์อื่น ถ้าไม่กำหนด ระบบจะใช้ค่าเริ่มต้นซึ่งอาจไม่ตรงกับจุดที่วิศวกร
        ต้องการอ้างอิงเวลาวางจริง
    </p>
    <ul>
        <li><strong>Place origin for subcircuit</strong> — เลือกตำแหน่งจุดอ้างอิงบนพื้นที่ที่จะ Export</li>
        <li><strong>Display origin for subcircuit</strong> — แสดงจุดอ้างอิงปัจจุบันเพื่อตรวจสอบก่อน Export จริง</li>
    </ul>

    <div class="tip">
        <strong>Tip:</strong> เลือก Origin ไว้ที่มุมซ้ายบนของวงจร หรือจุดที่วิศวกรมักคลิกวางก่อนเสมอ (เช่น จุดจ่ายไฟเข้า) จะทำให้
        คนอื่นในทีมนำ Subcircuit นี้ไปวางต่อได้เข้าใจง่ายและตรงตำแหน่งโดยไม่ต้องขยับแก้ทีหลัง
    </div>

    <h2>2. Export วงจรออกเป็นไฟล์ .e3p</h2>
    <ol class="steps">
        <li>เลือกพื้นที่/ชีทที่จะแปลงเป็น Subcircuit บน Project Window หรือเลือกวัตถุบนชีทโดยตรง</li>
        <li>Main Menu → File → Export → Drawing</li>
        <li>เลือก <strong>Include sheet border</strong> ถ้าต้องการเก็บกรอบชีทและ Sheet Text ไปด้วย หรือปิดไว้ถ้าต้องการแค่พื้นที่ที่เลือก</li>
        <li>เลือก <strong>Devices only</strong> หรือรวม <strong>Cables/Wires</strong> ไปด้วย ตามที่ต้องการให้ Subcircuit สมบูรณ์แค่ไหน</li>
        <li>เปิด <strong>Group objects</strong> ถ้าต้องการให้วัตถุทั้งหมดยังคงถูกจัดกลุ่มไว้ด้วยกันตอน Import กลับ</li>
        <li>บันทึกเป็นไฟล์ <code>.e3p</code></li>
    </ol>

    <h2>3. นำเข้า .e3p และบันทึกเป็น Component ชนิด Subcircuit</h2>
    <p>
        Import ไฟล์กลับได้จาก Main Menu → File → Import → Drawing — จุดเด่นของการใช้ <strong>Paste Extended</strong>
        คือ Subcircuit ที่ Import เข้ามาจะแวะพักที่ Clipboard ก่อน ให้แก้ไข/ปรับแต่งได้ก่อนค่อยรวมเข้าโปรเจกต์จริง
        ถ้าต้องการวางที่พิกัดเดิมเป๊ะเหมือนตอน Export ใช้คำสั่ง <strong>Place at original position</strong>
        (<code>Shift+O</code>)
    </p>
    <p>
        แต่ถ้าต้องการให้ทีมทั้งหมดเรียกใช้ Subcircuit นี้ได้ทุกโปรเจกต์โดยไม่ต้องแจกไฟล์ <code>.e3p</code> เอง ให้บันทึกมันเป็น
        <strong>Component ชนิด "Subcircuit"</strong> ในฐานข้อมูลกลางแทน (ทำผ่าน Database Editor — บทที่ 9) จากนั้นวิศวกรคนอื่น
        เพียงค้นหาใน Database Window แล้วลากวางจาก Database Window ได้เลย ระบบจะวาง "วงจรทั้งชุด" ให้ครบในขั้นตอนเดียว
        (Placing Database Subcircuit) เหมือนวางอุปกรณ์ชิ้นเดียวปกติ และยังแก้ไขต่อได้หลังวางถ้าจำเป็น
    </p>

    <div class="note">
        <strong>เปรียบเทียบสองวิธี:</strong> ไฟล์ <code>.e3p</code> เหมาะกับการแชร์ครั้งคราวหรือส่งให้ทีมนอกโปรเจกต์
        ส่วน Database Subcircuit เหมาะกับวงจรมาตรฐานที่ทีมใช้ซ้ำบ่อยและอยากให้ทุกคนดึงจากแหล่งเดียวกันเสมอ (ตรงหลักการ
        Shared Database เดียวกับที่เรียนเรื่อง Component ในบทที่ 9)
    </div>

    <h2>ตัวอย่างฝึกทำ</h2>
    <p><strong>โจทย์:</strong> เลือกวงจรควบคุมมอเตอร์มาตรฐาน 1 ชุดที่เคยวาดไว้ กำหนด Origin ที่จุดจ่ายไฟเข้า แล้ว Export เป็น <code>.e3p</code> จากนั้นเปิดโปรเจกต์ใหม่และ Import กลับด้วย Place at original position</p>
    <p><strong>คำถามฝึกคิด:</strong> ทำไมการ Import ผ่าน Paste Extended (แวะที่ Clipboard ก่อน) ถึงปลอดภัยกว่าการวางลงชีทตรงๆ ทันที?</p>
    <div class="tip"><strong>เฉลย:</strong> เพราะ Clipboard เป็นพื้นที่ชั่วคราวที่ยังไม่ผูกกับโปรเจกต์จริง วิศวกรตรวจสอบและแก้ไข Subcircuit ได้ก่อน เช่น เปลี่ยน Item Designation ให้ไม่ชนกับของเดิมในโปรเจกต์ปลายทาง ก่อนค่อยกดรวมเข้าแบบจริง ต่างจากการวางตรงๆ ที่ถ้าพบว่า Item Designation ชนกันจะต้องมาแก้ไขหลังวางไปแล้ว ซึ่งเสี่ยงต่อการตกหล่นบาง Device</div>

    <div class="page-nav">
        <a href="worksheet-07.html">← ก่อนหน้า: บทที่ 7</a>
        <a href="worksheet-09.html">ถัดไป: บทที่ 9 →</a>
    </div>'''

BODY[9] = '''    <h1>บทที่ 9: การพัฒนาชิ้นส่วนคลังและโมเดลอุปกรณ์ใหม่ใน DBE (Database Editor)</h1>
    <p class="lead">เมื่อของมาตรฐานไม่พอ ลงมือสร้าง Symbol และ Component เองใน Database Editor อย่างเป็นระบบ</p>

    <div class="objectives">
        <p>วัตถุประสงค์การเรียนรู้</p>
        <ol>
            <li>เพื่อเปิดใช้โหมดพัฒนาคลังอุปกรณ์ และสังเกตสัญลักษณ์ "E3.dbe" บน Title Bar เพื่อเริ่มกระบวนการจัดทำคลังข้อมูลอย่างเป็นทางการ</li>
            <li>เพื่อออกแบบสร้างสัญลักษณ์ (Symbol) ใหม่ โดยการวาดรูปกราฟิก จัดสิทธิ์ Nodes พินเชื่อมสาย ระบุ Text Place Holder และกำหนดจุดพิกัด Insertion Point (Symbol Origin)</li>
            <li>เพื่อเรียกใช้งาน Component Wizard ในการจับคู่เชื่อมโยง Symbol เข้ากับตัว Component จริง กำหนดตาราง Pin Properties และเขียนลำดับ Master/Slave Checklist ให้กับอุปกรณ์คอยล์และหน้าสัมผัสของรีเลย์อย่างครบถ้วน</li>
        </ol>
    </div>

    <h2>1. เข้าสู่โหมด Database Editor</h2>
    <p>
        เปิดได้จากคำสั่ง <strong>New Symbol</strong> หรือ <strong>New Component</strong> ในเมนูคลิกขวาของ Database Window
        (หรือใช้ Symbol/Component Edit ถ้าจะแก้ของเดิม) โปรแกรมจะเปิดหน้าต่างแยกใหม่ — จุดสังเกตสำคัญคือชื่อ
        <code>E3.dbe</code> ที่ปรากฏบน Title Bar ยืนยันว่ากำลังแก้ไข "ต้นแบบ" ในฐานข้อมูลจริง ไม่ใช่ Device ในโปรเจกต์
    </p>
    <div class="note">
        <strong>ข้อควรรู้:</strong> โหมด DBE กับโหมด Project แยกสีหน้าต่างให้ต่างกันชัดเจน และเปิดพร้อมกันได้ — แก้ไขใน DBE
        จะไม่กระทบ Device ที่วางไปแล้วในโปรเจกต์ที่เปิดคู่ขนานอยู่ จนกว่าจะสั่ง Update (ดูบทที่ 10) ก่อนสร้างใหม่ทุกครั้ง
        ค้นหาในฐานข้อมูลก่อนเสมอ อย่าสร้าง Symbol/Component ซ้ำกับที่มีอยู่แล้ว
    </div>

    <h2>2. ออกแบบ Symbol ใหม่ (Symbol Checklist)</h2>
    <ol class="steps">
        <li>กำหนด <strong>Symbol Properties</strong> — ชนิดและชื่อ Symbol</li>
        <li><strong>Insert Symbol Graphic</strong> — วาดรูปกราฟิกเอง หรือ Import จาก DXF/DWG ก็ได้ (กราฟิกนี้จะแก้ไขไม่ได้อีกในโหมด Project)</li>
        <li>วาง <strong>Nodes</strong> บนตำแหน่งที่ต้องการให้เส้น Connection เข้ามาต่อ — ต้องกำหนดทิศทางการเชื่อมต่อ (Connection Direction) และคำนึงถึง Working Grid ด้วย</li>
        <li>วาง <strong>Text Place Holder</strong> สำหรับข้อมูลที่ระบบหรือผู้ใช้จะเติมทีหลัง เช่น Item Designation</li>
        <li>ตรวจสอบ/กำหนด <strong>Space Requirement</strong> (พื้นที่ที่คลิกเลือก Symbol ได้ ค่าเริ่มต้น = ขนาดกราฟิกสูงสุด) และ <strong>Symbol Origin</strong> (จุด Insertion Point ตอนวางลงชีท)</li>
    </ol>

    <div class="tip">
        <strong>Tip:</strong> Nodes คือจุดที่กำหนดว่า Connection "เข้าได้จากทิศไหนบ้าง" — วาง Node ผิดทิศทางเป็นสาเหตุอันดับต้นๆ
        ที่ทำให้ Autoconnect (บทที่ 3) หาทางเชื่อมต่อ Symbol ตัวนี้ไม่เจอ ตรวจทิศทาง Node ให้ตรงกับหน้าสัมผัสจริงของอุปกรณ์เสมอ
    </div>

    <h2>3. Component Wizard และ Master/Slave Checklist (กรณีรีเลย์)</h2>
    <p>
        Symbol อย่างเดียวยังใช้งานจริงไม่ได้ ต้องผูกเข้ากับ <strong>Component</strong> ผ่าน Component Wizard ก่อน
        เลือกได้ว่าจะสร้าง <em>Component without Template</em> (กำหนดทุกอย่างเองใหม่หมด) หรือ <em>Component with Template</em>
        (ดึงโครงสร้าง/Attribute จาก Component ที่มีอยู่แล้วมาปรับแก้ — เร็วกว่าถ้ามีของใกล้เคียงอยู่แล้ว)
    </p>
    <p>ใน Pin Assignment ของ Wizard กำหนดชื่อพินแบบเรียงเลขอัตโนมัติได้ ไม่ต้องพิมพ์ทีละช่อง:</p>
    <table>
        <tr><th>รูปแบบที่กรอก</th><th>ผลลัพธ์</th></tr>
        <tr><td><code>1..10</code></td><td>เรียงเลข 1 ถึง 10 ต่อเนื่องอัตโนมัติ</td></tr>
        <tr><td><code>1,3,5,7,9,2,4,6,8,10</code></td><td>กำหนดลำดับเองทีละตัวคั่นด้วยจุลภาค</td></tr>
        <tr><td><code>2..9,12..19</code></td><td>ผสมสองรูปแบบเข้าด้วยกัน</td></tr>
    </table>

    <p>
        รีเลย์เป็นตัวอย่างคลาสสิกของ Component ที่ต้อง <strong>Master/Slave</strong> — เพราะขดลวด (Coil) กับหน้าสัมผัส
        (Contacts) เป็น Symbol คนละตัวที่ต้องแยกไปวางกันคนละจุดบนชีท (ตามที่ฝึกด้วยคีย์ลัด <code>N</code> ในบทที่ 2)
        แต่ทั้งหมดต้องอ้างอิงกลับไปเป็น "อุปกรณ์ตัวเดียวกัน" ในฐานข้อมูล:
    </p>
    <p><strong>Master/Slave Checklist:</strong></p>
    <ol class="steps">
        <li>เลือกชนิด Component และตั้งชื่อ</li>
        <li>เลือก Device Letter Code (เช่น K สำหรับรีเลย์)</li>
        <li>กรอก Component Properties</li>
        <li>วาง Symbol ทั้งหมดของอุปกรณ์นี้ (Coil + Contacts ทุกชุด)</li>
        <li>ตรวจ/กำหนดลำดับ Symbol (Symbol Order) — Symbol ตัวแรกในลำดับจะถูกใช้แสดงใน Preview Window เสมอ เว้นแต่กำหนด Preview Symbol แยกไว้</li>
        <li>Assign Pins ให้ครบทุก Symbol</li>
        <li>สร้าง Contact Arrangement หรือกำหนดความสัมพันธ์ Master/Slave ระหว่าง Coil กับ Contacts แต่ละชุด</li>
    </ol>

    <div class="note">
        <strong>ข้อควรรู้:</strong> Contact Arrangement ต้องมี Contact Arrangement Template Symbol กำหนดไว้ล่วงหน้าก่อนถึงจะสร้างได้
        — ถ้ายังไม่มี ต้องเตรียม Template Symbol นี้ก่อนเริ่มขั้นตอน Master/Slave Checklist
    </div>

    <h2>ตัวอย่างฝึกทำ</h2>
    <p><strong>โจทย์:</strong> สร้าง Symbol ขดลวดรีเลย์ 1 ตัว และ Symbol หน้าสัมผัส (Normally Open) อีก 1 ตัว จากนั้นใช้ Component Wizard แบบ Component without Template ผูกทั้งสอง Symbol เข้าเป็น Component เดียวกันด้วย Master/Slave Checklist กำหนด Device Letter Code เป็น K</p>
    <p><strong>คำถามฝึกคิด:</strong> ทำไม Component แบบ Master/Slave ถึงต้องกำหนด "ลำดับ Symbol" (Symbol Order) ให้ถูกต้อง ทั้งที่ Symbol แต่ละตัวจะถูกแยกไปวางคนละจุดบนชีทอยู่ดี?</p>
    <div class="tip"><strong>เฉลย:</strong> ลำดับ Symbol กำหนดว่า Symbol ตัวไหนจะถูกใช้แสดงใน Preview Window เป็นตัวแทนอุปกรณ์ทั้งชุด และยังมีผลต่อลำดับที่ Place Objects One-by-One (บทที่ 2) จะเสนอให้วางทีละตัวเมื่อกด <code>N</code> ไล่วางจนครบ ถ้าลำดับผิดอาจทำให้วิศวกรวางหน้าสัมผัสก่อนขดลวดโดยไม่รู้ตัว ซึ่งไม่ผิดทางไฟฟ้าแต่ทำให้ Workflow วางอุปกรณ์สับสน</div>

    <div class="page-nav">
        <a href="worksheet-08.html">← ก่อนหน้า: บทที่ 8</a>
        <a href="worksheet-10.html">ถัดไป: บทที่ 10 →</a>
    </div>'''

BODY[10] = '''    <h1>บทที่ 10: การอัปเดตระบบและการส่งออกรายงานขั้นอุตสาหกรรม (Database Sync &amp; Reporting)</h1>
    <p class="lead">ปิดงานด้วยการซิงค์ฐานข้อมูลเข้าโปรเจกต์ และผลิตเอกสาร BOM/รายงานพร้อมส่งฝ่ายผลิต</p>

    <div class="objectives">
        <p>วัตถุประสงค์การเรียนรู้</p>
        <ol>
            <li>เพื่ออัปเดตและซิงโครไนซ์ข้อมูลอุปกรณ์ที่แก้ไข Symbol ในคลังฐานข้อมูล ให้เข้าไปปรับปรุงหน้าสัมผัสบนแบบวงจรที่เขียนค้างไว้โดยอัตโนมัติผ่านคำสั่ง Update all components in project</li>
            <li>เพื่อศึกษาเทคโนโลยีการนำเข้าข้อมูลและการฝังไฟล์ภาพ 2D/3D และ STEP ในระบบแผงเลย์เอาต์ (Panel DBE) ของเวอร์ชัน 2026 ที่อัปเกรดให้สามารถแยกโพรเซสการจำลองข้อมูลได้รวดเร็วยิ่งขึ้น</li>
            <li>เพื่อใช้งานระบบสืบค้นอัตโนมัติและ Report Generator ในการผลิตเอกสาร BOM (Bill of Materials) รายการเชื่อมสายคอนเนคเตอร์ และเขียนสถิติกลับลงหน้าแบบ หรือส่งออก PDF ที่เชื่อมโยงจุด Cross-reference อัจฉริยะได้</li>
        </ol>
    </div>

    <h2>1. Update all Components and Symbols in Project</h2>
    <p>
        เมื่อแก้ไข Symbol/Component ต้นแบบใน Database Editor (บทที่ 9) — เช่น แก้ตำแหน่งหน้าสัมผัสของรีเลย์ — Device ที่วางไว้
        แล้วในโปรเจกต์เดิม<em>จะไม่เปลี่ยนตามทันที</em> เพราะเป็นระบบ Object-Oriented ที่แยกสำเนาโปรเจกต์ออกจากฐานข้อมูล
        ต้องสั่ง <strong>Update all Components and all Symbols in project</strong> เพื่อดึงการเปลี่ยนแปลงเข้ามาสู่งานที่ทำค้างไว้
    </p>
    <div class="note">
        <strong>อัพเดท 2026:</strong> คำสั่งนี้ถูกปรับปรุงให้กรองแสดงเฉพาะ Object ที่ <em>Timestamp เปลี่ยน</em> โดยไม่มี Attribute
        หรือค่าอื่นเปลี่ยนแปลงจริง แยกออกจาก Object ที่โครงสร้างเปลี่ยนจริง — เพราะการอัปเดตแค่ Timestamp เร็วและเสี่ยงน้อยกว่าการ
        อัปเดตทั้งโครงสร้างภายในของ Component ทั้งตัว (แม้จะทำให้ระบบต้องเทียบโครงสร้างระหว่างโปรเจกต์กับฐานข้อมูลทั้งหมด
        จึงอาจใช้เวลาโหลดนานขึ้นเล็กน้อย)
    </div>
    <p>
        คู่กันกับคำสั่งข้างต้นคือ <strong>Update All Models in Project</strong> สำหรับฝั่ง Panel — อัปเดตเฉพาะ Model ที่จำนวนและ
        คุณสมบัติของ Slot/Pin ไม่เปลี่ยน โดยไม่แตะ Component ที่ผูกอยู่ ปลอดภัยสำหรับ Sync เป็นประจำโดยไม่ต้องตรวจทานทุกจุด
    </p>

    <h2>2. STEP Import ใน Panel DBE 2026: เร็วขึ้นด้วยการแยกโพรเซส</h2>
    <p>
        การนำเข้าไฟล์ STEP ขนาดใหญ่เป็น Panel Model เคยมีปัญหาค้าง/ช้าในเวอร์ชันก่อนหน้า E3.series 2026 แก้โดยให้
        STEP Import <strong>รันแยกโพรเซส</strong> ออกจากโปรแกรมหลัก พร้อมปุ่มควบคุมใหม่ที่ Status Bar ระหว่าง Import:
    </p>
    <table>
        <tr><th>ปุ่ม</th><th>ผลลัพธ์</th></tr>
        <tr><td><strong>Cancel</strong></td><td>หยุด Import ทั้งหมด — ส่วนที่นำเข้าไปแล้ว (เช่น Front View) จะถูกลบทิ้งด้วย</td></tr>
        <tr><td><strong>Skip</strong></td><td>ข้ามเฉพาะเฟสปัจจุบัน (เช่น การ Import STEP/BREP หรือการสร้าง View หนึ่งๆ) แล้วไปทำเฟสถัดไปต่อ ไม่ต้องยกเลิกทั้งไฟล์</td></tr>
    </table>
    <p>
        นอกจากนี้ยังกำหนดจุดอ้างอิงพิกัด (Origin) ของโมเดลตอน Import ได้เอง — เลือกใช้ <code>Left | Bottom | Back
        (X:0, Y:0, Z:0)</code> เพื่อละ Origin เดิมของไฟล์ STEP แล้วเริ่มที่ (0,0,0) ใหม่ หรือใช้พิกัด X/Y ของไฟล์ STEP เดิม
        (Z:0) ก็ได้ ทำให้ยืดหยุ่นกับไฟล์ STEP ที่มาจากหลายแหล่งซึ่งกำหนด Origin ไว้ไม่ตรงกัน
    </p>

    <h2>3. Report Generator: ผลิตเอกสารส่งฝ่ายผลิต</h2>
    <p>
        ตั้งแต่เวอร์ชัน 2026 เมนู Reports แบบเดิม (Tools → Reports) ถูกปิดไปแล้ว แทนที่ด้วย Add-on แยกที่ต้องดาวน์โหลดเพิ่มจาก
        Zuken Support — ใช้งานฟรีไม่ต้องซื้อ License เพิ่ม มีสองเครื่องมือในเมนู Add-ons:
    </p>
    <ul>
        <li><strong>E3 ReportGenerator Creator</strong> — สร้างรายงานจากโปรเจกต์จริง เลือกจาก Template สำเร็จรูปได้ทันที</li>
        <li><strong>E3 ReportGenerator Designer</strong> — ปรับแต่งเนื้อหา/ดีไซน์ของ Template รายงาน โดยลาก Attribute/Text Type/Property ของ Object ลงในช่องตารางเอง</li>
    </ul>
    <p>รายงานมาตรฐาน 5 ชนิดที่ใช้บ่อยที่สุด:</p>
    <table>
        <tr><th>รายงาน</th><th>เนื้อหา</th></tr>
        <tr><td>Bill of Material</td><td>รายการชิ้นส่วนทั้งหมดพร้อมจำนวนและ Part Number</td></tr>
        <tr><td>Cable list</td><td>รายการสายเคเบิลทั้งหมดในโปรเจกต์</td></tr>
        <tr><td>Hose list</td><td>รายการท่อ (สำหรับงาน Pneumatic/Hydraulic)</td></tr>
        <tr><td>Connection list</td><td>รายการจุดเชื่อมต่อคอนเนคเตอร์ทั้งหมด ต้นทาง-ปลายทาง</td></tr>
        <tr><td>Content list</td><td>สารบัญเอกสารทั้งโปรเจกต์</td></tr>
    </table>
    <p>
        ส่งออกได้หลายรูปแบบ รวมถึง PDF ที่เชื่อมโยง Cross-Reference (จากบทที่ 5) ให้คลิกกระโดดข้ามหน้าได้จริงในไฟล์ PDF
        และยังเลือก Export กลับเป็น <strong>E3 Sheet</strong> เพื่อเขียนผลสรุปกลับลงบนแบบวงจรได้โดยตรงด้วย
    </p>

    <div class="note">
        <strong>ข้อควรรู้:</strong> รายงานที่สร้างไว้แล้วไม่ใช่ Online — ถ้าแก้วงจรหลัง Generate รายงานจะไม่อัปเดตอัตโนมัติ
        ต้องสั่งรันรายงานซ้ำเมื่อไรก็ตามที่แบบมีการเปลี่ยนแปลง ระบบจะอัปเดตรายงานเดิมในโปรเจกต์ให้เองเมื่อรันซ้ำ
    </div>

    <h2>ตัวอย่างฝึกทำ</h2>
    <p><strong>โจทย์:</strong> แก้ตำแหน่งหน้าสัมผัสของรีเลย์ที่สร้างไว้ในบทที่ 9 ผ่าน Database Editor แล้วกลับมาที่โปรเจกต์เดิม สั่ง Update all Components and all Symbols in project และสังเกตว่า Device บนชีทเปลี่ยนตามหรือไม่ จากนั้นสร้างรายงาน Bill of Material ด้วย E3 ReportGenerator Creator</p>
    <p><strong>คำถามฝึกคิด:</strong> ทำไมการแยก STEP Import ให้รันเป็นคนละโพรเซสถึงช่วยแก้ปัญหาไฟล์ STEP ขนาดใหญ่ค้างได้ดีกว่าการปรับปรุงแค่ความเร็วของอัลกอริทึมนำเข้าไฟล์?</p>
    <div class="tip"><strong>เฉลย:</strong> เพราะเวลาโปรแกรมหลักกับตัวนำเข้าไฟล์อยู่คนละโพรเซสกัน ถ้าการ Import ค้างหรือใช้เวลานาน ผู้ใช้ยังกดปุ่ม Cancel หรือ Skip ได้ทันทีโดยที่โปรแกรมหลัก (E3.series) ไม่ค้างตามไปด้วย ต่างจากการรันในโพรเซสเดียวกันที่ถ้าไฟล์มีปัญหา อาจทำให้ทั้งโปรแกรมค้างจนต้องปิดโปรแกรมทิ้งทั้งโปรเจกต์ที่ยังไม่ได้บันทึก</div>

    <div class="page-nav">
        <a href="worksheet-09.html">← ก่อนหน้า: บทที่ 9</a>
        <a href="cable.html">ถัดไป: Cable →</a>
    </div>'''

for _n in range(1, 11):
    gs.write(f"schematic/{_n:02d}.html", gs.page_html(TITLE[_n], BODY[_n], "schematic", _n))
