## @file color.py
#  @brief implementation class for colors

from typing import Union
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
    def __init__(self, color: Union[list, str]) -> None:
        if (type(color) is list):
            self._rgb = self.rgba_to_rgb(color)
            self._hex = self.rgba_to_hex(color)
        elif (type(color) is str):
            self._rgb = self.hex_to_rgb(color)
            self._hex = color
        else:
            raise TypeError(f"Expected parameter color type: str, list[int]. Got {type(color)}")
        
        self._r = self.rgb[0]
        self._g = self.rgb[1]
        self._b = self.rgb[2]
    
    ## @brief r channel in decimal value
    @property
    def r(self) -> int:
        return self._r
    
    @r.setter
    def r(self, new_value: int) -> None:
        new_color = [new_value, self.rgb[1], self.rgb[2]]
        
        self.__dict__.update(Color(new_color).__dict__)
    
    @property
    def g(self) -> int:
        return self._g
    
    @g.setter
    def g(self, new_value: int) -> None:
        new_color = [self.rgb[0], new_value, self.rgb[2]]
        
        self.__dict__.update(Color(new_color).__dict__)
    
    @property
    def b(self) -> int:
        return self._b
    
    @b.setter
    def b(self, new_value: int) -> None:
        new_color = [self.rgb[0], self.rgb[1], new_value]
        
        self.__dict__.update(Color(new_color).__dict__)
    
    ## @brief A RGB list (e.g., [r,g,b]) coded value color 
    #  
    #  @exception ValueError Raised if rgba_color leght != 4.
    #  @exception ValueError Raised if alpha value in not between ]0,1[.
    @property
    def rgb(self) -> list:
        return self._rgb
    
    @rgb.setter
    def rgb(self, new_value: list) -> None:       
        self.__dict__.update(Color(new_value).__dict__)
        
    ## @brief A hexadecimal string (e.g. "#RRGGBB") coded value color  
    #
    #  @exception ValueError Raised if hex_color does not match the "#RRGGBB" or "RRGGBB" strings
    #  or are not hexadecimal values.
    @property 
    def hex(self) -> str:
        return self._hex 
    
    @hex.setter
    def hex(self, new_value: str) -> None:       
        self.__dict__.update(Color(new_value).__dict__)
    
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
    #  @exception ValueError Raised if any R,G or B channel value is not between ]0,256].
    #  @exception ValueError Raised if alpha value in not between ]0,1[.
    @staticmethod
    def rgba_to_rgb(rgba_color: list) -> list[int]:
        if (len(rgba_color) != 3 and len(rgba_color) != 4):
            raise ValueError(f"Expected a list of length 3 ou 4 , got length {len(rgba_color)}")
        if (len(rgba_color) == 4):
            if (rgba_color[3] < 0 or rgba_color[3] > 1):
                raise ValueError(f"Invalid alpha value. Expected should be between ]0,1[")
        for i in range(3):
            if (rgba_color[i] < 0 or rgba_color[i] > 255):
                raise ValueError(f"")
        
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
    #  @exception ValueError Raised if any R,G or B channel value is not between ]0,256].
    #  @exception ValueError Raised if alpha value in not between ]0,1[.
    @staticmethod
    def rgba_to_hex(rgba_color: list) -> str:
        if (len(rgba_color) != 3 and len(rgba_color) != 4):
            raise ValueError(f"Expected a list of length 3 ou 4 , got length {len(rgba_color)}")
        if (len(rgba_color) == 4):
            if (rgba_color[3] < 0 or rgba_color[3] > 1):
                raise ValueError(f"Invalid alpha value. Expected should be between ]0,1[")
        for i in range(3):
            if (rgba_color[i] < 0 or rgba_color[i] > 255):
                raise ValueError(f"")
            
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
    #  Given a list containing color values (e.g., RGB or HEX) or a Color class, return the mean of
    #  every color at the list.
    #  The list can contain:
    #   - Color class instances;
    #   - hexadecimal string representing a color value;
    #   - A list with lenght of 3 or 4 (for alpha values).
    #
    #  @param color_list A list containing all hexadecimal colors to be added.
    #  @return A new Color instance representing the final blended color.
    #  @exception ValueError Raised if color_list leght == 0.
    #  @exception TypeError  Raised if any item on a list is not a: class Color, a list or string.
    @staticmethod
    def blend_list(color_list: list) -> 'Color':
        if (len(color_list) == 0):
            raise ValueError(f"Expected at least 1 color, got length {len(color_list)}")
        
        new_r = 0
        new_g = 0
        new_b = 0
        for i, color in enumerate(color_list):
            rgb_color = ""
            if (isinstance(color, Color)):
                rgb_color = color.rgb
            elif (isinstance(color, list)):
                rgb_color = Color.rgba_to_rgb(color)
            elif (isinstance(color, str)):
                rgb_color = Color.hex_to_rgb(color)
            else:
                raise TypeError(f"Expected type: Color, list or string. Got {type(color)}")
            new_r += rgb_color[0]
            new_g += rgb_color[1]
            new_b += rgb_color[2]
            
        new_r = ceil(new_r / len(color_list))
        new_g = ceil(new_g / len(color_list))
        new_b = ceil(new_b / len(color_list))
        
        return Color([new_r, new_g, new_b])
    
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
