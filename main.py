class Donut:
    def __init__(self,flaver,tipping,filling,size):
        self.flaver = flaver
        self.tipping = tipping
        self.filling = filling
        self.size = size

class Customer:
    def __init__(self,name,age,address,faverite_dessert):
        self.name = name
        self.age =  age
        self.address = address
        self.faverite_dessert = faverite_dessert

class Cake:
    def __init__(self,flaver,price,quality):
        self.flaver = flaver
        self.price = price
        self.quality = quality



class AdultBook:

    def __init__(self):
        self.BookLis = []

    def AddBookInfo(self,NameBook,IdBook,AmountBook,NameArtist):
        InfoBook = [NameBook,IdBook,AmountBook,NameArtist]
        Nofound = 0
        if len(self.BookLis) == 0:
            self.BookLis.append(InfoBook)
        else:
            for Name in self.BookLis:
                if Name[0] == NameBook:
                    Name[2] += AmountBook
                elif Name[0] != NameBook:
                    Nofound += 1
            if len(self.BookLis) == Nofound:
                self.BookLis.append(InfoBook)

    def FineBook(self,NameBook):
        Many = len(self.BookLis)
        NotFound = 0
        for Name in self.BookLis:
            if Name[0] == NameBook:
                print(Name)
            else:
                NotFound += 1
        if NotFound == Many:
            print("Not Found")

    def DeleteInfoBook(self,NameBook):
        for i,Name in enumerate(self.BookLis):
            if Name[0] == NameBook:
                Found = i
                self.BookLis.pop(Found)
                break
    def ShowAdultBook(self):
        Num = 1
        print("        "+"ชื่อ"+"   รหัสหนังสือ"+" จำนวน" +" ชื่อผู้แต่ง")
        for Book in self.BookLis:
            print("เล่มที่ " + str(Num),end = " ")
            for i in Book:
                print(str(i)+"  ",end = " ")
                Num += 1
            print()


class ChildrenBook:
    def __init__(self):
        self.BookList = []

    def AddBook(self, NameBook, IdBook, AmountBook, ArtistBook):
        no_found = 0
        BookInfo = [NameBook, IdBook, AmountBook, ArtistBook]
        if len(self.BookList) == 0:
            self.BookList.append(BookInfo)
        else:
            for name_book in self.BookList:
                if name_book[0] == NameBook:
                    name_book[2] += AmountBook
                elif name_book[0] != NameBook:
                    no_found += 1
            if no_found == len(self.BookList):
                self.BookList.append(BookInfo)

    def DeleteBook(self, NameBook):
        for name_book in self.BookList:
            if NameBook == name_book[0]:
                self.BookList.remove(name_book)

    def FindBook(self, NameBook):
        no_found = 0
        for name_book in self.BookList:
            if NameBook == name_book[0]:
                print(name_book)
            else:
                no_found += 1
        if no_found == len(self.BookList):
            print('Not Found')

    def ShowChildrenBookBook(self):
        Num = 1
        print("        "+"ชื่อ"+"   รหัสหนังสือ"+" จำนวน" +" ชื่อผู้แต่ง")
        for Book in self.BookList:
            print("เล่มที่ " + str(Num),end = " ")
            for i in Book:
                print(str(i)+"  ",end = " ")
                Num += 1
            print()



AdultBook = AdultBook()
ChildrenBookBook = ChildrenBook()

while True:
    Option = int(input("กด 1.เพิ่มข้อมูลหนังสือ 2.หาหนังสือ 3.ลบหนังสือ 4.แสดงหนังสือทั้งหมด : "))
    if Option == 1:
        State = True

        while State :
            OptionBook = int(input("ชนิดหนังสือ 1.หนังสือผู้ใหญ่ 2.หนังสือเด็ก : "))
            NameBook = input("ชื่อหนังสือที่ต้องการจะเพิ่ม : ")
            IdBook = input("นหัสหนังสือ : ")
            AmountBook = int(input("จำนวนหนังสือ : "))
            NameArtist = input("ชื่อผู้แต่ง : ")

            if OptionBook == 1:
                AdultBook.AddBookInfo(NameBook,IdBook,AmountBook,NameArtist)
            elif OptionBook == 2:
                ChildrenBookBook.AddBook(NameBook, IdBook, AmountBook, NameArtist)
            Out = input("ต้องการจะเพิ่มหนังสืออีกหรือไม่ N/Y : ")
            if Out == "N" or Out == "n":
                State = False
    elif Option == 2:
        State = True
        while State:
            OptionBook = int(input("ชนิดหนังสือ 1.หนังสือผู้ใหญ่ 2.หนังสือเด็ก : "))
            NameBook = input("ชื่อหนังสือที่ต้องการหา : ")

            if OptionBook == 1:
                AdultBook.FineBook(NameBook)
            elif OptionBook == 2:
                ChildrenBookBook.FindBook(NameBook)
            Out = input("ต้องการจะเพิ่มหนังสืออีกหรือไม่ N/Y : ")
            if Out == "N" or Out == "n":
                State = False
    elif Option == 3:
        State = True
        while State:
            OptionBook = int(input("ชนิดหนังสือ 1.หนังสือผู้ใหญ่ 2.หนังสือเด็ก : "))
            NameBook = input("ชื่อหนังสือที่ต้องกาลบ : ")
            if OptionBook == 1:
                AdultBook.DeleteInfoBook(NameBook)
            elif OptionBook == 2:
                ChildrenBookBook.DeleteBook(NameBook)
            Out = input("ต้องการจะเพิ่มหนังสืออีกหรือไม่ N/Y : ")
            if Out == "N" or Out == "n":
                State = False
    elif Option == 4:
        State = True
        while State :
            OptionBook = int(input("ชนิดหนังสือ 1.หนังสือผู้ใหญ่ 2.หนังสือเด็ก : "))
            if OptionBook == 1:
                AdultBook.ShowAdultBook()
            elif OptionBook == 2:
                ChildrenBookBook.ShowChildrenBookBook()
            Out = input("ต้องการจะเพิ่มหนังสืออีกหรือไม่ N/Y : ")
            if Out == "N" or Out == "n":
                State = False



