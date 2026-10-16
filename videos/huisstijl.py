"""Huisstijl van Debug Marketing voor de video's, overgenomen uit brand.json (Debug Marketing).
De pijplijn leest geen bouwdocumenten tijdens het draaien: de waarden staan hier vast."""

ACHTERGROND_BOVEN = "#0B1628"   # begin van het achtergrondverloop
ACHTERGROND_ONDER = "#1A2D4A"   # einde van het achtergrondverloop
ACCENT = "#4A7CC9"              # klikcirkel
CIRKEL_DEKKING = 0.40           # klikcirkel op 40 procent
HOEKSTRAAL = 24                 # afgeronde hoeken van het scherm, in uitvoerpixels

BREEDTE, HOOGTE = 1920, 1080    # uitvoer
FPS = 30                        # uitvoer
KADER = 0.84                    # het scherm past in 84 procent van breedte en hoogte
ZOOM = 1.8                      # inzoomen rond een klik


def rgb(hexkleur):
    h = hexkleur.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
