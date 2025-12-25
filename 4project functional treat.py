data_list = []
summary = {}

def input_data():
    """Input 1D list data from user"""
    global data_list
    data_list = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Data stored successfully")

def built_in_summary():
    """Display summary using built-in functions"""
    if not data_list:
        print("No data available")
        return

    print("Total elements:", len(data_list))
    print("Minimum value:", min(data_list))
    print("Maximum value:", max(data_list))
    print("Sum of values:", sum(data_list))
    print("Average value:", round(sum(data_list)/len(data_list), 2))

def factorial(n):
    """Calculate factorial using recursion"""
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

def filter_data():
    """Filter data using lambda function"""
    if not data_list:
        print("No data available")
        return

    threshold = int(input("Enter threshold value: "))
    result = list(filter(lambda x: x >= threshold, data_list))
    print("Filtered data:", result)

def sort_data():
    """Sort data in ascending or descending order"""
    if not data_list:
        print("No data available")
        return

    print("1. Ascending")
    print("2. Descending")
    choice = input("Enter choice: ")

    if choice == "1":
        data_list.sort()
        print("Ascending Order:", data_list)
    elif choice == "2":
        data_list.sort(reverse=True)
        print("Descending Order:", data_list)

def return_multiple():
    """Return multiple statistics"""
    minimum = min(data_list)
    maximum = max(data_list)
    total = sum(data_list)
    average = round(total / len(data_list), 2)
    return minimum, maximum, total, average

def args_demo(*args):
    """Display values using *args"""
    print("Values using *args:", args)

def kwargs_demo(**kwargs):
    """Display key-value pairs using **kwargs"""
    print("Dataset Summary:")
    for k, v in kwargs.items():
        print(k, ":", v)

while True:
    print("\n- Data Analyzer Menu -")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data (Lambda)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        input_data()

    elif choice == "2":
        built_in_summary()

    elif choice == "3":
        num = int(input("Enter number: "))
        print("Factorial:", factorial(num))

    elif choice == "4":
        filter_data()

    elif choice == "5":
        sort_data()

    elif choice == "6":
        if not data_list:
            print("No data available")
        else:
            min_val, max_val, total, avg = return_multiple()
            args_demo(min_val, max_val, total, avg)
            kwargs_demo(Minimum=min_val, Maximum=max_val, Sum=total, Average=avg)

    elif choice == "7":
        print("Thank you Program ended")
        break

    else:
        print("Invalid choice")
