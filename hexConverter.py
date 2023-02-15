def nibble_to_ascii(nibble: int) -> str:
  table = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
  return table[nibble]


def to_bin(number: int) -> str:
    """
    This is a comment
    Input: Number (integer)
    Output: String
    Example: Input = 43605, Output = "0b1010101001010101"
    """
    answer = ""
    
    # Forever loop
    while True:
        # Integer divide using the // operator
        quotient = number // 16
        # Get the remainder using the % operator
        remainder = number % 16
        
        # Accumulate result
        answer = nibble_to_ascii(remainder) + answer

        # Set the number we need to use for next time
        number = quotient
        
        # We break the "loop" when division turns to zero
        if (quotient == 0):
            break
    
    return "0x" + answer

print(to_bin(123456789))
print(to_bin(0b1010101))
print(to_bin(0xDEADBEEF))

