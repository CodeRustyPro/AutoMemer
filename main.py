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
    draw=ImageDraw.Draw(drake)
    font = ImageFont.truetype("Font.ttf",27)
    Text1 = input("Enter drake text(first row) : ")
    Text2 = input("Enter drake text(second row) : ")
    draw.text((360,75),Text1,(0,0,0),font=font)
    draw.text((355,430),Text2,(0,0,0),font=font)
    Result = drake.save("Meme.png")
    print("Image saved as Meme.png")
elif choice==2:
    DisBoy = Image.open("distractedBoyfriend.jpg")
    draw=ImageDraw.Draw(DisBoy)
    font = ImageFont.truetype("Font.ttf",27)
    font1 = ImageFont.truetype("Font.ttf",60)
    font2 = ImageFont.truetype("Font.ttf",48)


    Text1 = input("Enter Original GF text: ")
    Text2 = input("Enter BF text: ")    
    Text3 = input("Enter Other girl text : ")    
    draw.text((700,210),Text1,(0,0,0),font=font)
    draw.text((595,400),Text2,(0,0,0),font=font1)
    draw.text((175,450),Text3,(0,0,0),font=font2)
    Result = DisBoy.save("Meme1.png") 

  
else : 
    print("You messed up !")