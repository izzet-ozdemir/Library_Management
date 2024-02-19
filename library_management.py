import csv

database = "Books.txt"

class cls_Library:
    def __init__(self, p_Mode):
        if p_Mode == 'Add':
            self.p_Data = open(database, 'a+')
        elif p_Mode == 'List':
            self.p_Data = open(database, 'r')
        else:
            pass

    def __del__(self):
        self.p_Data.close()

class cls_Books:
    def __init__(self, p_BookName, p_Author, p_ReleaseDate, p_PageNumbers):
        self.BookName = p_BookName
        self.Author = p_Author
        self.ReleaseDate = p_ReleaseDate
        self.PageNumbers = p_PageNumbers

    def d_DecorateBook(self):
        p_BookLine = self.BookName+","+self.Author+","+self.ReleaseDate+","+self.PageNumbers+"\n"
        return p_BookLine


class cls_Management:
    def d_ListBooks():
        try:
            p_List = cls_Library('List')
            pListData = p_List.p_Data.readlines()
            p_length = len(pListData)
            if p_length == 0:
                print("Database is absent! Enter record Please!\n")
            else:
                say = 0
                print('\n')
                print('List of Books')
                print('------------------')
                for p_lines in pListData:
                    p_newlines = p_lines.replace(',','\n')
                    p_splitLines = p_newlines.splitlines()
                    arr_liste = list()
                    arr_liste = p_splitLines
                    say += 1
                    print("Book" + str(say) + " > Name: "+arr_liste[0]+" - Author: "+arr_liste[1])
                print('\n')
        except:
            print("Error : Didn't find database...\n")

    def d_AddBook():
        in_BookName = input("Enter the book name : ")
        in_Author = input("Enter the author of book : ")
        in_ReleaseDate = input("Enter the release date of book : ")
        in_PageNumbers = input("Enter the number of pages of the book : ")
        obj_Book = cls_Books(
            p_BookName=in_BookName,
            p_Author=in_Author,
            p_ReleaseDate=in_ReleaseDate,
            p_PageNumbers=in_PageNumbers
        )
        p_DecBook = obj_Book.d_DecorateBook()
        p_file = cls_Library('Add')
        p_file.p_Data.writelines(p_DecBook)
        p_file.p_Data.close()
        print("Adding Process Completed\n")

    def d_RemoveBook():
        pass

def d_GetMenu():
    print("*** Library Management ***")
    print("[1] List Books")
    print("[2] Add Book")
    print("[3] Remove Book")
    print("[4] Exit")
    print('------------------')
    p_choice = eval(input("Enter your chioce : "))
    return p_choice

def d_Main():
    try:
        while True:
            p_Option = d_GetMenu()
            if p_Option == 1:
                cls_Management.d_ListBooks()
            elif p_Option == 2:
                cls_Management.d_AddBook()
            elif p_Option == 3:
                cls_Management.d_RemoveBook()
            elif p_Option == 4:
                #del cls_Library
                break
            else:
                break
            # {1:df_ListBooks(), 2:df_AddBook(), 3:df_RemoveBook()}[p_Option]()
    except:
        print("Error : Call you admin please!\n")
    finally:
        print("We welcome you to our library again!")

d_Main()