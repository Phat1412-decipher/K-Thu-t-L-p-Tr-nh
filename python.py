class Playlist:
    def __init__(self, Songname,artist):
        self.Songname = Songname
        self.fullname= artist
def Classification(Data, Token):
    Token = sorted(Token, key=lambda x: x.Songname)
    if len(Data) == 0:
        Data.extend(Token)
    else:
        for i in range(len(Data)):
            for j in range(len(Token)):
                if Token[j].Songname > Data[i].Songname and Token[j].Songname < Data[i+1].Songname:
                    Data.insert(i, Token[j])
def Search(Data, Token):
    for i in range(len(Data)):
        if Data[i].Songname == Token:
            return Data[i].Songname + " - " + Data[i].fullname
    return "Not Found"
def Extend_file(Token):
    with open("playlist.txt", "a") as file:
        for i in range(len(Token)):
            file.write(f"Ten bai hat: {Token[i].Songname} - Ten tac gia: {Token[i].fullname}\n")
    Token.clear()
