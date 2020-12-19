import volume

VALIDINPUT = {'quit', 'q', 'cube', 'c', 'pyramid', 'p', 'ellipsoid', 'e'}

def main():

	results = []

	while True: 
		
		shape = input("Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): ").lower()
		while shape not in VALIDINPUT:
			shape = input("		-- invalid input: enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e) Please enter shape: ").lower()

main()