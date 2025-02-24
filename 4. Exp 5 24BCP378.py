for i in range(1,31,1): 

  for j in range(1,31,1): 

    c=((i*i + j*j)**0.5) 

  if c==int(c): 

   print((i,j,c)) 