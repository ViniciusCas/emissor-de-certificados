## @package themes
#  Themes classes that define rules to how a color scheme will to be.
#  
#  @see 
#  @author Vinicius Casimiro
#  @version 0.1

from typing import Union
from components.themes.base_theme import *
from enum import Enum

from utils.color import Color

class BlackTheme(BaseTheme):
    surface = Color("#121212")
    background = Color("#121212")
    error = Color("#CF6679")
    
    elevation_overlay = ElevationOverlay(surface, Color("#ffffff"))
    
    contrast_state_overlay = States(
        Color([255,255,255, 0.04]),
        Color([255,255,255, 0.12]),
        Color([255,255,255, 0.10]),
        Color([255,255,255, 0.12]),
        Color([255,255,255, 0.08])
    )
    
    primary_state_overlay = States(
        Color("#D9D9D9"),
        Color([187, 134, 252, 0.12]),
        Color([187, 134, 252, 0.10]),
        Color([187, 134, 252, 0.12]),
        Color([187, 134, 252, 0.08])
    )
    
    secondary_state_overlay = States(
        Color([  3, 218, 197, 0.04]),
        Color([  3, 218, 198, 0.12]),
        Color([  3, 218, 198, 0.12]),
        Color("#FFFFFF"),
        Color("#FFFFFF")
    )
    
        
    ## @class PrimaryColor
    #  @brief Standard primary colors separated by context
    class PrimaryColor(BaseColorEnum):
        c900 = Color("#23036A")
        c800 = Color("#30009C")
        c700 = Color("#3700B3")
        c600 = Color("#5600E8")
        c500 = Color("#6200EE")
        c400 = Color("#7F39FB")
        c300 = Color("#985EFF")
        c200 = Color("#BB86FC")
        c100 = Color("#DBB2FF")
        c50  = Color("#F2E7FE")
    
    ## @class SecondaryColor
    #  @brief Standard seconday colors separated by context
    class SecondaryColor(BaseColorEnum):
        c900 = Color("#005457")
        c800 = Color("#017374")
        c700 = Color("#018786")
        c600 = Color("#019592")
        c500 = Color("#01A299")
        c400 = Color("#00B3A6")
        c300 = Color("#00C4B4")
        c200 = Color("#03DAC5")
        c100 = Color("#70EFDE")
        c50  = Color("#C8FFF4")

    @staticmethod
    def outline(color: Color) -> Color:
        outline_color = Color([255,255,255,0.12])

        return outline_color.blend(color)
        
    @staticmethod
    def surface_overlay(color: Color) -> Color:
        overlay_color = Color([255,255,255,0.12])
        
        return overlay_color.blend(color)

    ## @brief Set differents context levels for texts depending on its use.
    #
    #  When working with the @ref surface color, a emphasis level blend with the @ref color 
    #  to create different context.
    #
    #  Emphasis colors:
    #   - HIGH     = (255, 255, 255, 87%)
    #   - MEDIUM   = (255, 255, 255, 74%)
    #   - DISABLED = (255, 255, 255, 38%)
    @staticmethod
    def emphasis_on_surface(color: Color, emphasis_level: BaseTheme.EmphasisLevel) -> Color:
        emphasis_blend_color =  ""
        if (emphasis_level == BaseTheme.EmphasisLevel.HIGH):
            emphasis_blend_color = Color.rgba_to_hex((255,255,255, 0.87))
        elif (emphasis_level == BaseTheme.EmphasisLevel.MEDIUM):
            emphasis_blend_color = Color.rgba_to_hex((255,255,255, 0.74))
        else:
            emphasis_blend_color = Color.rgba_to_hex((255,255,255, 0.38))
            
        return Color.blend([emphasis_blend_color, color.getHex()])
    
    ## @brief Set differents context levels for texts depending on its use.
    #
    #  When working with the @ref background color, a emphasis level blend with the @ref color 
    #  to create different context.
    #    
    #  Emphasis colors:
    #   - HIGH     = (0, 0, 0, 100%)
    #   - MEDIUM   = (0, 0, 0,  74%)
    #   - DISABLED = (0, 0, 0,  38%)
    @staticmethod
    def emphasis_on_primary(color: Color, emphasis_level: BaseTheme.EmphasisLevel) -> Color:
        emphasis_blend_color =  ""
        if (emphasis_level == BaseTheme.EmphasisLevel.HIGH):
            emphasis_blend_color = Color.rgba_to_hex((0,0,0, 1.00))
        elif (emphasis_level == BaseTheme.EmphasisLevel.MEDIUM):
            emphasis_blend_color = Color.rgba_to_hex((0,0,0, 0.74))
        else:
            emphasis_blend_color = Color.rgba_to_hex((0,0,0, 0.38))
            
        return Color.blend([emphasis_blend_color, color.getHex()])


