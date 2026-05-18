class Playlist:
    def __init__(self, Songname: str,artist: str,type: str,time: str):
        self.Songname = Songname
        self.fullname= artist
        self.type = type
        self.time = time
def Classification(Data, Token):
    Data.extend(Token)
    Data.sort(key=lambda x: x.Songname)
    return sorted(Token, key=lambda x: x.Songname)
def Search(Data, Token,left, right ,Draft=1):
    Mid = (left + right) // 2
    if left > right:
        return "Not Found"
    if Data[Mid].Songname == Token:
        if Draft == 1:
            return Data[Mid].Songname + " - " + Data[Mid].fullname + " - " + Data[Mid].type + " - " + Data[Mid].time
        if Draft == 2:
            return Mid
    if Data[Mid].Songname > Token:
        return Search(Data, Token, left, Mid - 1)
    else:
        return Search(Data, Token, Mid + 1, right)

def Extend_file(Token):
    with open("playlist.txt", "a") as file:
        for i in range(len(Token)):
            file.write(f"Ten bai hat: {Token[i].Songname} - Ten tac gia: {Token[i].fullname} - Loai: {Token[i].type} - Thoi luong: {Token[i].time}\n")
    Token.clear()

def Delete_item(Data, Token):
    Search_result = Search(Data, Token, 0, len(Data) - 1,2)   
    if Search_result == "Not Found":
        print("Not Found to delete !")
    else:
        del Data[Search_result]
        print("Deleted !")

def Delete_total_file():
    with open("playlist.txt", "w") as file:
        file.write("")

Per_var=True
Data=[]
Token=[]
while Per_var:
    Answer= input("Bạn muốn làm gì ? (1: Thêm bài hát, 2: Xóa bài hát, 3: Xóa toàn bộ file, 4: Tìm kiếm bài hát, 5: Thoát chương trình ,6: Hiển thị danh sách bài hát) ")
    if Answer == "1":
        Number = int(input("Nhập số lượng bài hát muốn thêm: "))
        for i in range(Number):
            Songname = input("Nhập tên bài hát: ")
            artist = input("Nhập tên tác giả: ")
            type = input("Nhập thể loại: ")
            time = input("Nhập thời lượng: ")
            Songname = Songname.upper()
            Token.append(Playlist(Songname,artist,type,time))
        Token=Classification(Data, Token)
        Extend_file(Token)
        print("Added !")
    if Answer == "2":
        Songname = input("Nhập tên bài hát cần xóa: ")
        Songname = Songname.upper()
        Delete_item(Data, Songname)
    if Answer == "3":
        Delete_total_file()
    if Answer == "4":
        Songname = input("Nhập tên bài hát cần tìm kiếm: ")
        Songname = Songname.upper()
        print(Search(Data, Songname, 0, len(Data) - 1))
    if Answer == "5":
        Per_var = False
        print("Goodbye ! no see you later !")
    if Answer == "6":
        with open("playlist.txt", "r") as file:
            print(file.read())


