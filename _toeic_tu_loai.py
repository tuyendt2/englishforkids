# Luyện thi TOEIC — Nhóm 1: Từ loại (Parts of speech)
#
# Mỗi bài là một dict:
#   theory   : cùng định dạng ngữ pháp  (## tiêu đề · = công thức · - ghi chú · EN|VN ví dụ)
#   quiz     : mỗi dòng  câu hỏi có ___|đáp án đúng|sai 1|sai 2|sai 3|giải thích
#              (build.py tự xáo vị trí A–D; câu hỏi phải có đúng một chỗ ___)
#   families : (tùy chọn) bảng họ từ, mỗi dòng  Danh từ|Động từ|Tính từ|Trạng từ  ("—" = không có)

GROUP = "🔤 Từ loại (Parts of speech)"

LESSONS = [
dict(slug="toeic-danh-tu", ico="🏷️", en="Nouns", vi="Danh từ", color="#1e88e5", theory="""
## Dấu hiệu nhận biết danh từ (hậu tố)
= -tion/-sion · -ment · -ness · -ity · -ance/-ence · -ship · -al · -ure · -age
- -tion/-sion: application, decision, expansion · -ment: management, agreement, payment
- -ness: awareness, effectiveness · -ity: ability, availability, security
- -ance/-ence: performance, maintenance, attendance, reference
- -ship: membership, partnership · -ure: departure, procedure · -age: storage, shortage
- Cẩn thận: -al vừa là đuôi danh từ (approval, arrival, proposal) vừa là đuôi tính từ (annual, financial)
The proposal received final approval.|Đề xuất đã được phê duyệt chính thức.
## Danh từ chỉ người
= -er/-or · -ee · -ant/-ent · -ist · -ian
- employer (người thuê) ≠ employee (người được thuê) · trainer ≠ trainee
- applicant, assistant, consultant, participant, resident, specialist, technician
- Phân biệt người / vật theo nghĩa: applicants (ứng viên) được phỏng vấn, applications (hồ sơ) được nộp
All applicants will be interviewed next week.|Tất cả ứng viên sẽ được phỏng vấn vào tuần sau.
## Vị trí của danh từ trong câu
= a/an/the · this/these · my/your/our/their · many/several + (adj) + ___
= ___ + động từ (chủ ngữ) · động từ + ___ (tân ngữ) · giới từ + ___
- Sau giới từ (for, of, in, with, by…) cần danh từ hoặc V-ing
- Danh từ ghép rất hay gặp: safety regulations, customer satisfaction, sales representative
- Trước "of" thường là danh từ: the construction of, the purpose of
Please submit your application by Friday.|Vui lòng nộp đơn trước thứ Sáu.
## Danh từ đếm được và không đếm được
= a/an · many · few · several · a number of + danh từ đếm được
= much · little · a great deal of · an amount of + danh từ không đếm được
- Không đếm được (không thêm -s, không đi với a/an): information, equipment, furniture, advice, luggage, baggage, machinery, merchandise, research, feedback, access
- Muốn đếm: a piece of information, a piece of equipment
We need more information about the project.|Chúng tôi cần thêm thông tin về dự án.
""", quiz="""
Please submit your ___ to the human resources department by Friday.|application|apply|applied|applicable|Sau tính từ sở hữu "your" cần một danh từ → application (đơn xin việc).
The ___ of the new factory will create 200 jobs.|construction|construct|constructive|constructed|Giữa "The" và "of" cần danh từ → construction (việc xây dựng).
All ___ must wear identification badges at all times.|employees|employ|employment|employed|Cần chủ ngữ chỉ người (người đeo thẻ) → employees (nhân viên). Employment nghĩa là "việc làm".
Customer ___ is our top priority.|satisfaction|satisfy|satisfied|satisfying|Danh từ ghép "customer satisfaction" (sự hài lòng của khách hàng) làm chủ ngữ.
The company offers free ___ to all new staff members.|training|trained|trainable|retrained|Sau tính từ "free" cần danh từ làm tân ngữ cho "offers" → training (sự đào tạo).
Mr. Kim was praised for his ___ to the project.|contribution|contribute|contributed|contributive|Sau "his" cần danh từ; contribution to = sự đóng góp cho.
We need more ___ before making a final decision.|information|informations|informative|inform|"Information" không đếm được nên không thêm -s.
The new office ___ will arrive on Monday.|furniture|furnitures|furnish|furnished|"Furniture" (đồ nội thất) không đếm được và đứng sau "office" để tạo danh từ ghép.
Several ___ for the manager position were interviewed this week.|applicants|applications|apply|applicable|Người được phỏng vấn là ứng viên → applicants; applications là hồ sơ.
There has been a sharp ___ in sales since January.|increase|increased|increasing|increasingly|Cấu trúc "a + tính từ (sharp) + danh từ" → increase (sự tăng).
Please read the safety ___ carefully before using the machine.|instructions|instruct|instructive|instructed|Danh từ ghép "safety instructions" (hướng dẫn an toàn) làm tân ngữ cho "read".
The ___ of the meeting is to discuss next year's budget.|purpose|purposeful|purposely|purposed|Sau "The" và trước "of" cần danh từ → purpose (mục đích).
Our ___ with Lotus Corporation has lasted for ten years.|partnership|partner|partnered|partnering|Chủ ngữ số ít đi với "has lasted" và mang nghĩa "mối quan hệ hợp tác" → partnership.
The hotel is closed for ___ until the end of the month.|renovation|renovate|renovated|renovates|Sau giới từ "for" cần danh từ → renovation (việc sửa chữa, cải tạo).
Visitors can gain ___ to the building with a temporary pass.|access|accessible|accessibly|accessed|Cụm cố định "gain access to" = được vào, tiếp cận.
"""),

dict(slug="toeic-dong-tu", ico="⚡", en="Verbs", vi="Động từ", color="#e53935", theory="""
## Dấu hiệu nhận biết động từ
= -ize/-ise · -ify · -en · -ate · tiền tố en- / re-
- -ize: organize, prioritize, finalize, minimize · -ify: notify, verify, clarify, simplify
- -en: strengthen, widen, shorten, broaden · -ate: activate, evaluate, demonstrate, facilitate
- en-: ensure, enable, enlarge · re-: renew, reschedule, reconsider
We need to finalize the schedule today.|Chúng ta cần chốt lịch trình trong hôm nay.
## Vị trí động từ
= S + ___ (+ O) — mỗi mệnh đề phải có một động từ chính được chia thì
= will · can · must · should · may + V nguyên mẫu
= to + V nguyên mẫu · Please + V nguyên mẫu (câu mệnh lệnh)
- Câu mệnh lệnh trong email/thông báo: Please contact…, Kindly note…
- help + (to) V: This will help (to) reduce costs.
Please contact us if you have any questions.|Vui lòng liên hệ với chúng tôi nếu bạn có thắc mắc.
## Hòa hợp chủ ngữ – động từ
= Chủ ngữ số ít / không đếm được + V-s/es · Chủ ngữ số nhiều + V
- "The list of items ___" → chủ ngữ chính là "list" (số ít) → is
- each / every / everyone / the number of + động từ số ít
- a number of + danh từ số nhiều + động từ số nhiều
The list of new products is on the website.|Danh sách sản phẩm mới có trên trang web.
## Câu giả định với "that"
= suggest · recommend · request · require · insist + that + S + V nguyên mẫu
= It is essential / important / necessary + that + S + V nguyên mẫu
- Không chia động từ theo chủ ngữ: that every employee attend (không phải attends)
The manager requested that every employee attend the meeting.|Quản lý yêu cầu mọi nhân viên tham dự cuộc họp.
""", quiz="""
The new software will ___ the payroll process.|simplify|simple|simply|simplicity|Sau "will" cần động từ nguyên mẫu → simplify (đơn giản hóa).
Please ___ the attached form and return it by Friday.|complete|completion|completely|completed|Câu mệnh lệnh "Please + V nguyên mẫu" → complete.
Our team ___ customer complaints every morning.|reviews|review|reviewing|to review|"Our team" là chủ ngữ số ít, "every morning" → hiện tại đơn → reviews.
The list of approved vendors ___ updated every month.|is|are|be|being|Chủ ngữ chính là "The list" (số ít), không phải "vendors" → is.
We must ___ that all products meet safety standards.|ensure|sure|surely|assurance|Sau "must" cần động từ nguyên mẫu → ensure (đảm bảo).
The director suggested that the meeting ___ postponed.|be|is|was|being|"Suggest that + S + V nguyên mẫu" (câu giả định) → be postponed.
Management will ___ the proposal before making a decision.|evaluate|evaluation|evaluative|evaluator|Sau "will" cần động từ nguyên mẫu → evaluate (đánh giá).
Each of the applicants ___ an interview next week.|has|have|having|to have|"Each of + danh từ số nhiều" đi với động từ số ít → has.
These measures will help ___ energy costs.|reduce|reduction|reductive|reduced|"help + V nguyên mẫu" → reduce.
The equipment in the lab ___ checked regularly.|is|are|be|have|"Equipment" không đếm được → động từ số ít is.
The city plans to ___ the main road to reduce traffic.|widen|wide|width|widely|Sau "to" cần động từ nguyên mẫu; widen = mở rộng (đuôi -en).
It is essential that every visitor ___ in at the front desk.|sign|signs|signed|signing|"It is essential that + S + V nguyên mẫu" → sign.
Ms. Lee ___ the clients about the schedule change yesterday.|notified|notify|notification|notifies|"yesterday" → thì quá khứ đơn → notified.
A number of customers ___ about the delay.|have complained|has complained|complaining|to complain|"A number of + danh từ số nhiều" đi với động từ số nhiều → have complained.
Kindly ___ your reservation 24 hours in advance.|confirm|confirmation|confirmed|confirming|"Kindly" giống "Please", theo sau là động từ nguyên mẫu → confirm.
"""),

dict(slug="toeic-tinh-tu", ico="🎨", en="Adjectives", vi="Tính từ", color="#8e24aa", theory="""
## Dấu hiệu nhận biết tính từ (hậu tố)
= -ive · -able/-ible · -ful · -less · -ous · -al · -ic · -ent/-ant · -ary · -y
- -ive: effective, expensive, competitive · -able/-ible: available, reliable, flexible
- -ful / -less: successful, useful, careless, wireless · -ous: various, numerous, generous
- -al: financial, additional, annual · -ic: economic, specific · -ent/-ant: efficient, significant
- Bẫy: friendly, costly, timely, likely, orderly đuôi -ly nhưng là TÍNH TỪ
Our staff are friendly and helpful.|Nhân viên của chúng tôi thân thiện và nhiệt tình.
## Vị trí của tính từ
= (a/the/my) + ___ + danh từ
= be · become · seem · remain · stay · look · appear + ___
= make · keep · find · consider + tân ngữ + ___
- Trạng từ đứng trước để bổ nghĩa cho tính từ: extremely popular, highly competitive
We will keep you informed of any changes.|Chúng tôi sẽ thông báo cho bạn về mọi thay đổi.
Customers found the service very helpful.|Khách hàng thấy dịch vụ rất hữu ích.
## Tính từ đuôi -ing và -ed
= -ing: gây ra cảm xúc (vật, sự việc) · -ed: cảm thấy (thường là người)
- interesting / interested · satisfying / satisfied · confusing / confused · exciting / excited
The results were disappointing.|Kết quả thật đáng thất vọng.
The manager was disappointed with the results.|Người quản lý thất vọng về kết quả.
## Tính từ dễ nhầm
= considerable (đáng kể) ≠ considerate (chu đáo)
= economic (thuộc kinh tế) ≠ economical (tiết kiệm)
= responsible (chịu trách nhiệm) ≠ responsive (phản hồi nhanh)
- reliable (đáng tin cậy) ≠ reliant on (phụ thuộc vào)
- comprehensive (toàn diện) ≠ comprehensible (dễ hiểu) · successful (thành công) ≠ successive (liên tiếp)
""", quiz="""
The new model is more ___ than the previous one.|reliable|rely|reliably|reliability|"is more + tính từ + than" (so sánh hơn) → reliable (đáng tin cậy).
We offer ___ prices on all office supplies.|competitive|compete|competition|competitively|Trước danh từ "prices" cần tính từ → competitive (cạnh tranh).
Tickets are ___ at the front desk.|available|availability|avail|availably|Sau "be" cần tính từ → available (có sẵn).
Ms. Park is ___ for training new employees.|responsible|responsibility|responsibly|responsive|"be responsible for" = chịu trách nhiệm về. Responsive nghĩa là "phản hồi nhanh".
The staff were ___ with the new schedule.|satisfied|satisfying|satisfy|satisfaction|Người cảm thấy hài lòng → tính từ đuôi -ed: satisfied with.
The training session was very ___.|informative|inform|information|informatively|Sau "very" và động từ "be" cần tính từ → informative (bổ ích, nhiều thông tin).
Please keep the door ___ during business hours.|open|openly|openness|opener|"keep + tân ngữ + tính từ" → keep the door open.
Sales showed a ___ increase last quarter.|significant|significance|signify|significantly|Trước danh từ "increase" cần tính từ → significant (đáng kể).
Our ___ representatives are available 24 hours a day.|friendly|friend|friendship|friendliness|"friendly" là tính từ dù có đuôi -ly, đứng trước danh từ "representatives".
The instructions were so ___ that nobody understood them.|confusing|confused|confuse|confusion|Hướng dẫn (vật) gây khó hiểu → tính từ đuôi -ing: confusing.
We need a more ___ car that uses less fuel.|economical|economic|economy|economist|"Economical" = tiết kiệm (nhiên liệu, tiền bạc); economic = thuộc về kinh tế.
Thank you for your ___ donation.|generous|generosity|generously|generosities|Giữa "your" và danh từ "donation" cần tính từ → generous (hào phóng).
Applicants must have ___ experience in sales.|previous|previously|preview|previewed|Trước danh từ "experience" cần tính từ → previous (trước đây).
The hotel is in a ___ location.|convenient|conveniently|convenience|conveniences|"a + tính từ + danh từ" → convenient (thuận tiện).
Mr. Tan found the proposal ___.|impressive|impress|impression|impressively|"find + tân ngữ + tính từ" → found the proposal impressive (ấn tượng).
"""),

dict(slug="toeic-trang-tu", ico="🚀", en="Adverbs", vi="Trạng từ", color="#00897b", theory="""
## Cách nhận biết trạng từ
= Tính từ + -ly → trạng từ: quick → quickly · careful → carefully
- -ble → -bly: possible → possibly · -y → -ily: easy → easily · -ic → -ically: automatic → automatically
- Không có -ly: fast, hard, late, early, well (good → well), soon, already, still, yet
## Vị trí của trạng từ
= S + ___ + V · V + O + ___
= have/has + ___ + V3 · be + ___ + V-ing/V3
= ___ + tính từ / trạng từ khác
= ___, S + V (đứng đầu câu, bổ nghĩa cho cả câu)
- Câu đã đủ thành phần (S + V + O) → chỗ trống còn lại thường là trạng từ
The price has recently increased.|Giá gần đây đã tăng.
The report was carefully reviewed.|Bản báo cáo đã được xem xét kỹ lưỡng.
Unfortunately, the flight was cancelled.|Thật không may, chuyến bay đã bị hủy.
## Trạng từ dễ nhầm
= hard (chăm chỉ) ≠ hardly (hầu như không)
= late (muộn) ≠ lately (gần đây) · high (cao) ≠ highly (rất, cực kỳ)
= near (gần) ≠ nearly (gần như) · close (gần) ≠ closely (chặt chẽ)
- Cụm hay gặp: highly recommended, highly qualified, closely monitor, nearly finished
- shortly = sắp, ngay sau đây · approximately = khoảng · immediately = ngay lập tức
## Trạng từ chỉ thời gian hay gặp
= already (đã… rồi) · yet (chưa — câu phủ định/câu hỏi) · still (vẫn)
= soon / shortly (sắp) · recently / lately (gần đây — thường với hiện tại hoàn thành)
The order has already been shipped.|Đơn hàng đã được gửi đi rồi.
The results are not available yet.|Kết quả vẫn chưa có.
""", quiz="""
The project was ___ completed ahead of schedule.|successfully|successful|success|succeed|"be + trạng từ + V3" → successfully.
Please read the contract ___ before signing it.|carefully|careful|care|cared|Câu đã đủ "read the contract" → cần trạng từ bổ nghĩa cho động từ → carefully.
Sales have ___ increased this year.|steadily|steady|steadiness|steadied|"have + trạng từ + V3" → steadily (đều đặn).
The museum is ___ located near the subway station.|conveniently|convenient|convenience|conveniences|"be + trạng từ + V3 (located)" → conveniently.
Mr. Ruiz is a ___ qualified engineer.|highly|high|height|higher|Trạng từ bổ nghĩa cho tính từ "qualified" → highly qualified (rất có năng lực).
___, the shipment arrived damaged.|Unfortunately|Unfortunate|Fortune|Misfortune|Đầu câu, trước dấu phẩy, bổ nghĩa cho cả câu → trạng từ Unfortunately.
The renovation is ___ finished; only the painting remains.|nearly|near|nearby|nearest|"nearly" = gần như; chỉ còn sơn nữa là xong.
We will respond to your inquiry ___.|shortly|short|shortage|shorten|Câu đã đủ thành phần → trạng từ shortly (sớm, ngay sau đây).
Our team has worked very ___ on this campaign.|hard|hardly|hardness|harden|"work hard" = làm việc chăm chỉ; hardly nghĩa là "hầu như không".
The new manager has not arrived ___.|yet|still|already|soon|Câu phủ định thì hiện tại hoàn thành, cuối câu → yet.
The software ___ saves your files every ten minutes.|automatically|automatic|automate|automation|Giữa chủ ngữ và động từ "saves" → trạng từ automatically.
Prices vary ___ depending on the season.|considerably|considerable|consider|consideration|Bổ nghĩa cho động từ "vary" → trạng từ considerably (đáng kể).
The event attracted ___ 500 visitors.|approximately|approximate|approximation|approximated|Trước con số dùng trạng từ approximately (khoảng).
The supervisor will ___ monitor the new employees.|closely|close|closed|closure|"closely monitor" = giám sát chặt chẽ; trạng từ đứng giữa will và động từ.
The new printer works ___ faster than the old one.|much|very|many|most|Bổ nghĩa cho so sánh hơn dùng much/far/even, không dùng very.
"""),

dict(slug="toeic-gioi-tu", ico="📍", en="Prepositions", vi="Giới từ", color="#f4511e", theory="""
## Giới từ chỉ thời gian
= at + giờ · on + thứ/ngày cụ thể · in + tháng/năm/mùa/buổi
- at 9 a.m., at noon · on Monday, on May 5 · in July, in 2025, in the morning
- in + khoảng thời gian = sau bao lâu nữa: The bus leaves in ten minutes.
## by · until · for · since · during · within
= by + mốc = trước / chậm nhất là (việc xong một lần)
= until + mốc = cho đến khi (việc kéo dài liên tục)
= for + khoảng thời gian · since + mốc thời gian (thì hoàn thành)
= during + danh từ (trong suốt) · within + khoảng (trong vòng)
- during + danh từ, còn while + mệnh đề: during the meeting / while we were meeting
Submit the report by Friday.|Nộp báo cáo chậm nhất vào thứ Sáu.
The store is open until 9 p.m.|Cửa hàng mở cửa đến 9 giờ tối.
## Giới từ chỉ nơi chốn
= at (một điểm) · in (bên trong) · on (trên bề mặt, tầng)
= between (giữa hai) · among (giữa nhiều) · across from / opposite (đối diện)
- next to / beside · near · behind · in front of · along · through
- at the front desk · in the conference room · on the second floor
## Giới từ cụm hay gặp trong TOEIC
= due to / because of / owing to + N (vì)
= despite / in spite of + N (mặc dù)
= in addition to · except for · according to · instead of · prior to (trước khi)
- Sau giới từ là danh từ hoặc V-ing, KHÔNG dùng mệnh đề (S + V)
- in charge of · in compliance with · on behalf of · in response to · regardless of
## Tính từ / động từ + giới từ
= responsible for · interested in · familiar with · aware of · eligible for
= apply for · comply with · depend on · participate in · respond to · consist of
All staff must comply with the safety rules.|Mọi nhân viên phải tuân thủ quy định an toàn.
""", quiz="""
The seminar will begin ___ 9:30 a.m.|at|on|in|for|Trước giờ cụ thể dùng "at".
Please submit your expense report ___ Friday.|by|until|since|during|Hạn chót (xong trước thứ Sáu) → by.
The library will be closed ___ the holiday period.|during|while|since|among|Trước danh từ "the holiday period" dùng during; while phải đi với mệnh đề.
Mr. Chen has worked here ___ 2018.|since|for|during|in|Thì hiện tại hoàn thành + mốc thời gian (2018) → since.
The flight was delayed ___ bad weather.|due to|because|although|despite|Trước cụm danh từ "bad weather", mang nghĩa nguyên nhân → due to; because phải đi với mệnh đề.
___ the high price, the product sold very well.|Despite|Although|Because of|However|Trước cụm danh từ, nghĩa tương phản → Despite; although cần mệnh đề.
The store stays open ___ 10 p.m. on weekends.|until|by|since|within|Hành động kéo dài liên tục đến một mốc → until.
Refunds are available ___ 30 days of purchase.|within|during|since|among|"within 30 days" = trong vòng 30 ngày.
The pharmacy is located ___ from the post office.|across|along|next|between|"across from" = đối diện.
Ms. Diaz is in charge ___ the marketing team.|of|for|with|at|Cụm cố định "in charge of" = phụ trách.
All visitors must comply ___ the safety rules.|with|to|for|on|"comply with" = tuân thủ.
___ attending the conference, Mr. Ito met several clients.|In addition to|Moreover|Besides that|Furthermore|Giới từ + V-ing → In addition to; moreover/furthermore là trạng từ liên kết, không đi với V-ing.
The bonus will be divided ___ the five team members.|among|between|within|through|Chia giữa nhiều hơn hai người → among.
Employees who work more than 40 hours are eligible ___ overtime pay.|for|to|of|with|"be eligible for + danh từ" = đủ điều kiện nhận.
Please read the manual ___ using the equipment.|before|until|since|during|"before + V-ing" = trước khi dùng; during không đi với V-ing.
"""),

dict(slug="toeic-lien-tu", ico="🔗", en="Conjunctions & Linking words", vi="Liên từ & Từ nối", color="#6d4c41", theory="""
## Liên từ hay giới từ? (dạng câu quan trọng nhất của Part 5)
= Liên từ + S + V (mệnh đề) · Giới từ + danh từ / V-ing
= because / since / as  ↔  because of / due to
= although / though / even though  ↔  despite / in spite of
= while  ↔  during · before / after (dùng được cả hai cách)
Although the price is high, the product sells well.|Mặc dù giá cao, sản phẩm vẫn bán chạy.
Despite the high price, the product sells well.|Bất chấp giá cao, sản phẩm vẫn bán chạy.
## Liên từ phụ thuộc thường gặp
= if · unless (trừ khi) · provided that / as long as (miễn là)
= once (một khi) · as soon as (ngay khi) · until · when · whenever
= so that / in order that (để) · whereas / while (trong khi — đối lập)
- Mệnh đề thời gian/điều kiện dùng hiện tại thay cho tương lai
As soon as the order arrives, we will call you.|Ngay khi hàng đến, chúng tôi sẽ gọi cho bạn.
## Liên từ tương quan (đi theo cặp)
= both A and B · either A or B · neither A nor B
= not only A but (also) B · whether A or B · A as well as B
- Với either…or / neither…nor, động từ chia theo B (chủ ngữ gần nhất)
Neither the manager nor the employees were informed.|Cả quản lý lẫn nhân viên đều không được thông báo.
## Trạng từ liên kết (thường đứng đầu câu, có dấu phẩy)
= however (tuy nhiên) · therefore / as a result (vì vậy)
= moreover / furthermore / in addition (hơn nữa) · otherwise (nếu không thì)
= meanwhile (trong khi đó) · instead (thay vào đó) · for example (ví dụ)
- Không dùng however/therefore để nối hai mệnh đề chỉ bằng dấu phẩy
The deadline is tomorrow. Therefore, please send your files today.|Hạn chót là ngày mai. Vì vậy, vui lòng gửi file trong hôm nay.
""", quiz="""
___ the weather was bad, the event was a success.|Although|Despite|Because of|However|Theo sau là mệnh đề (the weather was bad), nghĩa tương phản → liên từ Although.
The meeting was cancelled ___ the manager was sick.|because|because of|due to|despite|Theo sau là mệnh đề → liên từ because; because of/due to đi với danh từ.
Please call us ___ you have any questions.|if|unless|despite|whereas|"if" = nếu bạn có câu hỏi thì hãy gọi.
You cannot enter the lab ___ you have a security badge.|unless|if|although|because|"unless" = trừ khi có thẻ an ninh.
___ the order is confirmed, we will ship it immediately.|As soon as|Despite|During|Due to|Theo sau là mệnh đề → liên từ As soon as (ngay khi).
Both the director ___ the CFO will attend the meeting.|and|or|nor|but|Cặp "both … and".
Neither the printer ___ the scanner is working.|nor|or|and|but|Cặp "neither … nor".
The product is not only cheap ___ durable.|but also|and also|or also|as well|Cặp "not only … but also".
Sales increased last month. ___, profits fell.|However|Because|Although|Despite|Đầu câu, có dấu phẩy, nối hai ý trái ngược → trạng từ liên kết However.
Please arrive early ___ we can start on time.|so that|because of|in spite of|due to|Theo sau là mệnh đề chỉ mục đích → so that (để).
___ the renovation, the restaurant will be closed.|During|While|Although|Unless|Trước danh từ "the renovation" → giới từ During.
Mr. Lopez read the report ___ he was waiting for the train.|while|during|despite|because of|Theo sau là mệnh đề → liên từ while (trong khi).
The tickets were sold out. ___, we watched the show online.|Instead|Although|Unless|Whereas|"Instead" = thay vào đó, đứng đầu câu có dấu phẩy.
You can pay ___ by cash or by credit card.|either|neither|both|whether|Cặp "either … or" = hoặc … hoặc.
Please save your work regularly; ___, you may lose your data.|otherwise|unless|moreover|therefore|"otherwise" = nếu không thì.
"""),

dict(slug="toeic-dai-tu", ico="👥", en="Pronouns", vi="Đại từ", color="#3949ab", theory="""
## Bảng đại từ
= Chủ ngữ: I · you · he · she · it · we · they
= Tân ngữ: me · you · him · her · it · us · them
= Tính từ sở hữu (+ danh từ): my · your · his · her · its · our · their
= Đại từ sở hữu (không có danh từ): mine · yours · his · hers · ours · theirs
= Phản thân: myself · yourself · himself · herself · itself · ourselves · themselves
- Trước động từ → chủ ngữ · sau động từ/giới từ → tân ngữ · trước danh từ → tính từ sở hữu
## Đại từ phản thân
= S + V + oneself (chủ ngữ và tân ngữ là một người)
= by + oneself = tự mình, một mình
- Không dùng phản thân làm chủ ngữ: "Himself will…" ✗
Ms. Ford prepared the presentation by herself.|Cô Ford tự mình chuẩn bị bài thuyết trình.
## its hay it's · their hay there
= its + danh từ (của nó) · it's = it is
= their + danh từ (của họ) · there is/are · they're = they are
The company announced its new CEO.|Công ty đã công bố giám đốc điều hành mới.
## another · other · the other · others · those
= another + danh từ số ít (một cái khác) · other + danh từ số nhiều
= the other (cái còn lại trong hai) · others (những cái khác) · each other (lẫn nhau)
= those who = những người mà · those = thay cho danh từ số nhiều đã nhắc
Those who wish to attend should register by Monday.|Những ai muốn tham dự nên đăng ký trước thứ Hai.
""", quiz="""
Ms. Grant asked ___ assistant to book a flight.|her|she|hers|herself|Trước danh từ "assistant" cần tính từ sở hữu → her.
Mr. Davis repaired the printer by ___.|himself|him|his|he|"by + đại từ phản thân" = tự mình → by himself.
The company announced ___ annual results yesterday.|its|it's|it|itself|Trước cụm danh từ cần tính từ sở hữu "its"; it's = it is.
Please send ___ the revised contract as soon as possible.|us|we|our|ours|Sau động từ "send" cần đại từ tân ngữ → us.
These documents are ___, not mine.|yours|your|you|yourself|Không có danh từ theo sau, song song với "mine" → đại từ sở hữu yours.
___ who want to join the tour should meet in the lobby.|Those|They|Them|Their|"Those who" = những người mà.
Employees should respect each ___ opinions.|other's|another|others|other|"each other's + danh từ" = (ý kiến) của nhau.
We have two printers. One is broken, but ___ works fine.|the other|other|another|others|Chỉ có hai cái: một cái… cái còn lại → the other.
___ will receive a certificate after the course.|They|Them|Their|Theirs|Vị trí chủ ngữ trước động từ "will receive" → They.
The managers met with the clients to discuss ___ concerns.|their|they|them|themselves|Trước danh từ "concerns" cần tính từ sở hữu → their.
This cup is dirty. Could you bring me ___ one?|another|other|others|the others|"another + danh từ số ít" = một cái khác.
Ms. Wong wrote the report ___ because her assistant was on leave.|herself|her|hers|she|Nhấn mạnh tự mình làm → đại từ phản thân herself.
Mr. Patel and I have known ___ for ten years.|each other|one other|other|others|"each other" = nhau, lẫn nhau.
Our products are cheaper than ___ of our competitors.|those|that|them|they|"those" thay cho danh từ số nhiều "products" đã nhắc.
Visitors must sign in when ___ arrive.|they|them|their|themselves|Chủ ngữ của mệnh đề "when … arrive" → they.
"""),

dict(slug="toeic-ho-tu", ico="🌳", en="Word families", vi="Họ từ – chọn đúng từ loại", color="#43a047", theory="""
## Cách làm câu hỏi từ loại (chiếm khoảng 1/3 Part 5)
= Bước 1: nhìn 4 đáp án — cùng gốc từ, khác đuôi → câu hỏi từ loại
= Bước 2: xem từ đứng trước và sau chỗ trống → xác định vị trí cần loại từ gì
= Bước 3: chọn theo hậu tố, không cần dịch cả câu
- the/a/my + ___ + of/động từ → danh từ · a/the + ___ + danh từ → tính từ
- be/become + ___ → tính từ · have + ___ + V3, be + ___ + V3 → trạng từ
- will/can/to + ___ → động từ · câu đã đủ thành phần → trạng từ
## Hậu tố tổng hợp
= Danh từ: -tion · -ment · -ness · -ity · -ance/-ence · -er/-or · -ee · -ist
= Động từ: -ize · -ify · -en · -ate
= Tính từ: -ive · -able · -ful · -less · -ous · -al · -ic · -ent/-ant
= Trạng từ: tính từ + -ly
## Một từ có nhiều tính từ
- satisfactory (đạt yêu cầu) / satisfied (hài lòng) / satisfying (gây hài lòng)
- economic (kinh tế) / economical (tiết kiệm) · considerable (đáng kể) / considerate (chu đáo)
- Khi có hai tính từ trong đáp án, phải dịch nghĩa để chọn
""", families="""
analysis|analyze|analytical|analytically
application|apply|applicable|—
attraction|attract|attractive|attractively
availability|—|available|—
comparison|compare|comparable|comparably
competition|compete|competitive|competitively
completion|complete|complete|completely
confidence|—|confident|confidently
consideration|consider|considerable|considerably
creation|create|creative|creatively
decision|decide|decisive|decisively
difference|differ|different|differently
efficiency|—|efficient|efficiently
expansion|expand|expansive|—
extension|extend|extensive|extensively
finance|finance|financial|financially
impression|impress|impressive|impressively
information|inform|informative|—
innovation|innovate|innovative|innovatively
operation|operate|operational|operationally
preference|prefer|preferable|preferably
production|produce|productive|productively
profit|profit|profitable|profitably
reliability|rely|reliable|reliably
responsibility|—|responsible|responsibly
satisfaction|satisfy|satisfactory / satisfied|satisfactorily
simplicity|simplify|simple|simply
strength|strengthen|strong|strongly
success|succeed|successful|successfully
variety|vary|various|variously
width|widen|wide|widely
accuracy|—|accurate|accurately
convenience|—|convenient|conveniently
cooperation|cooperate|cooperative|cooperatively
""", quiz="""
The ___ of the new system took three months.|installation|install|installed|installs|Giữa "The" và "of" cần danh từ → installation (việc lắp đặt).
Ms. Kato speaks English very ___.|fluently|fluent|fluency|fluencies|Bổ nghĩa cho động từ "speaks" → trạng từ fluently.
Our goal is to make the process more ___.|efficient|efficiency|efficiently|efficiencies|"make + tân ngữ + (more) tính từ" → efficient.
The team worked ___ to finish the project on time.|efficiently|efficient|efficiency|efficiencies|Bổ nghĩa cho động từ "worked" → trạng từ efficiently.
Prices may ___ depending on the season.|vary|various|variety|variously|Sau "may" cần động từ nguyên mẫu → vary (thay đổi).
We offer a wide ___ of products.|variety|vary|various|variously|"a wide variety of" = rất nhiều loại; giữa tính từ và "of" cần danh từ.
The data must be recorded ___.|accurately|accurate|accuracy|accurateness|Câu bị động đã đủ thành phần → trạng từ accurately.
The ___ of this report is very important.|accuracy|accurate|accurately|accurateness|Chủ ngữ, giữa "The" và "of" → danh từ accuracy (độ chính xác).
The new packaging is very ___ to young customers.|attractive|attract|attraction|attractively|Sau "is very" cần tính từ → attractive (hấp dẫn).
Mr. Diaz is a ___ leader who always makes quick choices.|decisive|decide|decision|decisively|"a + tính từ + danh từ (leader)" → decisive (quyết đoán).
The company's profits have grown ___.|considerably|considerable|consider|consideration|Bổ nghĩa cho động từ "have grown" → trạng từ considerably.
The training program aims to ___ teamwork.|strengthen|strong|strength|strongly|Sau "to" cần động từ → strengthen (củng cố, đuôi -en).
Investing in this market could be very ___.|profitable|profit|profitably|profits|Sau "be very" cần tính từ → profitable (có lợi nhuận).
Thank you for your ___.|cooperation|cooperate|cooperative|cooperatively|Sau "your" cần danh từ → cooperation (sự hợp tác).
The results of the inspection were ___, so the factory passed.|satisfactory|satisfy|satisfaction|satisfactorily|Sau "were" cần tính từ; kết quả "đạt yêu cầu" → satisfactory.
Our new product is ___ with most smartphones.|compatible|compatibility|compatibly|compatibilities|Sau "is" cần tính từ → compatible with (tương thích với).
"""),
]
