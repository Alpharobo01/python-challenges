def factoriel (n: int)->int :
  if n > 0:
    result = 1
    for i in range(2, n + 1):
      result *= i
    return result
  elif n == 0 or n==1 :
    return 1
  else:
    return None
n = int(input("Enter n Value:"))
factoriel (n)
