# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jonathon Foltyn
#               Justin Smonko
#               Vedanti Naktode
#               sutton Elliot
# Section:      504
# Assignment:   Team Lab 9
# Date:         11/2/2022

#define function getpoints 
def getpoints(points):
    points_list = points.split()
    for i in range(len(points_list)):
        points_list[i]= points_list[i].split(',')
    for eachlist in points_list:
        index=0
        for num in eachlist:
            eachlist[index] = int(eachlist[index])
            index += 1
    return points_list

#def cross(a,b):
def cross(point1, point2):
    cross_section= (point1[0] * point2[1]) - (point1[1] * point2[0])
    return cross_section
    
#def shoelace():
def shoelace(points):
    area = 0 
    for i in range(len(points) - 1):
        area += cross(points[i], points[i + 1])
    area += cross(points [-1], points[0])
    area /= 2
    return area

#define main function
def main():
    string= input("Please enter the vertices: ")
    user_list= getpoints(string)   
    poly_area = shoelace(user_list)
    print(f'The area of the polygon is {poly_area:.1f}')
    
if __name__ == '__main__':
    main()