class WhiteTheme(BaseTheme):
    surface = Color("#FFFFFF")
    background = Color("#FFFFFF")
    error = Color("#CF6679")
    
    elevation_overlay = ElevationOverlay(surface, Color("#000000"))
    
    contrast_state_overlay = States(
        Color([0  , 0  , 0  , 0.04]),
        Color([0  , 0  , 0  , 0.12]),
        Color([0  , 0  , 0  , 0.10]),
        Color([0  , 0  , 0  , 0.12]),
        Color([0  , 0  , 0  , 0.08])
    )
    
    primary_state_overlay = States(
        Color([187, 134, 252, 0.04]),
        Color([187, 134, 252, 0.12]),
        Color([187, 134, 252, 0.10]),
        Color([187, 134, 252, 0.12]),
        Color([187, 134, 252, 0.08])
    )
    
    secondary_state_overlay = States(
        Color([  3, 218, 197, 0.04]),
        Color([  3, 218, 198, 0.12]),
        Color([  3, 218, 198, 0.12]),
        Color("#FFFFFF"),
        Color("#FFFFFF")
    )    
    
    ## @class PrimaryColor
    #  @brief Standard primary colors separated by context
    class PrimaryColor(BaseColorEnum):
        c900 = Color("#23036A")
        c800 = Color("#30009C")
        c700 = Color("#3700B3")
        c600 = Color("#5600E8")
        c500 = Color("#6200EE")
        c400 = Color("#7F39FB")
        c300 = Color("#985EFF")
        c200 = Color("#BB86FC")
        c100 = Color("#DBB2FF")
        c50  = Color("#F2E7FE")
    
    ## @class SecondaryColor
    #  @brief Standard seconday colors separated by context
    class SecondaryColor(BaseColorEnum):
        c900 = Color("#005457")
        c800 = Color("#017374")
        c700 = Color("#018786")
        c600 = Color("#019592")
        c500 = Color("#01A299")
        c400 = Color("#00B3A6")
        c300 = Color("#00C4B4")
        c200 = Color("#03DAC5")
        c100 = Color("#70EFDE")
        c50  = Color("#C8FFF4")

    @staticmethod
    def outline(color: Color) -> Color:
        outline_color = Color([0, 0, 0, 0.12])

        return outline_color.blend(color)
        
    @staticmethod
    def surface_overlay(color: Color) -> Color:
        overlay_color = Color([0, 0, 0, 0.12])
        
        return overlay_color.blend(color)
    
    ## @brief Set differents context levels for texts depending on its use.
    #
    #  When working with the @ref surface color, a emphasis level blend with the @ref color 
    #  to create different context.
    #
    #  Emphasis colors:
    #   - HIGH     = (0  , 0  , 0  , 87%)
    #   - MEDIUM   = (0  , 0  , 0  , 60%)
    #   - DISABLED = (0  , 0  , 0  , 38%)
    @staticmethod
    def emphasis_on_surface(color: Color, emphasis_level: BaseTheme.EmphasisLevel) -> Color:
        emphasis_blend_color =  ""
        if (emphasis_level == BaseTheme.EmphasisLevel.HIGH):
            emphasis_blend_color = Color.rgba_to_hex([0  , 0  , 0  , 0.87])
        elif (emphasis_level == BaseTheme.EmphasisLevel.MEDIUM):
            emphasis_blend_color = Color.rgba_to_hex([0  , 0  , 0  , 0.60])
        else:
            emphasis_blend_color = Color.rgba_to_hex([0  , 0  , 0  , 0.38])
            
        return Color.blend([emphasis_blend_color, color.getHex()])
    
    ## @brief Set differents context levels for texts depending on its use.
    #
    #  When working with the @ref background color, a emphasis level blend with the @ref color 
    #  to create different context.
    #    
    #  Emphasis colors:
    #   - HIGH     = (0, 0, 0, 100%)
    #   - MEDIUM   = (0, 0, 0,  74%)
    #   - DISABLED = (0, 0, 0,  38%)
    @staticmethod
    def emphasis_on_primary(color: Color, emphasis_level: BaseTheme.EmphasisLevel) -> Color:
        emphasis_blend_color =  ""
        if (emphasis_level == BaseTheme.EmphasisLevel.HIGH):
            emphasis_blend_color = Color.rgba_to_hex((255, 255, 255, 1.00))
        elif (emphasis_level == BaseTheme.EmphasisLevel.MEDIUM):
            emphasis_blend_color = Color.rgba_to_hex((255, 255, 255, 0.74))
        else:
            emphasis_blend_color = Color.rgba_to_hex((255, 255, 255, 0.38))
            
        return Color.blend([emphasis_blend_color, color.getHex()])

if __name__ == "__main__":
    theme = BlackTheme()
    