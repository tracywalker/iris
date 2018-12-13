from core.screen.screen import Screen
from core.finder.pattern import Pattern
from core.finder.finder import find_all, find, verify, match_template
from core.screen.region import Region
from core.enums import MatchTemplateType
from core.mouse.mouse_controller import Mouse
from core.helpers.location import Location
import time

region = Region(0, 50, 300, 200)
# region.highlight()
# print(region.double_click(Pattern('test.png', application='firefox')))
print(region.exists('Project', 'Word found'))







