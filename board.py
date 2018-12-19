import cell

class Board:
    def __init__(self, size):
        # cell配列を初期化
        self.cells = self.ini_cell(size)
        # ボード上のどこかに黒を置けるかどうか
        self.canBlackPlace = None
        self.canWhitePlace = None
        self.size = size
    
    # コピーコンストラクタは copy で挑戦

    # cellsの初期化
    def ini_cell(self, size):
        cells = []
        cells_line = []
        for i in range(size):
            for j in range(size):
                cells_line.append( cell.Cell(i,j) )
            cells.append(cells_line)
            cells_line = []
        return cells

    # ボード上にある指定した色の個数を取得 
    def getPieceNum(self, isBlack):
        num = 0
        for i in range(self.size):
            for j in range(self.size):
                # 空白ではない
                if self.cells[i][j].isBlank == False:
                    if self.cells[i][j].isBlank == isBlack:
                        num += 1
        return num
    
    # 指定した色はどこかに置ける場所があるか返す
    # def canPlace(self, isBlack):



    # 指定のセルに指定の色をおけるか返す
    # def canPlace(self, row, column, isBlack):


    # 指定のセルが黒かどうか返す．セルが空白の場合は常にfalseを返す
    def isBlack(self, row, column):
        if self.cells[row][column].isBlank == False:
            if self.cells[row][column].isBlack:
                return True
            else:
                return False
        else:
            return False

    # 指定のセルが空いているか返す
    def isBlank(self, row, column):
        return self.cell[row][column].isBlank
    
    # 指定のセルに指定の色を置く．おいた後にreverseメソッドを用いて挟まれたピースを裏返し，その後，calcConditionメソッドで盤面の再計算をする
    def set(self, row, column, isBlack):

    # 指定のセルに置かれたピースの周辺8方向について挟まれているか確認し，挟まれたピースを裏返す．
    # 挟めるかどうかの確認にはcanFlipメソッドを用いる．
    def reverse(self, row, column, isBlack):
        Y = [-1,-1,-1,0,1,1,1,0]
        X = [-1,0,1,1,1,0,-1,-1]
        

    
    # ボード上の全てのセルについて，黒と白それぞれがおけるかどうか計算し，cellsプロパティとcanBlackPlaceプロパティ，canWhitePlaceプロパティを更新する．
    def calcCondition(self):
        Y = [-1,-1,-1,0,1,1,1,0]
        X = [-1,0,1,1,1,0,-1,-1]
        for i in range(self.size):
            for j in range(self.size):
                # 空白しかありえないwwwwwですぞwwww
                if(not self.cells[i][j].isBlank):
                    continue
                # もし1方向でもひっくり返すことが出来ればtrueにする
                # 黒
                for k in range(8):
                    if(self.canFlip(i, j, X[k], Y[k], True) ):
                        self.cells[i][j].canBlackPlace = True
                        break
                # 白
                for k in range(8):
                    if(self.canFlip(i, j, X[k], Y[k], False) ):
                        self.cells[i][j].canWhitePlace = True
                        break
                

    # 指定のセルから指定の方向に挟めるか返す
    def canFlip(self, row, column, x, y, isBlack):
        # able = 
        i = 1
        while(1):
            ry = row + y*i
            cx = column + x*i
            # 辿る先が盤面内である
            if(  (ry < self.size and cx < self.size) and (ry > -1 and cx > -1) ):
                # もし先が空白ではなく相手の駒だったら
                if( self.cells[ry][cx].isBlank==False and self.cells[ry][cx].isBlack != isBlack ):
                    i += 1
                # もし先が自分の駒且つ挟めれば
                elif( (self.cells[ry][cx].isBlank==False and self.cells[ry][cx].isBlack == isBlack) and i > 1 ):
                    return [i]
                else:
                    return False
            # 挟めない又は盤面の外
            else:
                return False

    def icon(self):
        icon = []
        #  = self.state
        for y in range(self.size):
            icon_list = []
            for x in range(self.size):
                # 白
                if( (not self.cells[y][x].isBlank) and (self.cells[y][x].isBlack and False )):
                    icon_list.append("●")
                # 黒にしたかった
                elif (not self.cells[y][x].isBlank) and (self.cells[y][x].isBlack):
                    icon_list.append("o")
                else:
                    icon_list.append(" ")
            # print(icon_list)
            icon.append(icon_list)
        self.print_array_icon(icon)
    
    def print_array_icon(self, icon):
        for y in range(self.size):
            st = ""
            for x in range(self.size):
                st = st + icon[y][x] + " "
            print(st)

    
        

b = Board(8)
px = b.cells[7][7].row
print(px)
