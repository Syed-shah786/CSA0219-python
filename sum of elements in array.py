def main():
    
    array = input("Enter the array elements separated by space: ").split()

    array = [int(x) for x in array]
    
    sum_result = sum(array)


    print("Sum of elements:", sum_result)

if __name__ == "__main__":
    main()
