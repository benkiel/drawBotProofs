def drawSpacing(font, leftMargin, rightMargin, topMargin, bottomMargin, fontSize, lineHeight):
  gutter = 50
  
  if isinstance(font, RFont):
    fn = font.testInstall()
  else:
    fn = font
    
  uc = "HOH%sHO%sOHO"
  lc = "non%sno%sono"

  glyphs = font.keys()
  glyphs.sort()
  
  t = FormattedString()
  t.font(fn)
  t.fontSize(24)
  t.lineHeight(40)
  
  for name in glyphs:
      if name.isupper():
          t.appendGlyph("H", "O", "H", name, "H", "O", name, "O", "H", "O")
          t += "\n"
      if name.islower():
          t.appendGlyph("n", "o", "n", name, "n", "o", name, "o", "n", "o")
          t += "\n"
          
  max_width = t.size().width
  
  orgin = leftMargin
  overflow = textBox(t, (orgin, bottomMargin, int(max_width + 1), height()-(bottomMargin + topMargin)))
  orgin = leftMargin + max_width + gutter
  
  over = len(overflow)
  
  while over > 0:
    print over
    if orgin + max_width > width() - rightMargin:
      newPage()
      orgin = (leftMargin, bottomMargin)
    overflow = textBox(overflow, (orgin, bottomMargin, int(max_width + 1), height()-(bottomMargin + topMargin)))
    over = len(overflow)
    orgin = orgin + max_width + gutter
    
      
size(1000,2000)
drawSpacing(CurrentFont(), 50, 50, 100, 100, 24, 40)