# Entry point for the math operations
from add import add
from sub import sub
from multiply import multiply

if __name__ == "__main__":
    print('Sum:', add(2, 3))
    print('Difference:', sub(5, 2))
    print('Product:', multiply(2, 3, 4, 5))
