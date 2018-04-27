#Shannon Lau
#SoftDev2 pd7
#K15 -- Do You Even List?
#2018-04-26

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"
SYMBOLS = ".?!&#,;:-_*"

def check_upper(pw):
    return len([i for i in pw if i in UPPER])

def check_lower(pw):
    return len([i for i in pw if i in LOWER])

def check_number(pw):
    return len([i for i in pw if i.isdigit()])

def check_symbol(pw):
    return len([i for i in pw if i in SYMBOLS])

def is_valid(pw):
    return check_upper(pw) > 0 and check_lower(pw) > 0 and check_number(pw) > 0

def rate(pw):
    score = 0
    if check_upper(pw) > 0:
        score += 2.5
    if check_lower(pw) > 0:
        score += 2.5
    if check_number(pw) > 0:
        score += 2.5
    if check_symbol(pw) > 0:
        score += 2.5
    return score

print is_valid("Bballlau11")
print is_valid("woo")

print rate("-4jS")
print rate("Hi!")
print rate("Hehe")
