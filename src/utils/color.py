## @file color.py
#  @brief implementation class for colors

from math import ceil
import re

## @ingroup utils
#  @class Color
#  @brief implementation for color manipulation.
#
#  @detailed
#  All colors are RGB coded, so do not have trasparency values, even knowing that alpha values can be 
#  used, they only apply to the current color, not overlayed colors. 
class Color:
    ## @brief Constructor for creating a color.
    #  
    #  @param r red channel in RGBA.  
    #  @param g green channel in RGBA.  
    #  @param b blue channel in RGBA.
    #  @param a alpha channel in RGBA.     
    #  @exception ValueError Raised if a is not between ]0,1[.
    def __init__(self, r: int, g: int, b: int, a: int = 1) -> None:      
        self.rgb = self.rgba_to_rgb([r, g, b, a])
        self.hex = self.rgba_to_hex(self.rgba)
    
    ## @brief Constructor for creating a color.
    #    
    #  @param hex_color A string representing a rgb color (e.g., "#RRGGBB" or "RRGGBB or #RGB or RGB").
    #  @exception ValueError Raised if rgba_color leght != 4.
    #  @exception ValueError Raised if alpha value in not between ]0,1[.
    def __init__(self, rgba_color: list) -> None:
        self.hex = self.rgba_to_hex(rgba_color)
        self.rgb = self.rgba_to_rgb(rgba_color)
        
    ## @brief Constructor for creating a color.
    #    
    #  @param hex_color A string representing a rgb color (e.g., "#RRGGBB" or "RRGGBB or #RGB or RGB").
    #  @exception ValueError Raised if hex_color does not match the "#RRGGBB" or "RRGGBB" strings
    #  or are not hexadecimal values.
    def __init__(self, hex_color: str) -> None:
        self.hex = hex_color
        self.rgb = self.hex_to_rgb(self.hex)
    
    def getHex(self) -> str:
        return self.hex
    
    def getRGB(self) -> str:
        return self.rgb
    
    # def update_colors(self, )
    
    ## @brief Static method to convert a rgba list color value (e.g., (r, g, b, a)) to a rgb color
    #  value (e.g., (r, g, b)).
    #
    #  @param rgba_color A string with the rgba color value.
    #  @return A Color with the color in hexadecimal format "#RRGGBB".
    #  @exception ValueError Raised if rgba_color leght != 4.
    #  @exception ValueError Raised if alpha value in not between ]0,1[.
    @staticmethod
    def rgba_to_rgb(rgba_color: list) -> list[int]:
        if (len(rgba_color) != 4):
            raise ValueError(f"Expected a list of length 4, got length {len(rgba_color)}")
        elif (rgba_color[3] < 0 or rgba_color[3] > 1):
            raise ValueError(f"Invalid alpha value. Expected should be between ]0,1[")
        
        a = rgba_color[3]
        r = rgba_color[0] * a
        g = rgba_color[1] * a
        b = rgba_color[2] * a

        return [r,g,b]
    
    ## @brief Static method to convert a rgba list color value (e.g., (r, g, b, a)) to a hexadecimal
    #  value (e.g., "#RRGGBB").
    #
    #  @param rgba_color A string with the rgba color value.
    #  @return A Color with the color in hexadecimal format "#RRGGBB".
    #  @exception ValueError Raised if rgba_color leght != 4.
    #  @exception ValueError Raised if alpha value in not between ]0,1[.
    @staticmethod
    def rgba_to_hex(rgba_color: list) -> str:
        if (len(rgba_color) != 4):
            raise ValueError(f"Expected a list of length 4, got length {len(rgba_color)}")
        elif (rgba_color[3] < 0 or rgba_color[3] > 1):
            raise ValueError(f"Invalid alpha value. Expected should be between ]0,1[")
        
        r = hex(ceil(rgba_color[0] * rgba_color[3]))[2:]
        g = hex(ceil(rgba_color[1] * rgba_color[3]))[2:]
        b = hex(ceil(rgba_color[2] * rgba_color[3]))[2:]
        
        return f"#{r}{g}{b}"
    
    ## @brief Static method to convert a hexadecimal color string (e.g., "#RRGGBB" or "RRGGBB") 
    #  to an RGB tuple (R, G, B).
    #
    #  @param hex_color A string with the hexadecimal color value.
    #  @return A Color in the format (R, G, B).
    #  @exception ValueError Raised if hex_color does not match the "#RRGGBB" or "RRGGBB" strings
    #  or are not hexadecimal values.
    @staticmethod
    def hex_to_rgb(hex_color: str) -> list:
        hex_color = hex_color.lstrip("#")
        if (not re.match(r"^(?:[0-9a-fA-F]{3}){1,2}$", hex_color)):
            raise ValueError(f"Hexadecimal color value expected, instead got {hex_color}")

        hex_values_offset = len(hex_color)

        r = int(hex_color[0:hex_values_offset], 16)
        g = int(hex_color[hex_values_offset:hex_values_offset*2], 16)
        b = int(hex_color[hex_values_offset*2:hex_values_offset*3], 16)
        
        return [r, g, b]
    
    ## @brief Create a blended color from multiple colors in the color_list.
    #
    #  @param color_list A list containing all hexadecimal colors to be added.
    #  @return A string with the final blended color in hexadecimal format "#RRGGBB".
    #  @exception ValueError Raised if color_list leght == 0.
    #  @exception TypeError  Raised if any item on a list is not a class Color.
    @staticmethod
    def blend(self, color_list: list) -> str:
        if (len(color_list) == 0):
            raise ValueError(f"Expected at least 1 color, got length {len(color_list)}")
        
        r = 0
        g = 0
        b = 0
        for i, hex_color in enumerate(color_list):
            rgb_color = self.hex_to_rgb(hex_color)
            r += rgb_color[0]
            g += rgb_color[1]
            b += rgb_color[2]
            
        r = r / len(color_list)
        g = g / len(color_list)
        b = b / len(color_list)
        
        return self.rgba_to_hex([r, g, b, 1])
    
    ## @brief Create a blended color.
    #
    #  @param other A Color to be added.
    #  @param inplace If True, change the self instance values
    #  @return A string with the final blended color in hexadecimal format "#RRGGBB".
    #  @exception ValueError Raised if color_list leght == 0.
    #  @exception TypeError  Raised if any item on a list is not a class Color.
    def blend(self, other: 'Color', inplace: bool = False) -> 'Color':
        return Color.blend([self.getHex(), Color.getHex()])