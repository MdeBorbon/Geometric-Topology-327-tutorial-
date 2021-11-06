#e.g. [[1,4,2,5],[3,6,4,1],[5,2,6,3]]
PD = input('Enter PD code:')

#python takes the input as a string, to make it a list we introduce the following two lines
import ast
PD = ast.literal_eval(PD)

writhe = 0

for c in PD:
    sign = (c[1]-c[3]) % (2*len(PD)) #sign is a positive integer from 1 to 2(number of crossings) -1
    if sign == 2*len(PD) -1:
        sign = -1
    writhe = writhe + sign

print('the writhe is', writhe)
