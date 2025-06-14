## @file base_theme.py
#  @brief implementation for abstract base class for color themes.

from typing import Union
from abc import ABC, abstractmethod
from enum import Enum, EnumMeta, auto

from utils.color import Color

## @ingroup abc
#  @class BaseTheme
#  @brief Abstract base class for color themes.
#  
#  @details
#  Define all color properties and methods that must exist.
#
#  @see @ref https://docs.python.org/3/library/abc.html#abc.ABC
class BaseTheme(ABC):
    
    ## @class EmphasisLevel
    #  @brief Set standard emphasis levels to use on diferent contexts in the UI.
    #
    #   
    #  When light text appears on dark backgrounds it should use opacity levels that describe its use.
    class EmphasisLevel(Enum):
        HIGH = auto()
        MEDIUM = auto()
        DISABLED = auto()        
        
    ##  @brief Main color for the color theme
    @property
    @abstractmethod
    def surface(self):
        pass

    ## @brief Error color for the color theme
    @property
    @abstractmethod
    def error(self):
        pass
    
    ## @brief Background color for the color theme
    @property
    @abstractmethod
    def background(self):
        pass
    
    ## @brief Elevation overlay colors for different depht levels
    #
    @property
    @abstractmethod
    def elevation_overlay(self):
        pass
    
    ## @brief State colors fot
    @property
    @abstractmethod
    def contrast_state_overlay(self):
        pass
    
    @property
    @abstractmethod
    def primary_state_overlay(self):
        pass
    
    @property
    @abstractmethod
    def secondary_state_overlay(self):
        pass
    
    ## @brief Define a new color based on the outline value alpha channel, and the input color
    # 
    # @params color A hexadecimal string that represents a color value 
    # @return A hexadecimal string that represents the new color value with the outline percentage 
    # aplied
    @staticmethod
    @abstractmethod
    def outline(self, color: str) -> str:
        pass
    
    ## Define a new color based on the surface overlay value alpha channel, and the input color.
    #  Must be used for chips and text fields.
    #
    #  @params color A hexadecimal string that represents a color value 
    #  @return A hexadecimal string that represents the new color value with the surface overlay 
    #  percentage aplied
    @staticmethod
    @abstractmethod
    def surface_overlay(self, color: str) -> str:
        pass
        
    
    ## @brief Based on the emphasis level, returns a different hexadecimal color with the emphasis level  
    @staticmethod
    @abstractmethod
    def emphasis_on_surface(self, emphasis_level: EmphasisLevel) -> str:
        pass
    
    ## @brief Based on the emphasis level, returns a different hexadecimal blended color with the emphasis level  
    @staticmethod
    @abstractmethod
    def emphasis_on_primary(self, emphasis_level : EmphasisLevel) -> str:
        pass
    

## @class ElevationOverlay
#  @brief Standard elevation overlay level to use on diferent contexts in the UI.
#
#  To express elevation and space in an environment with a wider range of depth. Knowing this,
#  the background will have 0dp elevation surface overlay, meaning the lowest level of depth. 
class ElevationOverlay:            
    ## @brief Constructor for instantiate a new elevation overlay based on the given theme surface color
    #
    #  @param surface  Color class that indicates the surface color for the theme 
    #  @param contrast Color class that indicates the contrast color for the theme
    def __init__(self, surface: Color, contrast: Color):
        alphas = [(1,0.05),(2,0.07), (3,0.08), (4, 0.09), (6, 0.11), (8, 0.12), 
                            (12, 0.14), (16, 0.15), (24, 0.16)]
        self.members = {
            f"dp{n:02d}": str(Color.blend_list([surface, [contrast.r, contrast.g, contrast.b, a]]))
            for n,a in alphas                
        }
        
    ## @brief Method to retrieve the required overlay color for a given level
    #
    #  The overlays vary between 1, 2, 3, 4, 6, 8, 12, 16 and 24
    #  @param overlay_level A integer representing the wanted level
    #  @return A Color class for the needed overlay_level
    #  @exception ValueError Raised if the number is out of the list of levels, 
    def get_elevation(self, overlay_level: int) -> Color:
        try:
            return self.members[f"dp{overlay_level:02d}"]
        except:
            raise ValueError(f"Expected a integer in {self.members.keys()}, got dp{overlay_level}")
    
    ## @brief Method to retrieve all overlay levels
    #
    #  @return A dictionary of [level: Color] 
    def get_all_members(self) -> dict[int, Color]:
        return self.members
    
## @ingroup abc
#  @class BaseColorEnum
#  @brief Standard interface color.
#  
#  Define all color properties and methods that must exist.
class BaseColorEnum(ABC, EnumMeta):
    pass
    
#  @class States
#  @brief Standard interface for UI states. 
#
#  Define all states that components can have, and sets standard interactions for every one.
class States:    
    def __init__(self, hover, focus, pressed, dragged, selected):
        self._hover = hover
        self._focus = focus
        self._pressed = pressed 
        self._dragged = dragged
        self._selected = selected
    
    def hover(self, color: Union[str, Color, list]) -> Color:
        return Color.blend_list([self._hover, color])
    
    def focus(self, color: Union[str, Color, list]) -> Color:   
        return Color.blend_list([self._focus, color])
    
    def pressed(self, color: Union[str, Color, list]) -> Color:     
        return Color.blend_list([self._pressed, color])
    
    def dragged(self, color: Union[str, Color, list]) -> Color:     
        return Color.blend_list([self._dragged, color])
    
    def selected(self, color: Union[str, Color, list]) -> Color:     
        return Color.blend_list([self._selected, color])