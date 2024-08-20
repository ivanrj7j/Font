from freetype import Glyph
import numpy as np

class Character:
    def __init__(self, glyph:Glyph) -> None:
        self.glyph = glyph


    def getBitmap(self):
        bitmap = self.glyph.bitmap
        
        height = bitmap.rows
        width = bitmap.width

        top = self.glyph.bitmap_top

        diff = height - top

        descent = max(0, diff)
        ascent = min(0, diff)

        return bitmap.buffer, (width, height), (ascent, descent)
    
    def getCharacter(self):
        buffer, (width, height), (ascent, descent) = self.getBitmap()
        char = np.array(buffer).reshape((height, width))/255

        baseLine = height + ascent

        return char, (width, height), (ascent, descent), baseLine