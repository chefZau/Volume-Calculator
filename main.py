import volume

VALIDINPUT = {'quit', 'q', 'cube', 'c', 'pyramid', 'p', 'ellipsoid', 'e'}

def main():

	results = []

	while True: 
		
		shape = input("Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): ").lower()
		while shape not in VALIDINPUT:
			shape = input("		-- invalid input: enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e) Please enter shape: ").lower()

		if shape in ['cube', 'c']:
			side = float(input("Enter length of side for the cube: "))
			results.append(("cube", volume.cube(side)))
			print("The volume of a cube with side {} is: {:.2f}\n".format(side, results[-1][1]))

		elif shape in ['pyramid', 'p']:
			base = float(input("Enter the base of the pyramid: "))
			height = float(input("Enter the height of the pyramid: "))
			results.append(("pyramid", volume.pyramid(base, height)))
			print("The volume of a pyramid with base {} and height {} is: {:.2f}\n".format(base, height, results[-1][1]))

		elif shape in ['ellipsoid', 'e']:
			r1 = float(input("Enter the first radius: "))
			r2 = float(input("Enter the second radius: "))
			r3 = float(input("Enter the third radius: "))
			results.append(("ellipsoid", volume.ellipsoid(r1, r2, r3)))
			print("The volume of an ellipsoid with radii {} and {} and {} is: {:.2f}\n".format(r1, r2, r3, results[-1][1]))

		else:
			break

	if not results:
		print("Output: No shapes entered.")
	
	else:
		results.sort(key = lambda results: results[1])
		
		print("Output: Volumes of shapes entered in sorted order:")
		for shape, value in results:
			print(shape, "{:.2f}".format(value))
	
	print()

main()