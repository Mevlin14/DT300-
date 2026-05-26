import tkinter as tk

Max_STOCK = 50

#Album class 
class Album:
    def __init__(self,title,artist,stock):
        self.title = title
        self.artist = artist
        self.stock = stock
        self.sold = 0
        
#function to sell one album 
    def sell_album(self):
        if self.stock > 0 :
            self.stock -= 1
            self.sold += 1
            return True
        return False

#function to restock  album
    def restock_album(self,amount):
        if self.stock + amount <= MAX_STOCK:
            self.stock += amount
            return True
        return False

#main application class
    class InventoryApp:
     def __init__(self,root):
         self.root = root
         self.root.title("Record store Inventory")
         self.root.geometry("500*500")

#Dictionary storing album objects
         self.albums={"Thriller":Album("Thriller","Michael Jackson",15),
                      "Rumours":Album("Rumours", "Fleetwood Mac",20),
                      "Born to run": Album("born to Run","Bruce springsteens",10)
                      }
         #Variable for selected album
         self.selected_album = tk.StringVar()
         self.selected_album.set("Thriller")

         #Title label
         title_label = tk.Label(
             root,text="Record Store Inventory System",
             font=("Arial",16))

         title_label.pack(pady=10)

         #Dropdown menu
         album_menu = tk.OptionMenu(
             root, self.selected_album,
             *self.albums.keys()
             )
         album_menu.pack(pady=5)


         #sell button
         sell_button = tk.Button(
             root,
             text = "Sell Album",
             command=self.sell_album
             )
         sell_button.pack(pady=5)

         #restock label
         restock_label = tk.Label(
             root,
             text="Enter amount to restock:"
             )

         restock_label.pack(pady=5)

         

         #Restock entry box
         self.restock_entry = tk.Entry(root)
         
         self.restock_entry.pack(pady=5)

         
         #Restock button
         restock_button = tk.button(
             root,
             text="Restock Album",
             command=self.restock_album
             )
         restock_button.pack(pady=5)

         #inventory display label
         self.inventory_label = tk.Label(
             root,
             text="",
             jusitfy="left",
             fornt=("Arisl",12)
             )
         self.inventory_label.pack(pady=5)
        

        #update inventory display
        self.update_inventory_dispaly()

        #function to update inventory display
        def update_inventory_display(self):
            display_text = "Current Inventory:\n\n"

            for album in self.album.values():
                display_text +=(
                    f"{ablum_title}by{album.artist}\n"
                    f"Stock:{album.stock}\n"
                    f"Album Sold:{album.sold}\n\n"
                    )
                self.inventory_label.config(text=display_text)

                #function too sell album
                def sell_album(self):
                    album=self.albums[self.selected_album.get()]

                    if album = self_album():
                        messagebox.showinfo(
                            "Success",
                            "Album sold successfully".
                            )
                        else:
                            messagebox.showerror(
                                "Error",
                                "Album is out of stock".
                                )

                            self.update_inventory_display()

                            #function to restock album
                            def restock_album(self):
                                album=self.albums[self.selected_album.get()]

                                try:
                                    amount=int(self.restock_entry.get())

                                    #validation
                                    if amount<=0:
                                        messagebox.showerror(
                                            "Error",
                                            "Please enter a positive number".
                                            )
                                        return

                                    #restock if under limit
                                    if album.restock_album(amount):
                                        messagebox,showinfo(
                                            "success",
                                            "Album restocked successfully".
                                            )
                                        else:
                                            messagebox.showerror(
                                                "Error",
                                                f"Cannot exceed maximum stock limit of {MAX_STOCK}."
                                                )
                                            except ValueError:
                                                messagebox.showerror(
                                                    "Error",
                                                    "Please enter a valid number."
                                                    )

                                                #update display and clear entry box
                                                self.update_inventory_display()
                                                self.restock_entry.delete(0.tk.END)
                                            

                                    
                            
        






#start program    
root = tk.Tk()
root.title("Record store Inventory")
root.geometry("500*400")

root.mainloop()

