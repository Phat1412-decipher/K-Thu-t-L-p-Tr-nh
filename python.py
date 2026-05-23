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
            return [f"Tên bài hát: {Data[Mid].Songname} - Tên tác giả: {Data[Mid].fullname} - Thể loại: {Data[Mid].type} - Thời lượng: {Data[Mid].time}",Mid]
        if Draft == 2:
            return Mid
    if Data[Mid].Songname > Token:
        return Search(Data, Token, left, Mid - 1)
    else:
        return Search(Data, Token, Mid + 1, right)

def Extend_file(Token):
    with open("playlist.txt", "a", encoding="utf-8") as file:
        for i in range(len(Token)):
            file.write(f"Tên bài hát: {Token[i].Songname} - Tên tác giả: {Token[i].fullname} - Thể loại: {Token[i].type} - Thời lượng: {Token[i].time}\n")
    Token.clear()

def Delete_item(Data, Token):
    Search_result = Search(Data, Token, 0, len(Data) - 1,2)   
    if Search_result == "Not Found":
        print("Not Found to delete !")
    else:
        del Data[Search_result]
        print("Deleted !")
    with open("playlist.txt", "w", encoding="utf-8") as file:
        for i in range(len(Data)):
            file.write(f"Tên bài hát: {Data[i].Songname} - Tên tác giả: {Data[i].fullname} - Thể loại: {Data[i].type} - Thời lượng: {Data[i].time}\n")

def Delete_total_file():
    with open("playlist.txt", "w", encoding="utf-8") as file:
        file.write("")

def Divide_String(line,l,r):
    a=""
    b=[]
    for i in range(len(line)):
        if line[i]== l:
            for j in range (i+1,len(line)):
                if line[j]==r or line[j]=="\n":
                    b.append(a)
                    a=""
                    break
                else:
                    a+=line[j]
            i=j
    return b              
            
Per_var=True
Data=[]
with open("playlist.txt", "r", encoding="utf-8") as f:
    for line in f:
        Draft=[]
        Draft=Divide_String(line,":","-")
        Data.append(Playlist(Draft[0].strip(),Draft[1].strip(),Draft[2].strip(),Draft[3].strip()))        
if len(Data)==0:
    Most_Searched=[0]
else:
    Most_Searched=[0]*len(Data)    
Token=[]
while Per_var:
    print("-"*50)
    print(f"Hiện tại có {len(Data)} bài hát trong playlist !")
    if max(Most_Searched) != 0:
        print(f"Bài hát được tìm kiếm nhiều nhất là: {Data[Most_Searched.index(max(Most_Searched))].Songname} với {max(Most_Searched)} lượt tìm kiếm !")
    else:
        print("Chưa có bài hát nào được tìm kiếm !")
    Answer= input("Bạn muốn làm gì ? (1: Thêm bài hát, 2: Xóa bài hát, 3: Xóa toàn bộ file, 4: Tìm kiếm bài hát, 5: Thoát chương trình ,6: Hiển thị danh sách bài hát) ")
    if Answer not in ["1","2","3","4","5","6"]:
        print("Vui lòng nhập một lựa chọn hợp lệ!")
        continue
    if Answer == "1":
        while True:
            try:
                
                
                Number = int(input("Nhập số lượng bài hát muốn thêm: "))
                if Number > 0:
                    break
                print("Vui lòng nhập một số dương!")
            except ValueError:
                print("Vui lòng nhập một số hợp lệ!")
                continue
        for i in range(Number):
            Songname = input("Nhập tên bài hát: ").strip()
            while not Songname:
                print("Tên bài hát không được để trống! Vui lòng nhập lại.")
                Songname = input("Nhập tên bài hát: ").strip()
            artist = input("Nhập tên tác giả: ").strip()
            while not artist:
                print("Tên tác giả không được để trống! Vui lòng nhập lại.")
                artist = input("Nhập tên tác giả: ").strip()
            type = input("Nhập thể loại: ").strip()
            while not type:
                print("Thể loại không được để trống! Vui lòng nhập lại.")
                type = input("Nhập thể loại: ").strip()
            while True:
                try:
                    
                    time = input("Nhập thời lượng (định dạng mm:ss): ").strip()
                    if ':' not in time:
                        print("Thiếu dấu ':' rồi! Vui lòng nhập đúng định dạng mm:ss.")
                        continue
                    minutes, seconds = map(int, time.split(':'))
                    if minutes < 0 or seconds < 0 or seconds >= 60:
                        raise ValueError
                    else:
                        break    
                except ValueError:
                    print("Định dạng thời lượng không hợp lệ! Vui lòng nhập theo định dạng mm:ss.")
                    continue
            Songname = Songname.upper()
            Token.append(Playlist(Songname,artist,type,time))
        Token=Classification(Data, Token)
        Extend_file(Token)
        print("Added !")
    if Answer == "2":
        Songname = input("Nhập tên bài hát cần xóa: ").strip()
        Songname = Songname.upper()
        Delete_item(Data, Songname)
    if Answer == "3":
        Delete_total_file()
        print("Deleted !")
    if Answer == "4":
        Songname = input("Nhập tên bài hát cần tìm kiếm: ").strip()
        Songname = Songname.upper()
        Output=Search(Data, Songname, 0, len(Data) - 1)
        print(Output[0])
        Most_Searched[Output[1]]+=1
    if Answer == "5":
        Per_var = False
        print("Goodbye ! no see you later !")
    if Answer == "6":
        with open("playlist.txt", "r", encoding="utf-8") as file:
            print(file.read())


