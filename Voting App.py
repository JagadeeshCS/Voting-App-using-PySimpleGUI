import PySimpleGUI as s
import matplotlib.pyplot as plt
import numpy as np

  
DMK   = 0
ADMK  = 0
MNM   = 0
NTK   = 0
BJP   = 0
NOTA  = 0


v = [123,456,789,111,222,333,444,555,666,777,888,999]     # List containing Voter Id 

m = len(v)


# Button designs

bw = {'size':(5,2), 'font':('Franklin Gothic Book', 22)}

bt = {'size':(7,2), 'font':('Franklin Gothic Book', 20), 'button_color':("white","black")}

bo = {'size':(8,2), 'font':('Franklin Gothic Book', 18), 'button_color':("white","black")}



s.theme("")



layout = [[s.Text("Enter Voter ID :",font='Courier 15'),s.Input()],

          [s.Button("Enter"),s.Text("   Checking your voter ID... \t\t\t",text_color='#54C571', background_color='black', font='Courier 14',key = 'out')],

          [s.Text("Voting Button :",font='Courier 14')],

          [s.Button( "Vote DMK",pad=(50,30),**bw,button_color =("red","white")) , s.Button( "Vote ADMK",pad=(30,30),**bw, button_color =("green","white")),

           s.Button( "Vote MNM",pad=(30,30),**bw,button_color =("blue","white"))],

          [s.Button( "Vote NTK",pad=(50,30),**bw,button_color =("Brown","white")),

           s.Button( "Vote BJP",pad=(30,30),**bw,button_color =("orange","white")),

           s.Button( "NOTA",pad=(30,30),**bw,button_color =("black","white"))],

          [s.Button("Generate Result",pad=(200,30),**bo)],

          [s.Text(" **\t Loading Result ....     ** ",text_color='#FFFF00', background_color='black', font='Courier 20',key = 'res')],

          [s.Button("Generate statistics",**bt),s.Button("Voter statistics",pad=(100,0),**bo),s.Button("All Voted",**bo)]]



Window = s.Window("Voteing App",layout)




def result():                        # Function for Generating and Displaying the Result
    global l   # globalization of list l

    l  = [DMK,ADMK,MNM,NTK,BJP,NOTA]    # list containing  votes of the partise 

    if max(l) == DMK:
        Window['res'].update("\t     DMK wins        \t")

    elif max(l) == ADMK:
        Window['res'].update("\t     ADMK wins        \t")  

    elif max(l) == MNM:
        Window['res'].update("\t     MNM wins        \t")

    elif max(l) == NTK:
        Window['res'].update("\t     NTK wins        \t")

    elif max(l) == BJP:
        Window['res'].update("\t     BJP wins        \t")

    elif max(l) == NOTA:
        Window['res'].update("\t     NOTA wins       \t")


   

def Voter_ID_checker():         # Function for checking voter Id

    if int(values[0]) in v:
        Window['out'].update("  Eligible to vote        \t")
        v.remove(int(values[0]))     

    else:
        Window['out'].update("Not Eligible to vote ( or ) you already voted")




def piechart(l):             # Function for Generating piechart

    y = np.array(l)
    labels = ["DMK","ADMK","MNM","NTK","BJP","NOTA"]
    fig1, ax1 = plt.subplots()
    ax1.pie(y,labels=labels, autopct='%1d%%',startangle=90)
    plt.show() 



def Additional_voter_info():     # Function for Generating voter info piechart

    s = m - len(l)
    n = [s,len(l)]
    x = np.array(n)
    labels = ["Voted","Not Voted"]
    fig1, ax1 = plt.subplots()
    ax1.pie(x,labels=labels, autopct='%1d%%',startangle=90)
    plt.show() 



while True:
    event , values = Window.read()

    if event == "Enter":
        Voter_ID_checker()

    elif event == "Vote DMK":
        DMK += 1

    elif event == "Vote ADMK":
        ADMK += 1

    elif event == "Vote MNM":
        MNM += 1

    elif event == "Vote NTK":
        NTK += 1

    elif event == "Vote BJP":
        BJP += 1

    elif event == "NOTA":
        NOTA += 1

    elif event == "Generate Result":
        result()

    elif event == "Generate statistics":
        piechart(l)

    elif event == "Voter statistics":
        Additional_voter_info()

    elif event == "All Voted":
        break
 
 
Window.close()
