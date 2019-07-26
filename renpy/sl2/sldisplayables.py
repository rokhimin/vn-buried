# Copyright 2004-2014 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

##############################################################################
# Definitions of screen language statements.

import renpy.display
import renpy.text.text

from renpy.sl2.slparser import Positional, Keyword, Style, PrefixStyle, add
from renpy.sl2.slparser import DisplayableParser, many

position_property_names = [
        "anchor",
        "xanchor",
        "yanchor",
        "pos",
        "xpos",
        "ypos",
        "align",
        "xalign",
        "yalign",
        "xoffset",
        "yoffset",
        "maximum",
        "xmaximum",
        "ymaximum",
        "area",
        "clipping",
        "xfill",
        "yfill",
        # no center, since it can conflict with the center transform.
        "xcenter",
        "ycenter",
        "xsize",
        "ysize",
        "xysize",
        ]

position_properties = [ Style(i) for i in position_property_names ]
text_position_properties = [ PrefixStyle("text_", i) for i in position_property_names ]
side_position_properties = [ PrefixStyle("side_", i) for i in position_property_names ]

text_property_names = [
        "antialias",
        "vertical",
        "black_color",
        "bold",
        "color",
        "drop_shadow",
        "drop_shadow_color",
        "first_indent",
        "font",
        "size",
        "hyperlink_functions",
        "italic",
        "justify",
        "kerning",
        "language",
        "layout",
        "line_leading",
        "line_spacing",
        "minwidth",
        "min_width",
        "newline_indent",
        "outlines",
        "rest_indent",
        "ruby_style",
        "slow_cps",
        "slow_cps_multiplier",
        "slow_abortable",
        "strikethrough",
        "text_align",
        "text_y_fudge",
        "underline",
        "minimum",
        "xminimum",
        "yminimum",
        ]

text_properties = [ Style(i) for i in text_property_names ]
text_text_properties = [ PrefixStyle("text_", i) for i in text_property_names ]

window_properties = [ Style(i) for i in [
        "background",
        "foreground",
        "left_margin",
        "right_margin",
        "bottom_margin",
        "top_margin",
        "xmargin",
        "ymargin",
        "left_padding",
        "right_padding",
        "top_padding",
        "bottom_padding",
        "xpadding",
        "ypadding",
        "size_group",
        "minimum",
        "xminimum",
        "yminimum",
        ] ]

button_properties = [ Style(i) for i in [
        "sound",
        "mouse",
        "focus_mask",
        "child",
        ] ]

bar_properties = [ Style(i) for i in [
        "bar_vertical",
        "bar_invert",
        "bar_resizing",
        "left_gutter",
        "right_gutter",
        "top_gutter",
        "bottom_gutter",
        "left_bar",
        "right_bar",
        "top_bar",
        "bottom_bar",
        "thumb",
        "thumb_shadow",
        "thumb_offset",
        "mouse",
        "unscrollable",
        ] ]

box_properties = [ Style(i) for i in [
        "box_layout",
        "box_wrap",
        "box_reverse",
        "order_reverse",
        "spacing",
        "first_spacing",
        "fit_first",
        "minimum",
        "xminimum",
        "yminimum",
        ] ]

ui_properties = [
    Keyword("at"),
    Keyword("id"),
    Keyword("style"),
    Keyword("style_group"),
    Keyword("focus"),
    Keyword("default"),
    ]


DisplayableParser("null", renpy.display.layout.Null, "default", 0)
Keyword("width")
Keyword("height")
add(ui_properties)
add(position_properties)

DisplayableParser("text", renpy.text.text.Text, "text", 0, scope=True, replaces=True)
Positional("text")
Keyword("slow")
Keyword("slow_done")
Keyword("substitute")
Keyword("scope")
add(ui_properties)
add(position_properties)
add(text_properties)

DisplayableParser("hbox", renpy.display.layout.MultiBox, "hbox", many)
add(ui_properties)
add(position_properties)
add(box_properties)

DisplayableParser("vbox", renpy.display.layout.MultiBox, "vbox", many)
add(ui_properties)
add(position_properties)
add(box_properties)

DisplayableParser("fixed", renpy.display.layout.Fixed, "fixed", many)
add(ui_properties)
add(position_properties)
add(box_properties)

DisplayableParser("grid", renpy.display.layout.Grid, "grid", many)
Positional("cols")
Positional("rows")
Keyword("transpose")
Style("spacing")
add(ui_properties)
add(position_properties)

DisplayableParser("side", renpy.display.layout.Side, "side", many)
Positional("positions")
Style("spacing")
add(ui_properties)
add(position_properties)

# Omit sizer, as we can always just put an xmaximum and ymaximum on an item.

for name in [ "window", "frame" ]:
    DisplayableParser(name, renpy.display.layout.Window, name, 1)
    add(ui_properties)
    add(position_properties)
    add(window_properties)

DisplayableParser("key", renpy.ui._key, None, 0)
Positional("key")
Keyword("action")

DisplayableParser("timer", renpy.display.behavior.Timer, "default", 0, replaces=True)
Positional("delay")
Keyword("action")
Keyword("repeat")

