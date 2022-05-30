# Dynamic Visualization of 3Mark’s Randomized 2-Dimensional Linear Programming 
#### Parker Whitehead
#### CS 6319 Computational Geometry
#### University of Texas at Dallas, Richardson, TX, USA

----
## Abstract
Computational Geometry Algorithms and Applications (3Marks), written by Mark de Berg, Otfried Cheong, Marc van Kreveld, and Mark Overmars, is an excellent tool for thoroughly comprehending the intricacies of complex computational geometry concepts. Such a concept is the Randomized d-Dimensional Linear Programming, which seeks to optimize an objective function whilst under a set of constraints. However, despite the detailed description and many diagrams of the algorithm, I found myself, along with my classmates, struggling to fully grasp how the 3Marks book’s implementation works. In an effort to remedy this, I developed a python program that takes an objective function along with a set of constraints and consequently produces a dynamic visualization of the 3Marks algorithm. This is implemented via Minam, a python library that allows the dynamic creation of graphs & mathematical visuals to be generated by code & then sent to an mp4. The python program implements the 3Marks program as described in the book, and alongside this, prepares the visuals for the eventual mp4 exportation via Minam. Through this program & paper, I hope to further bridge the gap between concept and true understanding for others hoping to obtain a deeper grasp for Linear Programming.

## 1.	Introduction
Consider the following problem. You are given a d-dimensional objective function with variables x1 … xd representing each dimension and scalars c1 … cd which provide a weight to each dimensional variable. The sum of each dimensional variable multiplied by its respective scalar is to be maximized, and has the following format:

#### Maximize	c1x1 + c2x2 + … + cdxd

Without any constraints, it is clear that a solution to this problem would be unbounded, as you can infinitely scale the size of the objective function. However, the maximization of the objective function must be subject to a set of constraints. These constraints are defined as follows:
	
#### a1,1x1 + a1,2x2 + … + a1,dxd <= b1
#### a2,1x1 + a2,2x2 + … + a2,dxd <= b2
#### …
#### a3,1x1 + a3,2x2 + … + a3,dxd <= bn

Variable ai,j is a weight-scalar, where “i” corresponds to the constraint index and “j” corresponds to the dimension. Variable bi is the maximum possible value for constraint “i”. Put simply, we need to obtain the greatest possible sum from the objective function while still abiding by all of the constraints given to us. 
The solution to this problem can be described in terms of a point p = (x1, x2, … xd), where x1, x2, … xd are the values that maximize the objective function with respect to the given set of constraints. 

Additionally, we can represent each of the constraints as a halfspace. Put simply, a half space is a plane that divides a d-dimensional space into two parts, one of which is the halfspace’s valid region. Assuming that taking the union of all of these constraints will produce a closed, non-infinite region, a feasible polytope is created. This is essentially an area such that any point within the given area is a valid point in regards to the given constraint halfspaces.
 
Figure 1: The first box displays a 2-dimensional left-facing halfspace. As shown, the space to the left of the halfspace is not within the set of valid points for the halfspace, while the shaded blue region is. The second box shows the union of all halfspace regions, which produces a polytope.

For the sake of visualization convenience, further problems described in this paper will be of 2 dimensions. The motivation behind this is to provide an easily interpretable visual, allowing us to graph both the optimum point and all constraints as 2 dimensional points & lines, respectively. 

Given our definition of a linear program, we are left with 4 possible outcomes given an objective function and a set of points:

 
Figure 2: Cases 1 through 4 represent the possible outcomes of a 2-dimensional linear programming problem.

Case 1: The first case reflects what was shown in Figure 2, which is a closed polytope produced by the union of all half space constraints. However, this diagram now contains a point & a vector’s direction. This represents the optimal coordinates which satisfy the objective function in respect to the constraints. Observe that its location is at the intersection of two halfspaces. As the 3Marks book describes in detail, if there is to exist a single optimal solution, then it must lie on an intersection. The reasoning behind this can be derived from the following observation:
	
