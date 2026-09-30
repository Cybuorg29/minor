import random

def generate_palette(n): 
    palette = [] 
    for i in range(n): 
        rgb = [] 
        for j in range(3): 
            rgb.append(random.randint(1, 255)) 
        palette.append(rgb) 
          
    return palette

if __name__ == "__main__": 
    n = 10
    palette = generate_palette(n) 
    print(palette)