# Omit behaviors.
# Omit menu as being too high-level.

DisplayableParser("input", renpy.display.behavior.Input, "input", 0, replaces=True)
Keyword("default")
Keyword("length")
Keyword("allow")
Keyword("exclude")
Keyword("prefix")
Keyword("suffix")
Keyword("changed")
Keyword("pixel_width")
add(ui_properties)
add(position_properties)
add(text_properties)

DisplayableParser("image", renpy.display.im.image, "default", 0)
Positional("im")

# Omit imagemap_compat for being too high level (and obsolete).

DisplayableParser("button", renpy.display.behavior.Button, "button", 1)
Keyword("action")
Keyword("clicked")
Keyword("hovered")
Keyword("unhovered")
Keyword("alternate")
add(ui_properties)
add(position_properties)
add(window_properties)
add(button_properties)

DisplayableParser("imagebutton", renpy.ui._imagebutton, "image_button", 0)
Keyword("auto")
Keyword("idle")
Keyword("hover")
Keyword("insensitive")
Keyword("selected_idle")
Keyword("selected_hover")
Keyword("selected_insensitive")
Keyword("action")
Keyword("clicked")
Keyword("hovered")
Keyword("unhovered")
Keyword("alternate")
Keyword("image_style")
add(ui_properties)
add(position_properties)
add(window_properties)
add(button_properties)

DisplayableParser("textbutton", renpy.ui._textbutton, 0, scope=True)
Positional("label")
Keyword("action")
Keyword("clicked")
Keyword("hovered")
Keyword("unhovered")
Keyword("alternate")
Keyword("text_style")
Keyword("substitute")
Keyword("scope")
add(ui_properties)
add(position_properties)
add(window_properties)
add(button_properties)
add(text_position_properties)
add(text_text_properties)

DisplayableParser("label", renpy.ui._label, "label", 0, scope=True)
Positional("label")
Keyword("text_style")
add(ui_properties)
add(position_properties)
add(window_properties)
add(text_position_properties)
add(text_text_properties)

for name in [ "bar", "vbar" ]:
    DisplayableParser(name, renpy.display.behavior.Bar, name, 0, replaces=True)
    Keyword("adjustment")
    Keyword("range")
    Keyword("value")
    Keyword("changed")
    Keyword("hovered")
    Keyword("unhovered")
    add(ui_properties)
    add(position_properties)
    add(bar_properties)

# Omit autobar. (behavior)

DisplayableParser("viewport", renpy.ui._viewport, "viewport", 1, replaces=True)
Keyword("child_size")
Keyword("mousewheel")
Keyword("draggable")
Keyword("edgescroll")
Keyword("xadjustment")
Keyword("yadjustment")
Keyword("xinitial")
Keyword("yinitial")
Keyword("scrollbars")
PrefixStyle("side_", "spacing")
add(ui_properties)
add(position_properties)
add(side_position_properties)

DisplayableParser("imagemap", renpy.ui._imagemap, "imagemap", many, imagemap=True)
Keyword("ground")
Keyword("hover")
Keyword("insensitive")
Keyword("idle")
Keyword("selected_hover")
Keyword("selected_idle")
Keyword("selected_insensitive")
Keyword("auto")
Keyword("alpha")
Keyword("cache")
add(ui_properties)
add(position_properties)

DisplayableParser("hotspot", renpy.ui._hotspot, "hotspot", 1)
Positional("spot")
Keyword("action")
Keyword("clicked")
Keyword("hovered")
Keyword("unhovered")
add(ui_properties)
add(position_properties)
add(window_properties)
add(button_properties)

DisplayableParser("hotbar", renpy.ui._hotbar, "hotbar", 0, replaces=True)
Positional("spot")
Keyword("adjustment")
Keyword("range")
Keyword("value")
add(ui_properties)
add(position_properties)
add(bar_properties)


DisplayableParser("transform", renpy.display.motion.Transform, "transform", 1)
Keyword("at")
Keyword("id")
for i in renpy.atl.PROPERTIES:
    Style(i)

DisplayableParser("add", renpy.ui._add, None, 0)
Positional("im")
Keyword("at")
Keyword("id")
for i in renpy.atl.PROPERTIES:
    Style(i)

DisplayableParser("on", renpy.ui.on, None, 0)
Positional("event")
Keyword("action")

DisplayableParser("drag", renpy.display.dragdrop.Drag, None, 1, replaces=True)
Keyword("drag_name")
Keyword("draggable")
Keyword("droppable")
Keyword("drag_raise")
Keyword("dragged")
Keyword("dropped")
Keyword("drag_handle")
Keyword("drag_joined")
Keyword("clicked")
Keyword("hovered")
Keyword("unhovered")
Style("child")
add(ui_properties)
add(position_properties)

DisplayableParser("draggroup", renpy.display.dragdrop.DragGroup, None, many, replaces=True)
add(ui_properties)
add(position_properties)

DisplayableParser("mousearea", renpy.display.behavior.MouseArea, 0, replaces=True)
Keyword("hovered")
Keyword("unhovered")
add(ui_properties)
add(position_properties)



