# Ngữ pháp Lớp 1–4 theo từng chủ đề (khóa = slug). Lớp 5+ nằm trong _data_lopNN.py
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
}
