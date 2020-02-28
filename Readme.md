## Home work2

**Mohamed Ahmed Sayed **

The goal of the task is to identify the compliance parameters for a cylindrical robot



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/calibration0.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/calibration0.png "image_tooltip")


The cylindrical robot consists of three joint RPP here is a schematic showing the joints and the coordinate frames



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/calibration1.jpg). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/calibration1.jpg "image_tooltip")


Let’s first define what is the compliance parameters. It is the property of a material of undergoing elastic deformation or change in volume when subjected to an applied force. It is equal to the reciprocal of stiffness. It can be calculated using this formula



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/calibration2.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/calibration2.png "image_tooltip")


There are two elements in the equation the A matrix and the delta t which is the deflection

Let’s start with the A matrix. The equation of the A matrix is as follow 



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/calibration3.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/calibration3.png "image_tooltip")


So I wrote a simple function which takes the 


```
def mat_a(q, force, param):
   j = jac_theta(q, param)
   # get the first three rows
   j = j[0:3, :]
   #print(j.shape)
   a = np.zeros((3,3))
   #print(force[:3,:].shape)
   for i in range(3):
       j1 = np.reshape(j[:, i], (3,1))
       t = j1 @ j1.T @ force[:3, :]
       a[:,i] = t.T
       #print(t)
   return a
```


The function depends on two variables the jacobian and forces. We get the jacobian and the forces for each configuration and then aggregate them together.

So let’s explain how to get the jacobian. I wrote another function 


```
def jac_theta(q, param):
   """get the theta jacobian
   Tz(l1). Rz(q1) . Tz(l2) . Tz(q2) . Tx(l3) . Tx(q3) . Tx(l4)
   """
   j = np.zeros((6, 3))
   l1, l2, l3, l4 = param

   t = Tz(l1) @ Rz(q[0]) @ drz(0) @ Tz(l2) @ Tz(q[1]) @ Tx(l3) @ Tx(q[2]) @ Tx(l4)
   j[:, 0] = np.array([t[0:3, 3][0],t[0:3, 3][1],t[0:3, 3][2], t[2,1], t[0,2], t[1,0]])
   t = Tz(l1) @ Rz(q[0]) @ Tz(l2) @ Tz(q[1]) @ dtz(0) @ Tx(l3) @ Tx(q[2]) @ Tx(l4)
   j[:, 1] = np.array([t[0:3, 3][0], t[0:3, 3][1], t[0:3, 3][2], t[2, 1], t[0, 2], t[1, 0]])
   t = Tz(l1) @ Rz(q[0]) @ Tz(l2) @ Tz(q[1]) @ Tx(l3) @ Tx(q[2]) @ dtx(0) @ Tx(l4)
   j[:, 2] = np.array([t[0:3, 3][0], t[0:3, 3][1], t[0:3, 3][2], t[2, 1], t[0, 2], t[1, 0]])
   return j
```


The function takes the configuration and links parameters and then I take the derivative for the transformations from the base to the end effector with respect to every variable which is in our case the joint values. Since the transformations are 4x4 matrices then the output is 4x4 and then to compute J1 we the first three elements in the fourth column and other three elements forming a 6x1 matrix then aggregate this vectors forming the jacobian of size 6x3

To calculate the end effector deflection



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/calibration4.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/calibration4.png "image_tooltip")



```
def deflection(q,force,param):
   """calculate the deflection and dq"""
   j = jac_theta(q, param)
   k = k_full()
   dq, _, _, _ = np.linalg.lstsq(k,(j.T @ force), rcond=-1,)
   dt = j @ dq
   return dt, dq
```


The first line I get the jacobian given the joint values and links parameters 

Then I calculate the stiffness using the function k_full()

Then the dq is calculated by left multiplication of the stiffness with the jacobian and the force

At the last step, I calculate the deflection by multiplying the jacobian with the dq (dot product)

Next, I will describe the main code which uses these function. At the beginning parameters of the links are defined also numpy arrays to store the values of the configurations and the forces 


```
forces = np.zeros((6, exp))
poses = np.zeros((3, exp))
defi = []
```


Then we start the for loop 


```
for i in range(exp):
   # generate random forces
   force = np.zeros((6,1))
   force[:3, 0] = np.asarray(random.sample(range(1, 100), 3))
   forces[:, i] = force.T

   # generate random joint values
   q = np.zeros((3,1))
   q = random.sample(range(1, 10), 3)
   poses[:,i] = q

   # calculate displacement for these positions and forces
   dt, dq = deflection(q, force, links)
   defi.append(np.linalg.norm(dt))

   dt = dt[:3,0]
   A = mat_a(q, force, links)

   s1 = s1 + A.T @ A
   s2 = s2 + A.T * dt
```


First, I generate random forces. Then calculate random joint values, then using these forces and joint values to calculate the deflection. Then calculate the matrix A at the last step sum the new A matrix and the deflection to the previous one 

After the for loop, I did left division to get the compliance


```
k = np.linalg.lstsq(s1, s2, rcond=-1)
```


References: \
Increasing Machining Accuracy of Industrial Manipulators Using Reduced Elastostatic Model

Reference code

Identification of the manipulator stiffness model parameters in industrial environment


<!-- Docs to Markdown version 1.0β18 -->
