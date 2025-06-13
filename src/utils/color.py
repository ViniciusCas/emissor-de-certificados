## @file color.py
#  @brief implementation class for colors

from math import ceil
import re

## @ingroup utils
#  @class Color
#  @brief implementation for color manipulation.
#
#  All colors are RGB coded, so do not have trasparency values, even knowing that alpha values can be 
#  used, they only apply to the current color, not overlayed colors. 
class Color:       
    ## @brief Constructor for creating a color.
    #    
    #  @param color A string representing a hexadecimal color (e.g., "#RRGGBB" or "RRGGBB)
    #  or a list representing a rgba color (e.g, [r,g,b,a]).
    #  @exception TypeError  Raised if color is not a list nor string.
    #  @exception ValueError Raised if color is a list and leght != 4 or != 3.
    #  @exception ValueError Raised if color is a list and alpha value in not between ]0,1[.
    #  @exception ValueError Raised if color is a string and does not match the "#RRGGBB" or "RRGGBB"
    #  strings or are not hexadecimal values.
    def __init__(self, color) -> None:
        if (type(color) is list):
            self._rgb = self.rgba_to_rgb(color)
            self._hex = self.rgba_to_hex(color)
        elif (type(color) is str):
            self._rgb = self.hex_to_rgb(color)
            self._hex = color
        else:
            raise TypeError(f"Expected parameter color type: str, list[int]. Got {type(color)}")
    ## @brief Constructor for creating a color.
    #    
    #  @param hex_color A string representing a rgb color (e.g., "#RRGGBB" or "RRGGBB).
    #  @exception ValueError Raised if hex_color does not match the "#RRGGBB" or "RRGGBB" strings
    #  or are not hexadecimal values.

    
    ## @brief A RGB list (e.g., [r,g,b]) coded value color 
    #  
    #  @exception ValueError Raised if rgba_color leght != 4.
    #  @exception ValueError Raised if alpha value in not between ]0,1[.
    @property
    def rgb(self) -> list:
        return self._rgb
    
    @rgb.setter
    def rgb(self, new_value: list) -> None:               
        self._rgb = self.rgba_to_rgb(new_value)
        self._hex = self.rgba_to_hex(new_value)
        
    ## @brief A hexadecimal string (e.g. "#RRGGBB") coded value color  
    #
    #  @exception ValueError Raised if hex_color does not match the "#RRGGBB" or "RRGGBB" strings
    #  or are not hexadecimal values.
    @property 
    def hex(self) -> str:
        return self._hex 
    
    @hex.setter
    def hex(self, new_value: str) -> None:       
        self._rgb = self.hex_to_rgb(new_value)
        self._hex = new_value
    
    ## @brief define a human-readable string representation of the color.
    #  
    #  @return The instance's hex color value   
    def __str__(self) -> str:
        return self.hex
    
    ## @brief Static method to convert a rgba list color value (e.g., (r, g, b, a)) to a rgb color
    #  value (e.g., (r, g, b)).
    #
    #  @param rgba_color A string with the rgba color value.
    #  @return A Color with the color in hexadecimal format "#RRGGBB".
    #  @exception ValueError Raised if rgba_color leght != 4 or != 3.
    #  @exception ValueError Raised if alpha value in not between ]0,1[.
    @staticmethod
    def rgba_to_rgb(rgba_color: list) -> list[int]:
        if (len(rgba_color) != 3 and len(rgba_color) != 4):
            raise ValueError(f"Expected a list of length 3 ou 4 , got length {len(rgba_color)}")
        if (len(rgba_color) == 4):
            if (rgba_color[3] < 0 or rgba_color[3] > 1):
                raise ValueError(f"Invalid alpha value. Expected should be between ]0,1[")
        
        if (len(rgba_color) == 3):
            rgba_color.append(1)
                   
        r = ceil(rgba_color[0] * rgba_color[3])
        g = ceil(rgba_color[1] * rgba_color[3])
        b = ceil(rgba_color[2] * rgba_color[3])

        return [r, g, b]
    
    ## @brief Static method to convert a rgba list color value (e.g., (r, g, b, a)) to a hexadecimal
    #  value (e.g., "#RRGGBB").
    #
    #  @param rgba_color A string with the rgba color value.
    #  @return A Color with the color in hexadecimal format "#RRGGBB".
    #  @exception ValueError Raised if rgba_color leght != 4 or != 3.
    #  @exception ValueError Raised if alpha value in not between ]0,1[.
    @staticmethod
    def rgba_to_hex(rgba_color: list) -> str:
        if (len(rgba_color) != 3 and len(rgba_color) != 4):
            raise ValueError(f"Expected a list of length 3 ou 4 , got length {len(rgba_color)}")
        if (len(rgba_color) == 4):
            if (rgba_color[3] < 0 or rgba_color[3] > 1):
                raise ValueError(f"Invalid alpha value. Expected should be between ]0,1[")
        
        if (len(rgba_color) == 3):
            rgba_color.append(1)
        
        r = hex(ceil(rgba_color[0] * rgba_color[3]))[2:].zfill(2)
        g = hex(ceil(rgba_color[1] * rgba_color[3]))[2:].zfill(2)
        b = hex(ceil(rgba_color[2] * rgba_color[3]))[2:].zfill(2)

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
        if (not re.match(r"^(?:[0-9a-fA-F]{2}){3}$", hex_color)):
            raise ValueError(f"Hexadecimal color value expected, instead got {hex_color}")

        offset = len(hex_color) // 3

        r = int(hex_color[0        : offset  ], 16)
        g = int(hex_color[offset   : offset*2], 16)
        b = int(hex_color[offset*2 : offset*3], 16)

        return [r, g, b]
    
    ## @brief Create a blended color from multiple colors in the color_list.
    #
    #  @param color_list A list containing all hexadecimal colors to be added.
    #  @return A string with the final blended color in hexadecimal format "#RRGGBB".
    #  @exception ValueError Raised if color_list leght == 0.
    #  @exception TypeError  Raised if any item on a list is not a class Color.
    @staticmethod
    def blend_list(color_list: list) -> 'Color':
        if (len(color_list) == 0):
            raise ValueError(f"Expected at least 1 color, got length {len(color_list)}")
        
        r = 0
        g = 0
        b = 0
        for i, hex_color in enumerate(color_list):
            rgb_color = Color.hex_to_rgb(hex_color)
            r += rgb_color[0]
            g += rgb_color[1]
            b += rgb_color[2]
            
        r = ceil(r / len(color_list))
        g = ceil(g / len(color_list))
        b = ceil(b / len(color_list))
        
        return Color([r, g, b, 1])
    
    ## @brief Create a blended color.
    #
    #  @param other A Color to be added.
    #  @param inplace If True, update the self instance values
    #  @return A string with the final blended color in hexadecimal format "#RRGGBB".
    #  @exception ValueError Raised if color_list leght == 0.
    #  @exception TypeError  Raised if any item on a list is not a class Color.
    def blend(self, other: 'Color', inplace: bool = False) -> 'Color':
        blended = Color.blend_list([self.hex, other.hex])
        if (inplace == True):
            self.__dict__.update(blended.__dict__)
            return self
                    
        return blended