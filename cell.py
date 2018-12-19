class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
         # true : 空白
        self.isBlank = True
        # true : 黒
        self.isBlack = None
        # true : 置ける
        self.canBlackPlace = False
        self.canWhitePlace = False
        # 
        self.eValueBlack = -100
        self.eValueWhite = -100

    # コピーコンストラクタは copy で挑戦
    
    def set(self, isBlack):
        self.isBlack = isBlack
        self.isBlank = False
