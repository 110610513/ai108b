# 爬山演算法介紹
爬山演算法是一種從隨機解開始找最佳解的演算法

Algorithm Hill-Climbing(pi)
  p = pi // 設定粒子 p 為起始粒子 pi
  while not isEnd()
    pn = move(p) //選擇粒子p的鄰居pn
    if pn.energy()<=p.energy() //能量更低，就接受
      p = pn;
End Algorithm

程式來源:
[老師的上課網站](http://ccckmit.wikidot.com/so:hillclimbing)
