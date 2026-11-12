# Luyện thi TOEIC — Nhóm 2: Ngữ pháp trọng tâm. Định dạng giống _toeic_tu_loai.py

GROUP = "⚙️ Ngữ pháp trọng tâm"

LESSONS = [
dict(slug="toeic-thi", ico="⏰", en="Verb tenses", vi="Thì động từ", color="#d81b60", theory="""
## Dấu hiệu thì hiện tại
= Hiện tại đơn: every day, usually, often, always · lịch trình cố định
= Hiện tại tiếp diễn: now, currently, at the moment, at present
= Hiện tại hoàn thành: since, for, already, yet, recently, so far, over the past … years
Mr. Lee is currently working on the budget.|Ông Lee hiện đang làm ngân sách.
Sales have risen by 10% over the past three months.|Doanh số đã tăng 10% trong ba tháng qua.
## Dấu hiệu thì quá khứ
= Quá khứ đơn: yesterday, last week, ago, in 2020
= Quá khứ tiếp diễn: when / while + hành động đang xảy ra thì bị xen vào
= Quá khứ hoàn thành: by the time + quá khứ, before + quá khứ
By the time we arrived, the meeting had already started.|Khi chúng tôi đến thì cuộc họp đã bắt đầu rồi.
## Dấu hiệu thì tương lai
= will / be going to: tomorrow, next week, soon, upcoming
= Tương lai hoàn thành: by + thời điểm tương lai, by the time + hiện tại đơn
- Mệnh đề when / if / before / as soon as dùng hiện tại đơn để nói về tương lai
By next March, we will have opened three new stores.|Đến tháng Ba tới, chúng tôi sẽ mở được ba cửa hàng mới.
## Mẹo chọn thì nhanh
- Tìm trạng từ chỉ thời gian trong câu trước tiên
- Chủ ngữ số ít → loại động từ số nhiều · có tân ngữ → loại bị động
- Câu chưa có động từ chính → loại V-ing và to V
""", quiz="""
Ms. Taylor ___ for the company since 2015.|has worked|works|worked|is working|"since 2015" → thì hiện tại hoàn thành.
The board ___ the proposal at yesterday's meeting.|approved|approves|has approved|will approve|"yesterday" → quá khứ đơn.
We ___ a new branch in Hanoi next month.|will open|opened|have opened|open|"next month" → tương lai đơn.
By the time the CEO arrived, the meeting ___.|had already started|has already started|already starts|will already start|"By the time + quá khứ" → quá khứ hoàn thành.
The shuttle bus ___ every 20 minutes.|leaves|left|is left|leaving|Lịch trình lặp lại ("every 20 minutes") → hiện tại đơn.
By the end of this year, the company ___ 500 employees.|will have hired|has hired|hired|hires|"By + thời điểm tương lai" → tương lai hoàn thành.
Mr. Brown ___ on a report at the moment.|is working|works|worked|has worked|"at the moment" → hiện tại tiếp diễn.
Prices ___ steadily over the past five years.|have risen|rise|will rise|rising|"over the past five years" → hiện tại hoàn thành.
Please call me as soon as the package ___.|arrives|will arrive|arrived|arriving|Mệnh đề "as soon as" nói về tương lai dùng hiện tại đơn.
The company ___ its headquarters to Seoul three years ago.|moved|has moved|moves|will move|"ago" → quá khứ đơn.
When the fire alarm rang, the staff ___ a meeting.|were having|have|are having|will have|Hành động đang diễn ra trong quá khứ thì bị xen vào → quá khứ tiếp diễn.
Ms. Kim ___ the report yet.|hasn't finished|didn't finish|doesn't finish|won't finish|"yet" trong câu phủ định → hiện tại hoàn thành.
The new policy ___ effect next Monday.|will take|took|has taken|taking|"next Monday" → tương lai; take effect = có hiệu lực.
So far, we ___ over 1,000 orders this month.|have received|receive|received|will receive|"So far" (tính đến nay) → hiện tại hoàn thành.
Before she joined our firm, Ms. Ali ___ in a bank for six years.|had worked|has worked|works|will work|Hành động xảy ra trước một hành động khác trong quá khứ → quá khứ hoàn thành.
"""),

dict(slug="toeic-bi-dong", ico="🔄", en="Passive voice", vi="Câu bị động", color="#5e35b1", theory="""
## Cấu trúc câu bị động
= be + V3/ed (+ by + người làm)
- Hiện tại: is/are + V3 · Quá khứ: was/were + V3 · Tiếp diễn: is being + V3
- Hoàn thành: has/have been + V3 · Tương lai: will be + V3 · Modal: can/must/should be + V3
The road is being repaired.|Con đường đang được sửa.
## Chủ động hay bị động?
= Sau chỗ trống có tân ngữ (danh từ) → chủ động
= Sau chỗ trống không có tân ngữ, hoặc có "by" → bị động
- Chủ ngữ là vật (report, package, order) thường đi với bị động
The manager signed the contract.|Quản lý đã ký hợp đồng. (có tân ngữ → chủ động)
The contract was signed yesterday.|Hợp đồng đã được ký hôm qua. (không có tân ngữ → bị động)
## Cấu trúc bị động hay gặp trong TOEIC
= be required / expected / asked / encouraged / advised + to V
= be scheduled to · be supposed to · be designed to
= S + be given / sent / offered / awarded + danh từ
Employees are required to wear helmets.|Nhân viên bắt buộc phải đội mũ bảo hộ.
All participants will be given a certificate.|Tất cả học viên sẽ được trao chứng chỉ.
## Phân từ rút gọn sau danh từ
= danh từ + V-ing (chủ động) · danh từ + V3 (bị động)
The documents attached to this email contain the details.|Các tài liệu đính kèm trong email này có thông tin chi tiết.
Customers wishing to return items must bring a receipt.|Khách hàng muốn trả hàng phải mang theo hóa đơn.
""", quiz="""
The new library ___ in 2019.|was built|built|has built|builds|Thư viện (vật) không tự xây, không có tân ngữ → bị động quá khứ was built.
All orders ___ within 24 hours.|are processed|process|processing|have processed|Đơn hàng được xử lý, không có tân ngữ → bị động are processed.
The meeting has ___ until next Tuesday.|been postponed|postponing|postpone|to postpone|"has been + V3" → hiện tại hoàn thành bị động.
Every participant ___ a certificate at the end of the course.|will be given|will give|gives|giving|Học viên được trao chứng chỉ → bị động "be given + danh từ".
Mr. Hong ___ the contract yesterday afternoon.|signed|was signed|is signed|signing|Có tân ngữ "the contract" → chủ động.
Visitors are required ___ a badge.|to wear|wearing|wear|wore|"be required + to V" = bắt buộc phải.
The documents ___ to this email contain the details.|attached|attaching|attach|attaches|Tài liệu "được đính kèm" → phân từ V3 rút gọn: attached.
The package should ___ by Friday.|be delivered|deliver|delivered|delivering|"modal + be + V3" → should be delivered.
Customers ___ to exchange items must bring a receipt.|wishing|wished|wish|are wishing|Khách hàng (chủ động) muốn → rút gọn bằng V-ing: wishing.
The road is ___ repaired, so please use another route.|being|been|be|to be|"is being + V3" → bị động tiếp diễn (đang được sửa).
The conference ___ to start at 9 a.m.|is scheduled|schedules|scheduling|has scheduled|"be scheduled to V" = được lên lịch.
Over 200 people ___ for the event so far.|have registered|have been registered|registering|be registered|"register for" (đăng ký) là nội động từ, người tự đăng ký → chủ động.
The report ___ by the finance team last week.|was reviewed|reviewed|has reviewed|reviews|Có "by the finance team" → bị động quá khứ.
Our products ___ to more than 30 countries.|are exported|export|exporting|have exported|Sản phẩm được xuất khẩu, không có tân ngữ → bị động.
The new employees ___ by Ms. Garcia next week.|will be trained|will train|are training|trained|Có "by Ms. Garcia" và "next week" → bị động tương lai.
"""),

dict(slug="toeic-to-v-ving", ico="🎯", en="Infinitives & Gerunds", vi="To V hay V-ing", color="#00acc1", theory="""
## Động từ + to V
= agree · decide · plan · hope · expect · want · need · offer · refuse · promise · fail · afford · intend · aim
= ask · tell · allow · encourage · require · invite · remind + tân ngữ + to V
The firm failed to meet the deadline.|Công ty đã không kịp hạn chót.
## Động từ + V-ing
= avoid · consider · enjoy · finish · suggest · recommend · mind · postpone · delay · keep · deny · discontinue
We recommend booking in advance.|Chúng tôi khuyên bạn nên đặt trước.
## Giới từ + V-ing (bẫy chữ "to")
= look forward to · be used to · be committed to · be dedicated to · object to + V-ing
= in addition to · prior to · with a view to + V-ing
- "to" ở đây là giới từ, không phải dấu hiệu của to V
We look forward to hearing from you.|Chúng tôi mong nhận được phản hồi từ bạn.
## Động từ đổi nghĩa
= remember / forget + to V (việc cần làm) · + V-ing (việc đã làm)
= stop + to V (dừng lại để làm việc khác) · stop + V-ing (thôi làm)
= try + to V (cố gắng) · try + V-ing (thử làm)
Remember to lock the door.|Nhớ khóa cửa nhé.
## Chỉ mục đích
= (in order) to V · so as to V · for + danh từ
We hired more staff to reduce waiting times.|Chúng tôi tuyển thêm nhân viên để giảm thời gian chờ.
""", quiz="""
The company decided ___ a new branch in Da Nang.|to open|opening|open|opened|"decide + to V".
Please avoid ___ the elevator during a fire.|using|to use|use|used|"avoid + V-ing".
We look forward to ___ you at the conference.|seeing|see|saw|seen|"look forward to + V-ing" — "to" là giới từ.
Ms. Ross agreed ___ the project.|to lead|leading|lead|led|"agree + to V".
The doctor recommended ___ more exercise.|getting|to get|get|got|"recommend + V-ing".
Employees are encouraged ___ in the training program.|to participate|participating|participate|participated|"be encouraged + to V".
Have you finished ___ the report?|writing|to write|write|written|"finish + V-ing".
The firm cannot afford ___ more staff this year.|to hire|hiring|hire|hired|"afford + to V".
Mr. Park is committed to ___ excellent service.|providing|provide|provided|provides|"be committed to + V-ing".
Please remember ___ off the lights before you leave.|to turn|turning|turn|turned|Việc cần làm trong tương lai → "remember + to V".
We are considering ___ our office to a larger building.|moving|to move|move|moved|"consider + V-ing".
Our manager asked us ___ the meeting room.|to prepare|preparing|prepare|prepared|"ask + tân ngữ + to V".
The store stopped ___ plastic bags last year.|offering|to offer|offer|offered|Thôi không cung cấp nữa → "stop + V-ing"; stop to offer nghĩa là dừng lại để đưa túi.
Prior to ___ the device, please read the instructions.|using|use|used|uses|"prior to" là giới từ → V-ing.
We hired more staff ___ customer waiting times.|to reduce|reducing|reduced|reduces|Chỉ mục đích → to V.
"""),

dict(slug="toeic-menh-de-quan-he", ico="🧩", en="Relative clauses", vi="Mệnh đề quan hệ", color="#7cb342", theory="""
## Đại từ quan hệ
= who (người, làm chủ ngữ) · whom (người, làm tân ngữ) · which (vật) · that (người/vật)
= whose + danh từ (sở hữu) · where (nơi chốn) · when (thời gian)
The client whose order was delayed received a discount.|Khách hàng có đơn hàng bị chậm đã được giảm giá.
## Chọn đúng đại từ quan hệ
- Sau chỗ trống là động từ → who / which / that (làm chủ ngữ)
- Sau chỗ trống là danh từ không có mạo từ → whose
- Sau chỗ trống là S + V đầy đủ → whom / which (tân ngữ) hoặc where / when
= Sau dấu phẩy hoặc sau giới từ: KHÔNG dùng that
- …, which … · in which · to whom
## Rút gọn mệnh đề quan hệ
= danh từ + who/which + V (chủ động) → danh từ + V-ing
= danh từ + who/which + be + V3 (bị động) → danh từ + V3
Employees wanting to attend should register online.|Nhân viên muốn tham dự hãy đăng ký trực tuyến.
The cars made in this factory are exported.|Những chiếc xe sản xuất tại nhà máy này được xuất khẩu.
## what · whoever · whatever
= what = the thing(s) that (cái mà, điều mà) · whoever = bất cứ ai · whatever = bất cứ cái gì
What we need is more time.|Điều chúng ta cần là thêm thời gian.
""", quiz="""
The manager ___ hired me has retired.|who|which|whose|whom|Chỉ người, theo sau là động từ "hired" → who.
The laptop ___ I bought last week is broken.|that|who|whose|where|Chỉ vật, làm tân ngữ của "bought" → that (hoặc which).
We want to hire someone ___ experience in marketing is strong.|whose|who|which|whom|Theo sau là danh từ "experience" (kinh nghiệm của người đó) → whose.
This is the hotel ___ the conference will be held.|where|which|who|whose|Nơi chốn, theo sau là mệnh đề đầy đủ → where.
Ms. Choi, ___ joined us last year, is now a team leader.|who|that|which|whom|Chỉ người, sau dấu phẩy, làm chủ ngữ → who (không dùng that sau dấu phẩy).
The report, ___ was published yesterday, shows strong growth.|which|that|who|what|Chỉ vật, sau dấu phẩy → which.
Applicants ___ the position must submit a resume.|seeking|sought|seek|are seeking|Rút gọn mệnh đề chủ động "who seek" → seeking.
The cars ___ in this factory are exported to Europe.|produced|producing|produce|are produced|Rút gọn mệnh đề bị động "which are produced" → produced.
___ we need now is a clear plan.|What|That|Which|Whose|"What" = điều mà; mệnh đề "What we need" làm chủ ngữ.
The candidate ___ we interviewed yesterday was excellent.|whom|which|whose|where|Chỉ người, làm tân ngữ của "interviewed" → whom.
___ wins the contest will receive a free trip.|Whoever|Whatever|Whom|Which|"Whoever" = bất cứ ai thắng.
The day ___ the store opened was very busy.|when|which|who|whose|Chỉ thời gian, theo sau là mệnh đề đầy đủ → when.
Please return the form ___ you received by email.|that|who|whose|what|Chỉ vật, làm tân ngữ → that.
Mr. Lee is the person to ___ you should send the invoice.|whom|who|that|which|Sau giới từ "to" và chỉ người → whom.
Employees ___ in the survey received a gift card.|participating|participate|participation|participates|Rút gọn mệnh đề chủ động "who participated" → participating.
"""),

dict(slug="toeic-so-sanh", ico="⚖️", en="Comparisons", vi="So sánh", color="#fb8c00", theory="""
## So sánh hơn
= tính từ ngắn + -er + than · more + tính từ dài + than
- cheaper than, faster than · more expensive than, more efficiently than
- Nhấn mạnh: much / far / even / a lot + so sánh hơn (không dùng very)
This model is much cheaper than that one.|Mẫu này rẻ hơn nhiều so với mẫu kia.
## So sánh nhất
= the + tính từ ngắn + -est · the most + tính từ dài
- one of the + so sánh nhất + danh từ số nhiều
- Có "of / in + nhóm" hoặc "ever" → so sánh nhất
This is one of the most popular products we have ever launched.|Đây là một trong những sản phẩm được ưa chuộng nhất mà chúng tôi từng tung ra.
## So sánh bằng
= as + tính từ / trạng từ + as · not as/so + tính từ + as
= the same + danh từ + as · twice / three times + as … as
The new model is twice as fast as the old one.|Mẫu mới nhanh gấp đôi mẫu cũ.
## Bất quy tắc và cấu trúc đặc biệt
= good/well → better → best · bad → worse → worst · far → farther/further
= many/much → more → most · little → less → least
= The + so sánh hơn …, the + so sánh hơn … (càng… càng…)
- further information = thông tin thêm
The sooner you book, the cheaper the ticket is.|Đặt càng sớm thì vé càng rẻ.
""", quiz="""
This year's sales are ___ than last year's.|higher|high|highest|highly|Có "than" → so sánh hơn: higher.
This is the ___ hotel in the city.|most expensive|more expensive|expensive|expensively|"the … in the city" → so sánh nhất.
The new printer is ___ faster than the old one.|much|very|more|most|Nhấn mạnh so sánh hơn dùng much, không dùng very.
Our prices are as ___ as our competitors'.|low|lower|lowest|lowly|So sánh bằng "as + tính từ nguyên dạng + as".
Mr. Han is one of the ___ engineers in the company.|most experienced|more experienced|experience|experiencing|"one of the + so sánh nhất + danh từ số nhiều".
The ___ you apply, the better your chances are.|earlier|earliest|early|more early|"The + so sánh hơn …, the + so sánh hơn" → earlier.
This route is ___ than the highway.|shorter|short|shortest|shortly|Có "than" → shorter.
Customer feedback this month was ___ than expected.|better|good|best|well|So sánh hơn của good là better.
For ___ information, please visit our website.|further|furthest|far|farther|"further information" = thông tin thêm.
The new software runs ___ efficiently than the old version.|more|most|much|very|Trạng từ dài "efficiently" + than → more efficiently.
This is the ___ product we have ever launched.|most successful|more successful|success|successfully|Có "ever" → so sánh nhất.
The second interview was ___ difficult than the first.|less|least|fewer|little|"less + tính từ + than" = kém… hơn.
The meeting room is not as ___ as the hall.|large|larger|largest|largely|"not as + tính từ nguyên dạng + as".
Of all the candidates, Ms. Wu is the ___ qualified.|best|better|good|well|"Of all…" → so sánh nhất: the best qualified.
The new model uses ___ energy than the previous one.|less|fewer|little|least|"energy" không đếm được → less; fewer dùng cho danh từ đếm được.
"""),

dict(slug="toeic-luong-tu", ico="🔢", en="Quantifiers & Agreement", vi="Lượng từ & Hòa hợp", color="#546e7a", theory="""
## Lượng từ với danh từ đếm được / không đếm được
= many · a few · few · several · a number of + danh từ số nhiều
= much · a little · little · a great deal of · an amount of + danh từ không đếm được
= a lot of · lots of · plenty of · some · any · most · all + cả hai loại
- few / little = rất ít (nghĩa tiêu cực) · a few / a little = một vài, một chút
## each · every · all · both
= each / every + danh từ số ít + động từ số ít
= each of / one of / either of + the + danh từ số nhiều + động từ số ít
= all / both / most / some of + the + danh từ số nhiều
Each of the rooms has a TV.|Mỗi phòng đều có một chiếc TV.
## the number of / a number of
= the number of + danh từ số nhiều + động từ số ít (con số)
= a number of + danh từ số nhiều + động từ số nhiều (nhiều)
The number of visitors has doubled.|Số lượng khách đã tăng gấp đôi.
A number of visitors have complained.|Nhiều khách đã phàn nàn.
## almost · most · enough
= almost all / almost every (hầu như tất cả) — không dùng "almost + danh từ"
= most + danh từ (hầu hết, nói chung) · most of the + danh từ (trong một nhóm xác định)
= enough + danh từ · tính từ + enough
Most employees work from home on Fridays.|Hầu hết nhân viên làm việc ở nhà vào thứ Sáu.
""", quiz="""
We received ___ complaints about the new design.|several|much|a little|every|"complaints" số nhiều đếm được → several.
There isn't ___ time left before the deadline.|much|many|several|few|"time" không đếm được → much.
___ employee must attend the safety training.|Every|All|Many|Several|Danh từ số ít "employee" → Every.
Each of the rooms ___ a private bathroom.|has|have|having|are having|"Each of + danh từ số nhiều" + động từ số ít → has.
The number of tourists ___ increased this year.|has|have|are|were|"The number of" + động từ số ít → has.
A number of employees ___ asked for flexible hours.|have|has|is|was|"A number of" + động từ số nhiều → have.
Only ___ people came to the meeting, so it was cancelled.|a few|a little|much|every|"people" đếm được → a few.
___ of the staff members agreed with the new policy.|Most|Almost|Every|Much|"Most of the + danh từ" → Most; almost không đi trực tiếp với "of".
We need a great deal of ___ to finish the project.|money|employees|computers|ideas|"a great deal of" + danh từ không đếm được → money.
___ all participants found the workshop useful.|Almost|Most|Mostly|Much|"almost all" = hầu như tất cả.
There is ___ information about the event on our website.|little|few|many|several|"information" không đếm được, động từ "is" → little.
___ applicants will be contacted by email.|All|Every|Each|Much|Danh từ số nhiều "applicants" → All.
Both of the candidates ___ excellent references.|have|has|having|is having|"Both of" + động từ số nhiều → have.
There are not ___ chairs for all the guests.|enough|much|a little|every|"enough + danh từ số nhiều" = đủ.
Either of the two dates ___ fine for me.|is|are|were|have been|"Either of + danh từ số nhiều" + động từ số ít → is.
"""),

dict(slug="toeic-dieu-kien", ico="🔀", en="Conditionals & Inversion", vi="Câu điều kiện & Đảo ngữ", color="#c0ca33", theory="""
## Câu điều kiện loại 1, 2, 3
= Loại 1: If + hiện tại đơn, will + V (có thể xảy ra)
= Loại 2: If + quá khứ đơn, would + V (không có thật ở hiện tại)
= Loại 3: If + had V3, would have V3 (không có thật trong quá khứ)
If you order today, you will receive a 10% discount.|Nếu đặt hàng hôm nay, bạn sẽ được giảm 10%.
If we had more staff, we would open on Sundays.|Nếu có thêm nhân viên, chúng tôi sẽ mở cửa vào Chủ nhật.
## unless · as long as · in case · otherwise
= unless = if … not (trừ khi) · provided (that) / as long as = miễn là
= in case = phòng khi · otherwise = nếu không thì
## Đảo ngữ câu điều kiện (rất hay gặp trong TOEIC)
= Should + S + V (= If + S + V, loại 1)
= Were + S + to V / Were + S + tính từ (= loại 2)
= Had + S + V3 (= loại 3)
Should you have any questions, please contact us.|Nếu có thắc mắc, vui lòng liên hệ với chúng tôi.
Had we known about the traffic, we would have left earlier.|Nếu biết trước về tình hình giao thông, chúng tôi đã đi sớm hơn.
## Đảo ngữ với trạng từ phủ định
= Never / Rarely / Seldom + trợ động từ + S + V
= Not only + trợ động từ + S + V, but … also …
= Only after / Only when + mệnh đề + trợ động từ + S + V
Rarely has the company seen such high profits.|Hiếm khi công ty đạt lợi nhuận cao như vậy.
""", quiz="""
If the shipment ___ late, we will contact you.|arrives|will arrive|arrived|arriving|Điều kiện loại 1: mệnh đề if dùng hiện tại đơn.
___ you have any questions, please call our hotline.|Should|Would|Had|Were|Đảo ngữ loại 1: Should + S + V.
If I ___ you, I would accept the offer.|were|am|be|have been|Điều kiện loại 2: "If I were you".
___ we known about the delay, we would have rescheduled.|Had|Have|Should|Were|Đảo ngữ loại 3: Had + S + V3.
The event will be held outdoors ___ it rains.|unless|if|provided|whether|"unless" = trừ khi trời mưa.
If we had hired more staff, we ___ the deadline.|would have met|will meet|met|would meet|Điều kiện loại 3: would have + V3.
Customers can return items ___ they keep the receipt.|as long as|unless|otherwise|despite|"as long as" = miễn là.
Take an umbrella ___ it rains.|in case|unless|otherwise|despite|"in case" = phòng khi.
If the company ___ more money, it would build a new factory.|had|has|will have|having|Điều kiện loại 2: mệnh đề if dùng quá khứ đơn.
Rarely ___ such a successful product launch.|have we seen|we have seen|we saw|seen we have|"Rarely" đứng đầu câu → đảo ngữ: trợ động từ + S + V.
Not only ___ the sales target, but they also exceeded it.|did they reach|they reached|they did reach|reached they|"Not only" đứng đầu câu → đảo ngữ: did + S + V.
___ the manager available, she would join the call.|Were|Was|Had|Should|Đảo ngữ loại 2: Were + S + tính từ.
Please register early; ___, you may not get a seat.|otherwise|unless|if|provided|"otherwise" = nếu không thì, đứng sau dấu chấm phẩy.
Should the printer ___ again, please call the technician.|break|breaks|broke|broken|"Should + S + V nguyên mẫu".
If you ___ the form by Friday, your application will not be processed.|do not submit|did not submit|had not submitted|not submit|Điều kiện loại 1 (mệnh đề chính dùng will) → hiện tại đơn.
"""),

dict(slug="toeic-tu-de-nham", ico="🤔", en="Confusing words & Collocations", vi="Từ dễ nhầm & Kết hợp từ", color="#ec407a", theory="""
## Cặp động từ dễ nhầm
= rise (tự tăng, không có tân ngữ) ≠ raise (nâng, tăng cái gì — có tân ngữ)
= lie (nằm) ≠ lay (đặt) · affect (v: ảnh hưởng) ≠ effect (n: tác động)
= borrow (mượn) ≠ lend (cho mượn) · say (nói điều gì) ≠ tell + người
Prices rose by 5%.|Giá đã tăng 5%.
The company raised prices by 5%.|Công ty đã tăng giá 5%.
## Cặp danh từ dễ nhầm
= advice (n: lời khuyên) ≠ advise (v: khuyên) · price (giá) ≠ prize (giải thưởng)
= fare (tiền vé xe) ≠ fee (phí) ≠ fine (tiền phạt)
- bus fare · membership fee · late fee · parking fine
- customer (khách mua hàng) ≠ client (khách dùng dịch vụ)
## Cặp tính từ / trạng từ dễ nhầm
= especially (đặc biệt là) ≠ specially (được làm riêng cho)
= every day (mỗi ngày — trạng từ) ≠ everyday (hằng ngày — tính từ)
= alternate (luân phiên) ≠ alternative (thay thế)
## Kết hợp từ (collocations) thường gặp
= make a decision · make an appointment · make a reservation · make progress
= do business · do research · do one's best
= meet a deadline · meet the needs · reach an agreement · place an order
= take place (diễn ra) · take part in · pay attention to · give a presentation
The annual conference will take place in Singapore.|Hội nghị thường niên sẽ diễn ra tại Singapore.
""", quiz="""
The company plans to ___ salaries next year.|raise|rise|arise|rose|Có tân ngữ "salaries" → raise (tăng cái gì).
Housing prices have ___ sharply this year.|risen|raised|raise|rising|Giá tự tăng, không có tân ngữ → rise, V3 là risen.
The new policy will ___ all employees.|affect|effect|effective|affection|Sau "will" cần động từ → affect (ảnh hưởng).
The new law had a positive ___ on small businesses.|effect|affect|effective|affected|"a positive + danh từ" → effect (tác động).
Could you ___ me your pen for a moment?|lend|borrow|lent|borrowing|"lend sb sth" = cho ai mượn cái gì.
Our consultant will ___ you on the best investment options.|advise|advice|advisory|advisable|Sau "will" cần động từ → advise; advice là danh từ.
Please ___ the documents on my desk.|lay|lie|lain|lying|"lay" = đặt (có tân ngữ); "lie" = nằm.
We need to ___ a decision by the end of the week.|make|do|play|give|Collocation: make a decision.
The annual conference will take ___ in Singapore.|place|part|time|care|"take place" = diễn ra.
Ms. Wang ___ an order for 50 laptops yesterday.|placed|took|did|went|Collocation: place an order = đặt hàng.
The membership ___ is $50 per year.|fee|fare|fine|tip|Phí thành viên → fee.
The bus ___ has increased to 10,000 dong.|fare|fee|fine|toll|Tiền vé xe buýt → fare.
The store is very busy, ___ on weekends.|especially|specially|special|specialize|"especially" = đặc biệt là.
We must work hard to ___ the deadline.|meet|do|join|take|Collocation: meet a deadline = kịp hạn chót.
The manager ___ the team that the project was approved.|told|said|spoke|talked|"tell + người + that…"; say không có tân ngữ chỉ người theo sau.
"""),
]
