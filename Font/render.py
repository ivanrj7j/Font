from Font.config import FontConfig
import numpy as np
from Font.character import Character

class Renderer:
    """
    Used to handle rendering text using custom font for cv2
    """

    def __init__(self, config: FontConfig, alpha: bool = True, space:int=1, wordSpace:int=4) -> None:
        """
        Initialize the Renderer object with a custom font configuration and an optional alpha channel.

        Parameters:
        - config (FontConfig): An instance of the FontConfig class containing the custom font to be used for rendering text.
        - alpha (bool, optional): A boolean value indicating whether the rendered text should have an alpha channel. Default is True.
        - space (int, optional): The spacing between characters. Default is 1.
        - wordSpace (int, optional): The spacing between words. Default is 4.
        """
        self.config = config
        self.face = config.createFace()
        self.alpha = alpha
        self.space = space
        self.wordSpace = wordSpace

    def renderMono(self, text: str) -> np.ndarray:
        """
        Renders the input text using the custom font specified in the FontConfig object.
        
        Parameters:
        - text (str): The text to be rendered using the custom font.
        
        Returns:
        - np.ndarray: A numpy array containing the rendered text using the custom font.
        """
        dataList = []
        for char in text:
            self.face.load_char(char)
            space = self.calculateSpace(char)

            ch = Character(self.face.glyph, space)
            dataList.append(ch.getCharacter())


        char, dims, asc = zip(*dataList)
        w, h = zip(*dims)
        t,b = zip(*asc)
        # unpacking data 

        totalD = max(t)
        totalHeight, totalWidth = max(h)+max(t)+max(b), sum(w)
        # calculating dimensions 

        canvas = np.zeros((totalHeight, totalWidth))
        # empty canvas 

        for i in range(len(dataList)):
            height = h[i]
            width = w[i]

            x = sum(w[:i])
            y = max(h)+t[i]+totalD+b[i]
            
            canvas[y-height:y, x:x+width] += char[i]

        return canvas

    def render(self, text:str):
        monoRender = self.renderMono(text)
        monoRender = np.expand_dims(monoRender, -1)

        channels = 4 if self.alpha else 3

        render = np.tile(monoRender, channels)
        backbox = self.config.backBox

        if self.alpha:
            render = render * (*self.config.color, 255)
            backbox = (*backbox, 255)
        else:
            render = render * self.config.color

        if sum(backbox[:3]) > 0:
            backbox = np.ones_like(render) * backbox
            render = backbox + render
        
        render = render.astype(np.uint8)
        return render
    
    def calculateSpace(self, char:str):
        space = self.space
        if char == " ":
            space = self.wordSpace
        if char == "\t":
            space = self.wordSpace*4

        return space
    
    def calculateDimension(self, text:str):
        totalWidth = 0
        totalHeight = 0
        totalD = 0
        totalA = 0

        for char in text:
            self.face.set_pixel_sizes(0, 128)
            self.face.load_char(char)
            space = self.calculateSpace(char)
            ch = Character(self.face.glyph, space)
            (w, h), (t, b) = ch.calculateDimension()
            totalWidth += w
            totalHeight = max(totalHeight, h)
            totalD = max(totalD, b)
            totalA = max(totalA, t)

        return totalWidth, totalHeight+totalD+totalA



