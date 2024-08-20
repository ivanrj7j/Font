from Font.config import FontConfig
import numpy as np

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

    def renderMono(self, text: str) -> np.ndarray:
        """
        Renders the input text using the custom font specified in the FontConfig object.
        
        Parameters:
        - text (str): The text to be rendered using the custom font.
        
        Returns:
        - np.ndarray: A numpy array containing the rendered text using the custom font.
        """

        return np.ones((32, 32))

    def render(self, text:str):
        monoRender = self.renderMono(text)
        monoRender = np.expand_dims(monoRender, -1)

        rgb = np.tile(monoRender, 3)
        rgb = rgb * self.config.color
        rgb = rgb.astype(np.uint8)
        # converting the image to rgb 

        if not self.alpha:
            return rgb

        alpha = np.ones_like(monoRender, np.uint8) * 255
        return np.concatenate((rgb, alpha), -1)



