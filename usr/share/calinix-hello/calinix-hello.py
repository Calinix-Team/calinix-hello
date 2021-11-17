#!/usr/bin/env python3
# ==================================================
# =          Authors: Arghya Sarkar                =
# ==================================================
import gi
import os
import GUI
import conflicts
# import wnck
import subprocess
import threading
import webbrowser
import shutil
import socket
from time import sleep
gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib, Wnck  # noqa

REMOTE_SERVER = "www.google.com"


class Main(Gtk.Window):
    def __init__(self):
        super(Main, self).__init__(title="Welcome To CalinixOS")
        self.set_border_width(10)
        self.set_default_size(860, 250)
        self.set_icon_from_file(os.path.join(
            GUI.base_dir, 'images/arcolinux.png'))
        self.set_position(Gtk.WindowPosition.CENTER)
        self.results = ""
        if not os.path.exists(GUI.home + "/.config/calinix-hello/"):
            os.mkdir(GUI.home + "/.config/calinix-hello/")
            with open(GUI.Settings, "w") as f:
                f.write("autostart=True")
                f.close()

        GUI.GUI(self, Gtk, GdkPixbuf)

        if GUI.username == GUI.user:
            t = threading.Thread(target=self.internet_notifier, args=())
            t.daemon = True
            t.start()

    def on_mirror_clicked(self, widget):
        t = threading.Thread(target=self.mirror_update)
        t.daemon = True
        t.start()

    def on_update_clicked(self, widget):
        print("Clicked")

    def on_ai_clicked(self, widget):
        subprocess.Popen(["/usr/bin/calamares_polkit", "-d"], shell=False)
     
    def on_aica_clicked(self, widget):
        subprocess.Popen(["/usr/bin/calamares_polkit", "-d"], shell=False)  

    def on_gp_clicked(self, widget):
        t = threading.Thread(target=self.run_app, args=(["/usr/bin/gparted"],))
        t.daemon = True
        t.start()

    def run_app(self, command):
        subprocess.call(command,
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

    def statup_toggle(self, widget):
        if widget.get_active() is True:
            if os.path.isfile(GUI.dot_desktop):
                shutil.copy(GUI.dot_desktop, GUI.autostart)
        else:
            if os.path.isfile(GUI.autostart):
                os.unlink(GUI.autostart)
        self.save_settings(widget.get_active())

    def save_settings(self, state):
        with open(GUI.Settings, "w") as f:
            f.write("autostart=" + str(state))
            f.close()

    def load_settings(self):
        line = "True"
        if os.path.isfile(GUI.Settings):
            with open(GUI.Settings, "r") as f:
                lines = f.readlines()
                for i in range(len(lines)):
                    if "autostart" in lines[i]:
                        line = lines[i].split("=")[1].strip().capitalize()
                f.close()
        return line

    def on_link_clicked(self, widget, link):
        t = threading.Thread(target=self.weblink, args=(link,))
        t.daemon = True
        t.start()

    def on_social_clicked(self, widget, event, link):
        t = threading.Thread(target=self.weblink, args=(link,))
        t.daemon = True
        t.start()

    def on_info_clicked(self, widget, event):
        window_list = Wnck.Screen.get_default().get_windows()
        state = False
        for win in window_list:
            if "Information" in win.get_name():
                state = True
        if not state:
            w = conflicts.Conflicts()
            w.show_all()

    def weblink(self, link):
        webbrowser.open_new_tab(link)

    def is_connected(self):
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            s.close()
            return True
        except:  # noqa
            pass
        return False

    def tooltip_callback(self, widget, x, y, keyboard_mode, tooltip, text):
        tooltip.set_text(text)
        return True

    def on_launch_clicked(self, widget, event, link):
        if os.path.isfile("/usr/bin/calinix-help-tool"):
            t = threading.Thread(target=self.run_app,
                                 args=("/usr/local/bin/calinix-help-tool",))
            t.daemon = True
            t.start()
        else:
            md = Gtk.MessageDialog(parent=self,
                                   flags=0,
                                   message_type=Gtk.MessageType.INFO,
                                   buttons=Gtk.ButtonsType.YES_NO,
                                   text="Not Found!")
            md.format_secondary_markup(
                "<b>Calinix Settings</b> was not found on your system\n\
Do you want to install it?")

            result = md.run()

            md.destroy()

            if result in (Gtk.ResponseType.OK, Gtk.ResponseType.YES):
                t1 = threading.Thread(target=self.installATT, args=())
                t1.daemon = True
                t1.start()

    def internet_notifier(self):
        bb = 0
        dis = 0
        while(True):
            if not self.is_connected():
                dis = 1
                GLib.idle_add(self.button8.set_sensitive, False)
                GLib.idle_add(self.cc.set_markup, "<span foreground='orange'><b><i>Not connected to internet</i></b> \nCalamares will <b>not</b> install additional software</span>")  # noqa
            else:
                if bb == 0 and dis == 1:
                    GLib.idle_add(self.button8.set_sensitive, True)
                    GLib.idle_add(self.cc.set_text, "")
                    bb = 1
            sleep(3)

    def mirror_update(self):
        GLib.idle_add(self.cc.set_markup, "<span foreground='orange'><b><i>Updating your mirrorlist</i></b> \nThis may take some time, please wait...</span>")  # noqa
        GLib.idle_add(self.button8.set_sensitive, False)
        subprocess.run(["pkexec", "/usr/bin/reflector", "--age", "6", "--latest", "21", "--fastest", "21", "--threads", "21", "--sort", "rate", "--protocol", "https", "--save", "/etc/pacman.d/mirrorlist"], shell=False)
        print("FINISHED!!!")
        GLib.idle_add(self.cc.set_markup, "<b>DONE</b>")
        GLib.idle_add(self.button8.set_sensitive, True)
    def MessageBox(self, title, message):
        md = Gtk.MessageDialog(parent=self,
                               flags=0,
                               message_type=Gtk.MessageType.INFO,
                               buttons=Gtk.ButtonsType.OK,
                               text=title)
        md.format_secondary_markup(message)
        md.run()
        md.destroy()


    def installCHT(self):
        subprocess.call(["pkexec",
                         "/usr/bin/pacman",
                         "-S",
                         "calinix-help-tool-git",
                         "--noconfirm"], shell=False)
        GLib.idle_add(self.MessageBox,
                      "Success!",
                      "<b>Calinix Help Tool</b> has been installed successfully")  # noqa

if __name__ == "__main__":
    w = Main()
    w.connect("delete-event", Gtk.main_quit)
    w.show_all()
    Gtk.main()
