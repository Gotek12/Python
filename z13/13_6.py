#!/usr/bin/python3
# -*- coding: iso-8859-2 -*

print("Szukamy liczby sposobów, na jakie można pokryć planszę 4x4 identycznymi klockami 2x1.")
# Recursive function to find number of ways to fill a n x 4 matrix
# with 1 x 4 tiles
def totalWays(n = 4):

	# base cases
	if n < 1:
		return 0

	if n < 2:
		return 1

	if n == 2:
		return 2

	# combine results of placing a tile horizontally and
	# placing 4 tiles vertically
	return totalWays(n - 1) + totalWays(n - 2)


print(totalWays())
