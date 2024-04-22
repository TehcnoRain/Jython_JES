def copyPicToCanvas(xStart, yStart):
  canvas = makeEmptyPicture(750, 750)
  pic = makePicture(pickAFile()) #Pick a small picture!
  for x in range(getWidth(pic)):
    for y in range(getHeight(pic)):
      p = getPixel(pic, x, y)
      canvasP = getPixel(canvas, x+xStart, y+yStart)
      colour = getColor(p)
      setColor(canvasP,colour)
  addText(canvas,50,50,"Hellow World", red)
  addLine(canvas,50,60,130,60,blue)
  #addTextWithStyles()
  setColor(canvasP, colour)
  show(canvas)
  return canvas  
  
def rotateSideways(file,picture):
  file = pickAFile()
  picture = makePicture(file)
  show(picture)
  canvas = makeEmptyPicture(getHeight(picture), getWidth(picture))
  targetX = 0
  width = getWidth(picture)
  for sourceX in range(getWidth(picture)):
    targetY = 0
    for sourceY in range(getHeight(picture)):
      colour = getColor(getPixel(picture, sourceX, sourceY))
      setColor(getPixel(canvas,targetY,targetX),colour)
      targetY = targetY + 1
    targetX = targetX + 1
  show(canvas)
  
def randomLines(width, height, minLines, maxLines): 
    import random
    canvas = makeEmptyPicture(width, height, black)
    longest = 0
    numLines = random.randrange(minLines, maxLines+1)
    # random.randrange: Chooses a random item 
    #  from range(start, stop[, step])
    for line in range(1, numLines + 1):
      startX = random.randrange(width) 
      startY = random.randrange(height)
      endX = random.randrange(width)
      endY = random.randrange(height)
      myRed = random.randrange(256)
      myGreen = random.randrange(256)
      myBlue = random.randrange(256)
      myColour = makeColor(myRed, myGreen, myBlue) #A random colour!
      length = sqrt((startX - endX)**2 + (startY - endY)**2)
      # Note the similarity to the distance function!
      #  Just copy the 'math', don't question it!!
      addLine(canvas, startX, startY, endX, endY, myColour)
      # Click on addLine and then click the Explain button below
      #  for the context-sensitive help
      if length > longest:
        longest = length
    outputString = "Total number of lines: " + str(numLines)
    addText(canvas, (width/2-45), 15, outputString, white)
    # Click on addText and then click the Explain addText button
    outputString = "Longest line is: " + str(int(longest)) + " pixels"
    addText(canvas, (width/2-45), 30, outputString, white)
    show(canvas)