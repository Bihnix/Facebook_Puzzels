# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
  ans=[]
  for char in C:
    if char == "A":
      ans.append(char.replace("A","B"))
    elif char != "A":
      ans.append(char.replace("B","A"))

  return ''.join(ans)
