import tkinter as tk

#constant
BGCOLOR = "#020f12"
CYAN = "#05d7ff"
LIGHTCYAN= "#65e7ff"
BLACK = "BLACK"
WHITE ="WHITE"



# WINDOW :
window = tk.Tk()
window.title("ADPS PARKING")
window.geometry("1920x1080")
#window.resizable(False,False)
window.configure(background=BGCOLOR)


#ICON :
#icon_image=tk.PhotoImage(file="")
#window.iconphoto(False,icon_image)



# MAIN PAGE :
def main_page():


#---------------------------------------------------------------------------------------------------------------------------------------
# ENTRY PAGE CODE STARTS FROM HERE :
#----------------------------------------------------------------------------------------------------------------------------------------
    #Page after clicking the entry button :
    def entry_page():
        
        page_title.destroy()
        page_subtitle.destroy()
        page_msg.destroy()
        entry_button.destroy()
        exit_button.destroy()


        entrypage_title=tk.Label(window, 
                          bg=CYAN, 
                          fg=BLACK, 
                          text="ENTRY PROCESS :",
                          font=('georgia',90, "bold")
                          )
        entrypage_title.pack(padx=0, pady=45)
        
        entrypage_msg = tk.Label(window, 
                        background=BGCOLOR,
                        foreground=LIGHTCYAN,
                        text = "Enter the Following Details : ",
                        font=('georgia',35)
                        )
        entrypage_msg.place(x=450,y=255)

        mobileno_title = tk.Label(window, 
                        background=BGCOLOR,
                        foreground=WHITE,
                        text = "Mobile number : ",
                        font=('georgia',25)
                        )
        mobileno_title.place(x=200,y=350)      

        vehicleno_title = tk.Label(window, 
                        background=BGCOLOR,
                        foreground=WHITE,
                        text = "Vehicle number : ",
                        font=('georgia',25)
                        )
        vehicleno_title.place(x=200,y=545)


        #DATA ENTRY FOR ENTRY :

        mobile_number=tk.StringVar()
        vehicle_number=tk.StringVar()

        mobile_number_entry = tk.Entry(window,
                                           textvariable=mobile_number,
                                           width=21,
                                           border=2,
                                           font=("arial",40)
                                           )
        mobile_number_entry.place(x=300,y=425,height=60)

        vehicle_number_entry = tk.Entry(window,
                                           textvariable=vehicle_number,
                                           width=21,
                                           border=2,
                                           font=("arial",40)
                                           )
        vehicle_number_entry.place(x=300,y=620,height=60)



#ENTRY END PAGE :
        def entry_end():
            
            entrypage_title.destroy()
            entrypage_msg.destroy()
            submit_button.destroy()
            clear_button.destroy()
            back_button.destroy()
            mobileno_title.destroy()
            vehicleno_title.destroy()
            mobile_number_entry.destroy()
            vehicle_number_entry.destroy()

            entryend_title=tk.Label(window, 
                          bg=CYAN, 
                          fg=BLACK, 
                          text="COMPLETED ✔️",
                          font=('georgia',90, "bold")
                          )
            entryend_title.place(x=280,y=45)

            entryend_msg=tk.Label(window,
                                  background=BGCOLOR,
                                  foreground=WHITE,
                                  text='''
Your entry process is completed successfully, And your receipt has 
been sent to your moblie number. You can complete the payment process
at the exit gate .

Thankyou Have a Nice Day !'''     ,
                                  font=('georgia',27)
                                  )
            entryend_msg.place(x=180,y=230)

            entryend_otp=tk.Label(window,
                                  background=BGCOLOR,
                                  foreground=WHITE,
                                  text=("Your Generated otp is :"+str(123234)),
                                  font=('georgia',35)
                                  )
            entryend_otp.place(x=440,y=530)

            def confirm():
                confirm_button.destroy()
                entryend_title.destroy()
                entryend_msg.destroy()
                entryend_otp.destroy()
                main_page()

            confirm_button=tk.Button(window, 
                        background=CYAN,
                        foreground=BLACK,
                        activebackground=LIGHTCYAN,
                        activeforeground=BLACK,
                        highlightthickness=2,
                        highlightbackground=CYAN,
                        highlightcolor=WHITE,
                        width=9,
                        height=1,
                        border=0,
                        cursor='hand1',
                        text="CONFIRM",
                        font=('arial',40,'bold'),
                        command=confirm
                        )
            confirm_button.place(x=620,y=650)


