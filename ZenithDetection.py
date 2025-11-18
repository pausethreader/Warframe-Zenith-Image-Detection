from PIL import Image, ImageGrab
from os import system



class detectScreen():

    def takeScreenshot(self):
        system('spectacle -bmno ./imgs/scr.png')
        return self.compressed_image(Image.open('./imgs/scr.png'))

    def showOnlyBrightest(self,img):
        w, h = img.size
        pixels=[]
        highest=0

        img = img.convert('RGB')
        newImg = Image.new('RGB',size=img.size)
        for x in range(w):
            for y in range(h):
                r,g,b = img.getpixel((x,y))
                #if within hue, within sat, within bright
                if g > 100 and r < 100 and b < 100:
                    newImg.putpixel((x,y), (255, 255,255))
                    #check nearby pixels


        #Mask through x axis    
        for y in range(h):
            oldPixel = None
            for x in range(w):
                if oldPixel != None:

                    if newImg.getpixel((x,y)) == (255,255,255):
                        if (x - oldPixel[0]) < 20:
                            for pixel in range(oldPixel[0], x):
                                if newImg.getpixel((pixel,y)) != (255,255,255):
                                    newImg.putpixel((pixel,y), (0,0,255))
                        oldPixel=(x,y)
                        
                        
                
                else:
                    if newImg.getpixel((x,y)) == (255,255,255):
                        oldPixel = (x,y)

        for x in range(w):
            oldPixel = None
            for y in range(h):
                if oldPixel != None:
                    
                    if newImg.getpixel((x,y)) in ((255,255,255), (0,0,255)):
                        if (y - oldPixel[1]) < 10:
                            for pixel in range(oldPixel[1], y):
                                if newImg.getpixel((x,pixel)) == (0,0,0):
                                    newImg.putpixel((x,pixel), (255,0,0))
                        oldPixel=(x,y)
                        
                        
                
                else:
                    if newImg.getpixel((x,y)) == (255,255,255):
                        oldPixel = (x,y)
            

        return newImg
                

    def compressed_image(self, image: Image) -> Image:
        w, h = image.size
        Image = image.resize((w, h))

        return Image

    def __init__(self, frame):

        self.threshold = 240
        img = self.takeScreenshot()
        
        img=self.showOnlyBrightest(img)
        with open('./imgs/'+str(frame)+'.jpg', 'w') as f:
            img.save(f)

frame=0
while True:
    frame+=1
    detectScreen(frame)
    print('Frame Captured: ', frame)