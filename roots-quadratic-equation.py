
print("To find the roots of a quadratic equation of the form ax^2 + bx + c, please input the values of a, b and c"
a = int(input("Input the value of a , a = "))
b = int(input("Input the value of b , b = "))
c = int(input("Input the value of c , c = "))

root1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
root2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
if root1!=root2:
   print("The roots of the equation  are", root1, root2)
else: print("The root of the equation is", root1)