Assume that there exists a single optimal solution that does lie on an intersection but instead resides on an edge of a half plane. Attempt to slide the point across the halfspace’s edge in a direction. If the value increases, you do not have the optimum solution; if the value decreases, this means that moving it in the opposite direction would cause an increase in value, and thus you do not have the optimum solution; if the value does not change, then there is more than one optimal solution, meaning that you do not have a single optimal solution. Sliding a point across a line will cause it to eventually run into an intersection, where it can no longer slide left or right. If you do not run into an intersection, this means that your solution is unbounded, which is something we will cover in case 4. As such, a single optimal solution will always exist at an intersection. 

Case 2: However, there are some cases in which multiple optimal solutions can exist. If the trajectory of the objective vector is perpendicular with a halfspace that makes up an edge of the feasible polytope, then any point across that halfspace is considered an optimal solution.

Case 3: There are also examples of halfplane union in which no feasible polytope is produced. This means that there is also no feasible solution, or rather the solution is infeasible.

Case 4: In contrast to this, if the polytope is unbounded and there exists no halfplane in the way of the objective function's infinite expansion, then we have an unbounded solution.

## 2. Discussion of Incremental and Randomized Linear Programming	

3Marks provides 2 algorithms to solve 2-Dimensional Linear Programming Problems: Iterative and Randomized. Although 3Marks makes mention of algorithms such as “simplex,” the point is made that most linear programming problems have few dimensions and numerous constraints. Simplex’s strength is handling high dimensions, and consequently struggles in low dimensions with a high volume of constraints. Both the Iterative and Randomized algorithms are at their best when in a low-dimensional environment.

The Iterative approach described by is quite similar to graham scan, in that it incrementally adds more and more elements to a problem until the entire set is constructed. Specifically, the Iterative approach starts with “d” constraints that produce a single optimal solution for the objective function. Since we are dealing with 2 dimensions, we begin with 2 objective functions as halfspaces that define a point p = (x1, x2) which represents the singular optimal solution for the objective function. Given this starting point, we gradually add more and more halfspaces, and update p for each iteration. 

However, this can come with significant drawbacks in regards to running time. Specifically, the act of having to update p in the case that a newly added halfspace is incredibly costly. Given a worst case scenario where every insertion of a new point produces a new p, 3Marks observes that we would be anticipating a time complexity of O(nd), which is not optimal for large numbers of constraints. 

To remedy this, 3Marks proposes a simple change to the Iterative algorithm: the shuffling of all half plane constraints prior to the algorithm starting. To save time, I will not go into thorough detail here, but by using a statistical analysis of the running time, this change brings the expected running time to O(d!n) Although this is not optimal for high numbers of dimensions, it is considerably improved for large quantities of constraints. 

 
[1] Figure 3: Above is the pseudo-code for 2D Randomized Linear Programming, as described by the 3Marks textbook

Although the above pseudo code provides a detailed explanation for the execution of the algorithm, for someone who is new to Computational Geometry, it can be difficult to interpret. I constructed my python visualization program with the intention of providing an intuitive resource to better comprehend the steps of the Marks3 Randomized LP Algorithm.


## 3. Implementation of Dynamic Randomized Linear Programming
I selected to implement my algorithm & visualizer in python for multiple reasons. First off, my goal with this whole project is to help someone with very little experience in Computational Geometry have a greater understanding of Linear Programming. The readability of python code is some of the best in computer science, making it perfect for anyone wishing to explore my implementation further & see what makes it tick. Additionally, python houses an expansive list of libraries that are incredibly easy to implement and use. Manim, an open-source mathematical visualization library, was the tipping point in my decision to use python, given that it provides an incredibly simplistic method of producing dynamic geometric visuals.

I opted for a semi-object oriented approach for my implementation. Although this is not the most efficient for time efficiency, python itself is not known for being particularly fast, so it was not of much concern to me. I created 2 classes: Objective & Constraint. The Objective class contains the 2 scalars for the 2 dimensional LP space. It also contains a function that evaluates the objective function given a set of points. The Constraint is similar to the Objective class in that it contains 2 scalar values. It also contains the b value for which c1*x + c2*y <= b. Additionally, the Constraint class houses a variety of functions that help to organize the program & remove redundant repetition of code.

