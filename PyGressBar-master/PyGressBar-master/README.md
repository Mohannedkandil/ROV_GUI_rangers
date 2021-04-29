# PyGressBar
Simple progress bar with pygame

Class `PyGressBar.bar(maximum, minimum, ticklen, height, bgcolor, bcolor, wx, wy)` creates the `bar` instance, you can only have one at a time due to limitations in pygame.

`maximum`: max value

`minimum`: min value

`ticklen`: distance between two values in px

`height`: bar height in px

`bgcolor`: background color [r,g,b]

`bcolor`: bar color [r,g,b]

`wx`, `wy`: Bar position. You must specify both or it will use system default.

All args are optional, and defaults to max=100, min=0, ticklen=2, height=100, bgcolor=[0,0,0], bcolor=[0,255,0], wx=None, wy=None

Method `bar.setval(val)` sets bar length to `val`

Mathod `bar.end()` closes a progress bar
