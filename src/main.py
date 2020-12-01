#!/usr/bin/python3

import gi, os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

books_img_list = []
for file in os.listdir("assets"):
    if file.endswith(".jpg"):
        books_img_list.append(os.path.join("assets", file))
show_book = 0

builder = Gtk.Builder()
builder.add_from_file("src/ui/main.glade")

def update_books_imgs():
	books_length = len(books_img_list)
	for i in range(books_length):
		img1 = builder.get_object("image1")
		img2 = builder.get_object("image2")
		img3 = builder.get_object("image3")
		img4 = builder.get_object("image4")
		img1.set_from_file(books_img_list[(i+show_book)%books_length])
		img2.set_from_file(books_img_list[(i+show_book+1)%books_length])
		img3.set_from_file(books_img_list[(i+show_book+2)%books_length])
		img4.set_from_file(books_img_list[(i+show_book+3)%books_length])
update_books_imgs()

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def on_quitButton_clicked(self, *args):
    	Gtk.main_quit()

    def on_backButton_clicked(self, *args):
    	global show_book
    	show_book -= 1
    	update_books_imgs()

    def on_forwardButton_clicked(self, *args):
    	global show_book
    	show_book += 1
    	update_books_imgs()

    def on_textbuffer1_changed(self, *args):
    	button = builder.get_object("quitButton")
    	button.set_label("Quit")
    	# image=Gtk.Image.set_from_icon_name("filesave",Gtk.IconSize.MENU)
    	# image.show()
    	# button.image.clear()
    	# button.add(image)

window = builder.get_object("mainWindow")
window.show_all()

builder.connect_signals(Handler())

Gtk.main()