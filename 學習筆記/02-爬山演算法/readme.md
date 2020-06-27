# 爬山演算法介紹
爬山演算法是一種從隨機解開始找最佳解的演算法
```
Algorithm Hill-Climbing(pi)
  p = pi // 設定粒子 p 為起始粒子 pi
  while not isEnd()
    pn = move(p) //選擇粒子p的鄰居pn
    if pn.energy()<=p.energy() //能量更低，就接受
      p = pn;
End Algorithm
```
[1528880638-446495441_n.png](1528880638-446495441_n.png)
# 程式來源:
[老師的上課網站](http://ccckmit.wikidot.com/so:hillclimbing)<br>
[圖片來源](https://andy850701.pixnet.net/blog/post/463288544-%E5%95%9F%E7%99%BC%E5%BC%8F%E6%BC%94%E7%AE%97%E6%B3%95-%E2%80%93-%E7%88%AC%E5%B1%B1%E6%BC%94%E7%AE%97%E6%B3%95)
