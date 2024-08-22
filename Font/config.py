from freetype import Face

class FontConfig:
    """
    Used as configuration for Renderer class.
    """
    def __init__(self, fontPath:str, fontSize:int, color:tuple[int, int, int], spacing:int=1, wordSpacing:int=3, lineSpacing:int=2, backBox:tuple=None, align:str="left") -> None:
        """
        Initialize a FontConfig object with the given parameters.

        Parameters:
        fontPath (str): The path to the font file.
        fontSize (int): The size of the font in points.
        color (tuple[int, int, int]): The color of the font as a tuple of RGB values (0-255).
        spacing (int, optional): The spacing between characters. Default is 1.
        wordSpacing (int, optional): The spacing between words. Default is 3.
        lineSpacing (int, optional): The spacing between lines. Default is 2.
        backBox (tuple[int, int, int], optional): The background color of the font as a tuple of RGB values (0-255). Default is None (ie no back box).
        align (str, optional): The alignment of the text. Can be "left", "center", or "right". Default is "left". This is not case sensitive.

        Returns:
        None
        """
        self.fontPath = fontPath
        self.fontSize = fontSize
        self.spacing = spacing
        self.wordSpacing = wordSpacing
        self.color = color
        self.backBox = backBox
        self.align = align.lower()
        self.lineSpacing = lineSpacing

    def createFace(self) -> Face:
        """
        Createss a FreeType face based on the given parameters.
        """
        face = Face(self.fontPath)
        face.set_pixel_sizes(0, self.fontSize)
        return face