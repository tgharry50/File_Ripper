import sys
import os
import customtkinter
from tkinter import filedialog
import shutil as sh
import subprocess


## Dodać kopiowanie z zamienianiem < In progress
## Kopiowanie zwykłe < zrobione
## Kopiowanie z atrybutem hidden < Zrobione
## Test ab
class App( customtkinter.CTk ) :
    def __init__(self) :
        super().__init__()
        self.resizable( width = False, height = False )
        self.geometry( "300x300" )
        self.grid_columnconfigure( 0, weight = 1 )
        ## Edycja
        self.button=customtkinter.CTkButton( self, text = "Edytuj liste rozszerzeń", command = self.Edycja,
                                             fg_color = "green" )
        self.button.grid( row = 0, column = 0, padx = 5, pady = 2 )
        ## Ripper
        self.button_1=customtkinter.CTkButton( self, text = "Wyszukaj Pliki", command = self.Ripper,
                                               fg_color = "#16BCBF" )
        self.button_1.grid( row = 1, column = 0, padx = 5, pady = 2 )
        ## Blocking
        # self.check_var=customtkinter.StringVar( value = "off" )
        # self.checkbox = customtkinter.CTkCheckBox(self, command = self.checkbox_event, variable=self.check_var, onvalue="on", offvalue="off", text = "Włącz tryb hidden")
        # self.checkbox.grid(row = 2, column = 1, padx = 5, pady = 2)
        # ## Hidden_Ripper
        self.button_2=customtkinter.CTkButton( self, text = "Wyszukaj Pliki oraz Ukryj je",
                                               command = self.The_Hidden_Ripper, fg_color = "#16BCBF")
        self.button_2.grid( row = 2, column = 0, padx = 5, pady = 2 )
        # ## Change
        self.button_3=customtkinter.CTkButton( self, text = "Zmień Format", command = self.Change, fg_color = "#16BCBF" )
        self.button_3.grid( row = 3, column = 0, padx = 5, pady = 2 )
        ###Text box
        self.textbox=customtkinter.CTkEntry( master = self, width = 75, height = 3, fg_color = "white",
                                             text_color = "black", placeholder_text = "INPUT" )
        self.textbox.grid( row = 4, column = 0 )
        ##
        self.textbox2=customtkinter.CTkEntry( master = self, width = 75, height = 3, fg_color = "white",
                                              text_color = "black", placeholder_text = "OUTPUT" )
        self.textbox2.grid( row = 5, column = 0 )

    ## Needs
    edit_file="./Hit_List"
    save="./Saved"
    converted="./Convertion"

    if not os.path.exists( edit_file ) :
        os.makedirs( edit_file )
        target=os.path.join( edit_file, "Hit_List.txt" )
        File=open( target, "w" )
        File.write( ".jpg\n.png\n.txt" )
        File.close()
    if not os.path.exists( save ) :
        os.makedirs( save )
    if not os.path.exists( converted ) :
        os.makedirs( converted )

    # def checkbox_event( self ):
    #     print(self.check_var.get())
    #     if self.check_var.get():
    #         self.button_1.configure( state = "normal")
    #     else:
    #         self.button_1.configure( state = "disabled" )
    #     self.button_1.update()

    def Edycja(self) :
        subprocess.Popen( ["notepad", "./Hit_List/Hit_List.txt"] )

    def Ripper(self) :
        #
        for f in os.listdir( "./Saved" ) :
            os.remove( os.path.join( "./Saved", f ) )
        #
        test=filedialog.askdirectory( title = "Wybierz lokacje" )
        self.button.configure(state = "disabled")
        self.button_1.configure( fg_color = "yellow", state = "disabled" )
        self.button.update()
        self.button_1.update()
        with open( "./Hit_List/Hit_List.txt" ) as file :
            data=file.read()
            formats=data.split( "\n" )
        for dirpath, dnames, fnames in os.walk( test ) :
            for format in formats :
                for f in fnames :
                    if f.endswith( f"{format}" ) :
                        source_file_path=os.path.join( dirpath, f )
                        dest_file_path=os.path.join( "./Saved", f )
                        sh.copyfile( source_file_path, dest_file_path )
        self.button_1.configure( fg_color = "#16BCBF", state = "normal")
        self.button_1.update()
        self.button.configure(state = "disabled")
        self.button.update()
    def The_Hidden_Ripper(self) :
        test=filedialog.askdirectory( title = "Wybierz lokacje" )
        #
        for f in os.listdir( "./Saved" ) :
            os.remove( os.path.join( "./Saved", f ) )
        #

        self.button.configure( state = "disabled")
        self.button_2.configure( state = "disabled", fg_color = "yellow" )
        self.button_2.update()
        self.button.update()
        #
        with open( "./Hit_List/Hit_List.txt" ) as file :
            data=file.read()
            formats=data.split( "\n" )
        for dirpath, dnames, fnames in os.walk( test ) :
            for format in formats :
                for f in fnames :
                    if f.endswith( f"{format}" ) :
                        source_file_path=os.path.join( dirpath, f )
                        dest_file_path=os.path.join( "./Saved", f )
                        sh.copyfile( source_file_path, dest_file_path )
        for root, dirs, files in os.walk( os.path.abspath( "./Saved" ) ) :
            for file in files :
                item=(os.path.join( root, file ))
                subprocess.check_call( ["attrib", "+H", f"{item}"] )

        self.button.configure( state = "normal", fg_color = "green" )
        self.button_2.configure( state = "normal", fg_color = "#16BCBF" )
        self.button_2.update()
        self.button.update()

    def Change(self) :
        self.button_3.configure(fg_color = "yellow")
        self.button_3.update()
        input=(self.textbox.get()).rstrip()
        output=(self.textbox2.get()).rstrip()
        for root, dirs, files in os.walk( os.path.abspath( "./Convertion" ) ) :
            for file in files :
                if file.endswith(f".{input}"):
                    item = (os.path.join( root, file ))
                    a=os.path.splitext( file )[0] + f'.{output}'
                    new_item=os.path.join( root, a )
                    print( new_item )
                    os.rename(item, new_item)
        self.button_3.configure(fg_color = "#16BCBF")
        self.button_3.update()

def _quit(self) :
    self.quit()
    self.destroy()
    sys.exit()


app=App()
app.mainloop()
