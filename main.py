from pathlib import Path
from tkinter import *
from tkinter import messagebox as msg
import random

#附加檔案路徑
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def reset():
    if num1 == "":
        msg.showerror("系統錯誤", "無法重製籤筒!")
    else:
        MsgBox = msg.askquestion('系統訊息','確定要重置籤筒嗎?')
        if MsgBox == 'yes':
            msg.showinfo("系統訊息", "已重置籤筒!")
            global allSet
            allSet = set()
            for i in range(1,num1 + 1):
                allSet.add(i)
            #TEST
            print(num1)
            print(allSet)
        else:
            pass

def takeNum():
    for item in RandOutPut:
        allSet.remove(item)
    #TEST
    print(list(allSet))
    print("---------------")


def debug_dontake():
    #TEST
    print(list(allSet))
    print("---------------")

#結果視窗

def openNewWindow():
    NewWindow = Tk()
    NewWindow.title("抽籤結果")
    NewWindow.geometry("972x546")
    NewWindow.geometry('+0+0')
    NewWindow.configure(bg = "#ffffff")
    canvas = Canvas(
        NewWindow,
        bg = "#ffffff",
        height = 546,
        width = 972,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    canvas.create_text(
        480.5, 95.0,
        text = "抽籤結果",
        fill = "#515486",
        font = ("Arial", int(70.0)))
    global StudentsInt

    if StudentsInt > 80:
        canvas.create_text(
            485.5, 290.5,
            text = RandOutPut,
            width = 900,
            fill = "#000000",
            font = ("Arial", int(30.0)))
    else:
        canvas.create_text(
            476.5, 278.5,
            text = RandOutPut,
            width = 900,
            fill = "#000000",
            font = ("Arial", int(30.0)))

    img0 = PhotoImage(file=relative_to_assets("result_img0.png"))
    result_b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        master = NewWindow,
        command = lambda:[takeNum(),NewWindow.destroy(), mainWindow()],
        relief = "flat")

    result_b0.place(
        x = 262, y = 440,
        width = 189,
        height = 54)

    img1 = PhotoImage(file=relative_to_assets("result_img1.png"))
    result_b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        master = NewWindow,
        command = lambda:[debug_dontake(),NewWindow.destroy(), mainWindow()],
        relief = "flat")

    result_b1.place(
        x = 514, y = 440,
        width = 189,
        height = 54)

    NewWindow.resizable(False, False)
    NewWindow.mainloop()

#剩餘視窗

