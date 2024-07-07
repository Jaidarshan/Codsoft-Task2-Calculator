# Task 2: Calculator
import tkinter as tk
def button_click(item):
    global expression
    expression+=str(item)
    input_text.set(expression)
def clear_display():
    global expression
    expression=""
    input_text.set("")
def delete_last():
    global expression
    expression=expression[:-1]
    input_text.set(expression)
def evaluate():
    global expression
    try:
        result=str(eval(expression))
        input_text.set(result)
        expression=result
    except:
        input_text.set("Error")
        expression=""
window=tk.Tk()
window.title("Calculator")
window.geometry("320x385")  
expression=""
heading=tk.Label(window,text="Calculator",font=("Helvetica",20,"bold"))
heading.pack(pady=10)
input_text=tk.StringVar()
input_frame=tk.Frame(window,width=312,height=50,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
input_frame.pack(side=tk.TOP)
input_frame.pack_propagate(0)
input_field=tk.Entry(input_frame,font=('arial',18,'bold'),textvariable=input_text,width=50,bg="#eee",bd=0,justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
btns_frame=tk.Frame(window, width=312,height=272.5,bg="grey")
btns_frame.pack()
clear_btn=tk.Button(btns_frame,text="C",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=clear_display).grid(row=0,column=0,padx=1,pady=1)
delete_btn=tk.Button(btns_frame,text="DEL",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=delete_last).grid(row=0,column=1,padx=1,pady=1)
divide=tk.Button(btns_frame,text="/",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click("/")).grid(row=0,column=2,padx=1,pady=1)
multiply=tk.Button(btns_frame,text="*",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click("*")).grid(row=0,column=3,padx=1,pady=1)
seven=tk.Button(btns_frame,text="7",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(7)).grid(row=1,column=0,padx=1,pady=1)
eight=tk.Button(btns_frame,text="8",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(8)).grid(row=1,column=1,padx=1,pady=1)
nine=tk.Button(btns_frame,text="9",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(9)).grid(row=1, column=2,padx=1,pady=1)
subtract=tk.Button(btns_frame,text="-",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click("-")).grid(row=1,column=3,padx=1,pady=1)
four=tk.Button(btns_frame,text="4",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(4)).grid(row=2,column=0,padx=1,pady=1)
five=tk.Button(btns_frame,text="5",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(5)).grid(row=2,column=1,padx=1,pady=1)
six=tk.Button(btns_frame,text="6",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(6)).grid(row=2,column=2,padx=1,pady=1)
add=tk.Button(btns_frame,text="+",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click("+")).grid(row=2,column=3,padx=1,pady=1)
one=tk.Button(btns_frame,text="1",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(1)).grid(row=3,column=0,padx=1, pady=1)
two = tk.Button(btns_frame,text="2",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(2)).grid(row=3,column=1,padx=1,pady=1)
three=tk.Button(btns_frame,text="3",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(3)).grid(row=3,column=2,padx=1,pady=1)
point=tk.Button(btns_frame,text=".",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(".")).grid(row=3,column=3,padx=1,pady=1)
zero=tk.Button(btns_frame,text="0",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(0)).grid(row=4,column=1,padx=1,pady=1)
double_zero=tk.Button(btns_frame,text="00",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click("00")).grid(row=4,column=0,padx=1,pady=1)
equals = tk.Button(btns_frame,text="=",fg="black",width=21,height=3,bd=0,bg="#fff",cursor="hand2",command=evaluate).grid(row=4,column=2,columnspan=2,padx=1,pady=1)
window.mainloop()
