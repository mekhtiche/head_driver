#!/usr/bin/env python
import thread
import rospy
from std_msgs.msg import String
from Tkinter import *
def show_face(data):
    print "showing image : " + data.data
    #img = PhotoImage(file='emotion.gif')
    #emotion.config(image = img)
    #emotion.image = img

def show_text(data):
    print "showing text : " + data.data
    #emotion.config(image='')
    #text.set("hello")
def face():
    root = Tk()
    root.config(bg="white")
    root.attributes("-fullscreen", True)
    text = StringVar()
    emotion = Label(root, bg = "white", textvariable = text, font="Helvetica 200 bold italic")
    emotion.pack(anchor=CENTER)
    #showimage = Button(root, text="Show Image", command = show_face)
    #showimage.pack(anchor=W)
    #showtext = Button(root, text="Show Text", command = show_text)
    #showtext.pack(anchor=W)
    root.mainloop()

def subscribers():
    rospy.init_node('robot_face', anonymous=True)
    rospy.Subscriber('poppy/face/emotion', String, callback=show_face)
    rospy.Subscriber('poppy/face/text', String, callback=show_text)
    print 'FACE subscribers successful Initial'
    rospy.spin()

if __name__ == '__main__':
    thread.start_new_thread(face, ())
    subscribers()