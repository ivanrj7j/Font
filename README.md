# Font Rendering Library for OpenCV

![With Backbox center](https://github.com/ivanrj7j/Font/blob/main/docs/render8.png?raw=true)

## Introduction
The `Font` library is designed to solve the problem of rendering text with custom TrueType fonts in OpenCV applications. OpenCV, a popular computer vision library, does not natively support the use of TrueType fonts, which can be a limitation for many projects that require advanced text rendering capabilities.

This library provides a simple and efficient solution to this problem by allowing developers to use custom fonts in their OpenCV projects. It abstracts away the low-level details of font rendering, providing a clean and intuitive API for text rendering.

## Features
- Support for custom TrueType fonts
- Configurable font settings (size, color, spacing, alignment, background)
- Rendering of single-line and multi-line text
- Efficient rendering using a custom `Character` class and `Renderer` class
- Compatibility with OpenCV (tested with OpenCV 4.x)

## Installation
To use the `Font` library in your project, follow these steps:

```
$ pip install Font
```

or


1. Clone the repository:
   ```
   git clone https://github.com/ivanrj7j/Font.git
   ```
2. Add the `character.py`, `config.py`, and `render.py` files to your project's directory.

## Usage
For detailed usage instructions and examples, please refer to the [Usage Guide](https://github.com/ivanrj7j/Font/wiki/Usage).

## Example

![Raw Image](https://github.com/ivanrj7j/Font/blob/main/docs/image.jpg?raw=true)

```python
renderedImage = putTTFText(image, "Hello world!\nI'm rendering text!", (0, 0), "alktall.ttf", 1000, color=(255, 0, 0), spacing=20, wordSpacing=100, lineSpacing=30, backBox=(0, 0, 0), align="center")
```

![With Backbox center](https://github.com/ivanrj7j/Font/blob/main/docs/render8.png?raw=true)

## API Reference
For detailed information about the available classes and methods, please refer to the [API Reference](https://github.com/ivanrj7j/Font/wiki/API-Reference).

## Contributing
Contributions to the `Font` library are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/ivanrj7j/Font).

## License
Click [here](https://raw.githubusercontent.com/ivanrj7j/Font/main/LICENSE) to see the license