from typing import Text
from PIL import Image,ImageFont,ImageDraw

print("\n\n\t\t Welcome To AutoMemer ! Make memes instantly XD")

print("""    _         _        __  __                          
   / \  _   _| |_ ___ |  \/  | ___ _ __ ___   ___ _ __ 
  / _ \| | | | __/ _ \| |\/| |/ _ \ '_ ` _ \ / _ \ '__|
 / ___ \ |_| | || (_) | |  | |  __/ | | | | |  __/ |   
/_/   \_\__,_|\__\___/|_|  |_|\___|_| |_| |_|\___|_|   
""")

print("""
Choose template :
1 : Drake meme
2 : Distracted Boyfriend meme
""")
choice= int(input("Enter the number : "))

if choice == 1:
    drake = Image.open("drake.jpg")
    Result1 = Image.open('drake.jpg')
    draw=ImageDraw.Draw(drake)
    font = ImageFont.truetype("Font.ttf",27)
    Text1 = input("Enter drake text(first row) : ")
    Text2 = input("Enter drake text(second row) : ")
    draw.text((360,75),Text1,(0,0,0),font=font)
    draw.text((355,430),Text2,(0,0,0),font=font)
    Result = drake.save("Meme.png")
    print("Image saved as Meme.png")
else : 
    print("You messed up !")
