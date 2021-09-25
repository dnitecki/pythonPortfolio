from tkinter import *
import numpy.lib.financial as np

def NPV(R,CASHFLOWS):
    return np.npv(R,CASHFLOWS)

def IRR(CASHFLOWS):
    return np.irr(CASHFLOWS)

def N(IPER,PV,PMT,FV):
    return np.nper(IPER,PMT,PV,FV,0)

def R(NPER,PV,PMT,FV):
    return np.rate(NPER,PMT,PV,FV,0)

def PV(NPER,IPER,PMT,FV):
    return np.pv(IPER,NPER,PMT,FV,0)

def PMT(NPER,IPER,PV,FV):
    return np.pmt(IPER,NPER,PV,FV,0)

def FV(NPER,IPER,PV,PMT):
    return np.fv(IPER,NPER,PMT,PV,0)

def btnBack():
    global operator
    text_Input.set(operator[0:-1])

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=''
    text_Input.set('')
     
def btnEqualsInput():
    try:
        global operator
        sumup=str(eval(operator))
        text_Input.set(sumup)
        operator=''

    except: 
        text_Input.set(" ERROR ") 
        operator='' 
    
cal = Tk()

cal.title('UK MSF Financial Calculator')

operator=''
text_Input=StringVar()

textDisplay = Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,width=36,
                    bg='light blue',justify='right',relief=RIDGE, cursor="none").grid(columnspan=5)

nn=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='N',command=lambda:btnClick('N')).grid(row=1,column=0)
rr=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='R',command=lambda:btnClick('R')).grid(row=1,column=1)
btpv=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='PV',command=lambda:btnClick('PV')).grid(row=1,column=2)
btpm=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='PMT',command=lambda:btnClick('PMT')).grid(row=1,column=3)
btfv=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='FV',command=lambda:btnClick('FV')).grid(row=1,column=4)

btn1=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='1',command=lambda:btnClick(1)).grid(row=2,column=0)
btn2=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='2',command=lambda:btnClick(2)).grid(row=2,column=1)
btn3=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='3',command=lambda:btnClick(3)).grid(row=2,column=2)
btn4=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='4',command=lambda:btnClick(4)).grid(row=2,column=3)
btn5=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='5',command=lambda:btnClick(5)).grid(row=2,column=4)

btn6=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='6',command=lambda:btnClick(6)).grid(row=3,column=0)
btn7=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='7',command=lambda:btnClick(7)).grid(row=3,column=1)
btn8=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='8',command=lambda:btnClick(8)).grid(row=3,column=2)
btn9=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='9',command=lambda:btnClick(9)).grid(row=3,column=3)
btn0=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='0',command=lambda:btnClick(0)).grid(row=3,column=4)

btnp=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='+',command=lambda:btnClick('+')).grid(row=4,column=0)
btnm=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='-',command=lambda:btnClick('-')).grid(row=4,column=1)
btnt=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='*',command=lambda:btnClick('*')).grid(row=4,column=2)
btnd=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='/',command=lambda:btnClick('/')).grid(row=4,column=3)
btno=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='.',command=lambda:btnClick('.')).grid(row=4,column=4)

pp=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='(',command=lambda:btnClick('(')).grid(row=5,column=0)
pq=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text=')',command=lambda:btnClick(')')).grid(row=5,column=1)
bpp=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='[',command=lambda:btnClick('[')).grid(row=5,column=2)
bpq=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text=']',command=lambda:btnClick(']')).grid(row=5,column=3)
ce=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text=',',command=lambda:btnClick(',')).grid(row=5,column=4)

BTNPV=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='NPV',command=lambda:btnClick('NPV')).grid(row=6,column=0)
BTIRR=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='IRR',command=lambda:btnClick('IRR')).grid(row=6,column=1)
BTCE=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='Undo',command=btnBack).grid(row=6,column=2)
cc=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='Clear',command=btnClearDisplay).grid(row=6,column=3)
eq=Button(cal,padx=16,bd=8,fg='black',font=('arial',20,'bold'),width=6,text='=',command=btnEqualsInput).grid(row=6,column=4)

cal.mainloop()

