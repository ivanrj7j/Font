import numpy as np
from Font.config import FontConfig
from Font.render import Renderer
import cv2

def putTTFText(img:np.ndarray, text:str, org:tuple[int, int], fontFace:str, fontSclae:int, color:tuple[int, int, int]=(255, 255, 255), spacing:int=1, wordSpacing:int=3, lineSpacing:int=2, backBox:tuple=None, align:str="left", applyMask:bool=True):
    """
    This function overlays a given text onto an image using TrueType fonts.

    Parameters:
    img (np.ndarray): The input image on which the text will be overlayed.
    text (str): The text to be rendered.
    org (tuple[int, int]): The origin (x, y) coordinates of the text's top-left corner on the image.
    fontFace (str): The path to the TrueType font file.
    fontSclae (int): The size of the font in pixels.
    color (tuple[int, int, int], optional): The color of the text in RGB format. Default is white (255, 255, 255).
    spacing (int, optional): The spacing between characters in pixels. Default is 1.
    wordSpacing (int, optional): The spacing between words in pixels. Default is 3.
    lineSpacing (int, optional): The spacing between lines in pixels. Default is 2.
    backBox (tuple, optional): The dimensions (width, height) of the background box for the text. Default is None.
    align (str, optional): The alignment of the text. Can be "left", "center", or "right". Default is "left".
    applyMask (bool, optional): Whether to apply a mask to the rendered text. Default is True.

    Returns:
    np.ndarray: The image with the rendered text overlayed.
    """
    alpha = img.shape[-1] == 4

    config = FontConfig(fontPath=fontFace, fontSize=fontSclae, color=color, spacing=spacing, wordSpacing=wordSpacing,lineSpacing=lineSpacing, backBox=backBox, align=align)
    renderer = Renderer(config, alpha)

    renderedImage = renderer.render(text)

    return renderer.overlay(background=img, foreground=renderedImage, org=org, applyMask=applyMask)

cv2.putTTFText = putTTFText