# BUTTONS FOR ENTRY PAGE STARTS HERE :
            
        submit_button=tk.Button(window, 
                        background=CYAN,
                        foreground=BLACK,
                        activebackground=LIGHTCYAN,
                        activeforeground=BLACK,
                        highlightthickness=2,
                        highlightbackground=CYAN,
                        highlightcolor=WHITE,
                        width=8,
                        height=1,
                        border=0,
                        cursor='hand1',
                        text="SUBMIT",
                        font=('arial',40,'bold'),
                        command=entry_end,
                        )
        submit_button.place(x=1150,y=350)

        def clear():
            mobile_number.set('')
            vehicle_number.set('')

        clear_button=tk.Button(window, 
                        background=CYAN,
                        foreground=BLACK,
                        activebackground=LIGHTCYAN,
                        activeforeground=BLACK,
                        highlightthickness=2,
                        highlightbackground=CYAN,
                        highlightcolor=WHITE,
                        width=8,
                        height=1,
                        border=0,
                        cursor='hand1',
                        text="CLEAR",
                        font=('arial',40,'bold'),
                        command=clear
                        )
        clear_button.place(x=1150,y=500)

        def back():
            entrypage_title.destroy()
            entrypage_msg.destroy()
            submit_button.destroy()
            clear_button.destroy()
            back_button.destroy()
            vehicleno_title.destroy()
            mobileno_title.destroy()
            vehicle_number_entry.destroy()
            mobile_number_entry.destroy()
            main_page()

        back_button=tk.Button(window, 
                        background=CYAN,
                        foreground=BLACK,
                        activebackground=LIGHTCYAN,
                        activeforeground=BLACK,
                        highlightthickness=2,
                        highlightbackground=CYAN,
                        highlightcolor=WHITE,
                        width=8,
                        height=1,
                        border=0,
                        cursor='hand1',
                        text="BACK",
                        font=('arial',40,'bold'),
                        command=back
                        )
        back_button.place(x=1150,y=650)

   
#---------------------------------------------------------------------------------------------------------------------------------------
# EXIT PAGE CODE STARTS FROM HERE :
#----------------------------------------------------------------------------------------------------------------------------------------       

    def exit_page():
        
        #color_box.destroy()
        page_title.destroy()
        page_subtitle.destroy()
        page_msg.destroy()
        entry_button.destroy()
        exit_button.destroy()

        exitpage_title=tk.Label(window, 
                          bg=CYAN, 
                          fg=BLACK, 
                          text=" EXIT PROCESS :",
                          font=('georgia',90, "bold")
                          )
        exitpage_title.pack(padx=0, pady=45)
        
        exitpage_msg = tk.Label(window, 
                        background=BGCOLOR,
                        foreground=LIGHTCYAN,
                        text = "Enter the Following Details : ",
                        font=('georgia',35)
                        )
        exitpage_msg.place(x=450,y=255)

        otpno_title = tk.Label(window, 
                        background=BGCOLOR,
                        foreground=WHITE,
                        text = "OTP number : ",
                        font=('georgia',25)
                        )
        otpno_title.place(x=200,y=350)      

        vehicleno_title = tk.Label(window, 
                        background=BGCOLOR,
                        foreground=WHITE,
                        text = "Vehicle number : ",
                        font=('georgia',25)
                        )
        vehicleno_title.place(x=200,y=545)




        #DATA ENTRY FOR EXIT  :

        otp_number=tk.StringVar()
        vehicle_number=tk.StringVar()

        otp_number_entry = tk.Entry(window,
                                           textvariable=otp_number,
                                           width=21,
                                           border=2,
                                           font=("arial",40)
                                           )
        otp_number_entry.place(x=300,y=425,height=60)

        vehicle_number_entry = tk.Entry(window,
                                           textvariable=vehicle_number,
                                           width=21,
                                           border=2,
                                           font=("arial",40)
                                           )
        vehicle_number_entry.place(x=300,y=620,height=60)

        
        def exit_end():
            
            exitpage_title.destroy()
            exitpage_msg.destroy()
            submit_button.destroy()
            clear_button.destroy()
            back_button.destroy()
            otpno_title.destroy()
            vehicleno_title.destroy()
            otp_number_entry.destroy()
            vehicle_number_entry.destroy()


            exitend_title=tk.Label(window, 
                          bg=CYAN, 
                          fg=BLACK, 
                          text="COMPLETED ✔️",
                          font=('georgia',90, "bold")
                          )
            exitend_title.place(x=280,y=45)

            exitend_msg=tk.Label(window,
                                  background=BGCOLOR,
                                  foreground=WHITE,
                                  text='''
Your exit process is completed successfully. Please press the below
confirm button after completing all the process to close this tab.

Thanks for comming and visit again 🙏 !'''     ,
                                  font=('georgia',33)
                                  )
            exitend_msg.place(x=110,y=250)

            def confirm():
                confirm_button.destroy()
                exitend_title.destroy()
                exitend_msg.destroy()
                main_page()

            confirm_button=tk.Button(window, 
                        background=CYAN,
                        foreground=BLACK,
                        activebackground=LIGHTCYAN,
                        activeforeground=BLACK,
                        highlightthickness=2,
                        highlightbackground=CYAN,
                        highlightcolor=WHITE,
                        width=9,
                        height=1,
                        border=0,
                        cursor='hand1',
                        text="CONFIRM",
                        font=('arial',40,'bold'),
                        command=confirm
                        )
            confirm_button.place(x=620,y=650)

