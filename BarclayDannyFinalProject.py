from tkinter import *

root = Tk()
root.title('Dan\'s Music Shop')
root.geometry("450x675")
root.iconbitmap('stratocaster_guitar_love.ico')
root.configure(background='#efe4b0')

shpCart = []
prices = []
userInfo = []

#Business Logo

logo = PhotoImage(file="Dan's Music Shop Logo.png")
lblLogo = Label(image=logo, borderwidth=0, highlightthickness=0)
lblLogo.grid(row=0, column=0, columnspan=4)

# Divider between sections

divider = PhotoImage(file="Spacer image.png")
lblDivider = Label(image=divider, borderwidth=0, highlightthickness=0)
lblDivider.grid(row=9, column=1, columnspan=6)

# Miscellaneous Labels


lblSkip = Label(root, text=" ", bg="#efe4b0")
lblSkip2 = Label(root, text="", bg="#efe4b0")
lblSkip3 = Label(root, text="", bg="#efe4b0")
lblAdded = Label(root, text="Added!", bg="#efe4b0")

# Alert Labels
lblAlertEmpty = Label(root, text="Cart Empty.", fg="red", bg="#efe4b0")
lblAlert = Label(root, text="Place order here!")
lblAlert.grid(row=18, column=3)

# User Information

lblOrderForm = Label(root, text="Order Form ", bg="#efe4b0")
lblOrderForm.config(font=("Helvetica", 20))

lblFirstName = Label(root, text="First Name: ", bg="#efe4b0")
lblLastName = Label(root, text="Last Name: ", bg="#efe4b0")
lblAddress = Label(root, text="Street Address: ", bg="#efe4b0")
lblCity = Label(root, text="City: ", bg="#efe4b0")
lblZipCode = Label(root, text="Zipcode: ", bg="#efe4b0")
lblEmail = Label(root, text="Email: ", bg="#efe4b0")

# User item choices

lblItems = Label(root, text="What would you like to order?", bg="#efe4b0")
lblItems.config(font=("Helvetica", 15))
lblDrumSet = Label(root, text="Drumset: $1,100", bg="#efe4b0")
lblGuitar = Label(root, text="Guitar: $600", bg="#efe4b0")
lblBassGuitar = Label(root, text="Bass Guitar: $650", bg="#efe4b0")

# Optional add-ons

lblOptions = Label(root, text="Extra Add-Ons (+$5)", bg="#efe4b0")
lblStrings = Label(root, text="Strings", bg="#efe4b0")
lblDrumsticks = Label(root, text="Drum Sticks", bg="#efe4b0")
lblLessons = Label(root, text="1 mo. lessons ($160)", bg="#efe4b0")


# Entry Fields

txtFirstName = Entry(root, width=20, borderwidth=3, justify=LEFT)
txtLastName = Entry(root, width=20, borderwidth=3)
txtAddress = Entry(root, width=20, borderwidth=3)
txtCity = Entry(root, width=20, borderwidth=3)
txtZipCode = Entry(root, width=20, borderwidth=3)
txtEmail = Entry(root, width=20, borderwidth=3)


# Display Labels

lblOrderForm.grid(row=1, column=0, columnspan=6)
lblFirstName.grid(row=3, column=0)
lblLastName.grid(row=4, column=0)
lblAddress.grid(row=5, column=0)
lblCity.grid(row=6,column=0)
lblZipCode.grid(row=7, column=0)
lblEmail.grid(row=8, column=0)


#Display Entry Fields for User Information

txtFirstName.grid(row=3,column=1)
txtLastName.grid(row=4,column=1)
txtAddress.grid(row=5,column=1)
txtCity.grid(row=6,column=1)
txtZipCode.grid(row=7,column=1)
txtEmail.grid(row=8,column=1)

# Display Items to buy

lblItems.grid(row=10, column=0, columnspan=6)
lblSkip2.grid(row=11, column=0)
lblDrumSet.grid(row=12, column=0)
lblGuitar.grid(row=13, column=0)
lblBassGuitar.grid(row=14, column=0)

# Create the 'add to cart' buttons

btnDrumSet = Button(root, text="Add to Cart!", command= lambda: addDrums())
btnGuitar = Button(root, text="Add to Cart!", command = lambda: addGuitar())
btnBassGuitar = Button(root, text="Add to Cart!", command = lambda: addBass())

btnStrings = Button(root, text="Add to Cart!", command= lambda: addStrings())
btnDrumSticks = Button(root, text="Add to Cart!", command = lambda: addSticks())
btnLessons = Button(root, text="Add to Cart!", command= lambda: addLessons())

# display the 'add to cart' buttons

btnDrumSet.grid(row=12, column=1, pady=4)
btnGuitar.grid(row=13, column=1, pady=4)
btnBassGuitar.grid(row=14, column=1, pady=4)

