import tkinter

import matplotlib.pyplot as plt
from tkinter import *
from memo import read_data
from change import *
import numpy as np


def make_interface(k):
    win = Tk()

    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()

    win.geometry('%dx%d+%d+%d' % (300, 500, ws * 2 / 3 - 100, hs / 2 - 250))
    win.option_add("*Font", "궁서 20")

    title = Label(win, text='H-R도 계열 예측기')
    Na = Label(win, text="이름:")
    Ca = Label(win, text="분광형:")
    La = Label(win, text="광도:")

    Name = Entry(win, width=10)
    C = Entry(win, width=10)
    L = Entry(win, width=10)

    title.place(relx=0.1, rely=0.15)
    Name.place(relx=0.4, rely=0.4)
    C.place(relx=0.4, rely=0.5)
    L.place(relx=0.4, rely=0.6)
    Na.place(relx=0.15, rely=0.4)
    Ca.place(relx=0.08, rely=0.5)
    La.place(relx=0.15, rely=0.6)
    result2 = Label(win, text="결과는~~")
    result2.place(relx=0.4, rely=0.8)
    def get_data():
        result2 = Label(win, text="결과는~~")
        result2.place(relx=0.4, rely=0.8)
        Name_Data = Name.get()
        C_Data = C.get()
        L_Data = L.get()

        ARR = [Name_Data, C_Data, L_Data]
        print(Name_Data, C_Data, L_Data, type(Name_Data), type(C_Data), type(L_Data))
        x = [ARR[1]]
        y = [ARR[2]]

        datas = read_data()

        X = []
        Y = []
        keys = list(datas.keys())

        for a in range(len(keys)):
            X.append(datas[keys[a]][0])
            Y.append(datas[keys[a]][1])

        chages(X, Y)
        chages(x, y)

        dis = []
        for a, b in zip(X, Y):
            dis.append(((a - x[0]) ** 2 + (b - y[0]) ** 2) ** (1 / 2))

        fes = {}
        for i, a in enumerate(dis):
            fes[a] = datas[keys[i]][2]
        print(fes)
        fes_keys = list(fes.keys())
        fes_keys.sort()
        fes_keys = fes_keys[:k]

        Q = []
        for a in fes_keys:
            Q.append(fes.get(a))
        q = 0
        n = 0
        whe=0
        for a in Q:
            n = Q.count(a)
            if q > n:
                q = n
                whe = Q.index(a)

        print(whe)
        result = Label(win, text=Q[whe])
        result.place(relx=0.4, rely=0.8)

        x = np.array(x)
        y = np.array(y)
        X = np.array(X)
        Y = np.array(Y)

        plt.title("H-R도")
        plt.xlabel('분광형')
        plt.ylabel('광도')

        plt.scatter(X, Y, c='r')
        plt.scatter(x, y)
        plt.show()

    bnt = Button(win, text="예측하기")
    bnt.config(command=get_data)
    bnt.place(relx=0.4, rely=0.7)
    bnt = Button(win, text="종료")
    bnt.config(command=lambda:[win.destroy(),plt.close()])
    bnt.place(relx=0.7, rely=0.025)
    win.mainloop()
