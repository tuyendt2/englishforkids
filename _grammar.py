# Ngữ pháp theo từng chủ đề (khóa = slug chủ đề)
# Định dạng mỗi khối:
#   ## Tên điểm ngữ pháp
#   = Công thức            (có thể nhiều dòng)
#   - Ghi chú / cách dùng   (có thể nhiều dòng)
#   Câu ví dụ tiếng Anh|Nghĩa tiếng Việt
# Một chủ đề có thể có nhiều khối "##".

GRAMMAR = {
# ───────────── TIỂU HỌC ─────────────
"01-chao-hoi": """
## Động từ "to be": am / is / are
= I + am
= He / She / It / Nam + is
= You / We / They + are
- Viết tắt: I'm, he's, she's, it's, you're, we're, they're.
- Phủ định thêm "not": I'm not, he isn't, they aren't.
I am Nam. → I'm Nam.|Mình là Nam.
She is my friend.|Bạn ấy là bạn của mình.
We are fine, thank you.|Chúng mình khỏe, cảm ơn.
""",
"02-so-dem": """
## Danh từ số nhiều & How many...?
= How many + danh từ số nhiều + are there?
= There is one + danh từ / There are + số + danh từ số nhiều
- Thêm -s: book → books. Tận cùng s, x, ch, sh, o thêm -es: box → boxes.
- Bất quy tắc: child → children, man → men, foot → feet.
How many pens are there? → There are five pens.|Có bao nhiêu cái bút? → Có năm cái bút.
There is one apple.|Có một quả táo.
I have two boxes.|Mình có hai cái hộp.
""",
"03-mau-sac-hinh-khoi": """
## It's / They're + tính từ; tính từ đứng trước danh từ
= It is (It's) + màu → nói về 1 vật
= They are (They're) + màu → nói về nhiều vật
= a/an + tính từ + danh từ
- Tiếng Anh đặt tính từ TRƯỚC danh từ (khác tiếng Việt): a red ball = quả bóng đỏ.
It's yellow.|Nó màu vàng.
They're green.|Chúng màu xanh lá.
I have a big blue bag.|Mình có một cái cặp to màu xanh dương.
""",
"04-do-dung-hoc-tap": """
## a / an & this / that / these / those
= a + danh từ bắt đầu bằng phụ âm: a pen, a ruler
= an + danh từ bắt đầu bằng nguyên âm (a, e, i, o, u): an eraser
= This/That is + a/an + N (số ít) — These/Those are + N số nhiều
- this/these: ở gần; that/those: ở xa.
This is an eraser.|Đây là một cục tẩy.
That is my school bag.|Kia là cặp sách của mình.
These are my crayons.|Đây là những chiếc bút sáp của mình.
""",
"05-truong-lop-mon-hoc": """
## have / has (có) & Do you have...?
= I / You / We / They + have
= He / She / It + has
= Do you have + N? → Yes, I do. / No, I don't.
= When do you have + môn học? → I have it on + thứ.
I have English today.|Hôm nay mình có môn tiếng Anh.
She has Maths on Monday.|Bạn ấy có môn Toán vào thứ Hai.
Do you have Music? → Yes, I do.|Bạn có môn Âm nhạc không? → Có.
""",
"06-gia-dinh": """
## Tính từ sở hữu & sở hữu cách 's
= my (của tôi), your (của bạn), his (của anh ấy), her (của cô ấy), our (của chúng tôi), their (của họ)
= Tên người + 's + danh từ
- Tính từ sở hữu đứng trước danh từ: my mother, her brother.
This is my father.|Đây là bố của mình.
His name is Minh.|Tên cậu ấy là Minh.
This is Lan's sister.|Đây là chị gái của Lan.
""",
"07-co-the-khuon-mat": """
## have got / has got (miêu tả ngoại hình)
= I / You / We / They + have got + N
= He / She / It + has got + N
- Số nhiều bất quy tắc: tooth → teeth, foot → feet.
I have got two hands.|Mình có hai bàn tay.
She has got long hair.|Bạn ấy có mái tóc dài.
My dog has got big ears.|Con chó của mình có đôi tai to.
""",
"08-dong-vat": """
## can / can't (khả năng)
= S + can + V (nguyên thể)
= S + can't (cannot) + V
= Can + S + V? → Yes, S can. / No, S can't.
- Sau "can" động từ luôn ở dạng nguyên thể, không thêm -s.
A bird can fly.|Con chim có thể bay.
A fish can't walk.|Con cá không thể đi.
Can a monkey climb? → Yes, it can.|Con khỉ có leo trèo được không? → Có.
""",
"09-do-an-thuc-uong": """
## some / any & would like
= some + N: câu khẳng định, lời mời
= any + N: câu phủ định và câu hỏi
= Would you like + N? → Yes, please. / No, thank you.
= I'd like (I would like) + N
- Danh từ không đếm được (milk, water, rice) không có số nhiều, không dùng a/an.
I'd like some milk.|Mình muốn một ít sữa.
There aren't any eggs.|Không còn quả trứng nào.
Would you like some juice? → Yes, please.|Bạn uống nước ép nhé? → Vâng, cảm ơn.
""",
"10-quan-ao": """
## Thì hiện tại tiếp diễn (đang mặc) & Whose...?
= S + am / is / are + V-ing
= What are you wearing? → I'm wearing + quần áo.
= Whose + N + is this? → It's + tên's.
- Thêm -ing: wear → wearing, put → putting, make → making.
I'm wearing a blue T-shirt.|Mình đang mặc áo phông xanh.
She is wearing a skirt.|Bạn ấy đang mặc váy.
Whose hat is this? → It's Mai's.|Cái mũ này của ai? → Của Mai.
""",
"11-do-choi": """
## Giới từ chỉ vị trí: in / on / under / next to / behind
= Where is + N (số ít)? → It's + giới từ + the + N.
= Where are + N (số nhiều)? → They're + giới từ + the + N.
- in: bên trong · on: trên bề mặt · under: bên dưới · next to: bên cạnh · behind: phía sau.
Where is my teddy bear? → It's on the bed.|Gấu bông của mình ở đâu? → Nó ở trên giường.
The ball is under the table.|Quả bóng ở dưới gầm bàn.
My cars are in the box.|Những chiếc ô tô của mình ở trong hộp.
""",
"12-ngoi-nha": """
## There is / There are (có...)
= There is + a/an + N (số ít)
= There are + N (số nhiều)
= Is there a...? → Yes, there is. / No, there isn't.
= Are there any...? → Yes, there are. / No, there aren't.
There is a sofa in the living room.|Có một cái ghế sofa trong phòng khách.
There are two bedrooms in my house.|Nhà mình có hai phòng ngủ.
Is there a garden? → Yes, there is.|Có vườn không? → Có.
""",
"13-nghe-nghiep": """
## Thì hiện tại đơn với ngôi thứ ba (he/she)
= He / She + V-s / V-es
= What does he/she do? → He's/She's a + nghề.
= Where does he/she work? → He/She works in a + nơi.
- go → goes, watch → watches, study → studies, have → has.
My father is a doctor. He works in a hospital.|Bố mình là bác sĩ. Bố làm việc ở bệnh viện.
What does your mother do? → She's a teacher.|Mẹ bạn làm nghề gì? → Mẹ mình là giáo viên.
A farmer grows rice.|Người nông dân trồng lúa.
""",
"14-thoi-tiet-mua": """
## Hỏi về thời tiết & giới từ "in" với mùa
= What's the weather like? → It's + tính từ (sunny, rainy, cold...)
= What's the weather like in + mùa/nơi? → It's often + tính từ.
- Dùng "in" trước mùa và tháng: in summer, in May.
It's sunny today.|Hôm nay trời nắng.
It's often cold in winter.|Mùa đông trời thường lạnh.
What's the weather like in Da Lat? → It's cool.|Thời tiết ở Đà Lạt thế nào? → Trời mát.
""",
"15-ngay-thang-gio": """
## Giới từ thời gian: at / on / in
= at + giờ: at 7 o'clock, at noon
= on + thứ / ngày: on Monday, on 2nd September
= in + tháng / năm / mùa / buổi: in May, in 2026, in the morning
- Hỏi giờ: What time is it? → It's half past six. (6 giờ 30)
I get up at six o'clock.|Mình thức dậy lúc 6 giờ.
My birthday is on 5th May.|Sinh nhật mình vào ngày 5 tháng 5.
We have a holiday in June.|Chúng mình được nghỉ vào tháng Sáu.
""",
"16-so-thich-the-thao": """
## like / love / enjoy + V-ing & How often...?
= S + like / love / enjoy + V-ing
= What do you like doing? → I like + V-ing.
= How often do you + V? → once / twice / three times a week
I like playing football.|Mình thích chơi bóng đá.
She loves dancing.|Bạn ấy rất thích nhảy.
How often do you swim? → Twice a week.|Bạn bơi bao lâu một lần? → Hai lần một tuần.
""",
"17-noi-chon": """
## Câu mệnh lệnh để chỉ đường
= V (nguyên thể) + ...: Go straight. / Turn left.
= Don't + V: Don't cross here.
= Where's the + nơi? → It's next to / opposite / between...
- Câu mệnh lệnh không có chủ ngữ, bắt đầu bằng động từ.
Go straight and turn right.|Đi thẳng rồi rẽ phải.
The bank is opposite the park.|Ngân hàng ở đối diện công viên.
Don't run in the street!|Đừng chạy ngoài đường!
""",
"18-hoat-dong-hang-ngay": """
## Hiện tại đơn + trạng từ tần suất
= S + always / usually / often / sometimes / never + V
= What time do you + V? → I + V + at + giờ.
- Trạng từ tần suất đứng TRƯỚC động từ thường, SAU động từ to be.
- always (luôn luôn) > usually > often > sometimes > never (không bao giờ).
I always brush my teeth before bed.|Mình luôn đánh răng trước khi ngủ.
She usually walks to school.|Bạn ấy thường đi bộ đến trường.
He is never late.|Cậu ấy không bao giờ đi muộn.
""",
"19-cam-xuc-tinh-cach": """
## feel / look + tính từ & Why...? Because...
= S + feel(s) / look(s) + tính từ
= Why + be/do + S...? → Because + mệnh đề.
- Miêu tả tính cách: S + be + tính từ (kind, funny, shy...).
I feel happy today.|Hôm nay mình thấy vui.
You look tired.|Trông bạn mệt mỏi.
Why are you sad? → Because I lost my pen.|Sao bạn buồn? → Vì mình làm mất bút.
""",
"20-quoc-gia-thien-nhien": """
## Where are you from? & so sánh hơn ngắn (-er)
= Where are you from? → I'm from + quốc gia.
= What nationality are you? → I'm + quốc tịch.
= S + be + adj-er + than + N
- big → bigger, hot → hotter, happy → happier.
I'm from Viet Nam. I'm Vietnamese.|Mình đến từ Việt Nam. Mình là người Việt Nam.
An elephant is bigger than a tiger.|Con voi to hơn con hổ.
The Mekong is longer than the Red River.|Sông Mê Kông dài hơn sông Hồng.
""",
"21-suc-khoe": """
## What's the matter? & should / shouldn't (lời khuyên)
= What's the matter (with you)? → I have a/an + bệnh.
= S + should + V (nên)
= S + shouldn't + V (không nên)
- Sau should / shouldn't dùng động từ nguyên thể.
I have a toothache.|Mình bị đau răng.
You should go to the dentist.|Bạn nên đi nha sĩ.
You shouldn't eat a lot of sweets.|Bạn không nên ăn nhiều kẹo.
""",
"22-giao-thong": """
## Hỏi phương tiện & khoảng cách
= How do you go to + nơi? → I go by + phương tiện / on foot.
= How can I get to + nơi? → You can + V...
= How far is it from A to B? → It's about + khoảng cách.
- Dùng "by" + phương tiện, không có a/the: by bus, by train. Riêng đi bộ: on foot.
I go to school by bus.|Mình đi học bằng xe buýt.
My dad goes to work on foot.|Bố mình đi bộ đi làm.
How far is it? → It's about five kilometres.|Bao xa vậy? → Khoảng 5 km.
""",
"23-le-hoi": """
## Thì quá khứ đơn (động từ có quy tắc)
= S + V-ed
= S + didn't + V (nguyên thể)
= Did + S + V? → Yes, S did. / No, S didn't.
- watch → watched, decorate → decorated, visit → visited, stop → stopped.
- Dấu hiệu: yesterday, last week, last Tet, ago.
We decorated our house last Tet.|Tết năm ngoái chúng mình đã trang trí nhà cửa.
I visited my grandparents yesterday.|Hôm qua mình đã đi thăm ông bà.
Did you watch the fireworks? → Yes, I did.|Bạn có xem pháo hoa không? → Có.
""",
"24-ky-nghi": """
## Quá khứ đơn: động từ bất quy tắc & câu hỏi Wh-
= Wh- + did + S + V? (Where did you go? What did you do?)
= How was + N? → It was + tính từ.
- go → went, have → had, see → saw, swim → swam, eat → ate, build → built.
- Quá khứ của "be": I/He/She/It → was; You/We/They → were.
Where did you go? → I went to Hue.|Bạn đã đi đâu? → Mình đã đi Huế.
We saw a lot of fish.|Chúng mình đã nhìn thấy rất nhiều cá.
The trip was great.|Chuyến đi thật tuyệt.
""",

# ───────────── THCS ─────────────
"25-khu-pho": """
## So sánh hơn của tính từ
= Tính từ ngắn: S + be + adj-er + than + N
= Tính từ dài: S + be + more + adj + than + N
- Bất quy tắc: good → better, bad → worse, far → farther/further.
- Tính từ 2 âm tiết tận cùng -y: noisy → noisier, busy → busier.
My street is noisier than yours.|Con phố của tôi ồn ào hơn phố của bạn.
The city is more exciting than the countryside.|Thành phố sôi động hơn nông thôn.
Life here is better than before.|Cuộc sống ở đây tốt hơn trước.
""",
"26-truyen-hinh": """
## Từ để hỏi (Wh-) & liên từ and / but / so / because
= What / Who / Where / When / What time / How often + trợ động từ + S + V?
= Mệnh đề + and / but / so / because + mệnh đề
- and: và (thêm ý) · but: nhưng (đối lập) · so: vì vậy (kết quả) · because: vì (lý do).
When is the show on? → It's on Saturday.|Chương trình chiếu khi nào? → Vào thứ Bảy.
I was tired, so I went to bed early.|Tôi mệt nên đi ngủ sớm.
I like cartoons because they are funny.|Tôi thích hoạt hình vì chúng vui nhộn.
""",
"27-nha-tuong-lai": """
## Tương lai đơn (will) & might
= S + will + V (sẽ chắc chắn / dự đoán)
= S + won't (will not) + V
= S + might + V (có thể sẽ — không chắc chắn)
- Dấu hiệu: in the future, in 2050, next year, I think...
My house will have solar panels.|Nhà tôi sẽ có pin mặt trời.
Robots won't go to school for us.|Robot sẽ không đi học thay chúng ta.
We might live on the Moon.|Chúng ta có thể sẽ sống trên Mặt Trăng.
""",
"28-the-gioi-xanh": """
## Câu điều kiện loại 1
= If + S + V (hiện tại đơn), S + will / can + V
- Diễn tả điều có thể xảy ra ở hiện tại hoặc tương lai.
- Mệnh đề If có thể đứng sau, khi đó bỏ dấu phẩy.
If we plant more trees, the air will be cleaner.|Nếu chúng ta trồng thêm cây, không khí sẽ trong lành hơn.
If you recycle paper, you will save trees.|Nếu bạn tái chế giấy, bạn sẽ cứu được cây xanh.
We can save water if we turn off the tap.|Chúng ta có thể tiết kiệm nước nếu khóa vòi.
""",
"29-song-khoe": """
## more / less / fewer + danh từ & câu mệnh lệnh
= more + N đếm được / không đếm được (nhiều hơn)
= less + N không đếm được (ít hơn): less sugar, less fast food
= fewer + N đếm được số nhiều (ít hơn): fewer sweets
= V + ... / Don't + V (lời khuyên trực tiếp)
Eat more fruit and less sugar.|Hãy ăn nhiều trái cây hơn và ít đường hơn.
You should eat fewer sweets.|Bạn nên ăn ít kẹo hơn.
Don't stay up late.|Đừng thức khuya.
""",
"30-cong-dong": """
## Ôn tập quá khứ đơn
= S + V2 / V-ed (+ thời gian trong quá khứ)
= S + didn't + V
= Did + S + V...?
- Dấu hiệu: last summer, two days ago, in 2020, yesterday.
We cleaned up the beach last weekend.|Cuối tuần trước chúng tôi đã dọn dẹp bãi biển.
They gave food to homeless people.|Họ đã tặng đồ ăn cho người vô gia cư.
Did you volunteer last year? → No, I didn't.|Năm ngoái bạn có đi tình nguyện không? → Không.
""",
"31-phim-anh": """
## Although / Though & However (diễn tả sự tương phản)
= Although / Though + mệnh đề 1, mệnh đề 2
= Câu 1. However, câu 2.
- Although/though nối hai mệnh đề trong cùng một câu (không dùng thêm "but").
- However đứng đầu câu thứ hai, theo sau là dấu phẩy.
Although the film was frightening, I liked it.|Mặc dù bộ phim đáng sợ, tôi vẫn thích nó.
Though it was late, we watched another film.|Dù đã muộn, chúng tôi vẫn xem thêm một phim.
The story was simple. However, the acting was excellent.|Cốt truyện đơn giản. Tuy nhiên, diễn xuất rất xuất sắc.
""",
"32-nang-luong": """
## be going to & will
= S + am/is/are + going to + V → kế hoạch, dự định đã có từ trước
= S + will + V → quyết định tức thì, dự đoán theo ý kiến cá nhân
- be going to còn dùng để dự đoán khi có bằng chứng: Look at the clouds! It's going to rain.
We are going to use solar energy next year.|Năm sau chúng tôi sẽ dùng năng lượng mặt trời.
It's dark in here. I'll turn on the light.|Trong này tối quá. Tôi sẽ bật đèn.
I think wind power will become cheaper.|Tôi nghĩ điện gió sẽ trở nên rẻ hơn.
""",
"33-nong-thon": """
## So sánh hơn của trạng từ
= Trạng từ ngắn: S + V + adv-er + than + ...  (hard → harder, fast → faster, early → earlier)
= Trạng từ dài (-ly): S + V + more + adv + than + ...  (more slowly, more carefully)
- Bất quy tắc: well → better, badly → worse, far → farther.
Farmers get up earlier than city people.|Nông dân dậy sớm hơn người thành phố.
People in the countryside live more peacefully.|Người dân nông thôn sống yên bình hơn.
She speaks English better than me.|Cô ấy nói tiếng Anh giỏi hơn tôi.
""",
"34-phong-tuc": """
## should / have to / must
= S + should / shouldn't + V → lời khuyên
= S + have to / has to + V → bắt buộc do quy định, hoàn cảnh bên ngoài
= S + must / mustn't + V → bắt buộc theo ý người nói / cấm đoán
- don't have to = không cần phải (≠ mustn't = không được phép).
You should greet older people first.|Bạn nên chào người lớn tuổi trước.
We have to wear a uniform at school.|Chúng tôi phải mặc đồng phục ở trường.
You mustn't point at people with chopsticks.|Bạn không được chỉ đũa vào người khác.
""",
"35-thien-tai": """
## Thì quá khứ tiếp diễn
= S + was / were + V-ing
= S + was/were + V-ing + when + S + V2 (hành động đang xảy ra thì hành động khác xen vào)
= While + S + was/were + V-ing, S + V2
- Diễn tả hành động đang diễn ra tại một thời điểm trong quá khứ.
At 8 p.m. last night, we were watching the weather forecast.|Lúc 8 giờ tối qua, chúng tôi đang xem dự báo thời tiết.
I was sleeping when the earthquake happened.|Tôi đang ngủ thì động đất xảy ra.
While they were evacuating, the bridge collapsed.|Trong khi họ đang sơ tán thì cây cầu sập.
""",
"36-khoa-hoc-cong-nghe": """
## Câu tường thuật (câu trần thuật)
= S + said (that) + S + V (lùi thì)
= S + told + O + (that) + S + V (lùi thì)
- Lùi thì: hiện tại đơn → quá khứ đơn; hiện tại tiếp diễn → quá khứ tiếp diễn; will → would; can → could.
- Đổi đại từ và trạng từ: I → he/she, now → then, today → that day, here → there.
"I like robots." → He said (that) he liked robots.|"Tôi thích robot." → Anh ấy nói rằng anh ấy thích robot.
"We will build a satellite." → They said they would build a satellite.|"Chúng tôi sẽ chế tạo vệ tinh." → Họ nói họ sẽ chế tạo vệ tinh.
She told me she could use the 3D printer.|Cô ấy nói với tôi rằng cô ấy biết dùng máy in 3D.
""",
"37-cuoc-song-thanh-pho": """
## So sánh kép & cụm động từ (phrasal verbs)
= adj-er and adj-er / more and more + adj → càng ngày càng
= The + so sánh hơn + S + V, the + so sánh hơn + S + V → càng... càng...
= Phrasal verb = động từ + giới từ/trạng từ, mang nghĩa mới: get around (đi lại), grow up (lớn lên), look forward to (mong chờ), turn down (từ chối).
The city is getting more and more crowded.|Thành phố ngày càng đông đúc.
The bigger the city is, the more expensive life becomes.|Thành phố càng lớn, cuộc sống càng đắt đỏ.
I'm looking forward to visiting Ho Chi Minh City.|Tôi đang mong chờ được đến thăm TP. Hồ Chí Minh.
""",
"38-du-lich": """
## Thì hiện tại hoàn thành
= S + have / has + V3 (past participle)
= S + haven't / hasn't + V3
= Have / Has + S + V3? → Yes, S have/has. / No, S haven't/hasn't.
- Dùng cho trải nghiệm (ever, never), việc vừa xảy ra (just, already, yet), kéo dài đến hiện tại (for, since).
- for + khoảng thời gian (for 3 years); since + mốc thời gian (since 2020).
I have visited Hue twice.|Tôi đã đến Huế hai lần.
She has never been on a plane.|Cô ấy chưa bao giờ đi máy bay.
We have lived here since 2018.|Chúng tôi đã sống ở đây từ năm 2018.
""",
"39-thiet-bi-dien-tu": """
## Câu bị động
= Hiện tại đơn: S + am/is/are + V3 (+ by O)
= Quá khứ đơn: S + was/were + V3 (+ by O)
= Hiện tại tiếp diễn: S + am/is/are + being + V3
= Động từ khuyết thiếu: S + can/will/should + be + V3
- Dùng khi muốn nhấn mạnh hành động/đối tượng chịu tác động hơn là người làm.
These laptops are made in Japan.|Những chiếc laptop này được sản xuất ở Nhật Bản.
The first iPhone was released in 2007.|Chiếc iPhone đầu tiên được ra mắt năm 2007.
The software can be updated online.|Phần mềm có thể được cập nhật trực tuyến.
""",
"40-chon-nghe": """
## Mệnh đề quan hệ xác định (who / which / that)
= N (người) + who / that + V...
= N (vật) + which / that + V...
= whose + N → chỉ sở hữu
- Mệnh đề quan hệ xác định cần thiết để xác định danh từ, không có dấu phẩy.
A surgeon is a doctor who performs operations.|Bác sĩ phẫu thuật là bác sĩ thực hiện các ca mổ.
This is the job which I really want.|Đây là công việc mà tôi thực sự muốn.
She is the girl whose father is a pilot.|Cô ấy là cô gái có bố làm phi công.
""",

# ───────────── THPT ─────────────
"41-cuoc-song-gia-dinh": """
## Hiện tại đơn & hiện tại tiếp diễn
= Hiện tại đơn: S + V(s/es) → thói quen, sự thật, lịch trình
= Hiện tại tiếp diễn: S + am/is/are + V-ing → đang xảy ra lúc nói / xung quanh hiện tại
- Dấu hiệu HTĐ: always, usually, every day. HTTD: now, at the moment, today, these days.
- Động từ trạng thái (like, know, want, need, believe) thường không dùng ở dạng tiếp diễn.
My father usually does the shopping.|Bố tôi thường đi chợ.
My sister is doing the laundry now.|Chị tôi đang giặt đồ.
I know that housework is important.|Tôi biết rằng việc nhà rất quan trọng.
""",
"42-phat-minh": """
## Danh động từ (V-ing) & động từ nguyên mẫu có "to"
= S + enjoy / avoid / mind / finish / suggest / keep + V-ing
= S + want / decide / hope / plan / agree / need + to V
= S + allow / help / encourage + O + to V
= Giới từ + V-ing: be interested in inventing, good at designing
- Một số động từ đi được với cả hai và nghĩa thay đổi: remember / stop / try.
He enjoys inventing new gadgets.|Anh ấy thích phát minh ra những thiết bị mới.
They decided to build a robot.|Họ quyết định chế tạo một con robot.
The Internet allows people to work from home.|Internet cho phép mọi người làm việc tại nhà.
""",
"43-binh-dang-gioi": """
## Câu bị động với động từ khuyết thiếu
= S + can / could / should / must / will / may + be + V3 (+ by O)
= S + modal + not + be + V3
- Chủ động: We should treat everyone equally. → Bị động: Everyone should be treated equally.
Women should be given equal opportunities.|Phụ nữ nên được trao cơ hội bình đẳng.
Discrimination must be stopped.|Sự phân biệt đối xử phải bị chấm dứt.
Housework can be shared by all family members.|Việc nhà có thể được chia sẻ bởi tất cả các thành viên.
""",
"44-du-lich-sinh-thai": """
## Câu điều kiện loại 1 & loại 2
= Loại 1 (có thể xảy ra): If + S + V (hiện tại), S + will + V
= Loại 2 (không có thật ở hiện tại): If + S + V2/ed (were), S + would + V
- Ở loại 2, "be" dùng "were" cho tất cả các ngôi: If I were you...
If we protect the forest, more animals will survive.|Nếu chúng ta bảo vệ rừng, nhiều động vật sẽ sống sót hơn.
If I had more money, I would travel to national parks.|Nếu tôi có nhiều tiền hơn, tôi sẽ đi du lịch các vườn quốc gia.
If I were you, I would stay in a homestay.|Nếu tôi là bạn, tôi sẽ ở homestay.
""",
"45-song-khoe-song-lau": """
## Quá khứ đơn & hiện tại hoàn thành
= Quá khứ đơn: S + V2/ed → hành động đã kết thúc, có thời gian xác định
= Hiện tại hoàn thành: S + have/has + V3 → không rõ thời gian, kết quả còn ở hiện tại, kéo dài đến nay
- QKĐ: yesterday, last year, in 2010, ago. HTHT: ever, never, just, already, yet, for, since, so far.
I started doing yoga two years ago.|Tôi bắt đầu tập yoga cách đây hai năm.
I have done yoga for two years.|Tôi đã tập yoga được hai năm.
Scientists have found new ways to slow down ageing.|Các nhà khoa học đã tìm ra những cách mới để làm chậm lão hóa.
""",
"46-khoang-cach-the-he": """
## Động từ khuyết thiếu: must / have to / should (nghĩa vụ & lời khuyên)
= must + V → bắt buộc (người nói thấy cần thiết)
= have to + V → bắt buộc (quy định, hoàn cảnh)
= should / ought to + V → lời khuyên
= mustn't + V → cấm · don't have to + V → không cần thiết
I have to finish my homework before going out.|Tôi phải làm xong bài tập trước khi ra ngoài.
You mustn't speak rudely to your grandparents.|Bạn không được nói hỗn với ông bà.
You don't have to follow every tradition, but you ought to respect them.|Bạn không nhất thiết phải theo mọi truyền thống, nhưng bạn nên tôn trọng chúng.
""",
"47-nong-len-toan-cau": """
## Mệnh đề phân từ (V-ing / Having + V3)
= V-ing..., S + V → hai hành động cùng chủ ngữ, xảy ra đồng thời hoặc nối tiếp
= Having + V3..., S + V → hành động thứ nhất hoàn tất trước hành động thứ hai
= Danh động từ hoàn thành: S + V + having + V3 (be accused of / admit / deny having done...)
- Hai mệnh đề phải có cùng chủ ngữ.
Burning coal, factories release a lot of CO₂.|Đốt than, các nhà máy thải ra rất nhiều CO₂.
Having learned about climate change, we decided to cycle to school.|Sau khi tìm hiểu về biến đổi khí hậu, chúng tôi quyết định đạp xe đến trường.
The company denied having polluted the river.|Công ty phủ nhận việc đã làm ô nhiễm dòng sông.
""",
"48-di-san": """
## Mệnh đề to-infinitive
= the first / the second / the last / the only + N + to V
= It is + adj + (for O) + to V
= N + to V → chỉ mục đích / việc cần làm (a place to visit, something to do)
- Thay cho mệnh đề quan hệ: the first person who arrived → the first person to arrive.
Hue was the first city in Viet Nam to be recognised by UNESCO.|Huế là thành phố đầu tiên ở Việt Nam được UNESCO công nhận.
It is necessary for us to protect our heritage.|Việc chúng ta bảo vệ di sản là cần thiết.
Hoi An is a great place to visit.|Hội An là một nơi tuyệt vời để tham quan.
""",
"49-da-van-hoa": """
## Mệnh đề quan hệ không xác định
= N (đã xác định), who / which / whose + ..., V...
- Chỉ bổ sung thông tin thêm, có dấu phẩy, KHÔNG dùng "that".
- Dùng sau tên riêng, danh từ duy nhất, hoặc có tính từ sở hữu (my mother, ...).
- "which" có thể thay cho cả mệnh đề phía trước: He passed the exam, which surprised everyone.
Ha Noi, which is the capital of Viet Nam, has a long history.|Hà Nội, thủ đô của Việt Nam, có lịch sử lâu đời.
My teacher, who lived in Japan for ten years, loves sushi.|Thầy tôi, người từng sống ở Nhật mười năm, rất thích sushi.
Many young people listen to K-pop, which shows the power of globalisation.|Nhiều bạn trẻ nghe K-pop, điều đó cho thấy sức mạnh của toàn cầu hóa.
""",
"50-the-gioi-viec-lam": """
## Câu tường thuật: câu hỏi & câu mệnh lệnh
= Câu hỏi Yes/No: S + asked (O) + if / whether + S + V (lùi thì)
= Câu hỏi Wh-: S + asked (O) + Wh- + S + V (lùi thì, không đảo ngữ)
= Mệnh lệnh / lời khuyên: S + told / asked / advised + O + (not) to V
"Do you have a CV?" → He asked me if I had a CV.|"Bạn có CV không?" → Anh ấy hỏi tôi có CV không.
"Where did you study?" → She asked where I had studied.|"Bạn học ở đâu?" → Cô ấy hỏi tôi đã học ở đâu.
"Don't be late." → The manager told me not to be late.|"Đừng đến muộn." → Quản lý dặn tôi không được đến muộn.
""",
"51-tri-tue-nhan-tao": """
## Tương lai tiếp diễn & tương lai hoàn thành
= Tương lai tiếp diễn: S + will be + V-ing → đang diễn ra tại một thời điểm trong tương lai
= Tương lai hoàn thành: S + will have + V3 → sẽ hoàn tất trước một thời điểm trong tương lai
- Dấu hiệu TLTD: at this time tomorrow, at 9 a.m. next Monday. TLHT: by + thời gian (by 2030, by the end of...).
At this time next week, I will be attending an AI workshop.|Giờ này tuần sau, tôi sẽ đang tham dự một hội thảo về AI.
By 2030, self-driving cars will have become common.|Đến năm 2030, xe tự lái sẽ đã trở nên phổ biến.
By the end of this year, we will have finished our chatbot project.|Đến cuối năm nay, chúng tôi sẽ hoàn thành dự án chatbot.
""",
"52-bao-ton-dong-vat": """
## Câu điều kiện loại 3 & điều kiện hỗn hợp
= Loại 3 (trái với quá khứ): If + S + had + V3, S + would have + V3
= Hỗn hợp (quá khứ → hiện tại): If + S + had + V3, S + would + V (now)
- Đảo ngữ loại 3: Had + S + V3, S + would have + V3.
If we had acted earlier, the species would have survived.|Nếu chúng ta hành động sớm hơn, loài đó đã sống sót.
If they hadn't destroyed the forest, the tigers would still live here now.|Nếu họ không phá rừng, giờ đây hổ vẫn còn sống ở đây.
Had the poachers been caught, the rhinos wouldn't have been killed.|Nếu những kẻ săn trộm bị bắt, những con tê giác đã không bị giết.
""",
}
