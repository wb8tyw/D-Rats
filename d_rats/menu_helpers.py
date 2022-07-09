'''Menu Helpers.'''
#
# Copyright 2022 John Malmberg <wb8tyw@gmail.com>
# Portions derived from works:
# Copyright 2009 Dan Smith <dsmith@danplanet.com>
# review 2019 Maurizio Andreotti  <iz2lxi@yahoo.it>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gdk
from gi.repository import Gtk


def _add_menu_accel_image(menu_item, menu_icon, label_text,
                         accel_key_char, accel_mods):
    '''
    Add Menu with Accelerator and Theme Image.

    :param menu_item: Menu item object
    :type menu_item: :class:`Gtk.MenuItem`
    :param icon_name: Icon image
    :type icon_name: :class:`Gtk.Image`
    :param label_text: Text for label
    :type label_text: str
    :param accel_key_char: Accelerator Key character, Default None
    :type accel_key_char: str
    :param accel_mods: Modifiers for key
    :type accel_mods: :class:`Gdk.ModifierType`
    '''
    accel_key = Gdk.unicode_to_keyval(ord(accel_key_char))
    menu_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
    menu_box.add(menu_icon)
    label = Gtk.AccelLabel.new(label_text)
    accel_group = Gtk.AccelGroup.new()
    label.set_xalign(0.0)
    menu_item.add_accelerator("activate", accel_group,
                              accel_key,
                              accel_mods,
                              Gtk.AccelFlags.VISIBLE)
    menu_box.pack_end(label, True, True, 0)
    label.set_accel_widget(menu_item)
    menu_item.add(menu_box)
    menu_item.show_all()

def add_menu_accel_theme_image(menu_item, icon_name, label_text,
                               accel_key_char, accel_mods):
    '''
    Add Menu with Accelerator and Theme Image.

    :param menu_item: Menu item object
    :type menu_item: :class:`Gtk.MenuItem`
    :param icon_name: Named Icon
    :type icon_name: str
    :param label_text: Text for label
    :type label_text: str
    :param accel_key_char: Accelerator Key character, Default None
    :type accel_key_char: str
    :param accel_mods: Modifiers for key
    :type accel_mods: :class:`Gdk.ModifierType`
    '''
    menu_icon = Gtk.Image.new_from_icon_name(icon_name, Gtk.IconSize.MENU)
    _add_menu_accel_image(menu_item, menu_icon, label_text,
                          accel_key_char, accel_mods)


def add_menu_accel_file_image(menu_item, icon_file, label_text,
                              accel_key_char, accel_mods):
    '''
    Add Menu with Accelerator and Theme Image.

    :param menu_item: Menu item object
    :type menu_item: :class:`Gtk.MenuItem`
    :param icon_name: File with icon
    :type icon_name: str
    :param label_text: Text for label
    :type label_text: str
    :param accel_key_char: Accelerator Key character, Default None
    :type accel_key_char: str
    :param accel_mods: Modifiers for key
    :type accel_mods: :class:`Gdk.ModifierType`
    '''
    image = Gtk.Image()
    image.set_from_file(icon_file)
    _add_menu_accel_image(menu_item, image, label_text,
                          accel_key_char, accel_mods)


def add_menu_theme_image(menu_item, icon_name, label_text):
    '''
    Add Menu with Theme Image.

    :param menu_item: Menu item object
    :type menu_item: :class:`Gtk.MenuItem`
    :param icon_name: Named Icon
    :type icon_name: str
    :param label_text: Text for label
    :type label_text: str
    '''
    menu_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
    menu_icon = Gtk.Image.new_from_icon_name(icon_name, Gtk.IconSize.MENU)
    menu_box.add(menu_icon)
    label = Gtk.Label.new(label_text)
    label.set_xalign(0.0)
    menu_box.add(label)
    menu_item.add(menu_box)
    menu_item.show_all()
