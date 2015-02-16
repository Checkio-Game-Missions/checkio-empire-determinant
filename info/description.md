In linear algebra, the  [determinant](http://en.wikipedia.org/wiki/Determinant") is a value associated with a square matrix.
It can be computed from the entries of the matrix by a specific arithmetic expression 
(There are other ways to determine its value as well.)

The determinant of a matrix **A** is denoted **det(A)**, **det A**, or **|A|**.
In the case where the matrix entries are written out in full, the determinant 
is denoted by surrounding the matrix entries by vertical bars instead of the brackets or parentheses of the matrix.

There are various ways to define the determinant of a square matrix **A**, i.e.
one with the same number of rows and columns. Perhaps the most natural way
is expressed in terms of the columns of the matrix. If we write an **N×N**
matrix in terms of its column vectors:

A = [a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>]

Where there are vectors of size n, then the determinant of A is defined so that:

det[a<sub>1</sub>, ..., b*a<sub>j</sub>+c*v, ..., a<sub>n</sub>] = b*det(A)+c*det[a<sub>1</sub>, ..., v, ..., a<sub>n</sub>]

det[a<sub>1</sub>, ..., a<sub>j</sub>, a<sub>j+1</sub>, ..., a<sub>n</sub>] = -det[a<sub>1</sub>, ..., a<sub>j+1</sub>, a<sub>j</sub>, ..., a<sub>n</sub>]

det(I) = 1

Where **b** and **c** are scalars, **v** is any vector of size **N** and **I** is the identity matrix of size **N**.
These properties state that the determinant is an alternating multilinear function of the columns, and they suffice to
uniquely calculate the determinant of any square matrix. 
Provided the underlying scalars form a field (more generally, a commutative ring with unity).
Equivalently, the determinant can be expressed as a sum of products of entries of the matrix where each product has
**N** terms and the coefficient of each product is −1 or 1 or 0 according to a given rule:
it is a polynomial expression of the matrix entries.
This expression grows rapidly with the size of the matrix (an **NxN** matrix contributes **N!** terms),
so it will first be given explicitly for the case of 2×2 matrices and 3×3 matrices,
followed by the rule for arbitrary size matrices, which subsumes these two cases.


</p>