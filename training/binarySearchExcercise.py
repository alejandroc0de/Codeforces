A = [-3, -1, 0, 1, 4, 7]

# Traditional Binary Search - Looking up if number is in array:
# Time: O(log n)
# Space: O(1)

def binary_search(arr, target):
  N = len(arr)
  L = 0
  R = N - 1

  while L <= R:
    M = L + ((R-L) // 2)

    if arr[M] == target:
      return True
    elif target < arr[M]:
      R = M - 1
    else:
      L = M + 1
  return False

binary_search(A, 8)


# Condition based
B = [False, False, False, False, True]

def binary_search_condition(arr):
  N = len(arr)
  L = 0
  R = N - 1

  while L < R:
    M = (L + R) // 2

    if arr[M]:
      R = M
    else:
      L = M + 1

  return L

print(binary_search_condition(B)) 
#R:4 Aca empiezan los True, para eso es el algoritmo


# Range-Based
def check(x):
    return x * x >= 50  # condición a cumplir

L, R = 1, 100
ans = -1

while L <= R:
    M = (L + R) // 2
    if check(M):
        ans = M        # posible respuesta
        R = M - 1      # buscamos si hay uno menor que también cumpla
                       # Si cambiamos la condicion cambia entre - a + en R
    else:
        L = M + 1
print(ans) #R: 8