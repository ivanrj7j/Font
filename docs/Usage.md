# Usage 

Using this module is as close to as using opencv natively as possible.

To get started:

```python
from Font.funcs import cv2
```

This imports cv2 with all its default methods but with `cv2.putTTFText()` method included.

If you dont want to directly import cv2 like that, you can just

```python
from Font.funcs import putTTFText
import cv2

cv2.putTTFText = putTTFText
# you dont have to do this you can just access putTTFText() directly if you want. 
```

## Adding text to image

```python
image = cv2.imread("docs/image.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
# reading an image in RGBA this is very important
```
![Loaded Image](image.jpg)

```python
renderedImage = putTTFText(image, "Hello world!", (0, 0), "test.ttf", 1000)
```

or

```python
renderedImage = cv2.putTTFText(image, "Hello world!", (0, 0), "alktall.ttf", 1000)
```

![Rendered Image 1](render1.png)

### Code Explaination: 

`putTTFText()` method takes positional arguments

- `img (np.ndarray)`: The input image on which the text will be overlayed.
- `text (str)`: The text to be rendered.
- `org (tuple[int, int])`: The origin (x, y) coordinates of the text's top-left corner on the image.
- `fontFace (str)`: The path to the TrueType font file.
- `fontSclae (int)`: The size of the font in pixels.

## Chaning font color

```python
renderedImage = putTTFText(image, "Hello world!", (0, 0), "alktall.ttf", 1000, color=(255, 0, 0))
```

![Red color](render2.png)

### Code Explaination: 

Here we passed `color` argument to the method, where `color` accepts a value in `RGB` format

## Spacing

As you can see from the images above, the spacing looks awful. To fix this issue you can:

```python
renderedImage = putTTFText(image, "Hello world!", (0, 0), "alktall.ttf", 1000, color=(255, 0, 0), spacing=10, wordSpacing=40)
```

Before:
![Red color](render2.png)

After:
![Red color with space](render3.png)

As you can see from the images above, the spacing looks much better

### Code Explaination:

Here we have passed two keyword arguments:

- `spacing (int, optional)`: The spacing between characters in pixels. Default is 1.
- `wordSpacing (int, optional)`: The spacing between words in pixels. Default is 3.

## Multi line text

Rendering multi-line text is just simple as adding `\n` character at every line break and the program will automatically render them as multiple characters.

```python
renderedImage = putTTFText(image, "Hello world!\nI'm rendering text!", (0, 0), "alktall.ttf", 1000, color=(255, 0, 0), spacing=20, wordSpacing=100)
```

![Multi line text](render4.png)

### Changing line spacing

```python
renderedImage = putTTFText(image, "Hello world!\nI'm rendering text!", (0, 0), "alktall.ttf", 1000, color=(255, 0, 0), spacing=20, wordSpacing=100, lineSpacing=30)
```

![Multi line text with spacing](render5.png)

#### Code Explaination
`lineSpacing` keyword argument determines the line spacing between two lines.


## Adding Backbox
```python
renderedImage = putTTFText(image, "Hello world!\nI'm rendering text!", (0, 0), "alktall.ttf", 1000, color=(255, 0, 0), spacing=20, wordSpacing=100, lineSpacing=30, backBox=(0, 0, 0))
```

![With Backbox](render6.png)

### Code Explaination

`backBox` keyword argument determines the color of the backbox, it is None by default, meaning there is no backbox. It accepts RGB values.

## Alignment

### Left

```python
renderedImage = putTTFText(image, "Hello world!\nI'm rendering text!", (0, 0), "alktall.ttf", 1000, color=(255, 0, 0), spacing=20, wordSpacing=100, lineSpacing=30, backBox=(0, 0, 0), align="left")
```

```python
renderedImage = putTTFText(image, "Hello world!\nI'm rendering text!", (0, 0), "alktall.ttf", 1000, color=(255, 0, 0), spacing=20, wordSpacing=100, lineSpacing=30, backBox=(0, 0, 0), align="hello")
```

![With Backbox](render6.png)

### Code Explaination

`align` keyword argument specifies the alignment of the text. This is case insensitive. Also the default value is `left`. As you can see in the second example, when `align="hello"` the text is still aligned at left, this is because left is the default argument and if the `align` keyword argument is invalid, it defaults to `left`.

### Center

```python
renderedImage = putTTFText(image, "Hello world!\nI'm rendering text!", (0, 0), "alktall.ttf", 1000, color=(255, 0, 0), spacing=20, wordSpacing=100, lineSpacing=30, backBox=(0, 0, 0), align="center")
```

![With Backbox center](render8.png)

### Right

```python
renderedImage = putTTFText(image, "Hello world!\nI'm rendering text!", (0, 0), "alktall.ttf", 1000, color=(255, 0, 0), spacing=20, wordSpacing=100, lineSpacing=30, backBox=(0, 0, 0), align="right")
```

![With Backbox center](render9.png)