## @package themes
#  Themes classes that define rules to how a color scheme will to be.
#  
#  @see 
#  @author Vinicius Casimiro
#  @version 0.1

from abstract_theme import BaseTheme
from utils.color import Color

class BlackTheme(BaseTheme):
    surface = Color("#121212")
    error = Color("#CF6679")
    background = Color("#121212")
    
    def outline(color: Color) -> Color:
        outline_color = Color(255,255,255,0.12)
        outline_color = Color.rgba_to_hex(outline_color)
        
        return Color.blend([outline_color, color])
        
    def surface_overlay(self, color: Color) -> Color:
        overlay_color = (255,255,255,0.12)
        overlay_color = Color.rgba_to_hex(overlay_color)
        
        return Color.blend([overlay_color, color])

    def emphasis_on_surface(self, color: Color, emphasis_level: BaseTheme.EmphasisLevel) -> Color:
        """
        @detailed
        When working with the surface color #121212, a emphasis level blend with the surface color 
        to create different context
        
        Emphasis colors:
            - HIGH     = (255, 255, 255, 87%)
            - MEDIUM   = (255, 255, 255, 74%)
            - DISABLED = (255, 255, 255, 38%)
        """
        emphasis_blend_color =  ""
        if (emphasis_level == BaseTheme.EmphasisLevel.HIGH):
            emphasis_blend_color = Color.rgba_to_hex((255,255,255, 0.87))
        elif (emphasis_level == BaseTheme.EmphasisLevel.MEDIUM):
            emphasis_blend_color = Color.rgba_to_hex((255,255,255, 0.74))
        else:
            emphasis_blend_color = Color.rgba_to_hex((255,255,255, 0.38))
            
        return Color.blend([emphasis_blend_color, color.getHex()])
    
    def emphasis_on_primary(self, color: Color, emphasis_level: BaseTheme.EmphasisLevel) -> str:
        """
        @detailed
        When in a surface #121212, a emphasis level blend with the surface color to create
        different context
        
        Emphasis colors:
            - HIGH     = (0, 0, 0, 100%)
            - MEDIUM   = (0, 0, 0,  74%)
            - DISABLED = (0, 0, 0,  38%)
        """
        emphasis_blend_color =  ""
        if (emphasis_level == BaseTheme.EmphasisLevel.HIGH):
            emphasis_blend_color = Color.rgba_to_hex((0,0,0, 1.00))
        elif (emphasis_level == BaseTheme.EmphasisLevel.MEDIUM):
            emphasis_blend_color = Color.rgba_to_hex((0,0,0, 0.74))
        else:
            emphasis_blend_color = Color.rgba_to_hex((0,0,0, 0.38))
            
        return Color.blend([emphasis_blend_color, color.getHex()])

    
class WhiteTheme(BaseTheme):
    pass


