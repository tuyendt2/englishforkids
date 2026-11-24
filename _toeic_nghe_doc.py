# Luyện thi TOEIC — Nghe hiểu (Part 1, 2, 3, 4) và Đọc hiểu (Part 6, 7)
#
# Bài nghe dùng giọng đọc có sẵn của trình duyệt (không cần file âm thanh).
#   Part 1 (items): mỗi dòng  tên ảnh|đúng|sai|sai|sai|giải thích   (ảnh vẽ trong _toeic_part1_svg.py)
#   Part 2 (items): mỗi dòng  câu hỏi|đáp án đúng|sai|sai|giải thích   (3 lựa chọn, chỉ nghe, không in ra)
#   Part 3/4 (sets): script = các dòng "M: …" / "W: …" (M = giọng nam, W = giọng nữ)
#                   quiz   = mỗi dòng  câu hỏi|đúng|sai|sai|sai|giải thích
# Bài đọc:
#   Part 6 (sets): text có chỗ trống [1] [2] [3] [4]; quiz mỗi dòng  đúng|sai|sai|sai|giải thích (theo thứ tự chỗ trống)
#   Part 7 (sets): text là bài đọc; quiz mỗi dòng  câu hỏi|đúng|sai|sai|sai|giải thích
# Trong text, dòng trống = xuống đoạn; dòng bắt đầu bằng "### " = tiêu đề văn bản (khi có 2 văn bản).

LISTEN_GROUP = "🎧 Nghe hiểu (Listening) – Part 1, 2, 3, 4"
READ_GROUP = "📖 Đọc hiểu (Reading) – Part 6, 7"

