# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 15:37:15 2022

@author: AhmedZ
"""


#%% Python Sorting Algorithm Visualizer Tutorial



import pygame
import random 
import math


pygame.init()

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255,99,71
    DRAW_COLOR = 0,191,255
    BG_COLOR = BLACK
    
    SIDE_PAD = 100
    TOP_PAD = 150
    PAD = 1
  
    
    FONT = pygame.font.SysFont('comicsans', 20)
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)
    
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Sorting Algorithm Visualizer')
        self.set_list(lst)
    
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        
        self.block_width = max(1,round((self.width - self.SIDE_PAD-(len(self.lst)-1)*self.PAD)/len(self.lst)))
        self.block_height = math.floor((self.height-self.TOP_PAD)/(self.max_val-self.min_val))
        self.start_x = self.SIDE_PAD // 2
        


def draw(draw_info, algo_name="Bubble Sort", ascending=None):
    
    draw_info.window.fill(draw_info.BG_COLOR) 
    direction_text = 'Sorting direction'
    if ascending is not None:
        direction_text = 'Ascending' if ascending else 'Descending'
    algo_info = draw_info.LARGE_FONT.render(f"{algo_name} - {f'{direction_text}' }", 1, draw_info.WHITE)
    
    text_ascend = "A - Ascending | D - Descending"
    text = "R - Reset | Start Sorting - SPACE"
    text_sorting = "I - Insertion Sort | B - Bubble Sort | S - Selection Sort"
    controls = draw_info.FONT.render(text, 1, draw_info.WHITE)
    direction = draw_info.FONT.render(text_ascend, 1, draw_info.WHITE)
    sorting = draw_info.FONT.render(text_sorting, 1, draw_info.WHITE)
    
    draw_info.window.blit(algo_info, (draw_info.width/2-algo_info.get_width()/2,5))
    
    draw_info.window.blit(sorting,(draw_info.width/2-sorting.get_width()/2,80))
    draw_info.window.blit(direction,(draw_info.width/2-direction.get_width()/2,55))
    draw_info.window.blit(controls,(draw_info.width/2-controls.get_width()/2,105))
    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg = False):
    
    if clear_bg:
        clear_rect = (0, draw_info.TOP_PAD, 
                      draw_info.width,draw_info.height-draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BG_COLOR,clear_rect)
    lst = draw_info.lst
    for i, val in enumerate(lst):
        x = draw_info.start_x+i*draw_info.block_width+i*draw_info.PAD
        y = draw_info.height-(val-draw_info.min_val)*draw_info.block_height-draw_info.SIDE_PAD//2
        
        color = draw_info.DRAW_COLOR
        if i in color_positions:
            color = color_positions[i]
        pygame.draw.rect(draw_info.window, color, (x,y, draw_info.block_width, draw_info.height))
    
    if clear_bg:
        pygame.display.update()
    
    
    
    
    
def generate_starting_list(n, min_val, max_val):
    lst = []
    
    for x in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    
    return lst

def Swap(array,i,j):
    array[i], array[j] = array[j], array[i]
    
    return array
      
def bubbleSort(draw_info,ascending = True):
    array = draw_info.lst
    isSorted = False
    
    while not isSorted:
        count = 0
        for i in range(len(array)-1):
            if (array[i+1] < array[i] and ascending) or (array[i+1] > array[i] and not ascending) :
                array = Swap(array,i,i+1)
                count +=1 
                draw_list(draw_info, {i: draw_info.GREEN, i+1: draw_info.RED }, True)
                yield True
        if count == 0:
            isSorted = True
            
    return array

def insertionSort(draw_info,ascending = True):
    array = draw_info.lst
    
    for i in range(1, len(array)):
        current = array[i]
        while True:
            ascending_sort = i > 0 and array[i-1] > current and ascending
            descending_sort = i > 0 and array[i-1] < current and not ascending
    
            if not ascending_sort and not descending_sort:
                break
            
            array = Swap(array,i,i-1)
            i = i-1
            draw_list(draw_info, {i: draw_info.GREEN, i-1: draw_info.RED }, True)
            yield True
        
                
    return array

def selectionSort(draw_info,ascending = True):
    array = draw_info.lst
    
    sort = False
    while not sort:
        count = 0
        for i in range(len(array)):
            curmin = float("inf")
            for j in range(i+1,len(array)):
                curmin = min(curmin, array[j])
                if (curmin == array[j] and curmin < array[i] and ascending) or (curmin == array[j] and curmin > array[i] and not ascending):
                    Swap(array,i,j)
                    draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED }, True)
                    count +=1
                    yield True
                else:
                    yield True
                    break

        if count == 0:
            sort = True
    return array




    
    
    

def main():
    run = True
    clock = pygame.time.Clock()
    fps = 20
    n = 50
    min_val = 1
    max_val = 100
    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(max(1000,n*2), 600, lst)
    
    sorting = False
    ascending = None  
    sorting_algorithm = None
    sorting_algo_name = None
    sorting_algorithm_generator = None
    
    algorithms = [bubbleSort, insertionSort,selectionSort]
    algorithms_name = ["Bubble Sort", "Insertion Sort", "Selection Sort"]
    
    algorithm_dict = {}
    for i in range(len(algorithms)):
        algorithm_dict[f'{algorithms_name[i][0].lower()}'] =  (algorithms[i],algorithms_name[i]) 
                 
    sorting_algo_name='Choose Algorithm'
    
    
    
  
    while run:
        # clock.tick(fps)
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info,sorting_algo_name , ascending)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type != pygame.KEYDOWN:
                continue
            
            if event.key == pygame.K_i and not sorting:
                sorting_algorithm, sorting_algo_name =algorithm_dict['i']
                draw(draw_info, sorting_algo_name, ascending)
                
            if event.key == pygame.K_b and not sorting:
                sorting_algorithm, sorting_algo_name =algorithm_dict['b']
                draw(draw_info, sorting_algo_name, ascending)
                
            if event.key == pygame.K_s and not sorting:
                sorting_algorithm, sorting_algo_name =algorithm_dict['s']
                draw(draw_info, sorting_algo_name, ascending)
                
                
            if event.key == pygame.K_r and not sorting:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
        
            if event.key == pygame.K_a:
                ascending = True
                draw(draw_info, sorting_algo_name, ascending)
          
            if event.key == pygame.K_d:
                ascending = False
                draw(draw_info, sorting_algo_name, ascending)
                
            if event.key == pygame.K_SPACE and ascending is not None and sorting_algo_name is not None:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                
                
                
    
    pygame.quit()
    
    
if __name__ == "__main__":
    main()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        