#--------------- BUTTONS FOR EXIT PAGE STARTS HERE :

        submit_button=tk.Button(window, 
                        background=CYAN,
                        foreground=BLACK,
                        activebackground=LIGHTCYAN,
                        activeforeground=BLACK,
                        highlightthickness=2,
                        highlightbackground=CYAN,
                        highlightcolor=WHITE,
                        width=8,
                        height=1,
                        border=0,
                        cursor='hand1',
                        text="SUBMIT",
                        font=('arial',40,'bold'),
                        command=exit_end,
                        )
        submit_button.place(x=1150,y=350)

        def clear():
            otp_number.set('')
            vehicle_number.set('')

        clear_button=tk.Button(window, 
                        background=CYAN,
                        foreground=BLACK,
                        activebackground=LIGHTCYAN,
                        activeforeground=BLACK,
                        highlightthickness=2,
                        highlightbackground=CYAN,
                        highlightcolor=WHITE,
                        width=8,
                        height=1,
                        border=0,
                        cursor='hand1',
                        text="CLEAR",
                        font=('arial',40,'bold'),
                        command=clear
                        )
        clear_button.place(x=1150,y=500)

        def back():
            exitpage_title.destroy()
            exitpage_msg.destroy()
            submit_button.destroy()
            clear_button.destroy()
            back_button.destroy()
            otpno_title.destroy()
            vehicleno_title.destroy()
            otp_number_entry.destroy()
            vehicle_number_entry.destroy()
            main_page()

        back_button=tk.Button(window, 
                        background=CYAN,
                        foreground=BLACK,
                        activebackground=LIGHTCYAN,
                        activeforeground=BLACK,
                        highlightthickness=2,
                        highlightbackground=CYAN,
                        highlightcolor=WHITE,
                        width=8,
                        height=1,
                        border=0,
                        cursor='hand1',
                        text="BACK",
                        font=('arial',40,'bold'),
                        command=back
                        )
        back_button.place(x=1150,y=650)




        def exit_end():
            pass
    
    
    
    
    color_box = tk.Frame(window, 
                        width=1920, 
                        height=220, 
                        background=CYAN,
                        )
    color_box.place(x=0,y=0)

    page_title = tk.Label(window, 
                          bg=CYAN, 
                          fg=BLACK, 
                          text="ADPS PARKING SYSTEM",
                          font=('georgia', 80, "bold")
                          )
    page_title.place(x=60, y=50)

    page_subtitle = tk.Label(window, 
                        background=BGCOLOR,
                        foreground=LIGHTCYAN,
                        text = "Please select the operation : ",
                        font=('georgia',40)
                        )
    page_subtitle.place(x=435,y=250)

    page_msg = tk.Label(window,
                        background=BGCOLOR,
                        foreground=WHITE,
                        text='''
                        ENTRY - For entering the parking.

                        EXIT - For exiting the parking.''',
                        font=('georgia',30)
                        )
    page_msg.place(x=210,y=330)

# BUTTONS FOR MAIN PAGE :
    entry_button=tk.Button(window, 
                        background=CYAN,
                        foreground=BLACK,
                        activebackground=LIGHTCYAN,
                        activeforeground=BLACK,
                        highlightthickness=2,
                        highlightbackground=CYAN,
                        highlightcolor=WHITE,
                        width=8,
                        height=1,
                        border=0,
                        cursor='hand1',
                        text="ENTRY",
                        font=('arial',50,'bold'),
                        command=entry_page,
                        )
    entry_button.place(x=235,y=600)

    exit_button=tk.Button(window, 
                        background=CYAN,
                        foreground=BLACK,
                        activebackground=LIGHTCYAN,
                        activeforeground=BLACK,
                        highlightthickness=2,
                        highlightbackground=CYAN,
                        highlightcolor=WHITE,
                        width=8,
                        height=1,
                        border=0,
                        cursor='hand1',
                        text=" EXIT ",
                        font=('arial',50,'bold'),
                        command=exit_page
                        )
    exit_button.place(x=955,y=600)



main_page()
window.mainloop()