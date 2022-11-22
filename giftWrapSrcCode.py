from tkinter import *
root = Tk()
root.title("Gift wrapping customisation")
root.config(bg="cornsilk")

#===============The shape selection dropdown menu========================================0

def shapeSelected():
    if shapeVariable.get() == 1:
        heightE.delete(0, 'end')
        heightE.config(state='normal')
        widthE.delete(0, 'end')
        widthE.config(state='disabled')
        lengthE.delete(0, 'end')
        lengthE.config(state='disabled')
        radiusE.delete(0, 'end')
        radiusE.config(state='disabled')
    elif shapeVariable.get() == 2:
        heightE.delete(0, 'end')
        heightE.config(state='normal')
        widthE.delete(0, 'end')
        widthE.config(state='normal')
        lengthE.delete(0, 'end')
        lengthE.config(state='normal')
        radiusE.delete(0, 'end')
        radiusE.config(state='disabled')
    elif shapeVariable.get() == 3:
        heightE.delete(0, 'end')
        heightE.config(state='normal')
        widthE.delete(0, 'end')
        widthE.config(state='disabled')
        lengthE.delete(0, 'end')
        lengthE.config(state='disabled')
        radiusE.delete(0, 'end')
        radiusE.config(state='normal')


shapeVariable = IntVar(root)
shapeVariable.set('Not yet defined')
shapeLabel = Label(root, text="Select a shape: ", bg='lightblue').grid(row=0, column=0)

cubeBtn = Radiobutton(root, text="  Cube    ", variable= shapeVariable, value=1, bg='thistle', command= shapeSelected).grid(column=1, row=0, sticky='w')
cuboidBtn = Radiobutton(root, text="Cuboid", variable= shapeVariable, value=2, bg='thistle', command= shapeSelected).grid(column=2, row=0, sticky='w')
cylinderBtn = Radiobutton(root, text="Cylinder", variable= shapeVariable, value=3, bg='thistle', command=shapeSelected).grid(column=1, row=1, sticky='nw')



#===================Dimensions entries=====================================================

Label(root, text="Height (cm)", bg='lightblue').grid(row=2, pady=10)
Label(root, text="Length (cm)", bg='lightblue').grid(row=3, pady=10)
Label(root, text="Width (cm)", bg='lightblue').grid(row=4, pady=10)
Label(root, text="Radius (cm)", bg='lightblue').grid(row=5, pady=10)

heightE = Entry(root, bg='greenyellow')
heightE.grid(row=2, column=1, columnspan=2)
heightE.config(state='disabled')

lengthE = Entry(root, bg='greenyellow')
lengthE.grid(row=3, column=1,columnspan=2)
lengthE.config(state='disabled')

widthE = Entry(root, bg='greenyellow')
widthE.grid(row=4, column=1,columnspan=2)
widthE.config(state='disabled')

radiusE = Entry(root, bg='greenyellow')
radiusE.grid(row=5, column=1,columnspan=2)
radiusE.config(state='disabled')
# E = entry

#======================Pattern selection menu==========================================

col = StringVar(root)
col.set = ('Purple')

global c
c = Canvas(root, width=270, height=180)
c.grid(column=3, row=2, rowspan=4, columnspan=2)
c.create_rectangle(0, 0, 270, 180, fill='white', outline='white')