def LeftWindow():
    global allSet
    if len(allSet) == 0:
        ShowLeft = "無號碼可顯示"
    else:
        ShowLeft = str(allSet)
        ShowLeft = ShowLeft.replace("{","")
        ShowLeft = ShowLeft.replace("}","")
    LeftWindow = Tk()
    LeftWindow.geometry("1000x600")
    LeftWindow.geometry('+0+0')
    LeftWindow.configure(bg = "#344966")
    canvas = Canvas(
        LeftWindow,
        bg = "#344966",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    canvas.create_text(
        492.0, 63.0,
        text = "籤筒剩餘號碼",
        fill = "#fafffd",
        font = ("Arial", int(54.0)))

    canvas.create_text(
        491.5, 305.0,
        text = ShowLeft,
        width = 900,
        fill = "#fafffd",
        font = ("Arial", int(36.0)))

    img0 = PhotoImage(
        file=relative_to_assets("close.png"))
    b0 = Button(
        image = img0,
        borderwidth = 0,
        master = LeftWindow,
        highlightthickness = 0,
        command = lambda:[LeftWindow.destroy(), mainWindow()],
        relief = "flat")

    b0.place(
        x = 413, y = 506,
        width = 160,
        height = 49)

    LeftWindow.resizable(False, False)
    LeftWindow.mainloop()

#主要視窗

def mainWindow():

    def GenerateNum():
        global StudentsInt
        Students = entry0.get()
        need = entry1.get()
        try:
            StudentsInt = int(Students)
            NeedInt = int(need)
            if StudentsInt > 100:
                msg.showerror("輸入錯誤", "無法抽取大於100人!")
            elif NeedInt > StudentsInt:
                msg.showerror("輸入錯誤", "抽取人數無法大於班級人數!")
            elif NeedInt == 0:
                msg.showerror("輸入錯誤", "請至少抽取1個人!")
            else:
                global num0
                global num1
                global allSet
                global RandOutPut
                if num1 == "":
                    num1 = StudentsInt
                    #生成
                    allSet = set()
                    for i in range(1,StudentsInt + 1):
                        allSet.add(i)
                else:
                    num2 = StudentsInt
                    if num1 != num2:
                        num1 = num2
                        num2 = None
                        #生成
                        msg.showinfo("系統訊息", "系統偵測到你修改了班級人數，已重置籤筒!")
                        allSet = set()
                        for i in range(1,StudentsInt + 1):
                            allSet.add(i)
                if len(allSet) == 0:
                    msg.showinfo("系統訊息", "籤筒內已經沒人，請將所有人放回籤筒!")
                elif NeedInt > len(allSet):
                    msg.showerror("輸入錯誤", f"目前籤筒內只剩下{len(allSet)}個人")
                else:
                    RandOutPut = random.sample(allSet,NeedInt)
                    for item in RandOutPut:
                        print(item,end="  ") #TEST

                    window.destroy()
                    openNewWindow()
        except:
            msg.showerror("輸入錯誤", "請輸入一個正確的數值!")

    global window
    window = Tk()
    window.title("班級抽籤系統")
    window.geometry("577x730")
    window.geometry('+0+0')
    window.configure(bg = "#3c91e6")
    canvas = Canvas(
        window,
        bg = "#3c91e6",
        height = 730,
        width = 577,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    canvas.create_text(
        291.0, 83.0,
        text = "班級抽籤工具",
        fill = "#fafffd",
        font = ("Arial", int(50.0)))

    canvas.create_text(
        288.5, 138.5,
        text = "請輸入以下資料並且點擊”抽籤”",
        fill = "#fafffd",
        font = ("Arial", int(18.0)))

    entry0_img = PhotoImage(
        file = relative_to_assets("img_textBox0.png"))
    entry0_bg = canvas.create_image(
        287.5, 283.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#fafffd",
        font= ('Arial 18'),
        highlightthickness = 0)
    global num1
    entry0.insert(END, num1)

    entry0.place(
        x = 119.0, y = 263,
        width = 337.0,
        height = 39)

    entry1_img = PhotoImage(
        file = relative_to_assets("img_textBox1.png"))
    entry1_bg = canvas.create_image(
        288.0, 408.5,
        image = entry1_img)
    entry1 = Entry(
        bd = 0,
        bg = "#fafffd",
        font= ('Arial 18'),
        highlightthickness = 0)

    entry1.place(
        x = 119.0, y = 388,
        width = 338.0,
        height = 39)

    canvas.create_text(
        195.5, 369.0,
        text = "請輸入抽取人數:",
        fill = "#fafffd",
        font = ("Arial", int(17.0)))

    img0 = PhotoImage(
        file = relative_to_assets("img0.png"))
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:[GenerateNum()],
        relief = "flat")

    b0.place(
        x = 112, y = 513,
        width = 160,
        height = 50)

    img1 = PhotoImage(
        file = relative_to_assets("img1.png"))
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:[window.destroy(), LeftWindow()],
        relief = "flat")

    b1.place(
        x = 421, y = 681,
        width = 150,
        height = 40)

    img2 = PhotoImage(
        file = relative_to_assets("img2.png"))
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = reset,
        relief = "flat")

    b2.place(
        x = 307, y = 513,
        width = 157,
        height = 46)

    canvas.create_text(
        195.5, 243.5,
        text = "請輸入班級人數:",
        fill = "#fafffd",
        font = ("Arial", int(17.0)))

    canvas.create_text(
        135.0, 703.0,
        text = "Made by 訊一2 35謝邵丞",
        fill = "#ffffff",
        font = ("Arial", int(17.0)))

    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    allSet = set()
    num1 = ""
    mainWindow()