def front_back(str):
  if len(str) <=1:
    return str
  
  startletter = str[0]
  endletter = str[-1]
  middle = str[1:-1]
  return endletter + middle + startletter