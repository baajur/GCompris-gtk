# PythonTest Board module
import gobject
import gnomecanvas
import gcompris
import gcompris.utils
import gcompris.skin
import gcompris.admin
import gtk
import gtk.gdk
import random

from gcompris import gcompris_gettext as _

class Gcompris_pythontest:
  """Testing gcompris python class"""


  def __init__(self, gcomprisBoard):
    self.gcomprisBoard = gcomprisBoard

    self.gcomprisBoard.disable_im_context = True

    self.canvasitems = {}

    self.colors = {}
    self.colors['circle_in'] = gcompris.skin.get_color("pythontest/circle in")
    self.colors['circle_out'] = gcompris.skin.get_color("pythontest/circle out")
    self.colors['line'] = gcompris.skin.get_color("pythontest/line")

    # Just for config demo
    self.config_colors = { 'red' : 0xFF0000FFL,
                           'green' : 0x00FF00FFL,
                           'blue' : 0x0000FFFFL }

    # dict .keys() list of keys has random order
    self.config_colors_list = [ 'red', 'green', 'blue']

    self.movingline='none'

    # Find a number game
    self.solution = random.randint(0,9)

    print("Gcompris_pythontest __init__.")

    #initialisation to default values. Some of them will be replaced by
    #the configured values.

  def start(self):
    logged = gcompris.admin.get_current_user()

    # API Test, return the absolute path to this file
    print gcompris.utils.find_file_absolute("sounds/bleep.wav")
