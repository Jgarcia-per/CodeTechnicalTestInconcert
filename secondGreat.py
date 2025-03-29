def second_great(list):
    if len(list) < 2:
        return None 

    first = second = float('-inf')

    for number in list:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number

    return second if second != float('-inf') else None

# Ejemplos de uso
print(second_great([10, 5, 8, 20]))
print(second_great([1, 2]))
print(second_great([5]))        
print(second_great([7, 7, 7]))
