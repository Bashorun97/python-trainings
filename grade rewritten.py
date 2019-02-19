print('Enter a value between 0.0 an 1.0 to determine the corresponding grade')

score = float(input('Enter score: '))
msg = ''
def computegrade(score):
    if score >= 0.90 and score <=1.00:
        msg = 'A'
    elif score >= 0.80 and score <=0.89:
        msg =  'B'
    elif score >= 0.70 and score <= 0.79:
        msg =  'C'
    elif score >= 0.60 and score <= 0.69:
        msg =  'D'
    elif score <= 0.59:
        msg =  'F'
    else:
        msg =  'Bad score'
    print(msg)
    
computegrade(score)
