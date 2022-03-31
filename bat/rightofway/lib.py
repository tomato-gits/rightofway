ROW_MESSAGE = "party {} has right-of-way"

def report_row(A, B):
    row = 'A' if A>B else 'B'
    return ROW_MESSAGE.format(row)