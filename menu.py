# Import Tkinter library
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import subprocess

# Create the main window
window = tk.Tk()
window.title("Face Detection Project By Aditya Bahl")
window.geometry("950x400")


choice = 0
print("Switch over to the tkinter GUI")

# Create a function to open report.pdf
def report():
    path = 'report.pdf'
    subprocess.Popen([path], shell=True)

# Create a function to change mode in program 1 to select user given images
def SelImg():
    global choice
    choice = 1

# Create a function to change mode in program 1 to default
def DefImg():
    global choice
    choice = 0

# Create a function to show applications of Face Detection in Real World
def applications():
    messagebox.showinfo('Applications', '1. Image Recognition\n2. Speech Recognition\n3. Traffic prediction\n4. Product recommendations\n5. Self-driving cars\n6. Email Spam and Malware Filtering\n7. Virtual Personal Assistant\n8. Online Fraud Detection\n9. Stock Market trading\n10. Medical Diagnosis\n11. Automatic Language Translation')

# Create a function to show Information on Face Detection
def FD():
    messagebox.showinfo(
        'Face Detection', 'This code loads an image and runs a Haar cascade face detection model on it. The Haar cascade is a machine learning object detection method used to identify objects in images.\nIt works by training a classifier on positive and negative images and then using it to detect objects in new images.The code then draws rectangles around the detected faces and displays the image with the rectangles.')

# Create a function to show about menu section
def about():
    messagebox.showinfo(
        'About', 'This is a mini-project by:\n->Aditya Bahl\n->5th sem\n->2016580\nfor Face Detection')

# Create a function to run program 1 processes
def prog1Process(face_cascade, image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # To run the face detection model images
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # To draw a rectangle around the detected faces for presentation
    for(x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the image
    cv2.imshow('Face Detection', image)
    cv2.waitKey()

# Create a function to run program 1
def run_program_1():
    # Code for running program 1 goes here
    print("Running program 1")
    # Load the Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # After Loading the image, we shall convert it to grayscale
    if(choice == 0):
        for i in {'test1.jpg', 'test2.jpg', 'test3.jpg'}:
            image = cv2.imread(i)
            prog1Process(face_cascade, image)

    # if user wishes to select from own, un-comment the below 3 lines and comment the above 3 lines
    if(choice == 1):
        filePath = filedialog.askopenfilename()
        image = cv2.imread(filePath)
        prog1Process(face_cascade, image)

# end of program 1
    
# Create a function to run program 2
def run_program_2():
    # Code for running program 2 goes here
    print("Running program 2")
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    # cap=cv2.VideoCapture('filename')
    while True:
        _, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('img', img)
        # cv2.waitKey()
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()

    # to close the webcam window, press esc
# end of program 2

# Create a menu bar
menu_bar = tk.Menu(window)

# Create a menu with commands
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Select Image", command=SelImg)
file_menu.add_command(label="Default Images", command=DefImg)
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_command(label="About Me", command=about)
menu_bar.add_command(label='Project', command=FD)
menu_bar.add_command(label='Applications', command=applications)
menu_bar.add_command(label='Report', command=report)

# Create a label with text for Application Name
label = tk.Label(window, text="  Face Detection", font=("Helvetica", 25))

# Add the label to the window
label.grid()

#Button 1
button1 = tk.Button(window, text='Face Detection for sample image(s)',
                    command=run_program_1, height=5, width=30,  padx=3, pady=3)
# button1.pack()
button1.grid(row=4, column=1, padx=5, pady=10)

#Button 2
button2 = tk.Button(window, text='Face Detection for Live Webcam',
                    command=run_program_2, height=5, width=30, padx=3, pady=3)
# button2.pack()
button2.grid(row=4, column=2, padx=5, pady=30)

# Display the menu bar
window.config(menu=menu_bar)

# Create a label with text
label = tk.Label(window, text="\n\n\n\n\n\n\n\n\n\n\n      Made by Aditya Bahl,5th Sem(2022-23)", font=("Arial", 10))

# Add the label to the window
label.grid()

# Run the GUI
window.mainloop()

print("Thank you!")
