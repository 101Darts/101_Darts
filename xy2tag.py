import math

class xy2tag:
    def get_score(self, x_cm, y_cm): 
        rr=math.sqrt(x_cm**2 + y_cm**2)
        if rr < 0.9:
            return "DBE"
        elif rr < 2.1:
            return "BE"

        num = self.get_right_num(x_cm, y_cm)
        
        if 2.1< rr < 10.1:
            return "A" + num
        if 10.1< rr < 12.1:
            return "T" + num
        if 12.1< rr < 17.3:
            return "B" + num
        if 17.3< rr < 19.1:
            return "D" + num
				
        return "MISSED"

    def get_right_num(self, x_cm, y_cm):  
        felder = [3, 19, 7, 16, 8, 11, 14, 9, 12, 5, 20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3]
        alpha = math.atan2(x_cm, y_cm) / math.pi * 180
        alpha += 180 + 9
        index = int(alpha / 18)
        return str(felder[index])

#x_input_cm = float(input("Enter the x-coordinate in centimeters: ")) 
#y_input_cm = float(input("Enter the y-coordinate in centimeters: "))


#xy2tag_instance = xy2tag()

#print(xy2tag_instance.get_score(x_input_cm, y_input_cm))