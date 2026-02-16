from pygame import Rect

def draw_text_block(surface, text, font, rect=Rect(30, 610, 735, 180), color=(0,0,0), line_spacing=2):
    
    words = text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        test_line = current_line + (' ' if current_line != '' else '') + word
        if font[0].size(test_line)[0] <= rect.width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    y = rect.y
    for line in lines:
        line_surface = font[0].render(line, True, color)
        if y + line_surface.get_height() > rect.y + rect.height:
            break  
        surface.blit(line_surface, (rect.x, y))
        y += line_surface.get_height() + line_spacing