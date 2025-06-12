## @file abstract_theme.py
#  @brief implementation for abstract base class for color themes.


from abc import ABC, abstractmethod
from enum import Enum

## @ingroup abc
#  @class BaseTheme
#  @brief Abstract base class for color themes.
#  
#  @details
#  Define all color properties and methods that must exist.
#
#  @see @ref https://docs.python.org/3/library/abc.html#abc.ABC
class BaseTheme(ABC):
    """Abstract base class for color themes."""
    
    ## @class EmphasisLevel
    #  @brief Set standard emphasis levels to use on diferent contexts in the UI.
    #
    #  @detailed
    #  When light text appears on dark backgrounds it should use opacity levels that describe its use.
    class EmphasisLevel(Enum):
        HIGH = 0
        MEDIUM = 1
        DISABLED = 2
    
    ## @class ElevationOverlay
    #  @brief Set standard elevation overlay level to use on diferent contexts in the UI.
    #
    #  @detailed
    #  To express elevation and space in an environment with a wider range of depth. Knowing this,
    #  the background will have 0dp elevation surface overlay, meaning the lowest level of depth  
    class ElevationOverlay(Enum):
        dp01 = 0
        dp02 = 1
        dp03 = 2
        dp04 = 3
        dp06 = 4
        dp08 = 5
        dp12 = 6
        dp16 = 7
        dp24 = 8
            
    @property
    @abstractmethod
    def surface(self):
        """Main color for the color theme"""
        pass

    @property
    @abstractmethod
    def error(self):
        """Error color for the color theme"""
    
        pass
    
    @property
    @abstractmethod
    def background(self):
        """Background color for the color theme"""
        
        pass
    
    @abstractmethod
    def outline(self, color: str) -> str:
        """
        @brief Define a new color based on the outline value alpha channel, and the input color
        
        @params color A hexadecimal string that represents a color value 
        @return A hexadecimal string that represents the new color value with the outline percentage 
        aplied
        """
        pass
    
    @abstractmethod
    def surface_overlay(self, color: str) -> str:
        """
        Define a new color based on the surface overlay value alpha channel, and the input color.
        Must be used for chips and text fields.
        
        @params color A hexadecimal string that represents a color value 
        @return A hexadecimal string that represents the new color value with the surface overlay 
        percentage aplied
        """
        pass
        
    def emphasis_on_surface(self, emphasis_level: EmphasisLevel) -> str:
        """
        @brief Based on the emphasis level, returns a different hexadecimal color with the emphasis level  
        """
        pass
    
    def emphasis_on_primary(self, emphasis_level : EmphasisLevel) -> str:
        """
        @brief Based on the emphasis level, returns a different hexadecimal blended color with the emphasis level  
        """
        pass
    
    