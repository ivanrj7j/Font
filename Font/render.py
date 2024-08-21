from Font.config import FontConfig
import numpy as np
from Font.character import Character

class Renderer:
    """
    Used to handle rendering text using custom font for cv2
    """

    def __init__(self, config: FontConfig, alpha: bool = True) -> None:
        """
        Initialize the Renderer object with a custom font configuration and an optional alpha channel.

        Parameters:
        - config (FontConfig): An instance of the FontConfig class containing the custom font to be used for rendering text.
        - alpha (bool, optional): A boolean value indicating whether the rendered text should have an alpha channel. Default is True.
        """
        self.config = config
        self.face = config.createFace()
        self.alpha = alpha

    def renderMonoLine(self, text: str) -> np.ndarray:
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
    def calculateAnchorPoint(self, width:int, totalWidth:int):
        if self.config.align == "right":
            return totalWidth - width
        if self.config.align == "center":
            return (totalWidth-width )// 2
        return 0
    
    def renderMono(self, text:str):
        if "\n" not in text:
            return self.renderMonoLine(text)
        
        heights = []
        totalWidth = 0
        renders = []
        for line in text.split("\n"):
            render = self.renderMonoLine(line)
            heights.append(render.shape[0])
            totalWidth = max(totalWidth, render.shape[1])
            renders.append(render)
        totalHeight = sum(heights)
        
        canvas = np.zeros((totalHeight, totalWidth), dtype=np.uint8)

        for i in range(len(renders)):
            w = renders[i].shape[1]
            x = self.calculateAnchorPoint(w, totalWidth)

            h = heights[i]
            y = sum(heights[:i])
            # calculating dimensions 

            canvas[y:y+h, x:x+w] = renders[i]

        return canvas
    
    def calculateSpace(self, char:str):
        space = self.config.spacing
        if char == " ":
            space = self.config.wordSpacing
        if char == "\t":
            space = self.config.wordSpacing*4

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