#    wordlist = gcompris.get_wordlist('wordslevel_max_pt_BR')
#    print wordlist
#    print wordlist.filename
#    print wordlist.level
#    print wordlist.locale
#    print wordlist.description
#    print wordlist.words


    if logged:
      print "User Logged in:"
      print "   ", logged.login, logged.firstname, logged.lastname

    self.gcomprisBoard.level=1
    self.gcomprisBoard.maxlevel=1
    self.gcomprisBoard.sublevel=1
    self.gcomprisBoard.number_of_sublevel=1

    # init config to default values
    self.config_dict = self.init_config()

    print "init self.config_dict :", self.config_dict

    # change configured values
    print "gcompris.get_board_conf() : ", gcompris.get_board_conf()
    self.config_dict.update(gcompris.get_board_conf())

    print "self.config_dict final :", self.config_dict

    self.previous_locale = gcompris.get_locale()

    if self.config_dict.has_key('locale'):
      gcompris.change_locale(self.config_dict['locale'])

    # self.colors['line'] s set in init.
    # I put here the configuration use

    color_name = self.config_dict['color_line']
    self.colors['line'] = self.config_colors[color_name]

    gcompris.bar_set(gcompris.BAR_CONFIG)
    gcompris.set_background(self.gcomprisBoard.canvas.root(),
                            gcompris.skin.image_to_skin("gcompris-bg.jpg"))
    gcompris.bar_set_level(self.gcomprisBoard)

    # Create our rootitem. We put each canvas item in it so at the end we
    # only have to kill it. The canvas deletes all the items it contains automaticaly.
    self.rootitem = self.gcomprisBoard.canvas.root().add(
      gnomecanvas.CanvasGroup,
      x=0.0,
      y=0.0
      )

    # distance is used to demo of gcompris.spin_int
    distance = eval(self.config_dict['distance_circle'])

    # pattern is for gcompris.radio_buttons
    pattern = self.config_dict['pattern']

    patterns = { 'circle': gnomecanvas.CanvasEllipse,
                 'rectangle': gnomecanvas.CanvasRect
                 }

    #error check
    if not patterns.has_key(pattern):
      pattern = 'circle'

    self.canvasitems[1] = self.rootitem.add(
      patterns[pattern],
      x1=400.0 - distance ,
      y1=200.0,
      x2=380.0 - distance,
      y2=220.0,
      fill_color_rgba= self.colors['circle_in'],
      outline_color_rgba= self.colors['circle_out'],
      width_units=1.0
      )
    self.canvasitems[1].connect("event", self.circle_item_event)

    self.canvasitems[2] = self.rootitem.add(
      patterns[pattern],
      x1=400.0 + distance,
      y1=200.0,
      x2=420.0 + distance,
      y2=220.0,
      fill_color_rgba= self.colors['circle_in'],
      outline_color_rgba= self.colors['circle_out'],
      width_units=1.0
      )
    self.canvasitems[2].connect("event", self.circle_item_event)

    self.canvasitems[3] = self.rootitem.add(
      gnomecanvas.CanvasText,
      x=400.0,
      y=100.0,
      text=_("This is the first plugin in GCompris coded in the Python\nProgramming language."),
      fill_color="black",
      justification=gtk.JUSTIFY_CENTER
      )

    self.canvasitems[4] = self.rootitem.add(
      gnomecanvas.CanvasText,
      x=400.0,
      y=140.0,
      text=_("It is now possible to develop GCompris activities in C or in Python.\nThanks to Olivier Samys who makes this possible."),
      fill_color="black",
      justification=gtk.JUSTIFY_CENTER
      )

    self.canvasitems[5] = self.rootitem.add(
      gnomecanvas.CanvasText,
      x=400.0,
      y=250.0,
      text=_("This activity is not playable, just a test"),
      fill_color="black",
      justification=gtk.JUSTIFY_CENTER
      )

    #----------------------------------------
    # A simple game.
    # Try to hit left shift and right shift together. The peed increases
    self.rootitem.add(
          gnomecanvas.CanvasRect,
          x1=20,
          y1=gcompris.BOARD_HEIGHT-180,
          x2=gcompris.BOARD_WIDTH-20,
          y2=gcompris.BOARD_HEIGHT-10,
          fill_color_rgba=0xe0ecfaFFL,
          outline_color_rgba=0xc3d9f1FFL,
          width_units=2.0)

    # For the game status WIN/LOOSE
    self.canvasitems[6] = self.rootitem.add(
      gnomecanvas.CanvasText,
      x=gcompris.BOARD_WIDTH / 2,
      y=gcompris.BOARD_HEIGHT - 40,
      font=gcompris.skin.get_font("gcompris/content"),
      fill_color_rgba=0x102010FFL,
      justification=gtk.JUSTIFY_CENTER
      )

    self.rootitem.add(
      gnomecanvas.CanvasText,
      x=400.0,
      y=400.0,
      text=("Test your reflex with the counter. Hit the 2 shifts key together.\nHit space to reset the counter and increase the speed.\nBackspace to reset the speed"),
      fill_color="black",
      justification=gtk.JUSTIFY_CENTER
      )

    # The basic tick for object moves
    self.timerinc = 1000

    self.timer_inc  = gobject.timeout_add(self.timerinc, self.timer_inc_display)

    self.counter_left  = 0
    self.counter_right = 0

    self.canvasitems[7] = self.rootitem.add(
      gnomecanvas.CanvasText,
      x=gcompris.BOARD_WIDTH / 2,
      y=gcompris.BOARD_HEIGHT - 80,
      font=gcompris.skin.get_font("gcompris/content"),
      text="Speed="+str(self.timerinc)+" ms",
      fill_color="black",
      justification=gtk.JUSTIFY_CENTER
      )

    self.textitem_left = self.rootitem.add(
      gnomecanvas.CanvasText,
      font=gcompris.skin.get_font("gcompris/content"),
      x=gcompris.BOARD_WIDTH / 3,
      y=gcompris.BOARD_HEIGHT - 40,
      fill_color_rgba=0xFF000FFFL
      )

    self.textitem_right = self.rootitem.add(
      gnomecanvas.CanvasText,
      font=gcompris.skin.get_font("gcompris/content"),
      x=gcompris.BOARD_WIDTH / 1.5,
      y=gcompris.BOARD_HEIGHT - 40,
      fill_color_rgba=0xFF000FFFL
      )

    self.left_continue  = True
    self.right_continue = True

    print("Gcompris_pythontest start.")


  def end(self):

    gcompris.reset_locale()

    # Remove the root item removes all the others inside it
    self.rootitem.destroy()

    if self.timer_inc :
      gobject.source_remove(self.timer_inc)


  def ok(self):
    print("Gcompris_pythontest ok.")


  def repeat(self):
    print("Gcompris_pythontest repeat.")


  def config(self):
    print("Gcompris_pythontest config.")


  def key_press(self, keyval, commit_str, preedit_str):
    utf8char = gtk.gdk.keyval_to_unicode(keyval)
    strn = u'%c' % utf8char

    print("Gcompris_pythontest key press keyval=%i %s" % (keyval, strn))

    win = False

    if (keyval == gtk.keysyms.Shift_L):
      self.left_continue  = False

    if (keyval == gtk.keysyms.Shift_R):
      self.right_continue = False

    if(not self.left_continue and not self.right_continue):
      if(self.counter_left == self.counter_right):
        self.canvasitems[6].set(text="WIN",
                                fill_color_rgba=0x2bf9f2FFL)
        win=True
      else:
        self.canvasitems[6].set(text="LOOSE",
                                fill_color_rgba=0xFF0000FFL)

    if ((keyval == gtk.keysyms.BackSpace) or
        (keyval == gtk.keysyms.Delete)):
      self.timerinc = 1100
      keyval = 32

    if (keyval == 32):
      self.left_continue  = True
      self.right_continue = True
      self.counter_left  = 0
      self.counter_right = 0
      if(win):
        if(self.timerinc>500):
          self.timerinc -= 100
        elif(self.timerinc>200):
          self.timerinc -= 50
        elif(self.timerinc>10):
          self.timerinc -= 10
        elif(self.timerinc>1):
          self.timerinc -= 1

      if(self.timerinc<1):
          self.timerinc = 1

      self.canvasitems[3].set(text="")
      self.canvasitems[6].set(text="")

    self.canvasitems[7].set(text="Speed="+str(self.timerinc)+" ms")

    # Find a number game
    if str(self.solution) == strn:
      print "WIN"
    else:
      print "LOST"

    # Return  True  if you did process a key
    # Return  False if you did not processed a key
    #         (gtk need to send it to next widget)
    return True

  def pause(self, pause):
    print("Gcompris_pythontest pause. %i" % pause)


  def set_level(self, level):
    print("Gcompris_pythontest set level. %i" % level)

