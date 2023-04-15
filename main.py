import random
import time


def BinarySearch(input_list: list[int], target: int) -> int:
    # Validate input_list for nullness
    assert input_list is not None, "input_list cannot be None"
    
    # Validate input_list for unexpected or malicious values
    if not isinstance(input_list, list) or not all(isinstance(x, int) for x in input_list):
        raise ValueError("input_list must be a list of integers")
    
    # Validate target for nullness
    assert target is not None, "target cannot be None"
    
    # Validate target for unexpected or malicious values
    if not isinstance(target, int):
        raise ValueError("target must be an integer")
    
    # Local variables
    left_index = 0
    right_index = len(input_list) - 1

    # Function loop
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        guess = input_list[middle_index]
        print(f'left_index is {left_index} and right_index is {right_index}. middle_index is {middle_index}, guess is {guess}. TARGET:{target}')
        if guess == target:
            print(f'Target found at index: {middle_index}')
        if guess > target:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    return None

def GenerateIntList(x: int, y: int) -> list[int]:
    return random.sample(range(1, y+1), x)

def main() -> None:
    start_time = time.time()
    int_list = GenerateIntList(6, 100)
    end_time = time.time()
    print(f'The list creation took {end_time - start_time} seconds')
    start_time = time.time()
    print(f'{int_list[3]}\n{int_list}') # temp
    BinarySearch(int_list, int_list[3])
    end_time = time.time()
    print(f'The search took {end_time - start_time} seconds')
    print(f'{int_list[3]}\n{int_list}') # temp

if __name__ == '__main__':
    main()