# Knol and ten Berge (1989)

A python implementation of Knol, D. L., & ten Berge, J. M. (1989). This algorithm converts a non-positive definite matrix into a positive definite one. In addition, it allows constraints to fix some correlation factors and force the smallest eigenvalue to have a certain value. *Note: the second constraint related to eigenvalues has not been implemented as it does not relate to my current use case.* 

For information about the usage of this code, please view the [example](./example.ipynb) in the repository.

The ktb1989 script imports `numpy` and `scipy` (code written using `numpy==1.19.4` and `scipy==1.5.4`)

## Roadmap

Depending on my future use of this code, there are the following changes that I would make:

* [ ] additional checks/functionality to make sure constraints (such as matrix being symmetric) are adhered to
* [ ] improved documentation
* [ ] support for additional input types (like pandas DataFrames)
* [ ] additional utility functions for re-ordering matrices
* [ ] implement the remaining pieces of the algorithm
