import numpy as np
from Font.config import FontConfig
from Font.render import Renderer
import cv2

def putTTFText(img:np.ndarray, text:str, org:tuple[int, int], fontFace:str, fontSclae:int, color:tuple[int, int, int]=(255, 255, 255), spacing:int=1, wordSpacing:int=3, lineSpacing:int=2, backBox:tuple=None, align:str="left"):
    alpha = img.shape[-1] == 4

    config = FontConfig(fontPath=fontFace, fontSize=fontSclae, color=color, spacing=spacing, wordSpacing=wordSpacing,lineSpacing=lineSpacing, backBox=backBox, align=align)
    renderer = Renderer(config, alpha)

    renderedImage = renderer.render(text)

    return renderer.overlay(background=img, foreground=renderedImage, org=org)

cv2.putTTFText = putTTFText