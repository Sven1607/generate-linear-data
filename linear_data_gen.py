import math
import random


class vector:
    def __init__(self, x_1=None, x_2=None, y_1=None, y_2=None, x_cept=None, y_cept=None, slope=None):
        self.x_1 = x_1
        self.x_2 = x_2
        self.y_1 = y_1
        self.y_2 = y_2
        self.y_cept = y_cept
        self.slope = slope

    def equation(self):
        def find_slope(x1, x2, y1, y2):
            if self.slope == None:
                change_x = x2-x1
                change_y = y2-y1
                slope = change_y/change_x
                return slope
            else:
                return self.slope
        line_slope = find_slope(self.x_1, self.x_2, self.y_1, self.y_2)   
        def find_y_cept(x1, x2, y1, y2):
            if self.y_cept is not None:
                b = self.y_cept

            else:
                line_slope = find_slope(self.x_1, self.x_2, self.y_1, self.y_2)
                cept_1 = line_slope*self.x_1
                b = cept_1 + self.y_1
            
            return b
        
        b = find_y_cept(self.x_1, self.x_2, self.y_1, self.y_2)

        equation = [line_slope, b]

        return equation
    
my_vector = vector(y_cept=0, slope=1/2)
#generate x

print(my_vector.slope)
def generate_x(d, r):
    if r == "below":
        x_below = []
        for i in range(d):
            x = random.randint(1, d)
            x_below.append(x)

        return x_below
    
    if r == "above":
        x_above = []
        for i in range(d):
            x = random.randint(1, d)
            x_above.append(x)
        return x_above
        
def generate_y(x_values, bound, r=None):
    if bound == "above":
        y_above = []
        for i in x_values:
            min = math.ceil(my_vector.slope*i)

            y = random.randint(min, r)
            y_above.append(y)
          

        return y_above
    if bound == "below":

        y_below = []
        try:
            for i in x_values:
                max = (my_vector.slope*i)
                max_f = int(max)
                y = random.randint(1, max_f)
                y_below.append(y)

        except ValueError:
            for i in x_values:
                max = (my_vector.slope*i)
                max_f = int(max)
                y = random.randint(1, max_f+1)
                y_below.append(y)
        
        
      
        return y_below

x_above = generate_x(12, "above")
x_below = generate_x(12, "below")
y_below = generate_y(x_below, "below")
y_above = generate_y(x_above, "above", r=12)

above_points=[]
below_points=[]

for i in zip(x_above, y_above):
    above_points.append(i)

for i in zip(x_below, y_below):
    below_points.append(i)
print(len(above_points))
print(len(below_points))
print(x_below)
print(x_above)
print(y_below)
print(y_above)