LISTEN = [
dict(slug="toeic-part-1", part=1, ico="🖼️", en="Part 1 – Photographs", vi="Mô tả tranh", color="#2e7d32",
tips="""
## Cách làm Part 1
= Nhìn tranh trước khi nghe: ai, đang làm gì, ở đâu, đồ vật nào nổi bật
- Tranh có người → chú ý động từ V-ing: typing, watering, shaking hands, pointing at…
- Tranh không có người → đáp án hay dùng bị động: "Boxes have been stacked", "Cars are parked"; loại ngay câu nhắc tới người
- Bẫy hay gặp: đúng đồ vật nhưng sai hành động (carrying a ladder ≠ standing on a ladder), hoặc từ phát âm gần giống
- 4 câu (A)(B)(C)(D) chỉ được đọc một lần, không in ra — nghe xong câu nào loại ngay câu đó
The man is typing on a laptop.|Người đàn ông đang gõ phím trên máy tính xách tay.
""", items="""
p1-laptop|The man is typing on a laptop.|The man is drinking from a mug.|The man is putting on his jacket.|The man is closing a window.|Tay anh ấy đặt trên bàn phím laptop → typing. Cốc và cửa sổ có trong tranh nhưng không ai đang dùng.
p1-water|She's watering some plants.|She's planting a tree.|She's sweeping the path.|She's buying flowers at a market.|Cô ấy cầm bình tưới nước vào chậu cây → watering some plants.
p1-handshake|They're shaking hands.|They're waving goodbye.|They're carrying a box together.|They're sitting across from each other.|Hai người đứng đối diện, nắm tay nhau → shaking hands.
p1-warehouse|Boxes have been stacked on the shelves.|A worker is driving a forklift.|The shelves are being assembled.|Some boxes are being loaded onto a truck.|Tranh không có người → loại câu có người (worker) và câu bị động tiếp diễn "are being…" (cần người đang làm). Hộp đã được xếp lên kệ → have been stacked.
p1-bench|A woman is reading on a bench.|A woman is painting a bench.|A woman is walking under a tree.|A woman is putting a book on a shelf.|Người phụ nữ ngồi trên ghế dài, cầm sách mở → reading on a bench.
p1-ladder|A man is standing on a ladder.|A man is carrying a ladder.|A man is painting the wall.|A man is sitting on the floor.|Anh ấy đứng trên thang, với tay lên đèn → standing on a ladder. "Carrying a ladder" là bẫy: đúng đồ vật, sai hành động.
p1-meeting|A man is pointing at a chart.|Some people are leaving the room.|A man is erasing the board.|The chairs are stacked in a corner.|Người đàn ông đứng chỉ tay vào biểu đồ trên bảng → pointing at a chart.
p1-street|Some cars are parked along the street.|Cars are being washed.|People are crossing the street.|A bus is stopping at the station.|Không có người → loại câu có người. Xe đang đỗ dọc đường → are parked along the street.
p1-chef|A cook is stirring a pot.|A cook is washing the dishes.|A cook is serving food to customers.|A cook is opening the refrigerator.|Đầu bếp cầm muôi khuấy nồi đang bốc hơi → stirring a pot.
p1-phone|She's talking on the phone.|She's writing on a whiteboard.|She's handing over a key.|She's hanging up a picture.|Cô ấy áp điện thoại lên tai → talking on the phone.
p1-bikes|Bicycles are lined up in a rack.|Someone is riding a bicycle.|A bicycle is being repaired.|The bicycles are lying on the grass.|Không có người; các xe đạp xếp thành hàng ở giá → are lined up in a rack.
p1-cart|He's pushing a shopping cart.|He's stocking the shelves.|He's paying at the register.|He's carrying a basket.|Anh ấy hai tay đẩy xe đẩy hàng → pushing a shopping cart.
"""),
dict(slug="toeic-part-2", part=2, ico="💬", en="Part 2 – Question-Response", vi="Hỏi – Đáp", color="#00838f",
tips="""
## Cách làm Part 2
= Nghe từ để hỏi đầu câu: Who / What / When / Where / Why / How / Do-Does / Is-Are …
- When → thời gian (next Monday, at 3 o'clock) · Where → nơi chốn (in the lobby, on the desk) · Who → người, chức danh, phòng ban
- Đáp án lặp lại đúng từ trong câu hỏi hoặc từ phát âm gần giống thường là bẫy (copy – coffee, meeting – meet)
- Câu trả lời gián tiếp vẫn đúng: "Shall we start?" → "We're still waiting for Mr. Lee." (chưa bắt đầu được)
- Câu hỏi Yes/No có thể được trả lời mà không có Yes/No: "Have you finished the report?" → "I'll send it this afternoon."
Where is the meeting being held? → In conference room B.|Cuộc họp được tổ chức ở đâu? → Ở phòng họp B.
""", items="""
When will the new printer be delivered?|Sometime on Thursday morning.|In the supply room.|Yes, it prints in color.|Hỏi "When" → cần thời gian. "In the supply room" trả lời Where; câu C bẫy từ "printer – prints".
Where should I put these boxes?|Just leave them by the door.|About twenty of them.|Yes, I put it there.|Hỏi "Where" → nơi chốn: "by the door". Câu B trả lời How many.
Who is in charge of the marketing budget?|Ms. Patel handles that.|It's too expensive.|At the end of the month.|Hỏi "Who" → người: Ms. Patel. Câu B bẫy chủ đề tiền; câu C trả lời When.
Why was the flight delayed?|Because of the heavy snow.|At gate twelve.|I'd prefer a window seat.|Hỏi "Why" → lý do: "Because of…".
How often do you check your e-mail?|Several times a day.|By train, usually.|It's a new e-mail address.|"How often" hỏi tần suất → "several times a day". "By train" trả lời How (phương tiện).
Would you like some coffee?|No thanks, I just had some.|He likes his job.|The copy machine is broken.|Lời mời "Would you like…?" → nhận/từ chối. Câu C bẫy âm "coffee – copy".
Have you finished the sales report yet?|I'll send it to you this afternoon.|Sales went up last quarter.|Yes, the store is open.|Trả lời gián tiếp: chưa xong, chiều nay sẽ gửi. Câu B lặp từ "sales".
Can you help me move this desk?|Sure, where do you want it?|It's a wooden desk.|I moved here last year.|Lời nhờ "Can you…?" → đồng ý/từ chối. Câu C bẫy "move – moved".
Which bus goes to the airport?|The number 15 does.|It takes about an hour.|I'll pick you up.|"Which bus" → xác định chiếc xe: "The number 15".
Isn't the store open on Sundays?|Only in December.|I'll store them in the cabinet.|Yes, it's a large store.|Câu hỏi phủ định: chỉ mở Chủ nhật vào tháng 12. Câu B bẫy "store" (cất giữ).
Shall we start the meeting now?|We're still waiting for Mr. Lee.|It started raining.|In the main hall.|Trả lời gián tiếp: chưa bắt đầu được vì còn chờ ông Lee.
How much does it cost to ship this package?|About twenty dollars.|By express mail.|It's a large ship.|"How much" → giá tiền. Câu C bẫy "ship" (con tàu).
Whose jacket is this?|I think it's Tom's.|It's very warm outside.|Yes, it's on the chair.|"Whose" hỏi chủ sở hữu → "Tom's".
What time does the training session begin?|At nine thirty sharp.|In the training room.|Two new trainees.|"What time" → giờ cụ thể.
Do you know where the nearest bank is?|There's one across the street.|I don't have an account.|At ten o'clock.|Câu hỏi gián tiếp về nơi chốn → "across the street".
The air conditioner isn't working.|I'll call maintenance right away.|It's working hours.|Yes, I'll air the room.|Câu trần thuật báo vấn đề → phản ứng xử lý. Câu B/C bẫy "working", "air".
Should we take a taxi or walk to the restaurant?|Let's walk, it's not far.|Yes, a table for four.|I ate there yesterday.|Câu hỏi lựa chọn "A or B" → chọn một: walk.
Why don't we order lunch for the team?|That's a great idea.|Because the order was late.|At about noon.|"Why don't we…?" là lời đề nghị, không hỏi lý do → đồng ý.
Who's going to replace Ms. Chen while she's on leave?|Mr. Ito from accounting.|She left early today.|It's a nice place.|Hỏi người thay thế → Mr. Ito. Câu C bẫy "replace – place".
How long have you worked here?|For about five years.|It's a long way.|Every weekday.|"How long" + hiện tại hoàn thành → khoảng thời gian "for five years".
Where can I find the user manual?|It should be in the top drawer.|Yes, I can find it.|It's very useful.|Hỏi nơi chốn → "in the top drawer".
Are you attending the conference next week?|I haven't decided yet.|It was very interesting.|The conference room is booked.|Trả lời chưa quyết định là hợp lý. Câu B sai thì (quá khứ).
When is the deadline for the proposal?|It's due this Friday.|I proposed a new plan.|In the director's office.|"When … deadline" → "due this Friday". Câu B bẫy "proposal – proposed".
Could you send me a copy of the contract?|I'll e-mail it to you now.|I'd like a cup of coffee.|The contract was signed.|Lời nhờ gửi tài liệu → "I'll e-mail it now".
What did you think of the presentation?|It was very informative.|At two o'clock.|I'll present it tomorrow.|Hỏi ý kiến → nhận xét "very informative".
"""),
dict(slug="toeic-part-3", part=3, ico="👥", en="Part 3 – Conversations", vi="Hội thoại", color="#00695c",
tips="""
## Cách làm Part 3
= Đọc 3 câu hỏi TRƯỚC khi nghe → biết cần nghe gì (ai, ở đâu, vấn đề, sẽ làm gì tiếp)
- Câu 1 thường hỏi chủ đề / nơi chốn / nghề nghiệp → nằm ở 1–2 câu đầu hội thoại
- Câu cuối thường hỏi "What will the man probably do next?" → nghe câu cuối hội thoại (I'll…, Let me…)
- Đáp án đúng thường diễn đạt lại (paraphrase): "the printer is broken" → "a machine is not working"
What is the problem? → The order has not arrived.|Vấn đề là gì? → Đơn hàng chưa đến.
""", sets=[
dict(script="""
W: Hi, I ordered a laptop from your website last week, but it still hasn't arrived. The order number is 4-5-7-2.
M: I'm sorry about that. Let me check… It looks like the package was sent to your old address.
W: Oh no. I moved last month. Can you send it to my new address instead?
M: Of course. I'll contact the delivery company right now and update the address for you.
""", quiz="""
What is the woman's problem?|An order has not arrived.|A laptop is damaged.|A website is not working.|She was charged twice.|"It still hasn't arrived" → đơn hàng chưa đến.
Why was there a delay?|It was sent to the wrong address.|The item was out of stock.|The order number was incorrect.|The delivery truck broke down.|"The package was sent to your old address" → gửi nhầm địa chỉ.
What will the man probably do next?|Contact a delivery company.|Issue a refund.|Send a new laptop.|Visit the woman's home.|"I'll contact the delivery company right now".
"""),
dict(script="""
M: Jenny, are you going to the training workshop on Thursday?
W: I'd like to, but I have a meeting with a client that afternoon. Is it going to be repeated?
M: I think so. Human Resources said there'll be another session next month.
W: Great. I'll sign up for that one, then. Do you know who I should talk to?
M: Just send an e-mail to Mark Davis in HR.
""", quiz="""
What are the speakers mainly discussing?|A training workshop.|A client's complaint.|A job interview.|A new office.|Hội thoại xoay quanh "the training workshop on Thursday".
Why can't the woman attend on Thursday?|She has a client meeting.|She will be on vacation.|She is not eligible.|She has a doctor's appointment.|"I have a meeting with a client that afternoon".
What does the man suggest the woman do?|E-mail someone in Human Resources.|Ask her manager for permission.|Change her meeting time.|Read a training manual.|"Just send an e-mail to Mark Davis in HR".
"""),
dict(script="""
W: Good evening, I'd like to book a table for six people this Saturday at seven.
M: Let me see… I'm afraid we're fully booked at seven. We do have a table available at eight thirty.
W: Hmm, that's a little late. We'll be celebrating my father's birthday. Is there anything earlier?
M: We have a private room that's free at six. It's a bit more expensive, but it's quieter.
W: That sounds perfect. We'll take it.
""", quiz="""
Where does the man most likely work?|At a restaurant.|At a hotel.|At a travel agency.|At a bakery.|"Book a table for six people" → nhà hàng.
What is the purpose of the woman's event?|A birthday celebration.|A business dinner.|A retirement party.|A wedding anniversary.|"Celebrating my father's birthday".
What does the woman decide to do?|Reserve a private room.|Come at eight thirty.|Choose another restaurant.|Reduce the number of guests.|Cô chọn phòng riêng lúc 6 giờ: "That sounds perfect. We'll take it."
"""),
dict(script="""
M: Excuse me, the copy machine on the third floor is jammed again. It's the second time this week.
W: Really? I'll call the repair company. In the meantime, you can use the one in the lobby.
M: OK, but I need to print one hundred brochures for tomorrow's trade show.
W: In that case, it might be faster to use the print shop across the street. Just keep the receipt and you'll be reimbursed.
""", quiz="""
What problem does the man mention?|A machine is not working.|A delivery is late.|A room is too small.|A document has errors.|"The copy machine … is jammed again" → máy bị kẹt (diễn đạt lại: not working).
What does the man need to do by tomorrow?|Print some brochures.|Attend a job interview.|Book a hotel room.|Repair a computer.|"I need to print one hundred brochures for tomorrow's trade show".
What does the woman tell the man to keep?|A receipt.|A brochure.|A key.|A contract.|"Just keep the receipt and you'll be reimbursed".
"""),
dict(script="""
W: Mr. Garcia, thanks for coming in. I've reviewed your résumé, and your experience in sales is impressive.
M: Thank you. I've worked in retail for eight years, and I managed a team of twelve at my last job.
W: That's great. This position also requires some travel, about one week every month. Would that be a problem?
M: Not at all. I actually enjoy visiting clients in person.
W: Wonderful. We'll make our final decision by Friday, and I'll call you either way.
""", quiz="""
What is the purpose of the conversation?|A job interview.|A sales presentation.|A performance review.|A client meeting.|Người phụ nữ xem CV, hỏi về vị trí → phỏng vấn xin việc.
What does the woman say about the position?|It involves some travel.|It is a part-time job.|It requires a degree in finance.|It starts next week.|"This position also requires some travel".
When will a decision be made?|By Friday.|Tomorrow morning.|Next month.|In two weeks.|"We'll make our final decision by Friday".
"""),
dict(script="""
M: Hello, this is Kevin from Blue Sky Travel. I'm calling about your trip to Singapore next month.
W: Oh, hi Kevin. Is there a problem with my booking?
M: Unfortunately, your flight on the fifth has been cancelled by the airline. I can put you on a flight on the fourth or the sixth.
W: My conference starts on the sixth, so I'd better leave on the fourth. Will I need an extra night at the hotel?
M: Yes, but don't worry. I'll arrange that, and the airline will cover the cost.
""", quiz="""
Why is the man calling?|To report a flight cancellation.|To confirm a hotel payment.|To offer a discount.|To sell travel insurance.|"Your flight on the fifth has been cancelled".
When will the woman most likely leave?|On the fourth.|On the fifth.|On the sixth.|On the seventh.|"I'd better leave on the fourth".
What does the man say about the extra hotel night?|The airline will pay for it.|It is not available.|The woman must pay for it.|It includes breakfast.|"The airline will cover the cost".
"""),
dict(script="""
W: Ahmed, how are the preparations for the product launch going?
M: Pretty well. The advertisements are ready, but the supplier says the packaging will be a week late.
W: A week? The launch is scheduled for the fifteenth. Can we still make it?
M: I've asked them to send half of the order early. That should be enough for the first few days of sales.
W: Good thinking. Let's meet with the sales team tomorrow to update them.
""", quiz="""
What event are the speakers preparing for?|A product launch.|A company anniversary.|A trade show.|A staff training.|"Preparations for the product launch".
What problem does the man mention?|Packaging will be delayed.|An advertisement has an error.|Sales are declining.|A team member is sick.|"The packaging will be a week late".
What does the woman suggest?|Meeting with the sales team.|Changing the supplier.|Postponing the launch.|Hiring more staff.|"Let's meet with the sales team tomorrow".
"""),
dict(script="""
M: Hi, I'm interested in joining the gym. What kinds of membership do you offer?
W: We have monthly and yearly memberships. The yearly one costs more up front, but you save about thirty percent.
M: I'm moving to another city in six months, so I don't think a yearly membership makes sense.
W: Then the monthly plan is better for you. And this week there's no registration fee.
M: Great. Can I sign up now? I have my credit card with me.
""", quiz="""
Where is the conversation taking place?|At a fitness center.|At a bank.|At a real estate agency.|At a library.|"Joining the gym" → phòng tập thể hình (fitness center).
Why doesn't the man choose a yearly membership?|He is moving soon.|It is too expensive.|He travels often.|He prefers to exercise at home.|"I'm moving to another city in six months".
What is offered this week?|No registration fee.|A free personal trainer.|A thirty percent discount.|A free month.|"This week there's no registration fee".
"""),
]),
dict(slug="toeic-part-4", part=4, ico="📢", en="Part 4 – Short Talks", vi="Bài nói ngắn", color="#0277bd",
tips="""
## Cách làm Part 4
= Bài nói 1 người: thông báo, tin nhắn thoại, quảng cáo, bản tin, hướng dẫn tham quan
- Câu đầu bài nói cho biết người nói là ai / gửi cho ai / mục đích ("Hello, this is…", "Attention, passengers…")
- Nghe số liệu, thời gian, ngày tháng; câu hỏi thường hỏi lại chính xác các chi tiết này
- Cuối bài thường có yêu cầu: "Please call me back…", "Don't forget to…" → câu hỏi "What are listeners asked to do?"
Attention, passengers. The train to Boston will depart from platform 4.|Hành khách chú ý. Tàu đi Boston sẽ khởi hành từ sân ga số 4.
""", sets=[
dict(script="""
W: Attention, shoppers. Our store will be closing in fifteen minutes. Please bring your final purchases to the checkout counters at the front of the store. Don't forget that our summer sale continues all week, with discounts of up to fifty percent on outdoor furniture. Thank you for shopping at Green Home, and have a pleasant evening.
""", quiz="""
Where is the announcement being made?|In a store.|At an airport.|In a museum.|At a restaurant.|"Attention, shoppers… checkout counters" → cửa hàng.
What will happen in fifteen minutes?|The store will close.|A sale will start.|A delivery will arrive.|A new product will be shown.|"Our store will be closing in fifteen minutes".
What is on sale this week?|Outdoor furniture.|Kitchen equipment.|Summer clothing.|Garden tools.|"Discounts of up to fifty percent on outdoor furniture".
"""),
dict(script="""
M: Hi, Ms. Robinson. This is Daniel from Lakeside Dental Clinic. I'm calling to remind you of your appointment tomorrow at ten a.m. with Doctor Kim. Please arrive about ten minutes early to fill out a short form. If you need to reschedule, call us at 555-0182 before five o'clock today. Thank you, and see you tomorrow.
""", quiz="""
What is the purpose of the message?|To remind a patient of an appointment.|To cancel an appointment.|To introduce a new doctor.|To request a payment.|"Calling to remind you of your appointment".
What is the listener asked to do?|Arrive early.|Bring a medical record.|Pay in advance.|Call another clinic.|"Please arrive about ten minutes early to fill out a short form".
According to the speaker, why would the listener call the clinic?|To change the appointment time.|To ask for directions.|To get test results.|To order medicine.|"If you need to reschedule, call us…".
"""),
dict(script="""
W: Good morning, everyone, and welcome to your first day at Norton Electronics. I'm Sarah, and I'll be leading your orientation today. This morning, we'll tour the factory and the research lab. After lunch, which will be served in the cafeteria on the second floor, you'll meet your team leaders. Before we start, please make sure you're wearing the safety glasses in your welcome kit.
""", quiz="""
Who most likely are the listeners?|New employees.|Factory inspectors.|Potential customers.|Job applicants.|"Welcome to your first day" → nhân viên mới.
What will the listeners do after lunch?|Meet their team leaders.|Tour the research lab.|Fill out some forms.|Watch a safety video.|"After lunch… you'll meet your team leaders".
What are the listeners asked to do before the tour?|Wear safety glasses.|Sign a contract.|Leave their bags in a locker.|Turn off their phones.|"Please make sure you're wearing the safety glasses".
"""),
dict(script="""
M: And now for the local business news. The city's largest bookstore, Page Turner, announced yesterday that it will open a second location downtown next spring. The new store will include a café and a children's reading area. The company says it expects to hire about forty new employees. Job applications can be submitted on the company's website starting next Monday.
""", quiz="""
What is the news report mainly about?|The opening of a new store.|The closing of a café.|A new city library.|A change in management.|"Will open a second location downtown".
What will the new location include?|A café.|A movie theater.|A parking garage.|A printing service.|"The new store will include a café and a children's reading area".
How can people apply for jobs?|Online.|In person.|By telephone.|By mail.|"Job applications can be submitted on the company's website".
"""),
dict(script="""
W: Welcome aboard the City River Tour. Our cruise today will last about ninety minutes. On your left, you'll soon see the old City Hall, which was built more than two hundred years ago. Refreshments are available at the snack bar on the lower deck. For your safety, please remain seated while the boat is moving, and keep your hands inside the boat at all times.
""", quiz="""
Who most likely is the speaker?|A tour guide.|A ship engineer.|A city official.|A restaurant owner.|"Welcome aboard the City River Tour" → hướng dẫn viên.
How long will the tour last?|About an hour and a half.|About thirty minutes.|About two hours.|About forty-five minutes.|"About ninety minutes" = một tiếng rưỡi.
Where can listeners get refreshments?|On the lower deck.|At City Hall.|At the ticket office.|On the upper deck.|"Refreshments are available at the snack bar on the lower deck".
"""),
dict(script="""
M: Before we end this meeting, I have one more announcement. Starting next month, our office will switch to a new accounting software. To help everyone learn the system, the IT department will hold two training sessions, one on Tuesday morning and one on Thursday afternoon. Please sign up for one of them by this Friday using the online form I'll e-mail you after the meeting.
""", quiz="""
What change is the speaker announcing?|New software will be used.|The office will move.|A department will be closed.|Working hours will change.|"Our office will switch to a new accounting software".
How many training sessions will be held?|Two.|One.|Three.|Four.|"Two training sessions, one on Tuesday… one on Thursday".
What will the speaker send after the meeting?|An online form.|A training manual.|A meeting agenda.|A software license.|"Using the online form I'll e-mail you after the meeting".
"""),
]),
]

