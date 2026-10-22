# Task 01: Shopping Bill — GST First, Discount After

def calculateElectronicsGST(a, b):
    subtotal = a + b
    return subtotal + (subtotal * 18 / 100)


def calculateFashionGST(c, d):
    subtotal = c + d
    return subtotal + (subtotal * 13 / 100)


def calculateFoodGST(e):
    return e + (e * 7 / 100)


def totalBill(a, b, c, d, e):
    electronics_total = calculateElectronicsGST(a, b)
    fashion_total = calculateFashionGST(c, d)
    food_total = calculateFoodGST(e)
    return electronics_total + fashion_total + food_total


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount


if __name__ == "__main__":
    # Required sample values are passed directly; no input() is used.
    a, b, c, d, e = 100, 100, 100, 100, 100

    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_payable = calculateDiscountedBill(a, b, c, d, e)

    print(f"Electronics after 18% GST: Rs. {electronics:.2f}")
    print(f"Fashion after 13% GST:     Rs. {fashion:.2f}")
    print(f"Food after 7% GST:         Rs. {food:.2f}")
    print(f"Total after GST:           Rs. {total:.2f}")
    print(f"Discount (20%):            Rs. {discount:.2f}")
    print(f"Final payable amount:      Rs. {final_payable:.2f}")
