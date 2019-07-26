from tkinter import *
import tkinter.filedialog as tkfd
import os

# import dummy_module


class sap_gui(Frame):
    
    ''' "Simple As Possible GUI", see references below. '''

    def __init__(self,master=None, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)
        Frame.configure(self, background="gray80")
        self.grid(column=0, row=0, sticky=(N, S, E, W))
        self.grid_propagate(0)

        # CREATE WIDGETS
        
        # label
        lbl0 = Label(self, text="Path to input file:", bg = "gray80")
        lbl0.grid(column=2, row=1, columnspan=1,sticky=(W))
        
        # file system browse button
        file_brows_button = Button(self, text="INPUT FILE", command=self.browse_file, width=12, highlightbackground="gray72")
        file_brows_button.grid(column=1, row=2, sticky=(W), padx=10)
        
        # fit button
        fit_button = Button(self, text="FIT", command=self.retrieve_n_fit, width=12, highlightbackground="gray72")
        fit_button.grid(column=1, row=3, sticky=(W), padx=10)
        
        # file path entry widget
        self.e1 = Entry(self,width=30)
        self.e1.grid(column=2, row=2, sticky=(W))
        
        # label
        lbl1 = Label(self, text="x1       x2       x3       x4      x5       x6", bg = "gray80")
        lbl1.grid(column=2, row=3, columnspan=1, sticky=(W))
        
        # label
        lbl2 = Label(self, text="GUESS:", bg = "gray80")
        lbl2.grid(column=1, row=4, columnspan=1, padx=10)
    
        # input guess
        self.e2 = Entry(self,width=30)
        self.e2.grid(column=2, row=4, sticky=(W))
     
        # label
        lbl3 = Label(self, text="RESULT:", bg = "gray80")
        lbl3.grid(column=1, row=5, columnspan=1, padx=10)
        
        # input guess
        self.e3 = Entry(self, width=30)
        self.e3.grid(column=2, row=5)
    
        # logo
        #image = Image.open("../logo/mongo_logo_tinyer.gif")
        #photo = ImageTk.PhotoImage(image)
        #lbl4 = Label(self, image=photo)
        #lbl4.image = photo
        #lbl4.grid(column=3, row=2, rowspan=5, sticky=(E), padx=10, pady=0)

       
    # MEMBER FUNCTIONS:
    
    def browse_file(self):
        
        """ A member function that puts file path in entry widget e1"""
        
        fname = tkfd.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*")))
        self.e1.insert(0,fname)


    def retrieve_n_fit(self):
        
        """ A member function that retrievs path to input file and starting guess values"""
        
        input_path = str(self.e1.get())
        input_arg_string = str(self.e2.get())
        input_arg_list = input_arg_string.split()
        
        # Some primitive suboptimal error checking
        
        # check input path
        if os.path.isfile(input_path) == False:
            self.pop_up_window("Problem reading input file")
        
        
        # Check number of input arguments and do type check:
        
        if len(input_arg_list) != 6:
            self.pop_up_window("Problem input arguments\nno. of args")
        
        
        # convert from py str to float:
        
        try:
            x1 = float(input_arg_list[0])
            x2 = float(input_arg_list[1])
            x3 = float(input_arg_list[2])
            x4 = float(input_arg_list[3])
            x5 = float(input_arg_list[4])
            x6 = float(input_arg_list[5])
        
        except ValueError:
            self.pop_up_window("Problem input arguments\nconversion to float")
    
        '''
        optimized_params = dummy_module.optimize_param_func(x1, x2, x3, x4, x5, x6, x7)
        
        out_string = str(round(optimized_params[0],1))+" "+str(round(optimized_params[1],1))+" "+str(round(optimized_params[2],0))+" "+str(round(optimized_params[3],4))+" "+str(round(optimized_params[4],0))

        self.e3.insert(0,string=out_string)
        '''


    def pop_up_window(self, msg):
        
        """ A member function to create popup window with error messages"""
        
        t= Toplevel(self,bg="gray80")
        t.wm_title("ERROR!")
        t.geometry("175x75+150+150")
        lbl_in_popup = Label(t, text=msg, bg="gray80")
        lbl_in_popup.grid(row=2,column=2,sticky=(W))



root = Tk()
root.wm_title("sap_gui 1.0")
main_window = sap_gui(root,width=450,height=150)

if __name__ == "__main__":
    main_window.mainloop()



'''
REFERENCES:
-------------------------------------------------------------------------
The code is very much based on the folowing stackoverflow and blog posts:
https://softwareengineering.stackexchange.com/questions/213935/why-use-classes-when-programming-a-tkinter-gui-in-python
https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
https://stackoverflow.com/questions/7300072/inheriting-from-frame-or-not-in-a-tkinter-application
https://medium.com/@uditvashisht/how-to-create-a-macos-compatible-pop-up-window-in-tkinter-the-right-way-704053e34871
http://effbot.org/tkinterbook/wm.html
Especially the explainations by Bryan Oakly are very useful.
'''