READ = [
dict(slug="toeic-part-6", part=6, ico="🧩", en="Part 6 – Text Completion", vi="Điền vào đoạn văn", color="#5e35b1",
tips="""
## Cách làm Part 6
= Mỗi đoạn văn 4 chỗ trống: 3 câu ngữ pháp / từ vựng + 1 câu chọn CÂU phù hợp để điền
- Đọc cả câu trước và câu sau chỗ trống — nhiều câu phải dựa vào ngữ cảnh (thì của động từ, đại từ he/she/it/they)
- Câu điền câu: chọn câu nối mạch với câu trước và câu sau; loại câu nhắc tới thông tin không có trong bài
- Từ nối (however, therefore, in addition, as a result) phụ thuộc quan hệ giữa hai câu: đối lập, kết quả hay bổ sung
We regret to inform you that the event has been cancelled. However, all tickets will be refunded.|Chúng tôi rất tiếc thông báo sự kiện đã bị hủy. Tuy nhiên, toàn bộ vé sẽ được hoàn tiền.
""", sets=[
dict(title="E-mail", text="""
To: All staff
From: Linda Moore, Office Manager
Subject: Parking lot repairs

Dear colleagues,

The parking lot behind our building will be [1] from Monday, June 3, to Friday, June 7, while the surface is repaved. During this time, employees may park at the City Center Garage on Elm Street. [2]. Please show your company ID card at the entrance to receive the discount.

We understand that this may be [3] for some of you. To make your commute easier, a free shuttle will run between the garage and our office every fifteen minutes from 7:30 A.M. to 9:30 A.M.

Thank you for your [4] during the repairs.
""", quiz="""
closed|closes|close|closure|Sau "will be" cần quá khứ phân từ (bị động): bãi xe "sẽ bị đóng cửa" → closed.
The company has arranged a reduced daily rate for staff|The garage was built ten years ago|Elm Street is known for its restaurants|The repairs were completed last week|Câu tiếp theo nói "to receive the discount" → câu cần nhắc tới mức giá giảm cho nhân viên.
inconvenient|inconvenience|inconveniently|convenience|Sau "may be" cần tính từ → inconvenient (bất tiện).
patience|patient|patiently|patients|Sau tính từ sở hữu "your" cần danh từ → patience (sự kiên nhẫn). Patients = bệnh nhân.
"""),
dict(title="Notice", text="""
NOTICE TO ALL LIBRARY MEMBERS

Beginning September 1, the Westfield Public Library [1] its opening hours. The library will open at 9:00 A.M. and close at 8:00 P.M. from Monday to Saturday. It will remain closed on Sundays.

The change is the result of a recent survey of our members. [2] respondents said that they would prefer to visit the library in the evening after work. [3], the library will extend its evening hours and reduce its hours on the weekend.

[4]. Members can still return books at any time using the drop box next to the main entrance.
""", quiz="""
will change|changed|has changed|was changing|"Beginning September 1" là thời điểm trong tương lai → will change.
Most|Much|Every|Each other|"Respondents" là danh từ đếm được số nhiều → Most (hầu hết). Much đi với danh từ không đếm được; Every đi với danh từ số ít.
Therefore|However|Otherwise|For example|Câu sau là kết quả của mong muốn ở câu trước → Therefore (vì vậy).
We apologize for any inconvenience this may cause|The library has a large collection of magazines|The survey was sent to members by e-mail last year|New members can register online|Câu xin lỗi vì sự bất tiện nối tự nhiên với việc giảm giờ cuối tuần và câu sau "Members can still return books…".
"""),
dict(title="Letter", text="""
Dear Mr. Tanaka,

Thank you for your order of 200 office chairs from Comfort Seating. Unfortunately, the model you selected, the ErgoMax 300, is temporarily out of stock. Our supplier has informed us that new [1] will arrive in about three weeks.

If you prefer not to wait, we can offer you the ErgoMax 350 at the same price. This model is very [2] to the one you ordered, but it has an adjustable headrest. [3].

Please let us know which option you prefer by replying to this letter or calling our customer service team. We apologize for the delay and look forward to [4] you.

Sincerely,
Maria Lopez
Sales Department
""", quiz="""
shipments|shipping|shipped|ships|Sau tính từ "new" cần danh từ; "lô hàng mới sẽ đến" → shipments.
similar|same|alike|like|Cấu trúc "similar to" (tương tự với). "The same" phải đi với "as"; "alike" không đứng trước "to".
Many of our customers find it even more comfortable|The ErgoMax 300 was discontinued in 2019|Our office is closed on weekends|You can pay with a credit card|Câu này tiếp tục giới thiệu ưu điểm của mẫu 350 vừa nhắc → hợp mạch nhất.
serving|serve|served|be served|"Look forward to" + V-ing (to là giới từ) → serving.
"""),
dict(title="Advertisement", text="""
GRAND OPENING OF BRIGHT SMILE BAKERY

Bright Smile Bakery is proud to announce the opening of its third location at 25 Harbor Road. To celebrate, we are offering a free cup of coffee with [1] purchase over $10 during our opening week, March 4–10.

Our bakers arrive at 4:00 A.M. every day to prepare fresh bread, cakes, and pastries. All of our products are made with locally grown ingredients, and we never use [2] preservatives.

[3]. Simply place your order online at least 48 hours in advance, and we will deliver it to your home or office.

We look forward to [4] you at our new location!
""", quiz="""
every|all|many|few|Sau chỗ trống là danh từ số ít "purchase" → every (mỗi).
artificial|artificially|artifice|artificiality|Trước danh từ "preservatives" cần tính từ → artificial (nhân tạo).
We also provide cakes for birthdays and other special events|Our first location opened in 2010|Coffee prices have risen recently|The bakery is closed during holidays|Câu sau nói về đặt hàng trước và giao tận nơi → phù hợp với dịch vụ bánh cho sự kiện.
welcoming|welcome|welcomed|be welcomed|"Look forward to" + V-ing → welcoming.
"""),
]),
dict(slug="toeic-part-7", part=7, ico="📰", en="Part 7 – Reading Comprehension", vi="Đọc hiểu", color="#4527a0",
tips="""
## Cách làm Part 7
= Đọc câu hỏi trước → gạch từ khóa (tên người, ngày, số tiền) → tìm trong bài
- Câu hỏi "What is the purpose of…?" → đọc đoạn đầu · "What is NOT mentioned/true?" → loại từng đáp án có trong bài
- "Suggested / implied / most likely" → đáp án không có nguyên văn, phải suy luận từ chi tiết
- Bài 2 văn bản (double passage): câu cuối thường phải kết hợp thông tin của CẢ HAI văn bản
- Part 7 có 54 câu — chia thời gian khoảng 55 phút, đừng dừng quá lâu ở một câu
According to the notice, when will the work be completed?|Theo thông báo, khi nào công việc sẽ hoàn thành?
""", sets=[
dict(title="Text message chain", text="""
Kevin Park (9:12 A.M.): Hi Amy, are you at the office? I left my presentation file on my desk.
Amy Rossi (9:14 A.M.): Yes, I just got in. Do you need me to send it to you?
Kevin Park (9:15 A.M.): That would be great. I'm at the client's office, and the meeting starts at 10.
Amy Rossi (9:16 A.M.): Is it the blue folder or the USB drive?
Kevin Park (9:17 A.M.): The USB drive. The file is called "Q3 Sales Plan."
Amy Rossi (9:25 A.M.): Done. I've e-mailed it to you. Good luck!
""", quiz="""
Why does Mr. Park contact Ms. Rossi?|He needs a file he left behind.|He wants to reschedule a meeting.|He is looking for a client's address.|He wants her to attend a meeting.|"I left my presentation file on my desk" → cần tệp đã để quên.
At 9:16 A.M., why does Ms. Rossi ask about a blue folder?|To check which item contains the file.|To ask where to buy supplies.|To suggest a new presentation design.|To tell him the folder is missing.|Cô hỏi "the blue folder or the USB drive?" để biết tài liệu nằm ở đâu.
What does Ms. Rossi most likely do at 9:25 A.M.?|She sends an e-mail.|She leaves the office.|She calls the client.|She prints a document.|"I've e-mailed it to you".
"""),
dict(title="Notice", text="""
RIVERSIDE APARTMENTS — WATER SHUTOFF NOTICE

Dear residents,

Please be advised that the water supply to Buildings A and B will be shut off on Wednesday, May 14, from 9:00 A.M. to 3:00 P.M. Workers from Henley Plumbing will be replacing the main pipes, which are over thirty years old.

Building C will not be affected. Residents of Buildings A and B are welcome to use the fitness center showers in Building C during this time.

We recommend that you store some water for drinking and cooking before the work begins. If you have any questions, please contact the management office at 555-0147.

Thank you for your understanding.
Riverside Apartments Management
""", quiz="""
What is the purpose of the notice?|To inform residents about planned work.|To announce a new fitness center.|To request payment of a water bill.|To introduce a new manager.|Thông báo về việc cắt nước để thay đường ống.
Why will the water be shut off?|Old pipes will be replaced.|A building will be painted.|The water will be tested.|The fitness center will be cleaned.|"Replacing the main pipes, which are over thirty years old".
What are residents advised to do?|Store some water in advance.|Leave their apartments early.|Call Henley Plumbing.|Move to Building C.|"We recommend that you store some water… before the work begins".
What is NOT mentioned in the notice?|The cost of the repairs.|The time of the shutoff.|The name of the plumbing company.|A phone number to call.|Thông báo có giờ cắt nước, tên công ty, số điện thoại nhưng không nhắc tới chi phí.
"""),
dict(title="Job advertisement", text="""
GREENLEAF HOTELS — NOW HIRING: FRONT DESK SUPERVISOR

Greenleaf Hotels, a chain of eco-friendly hotels with 25 locations nationwide, is looking for a Front Desk Supervisor for its new hotel in Portland, opening in August.

Responsibilities:
• Supervise a team of 8 front desk agents
• Handle guest complaints and special requests
• Prepare weekly staff schedules

Requirements:
• At least 3 years of experience in hotel or customer service
• Excellent communication skills; knowledge of a second language is a plus
• Willingness to work evening and weekend shifts

To apply, send your résumé and two references to jobs@greenleafhotels.com by June 30. Only selected candidates will be contacted for an interview.
""", quiz="""
What is indicated about Greenleaf Hotels?|It has hotels in many places.|It was founded in Portland.|It is closing some locations.|It only hires experienced managers.|"A chain of eco-friendly hotels with 25 locations nationwide".
What is one responsibility of the position?|Creating work schedules.|Training new chefs.|Cleaning guest rooms.|Planning marketing campaigns.|"Prepare weekly staff schedules".
What is NOT a requirement for the job?|A university degree.|Customer service experience.|Good communication skills.|Ability to work on weekends.|Bài không yêu cầu bằng đại học; ngoại ngữ chỉ là điểm cộng.
What should applicants send?|A résumé and references.|A photo and a cover letter.|A completed application form.|Copies of their certificates.|"Send your résumé and two references".
"""),
dict(title="Article", text="""
LOCAL FIRM WINS ENVIRONMENTAL AWARD

HARRISON — Solaris Tech, a small solar panel manufacturer based in Harrison, has received this year's Green Business Award from the National Environment Council. The award recognizes companies that have significantly reduced their environmental impact.

Since moving into its new factory in 2021, Solaris Tech has cut its energy use by 40 percent and now recycles almost all of its production waste. "We wanted to make sure our own factory was as clean as the products we sell," said CEO Rachel Ford.

The company, which started with just five employees in a garage in 2015, now employs more than 300 people. Ms. Ford said the company plans to open a second factory next year and will use part of the award money to train local students in renewable energy.
""", quiz="""
What is the article mainly about?|A company receiving an award.|The opening of a new school.|A new government regulation.|The history of solar energy.|"Has received this year's Green Business Award".
According to the article, what happened in 2021?|The company moved into a new factory.|The company was founded.|The company won its first award.|The company hired its 300th employee.|"Since moving into its new factory in 2021".
How will Solaris Tech use some of the award money?|To train students.|To buy new equipment.|To build a garage.|To advertise its products.|"Use part of the award money to train local students".
"""),
dict(title="E-mail + Invoice (double passage)", text="""
### E-mail
To: billing@quickprintshop.com
From: s.nguyen@brightdesign.com
Date: October 8
Subject: Invoice #2287

Hello,

I have just received invoice #2287 for the printing job we picked up on October 6. I noticed that we were charged for 500 business cards, but we only ordered 300. Everything else on the invoice looks correct. Could you please send me a corrected invoice? We would like to pay before the end of the week.

Best regards,
Sophie Nguyen, Bright Design

### Invoice
QUICK PRINT SHOP — Invoice #2287 — Customer: Bright Design
Business cards (500) ........ $75.00
Flyers, color (1,000) ........ $120.00
Posters, large (20) ........ $60.00
TOTAL ........ $255.00
Payment due: October 20
""", quiz="""
Why did Ms. Nguyen write the e-mail?|To report a billing error.|To place a new order.|To complain about print quality.|To ask for a faster delivery.|"We were charged for 500 business cards, but we only ordered 300" → lỗi trên hóa đơn.
Which item on the invoice is incorrect?|Business cards.|Flyers.|Posters.|The payment date.|Cô nói "Everything else on the invoice looks correct" — chỉ sai mục danh thiếp.
What is suggested about Bright Design?|It wants to pay before the due date.|It picked up its order late.|It has ordered from Quick Print Shop many times.|It needs the posters reprinted.|Hạn trả là 20/10 (hóa đơn), nhưng email muốn trả "before the end of the week" (khoảng 10/10) → trước hạn. Câu cần kết hợp cả hai văn bản.
"""),
]),
]
