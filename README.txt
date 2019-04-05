Based on ASCE code:

12.2.2 Combinations of Framing Systems in Different
Directions. Different seismic force-resisting systems are
permitted to be used to resist seismic forces along each of the
two orthogonal axes of the structure. Where different systems are
used, the respective R, C d , and Ω 0 coefficients shall apply to each
system, including the structural system limitations contained in
Table 12.2-1.

12.2.3 Combinations of Framing Systems in the Same
Direction. Where different seismic force-resisting systems are
used in combination to resist seismic forces in the same direction,
other than those combinations considered as dual systems, the
most stringent applicable structural system limitations contained
in Table 12.2-1 shall apply and the design shall comply with the
requirements of this section.

12.2.3.1 R, C d , and Ω 0 Values for Vertical Combinations.
Where a structure has a vertical combination in the same
direction, the following requirements shall apply:

1. Where the lower system has a lower response modification
coefficient, R, the design coefficients (R, Ω 0 , and C d )
for the upper system are permitted to be used to calculate
the forces and drifts of the upper system. For the design of
the lower system, the design coefficients (R, Ω 0 , and C d )
for the lower system shall be used. Forces transferred
from the upper system to the lower system shall be
increased by multiplying by the ratio of the higher response
modification coefficient to the lower response modification
coefficient.

2. Where the upper system has a lower response modification
coefficient, the design coefficients (R, Ω 0 , and C d ) for the
upper system shall be used for both systems.

EXCEPTIONS:
1. Rooftop structures not exceeding two stories in height and
10% of the total structure weight.
2. Other supported structural systems with a weight equal to
or less than 10% of the weight of the structure.
3. Detached one- and two-family dwellings of light-frame
construction.

12.2.3.2 Two-Stage Analysis Procedure. A two-stage
equivalent lateral force procedure is permitted to be used for
structures that have a flexible upper portion above a rigid lower
portion, provided that the design of the structure complies with
all of the following:

a. The stiffness of the lower portion shall be at least 10 times
the stiffness of the upper portion.

b. The period of the entire structure shall not be greater than
1.1 times the period of the upper portion considered as a
separate structure supported at the transition from the upper
to the lower portion.

c. The upper portion shall be designed as a separate structure
using the appropriate values of R and ρ.

d. The lower portion shall be designed as a separate structure
using the appropriate values of R and ρ. The reactions from
the upper portion shall be those determined from the
analysis of the upper portion amplified by the ratio of the
R∕ρ of the upper portion over R∕ρ of the lower portion.
This ratio shall not be less than 1.0.

e. The upper portion is analyzed with the equivalent lateral
force or modal response spectrum procedure, and the lower
portion is analyzed with the equivalent lateral force
procedure.

This code converts the reactions of upper structure taken as an
output of ETABS software and inserts the reactions to e2k file 
of lower structure.
