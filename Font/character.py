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

        descent = max(0, height - top)
        ascent = max(0, max(top, height) - descent)

        return bitmap.buffer, (width, height), (ascent, descent)
    
    def getCharacter(self):
        buffer, (width, height), (ascent, descent) = self.getBitmap()
        char = np.array(buffer).reshape((height, width))/255

        if ascent > 0 or descent > 0:
            ascentSegment = np.zeros((ascent, width))
            descentSegment = np.zeros((descent, width))

            char = np.vstack((ascentSegment, char, descentSegment))

        return char, (width, height), (ascent, descent)