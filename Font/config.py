from freetype import Face

class FontConfig:
    def __init__(self, fontPath:str, fontSize:int, color:tuple[int, int, int], spacing:int=1, wordSpacing:int=3, backBox:tuple=[0, 0, 0], align:str="left") -> None:
        """
        Initialize a FontConfig object with the given parameters.

        Parameters:
        fontPath (str): The path to the font file.
        fontSize (int): The size of the font in points.
        color (tuple[int, int, int]): The color of the font as a tuple of RGB values (0-255).
        spacing (int, optional): The spacing between characters. Default is 1.
        wordSpacing (int, optional): The spacing between words. Default is 3.
        backBox (tuple[int, int, int], optional): The background color of the font as a tuple of RGB values (0-255). Default is [0, 0, 0].
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

    def createFace(self) -> Face:
        """
        Createss a FreeType face based on the given parameters.
        """
        face = Face(self.fontPath)
        face.set_pixel_sizes(0, self.fontSize)
        return face