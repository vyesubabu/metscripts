colors = {
  1: [  0,   0,   0],
  2: [255, 255, 255],
 21: [255, 250, 170],
 22: [255, 232, 120],
 23: [255, 192,  60],
 24: [255, 160,   0],
 25: [255,  96,   0],
 26: [255,  50,   0],
 27: [225,  20,   0],
 28: [192,   0,   0],
 29: [165,   0,   0],
 31: [230, 255, 225],
 32: [200, 255, 190],
 33: [180, 250, 170],
 34: [150, 245, 140],
 35: [120, 245, 115],
 36: [ 80, 240,  80],
 37: [ 55, 210,  60],
 38: [ 30, 180,  30],
 39: [ 15, 160,  15],
 41: [200, 255, 255],
 42: [175, 240, 255],
 43: [130, 210, 255],
 44: [ 95, 190, 250],
 45: [ 75, 180, 240],
 46: [ 60, 170, 230],
 47: [ 40, 150, 210],
 48: [ 30, 140, 200],
 49: [ 20, 130, 190],
 51: [220, 220, 255],
 52: [192, 180, 255],
 53: [160, 140, 255],
 54: [128, 112, 235],
 55: [112,  96, 220],
 56: [ 72,  60, 200],
 57: [ 60,  40, 180],
 58: [ 45,  30, 165],
 59: [ 40,   0, 160],
 61: [255, 230, 230],
 62: [255, 200, 200],
 63: [248, 160, 160],
 64: [230, 140, 140],
 65: [230, 112, 112],
 66: [230,  80,  80],
 67: [200,  60,  60],
 68: [180,  40,  40],
 69: [164,  32,  32],
 71: [250, 250, 250],
 72: [225, 225, 225],
 73: [200, 200, 200],
 74: [180, 180, 180],
 75: [160, 160, 160],
 76: [150, 150, 150],
 77: [140, 140, 140],
 78: [124, 124, 124],
 79: [112, 112, 112],
 80: [ 92,  92,  92],
 81: [ 80,  80,  80],
 82: [ 70,  70,  70],
 83: [ 60,  60,  60],
 84: [ 50,  50,  50],
 85: [ 40,  40,  40],
 86: [ 36,  36,  36],
 87: [ 32,  32,  32],

# MRF-GFS
 88: [  0, 236, 236],
 89: [  1, 160, 246],
 90: [  0,   0, 255],
 91: [  0, 255,   0],
 92: [  0, 200,   0],
 93: [  0, 144,   0],
 94: [255, 255,   0],
 95: [255, 144,   0],
 96: [255,   0,   0],
 97: [192,   0,   0],
 98: [255,   0, 255],
 99: [153,  85, 201],

# Channel 4 IR Cloud Top Color
100: [  0,   0, 255], # -39C a -45C
101: [179, 138,  70], # -45C a -51C
102: [  0, 255,   0], # -51C a -57C
103: [255, 255,   0], # -57C a -63C
104: [255,   0,   0], # -63C a -69C
105: [255,   0, 255], # -69C a -75C
106: [102, 102, 102], # < -75C

# Escala radar SMN
107: [  0, 240, 240], #  2 a  6 dBZ
108: [  0, 180, 230], #  6 a 10 dBZ
109: [  0, 120, 220], # 10 a 14 dBZ
110: [  0,   0, 210], # 14 a 18 dBZ
111: [  0, 240,   0], # 18 a 22 dBZ
112: [  0, 180,   0], # 22 a 26 dBZ
113: [  0, 120,   0], # 26 a 30 dBZ
114: [240, 240,   0], # 30 a 34 dBZ
115: [200, 200,   0], # 34 a 38 dBZ
116: [200, 140,   0], # 38 a 42 dBZ
117: [240,  40,   0], # 42 a 46 dBZ
118: [160,   0,   0], # 46 a 50 dBZ
119: [240,   0, 240], # 50 a 54 dBZ
120: [160,   0, 160], # 54 a 58 dBZ
121: [252, 252, 252], # 58 a 62 dBZ

# Escala radares meteorologia Cuba
122: [  0, 255, 255], #  10 dBZ
123: [  0, 204, 255], #  15 dBZ
124: [  0, 152, 255], #  20 dBZ
125: [  0, 255,  66], #  25 dBZ
126: [  0, 204,  51], #  30 dBZ
127: [ 51, 153, 102], #  35 dBZ
128: [255, 255,   0], #  40 dBZ
129: [255, 204,   0], #  45 dBZ
130: [255, 153,   0], #  50 dBZ
131: [255,   0,   0], #  55 dBZ
132: [204,   0,   0], #  60 dBZ
133: [153,   0,   0], #  65 dBZ
134: [204,   0, 255], #  70 dBZ
135: [153,   0, 255], #  75 dBZ
136: [127,  31, 170], #  80 dBZ

# Escala radar INTA Pergamino
137: [149, 234, 255], #  2 a  6 dBZ
138: [106, 191, 255], #  6 a 10 dBZ
139: [ 64, 149, 255], # 10 a 14 dBZ
140: [ 21, 106, 255], # 14 a 18 dBZ
141: [ 84, 252,   0], # 18 a 22 dBZ
142: [ 82, 192,   0], # 22 a 26 dBZ
143: [ 79, 132,   0], # 26 a 30 dBZ
144: [252, 252,   0], # 30 a 34 dBZ
145: [212, 212,   0], # 34 a 38 dBZ
146: [171, 171,   0], # 38 a 42 dBZ
147: [255,   0,   0], # 42 a 46 dBZ
148: [170,   0,   0], # 46 a 50 dBZ
149: [255,   0, 255], # 50 a 54 dBZ
150: [171,   0, 171], # 54 a 58 dBZ
151: [255, 255, 255], # 58 a 62 dBZ

# Escala radar NWS USA
152: [  4, 233, 231], #  5 a 10 dBZ
153: [  1, 159, 244], # 10 a 15 dBZ
154: [  3,   0, 244], # 15 a 20 dBZ
155: [  2, 253,   2], # 20 a 25 dBZ
156: [  1, 197,   1], # 25 a 30 dBZ
157: [  0, 142,   0], # 30 a 35 dBZ
158: [253, 248,   2], # 35 a 40 dBZ
159: [229, 188,   0], # 40 a 45 dBZ
160: [253, 149,   0], # 45 a 50 dBZ
161: [253,   0,   0], # 50 a 55 dBZ
162: [212,   0,   0], # 55 a 60 dBZ
163: [188,   0,   0], # 60 a 65 dBZ
164: [248,   0, 253], # 65 a 70 dBZ
165: [152,  84, 198], # 70 a 75 dBZ
166: [252, 252, 252], # > 75 dBZ

# Escala radar INTA (Romina)
167: [ 78, 235, 235], #  5 a 10 dBZ
168: [ 30, 166, 239], # 10 a 15 dBZ
169: [  7,  76, 225], # 15 a 20 dBZ
170: [107, 223,  18], # 20 a 25 dBZ
171: [ 87, 172,  59], # 25 a 30 dBZ
172: [ 29, 139,   2], # 30 a 35 dBZ
173: [236, 236,   0], # 35 a 40 dBZ
174: [244, 163,   0], # 40 a 45 dBZ
175: [244, 110,  14], # 45 a 50 dBZ
176: [226,   0,   0], # 50 a 55 dBZ
177: [166,  16,  29], # 55 a 60 dBZ
178: [ 98,   1,  14], # 60 a 65 dBZ
179: [255, 255, 255], # >65 dBZ (Blanco)

# Escala radares INTA
180: [  0, 255, 255], # 15.0 a 18.3 dBZ
181: [  0, 153, 255], # 18.3 a 22.1 dBZ
182: [  0,   0, 255], # 22.1 a 25.7 dBZ
183: [  0, 255,   0], # 25.7 a 29.3 dBZ
184: [  0, 204,   0], # 29.3 a 32.9 dBZ
185: [  0, 153,   0], # 32.9 a 36.4 dBZ
186: [255, 255,   0], # 36.4 a 40.0 dBZ
187: [255, 204,   0], # 40.0 a 43.6 dBZ
188: [255, 102,   0], # 43.6 a 47.1 dBZ
189: [255,   0,   0], # 47.1 a 50.7 dBZ
190: [204,   0,   0], # 50.7 a 54.3 dBZ
191: [153,   0,   0], # 54.3 a 57.9 dBZ
192: [255,   0, 255], # 57.9 a 61.4 dBZ
193: [153,   0, 255], # 64.4 a 65.0 dBZ
194: [255, 255, 255], # >65 dBZ (Blanco)
}

for icol in colors.values():
    icol[:] = [n / 255. for n in icol]