Upon running the program, the user is requested to provide the objective function, the number of constraints, and then each individual constraint. These inputs are converted into their corresponding objects & then stored for later use on the algorithm. The program then randomizes the list of all constraints, and calculates the initial 2 constraint vectors. It is imperative that these first 2 constraints provide a bounded singular solution to the LP. To ensure this, the Constraint class contains a function for evaluating whether points are within its corresponding halfspace. It then stretches slightly along each constraint line to test if it is both within the corresponding halfspace and more optimal than the vertex. If this is ever the case, then that means that there is not a singular optimal point for the LP, so another set of constraints should be selected for the initial set.

If a pair is not found, then that means that the LP is unbounded. This will close the problem, as it only handles visualizations of singular optimal points. Otherwise, the program continues to the iterative adding of constraints.

Whenever a new constraint is added, there are three possible results: the point either remains in the same location, it no longer has a feasible solution, or the point must be updated to a new location. In the case that the point remains, nothing changes and the constraint is simply added to the active list of constraints. In the case that the constraint changes, however, the method for calculating the new point in 3Marks is followed.  For every intersection between ell_i (the line of the constraint being added). And each “h” within the set of active constraints, let sigma_x represent the x coordinate of the intersection. Through this intersection, we can inch along the left and right of ell_i to see how h binds it. In the case that x<=sigma_x, then we know we have a right bound. The opposite exists for x>=sigma_x, as it defines a left bound. 

The variable x_left keeps track of the maximum x value of an intersection for left bounds, and the variable x_right keeps track of the minimum x value of an intersection for right bound. This causes x_left and x_right to represent the left and right bounds within the polytope respectfully. Because of this, we determine that the optimal solution must exist somewhere between [x_left : x_right]. 2 Points are created to represent the intersections where x_left and x_right exist. They are named point_left and point_right. These points are then evaluated by the objective function. In the case that both solutions are equal in value for the objective function, there are multiple possible solutions. The algorithm opts to simply choose one, as the case may be that this becomes irrelevant in future iterations of the algorithm. However, in the case that the values are different, it takes the one that maximizes the objective function.

This process continues until either an infeasible solution is found - in which case the program is aborted - or the program produces a singular optimal solution to the LP. During each insertion of a constraint, Manim is used to draw the corresponding line onto a graph. During the drawing of a singular optimal solution, a red point is drawn at the corresponding (x,y) coordinates. At the end of the program running, it will produce a .mp4 file containing the completed animation.


## 4. How to Install Dependencies and Run Program
To run the Randomized 2D Linear Program Visualizer, a few downloads are required. The first step is to ensure that you have Python of 3.7-3.10. Additionally, numerous dependencies for Manim are required before the program can be executed. Thankfully, Manim contains a fantastic and easy-to-follow guide, which can be found here:

[2] https://docs.manim.community/en/stable/installation.html

Ensure that you install all required dependencies. Additionally, the dependency “MiKTeX” is required, or at least some form of LaTex. Once all of the dependencies are installed, restart your device & then run the following command:
Python -m pip install manim

After this, you should be fully capable of running the LP Visualizer. However, this program is not run with a traditional python command. Rather, you run the file with Manim with the filename as an argument. This can be done  through the following command:

#### manim main.py DynamicLP -pqm

If you wish to preload the Linear Programming problem with a text file instead of through the command prompt, you may also execute the following command:

#### cat input.txt | manim main.py DynamicLP -pqm

Either option works, as the end result, given that you provide a LP problem with a singular optimal solution, will produce an mp4 titled DynamicLP. This file will be stored in an automatically generated folder in whatever directory the python script is located.

 
Figure 4: Example output of program. Produced by running manim command on the python script. Can be located under media -> videos 


## 6. Sources
	
[1]	M. de Berg, O. Cheong, M. van Kreveld, and M. Overmars, Computational geometry: Algorithms and applications, 3rd ed. Beijing: World Publishing Corporation, 2013.

[2]	“Manim Community overview,” Manim Community | Documentation. [Online]. Available: https://docs.manim.community/en/stable/. [Accessed: 12-May-2022]. 

