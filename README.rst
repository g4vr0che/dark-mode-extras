A Toggle Darkly
================

A simple app to enable extra hooks on dark mode changes with GTK-based Linux 
OSs

Basically, A Toggle Darkly watches the gsettings key for the theme and if it 
changes, it parses the contents of the theme name. Themes containing ``-dark``
are assumed to be dark mode (as per guidance from GTK), while all other themes 
are assumed to be light mode. Hooks persistent to the relevant theme mdoe are 
then fired off. 


Toggles
-------

Toggles are simple modules which contain the hooks for each mode. There is a 
standardized ``light_mode()`` and ``dark_mode()`` which trigger each hook. There 
is currently one implemented toggle:

FileToggle
^^^^^^^^^^

A simple toggle which swaps between two different versions of the same config 
file depending on the mode. The files need to be created externally.