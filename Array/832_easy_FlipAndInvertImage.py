# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'Array'))
    print(os.getcwd())
except:
    pass

# %%
# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。

# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

# 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

# 示例 1:

# 输入: [[1,1,0],[1,0,1],[0,0,0]]
# 输出: [[1,0,0],[0,1,0],[1,1,1]]
# 解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
#      然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
# 示例 2:

# 输入: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# 输出: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 解释: 首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
#      然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 说明:

# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1


# %%
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        A = list(map(lambda x: list(map(lambda y: 1-y, x)),
                     list(map(lambda x: x[::-1], A))))
        return A


# %%
A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]


# %%
s = Solution()
print(s.flipAndInvertImage(A))
