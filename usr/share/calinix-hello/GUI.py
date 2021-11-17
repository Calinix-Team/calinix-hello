
import os
import getpass
from os.path import expanduser

DEBUG = False
#DEBUG = True

base_dir = os.path.dirname(os.path.realpath(__file__))
home = expanduser("~")
username = getpass.getuser()

if DEBUG:
    user = username
else:
    user = "liveuser"

Settings = home + "/.config/calinix-hello/settings.conf"
Skel_Settings = "/etc/skel/.config/calinix-hello/settings.conf"
dot_desktop = "/usr/share/applications/calinix-hello.desktop"
autostart = home + "/.config/autostart/calinix-hello.desktop"


def GUI(self, Gtk, GdkPixbuf):

    autostart = eval(self.load_settings())

    self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    self.add(self.vbox)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    # vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    infoE = Gtk.EventBox()
    pbinfo = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/question.png'), 38, 38)
    infoimage = Gtk.Image().new_from_pixbuf(pbinfo)
    infoE.add(infoimage)
    infoE.connect("button_press_event", self.on_info_clicked)
    infoE.set_property("has-tooltip", True)
    infoE.connect("query-tooltip", self.tooltip_callback, "Conflicts Info")

    # ======================================================================
    #                   WELCOME LABEL
    # ======================================================================

    self.cc = Gtk.Label()

    label = Gtk.Label(xalign=0)
    label.set_markup(
        "<big>Welcome to <b>CalinixOS</b></big>")
    label.set_line_wrap(True)

    # pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
    #     os.path.join(base_dir, 'images/arcolinux-one-liner.png'), 145, 145)
    # image = Gtk.Image().new_from_pixbuf(pixbuf)

    label2 = Gtk.Label(xalign=0)
    label2.set_justify(Gtk.Justification.CENTER)
    label2.set_line_wrap(True)

    if username == user:

        label2.set_markup(
            "We advise to clean the computer with Gparted before installing. " +  # noqa
            "Thank you for choosing CalinixOS as your linux distribution. The social links below help you to commmunicate with us interactively and seek support for help. Calinix is our biggest project till now and we are happy to see people choosing it as main \n\n" +  # noqa
            "We appreciate your feed-back and donation.  \nLearn, have fun and enjoy. \n\n" +  # noqa
            "The Calinix Team")
    else:
        label2.set_markup("Thank you for choosing CalinixOS as your linux distribution. The social links below help you to commmunicate with us interactively and seek support for help. Calinix is our biggest project till now and we are happy to see people choosing it as main \n\n" +  # noqa
                          "We appreciate your feed-back and donation.  \nLearn, have fun and enjoy. \n\n" +  # noqa
                          "The Calinix Team")
    # label2.connect( "size-allocate", self.cb_allocate )
    # vbox1.pack_start(image, False, False, 0)
    # vbox2.pack_start(label, False, False, 0)
    # vbox2.pack_start(label2, False, False, 0)
    hbox1.pack_start(label, False, False, 0)
    hbox1.pack_end(self.cc, False, False, 0)
    # hbox4.set_homogeneous(False)
    hbox4.pack_start(label2, False, False, 0)

    # ======================================================================
    #                   MAIN BUTTONS
    # ======================================================================

    button1 = Gtk.Button(label="")
    button1_label = button1.get_child()
    button1_label.set_markup("<span size='large'><b>Run GParted</b></span>")
    button1.connect("clicked", self.on_gp_clicked)
    button1.set_size_request(0, 80)

    button2 = Gtk.Button(label="")
    button2_label = button2.get_child()
    button2_label.set_markup("<span size='large'><b>Installation Guide</b></span>")
 
    button2.connect("clicked", self.on_ai_clicked)
    button2.set_size_request(0, 80)

    buttonca = Gtk.Button(label="")
    buttonca_label = buttonca.get_child()
    buttonca_label.set_markup("<span size='large'><b>Start Installer</b></span>")

    buttonca.connect("clicked", self.on_aica_clicked)
    buttonca.set_size_request(0, 80)


    self.button8 = Gtk.Button(label="")
    button8_label = self.button8.get_child()
    button8_label.set_markup("<span size='large'><b>Get the fastest Arch Linux mirrors</b></span>")
    self.button8.connect("clicked", self.on_mirror_clicked)
    self.button8.set_size_request(420, 70)

    # grid.add(button1)
    if username == user:
        grid = Gtk.Grid()
        grid.attach(self.button8, 2, 0, 2, 2)
        #grid.attach(button13, 2, 0, 2, 2)
        grid.attach(button1, 2, 2, 2, 2)
        grid.attach(button2, 1, 4, 2, 2)
        grid.attach(buttonca, 3, 4, 2, 2)
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
    else:
        grid = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.button8.set_size_request(420, 70)
        grid.pack_start(self.button8, True, False, 0)
    # grid.set_row_homogeneous(True)

    # ======================================================================
    #                   NOTICE
    # ======================================================================

    # label3 = Gtk.Label(xalign=0)
    # label3.set_line_wrap(True)

    # label4 = Gtk.Label(xalign=0)
    # label4.set_line_wrap(True)

    # self.vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    # self.vbox2.pack_start(label3, False,False,0)
    # self.vbox2.pack_start(label4, False,False,0)

    # ======================================================================
    #                   USER INFO
    # ======================================================================

    lblusrname = Gtk.Label(xalign=0)
    lblusrname.set_text("User:")

    lblpassword = Gtk.Label(xalign=0)
    lblpassword.set_text("Pass:")

    lblusr = Gtk.Label(xalign=0)
    lblusr.set_text("liveuser  |")

    lblpass = Gtk.Label(xalign=0)
    lblpass.set_markup("<i>No Password</i>")

    hboxUser = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hboxUser.pack_start(lblusrname, False, False, 0)
    hboxUser.pack_start(lblusr, False, False, 0)

    hboxUser.pack_start(lblpassword, False, False, 0)
    hboxUser.pack_start(lblpass, False, False, 0)

    # ======================================================================
    #                   FOOTER BUTTON LINKS
    # ======================================================================
    button3 = Gtk.Button(label="Release info")
    button3.connect("clicked", self.on_link_clicked,
                    "https://github.com/Calinix-Team/Calinix-Arch/releases/")

    button4 = Gtk.Button(label="Choose your project")
    button4.connect("clicked", self.on_link_clicked,
                    "https://get.calinix.tech/download.html/")

    button5 = Gtk.Button(label="Core info")
    button5.connect("clicked", self.on_link_clicked,
                    "https://get.calinix.tech/spotlights.html/")

    button6 = Gtk.Button(label="Reddit")
    button6.connect("clicked", self.on_link_clicked,
                    "http://reddit.com/r/CalinixOS")
    
    button7 = Gtk.Button(label="Forum")
    button7.connect("clicked", self.on_link_clicked,
                    "http://calinixos.forummotion.com/")

    hbox2.pack_start(button3, True, True, 0)
    hbox2.pack_start(button4, True, True, 0)
    hbox2.pack_start(button5, True, True, 0)
    hbox2.pack_start(button6, True, True, 0)
    hbox2.pack_start(button7, True, True, 0)

    button8 = Gtk.Button(label="")
    button8_label = button8.get_child()
    button8_label.set_markup("<b>Donate</b>")
    button8.connect("clicked", self.on_link_clicked,
                    "https://buymeacoffee.com/team.calinix")

    button9 = Gtk.Button(label="Get Involved")
    button9.connect("clicked", self.on_link_clicked,
                    "https://tinyurl.com/calinixdisc/")

    button10 = Gtk.Button(label="Debug")
    button10.connect("clicked", self.on_link_clicked,
                     "https://github.com/Calinix-Team/Calinix-Arch/issues/")

    button11 = Gtk.Button(label="Youtube")
    button11.connect("clicked", self.on_link_clicked,
                     "https://www.youtube.com/channel/UCyyXcHm8UswsF0cjOX6fMng")

    button12 = Gtk.Button(label="Quit")
    button12.set_size_request(200, 50)
    button12.connect("clicked", Gtk.main_quit)
    button12.set_tooltip_markup("Quit the Calinix Hello App")

    hbox5.pack_start(button8, True, True, 0)
    hbox5.pack_start(button9, True, True, 0)
    hbox5.pack_start(button10, True, True, 0)
    hbox5.pack_start(button11, True, True, 0)
    hbox5.pack_start(button12, True, True, 0)


    # hbox8.pack_start(self.button8, True, False, 0)

    # ======================================================================
    #                   Add to startup
    # ======================================================================

    check = Gtk.CheckButton(label="Autostart")
    check.connect("toggled", self.statup_toggle)
    check.set_active(autostart)
    hbox3.pack_end(check, False, False, 0)

    # ======================================================================
    #                   SOCIAL LINKS
    # ======================================================================
    fbE = Gtk.EventBox()
    tE = Gtk.EventBox()
    meE = Gtk.EventBox()
    inE = Gtk.EventBox()
    liE = Gtk.EventBox()
    pE = Gtk.EventBox()
    dE = Gtk.EventBox()
    tgE = Gtk.EventBox()

    pbd = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/discord.png'), 28, 28)
    dimage = Gtk.Image().new_from_pixbuf(pbd)

    pbtg = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/tg.png'), 28, 28)
    tgimage = Gtk.Image().new_from_pixbuf(pbtg)

    dE.add(dimage)
    tgE.add(tgimage)
    
    dE.connect("button_press_event", self.on_social_clicked,
               "https://tinyurl.com/calinixdisc")
    tgE.connect("button_press_event", self.on_social_clicked,
                "https://t.me/joinchat/_Sk3DB_FEbdhYTU1")

    dE.set_property("has-tooltip", True)
    tgE.set_property("has-tooltip", True)

    dE.connect("query-tooltip", self.tooltip_callback, "Discord")
    tgE.connect("query-tooltip", self.tooltip_callback, "Telegram")

    hbox3.pack_start(fbE, False, False, 0)
    hbox3.pack_start(tE, False, False, 0)
    hbox3.pack_start(meE, False, False, 0)
    hbox3.pack_start(inE, False, False, 0)
    hbox3.pack_start(liE, False, False, 0)
    hbox3.pack_start(pE, False, False, 0)

    hbox6.pack_start(dE, False, False, 0)
    hbox6.pack_start(tgE, False, False, 0)
    if username == user:
        hbox3.pack_start(hboxUser, True, False, 0)
    hbox3.pack_start(hbox6, True, False, 0)

    # ======================================================================
    #                   Start Calinix Help Tool
    # ======================================================================
    launchBox = Gtk.EventBox()
    pblaunch = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/hefftor.svg'), 40, 40)
    launchimage = Gtk.Image().new_from_pixbuf(pblaunch)

    launchBox.add(launchimage)
    launchBox.connect("button_press_event", self.on_launch_clicked, "")

    launchBox.set_property("has-tooltip", True)
    launchBox.connect("query-tooltip",
                      self.tooltip_callback,
                      "Run Calinix Help")

    hbox6.pack_start(launchBox, False, False, 0)
    hbox6.pack_start(infoE, False, False, 0)
    # ======================================================================
    #                   PACK TO WINDOW
    # ======================================================================
    label3 = Gtk.Label("0.6-4")
    hbox7.pack_end(label3, False, False, 0)
    # if self.is_connected():
    #     self.get_message(label3, label4)

    self.vbox.pack_start(hbox1, False, False, 7)  # Logo
    self.vbox.pack_start(hbox4, False, False, 7)  # welcome Label

    self.vbox.pack_start(grid, True, False, 7)  # Run GParted/Calamares

    # if self.results and self.is_connected():
    #     self.vbox.pack_start(self.vbox2, False, False, 0)  # Notice

    self.vbox.pack_end(hbox3, False, False, 0)  # Footer
    #self.vbox.pack_end(hbox7, False, False, 0)  # Version
    self.vbox.pack_end(hbox5, False, False, 7)  # Buttons
    self.vbox.pack_end(hbox2, False, False, 7)  # Buttons
