---
title: "矩陣對角化運算"
date: 2023-01-10T16:36:36+08:00
draft: false
---
### 矩陣相乘求 A 的 n 次方的時間複雜度是多少？

對於 M x M 的矩陣的每一個元素，都要花費一列乘一行，共 M 次的乘法才能獲得，因此矩陣乘法時間複雜度為$O(M^3)$，對於 A 的 n 次方，共要 n-1 次矩陣乘法才能完成，因此求 A 的 n 次方的時間複雜度是$O(N \times M^3)$

### diagonalization 的方法時間複雜度是多少？

將 M x M 對角矩陣 D 相乘要 M 次乘法，而求 D 的 n 次方需要把 D 相乘 n-1 次。再加上 和 P 以及 P^-1 相乘需要兩次矩陣乘法
因此時間複雜度為 $O(N\times M + 2\times M^3)$

### 使用對角化求矩陣的 n 次冪，節省了多少次乘法運算？

藉由兩者的時間複雜度可以大略估算節省了$N\times M^2 - 2\times M^3$次乘法運算。當 n 越大，節省的計算量越多。

### 為什麼 P 是由 eigenvector 構成的 invertible matrix 時，得到的 similar matrix 是 diagonal matrix？

$A = PDP^{-1}$ 可以視為將 A 轉換到其 eigenvectors 的 basis 上，由於$Ax = \lambda x$，轉換後 A 只剩下係數積乘以$x$，係數積的部分可以寫成乘以對角線矩陣的形式。



