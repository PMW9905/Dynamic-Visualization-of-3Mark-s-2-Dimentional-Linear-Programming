from halfspace import Constraint, Objective
import random
import itertools
from manim import *

class DynamicLP(Scene):
    
    def construct(self):

        #axes = Axes((-10,10),(-10,10))
        axes = NumberPlane(x_range=[-10,10],y_range=[-10,10],background_line_style={"stroke_opacity": 0.4})
        self.play(Write(axes))

        
        #input the objective vector
        c1, c2 = tuple(input("Please provide the objective vector in the following format: c1 c2: ").split(" "))
        objective_vector = Objective(float(c1),float(c2))
        objective_vector.printVector()
        #loop to input the contraint vectors
        number_of_constraints = int(input("Please provide the number of constraints: "))
        if number_of_constraints < 2:
            print("number of constraints must be greater than 2. Exiting...")
            quit()
        constraint_vectors = []

        boundary_opacity = .5 * (1/number_of_constraints)

        #Requesting user-given constraints
        print("Please provide your constraint vectors in the following format: c1 c2 b")
        for i in range(number_of_constraints):
            c1, c2, b = tuple(input("Vector "+str((i+1))+": ").split(" "))
            constraint_vectors.append(Constraint(float(c1),float(c2),float(b)))

        for cv in constraint_vectors:
            cv.printVector()

        #shuffling the constraint vector list
        random.shuffle(constraint_vectors)

        #list containing in-play half spaces.
        h = []
        p = None

        #find 2 feasable vectors & create point.
        for v1, v2 in itertools.combinations(constraint_vectors, 2):
            #find intersection
            p = v1.getIntersection(v2)

            #testing vector 1 bounds
            test_p = (p[0]+10,v2.getY(p[0]+10))
            if not v1.isInHalfspace(test_p):
                test_p = (p[0]-10,v2.getY(p[0]-10))
            if objective_vector.evaluatePoint(test_p) > objective_vector.evaluatePoint(p):
                continue #out of bounds

            #testing vector 2 bounds
            test_p = (p[0]+10,v1.getY(p[0]+10))
            if not v2.isInHalfspace(test_p):
                test_p = (p[0]-10,v1.getY(p[0]-10))
            if objective_vector.evaluatePoint(test_p) > objective_vector.evaluatePoint(p):
                continue #out of bounds
            h.append(v1)
            constraint_vectors.remove(v1)
            h.append(v2)
            constraint_vectors.remove(v2)
            break

        if len(h)>0:
            print("A pair was found.")
        else:
            print("A pair was not found. This means that the solution is unbound or invalid.")
            quit()
        #printing the 2 starting constraints
        #also print the halfspaces
        for h_i in h:
            line = axes.plot(lambda x: (h_i.b - h_i.c1*x) / h_i.c2, color=BLUE_C)
            self.play(Write(line))
            if h_i.isFacingLeft():
                triangle_coordinates = [(h_i.getX(10),10,0),(h_i.getX(-10),-10,0),(-100,0,0)]
            else:
                triangle_coordinates = [(h_i.getX(10),10,0),(h_i.getX(-10),-10,0),(100,0,0)]

            triangle = Polygon(fill_color = BLUE, fill_opacity = boundary_opacity, *triangle_coordinates)
            self.play(Write(triangle))

        #p = current point that maximizes objective function
        #h = current halfspaces being consitered 
        #h_i = next halfspace
        #be sure to convert all of this code into its own independent file w/ functions
        point_visual = Dot(axes.coords_to_point(p[0],p[1]), color = RED)
        self.play(Write(point_visual))

        for h_i in constraint_vectors:
            line = axes.plot(lambda x: (h_i.b - h_i.c1*x) / h_i.c2, color=BLUE_C)
            self.play(Write(line))
            if h_i.isFacingLeft():
                triangle_coordinates = [(h_i.getX(10),10,0),(h_i.getX(-10),-10,0),(-100,0,0)]
            else:
                triangle_coordinates = [(h_i.getX(10),10,0),(h_i.getX(-10),-10,0),(100,0,0)]

            triangle = Polygon(fill_color = BLUE, fill_opacity = boundary_opacity, *triangle_coordinates)
            self.play(Write(triangle))
            
            print("adding constraint:")
            h_i.printVector()
            #if current point is within halfspace, we're good!
            if h_i.isInHalfspace(p):
                h.append(h_i)
                continue
            x_left = None
            x_right = None
            print("Point needs to be moved.")
            for h_j in h:
                print("Checking intersection with following constraint:")
                h_j.printVector()
                sigma_x = h_i.getIntersection(h_j)[0]
                if h_j.isBoundToLeft(h_i): #need to change so that is combined with h_i
                    print("This was a left bound.")
                    if x_left is None or x_left <= sigma_x:
                        x_left = sigma_x
                else:
                    print("This was a right bound.")
                    if x_right is None or x_right >= sigma_x:
                        x_right = sigma_x
                print("Current x_left: "+str(x_left))
                print("Current x_right: "+str(x_right))

            if x_left is not None and x_right is not None and x_left>x_right:
                print("Solution is infeasable.")
                quit()
            if x_left is None:
                p = (x_right, h_i.getY(x_right))
            elif x_right is None:
                p = (x_left, h_i.getY(x_left))
            else:
                left_point = (x_left, h_i.getY(x_left))
                right_point = (x_right, h_i.getY(x_right))
                if objective_vector.evaluatePoint(left_point) > objective_vector.evaluatePoint(right_point):
                    p = left_point
                else:
                    p = right_point
            h.append(h_i)

            self.remove(point_visual)
            point_visual = Dot(axes.coords_to_point(p[0],p[1]), color = RED)
            self.play(Write(point_visual))
        print("Solution found: " + str(p))

        self.wait()