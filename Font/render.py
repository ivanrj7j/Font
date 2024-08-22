from Font.config import FontConfig
import numpy as np
from Font.character import Character
import cv2

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
        Renders the input text using the custom font specified in the FontConfig object. This only support 1 line. If you want to render multiple lines uses .renderMono() or .render() for mono or colored renders.
        
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

    def overlay(self, background:np.ndarray, foreground:np.ndarray, org:tuple[int, int]=(0, 0)):
        """
        Overlays the foregraound and the background image

        Parameters:
        - background (np.ndarray): The background image as a numpy array.(RGBA)
        - foreground (np.ndarray): The foreground image as a numpy array.(RGBA)
        - org (tuple[int, int]): The origin coordinates (top left) where the foreground image should be overlayed on the background image.
        """
        assert background.shape[-1] == foreground.shape[-1]  == 4, "Image should be RGBA"

        x, y = org
        x1, y1 =  min(x+foreground.shape[1], background.shape[1]), min(y+foreground.shape[0], background.shape[0])

        img = background.copy()
        foreground = foreground.copy()[:y1-y, :x1-x]

        mask = cv2.bitwise_not(foreground[:, :, -1])
        overlay = img[y:y1, x:x1]
        overlay = cv2.bitwise_and(overlay, overlay, mask=mask)
        overlay = cv2.add(overlay, foreground)

        img[y:y1, x:x1] = overlay

        return img

    def render(self, text:str) -> np.ndarray:
        """
        Renders the input text using the custom font specified in the configuration.

        Parameters:
        - text (str): The text to be rendered using the custom font.

        Returns:
        - np.ndarray: A numpy array containing the rendered text using the custom font.
        """
        monoRender = self.renderMono(text)
        monoRender = np.expand_dims(monoRender, -1)

        render = np.tile(monoRender, 3)

        if self.alpha:
            alphaChannels = monoRender * 255
            render = np.concatenate((render, alphaChannels), -1)  # adding alpha channel to the render
        
        render[:, :, :3] = render[:, :, :3] * self.config.color

        if self.config.backBox is not None and self.alpha:
            backBox = (*self.config.backBox, 255)
            backBox = np.ones_like(render) * backBox
            return self.overlay(backBox.astype(np.uint8), render.astype(np.uint8), (0, 0))
        
        render = render.astype(np.uint8)
        return render
    
    def calculateAnchorPoint(self, width:int, totalWidth:int) -> int:
        """
        Calculates the anchor point for rendering the text based on the specified alignment.

        Parameters:
        - width (int): The width of the rendered text.
        - totalWidth (int): The total width of the text area.

        Returns:
        - int: The calculated anchor point for rendering the text.

        This function calculates the anchor point for rendering the text based on the specified alignment. If the alignment is "right", the function returns the total width minus the width of the rendered text. If the alignment is "center", the function returns the difference between the total width and the width of the rendered text divided by 2. If the alignment is neither "right" nor "center", the function returns 0.
        """
        if self.config.align == "right":
            return totalWidth - width
        if self.config.align == "center":
            return (totalWidth-width )// 2
        return 0
    
    def renderMono(self, text:str) -> np.ndarray:
        """
        Renders the input text using the custom font specified in the configuration line by line.

        Parameters:
        - text (str): The text to be rendered using the custom font.

        Returns:
        - np.ndarray: A numpy array containing the rendered text using the custom font.

        This function renders the input text using the custom font specified in the FontConfig object. If the input text contains newline characters, the function splits the text into multiple lines and renders each line separately. The rendered lines are then combined to form the final rendered text.
        """
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

        totalHeight = sum(heights)+(len(heights) * self.config.lineSpacing)
        
        canvas = np.zeros((totalHeight, totalWidth), dtype=np.uint8)

        for i in range(len(renders)):
            w = renders[i].shape[1]
            x = self.calculateAnchorPoint(w, totalWidth)
            top = self.config.lineSpacing if i > 0 else 0
            h = heights[i]
            y = sum(heights[:i])+top
            # calculating dimensions 

            canvas[y:y+h, x:x+w] = renders[i]

        return canvas
    
    def calculateSpace(self, char:str) -> int:
        """
        Calculates the space for a given character based on the specified configuration.

        Parameters:
        - char (str): The character for which the space needs to be calculated.

        Returns:
        - float: The calculated space for the given character.

        This function calculates the space for a given character based on the specified configuration. It first sets the default space using the `config.spacing` attribute. If the character is a space, it sets the space to `config.wordSpacing`. If the character is a tab, it sets the space to `config.wordSpacing` multiplied by 4.
        """
        space = self.config.spacing
        if char == " ":
            space = self.config.wordSpacing
        if char == "\t":
            space = self.config.wordSpacing*4

        return space
    
    def calculateDimension(self, text:str) -> tuple[int, int]:
        """
        Calculates the dimensions of the rendered text based on the specified configuration.
    
        Parameters:
        - text (str): The text to be rendered using the custom font.
        
        Returns:
        - Tuple[int, int]: A tuple containing the total width and total height of the rendered text.
        """
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



