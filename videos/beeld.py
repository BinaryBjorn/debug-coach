"""PNG's voor de video (achtergrond, masker, klikcirkel), enkel met zlib en struct."""
import struct
import zlib

from huisstijl import ACCENT, ACHTERGROND_BOVEN, ACHTERGROND_ONDER, CIRKEL_DEKKING, rgb

# 4x4 Bayer-matrix: een fijne dither tegen banden in het donkere verloop
_BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def schrijf_png(pad, breedte, hoogte, kleurtype, rijen):
    """kleurtype 0 = grijs, 2 = RGB, 6 = RGBA; rijen = bytes per rij, zonder filterbyte."""
    def blok(soort, data):
        return struct.pack(">I", len(data)) + soort + data + struct.pack(">I", zlib.crc32(soort + data) & 0xFFFFFFFF)
    ruw = b"".join(b"\x00" + r for r in rijen)
    with open(pad, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(blok(b"IHDR", struct.pack(">IIBBBBB", breedte, hoogte, 8, kleurtype, 0, 0, 0)))
        f.write(blok(b"IDAT", zlib.compress(ruw, 6)))
        f.write(blok(b"IEND", b""))


def achtergrond(pad, breedte, hoogte):
    """Diagonaal verloop van linksboven (ACHTERGROND_BOVEN) naar rechtsonder (ACHTERGROND_ONDER)."""
    a, b = rgb(ACHTERGROND_BOVEN), rgb(ACHTERGROND_ONDER)
    d = [b[i] - a[i] for i in range(3)]
    noemer = float(breedte + hoogte - 2) or 1.0
    rijen = []
    for y in range(hoogte):
        bayer = _BAYER[y % 4]
        rij = bytearray(breedte * 3)
        for x in range(breedte):
            t = (x + y) / noemer
            r = (bayer[x % 4] + 0.5) / 16.0
            o = x * 3
            rij[o] = int(a[0] + d[0] * t + r)
            rij[o + 1] = int(a[1] + d[1] * t + r)
            rij[o + 2] = int(a[2] + d[2] * t + r)
        rijen.append(bytes(rij))
    schrijf_png(pad, breedte, hoogte, 2, rijen)


def _dekking_hoek(px, py, straal):
    """Dekking (0..1) van pixel (px, py) binnen een kwartcirkel met middelpunt (straal, straal); 4x4 subpixels."""
    binnen = 0
    for i in range(4):
        for j in range(4):
            dx = straal - (px + (i + 0.5) / 4)
            dy = straal - (py + (j + 0.5) / 4)
            if dx <= 0 or dy <= 0 or dx * dx + dy * dy <= straal * straal:
                binnen += 1
    return binnen / 16.0


def masker(pad, breedte, hoogte, straal):
    """Grijs masker: wit binnen een rechthoek met afgeronde hoeken, zwart erbuiten (randen afgevlakt)."""
    straal = max(0, min(straal, breedte // 2, hoogte // 2))
    hoek = [[int(round(255 * _dekking_hoek(x, y, straal))) for x in range(straal)] for y in range(straal)]
    vol = b"\xff" * breedte
    rijen = []
    for y in range(hoogte):
        if y < straal or y >= hoogte - straal:
            hy = y if y < straal else hoogte - 1 - y
            links = bytes(hoek[hy])
            rijen.append(links + b"\xff" * (breedte - 2 * straal) + links[::-1])
        else:
            rijen.append(vol)
    schrijf_png(pad, breedte, hoogte, 0, rijen)


def cirkel(pad, diameter):
    """Klikcirkel in ACCENT met CIRKEL_DEKKING, afgevlakte rand, transparant erbuiten."""
    r, g, b = rgb(ACCENT)
    straal = diameter / 2.0
    rijen = []
    for y in range(diameter):
        rij = bytearray(diameter * 4)
        for x in range(diameter):
            binnen = 0
            for i in range(4):
                for j in range(4):
                    dx = x + (i + 0.5) / 4 - straal
                    dy = y + (j + 0.5) / 4 - straal
                    if dx * dx + dy * dy <= straal * straal:
                        binnen += 1
            o = x * 4
            rij[o:o + 4] = bytes((r, g, b, int(round(255 * CIRKEL_DEKKING * binnen / 16.0))))
        rijen.append(bytes(rij))
    schrijf_png(pad, diameter, diameter, 6, rijen)
