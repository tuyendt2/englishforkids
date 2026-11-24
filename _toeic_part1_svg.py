# Ảnh minh họa TOEIC Part 1 — vẽ tay bằng SVG (Recraft không dùng được trong phiên tạo ảnh).
# Phong cách: tranh phẳng, màu dịu, khung 480×320. Mỗi hàm trả về một chuỗi SVG.
# build.py ghi ra toeic/img/<tên>.svg và dùng trong trang Part 1.

W, H = 480, 320
SKIN = ["#f2c9a0", "#d9a273", "#a8714a"]
DARK = "#37474f"

def svg(body, bg):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img">'
            f'<rect width="{W}" height="{H}" fill="{bg}"/>{body}</svg>')

def poly(pts, color, w):
    p = " ".join(f"{x},{y}" for x, y in pts)
    return f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'

def rect(x, y, w, h, fill, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>'

def circle(x, y, r, fill, extra=""):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" {extra}/>'

def person(hx, hy, shirt, pants, arms, legs, skin=SKIN[0], hair="#3b2a20", long=False, skirt=False, face=1, hat=False):
    """hx,hy = tâm đầu. arms/legs = 2 đường gấp khúc (danh sách điểm tuyệt đối) nối từ vai/hông.
    Tay thứ nhất và chân vẽ sau thân (ở phía sau), tay thứ hai vẽ trước thân. face = 1 nhìn sang phải, -1 sang trái."""
    sl, sr = (hx - 8, hy + 21), (hx + 8, hy + 21)
    hl, hr = (hx - 6, hy + 52), (hx + 6, hy + 52)
    back_sh, front_sh = (sl, sr) if face == 1 else (sr, sl)
    out = []
    if long:
        out.append(rect(hx - 13 if face == 1 else hx - 3, hy - 6, 16, 32, hair, 7))
    out.append(poly([back_sh] + arms[0], shirt, 8))
    out.append(circle(*arms[0][-1], 4.5, skin))
    for hip, leg in zip((hl, hr), legs):
        out.append(poly([hip] + leg, pants, 10))
        fx, fy = leg[-1]
        out.append(f'<ellipse cx="{fx + 4 * face}" cy="{fy + 3}" rx="8" ry="4" fill="{DARK}"/>')
    out.append(rect(hx - 13, hy + 14, 26, 42, shirt, 9))
    if skirt:
        out.append(f'<path d="M{hx-14},{hy+46} L{hx+14},{hy+46} L{hx+19},{hy+72} L{hx-19},{hy+72}Z" fill="{pants}"/>')
    out.append(rect(hx - 4, hy + 9, 8, 7, skin))
    out.append(circle(hx, hy, 12, skin))
    out.append(f'<path d="M{hx-12},{hy-1} A12,12 0 0 1 {hx+12},{hy-1} L{hx+12 - 16*(face==1)},{hy-4} L{hx-12 + 16*(face==-1)},{hy-4}Z" fill="{hair}"/>')
    out.append(circle(hx + 6 * face, hy, 1.6, DARK))
    if hat:
        out.append(rect(hx - 11, hy - 26, 22, 16, "#fff", 6, 'stroke="#cfd8dc" stroke-width="1.5"') + rect(hx - 13, hy - 13, 26, 5, "#fff", 2, 'stroke="#cfd8dc" stroke-width="1.5"'))
    out.append(poly([front_sh] + arms[1], shirt, 8))
    out.append(circle(*arms[1][-1], 4.5, skin))
    return "".join(out)

def floor(y, wall, fl):
    return rect(0, 0, W, y, wall) + rect(0, y, W, H - y, fl)

def plant(x, y, s=1.0, pot="#c8734a"):
    return (f'<path d="M{x-14*s},{y} L{x+14*s},{y} L{x+10*s},{y+24*s} L{x-10*s},{y+24*s}Z" fill="{pot}"/>'
            + "".join(f'<ellipse cx="{x+dx*s}" cy="{y-ry*s}" rx="{7*s}" ry="{15*s}" fill="{c}" transform="rotate({a} {x+dx*s} {y-ry*s})"/>'
                      for dx, ry, a, c in ((-8, 12, -30, "#66bb6a"), (8, 12, 30, "#66bb6a"), (0, 18, 0, "#43a047"))))

def car(x, y, color):
    return (f'<path d="M{x},{y+28} L{x},{y+12} Q{x+2},{y+6} {x+14},{y+5} L{x+30},{y-10} L{x+78},{y-10} L{x+96},{y+5} Q{x+112},{y+7} {x+114},{y+14} L{x+114},{y+28}Z" fill="{color}"/>'
            + f'<path d="M{x+34},{y-5} L{x+52},{y-5} L{x+52},{y+5} L{x+24},{y+5}Z M{x+57},{y-5} L{x+76},{y-5} L{x+88},{y+5} L{x+57},{y+5}Z" fill="#cfe8f7"/>'
            + "".join(circle(x + cx, y + 28, 11, DARK) + circle(x + cx, y + 28, 4.5, "#b0bec5") for cx in (24, 90)))

def bike(x, y, color):
    r = 18
    return (circle(x, y, r, "none", f'stroke="{DARK}" stroke-width="3.5"') + circle(x + 56, y, r, "none", f'stroke="{DARK}" stroke-width="3.5"')
            + poly([(x, y), (x + 22, y - 26), (x + 46, y - 26), (x + 56, y)], color, 4) + poly([(x, y), (x + 28, y), (x + 22, y - 26)], color, 4)
            + poly([(x + 28, y), (x + 46, y - 26)], color, 4) + poly([(x + 18, y - 32), (x + 28, y - 32)], DARK, 4)
            + poly([(x + 46, y - 26), (x + 44, y - 38), (x + 52, y - 40)], DARK, 3.5))

def box(x, y, w, h, c="#d7a86e"):
    return rect(x, y, w, h, c, 2, 'stroke="#a97c45" stroke-width="2"') + rect(x + w / 2 - 5, y, 10, h, "#c4965c")

# ───────────────────────── 12 cảnh ─────────────────────────
def s_laptop():
    b = floor(240, "#e8eef5", "#cfd8dc")
    b += rect(60, 50, 90, 70, "#bbdefb", 4, 'stroke="#fff" stroke-width="6"')  # cửa sổ
    b += rect(205, 190, 210, 9, "#8d6e63", 3) + rect(215, 199, 8, 50, "#6d4c41") + rect(397, 199, 8, 50, "#6d4c41")  # bàn
    b += rect(150, 180, 46, 8, DARK, 3) + rect(144, 128, 9, 60, DARK, 4) + rect(169, 188, 6, 54, DARK)  # ghế
    b += rect(232, 184, 66, 6, "#90a4ae", 2) + '<path d="M294,184 L310,136 L316,138 L301,186Z" fill="#607d8b"/>'  # laptop
    b += rect(350, 168, 16, 18, "#fff", 3, 'stroke="#90a4ae" stroke-width="2"') + '<path d="M366,172 q8,5 0,10" fill="none" stroke="#90a4ae" stroke-width="2.5"/>'  # cốc
    b += person(178, 118, "#1e88e5", "#37474f", arms=[[(196, 162), (244, 180)], [(200, 166), (254, 182)]],
                legs=[[(214, 172), (216, 236)], [(222, 172), (226, 236)]], hair="#2b1d14")
    return svg(b, "#e8eef5")

def s_water():
    b = rect(0, 0, W, 230, "#dff1fb") + rect(0, 230, W, 90, "#a5d6a7") + circle(420, 50, 26, "#ffe082")
    b += rect(0, 200, W, 34, "#bcaaa4")  # hàng rào thấp
    for x in (300, 350, 400):
        b += plant(x, 222, 1.3)
    b += person(190, 140, "#ef6c00", "#5d4037", arms=[[(205, 190), (232, 186)], [(214, 182), (240, 178)]],
                legs=[[(184, 248), (182, 290)], [(198, 248), (204, 290)]], hair="#4e342e", long=True, skirt=True)
    b += '<path d="M232,170 L262,170 L266,196 L228,196Z" fill="#26a69a"/><path d="M262,178 L296,160" stroke="#26a69a" stroke-width="6" stroke-linecap="round"/>'
    b += "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.5" ry="5" fill="#29b6f6"/>' for x, y in ((300, 172), (306, 186), (296, 196), (310, 200)))
    return svg(b, "#dff1fb")

def s_handshake():
    b = floor(250, "#ede7f6", "#d1c4e9")
    b += rect(30, 40, 120, 160, "#b39ddb", 4) + rect(40, 50, 100, 140, "#d1c4e9", 2)  # cửa
    b += plant(420, 226, 1.4)
    b += person(190, 120, "#455a64", "#263238", arms=[[(176, 166), (182, 194)], [(212, 160), (238, 168)]],
                legs=[[(186, 216), (184, 268)], [(200, 216), (204, 268)]], hair="#212121")
    b += person(286, 122, "#c2185b", "#37474f", arms=[[(298, 168), (292, 194)], [(264, 162), (242, 168)]],
                legs=[[(282, 218), (278, 268)], [(294, 218), (296, 268)]], skin=SKIN[1], hair="#3e2723", long=True, face=-1)
    return svg(b, "#ede7f6")

def s_warehouse():
    b = floor(250, "#eceff1", "#b0bec5")
    for sx in (40, 250):
        b += rect(sx, 40, 8, 210, "#1565c0") + rect(sx + 182, 40, 8, 210, "#1565c0")
        for sy in (110, 180, 245):
            b += rect(sx, sy, 190, 6, "#ef6c00")
        for row, sy in enumerate((110, 180, 245)):
            for k in range(3 if row != 1 else 2):
                b += box(sx + 14 + k * 56, sy - 46, 48, 46)
    return svg(b, "#eceff1")

def s_bench():
    b = rect(0, 0, W, 220, "#e1f5fe") + rect(0, 220, W, 100, "#aed581") + rect(0, 262, W, 26, "#d7ccc8")
    b += rect(372, 90, 22, 140, "#795548") + circle(383, 80, 58, "#66bb6a") + circle(345, 104, 36, "#4caf50") + circle(420, 108, 36, "#4caf50")
    b += rect(150, 206, 170, 10, "#8d6e63", 3) + rect(150, 176, 170, 9, "#8d6e63", 3) + rect(160, 216, 7, 40, "#5d4037") + rect(303, 216, 7, 40, "#5d4037")
    b += person(222, 150, "#7e57c2", "#455a64", arms=[[(236, 192), (254, 182)], [(240, 196), (258, 186)]],
                legs=[[(250, 204), (252, 254)], [(258, 204), (262, 254)]], hair="#212121", long=True, skin=SKIN[1])
    b += '<path d="M248,170 L262,178 L276,170 L276,190 L262,198 L248,190Z" fill="#fff" stroke="#e53935" stroke-width="2.5"/>'
    return svg(b, "#e1f5fe")

def s_ladder():
    b = floor(260, "#fff8e1", "#d7ccc8")
    b += rect(0, 0, W, 14, "#efebe9") + rect(286, 14, 4, 22, "#9e9e9e") + '<path d="M268,36 L308,36 L298,52 L278,52Z" fill="#ffca28"/>'
    b += poly([(220, 266), (250, 110)], "#90a4ae", 7) + poly([(300, 266), (262, 110)], "#90a4ae", 7)
    for y in (230, 196, 162, 128):
        t = (266 - y) / 156
        b += poly([(220 + 30 * t + 3, y), (300 - 38 * t - 3, y)], "#78909c", 5)
    b += person(262, 66, "#43a047", "#1565c0", arms=[[(270, 80), (280, 56)], [(278, 74), (288, 54)]],
                legs=[[(252, 140), (250, 160)], [(268, 138), (262, 160)]], hair="#5d4037")
    b += rect(352, 180, 60, 80, "#a1887f", 3) + plant(382, 156, 1.0)
    return svg(b, "#fff8e1")

def s_meeting():
    b = floor(250, "#f3f6f8", "#cfd8dc")
    b += rect(40, 40, 190, 120, "#fff", 4, 'stroke="#90a4ae" stroke-width="5"')
    for k, h in enumerate((40, 62, 52, 84)):
        b += rect(64 + k * 38, 140 - h, 24, h, ("#42a5f5", "#66bb6a", "#ffa726", "#ef5350")[k], 2)
    b += person(270, 112, "#5c6bc0", "#37474f", arms=[[(282, 156), (282, 182)], [(250, 140), (214, 108)]],
                legs=[[(266, 208), (262, 262)], [(278, 208), (282, 262)]], hair="#3e2723", face=-1)
    b += rect(300, 196, 170, 10, "#8d6e63", 3) + rect(310, 206, 8, 50, "#6d4c41") + rect(452, 206, 8, 50, "#6d4c41")
    for x, sh, sk, lg in ((350, "#26a69a", SKIN[0], True), (420, "#ab47bc", SKIN[2], False)):
        b += person(x, 146, sh, "#455a64", arms=[[(x - 10, 186), (x - 24, 196)], [(x - 6, 188), (x - 22, 198)]],
                    legs=[[(x - 30, 202), (x - 30, 250)], [(x - 22, 202), (x - 20, 250)]], skin=sk, hair="#212121", long=lg, face=-1)
    return svg(b, "#f3f6f8")

def s_street():
    b = rect(0, 0, W, 200, "#e3f2fd")
    for x, h, c in ((0, 130, "#b0bec5"), (110, 160, "#90a4ae"), (230, 120, "#cfd8dc"), (350, 150, "#b0bec5")):
        b += rect(x, 200 - h, 120, h, c)
        for wy in range(200 - h + 16, 186, 30):
            for wx in range(x + 14, x + 110, 28):
                b += rect(wx, wy, 16, 18, "#e3f2fd", 2)
    b += rect(0, 200, W, 22, "#bdbdbd") + rect(0, 222, W, 98, "#616161")
    b += "".join(rect(x, 272, 40, 6, "#fafafa") for x in range(10, W, 80))
    for x in (70, 300):
        b += rect(x, 150, 8, 60, "#6d4c41") + circle(x + 4, 140, 26, "#66bb6a")
    b += car(20, 210, "#e53935") + car(160, 210, "#1e88e5") + car(318, 210, "#fdd835")
    return svg(b, "#e3f2fd")

def s_chef():
    b = floor(250, "#fafafa", "#bcaaa4")
    b += "".join(rect(x, y, 38, 28, "#e0f2f1", 0, 'stroke="#b2dfdb" stroke-width="1"') for x in range(0, W, 38) for y in range(40, 160, 28))
    b += rect(250, 190, 200, 70, "#78909c", 4) + rect(250, 184, 200, 8, "#546e7a", 2)
    b += rect(296, 150, 74, 38, "#b0bec5", 6) + rect(288, 152, 10, 6, "#90a4ae", 2) + rect(368, 152, 10, 6, "#90a4ae", 2)
    b += "".join(f'<path d="M{x},140 q-8,-14 0,-28 q8,-14 0,-28" fill="none" stroke="#cfd8dc" stroke-width="4" stroke-linecap="round"/>' for x in (316, 336, 356))
    b += person(230, 108, "#fff", "#37474f", arms=[[(250, 150), (282, 150)], [(258, 140), (300, 134)]],
                legs=[[(226, 204), (222, 258)], [(238, 204), (242, 258)]], hair="#4e342e", hat=True, skin=SKIN[1])
    b += poly([(300, 134), (330, 168)], "#8d6e63", 5)
    return svg(b, "#fafafa")

def s_phone():
    b = floor(260, "#e0f7fa", "#b2dfdb")
    b += rect(60, 30, 180, 40, "#00838f", 6) + '<text x="150" y="57" font-family="Arial" font-size="20" font-weight="700" fill="#fff" text-anchor="middle">RECEPTION</text>'
    b += person(200, 120, "#00897b", "#37474f", arms=[[(214, 162), (228, 196)], [(176, 150), (196, 122)]],
                legs=[[(196, 220), (196, 262)], [(206, 220), (208, 262)]], hair="#212121", long=True, skin=SKIN[2], face=1)
    b += rect(190, 108, 9, 26, DARK, 3)
    b += rect(120, 190, 260, 80, "#8d6e63", 4) + rect(110, 184, 280, 10, "#6d4c41", 3)
    b += rect(282, 132, 70, 48, DARK, 4) + rect(288, 138, 58, 36, "#80deea", 2) + rect(312, 180, 10, 6, DARK)
    b += plant(420, 236, 1.3)
    return svg(b, "#e0f7fa")

def s_bikes():
    b = rect(0, 0, W, 210, "#fff3e0") + rect(40, 40, 400, 170, "#ffcc80") + rect(200, 110, 80, 100, "#8d6e63", 3)
    b += "".join(rect(x, 70, 50, 40, "#e3f2fd", 3) for x in (70, 140, 300, 370))
    b += rect(0, 210, W, 110, "#bdbdbd") + poly([(30, 250), (450, 250)], "#757575", 5)
    for k, c in enumerate(("#e53935", "#1e88e5", "#43a047", "#fb8c00")):
        b += poly([(58 + k * 104, 286), (58 + k * 104, 250)], "#757575", 4)
        b += bike(44 + k * 104, 286, c)
    return svg(b, "#fff3e0")

def s_cart():
    b = floor(250, "#fffde7", "#e0e0e0")
    for sx in (10, 340):
        b += rect(sx, 40, 130, 210, "#90a4ae", 3)
        for sy in (80, 130, 180, 230):
            b += rect(sx, sy, 130, 6, "#607d8b")
            b += "".join(rect(sx + 8 + i * 20, sy - 28, 15, 28, c, 2) for i, c in enumerate(("#ef5350", "#ffca28", "#66bb6a", "#42a5f5", "#ab47bc", "#ff7043")))
    b += person(190, 120, "#6d4c41", "#283593", arms=[[(206, 160), (232, 172)], [(212, 164), (236, 176)]],
                legs=[[(184, 218), (176, 266)], [(198, 218), (208, 266)]], hair="#212121")
    b += poly([(236, 174), (246, 174), (258, 214), (316, 214), (324, 184), (250, 184)], "#546e7a", 4)
    b += "".join(poly([(256 + i * 14, 186), (262 + i * 12, 212)], "#90a4ae", 2) for i in range(5))
    b += circle(266, 232, 7, DARK) + circle(310, 232, 7, DARK) + poly([(258, 214), (266, 226), (310, 226), (316, 214)], "#546e7a", 4)
    return svg(b, "#fffde7")

SCENES = {
    "p1-laptop": s_laptop, "p1-water": s_water, "p1-handshake": s_handshake, "p1-warehouse": s_warehouse,
    "p1-bench": s_bench, "p1-ladder": s_ladder, "p1-meeting": s_meeting, "p1-street": s_street,
    "p1-chef": s_chef, "p1-phone": s_phone, "p1-bikes": s_bikes, "p1-cart": s_cart,
}