def pattern1():
    c.create_rectangle(0, 0, 270, 180, fill='white', outline='white')
    # first row
    c.create_polygon(0, 30, 30, 0, 60, 0, 90, 30, 60, 60, 30, 60, 0, 30, fill=colourVariable.get(), outline="black")
    c.create_polygon(90, 30, 120, 0, 150, 0, 180, 30, 150, 60, 120, 60, fill=colourVariable.get(), outline="black")
    c.create_polygon(180, 30, 210, 0, 240, 0, 270, 30, 240, 60, 210, 60, fill=colourVariable.get(), outline="black")
    c.create_polygon(270, 30, 300, 0, 330, 0, 360, 30, 330, 60, 300, 60, fill=colourVariable.get(), outline="black")
    # #second row
    c.create_polygon(60, 60, 90, 60, 120, 90, 90, 120, 60, 120, 30, 90, fill=colourVariable.get(), outline="black")
    c.create_polygon(120, 90, 150, 60, 180, 60, 210, 90, 180, 120, 150, 120, fill=colourVariable.get(), outline="black")
    c.create_polygon(210, 90, 240, 60, 270, 60, 300, 90, 270, 120, 240, 120, fill=colourVariable.get(), outline="black")
    c.create_polygon(300, 90, 330, 60, 360, 60, 390, 90, 360, 120, 330, 120, fill=colourVariable.get(), outline="black")
    c.create_polygon(0, 60, 30 ,90, 0, 120,  fill=colourVariable.get(), outline="black")
    # #third row
    c.create_polygon(0, 150, 30, 120, 60, 120, 90, 150, 60, 180, 30, 180, fill=colourVariable.get(), outline="black")
    c.create_polygon(90, 150, 120, 120, 150, 120, 180, 150, 150, 180, 120, 180, fill=colourVariable.get(), outline="black")
    c.create_polygon(180, 150, 210, 120, 240, 120, 270, 150, 240, 180, 210, 180, fill=colourVariable.get(), outline="black")
    c.create_polygon(270, 150, 300, 120, 330, 30, 360, 150, 330, 120, 300, 180, fill=colourVariable.get(), outline="black")

def pattern2():
    c.create_rectangle(0, 0, 270, 180, fill='white', outline='white')

    c.create_polygon(0, 300, 150, 0, 300, 300, fill=colourVariable.get(), outline="black")
    c.create_polygon(30, 300, 150, 60, 270, 300, fill="white", outline="black")
    c.create_polygon(60, 300, 150, 120, 240, 300, fill=colourVariable.get(), outline="black")
    c.create_polygon(80, 300, 150, 160, 220, 300,  fill='white', outline="black")


patternPrice = float(0)
global PatternMenu

def patternSelected(self):
    global patternPrice
    if patternVariable.get() == ("""Pattern 1(0.4p / cm2)"""):
        patternPrice = 0.004
        pattern1()
        return patternPrice
    elif patternVariable.get() == ("""Pattern 2(0.75p / cm2)"""):
        patternPrice = 0.0075
        pattern2()
        return patternPrice


patternVariable = StringVar(root)
patternVariable.set("Select pattern")
PatternMenu = OptionMenu(root, patternVariable, """Pattern 1(0.4p / cm2)""", """Pattern 2(0.75p / cm2)""", command= patternSelected)
PatternMenu.config(font=('Helvetica', 12), bg='mediumseagreen')
PatternMenu.grid(column=3, row=0, pady=3, columnspan=2)

#==================Colour selection menu===================================================

def colourChosen(text):
    colourInFunction = colourVariable.get()
    for colourInFunction in colourList:
        col = text


colourList = [
"Purple",
"DarkSlateGray",
"DeepSkyBlue",
"LightSeaGreen",
"VioletRed",
"Gold"
]

colourVariable = StringVar(root)
colourVariable.set("Purple")
Colours = OptionMenu(root, colourVariable, *colourList, command=colourChosen and patternSelected)
Colours.config(font=('Helvetica', 12), bg='mediumseagreen')
Colours.grid(column=3, row=1, columnspan=2, pady=5, ipadx=10)

#====================================Bow Selection==============================================0

bowSelection = IntVar()
bowPrice = float(0)
def bowPriceAddition():
    global bowPrice
    if bowSelection.get() == 1:
        bowPrice = 1.50
    elif bowSelection.get() == 2:
        bowPrice = 0

Label(root, text="""Would you like a bow?
(£1.50)""", bg='lightblue').grid(row=6, column=3 ,pady=10, sticky='w')