btnStrings.grid(row=18,column=1, pady=4)
btnDrumSticks.grid(row=19,column=1, pady=4)
btnLessons.grid(row=20,column=1, pady=4)

# Display 'Add-ons' section labels

lblSkip2.grid(row=15, column=0)
lblOptions.grid(row=16, column=0, columnspan=2)
lblSkip.grid(row=17, column=0)
lblStrings.grid(row=18, column=0)
lblDrumsticks.grid(row=19, column=0)
lblLessons.grid(row=20, column=0)

# Submit and Clear Buttons

btnSubmit = Button(root, text="Submit Form!", command= lambda: formValidation())
btnClear = Button(root, text="Clear Form!    ", command= lambda: clearForm())

# Display Submit and Clear Buttons

btnSubmit.grid(row=19,column=3, pady=4)
btnClear.grid(row=20, column=3, pady=4)


# This function will clear all entered information, and also empty the cart and stored user information.  
def clearForm():
    txtFirstName.delete(0,END)
    txtLastName.delete(0,END)
    txtAddress.delete(0,END)
    txtCity.delete(0,END)
    txtZipCode.delete(0,END)
    txtEmail.delete(0,END)
    lblAdded.grid_forget()
    lblAlert.config(text="")

    
    #clear shopping cart and prices list
    
    shpCart.clear()
    prices.clear()
    

def formValidation():
    if len(shpCart) == 0: 
        lblAlert.config(text="No Items Added")
        if len(txtFirstName.get()) == 0:
            lblAlert.config(text="Please Enter First Name")
        if len(txtLastName.get()) == 0:
            lblAlert.config(text="Please Enter Last Name")
        if len(txtAddress.get()) == 0:
            lblAlert.config(text="Enter Valid Address")
        if len(txtCity.get()) == 0:
            lblAlert.config(text="Enter Valid City")    
        try:
            x = int(txtZipCode.get())
            pass
        except: 
            lblAlert.config(text="Incorrect Zipcode")
        if '@' in txtEmail.get() and '.com' in txtEmail.get():
            pass
        else:
            lblAlert.config(text="Email format: abc@abc.com")
    
    submitForm()
    
    
# User Info Functions 

   
# Add to Cart Functions

def addDrums():
    shpCart.append("Drumset")
    prices.append(1100)
    lblAdded.grid(row=12, column=2)
    
def addGuitar():
    shpCart.append("Guitar")
    prices.append(600)
    lblAdded.grid(row=13, column=2)

def addBass():
    shpCart.append("Bass Guitar")
    prices.append(650)
    lblAdded.grid(row=14, column=2)
    
def addStrings():
    shpCart.append("Strings")
    prices.append(5)
    lblAdded.grid(row=18, column=2)
    
def addSticks():
    shpCart.append("Drumsticks")
    prices.append(5)
    lblAdded.grid(row=19, column=2)    
    
def addLessons():
    shpCart.append("Lessons")
    prices.append(160)
    lblAdded.grid(row=20, column=2)
    
    

    
# SECOND WINDOW - This function is executed by the function that validates the user's information. 

