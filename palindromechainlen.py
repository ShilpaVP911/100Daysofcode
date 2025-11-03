def palindrome_steps(num, steps=0):
    rev = int(str(num)[::-1])

    if num == rev:
        print(f"{num} is a palindrome after {steps} step(s).")
        return steps
    else:
        new_num = num + rev
        return palindrome_steps(new_num, steps + 1)


# Example run
n1 = int(input("Enter a number: "))
palindrome_steps(n1)
