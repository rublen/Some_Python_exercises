'''
you should calculate type of triangle with three given sides a, b and c (given in any order).
If all angles are less than 90*, this triangle is acute and function should return 1.
If one angle is strictly 90*, this triangle is right and function should return 2.
If one angle more than 90*, this triangle is obtuse and function should return 3.
If three sides cannot form triangle, or one angle is 180* (which turns triangle into segment) - function should return 0.
Input parameters are sides of given triangle. All input values are non-negative floating point or integer numbers (or both).
'''

def triangle_type(a, b, c):
  a, b, c = sorted([a, b, c])
  if c >= a + b: return 0
  if c**2 == a**2 + b**2: return 2
  return 1 if c**2 < a**2 + b**2 else 3 



print(triangle_type(7,3,2)) # 0 Not triangle
print(triangle_type(2,4,6)) # 0 (Not triangle)
print(triangle_type(8,5,7)) # 1 (Acute)
print(triangle_type(3,4,5)) # 2 (Right)
print(triangle_type(7,12,8)) # 3 (Obtuse)