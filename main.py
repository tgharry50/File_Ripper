import subprocess
import sys
import os
import glob
import customtkinter
from tkinter import filedialog
import shutil as sh


## Dodać kopiowanie z zamienianiem
## Kopiowanie zwykłe < zrobione
## Kopiowanie z atrybutem hidden
## Test a
class App( customtkinter.CTk ) :
    def __init__(self) :
        super().__init__()
        self.resizable( width = False, height = False )
        self.geometry( "200x200" )
        self.grid_columnconfigure( 0, weight = 1 )
        ## Edycja
        self.button=customtkinter.CTkButton( self, text = "Edytuj liste rozszerzeń", command = self.Edycja,
                                             fg_color = "green" )
        self.button.grid( row = 0, column = 0, padx = 5, pady = 2 )
        ## Ripper
        self.button_1=customtkinter.CTkButton( self, text = "Wyszukaj Pliki", command = self.Ripper, fg_color = "blue" )
        self.button_1.grid( row = 1, column = 0, padx = 5, pady = 2 )

    ## Needs
    edit_file="./Hit_List"
    save = "./Saved"
    if not os.path.exists( edit_file ):
        os.makedirs( edit_file )
        target=os.path.join( edit_file, "Hit_List.txt" )
        File=open( target, "w" )
        File.write( ".jpg\n.png\n.txt" )
        File.close()
    if not os.path.exists(save):
        os.makedirs(save)
    def Edycja(self) :
        subprocess.Popen( ["notepad", "./Hit_List/Hit_List.txt"] )

    def Ripper(self) :
        test=filedialog.askdirectory( title = "Wybierz lokacje" )
        with open( "./Hit_List/Hit_List.txt" ) as file :
            data=file.read()
            formats=data.split( "\n" )
        for dirpath, dnames, fnames in os.walk( test ) :
            for format in formats:
                for f in fnames :
                    if f.endswith( f"{format}" ) :
                        source_file_path=os.path.join( dirpath, f )
                        dest_file_path = os.path.join( "./Saved", f )
                        sh.copyfile( source_file_path, dest_file_path )

    def _quit(self) :
        self.quit()
        self.destroy()
        sys.exit()


app=App()
app.mainloop()
