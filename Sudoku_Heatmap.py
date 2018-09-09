"""
Created on Fri May 11 19:47:51 2018

@author: SamRolfe
"""

# Import Libraries
# =============================================================================
#
import numpy as np
import decimal
import matplotlib.pyplot as plt
from matplotlib import colors

#np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.0f}'.format})

# Load Data
# =============================================================================


easy_boards_file_location   = <file location>
medium_boards_file_location = <file location>
hard_boards_file_location   = <file location>
evil_boards_file_location   = <file location>

easy_boards   = np.genfromtxt(easy_boards_file_location, np.int64, delimiter = ",")
medium_boards = np.genfromtxt(medium_boards_file_location, np.int64, delimiter = ",")
hard_boards   = np.genfromtxt(hard_boards_file_location, np.int64, delimiter = ",")
evil_boards   = np.genfromtxt(evil_boards_file_location, np.int64, delimiter = ",")



# Data Structures
# =============================================================================


## Position is Interval[0:80]

## Values is Interval[0:9]

## Board is np.array[[ListOfValues]]

## Board Set is np.array[[ListOfBoards]]

## Frequency is Interval[0:1]
## interp. number of non-zeroes Values for a given Position / the total number 
## of Boards in the given Board Set

## Frequency Board is np.array[[ListOfFrequencies]]



# Functions
# =============================================================================

## Board Set, Board Set, Board Set, Board Set, -> Heat Map
def sudoku_heat_map(easy_set, medium_set, hard_set, evil_set):
    
    easy_frequency_board   = board_set_to_freq_board(easy_set)
    medium_frequency_board = board_set_to_freq_board(medium_set)
    hard_frequency_board   = board_set_to_freq_board(hard_set)
    evil_frequency_board   = board_set_to_freq_board(evil_set)
    
    min_max = min_max_frequency(easy_frequency_board, medium_frequency_board, hard_frequency_board, evil_frequency_board)

    reformatted_easy_board   = reformat_board(easy_frequency_board)
    reformatted_medium_board = reformat_board(medium_frequency_board)
    reformatted_hard_board   = reformat_board(hard_frequency_board)
    reformatted_evil_board   = reformat_board(evil_frequency_board)

    print("Clue Distribution by Difficulty")
    visualize_board(reformatted_easy_board, 'Easy',  min_max)
    visualize_board(reformatted_medium_board, 'Medium',  min_max)
    visualize_board(reformatted_hard_board, 'Hard', min_max)
    visualize_board(reformatted_evil_board, 'Evil', min_max)



## Board Set -> Board of Frequencies
## Given a Board Set, return a Frequency Board for the given Board Set 

def board_set_to_freq_board(board_set):
    num_of_boards = board_set.shape[0]
    total_clue_board = np.zeros(81)
    frequency_board = np.array([])
    
    for board in board_set:
        for position in range(board.shape[0]):
            if board[position] != 0:
                total_clue_board[position] += 1
    
#   print(reformat_board(total_clue_board))
    frequency_board = total_clue_board / num_of_boards
    return frequency_board



## Frequency Board, Frequency Board, Frequency Board, Frequency Board -> Tuple
## Given the frequency boards, returns a single min & max
def min_max_frequency(easy_board, medium_board, hard_board, evil_board):
    min_frequency = []
    min_frequency.append(easy_board.min())
    min_frequency.append(medium_board.min())
    min_frequency.append(hard_board.min())
    min_frequency.append(evil_board.min())
    
    max_frequency = []
    max_frequency.append(easy_board.max())
    max_frequency.append(medium_board.max())
    max_frequency.append(hard_board.max())
    max_frequency.append(evil_board.max())
                
    min_frequency = min(min_frequency)
    max_frequency = max(max_frequency)
    
    return (min_frequency, max_frequency)



## 81x1 Board -> 9x9 Board
## Given an 81 x 1 array, returns a 9x9 numpy array
    
def reformat_board(board):
    reformatted_board = board.reshape([9, 9])
    return(reformatted_board)
    
    
## Board, String, (real[0:1], real[0:1])
## Given board, title, and min/max, returns matplotlib heatmap visualization
def visualize_board(board, title, min_max_frequency):
    
    normalize_color_across_boards = colors.Normalize(min_max_frequency[0], min_max_frequency[1])
    plt.title(title)
    board_heatmap = plt.imshow(board, cmap='hot', norm = normalize_color_across_boards, interpolation='nearest')
    
    tick_list = tick_range(min_max_frequency)
    plt.colorbar(board_heatmap, ticks = tick_list)
    
    ## ax is axis object
    ax = plt.gca()
    ax.set_xticks([2.5, 5.5])
    ax.set_yticks([2.5, 5.5])
    ax.set_xticklabels(['', ''])
    ax.set_yticklabels(['', ''])
    ax.grid(color='black', linestyle='-', linewidth=2)
    
    plt.show()
    
    
    
def tick_range(min_max):
    difference = min_max[1] - min_max[0]
    space = round(difference / 9, 2)
    upper = round(min_max[1] - space, 2)
    lower = round(min_max[0] + space, 2)
    middle = round((min_max[1] + min_max[0]) / 2, 2)
    return [lower, middle, upper]
    
    
    
    
# =============================================================================
sudoku_heat_map(easy_boards, medium_boards, hard_boards, evil_boards)
# =============================================================================










