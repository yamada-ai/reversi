# reversi
## それぞれのクラスの概要 
### Board
    オセロの盤面そのものを表すクラス
### Place 
    オセロの1マスを特定する為に使うクラス  
    AI の手の出力はこのクラスが使われる
### Cell
    オセロの1マスを表す使うクラス  
    そのマスの状態(黒か否か等)を保持している
### State
    AI が次の手を考える為に使うクラス  
    Board を継承している
### BasicAI
    AI を表すクラス  
    評価関数と State を用いて次の手を決める
### GameController
    オセロの進行をするクラス  
    ゲームの開始，終了はここで行われる
### Frame, MainFrame
    GUIの全てを司るクラス  
    オセロの流れを可視化したいなら使うべし．べしべし


- 2019/01/04 
    - AI 仕様で新たにファイルを作成(または更新)
        - boardAI.py
        - controllerAI.py
        - simpleAI.py(更新)
        - stateAI.py
    - GUI ではなく CLI 上で結果のみ表示できる仕様へ
        - これにより高速になる
        - 使用したい際は " python battleAI.py" を実行
        
    