# ---- End of Initialisation

  def timer_inc_display(self):

    if(self.left_continue):
      self.textitem_left.set(text=str(self.counter_left))
      self.counter_left += self.timer_inc

    if(self.right_continue):
      self.textitem_right.set(text=str(self.counter_right))
      self.counter_right += self.timer_inc

    self.timer_inc  = gobject.timeout_add(self.timerinc, self.timer_inc_display)

  def circle_item_event(self, widget, event=None):
    if eval(self.config_dict['disable_line']):
      return False

    if event.type == gtk.gdk.BUTTON_PRESS:
      if event.button == 1:
        bounds = widget.get_bounds()
        self.pos_x = (bounds[0]+bounds[2])/2
        self.pos_y = (bounds[1]+bounds[3])/2
        if 'line 1' in self.canvasitems:
          self.canvasitems['line 1'].destroy()
        self.canvasitems['line 1'] = self.rootitem.add(
          gnomecanvas.CanvasLine,
          points=( self.pos_x, self.pos_y, event.x, event.y),
          fill_color_rgba=self.colors['line'],
          width_units=5.0
          )
        self.movingline='line 1'
        print "Button press"
        return True
    if event.type == gtk.gdk.MOTION_NOTIFY:
      if event.state & gtk.gdk.BUTTON1_MASK:
        self.canvasitems[self.movingline].set(
          points=( self.pos_x, self.pos_y, event.x, event.y)
          )
    if event.type == gtk.gdk.BUTTON_RELEASE:
      if event.button == 1:
        self.movingline='line 1'
        print "Button release"
        return True
    return False

  ###################################################
  # Configuration system
  ###################################################

  #mandatory but unused yet
  def config_stop(self):
    pass

  # Configuration function.
  def config_start(self, profile):
    # keep profile in mind
    # profile can be Py_None
    self.configuring_profile = profile

    # init with default values
    self.config_dict = self.init_config()

    #get the configured values for that profile
    self.config_dict.update(gcompris.get_conf(profile, self.gcomprisBoard))

    # Init configuration window:
    # all the configuration functions will use it
    # all the configuration functions returns values for their key in
    # the dict passed to the apply_callback
    # the returned value is the main GtkVBox of the window,
    #we can add what you want in it.

    self.main_vbox = gcompris.configuration_window ( \
      _('<b>%s</b> configuration\n for profile <b>%s</b>') % ('Pythontest', profile.name ),
      self.ok_callback
      )

    # toggle box
    control_line = gcompris.boolean_box(_('Disable line drawing in circle'),
                                        'disable_line',
                                        eval(self.config_dict['disable_line'])
                                        )
    # sample of control in python
    control_line.connect("toggled", self.color_disable)

    # combo box
    self.color_choice = \
       gcompris.combo_box(_('Color of the line'),
                          self.config_colors_list,
                          'color_line',
                          self.config_dict['color_line']
                          )
    self.color_choice.set_sensitive(not eval(self.config_dict['disable_line']))

    gcompris.separator()

    #spin button for int
    self.distance_box = \
       gcompris.spin_int(_('Distance between circles'),
                         'distance_circle',
                         20,
                         200,
                         20,
                         eval(self.config_dict['distance_circle'])
                         )

    gcompris.separator()

    #radio buttons for circle or rectangle
    patterns = { 'circle': _('Use circles'),
                 'rectangle': _('Use rectangles')
                 }

    gcompris.radio_buttons(_('Choice of pattern'),
                           'pattern',
                           patterns,
                           self.config_dict['pattern']
                           )

    print "List of locales shown in gcompris.combo_locale :"
    print gcompris.get_locales_list()

    gcompris.separator()

    gcompris.combo_locales( self.config_dict['locale'])

    gcompris.separator()

    print "List of locales shown in gcompris.combo_locales_asset :"
    locales_purple = gcompris.get_locales_asset_list( "gcompris colors", None, "audio/x-ogg", "purple.ogg")
    print locales_purple

    label = gtk.Label()
    label.set_markup('<i>-- unused, but here for test --</i>')
    label.show()
    self.main_vbox.pack_start (label, False, False, 8)

    gcompris.combo_locales_asset( _("Select sound locale"), self.config_dict['locale_sound'], "gcompris colors", None, "audio/x-ogg", "purple.ogg" )

    print gcompris.utils.get_asset_file ("gcompris colors", None, "audio/x-ogg", "purple.ogg")
    print gcompris.utils.get_asset_file_locale ("gcompris colors", None, "audio/x-ogg", "purple.ogg", None)
    for lang in locales_purple:
      print gcompris.utils.get_asset_file_locale ("gcompris colors", None, "audio/x-ogg", "purple.ogg", lang)

  def color_disable(self, button):
    self.color_choice.set_sensitive(not button.get_active())

  # Callback when the "OK" button is clicked in configuration window
  # this get all the _changed_ values
  def ok_callback(self, table):
    if (table == None):
      print 'Configuration returns None'
      return

    print "Keys and values returned by PythonTest config window:"

    if (len(table) == 0):
        print '%20s' % 'None'

    for key,value in table.iteritems():
      print '%20s:%20s    ' % (key, value)
      gcompris.set_board_conf(self.configuring_profile, self.gcomprisBoard, key, value)


  def init_config(self):
    default_config = { 'disable_line'    : 'False',
                       'color_line'      : 'red',
                       'distance_circle' : '100',
                       'pattern'         : 'circle',
                       'locale'          : 'NULL',
                       'locale_sound'    : 'NULL'
                       }
    return default_config