Radiobutton(root, text="Yes", variable= bowSelection, value=1, bg='peachpuff').grid(row=6, column=3, sticky='e')
Radiobutton(root, text="No", variable= bowSelection, value=2, bg='peachpuff').grid(row=6, column=4, sticky='w')

##===========================================Gift tag entry===================================

giftTagText = IntVar()
tagVariable = float(0)

def tagInputActivation():
    global tagVariable
    if giftTagText.get() == 1:
        tagVariable = 0.50
        tagInput.config(state='normal')
    elif giftTagText.get() == 2:
        tagVariable = 0
        tagInput.delete(0, 'end')
        tagInput.config(state='disabled')


Label(root, text= """Do you want to add a gift tag?
(50p + 2p/character)""", bg='lightblue').grid(row=6, pady=10)
Radiobutton(root, text="Yes", variable=giftTagText, value=1, command=tagInputActivation, bg='peachpuff').grid(row=6, column=1)
Radiobutton(root, text="No", variable=giftTagText, value=2, command=tagInputActivation, bg='peachpuff').grid(row=6, column=2)

tag = Label(root, text="Enter text (optional): ", bg='lightblue')
tag.grid(column=0, row=7)
tagInput = Entry(root, bg='greenyellow')
tagInput.grid(column=1, row=7, columnspan=2)
tagInput.config(state='disabled')

#=================================================Surface area calculation====================
import math
surfaceA = 0

def calculator():
    global surfaceA
    if shapeVariable.get() == 1:
        try:
            float(heightE.get())
            h = int(heightE.get())
            surfaceA = ((12*h*h)+(42*h)+36)
            surfaceA = int(surfaceA)
            errorLabel.config(text='', bg='cornsilk')
            return surfaceA
        except ValueError:
            if heightE.get() == '':
                errorLabel.config(text="""PLease input dimensions""", bg='red')
            else: errorLabel.config(text="""Only enter whole numbers.
        (No letters or decimals)""", bg='red')
    elif shapeVariable.get() == 2:
        try:
            float(heightE.get())
            float(widthE.get())
            float(lengthE.get())
            h = int(heightE.get())
            w = int(widthE.get())
            l = int(lengthE.get())
            surfaceA = ((2*w)+(2*h)+6) * ((2*h)+l+6)
            surfaceA = int(surfaceA)
            errorLabel.config(text="", bg='cornsilk')
            return surfaceA
        except ValueError:
            errorLabel.config(text="""Only enter whole numbers.
            (No letters or decimals)""", bg='red')
    elif shapeVariable.get() == 3:
        try:
            float(heightE.get())
            float(radiusE.get())
            h = int(heightE.get())
            r = int(radiusE.get())
            surfaceA = ((2*r*(math.pi))+6) * ((2*r)+h+6)
            surfaceA = int(surfaceA)
            errorLabel.config(text='', bg='cornsilk')
            return surfaceA
        except ValueError:
            errorLabel.config(text="""Only enter whole numbers.
            (No letters or decimals)""", bg='red')

#this label is only usen when/if the user enters letters instead of numbers in the dimensions' fields
errorLabel = Label(root, text='', bg='cornsilk')
errorLabel.grid(column=3, row=9, sticky='w')

#===============================================Final price calculation==============================

def totalPrice():
    global surfaceA
    calculator()
    tagPrice = (((len(tagInput.get())*0.02)) + tagVariable)
    #check pattern selected if error
    bowPriceAddition()
    totalSum = ((patternPrice * surfaceA) + (tagPrice) + (bowPrice))
    priceLbl = Label(root, text="Your total price is: £{0}".format(round(totalSum,2)), bg='BLACK',fg='white', relief=RAISED).grid(column=3, row=7)

clickBtn = Button(root, text='Confirm!', command= totalPrice).grid(column=0, row=9, sticky='e', pady=20)
#cardLbl = Label(root, text='The card will read: ').grid(column=3, row=6)


root.mainloop()
