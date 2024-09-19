import random
import string
from PIL import Image as PILImage, ImageDraw, ImageFont
from tkinter import *
from tkinter import messagebox
import os
from PIL import Image as Img
import time

class CaptchaApp:
    def __init__(self, root):
        self.root = root
        self.random_text = self.generate_captcha()
        self.photo = PhotoImage(file="out.png")
        self.l1 = Label(root, image=self.photo, height=100, width=200)
        self.l1.image = self.photo
        self.l1.pack()
        self.t1 = Text(root, height=5, width=50)
        self.t1.pack()
        self.b1 = Button(root, text="Submit", command=self.verify)
        self.b1.pack()
        self.b2 = Button(root, text="Refresh", command=self.refresh)
        self.b2.pack()
        self.last_refresh = time.time()

    def generate_captcha(self):
        characters = string.ascii_uppercase + string.digits
        captcha_text = ''.join(random.choice(characters) for _ in range(6))

        img = PILImage.new('RGB', (200, 50), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype('arial.ttf', 24)
        draw.text((10, 10), captcha_text, font=font, fill=(0, 0, 0))

        for _ in range(100):
            x = random.randint(0, 200)
            y = random.randint(0, 50)
            draw.point((x, y), fill=(0, 0, 0))

        img.save('out.png')

        return captcha_text

    def verify(self):
        user_input = self.t1.get("0.0", END)
        if user_input.strip() == self.random_text:
            messagebox.showinfo("Success", "Verified")
        else:
            messagebox.showinfo("Alert", "Not verified")
            self.refresh()

    def refresh(self):
        current_time = time.time()
        if current_time - self.last_refresh < 1:
            messagebox.showinfo("Alert", "Please wait 1 second before refreshing")
            return
        self.last_refresh = current_time
        self.random_text = self.generate_captcha()
        self.photo = PhotoImage(file="out.png")
        self.l1.config(image=self.photo, height=100, width=200)
        self.l1.image = self.photo
        self.l1.update()

root = Tk()
app = CaptchaApp(root)
root.mainloop()