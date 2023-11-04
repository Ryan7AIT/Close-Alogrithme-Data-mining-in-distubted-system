from tkinter import *
from tkinter import font as tkfont
from tkinter import filedialog
import csv
from close import close
from dClose import dClose
from tkinter import ttk
import math

#input : minsup&&database


class MyWindow:

    def UploadAction(self):
        self.filename = filedialog.askopenfilename()

    def UploadAction2(self):
        self.filename2 = filedialog.askopenfilename()
                

    def __init__(self, win):
        
        self.lbl0=Label(win, text='Welcome to close algorithme ')
        self.lbl0.place(x=350, y=10)
        
        self.lbl1=Label(win, text='Chosse a minsup:')
        self.lbl2=Label(win, text='import the first data base:')
        self.lbl3=Label(win, text='import the second data base:') 

         
        self.t1=Entry()
        # self.t2=Entry()

        self.button =  Button(text='Open', command=self.UploadAction)
        self.button.pack()

        self.button2 =  Button(text='Open', command=self.UploadAction2)
        self.button2.pack()

        
        # self.btn2=Button(win, text='Begin')
        
        
        
        self.lbl1.place(x=100, y=100)
        self.t1.place(x=320, y=100)
        
        self.lbl2.place(x=100, y=150)
        self.lbl3.place(x=100, y=200)

        self.button.place(x=320,y=150)
        self.button2.place(x=320,y=200)

        

        self.b2=Button(win, text='Begin')
        self.b2.bind('<Button-1>', self.solve)
        
        self.b2.place(x=340, y=300)
        

        self.frame1 = LabelFrame(window, text="Local frequent item set for the first Daatabase")
        self.frame1.place(rely=0.4, relx=0.2, height=300, width=300)

        self.frame2 = LabelFrame(window, text="Local frequent item set for the second Daatabase")
        self.frame2.place(rely=0.4, relx=0.4, height=300, width=300)

        self.frame3 = LabelFrame(window, text="Gloabl frequent item set for the first Daatabase")
        self.frame3.place(rely=0.4, relx=0.6, height=300, width=300)


        self.frame4 = LabelFrame(window, text="Global Associative rules")
        self.frame4.place(rely=0.4, relx=0.8, height=300, width=300)


    def solve(self, event):
        pass
        data = {}
        # #self.t3.delete(0, 'end')
        minsup= float(self.t1.get())
        filepath= self.filename
        filepath2= self.filename2


        # print(minsup)
        # print(filepath)


        dataset1 = []
        dataset2 = []


        csv_file_path1 = filepath
        csv_file_path2 = filepath2



        with open(csv_file_path1, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            
            # Iterate through each row in the CSV file
            for row in csv_reader:
                # Append the row as a sublist to the list
                dataset1.append(row)


        database1 = [[item for item in sublist if item] for sublist in dataset1]



        with open(csv_file_path2, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            
            # Iterate through each row in the CSV file
            for row in csv_reader:
                # Append the row as a sublist to the list
                dataset2.append(row)


        database2 = [[item for item in sublist if item] for sublist in dataset2]




        


        # num4= self.t4.get()
        
        # v1 = num1.split()
        # v2 = num2.split()
        # vecContraint = num4.split()
        # lmda = 0.0001
        # p=0.3
        # poid= int(self.t5.get())
        
        # #data[weights] = weight
        
        # (optimalvalue,pmax,v1all,v2all,xi,alloptimal)= aggregation(vecContraint, v1, v2, lmda, p, poid)



        # a = [['A', 'B', 'C', 'D', 'E'],
        #    ['A', 'B'],
        #    ['C', 'E'],
        #    ['A', 'B', 'D', 'E'],
        #    ['A', 'C', 'D']]
        
        # minsup = math.exp(-0.4 * len(database) - 0.2) + 0.2


        # self.t1.insert(END, str(minsup))


        print('data1')
        print(database1)
        print('data2:')

        print(database2)

        d1 = [['A', 'B', 'C', 'D', 'E'],['A','B']]
        d3= [['C', 'E'], ['A', 'B', 'D', 'E'], ['A', 'C', 'D']]
        df1,df2,df3 = dClose([database1,database2],minsup)
        print('df1:====')
        print(df1)  
        # print(df2)


        tv1 = ttk.Treeview(self.frame1)
        column_list_account = ["Rule", "Support"]
        tv1['columns'] = column_list_account
        tv1["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv1.heading(column, text=column)
            tv1.column(column, width=50)
        tv1.place(relheight=10, relwidth=0.995)
        treescroll = ttk.Scrollbar(self.frame1)
        treescroll.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")


        tv2 = ttk.Treeview(self.frame2)
        column_list_account = ["Rule", "Support"]
        tv2['columns'] = column_list_account
        tv2["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv2.heading(column, text=column)
            tv2.column(column, width=50)
        tv2.place(relheight=10, relwidth=0.995)
        treescroll = ttk.Scrollbar(self.frame2)
        treescroll.configure(command=tv2.yview)
        tv2.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")


        tv3 = ttk.Treeview(self.frame3)
        column_list_account = ["Rule", "Count"]
        tv3['columns'] = column_list_account
        tv3["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv3.heading(column, text=column)
            tv3.column(column, width=50)
        tv3.place(relheight=10, relwidth=0.995)
        treescroll = ttk.Scrollbar(self.frame3)
        treescroll.configure(command=tv3.yview)
        tv3.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")





        # self.pokemon_info = [['Bulbasaur', 'Grass', '318'], ['Ivysaur', 'Grass', '405'], ['Venusaur', 'Grass', '525'], ['Charmander', 'Fire', '309'], ['Charmeleon', 'Fire', '405'], ['Charizard', 'Fire', '534'], ['Squirtle', 'Water', '314'], ['Wartortle', 'Water', '405'], ['Blastoise', 'Water', '530'], ['Caterpie', 'Bug', '195'], ['Metapod', 'Bug', '205'], ['Butterfree', 'Bug', '395'], ['Weedle', 'Bug', '195'], ['Kakuna', 'Bug', '205'], ['Beedrill', 'Bug', '395'], ['Pidgey', 'Normal', '251'], ['Pidgeotto', 'Normal', '349'], ['Pidgeot', 'Normal', '479'], ['Rattata', 'Normal', '253'], ['Raticate', 'Normal', '413'], ['Spearow', 'Normal', '262'], ['Fearow', 'Normal', '442'], ['Ekans', 'Poison', '288'], ['Arbok', 'Poison', '448'], ['Pikachu', 'Electric', '320'], ['Raichu', 'Electric', '485'], ['Sandshrew', 'Ground', '300'], ['Sandslash', 'Ground', '450'], ['Nidoran?', 'Poison', '275'], ['Nidorina', 'Poison', '365'], ['Nidoqueen', 'Poison', '505'], ['Nidoran?', 'Poison', '273'], ['Nidorino', 'Poison', '365'], ['Nidoking', 'Poison', '505'], ['Clefairy', 'Fairy', '323'], ['Clefable', 'Fairy', '483'], ['Vulpix', 'Fire', '299'], ['Ninetales', 'Fire', '505'], ['Jigglypuff', 'Normal', '270'], ['Wigglytuff', 'Normal', '435'], ['Zubat', 'Poison', '245'], ['Golbat', 'Poison', '455'], ['Oddish', 'Grass', '320'], ['Gloom', 'Grass', '395'], ['Vileplume', 'Grass', '490'], ['Paras', 'Bug', '285'], ['Parasect', 'Bug', '405'], ['Venonat', 'Bug', '305'], ['Venomoth', 'Bug', '450'], ['Diglett', 'Ground', '265'], ['Dugtrio', 'Ground', '425'], ['Meowth', 'Normal', '290'], ['Persian', 'Normal', '440'], ['Psyduck', 'Water', '320'], ['Golduck', 'Water', '500'], ['Mankey', 'Fighting', '305'], ['Primeape', 'Fighting', '455'], ['Growlithe', 'Fire', '350'], ['Arcanine', 'Fire', '555'], ['Poliwag', 'Water', '300'], ['Poliwhirl', 'Water', '385'], ['Poliwrath', 'Water', '510'], ['Abra', 'Psychic', '310'], ['Kadabra', 'Psychic', '400'], ['Alakazam', 'Psychic', '500'], ['Machop', 'Fighting', '305'], ['Machoke', 'Fighting', '405'], ['Machamp', 'Fighting', '505'], ['Bellsprout', 'Grass', '300'], ['Weepinbell', 'Grass', '390'], ['Victreebel', 'Grass', '490'], ['Tentacool', 'Water', '335'], ['Tentacruel', 'Water', '515'], ['Geodude', 'Rock', '300'], ['Graveler', 'Rock', '390'], ['Golem', 'Rock', '495'], ['Ponyta', 'Fire', '410'], ['Rapidash', 'Fire', '500'], ['Slowpoke', 'Water', '315'], ['Slowbro', 'Water', '490'], ['Magnemite', 'Electric', '325'], ['Magneton', 'Electric', '465'], ["Farfetch'd", 'Normal', '377'], ['Doduo', 'Normal', '310'], ['Dodrio', 'Normal', '470'], ['Seel', 'Water', '325'], ['Dewgong', 'Water', '475'], ['Grimer', 'Poison', '325'], ['Muk', 'Poison', '500'], ['Shellder', 'Water', '305'], ['Cloyster', 'Water', '525'], ['Gastly', 'Ghost', '310'], ['Haunter', 'Ghost', '405'], ['Gengar', 'Ghost', '500'], ['Onix', 'Rock', '385'], ['Drowzee', 'Psychic', '328'], ['Hypno', 'Psychic', '483'], ['Krabby', 'Water', '325'], ['Kingler', 'Water', '475'], ['Voltorb', 'Electric', '330'], ['Electrode', 'Electric', '490'], ['Exeggcute', 'Grass', '325'], ['Exeggutor', 'Grass', '530'], ['Cubone', 'Ground', '320'], ['Marowak', 'Ground', '425'], ['Hitmonlee', 'Fighting', '455'], ['Hitmonchan', 'Fighting', '455'], ['Lickitung', 'Normal', '385'], ['Koffing', 'Poison', '340'], ['Weezing', 'Poison', '490'], ['Rhyhorn', 'Ground', '345'], ['Rhydon', 'Ground', '485'], ['Chansey', 'Normal', '450'], ['Tangela', 'Grass', '435'], ['Kangaskhan', 'Normal', '490'], ['Horsea', 'Water', '295'], ['Seadra', 'Water', '440'], ['Goldeen', 'Water', '320'], ['Seaking', 'Water', '450'], ['Staryu', 'Water', '340'], ['Starmie', 'Water', '520'], ['Scyther', 'Bug', '500'], ['Jynx', 'Ice', '455'], ['Electabuzz', 'Electric', '490'], ['Magmar', 'Fire', '495'], ['Pinsir', 'Bug', '500'], ['Tauros', 'Normal', '490'], ['Magikarp', 'Water', '200'], ['Gyarados', 'Water', '540'], ['Lapras', 'Water', '535'], ['Ditto', 'Normal', '288'], ['Eevee', 'Normal', '325'], ['Vaporeon', 'Water', '525'], ['Jolteon', 'Electric', '525'], ['Flareon', 'Fire', '525'], ['Porygon', 'Normal', '395'], ['Omanyte', 'Rock', '355'], ['Omastar', 'Rock', '495'], ['Kabuto', 'Rock', '355'], ['Kabutops', 'Rock', '495'], ['Aerodactyl', 'Rock', '515'], ['Snorlax', 'Normal', '540'], ['Articuno', 'Ice', '580'], ['Zapdos', 'Electric', '580'], ['Moltres', 'Fire', '580'], ['Dratini', 'Dragon', '300'], ['Dragonair', 'Dragon', '420'], ['Dragonite', 'Dragon', '600'], ['Mewtwo', 'Psychic', '680'], ['Mew', 'Psychic', '600']]

        self.dflist = df1.values.tolist()
        for row in self.dflist:
                tv1.insert("", "end", values=row)


        self.dflist = df2.values.tolist()
        for row in self.dflist:
                tv2.insert("", "end", values=row)


        df_no_duplicates = df3.drop_duplicates(subset=['Item'])
        self.dflist = df_no_duplicates.values.tolist()
        for row in self.dflist:
                tv3.insert("", "end", values=row)


        print('df333')
        print(df3)
        
        
        # self.t6.insert(END, str(xi[0])  + ' , '  + str(xi[1]) + ' , '  + str(xi[2]) + ' , '  + str(xi[3]) + ' , '  + str(xi[4])   )
        
        # self.t8.insert(END, str( alloptimal[0]) )


        # self.t9.insert(END, str(alloptimal[1]))


        # self.t10.insert(END, str(alloptimal[2]))
        
        # self.t11.insert(END, str(alloptimal[3]))
        
        # self.t12.insert(END, str(pmax))




        
        #self.t7.insert(END, str(optimalvalue))

window=Tk()
mywin=MyWindow(window)
window.title('Close Algorithm')
window.geometry("900x600")
window.mainloop()




