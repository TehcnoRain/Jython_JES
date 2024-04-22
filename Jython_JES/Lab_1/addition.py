def addition(x, y):
 z= x+ y
 sub = x - y
 mul= x*y
 div = x/y
 print z

def equation(x):
  result = x * x + x + 1
  print result

def pickAndShow():
  file = pickAFile()
  pic = makePicture(file)
  show(pic)
  
def pickAndPlay():
  file = pickAFile()
  sound = makeSound(file)
  play(sound)
