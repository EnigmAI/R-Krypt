# function to display polybius cipher text
def polybiusCipher(s):
    # convert each character to its encrypted code
    for char in s:
        # finding row of the table
        row = int((ord(char) - ord('a')) / 5) + 1
        # finding column of the table
        col = ((ord(char) - ord('a')) % 5) + 1

        # if character is 'k'
        if char == 'k':
            row = row - 1
            col = 5 - col + 1
        # if character is greater than 'j'
        elif ord(char) >= ord('j'):
            if col == 1:
                col = 6
                row = row - 1
            col = col - 1

        print(row, col, end='', sep='')


if __name__ == "__main__":
    s = "dhruvgarg"
    polybiusCipher(s)
