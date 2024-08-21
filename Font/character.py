from freetype import Glyph
import numpy as np

class Character:
    def __init__(self, glyph:Glyph, space:int) -> None:
        self.glyph = glyph
        self.space = space


    def getBitmap(self):
        bitmap = self.glyph.bitmap
        
        height = bitmap.rows
        width = bitmap.width

        top = self.glyph.bitmap_top

        diff = height - top

        bottomShift = max(0, diff)
        topShift = min(0, diff)

        return bitmap.buffer, (width, height), (topShift, bottomShift)
    
    def getCharacter(self):
        buffer, (width, height), (topShift, descent) = self.getBitmap()
        char = np.array(buffer).reshape((height, width))/255

        if len(buffer) == 0:
            char = np.zeros((1, self.space))
            return char, (self.space, 1), (topShift, descent)

        if self.space > 0:
            charSpace = np.zeros((height, self.space))
            char = np.hstack((char, charSpace))

        height, width = char.shape

        return char, (width, height), (topShift, descent)
    
    def calculateDimension(self):
        bitmap = self.glyph.bitmap

        height = bitmap.rows
        width = bitmap.width + self.space
        diff = height - self.glyph.bitmap_top


        return (width, height), (max(0, diff), min(0, diff))