def submitForm():
    if len(shpCart) > 0:
        

        global logo2
        global divider2
        
        # formatting second window
        top = Toplevel()
        top.title('Dan\'s Music Shop')
        top.geometry("430x650")
        top.iconbitmap('stratocaster_guitar_love2.ico')
        top.configure(background='#efe4b0')
        
        logo2 = PhotoImage(master=top, file="Dan's Music Shop Logo2.png")
        lblLogo2 = Label(top, image=logo2, borderwidth=0, highlightthickness=0)
        lblLogo2.grid(row=0, column=0, columnspan=4)
        
        divider2 = PhotoImage(master=top, file="Spacer image2.png")
        lblDivider2 = Label(top, image=divider2, borderwidth=0, highlightthickness=0)
        lblDivider2.grid(row=9, column=2, columnspan=3)

        #This will display user information entered from before
        
        lblBillingInfo = Label(top, text="Billing Information", bg="#efe4b0")
        lblBillingInfo.config(font=("Helvetica", 20))
        lblBillingInfo.grid(row=1, column=0, columnspan=4)
        
        lblShoppingCart = Label(top, text="Shopping Cart ", bg="#efe4b0")
        lblShoppingCart.config(font=("Helvetica", 20))
        lblShoppingCart.grid(row=10, column=1, columnspan=4)
        
        lblName = Label(top, text="Name:", bg="#efe4b0")
        lblName.grid(row=2, column=2)
        lblNameData = Label(top, text=(txtFirstName.get() + " " + txtLastName.get()), bg="#efe4b0")
        lblNameData.grid(row=2, column=3)
       
        lblAddressSecond = Label(top, text="Address:", bg="#efe4b0")
        lblAddressSecond.grid(row=3, column=2)
        lblAddressData = Label(top, text=(txtAddress.get()), bg="#efe4b0")
        lblAddressData.grid(row=3, column=3)
        
        lblCitySecond = Label(top, text="City:", bg="#efe4b0")
        lblCitySecond.grid(row=4, column=2)
        lblCityData = Label(top, text=(txtCity.get()), bg="#efe4b0")
        lblCityData.grid(row=4, column=3)
        
        lblZipCodeSecond = Label(top, text="Zipcode:", bg="#efe4b0")
        lblZipCodeSecond.grid(row=5, column=2)
        lblZipCodeData = Label(top, text=(txtZipCode.get()), bg="#efe4b0")
        lblZipCodeData.grid(row=5, column=3)
        
        lblEmailSecond = Label(top, text="Email:", bg="#efe4b0")
        lblEmailSecond.grid(row=6, column=2)
        lblEmailData = Label(top, text=(txtEmail.get()), bg="#efe4b0")
        lblEmailData.grid(row=6, column=3)
        
        # Exit and Place Order Buttons
        
        btnPlaceOrder = Button(top, text="Place Order", command= lambda: placeOrder())
        btnPlaceOrder.grid(row=21, column=3, pady=4)
        btnCancelOrder = Button(top, text="Exit", command= lambda: closeProgram())
        btnCancelOrder.grid(row=22, column=3, pady=4) 
        
        # Display Cart
    
        def displayCart():
            global totalPrice
            global tax
               
            if len(shpCart) == 1:
                lblItem1 = Label(top, text=shpCart[0], bg="#efe4b0")
                lblItem1.grid(row=11, column=2)
                lblPrice1 = Label(top, text="$"+str(prices[0]), bg="#efe4b0")
                lblPrice1.grid(row=11, column=3)
                
                totalPrice = prices[0]
                
            elif len(shpCart) == 2:
                lblItem1 = Label(top, text=shpCart[0], bg="#efe4b0")
                lblItem1.grid(row=11, column=2)
                lblPrice1 = Label(top, text="$"+str(prices[0]), bg="#efe4b0")
                lblPrice1.grid(row=11, column=3)
                
                lblItem2 = Label(top, text=shpCart[1], bg="#efe4b0")
                lblItem2.grid(row=12, column=2)
                lblPrice2 = Label(top, text="$"+str(prices[1]), bg="#efe4b0")
                lblPrice2.grid(row=12, column=3)
                
                totalPrice = (prices[0] + prices[1])
                
            elif len(shpCart) == 3:
                lblItem1 = Label(top, text=shpCart[0], bg="#efe4b0")
                lblItem1.grid(row=11, column=2)
                lblPrice1 = Label(top, text="$"+str(prices[0]), bg="#efe4b0")
                lblPrice1.grid(row=11, column=3)
                
                lblItem2 = Label(top, text=shpCart[1], bg="#efe4b0")
                lblItem2.grid(row=12, column=2)
                lblPrice2 = Label(top, text="$"+str(prices[1]), bg="#efe4b0")
                lblPrice2.grid(row=12, column=3)
                
                lblItem3 = Label(top, text=shpCart[2], bg="#efe4b0")
                lblItem3.grid(row=13, column=2)
                lblPrice3 = Label(top, text="$"+str(prices[2]), bg="#efe4b0")
                lblPrice3.grid(row=13, column=3)
                
                totalPrice = (prices[0] + prices[1] + prices[2])
                
            elif len(shpCart) == 4:
                lblItem1 = Label(top, text=shpCart[0], bg="#efe4b0")
                lblItem1.grid(row=11, column=2)
                lblPrice1 = Label(top, text="$"+str(prices[0]), bg="#efe4b0")
                lblPrice1.grid(row=11, column=3)
                
                lblItem2 = Label(top, text=shpCart[1], bg="#efe4b0")
                lblItem2.grid(row=12, column=2)
                lblPrice2 = Label(top, text="$"+str(prices[1]), bg="#efe4b0")
                lblPrice2.grid(row=12, column=3)
                
                lblItem3 = Label(top, text=shpCart[2], bg="#efe4b0")
                lblItem3.grid(row=13, column=2)
                lblPrice3 = Label(top, text="$"+str(prices[2]), bg="#efe4b0")
                lblPrice3.grid(row=13, column=3)
                
                lblItem4 = Label(top, text=shpCart[3], bg="#efe4b0")
                lblItem4.grid(row=14, column=2)
                lblPrice4 = Label(top, text="$"+str(prices[3]), bg="#efe4b0")
                lblPrice4.grid(row=14, column=3)
                
                totalPrice = (prices[0] + prices[1] + prices[2] + prices[3])
                
            elif len(shpCart) == 5:
                lblItem1 = Label(top, text=shpCart[0], bg="#efe4b0")
                lblItem1.grid(row=11, column=2)
                lblPrice1 = Label(top, text="$"+str(prices[0]), bg="#efe4b0")
                lblPrice1.grid(row=11, column=3)
                
                lblItem2 = Label(top, text=shpCart[1], bg="#efe4b0")
                lblItem2.grid(row=12, column=2)
                lblPrice2 = Label(top, text="$"+str(prices[1]), bg="#efe4b0")
                lblPrice2.grid(row=12, column=3)
                
                lblItem3 = Label(top, text=shpCart[2], bg="#efe4b0")
                lblItem3.grid(row=13, column=2)
                lblPrice3 = Label(top, text="$"+str(prices[2]), bg="#efe4b0")
                lblPrice3.grid(row=13, column=3)
                
                lblItem4 = Label(top, text=shpCart[3], bg="#efe4b0")
                lblItem4.grid(row=14, column=2)
                lblPrice4 = Label(top, text="$"+str(prices[3]), bg="#efe4b0")
                lblPrice4.grid(row=14, column=3)
                
                lblItem5 = Label(top, text=shpCart[4], bg="#efe4b0")
                lblItem5.grid(row=15, column=2)
                lblPrice5 = Label(top, text="$"+str(prices[4]), bg="#efe4b0")
                lblPrice5.grid(row=15, column=3)
                
                totalPrice = (prices[0] + prices[1] + prices[2] + prices[3] + prices[4])
                
            elif len(shpCart) == 6:
                lblItem1 = Label(top, text=shpCart[0], bg="#efe4b0")
                lblItem1.grid(row=11, column=2)
                lblPrice1 = Label(top, text="$"+str(prices[0]), bg="#efe4b0")
                lblPrice1.grid(row=11, column=3)
                
                lblItem2 = Label(top, text=shpCart[1], bg="#efe4b0")
                lblItem2.grid(row=12, column=2)
                lblPrice2 = Label(top, text="$"+str(prices[1]), bg="#efe4b0")
                lblPrice2.grid(row=12, column=3)
                
                lblItem3 = Label(top, text=shpCart[2], bg="#efe4b0")
                lblItem3.grid(row=13, column=2)
                lblPrice3 = Label(top, text="$"+str(prices[2]), bg="#efe4b0")
                lblPrice3.grid(row=13, column=3)
                
                lblItem4 = Label(top, text=shpCart[3], bg="#efe4b0")
                lblItem4.grid(row=14, column=2)
                lblPrice4 = Label(top, text="$"+str(prices[3]), bg="#efe4b0")
                lblPrice4.grid(row=14, column=3)
                
                lblItem5 = Label(top, text=shpCart[4], bg="#efe4b0")
                lblItem5.grid(row=15, column=2)
                lblPrice5 = Label(top, text="$"+str(prices[4]), bg="#efe4b0")
                lblPrice5.grid(row=15, column=3)
                
                lblItem6 = Label(top, text=shpCart[5], bg="#efe4b0")
                lblItem6.grid(row=16, column=2)
                lblPrice6 = Label(top, text="$"+str(prices[5]), bg="#efe4b0")
                lblPrice6.grid(row=16, column=3)
                
                totalPrice = (prices[0] + prices[1] + prices[2] + prices[3] + prices[4] + prices[5])
            
            lblTotalNoTax = Label(top, text="Total Before Tax:", bg="#efe4b0")
            lblTotalNoTax.grid(row=17, column=2)
            lbltotalPriceNoTax = Label(top, text="$"+ str(totalPrice), bg="#efe4b0")
            lbltotalPriceNoTax.grid(row=17, column=3)
            
            lblTax = Label(top, text="Tax: ", fg="red", bg="#efe4b0")
            lblTax.grid(row=18, column=2)
            tax = round(totalPrice * .07, 2)
            lblTotalTax = Label(top, text="$" + str(tax), bg="#efe4b0")
            lblTotalTax.grid(row=18, column=3)
            lblTotalAfterTax = Label(top, text="Total After Tax", bg="#efe4b0")
            lblTotalAfterTax.grid(row=20, column=2)
            lblTotalPriceAfterTax = Label(top, text="$"+str(tax+totalPrice), bg="#efe4b0")
            lblTotalPriceAfterTax.grid(row=20, column=3) 
            
        # The displaycart function will be called.    
        displayCart()
    
# This function will 'submit' the order and make an "order placed, thank you" message appear.
    def placeOrder():
        lblOrderPlaced = Label(top, text="Order Placed!! Thank you!", fg="green", bg="#efe4b0")
        lblOrderPlaced.grid(row=22, column=1, columnspan=2)
        
# This function will exit the program.         
    def closeProgram():
        root.destroy()
       
# places cursor in first entry box    
txtFirstName.focus()  
  
# executes the program    
mainloop()
     