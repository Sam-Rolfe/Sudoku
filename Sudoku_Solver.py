#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 17:23:35 2018

@author: SamRolfe
"""



## Imports unsolved sudoku boards. Boards separated by line breaks, numbers 
## separated by commas. Exports solved boards as lists of comma separated 
## integers



## Content
# =============================================================================
# 1. Import libraries, file names, global Variables
# 2. Sudoku Templates
# 3. Sudoku solver
# 4. Top Level Functions
# 5. Solver Helpers
# 6. Solver Performace 
# 7. Run File
# =============================================================================






## 1. Import libraries, file names, global Variables
# =============================================================================

from random import *
import time

start = time.time()


input_data_file = <file_location>
output_data_file = <file_location>



## Global Variables
board_length = 81
number_of_rows = 9
number_of_columns = 9

total_boards = len(unsolved_boards)
valid_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]




## 2. Sudoku Templates
## =============================================================================

rows =    [[0,  1,  2,  3,  4,  5,  6,  7,  8],
           [9,  10, 11, 12, 13, 14, 15, 16, 17],
           [18, 19, 20, 21, 22, 23, 24, 25, 26],
           [27, 28, 29, 30, 31, 32, 33, 34, 35],
           [36, 37, 38, 39, 40, 41, 42, 43, 44],
           [45, 46, 47, 48, 49, 50, 51, 52, 53],
           [54, 55, 56, 57, 58, 59, 60, 61, 62],
           [63, 64, 65, 66, 67, 68, 69, 70, 71],
           [72, 73, 74, 75, 76, 77, 78, 79, 80]]

columns = [[0,  9, 18, 27, 36, 45, 54, 63, 72],
           [1, 10, 19, 28, 37, 46, 55, 64, 73],
           [2, 11, 20, 29, 38, 47, 56, 65, 74],
           [3, 12, 21, 30, 39, 48, 57, 66, 75],
           [4, 13, 22, 31, 40, 49, 58, 67, 76],
           [5, 14, 23, 32, 41, 50, 59, 68, 77],
           [6, 15, 24, 33, 42, 51, 60, 69, 78],
           [7, 16, 25, 34, 43, 52, 61, 70, 79],
           [8, 17, 26, 35, 44, 53, 62, 71, 80]]

units =   [[0,   1,  2,  9, 10, 11, 18, 19, 20],
           [3,   4,  5, 12, 13, 14, 21, 22, 23],
           [6,   7,  8, 15, 16, 17, 24, 25, 26],
           [27, 28, 29, 36, 37, 38, 45, 46, 47],
           [30, 31, 32, 39, 40, 41, 48, 49, 50],
           [33, 34, 35, 42, 43, 44, 51, 52, 53],
           [54, 55, 56, 63, 64, 65, 72, 73, 74],
           [57, 58, 59, 66, 67, 68, 75, 76, 77],
           [60, 61, 62, 69, 70, 71, 78, 79, 80]]


## = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 

unsolved_board =   [0, 4, 0, 1, 0, 0, 0, 5, 0, 
                    1, 0, 7, 0, 0, 3, 9, 6, 0, 
                    5, 2, 0, 0, 0, 8, 0, 0, 0, 
                    9, 0, 0, 0, 0, 0, 0, 1, 7, 
                    0, 0, 0, 9, 0, 6, 8, 0, 0, 
                    8, 0, 3, 0, 5, 0, 6, 2, 0, 
                    0, 9, 0, 0, 6, 0, 5, 4, 3, 
                    6, 0, 0, 0, 8, 0, 7, 0, 0, 
                    2, 5, 0, 0, 9, 7, 1, 0, 0]

solved_board =     [3, 4, 6, 1, 7, 9, 2, 5, 8, 
                    1, 8, 7, 5, 2, 3, 9, 6, 4, 
                    5, 2, 9, 6, 4, 8, 3, 7, 1, 
                    9, 6, 5, 8, 3, 2, 4, 1, 7, 
                    4, 7, 2, 9, 1, 6, 8, 3, 5, 
                    8, 1, 3, 7, 5, 4, 6, 2, 9, 
                    7, 9, 8, 2, 6, 1, 5, 4, 3, 
                    6, 3, 1, 4, 8, 5, 7, 9, 2, 
                    2, 5, 4, 3, 9, 7, 1, 8, 6]


## 3. Sudoku Solver
# =============================================================================

## Given file location of unsolved boards, solves each board and exports to
## file location

def sudoku_solver(input_data_file, output_data_file):
    unsolved_boards = import_data(input_data_file)
    solved_boards = []
    
    print("\nSolving ", total_boards, " boards...\n")
    
    for board in range(len(unsolved_boards)):
        solved_boards.append(solver(unsolved_boards[board]))
        print("Completed board number: ", board + 1)
    
    export_data(solved_boards, output_data_file)
    print_metrics(solved_boards)



## 4. Top Level Functions
# =============================================================================

## Board -> Board or Boolean
## returns solved Board is solvable, else False

def solver(board):
    def solve_board(board):
        if solved(board):
            return board        
        else:
            return solve_list_of_boards(create_sub_boards(board))
        
    def solve_list_of_boards(sub_boards):
        if len(sub_boards) == 0:
            return False
        else:
            solved_board = solve_board(sub_boards[0])
            if solved_board:
                return solved_board
            else:
                return solve_list_of_boards(sub_boards[1:])
            
    return solve_board(board)


## DataFile -> List of Boards
## Returns list of unsolved boards given file location
    
def import_data(input_data_file):
    unsolved_boards = []
    with open(input_data_file) as inputfile:
        for line in inputfile:
            unsolved_board = []
            string_board = (line.strip().split(','))
            for position in string_board:
                unsolved_board.append(int(position))
            unsolved_boards.append(unsolved_board)
    return unsolved_boards



## Exports list of solved boards given solved board and file location
    
def export_data(solved_boards, output_data_file):
    with open(output_data_file, "w") as output:
        for i in solved_boards:
            output.write(str(i))
            output.write("\n")


 

## 5. Solver Helpers
# =============================================================================

## Board -> Boolean
## returns True if board has unsolved positions, else False
def solved(board):
    for i in range(board_length):
        if board[i] == 0:
            return False
    return True



## Board -> List of Boards
## Given a board, creates list of valid sub-boards based on first empty position. 
## If no valid sub_boards exist, return empty list
## ASSUME always given unsolved board, if no valid sub_boards return empty list
def create_sub_boards(board):
    first_empty = find_first_empty_position(board)
    valid_inputs = list_of_valid_inputs(first_empty, board)
    if (len(valid_inputs) == 0):
        return []
    else:
        sub_boards = create_list_of_sub_boards(first_empty, valid_inputs, board)
        return sub_boards



## ListofIntegers, Board -> ListofBoard
## Given a position, list of valid inputs, and board, returns list of Boards
## with position filled by valid inputs. If valid inputs empty, return empty list
def create_list_of_sub_boards(position, valid_inputs, board):
    sub_boards = []
    for i in valid_inputs:
        board_copy = board.copy()
        board_copy[position] = i
        sub_boards.append(board_copy)
    return sub_boards



## Board -> Position
## Returns position of first unsolved
## ASSUME always given unsolved board
def find_first_empty_position(board):
    for i in range(board_length):
        if board[i] == 0:
            return i
    return False




## 5a. list_of_valid_inputs() and Helpers
## = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =  

## Position, Board -> List of Integers
## Given a position and a board, returns list of valid inputs or empty list if none exist
## ASSUME always given board and position of empty space
def list_of_valid_inputs(position, board):
    inputs = []
    for i in valid_inputs:
        if (check_row(position, board, i) and check_column(position, board, i) and check_unit(position, board, i)):
            inputs.append(i)
    return inputs
        
    

## Position, Board, Value -> Boolean
## Returns True if input is valid based on row, else False
def check_row(position, board, value):
    row = position_to_row(position)
    row_positions = row_to_list_of_row_positions(row)
    row_values = list_of_positions_to_list_of_values(row_positions, board)
    if value not in row_values:
        return True
    else:
        return False
    


## Position, Board, Value -> Boolean
## Returns True if input is valid based on column, else False
def check_column(position, board, value):
    column = position_to_column(position)
    column_positions = column_to_list_of_column_positions(column)
    column_values = list_of_positions_to_list_of_values(column_positions, board)
    if value not in column_values:
        return True
    else:
        return False



## Position, Board, Value -> Boolean
## Returns True if input is valid based on column, else False
def check_unit(position, board, value):
    unit = position_to_unit(position)
    unit_positions = unit_to_list_of_unit_positions(unit)
    unit_values = list_of_positions_to_list_of_values(unit_positions, board)
    if value not in unit_values:
        return True
    else:
        return False



## Position -> Row
## Given position, returns row number
def position_to_row(position):
    return position // 9



## Row -> ListofIntegers
def row_to_list_of_row_positions(row):
    return rows[row]



## Position -> Column
## Given position, returns column number
def position_to_column(position):
    return position % 9



## Column -> ListofIntegers
def column_to_list_of_column_positions(column):
    return columns[column]



## Position -> Unit
## Given position, returns unit number
def position_to_unit(position):
    row = position_to_row(position)
    column = position_to_column(position)
    if row < 3:
        if column < 3:
            return 0
        if column < 6:
            return 1
        else:
            return 2
    if row < 6:
        if column < 3:
            return 3
        if column < 6:
            return 4
        else:
            return 5
    else:
        if column < 3:
            return 6
        if column < 6:
            return 7
        else:
            return 8



## Unit -> ListofIntegers
## Given unit, return list of positions in unit
def unit_to_list_of_unit_positions(unit):
    return units[unit]


## List Of Positions -> List Of Integers
## Given list of positions, returns list of values
def list_of_positions_to_list_of_values(positions, board):
    list_of_values = []
    for i in positions:
        list_of_values.append(board[i])
    return list_of_values


        

# 5. Solver Performace:
# =============================================================================

def return_time():
    end = time.time()
    return (end - start)


def print_metrics(list_initial_clue_positions):
    time = return_time()
    time_per_board = time / total_boards
    
    print("")
    print("===================================")
    print("")
    
    print("Boards solved: ", total_boards)
    print("Time: ", time)
    print("Time per Board: ", time_per_board)
    
    print("")
    print("===================================")
    print("")


#6. Run File 
# =============================================================================
sudoku_solver(input_data_file, output_data_file)
# =============================================================================









