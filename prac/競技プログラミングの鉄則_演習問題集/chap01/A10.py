# 2025-09-23
N = int(input())
A = list(map(int, input().split()))
D = int(input())

# 左右からそれぞれ見た最大を保存する
P = [None] * N
P[0] = A[0]
for i in range(1, N):
  P[i] = max(P[i-1], A[i])

Q = [None] * N
Q[N-1] = A[N-1]
for i in range(N-2, -1, -1):
  Q[i] = max(Q[i+1], A[i])
  
# ans
for _ in range(D):
  L, R = map(int, input().split())
  ans = max(P[L-1-1], Q[R-1+1])
  print(ans)