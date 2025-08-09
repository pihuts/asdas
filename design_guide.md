AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 43
Chapter 5
Design Examples
The design examples of this section are worked in a generally
complete manner and the design approach for each connec-
tion type is presented in the example. Design aid tables that
are currently printed in the AISC Steel Construction Manual
(AISC, 2011), hereafter referred to as the AISC Manual ,
have been used where possible. Examples 5.1 through 5.
address a corner bracing connection with the gusset plate
connected to the column flange (strong-axis bracing con-
nection). Examples 5.5 through 5.8 address a corner bracing

connection with the gusset plate connected to the column
web (weak-axis bracing connection). For each configuration,
four different uniform force method (UFM) procedures are
exemplified: general UFM, Special Case 1, Special Case 2,
and Special Case 3. Example 5.9 demonstrates the design of
a chevron bracing connection. Nonorthogonal bracing con-
nections, truss connections, and brace-to-column base plate
connections are addressed in Examples 5.10, 5.11 and 5.12,
respectively.
Example 5.1—Corner Connection-to-Column Flange: General Uniform Force Method

Given:

Design the corner bracing connection shown in Figure 5-1 given the listed members, geometry and loads. The bay width is 25 ft.
The connection designed in this problem is shown in Figure 5-1, in completed form (note that the final bolt type changes in the
course of the design example).

Fig. 5-1. Strong axis bracing connection—general uniform force method.
44 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

The required strengths of the brace connection were chosen to force many limit states to be critical. The required strength of the
brace-to-gusset connection is:

LRFD ASD
Pu = 840 kips Pa = 560 kips
The transfer force, as shown in the elevation in Figure 5-1, is:

LRFD ASD
Aub = 100 kips Aab = 66.7 kips
The beam shear end reaction is:

LRFD ASD
Vu = 50.0 kips Va = 33.3 kips
Solution:

From AISC Manual Tables 2-4 and 2-5, the material properties are as follows:

ASTM A
Fy = 50 ksi Fu = 65 ksi
ASTM A572 Grade 50
Fy = 50 ksi Fu = 65 ksi
ASTM A
Fy = 36 ksi Fu = 58 ksi
From AISC Manual Tables 1-1, 1-7 and 1-15, the geometric properties are as follows:

Beam
W21× 83
d = 21.4 in. tw = 0.515 in. bf = 8.36 in. tf = 0.835 in. kdes = 1.34 in. k 1 = d in. Ix = 1,830 in.^4
Column
W14× 90
d = 14.0 in. tw = 0.440 in. bf = 14.5 in. tf = 0.710 in. Ix = 999 in.^4
Brace
2L8× 6 × 1 LLBB
Ag = 26.2 in.^2 x = 1.65 in. (single angle)
Brace-to-Gusset Connection

The brace-to-gusset connection should be designed first so that a minimum required size of the gusset plate can be determined.
In order to facilitate the connection design, a sketch of the connection should be drawn to scale (Figure 5-2). From this sketch,
the important dimensions can be checked graphically (either manually or on a computer) at the same time as they are being cal-
culated analytically.

Determine required number of bolts

The preliminary design uses d-in.-diameter ASTM A325-X bolts. The calculations begin with the assumption that A325-X bolts
will work. However, calculations later in this example will show that the beam-to-column connection requires d-in.-diameter
ASTM A490-X bolts. It is not advisable to use different grade bolts of the same diameter, so ASTM A490-X bolts are used for
all d-in.-diameter bolts as shown in Figure 5-1. For now, proceed with ASTM A325-X bolts.

AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 45
From the AISC Specification for Structural Steel Buildings (AISC, 2010c) , hereafter referred to as the AISC Specification, Sec-
tion J3.6, the available shear strength (in double shear) and available tensile strength are determined using Equation J3-1 and
Table J3.2, as follows:

LRFD ASD
φφ
π
φφ
rFA
r
nv nb
nt
=
= ()()⎡⎣⎢ ()⎤⎦⎥
=
=
20 75 68 4
61 3
.^2
.

ksiin.
kips
d
FFAnb
= ()⎡⎣⎢ ()⎤⎦⎥
=
0754
40 6
.^2
.

90 ksiin.
kips
π d
rFA
rF
nv nb
nt n
ΩΩ
Ω
=
=
()⎡⎣⎢ ()⎤⎦⎥

=
=
2684
200
40 9
ksiin.^2
kips
πd
.
.
AAb
Ω
=
()⎡⎣⎢ ()⎤⎦⎥

=
90 4
200
27 1
ksiin.^2
kips
πd
.
.
Alternatively, the available shear and tensile strengths can be determined directly from AISC Manual Tables 7-1 and 7-2. The
minimum number of d-in.-diameter ASTM A325-X bolts in double shear required to develop the required strength is:

Fig. 5-2. Geometry for Example 5.1 calculations.
46 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

LRFD ASD
N P
b P
u
n
=
=
=
φ
kips
kips/bolt
bolts
840
61 3
13 7
.
.
N P
b P
a
n
=
()
=
=
.
.
Ω
kips
kips/bolt
bolts
560
40 9
13 7
Use two rows of seven bolts with 3-in. spacing, 3-in. pitch, and 1 2 -in. edge distance as shown in Figure 5-1.

Check tensile yielding on the brace gross section

From AISC Specification Section D2(a), use Equation D2-1 to determine the available tensile yielding strength of the double-
angle brace:

LRFD ASD
φφ PFny = Ag
= ()()
=>
09036262
849 840
..ksiin.
kips kips
2
o.k.
Pn FAyg
ΩΩ=
=
()()
=>
36 26 2
167
565 560
ksiin.
kips kips
.^2
.
o.k.

Alternatively, from AISC Manual Table 5-8, the available tensile yielding strength of the double-angle brace is:

LRFD ASD
φ Pn => 849 840kips kips o.k. Pn
Ω
=> 565 560kips kips o.k.
Check tensile rupture on the brace net section

The net area of the double-angle brace is determined in accordance with AISC Specification Section B4.3, with the bolt hole
diameter, dh = , in., from AISC Specification Table J3.3:

Ang =− At ( dh +
=−()
=
4
2624100
22 2
z in.)
in.in.(, in. + z in.)
in.
2
2
..
.
Because the outstanding legs of the double angle are not connected to the brace, an effective net area of the double angle needs
to be determined. From AISC Specification Section D3 and Table D3.1, Case 2, the effective net area is:

Ae = AnU ( Spec. E q. D3 -1)
AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 47
where

U x
l
l
U
=−
= ()
=
=−
=
1
6300
18.0 in.
1 165
18 0
0 908
.
.
.
.
in.
in.
in.
Ae = (^) (22.2 in.^2 )(0.908)
= 20.2 in.^2
From AISC Specification Section D2(b), the available tensile rupture strength of the double-angle brace is:
LRFD ASD
φφ PFnu = Ae

= ()()
=>
07558202
879 840
..ksiin.
kips kips
2
o.k.
PFnuAe
ΩΩ
=
=
()()
=>
58 20 2
200
586 560
ksiin.
kips kips
.^2
.
o.k.

Alternatively, because Ae > 0.75 Ag , AISC Manual Table 5-8 could be used conservatively to determine the available tensile rup-
ture strength. The calculated values provide a more precise solution, however.

Check block shear rupture on the brace

The block shear rupture failure path is assumed as shown in Figure 5-2a. The available strength for the limit state of block shear
rupture is given in AISC Specification Section J4.3 as follows:

Rn = 0.60 Fu Anv + UbsFu Ant ≤ 0.60 Fy Agv + UbsFu Ant ( Spec. Eq. J4-5)
Shear yielding component:

Agv = 2(1.00 in.)[6(3.00 in.) + 1.50 in.]
= 39.0 in.^2
0.60 Fy Agv = 0.60(36ksi)(39.0 in.^2 )
= 842 kips
Shear rupture component:

Anv = 39.0 in.^2 − 6.5(2)(1.00 in.)(1.00 in.)
= 26.0 in.^2
0.60 Fu Anv = 0.60(58 ksi)(26.0 in.^2 )
= 905 kips
Tension rupture component:

Ubs = 1 from AISC Specification Section J4.3 because the bolts are uniformly loaded
Ant = 2(1.00 in.)[(3.00 in. + 2.00 in.) − 1.5(d in. + z in. + z in.)]
= 7.00 in.^2
UbsFu Ant = 1(58 ksi)(7.00 in.^2 )
= 406 kips
48 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

The available strength for the limit state of block shear rupture is:

0.60 Fu Anv + UbsFu Ant = 905 kips + 406 kips
= 1,310 kips
0.60 Fy Agv + UbsFu Ant = 842 kips + 406 kips
= 1,250 kips
Because 1,310 kips > 1,250 kips, use Rn = 1,250 kips.

LRFD ASD
φ Rn = 0.75(1,250 kips)
= 938 kips > 840 kips o.k.
Rn
Ω
=
=>
1 250
200
625 560
,
.
kips
kips kips o.k.
Check block shear rupture on the gusset plate

Assume that the gusset plate is 1 in. thick and verify the assumption later. The block shear rupture failure path is assumed as
shown in Figure 5-2b.

Shear yielding component:

Agv = 2(1.00 in.)(19.5 in.)
= 39.0 in.^2
0.60 FyAgv = 0.60(50 ksi)(39.0 in.^2 )
= 1,170 kips
Block shear
failure path on
double angle
Fig. 5-2a. Block shear rupture failure path on double-angle brace.
AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 49
Shear rupture component:

Anv = 39.0 in.^2 − 6.5(1.00 in.)(1.00 in.)(2)
= 26.0 in.^2
0.60 Fu Anv = 0.60(65 ksi)(26.0 in.^2 )
= 1,010 kips
Tension rupture component:

Ubs = 1 from AISC Specification Section J4.3 because the bolts are uniformly loaded
Ant = (1.00 in.)(3.00 in.) − 2(0.5)(1.00 in.)(1.00 in.)
= 2.00 in.^2
UbsFu Ant = 1(65 ksi)(2.00 in.^2 )
= 130 kips
The available strength for the limit state of block shear rupture is:

0.60 Fu Anv + UbsFuAnt = 1,010 kips + 130 kips
= 1,140 kips
0.60 FyAgv + UbsFuAnt = 1,170 kips + 130 kips
= 1,300 kips
Therefore, Rn = 1,140 kips.

From AISC Specification Section J4.3, the available block shear rupture strength is:

LRFD ASD
φ Rn = 0.75(1,140 kips)
= 855 kips > 840 kips o.k.
Rn
Ω
=
=>
1 140
200
570 560
,
.
kips
kips kips o.k.
Block shear
failure path on
gusset plate
Fig. 5-2b. Block shear rupture failure path on gusset plate.
50 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

Check bolt bearing on the gusset plate

Bearing strength at bolt holes on the gusset plate will control over bearing strength at bolt holes on the brace because the brace
has two angles for every bolt hole; therefore, only the gusset plate will be checked here. Assume the gusset plate is 1 in. thick.
Standard size holes are used in the brace. From AISC Specification Table J3.3, for a d-in.-diameter bolt, dh = , in.

According to the User Note in AISC Specification Section J3.6, the strength of the bolt group is taken as the sum of the effective
strengths of the individual fasteners. The effective strength is the lesser of the fastener shear strength and the bearing strength.
Assuming that deformation at the bolt hole at service load is a design consideration, use AISC Specification Equation J3-6a for
the nominal bearing strength:

Rn = 1.2 lctFu ≤ 2.4 dtFu ( Spec. Eq. J3-6a)
For the inner bolts, the clear distance is:
lc = 3.00 in. − 1.0 dh
= 3.00 in. − 1.0(, in.)
= 2.06 in.
LRFD ASD
φ1.2 lctFu = 0.75(1.2)(2.06 in.)(1.00 in.)(65 ksi)
= 121 kips
φ2.4 dtFu = 0.75(2.4)(d in.)(1.00 in.)(65 ksi)
= 102 kips
Therefore, φ rn = 102 kips.

1.2 lctFu /Ω = 1.2(2.06 in.)(1.00 in.)(65 ksi)/2.
= 80.3 kips
2.4 dtFu /Ω = 2.4 (d in.)(1.00 in.)(65 ksi)/2.
= 68.3 kips
Therefore, rn /Ω = 68.3 kips.
Because the available bolt shear strength determined previously (61.3 kips for LRFD and 40.9 kips for ASD) is less than the
bearing strength, the limit state of bolt shear controls the strength of the inner bolts.

For the end bolts:
lc = 1.50 in. − 0.5 dh
= 1.50 in. − 0.5(, in.)
= 1.03 in.
LRFD ASD
φ1.2 lctFu = 0.75(1.2)(1.03 in.)(1.00 in.)(65 ksi)
= 60.3 kips
φ2.4 dtFu = 0.75(2.4)(d in.)(1.00 in.)(65 ksi)
= 102 kips
Therefore, φ rn = 60.3 kips.

1.2 lctFu /Ω = 1.2(1.03 in.)(1.00 in.)(65 ksi)/2.
= 40.2 kips
2.4 dtFu /Ω = 2.4 (d in.)(1.00 in.)(65 ksi)/2.
= 68.3 kips
Therefore, rn /Ω = 40.2 kips.
For the end bolts, the available bearing strength governs over the available bolt shear strength determined previously. To deter-
mine the available strength of the bolt group, sum the individual effective strengths for each bolt.

The total available strength of the bolt group is:

LRFD ASD
φ Rn = (2 bolts)(60.3 kips) + (12 bolts)(61.3 kips)
= 856 kips > 840 kips o.k.
Rn
Ω =
=>
(2 bolts)(40.2 kips) + (12 bolts)(40.9 kips)
571 560kips kips o.k.
Therefore, the 1-in.-thick gusset plate is o.k. Additional checks are required as follows.

AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 51
Check the gusset plate for tensile yielding on the Whitmore section

From AISC Manual Part 9, the width of the Whitmore section is:
lw = 3.00 in. + 2(18.0 in.) tan 30°
= 23.8 in.

Approximately 4.70 in. of this length runs into the beam web, as shown in Figure 5-2, which is thinner than the gusset. AISC
Manual Part 9 states that the Whitmore section may spread across the joint between connected elements, which in this case
includes the beam web. Thus, the effective area of the Whitmore section is:
Aw = (23.8 in. − 4.70 in.)(1.00 in.) + (4.70 in.)(0.515 in.)
= 21.5 in.^2

From AISC Specification Section J4.1(a), the available tensile yielding strength of the gusset plate is:

LRFD ASD
    φ Rn = φ Fy Aw
= 0.90(50 ksi)(21.5 in.^2 )
= 968 kips > 840 kips o.k.
Rn FAyw
ΩΩ
=
=
()()
=>
50 21 5
167
644 560
ksiin^2
kips kips
..
.
o.k.
Check the gusset plate for compression buckling on the Whitmore section

The available compressive strength of the gusset plate based on the limit state of flexural buckling is determined from AISC
Specification Section J4.4, using an effective length factor, K , of 0.50 as established by full scale tests on bracing connections
(Gross, 1990). Note that this K value requires the gusset to be supported on both edges. Alternatively, the effective length factor

for gusset buckling could be determined according to Dowswell (2006). In this case, because KL / r is found to be less than 25
assuming K = 0.50, the same conclusion, that buckling does not govern, will be reached using either method.

r
tg
=
=
=
12
100
12
0 289
.
.
in.
in.
From Figure 5-2, the gusset plate unbraced length along the axis of the brace has been determined graphically to be 9.76 in.

KL
r
= ()
=
050976
0 289
16 9
..
.
.
in.
in.
Because KL
r

< 25, AISC Specification Equation J4-6 is applicable, and the available compressive strength is:
LRFD ASD
    φ Pn = φ FyAg
= 0.90(50 ksi)(20.9 in.^2 )
= 941 kips > 840 kips o.k.
Pn FAyg
ΩΩ
=
=
()()
=>
50 20 9
167
626 560
ksiin.^2
kips kips
.
.
o.k.
52 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

This completes the brace-to-gusset connection calculations and the gusset plate width and depth size can be determined as shown
in Figure 5-1. Squaring off the gusset on top shows that seven rows of bolts will fit.

Connection Interface Forces

The forces at the gusset-to-beam and gusset-to-column interfaces are determined using the general case of the UFM as discussed
in AISC Manual Part 13 and this Design Guide:

e d
e d
b b
c c
= = = = = =
2
21 4
2
10 7
2
14 0
2
700
.
.
.
.
in.
in.
in.
in.
From Figure 5-2:

tan
.
θ
θ
=
=
12
11
47 2°
8
Choose β = 12 in. Then, the constraint α − βtanθ = eb tanθ − ec from AISC Manual Part 13, with β = β, yields:
α = (10.7 in. + 12.0 in.)(1.08) − 7.00 in.
= 17.5 in.

This can also be done graphically as shown in Figure 5-2, with β = β = 12 in. Start at point a and construct a line through b to
intersect the brace line at c. From c , construct a line through point d until the top flange of the beam is intersected at point e.
The distance from point e to the face of the column flange is α. The points b , c and d , are known as the “control points” of the
uniform force method.

Arrange the horizontal edge of the gusset so that α = α and from Figure 5-1:

α= lh +win.+ tp
2
where tp is the yet to be determined end-plate thickness, w in. is the gusset corner clip thickness, and lh is the horizontal gusset
length.

Assume tp = 1 in. and solving for lh :
lh = 2(17.5 in.) − 2(1.00 in.) − w in.
= 32.3 in.

So, the tentative gusset plate size is 1 in. × 242 in. × 2 ft 8 4 in. The top edge of the gusset could be shaped as shown by the
broken line to reduce the excessive (but acceptable) edge distance. Proceeding with α = α = 17.5 in. and β = β = 12 in., there will
be no couples on any connection interface. This is the general case of the UFM.

AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 53
Using the previously determined variables and guidelines from AISC Manual Part 13:

re =+ c ++ eb
=+++
=
()()
()()
αβ^22
17 57 00 22120107
33
..in.in. ..in.in.
.. 4in.
( Manual Eq. 13-6)
The required shear force at the gusset-to-column connection and required normal force at the gusset-to-beam connection are
determined as follows:

V
r
c =β P
( Manual Eq. 13-2)
V e
r
b = bP
( Manual Eq. 13-4)
LRFD ASD
V
r
P
V e
r
P
uc u
ub b u
=
=⎛
⎝
⎜
⎞
⎠
⎟()
=
=
=
β
12 0
33 4
840
302
10
.
.
in.
in.
kips
kips
..
.
7
33 4
840
269
in.
in.
kips
kips
⎛
⎝
⎜
⎞
⎠
⎟()
=
V
r
P
V e
r
P
aca
ab b a
=
=⎛
⎝
⎜
⎞
⎠
⎟()
=
=
=
β
12 0
33 4
560
201
10
.
.
in.
in.
kips
kips
..
.
7 560
33 4
179
in. kips
in.
kips
()

⎛
⎝
⎜
⎞
⎠
⎟
=
Verify that the sum of the vertical gusset forces equals the vertical component of the brace force:

LRFD ASD
Σ( Vuc + Vub ) = 302 kips + 269 kips
= 571 kips
Pu (cos θ) = (840 kips)(cos 47.2°)
= 571 kips o.k.
Σ( Vac + Vab ) = 201 kips + 179 kips
= 380 kips
Pa (cos θ) = (560 kips)(cos 47.2°)
= 380 kips o.k.
The required normal force at the gusset-to-column connection and required shear force at the gusset-to-beam connection are
determined as follows:

Hc = ercP
( Manual E q. 13-3)
H
r
b =α P
( Manual Eq. 13-5)
54 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

LRFD ASD
H e
r
P
H
r
P
uc c u
ubu
=
=⎛
⎝
⎜
⎞
⎠
⎟()
=
=
=
700
33 4
840
176
17
.
.
in.
in.
kips
kips
α
..
.
5
33 4
840
440
in.
in.
kips
kips
⎛
⎝
⎜
⎞
⎠
⎟()
=
H e
r
P
H
r
P
ac c a
aba
=
=⎛
⎝
⎜
⎞
⎠
⎟()
=
=
=
700
33 4
560
117
17
.
.
in.
in.
kips
kips
α
..
.
5
33 4
560
293
in.
in.
kips
kips
⎛
⎝
⎜
⎞
⎠
⎟()
=
The total horizontal force at the brace-to-gusset connection is:

LRFD ASD
Σ( Huc + Hub ) = 176 kips + 440 kips
= 616 kips
Check that the sum of the horizontal gusset forces equals
the brace horizontal component
    Σ( Huc + Hub ) = (840 kips)(sin 47.2°)
= 616 kips o.k.
Σ( Hac + Hab ) = 117 kips + 293 kips
= 410 kips
Check that the sum of the horizontal gusset forces equals
the brace horizontal component
    Σ( Hac + Hab ) = (560 kips)(sin 47.2°)
= 411 kips o.k.
Figures 5-3a and 5-3b show the free body diagram (admissible force field) determined by the UFM.

Gusset-to-Beam Connection

Using the same symbols that were used in determining the UFM forces, the required strengths and weld length at the gusset-to-
beam interface are:

LRFD ASD
Required shear strength, Hub = 440 kips
Required normal strength, Vub = 269 kips
Length of weld, l = 324 in. − w in. = 31.5 in.
Required shear strength, Hab = 293 kips
Required normal strength, Vab = 179 kips
Length of weld, l = 324 in. − w in. = 31.5 in.
Check gusset plate for shear yielding and tensile yielding along the beam flange

The available shear yielding strength of the gusset plate is determined from AISC Specification Equation J4-3, and the available
tensile yielding strength is determined from AISC Specification Equation J4-1, as follows:

AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 55

Fig. 5-3a. Admissible force field for Example 5.1—LRFD.
Fig. 5-3b. Admissible force field for Example 5.1—ASD.
56 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

LRFD ASD
φ Rn = φ0.60 FyAgv
= 1.00(0.60)(50 ksi)(1.00 in.)(31.5 in.)
= 945 kips > 440 kips o.k.
φ Rn = φ FyAg
= 0.90(50 ksi)(1.00 in.)(31.5 in.)
= 1,420 kips > 269 kips o.k.
Rn FAygv
ΩΩ=
= ()()()
=
060
06050100 31 5
150
630
.
...
.
ksiin. in.
kipps> 293 kips o.k.
Rn FAyg
ΩΩ
=
=()()()
=>
50 100315
167
943 179
ksiin. in.
kips ki
..
.
pps o.k.
Consider force interaction for gusset plate

It is usually suggested that the von Mises yield criterion be used for checking interaction; however, in its underlying theory the
von Mises criterion requires three stresses at a point and only two stresses (normal and shear) are available. A better choice of
interaction check is the equation derived from plasticity theory (Neal, 1977) and suggested by Astaneh-Asl (1998) as:

LRFD ASD
M
M
V
N
H
V
ub
n
ub
n
ub
φφφ n
⎛
⎝
⎜
⎞
⎠
⎟+
⎛
⎝
⎜
⎞
⎠
⎟ +
⎛
⎝
⎜
⎞
⎠
⎟ ≤
24
1
From AISC Specification Equation F2-
φφ MM
FZ
F
tl
np
yx
y
g
=
=
=
⎛
⎝
⎜
⎜
⎞
⎠
⎟
⎟
= ()

090
090
4
09050
100
2
.
.
.
.
ksi
in. in.
kip-in.
⎡()()

⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
31 5
4
11 200
.^2

,
Incorporating the previously determined values
0
11 200
269
1 420
kip-in.^2
kip-in.
kips
,, kips
⎛
⎝⎜
⎞
⎠⎟
+⎛
⎝⎜
⎞
⎠⎟
+⎛
⎝
⎜
⎞
⎠
⎟ =<
440
945
0 0829 10
kips^4
kips
.. o.k.
M
M
V
N
H
V
ab
n
ab
n
ab
()ΩΩ n Ω
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
+
()
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
+
()
⎡
⎣
⎢
⎢
⎤
⎦
⎥ ≤
24
1
From AISC Specification Equation F2-
M M
FZ
Ftl
n p
yx
yg
ΩΩ
Ω
=
=
=
⎛
⎝
⎜⎜
⎞
⎠
⎟
⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
=⎛
1674
50
167
2
.
.
ksi
⎝⎝⎜
⎞
⎠⎟
⎡()()

⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
100315
4
7 430
..^2
,
in. in.
kip-in.
Incorporating the previously determined values
0
7 430
179
943
kip-in.^2
kip-in.
kips
, kips
⎛
⎝
⎜
⎞
⎠
⎟+
⎛
⎝
⎜
⎞
⎠
⎟
+⎛
⎝⎜
⎞
⎠⎟
(^293) =<
630
0 0828 10
kips^4
kips
..o.k.
Therefore, the 1-in.-thick gusset plate is adequate.
Note that interaction of the forces at the gusset-to-beam interface is generally not a concern in gusset design, as can be seen from
this result. The AISC Specification and Manual generally do not require that this interaction be checked.

AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 57
Design weld at gusset-to-beam flange connection

The forces involved are:

Vub = 269 kips and Vab = 179 kips
Hub = 440 kips and Hab = 293 kips
The UFM postulates uniform forces on each connection interface. For this to be possible, sufficient ductility must be present in
the system. As discussed in Section 1.2, most connection limit states have some ductility, or force redistribution can be accom-
plished either by support or element flexibility or by increasing the strength of nonductile elements to allow redistribution to
occur without premature local fracture. To allow for redistribution of stress in welded gusset connections, the weld is designed for
a stress of fpeak or 1.25 favg , as defined in the following. The 1.25 factor is the weld ductility factor discussed in the AISC Manual
Part 13 (Hewitt and Thornton, 2004), which is actually an overstrength factor, and is intended to allow redistribution to occur
before fracture of nonductile elements.

The required shear force and normal force per linear inch of weld on the gusset-to-beam flange interface are:

LRFD ASD
.
.
f V
l
f H
l
ua ub
uv ub
=
=
=
=
=
269
31 5
440
31
kips
in.
8 54 kip/in.
kips
..
.
5
0
in.
= 14 kip/in.
f V
l
f H
l
aa ab
av ab
.
.
=
=
=
=
=
179
31 5
293
31
kips
in.
5 68 kip/in.
kips
..
.
5
0
in.
= 93 kip/in.
Use a vector sum (square root of the sum of the squares) to combine the shear, axial and bending stresses on the gusset-to-beam
interface. The peak and average stresses are:

f ff f
f ff ffff
peak ab v
avgabvab v
= ()+

=−⎡ ()++()+
⎣
+
+
(^22)
(^12222)
2
⎢⎢
⎤
⎦⎥
Because fb , the bending stress, is zero in this case, the average stress on the gusset-to-beam flange interface is:
LRFD ASD
fua (^) vg fup (^) eak
8.54 kip/in. kip/in.
kip/i
=
= ()+()
=.
(^22) 14.
16 4nn.
The resultant load angle is:
θ= ⎛
⎝
⎜
⎞
⎠
⎟
=°
tan−.
.
.
1 854
14 0
31 4
kip/in.
kip/in.
faa vg fap eak
kip/in. kip/in.
kip/in
=
= ()+()
=
568930
10 9
..^22
...
The resultant load angle is:
θ= ⎛
⎝
⎜
⎞
⎠
⎟
=°
tan−.
.
.
1 568
930
31 4
kip/in.
kip/in.

58 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

According to AISC Manual Part 13, because the gusset is directly welded to the beam, the weld is designed for the larger of the
peak stress and 1.25 times the average stress:

LRFD ASD
fuwelduffavgu (^) peak
kip/in.

= ()
= ()
=
max. ,
..
.
125
125164
20 5kkip/in.
faweldaffavga (^) peak
kip/in.

= ()
= ()
=
max. ,
..
.
125
125109
13 6kkip/in.
The strength of fillet welds defined in AISC Specification Section J2.4 can be simplified, as explained in AISC Manual Part 8, to
AISC Manual Equations 8-2a and 8-2b. Also, incorporating the increased strength due to the load angle from AISC Specification
Equation J2-5, the required weld size is:

LRFD ASD
D = fuweld
()()+
=
kip/in.sin
kip/in.
21392 10 05 0
20 5
...^15
.
.θ
221392 10 05 0314
620
....^15
.
kip/in.sin.
sixteenths
()()+°
=
D = faweld
()()+
=
kip/in.sin
kip/in.
20928 10 05 0
13 6
...^15
.
.θ
220928 10 05 0314
617
....^15
.
kip/in.sin.
sixteenths
()()+°
=
From AISC Specification Table J2.4, the minimum fillet weld required is c in., which does not control in this case. Therefore,
use a two-sided v-in. fillet weld to connect the gusset plate to the beam.

Check beam web local yielding

The normal force is applied at 16.8 in. away from the beam end (assuming a w-in.-thick end plate), which is less than the beam
depth of 21.4 in. Therefore, use AISC Specification Equation J10-3 as follows:

LRFD ASD
φ Rn = φ Fywtw (2.5 k + lb )
= 1.00(50 ksi)(0.515 in.)[2.5(1.34 in.) + 31.5 in.]
= 897 kips > 269 kips o.k.
Rn Fywtw klb
ΩΩ
=
()+
=()()()

⎡ +
25
50 0 515 25 13 4315
.
ksii..n.⎣⎣ ..in.in.⎤⎦
=>
150
598
.
kips 179 kips o.k.
Alternatively, AISC Manual Table 9-4 may be used to determine the available strength of the beam due to web local yielding.
When the compressive force is applied at a distance less than the beam depth, use AISC Manual Equation 9-45 as follows:

LRFD ASD
φ Rn = φ R 1 + lb (φ R 2 )
= 86.3 kips + (31.5 in.)(25.8 kip/in.)
= 899 kips > 269 kips o.k.
Rn R l R
ΩΩ=+ b Ω
⎛
⎝⎜
⎞
⎠⎟
=+()()
=
12
575315 17 2
599
.. kips in.. kip/in.
kips> 179 kips o.k.
The differences in the calculated strength versus the table values are due to rounding.

AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 59
Check equivalent normal force, Ne

There is no moment on the gusset-to-beam connection, so there is no additional normal force due to the moment. If there were
a moment on the gusset-to-beam connection, the following calculation could be used to determine the equivalent normal force:

LRFD ASD
N V M
ueub l
=+ ub
⎛
⎝⎜
⎞
⎠⎟
=+()
⎛
⎝⎜
⎞
⎠⎟
=
2
2
269
20
31 5
2
269
kips
kip-in.
in..
kkips
NV M
aeab l
=+ ab
⎛
⎝⎜
⎞
⎠⎟
=+()
⎛
⎝⎜
⎞
⎠⎟
=
2
2
179
20
31 5
2
179
kips
kip-in.
in..
kkips
Check beam web local crippling

The normal force is applied at 16.8 in. away from the beam end (assuming a w-in.-thick end plate), which is greater than d /2.
Therefore, AISC Specification Equation J10-4 is applicable:

LRFD ASD
φφ Rtl
d
t
t
EF t
nw t
bw
f
ywf
w
=+⎛
⎝⎜
⎞
⎠⎟
⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
⎡
⎣
⎢
⎢
⎤
⎦
⎥
(^08013) ⎥
2
15
.
.
φ Rn = ()()+ ⎛
⎝
⎜
⎞
⎠
0750 80 0 515 (^13) ⎟
31 5
21 4
0 515
0
...^2.
.
.
.
in. in.
in.
in.
8835
29 000 50 0 835
0 515
15
in.
ksiksi in.
⎛
⎝
⎜
⎞
⎠
⎟
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
× ()()()
.
,.

. iin.

=> 766 kips 269 kips o.k.
R
t ld tt
EF t
t
n
w bw
f
ywf
w
ΩΩ
=
+ ⎛
⎝⎜
⎞
⎠⎟
⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
⎡
⎣
⎢
⎢
⎤
⎦
⎥
(^08013) ⎥
2
15
.
.
Rn
Ω
=
()()+ ⎛
⎝
⎜
⎞
⎠
(^080051513) ⎟
31 5
21 4
0 515
0 835
..^2.
.
.
in..
in.
in.
in.
inn.
ksiksi in.
in.
⎛
⎝
⎜
⎞
⎠
⎟
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
× ()()()
⎡^15
29 000 50 0 835
0 515
.
,.
⎣⎣.
⎢ ⎢ ⎢ ⎢ ⎢ ⎢
⎤
⎦
⎥ ⎥ ⎥ ⎥ ⎥ ⎥
=>
200
511 179
.
kips kips o.k.

Alternatively, AISC Manual Table 9-4 and Equation 9-49 (for x ≥ d /2) may be used to determine the available strength of the
beam for web local crippling:

LRFD ASD
φφ RRnb = ⎡⎣()+ lR ()φ ⎤⎦
=+⎡ ()()
2
2 122 315828
34
⎣⎣ kips .. in. kip/in.⎤⎦
=> 766 26 kips 9 kips o.k.
Rn RlR
Ω= ⎡⎣()ΩΩ+ b ()⎤⎦
= ()()
2
2813 315552
34
⎡⎡⎣ .. kips+in.. kip/in.⎤⎦
=>510 kips 179 kips o.k.
The differences in the calculated strength versus the table values are due to rounding.

60 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

Gusset-to-Column Connection

The required strengths at the gusset-to-column interface are:

LRFD ASD
Required normal strength, 176 kips
Required shear streng
Huc =
tth, Vuc =302 kips
Required axial strength, kips
Required shear strengt
Hac = 117
hh, Vac = 201 kips
Use an end-plate connection between the gusset plate and the column flange and the beam and the column flange, where the end
plate is continuous.

Design bolts at gusset-to-column connection

Use d-in.-diameter ASTM A325-X bolts in standard holes for preliminary analysis. If this bolt type proves to be insufficient,
use d-in.-diameter ASTM A490-X bolts with standard holes. Note that if A490 d-in.-diameter bolts are used for this part of the
connection, they should be used everywhere in this connection and on this job. It is not good practice to use different grades of
the same size bolts on a specific job.

For preliminary design, assume two rows, seven bolts per row, in the gusset-to-column portion of the connection.

The available shear and tensile strengths per bolt, from AISC Manual Tables 7-1 and 7-2, and the required shear and tensile
strengths per bolt are:

LRFD ASD
φ
φ
r
r
nv
nt
=
=
30 7
40 6
.
.
kips
kips
Required shear strength per bolt
kips
bolts
kips/boltkips
ruv =
=<
302
14
21 .. 6307 o.k.
Required tensile strength per bolt
r kips kips
ut ==<
176
14
12 64.. 0 .6 kips o.k.
r
r
nv
nt
Ω
Ω
=
=
20 4
27 1
.
.
kips
kips
Required shear strength per bolt
kips
bolts
kips/bolt < kips
rav =
=
201
14
14 .. 4204 o.k.
Required tensile strength per bolt
r kips kips
at ==<
117
14
83 .7 62 71.kips o.k.
The tensile strength requires an additional check due to the combination of tension and shear. From AISC Specification Section
J3.7, the available tensile strength of the bolts subject to combined tension and shear is:

LRFD ASD
Interaction of shear and tension on bolts is given by
AISC Specification Equation J3-3a
Interaction of shear and tension on bolts is given by
AISC SSpecication
FFF
F
ntnt nt fF
nv
rv nt
Equation J3-3a
ʹ =−13. ≤
φ
Note that the AISC Specification Commentary Section J
has an alternative elliptical formula, Equation C-J3-8a,
that can be used.
Interaction of shear and tension on bolts is given by
AISC Specification Equation J3-3b
Interaction of shear and tension on bolts is given by
AISC SSpecication
FFntnt FFnt fF
nv
rv nt
Equation J3-3b
ʹ =−13. Ω ≤
Note that the AISC Specification Commentary Section J
has an alternative elliptical formula, Equation C-J3-8b,
that can be used.
AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 61
LRFD ASD
From AISC Specification Table J3.
Fnt = 90 ksi
Fnv = 68 ksi
ʹ = ()−
()
⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
=
Fnt 1390 90
68
21 6
0 601
..
.

ksi ksi
0.75 ksi
kips
in.^2
553 .k 69 si< 0 ksi o.k.
The reduced available tensile strength per bolt due to com-
bined forces is:
φ rntntb =φ FA ʹ
= ()()
=>
075536 0 601
242126
...
..
kips in.
kips kips
2
o.k.
From AISC Specification Table J3.
Fnt = 90 ksi
Fnv = 68 ksi
ʹ = ()− ()⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
=
Fnt 1390
20090
68
14 4
0 601
.
..
.

ksi
ksi
ksi
kips
in.^2
553. ks 69 ik< 0 si o.k.
The reduced available tensile strength per bolt due to com-
bined forces is:
rntntbFA
ΩΩ
=
ʹ
()()
=
=>
53 60 601
16 18 36
2.
..
..
kips in.
kips kips
2
o.k.
A 1-in.-end-plate thickness, tp , has been assumed. The gage of the bolts is taken as 5 2 in., which is the standard gage for a
W14× 90 and will work with a 1-in.-thick gusset plate and assuming 2 -in. fillet welds. From Figure 5-4a, the clear distance from
the center of the bolt hole to the toe of the fillet is 1w in. From AISC Manual Table 7-15, the entering clearance for aligned d-in.-
diameter ASTM A325 and A490 bolts is d in. < 1 w in. The next step is to determine the fillet weld size of the end plate-to-gusset
plate connection to ensure that the 5 2 -in. gage will work.

Design gusset-to-end plate weld

The resultant load, R , and its angle with the vertical, θ, are:

LRFD ASD
Ru = ()+()
=
= ⎛
⎝
⎜
⎞
⎠
−
176 302
350
176
302
22
1
kips kips
kips
kips
kips
θ tan ⎟⎟
=°30 2.
Ra = ()+()
=
= ⎛
⎝
⎜
⎞
⎠
−
117 201
233
117
201
22
1
kips kips
kips
kips
kips
θ tan ⎟⎟
=°30 2.
Gusset
plate
End
plate
52 "
1 w""^2 " 1 ""
Fig. 5-4a. Washer clearance for end-plate bolts.
62 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

The weld size is determined from AISC Manual Equation 8-2, including the increase in strength allowed by AISC Specification
Section J2.4 when the angle of loading is not along the weld longitudinal axis. In the following, only the weld length tributary to
the group of bolts is used; therefore, l = 7(3.0 in.) = 21.0 in.

LRFD ASD
Rearranging AISC Manual Equation 8-2a, and incorpo-
rating AISC Specification Equation J2-5, the weld size
required is:
Dreqd ’.
(. .sin
=
+
350
10 05 0 15
kips
2(1.392 kip/in.)(21.0 in.) 30. 2 2)°
= 50 8.
Rearranging AISC Manual Equation 8-2b, and incorpo-
rating AISC Specification Equation J2-5, the weld size
required is:
Dreqd ’.
(. .sin
=
+
233
10 05 0 15
kips
2(0.928 kip/in.)(21.0 in.) 30. 2 2)°
= 50 7.
Therefore, use a two-sided a-in. fillet weld at the gusset-to-end plate connection. Note that this exceeds the minimum size fillet
weld of c in. required by AISC Specification Table J2.4. Note that in the equation for Dreq’d , no ductility factor has been used.
This is because the flexibility of the end plate will allow nonuniform gusset edge forces to be redistributed. If the edge force is
high at one point, the flexible end plate will deform and shed load to less highly loaded locations. Since the required fillet weld
of a-in. is less than the assumed 2 -in. fillet weld in Figure 5-4a, the assumed 5 2 -in. gage can be used.

Check gusset plate tensile and shear yielding at the gusset-to-end-plate interface

The available shear yielding strength of the gusset plate is determined from AISC Specification Equation J4-3, and the available
tensile yielding strength is determined from AISC Specification Equation J4-1 as follows:

LRFD ASD
φφ VFny = Agv
= ()()()()
=
060
1000 60 50 100238
714
.
.. ksi ..in.in.
kkips> 302 kips o.k.
φφ NFny = Ag
= ()()()
=>
09050100 23 8
1 070 176 kips
...
,
ksiin. in.
kips o.k.
Vn FAygv
ΩΩ
=
= ()()()
=
060
06050100 23 8
150
476
.
...
.
ksiin. in.
kipps> 201 kips o.k.
Nn FAyg
ΩΩ
=
=()()()
=>
50 100238
167
713 117
ksiin. in.
kips ki
..
.
pps o.k.
Check prying action on bolts at the end plate

Using AISC Manual Part 9, determine the effect of prying action on the end-plate connection. The end plate is initially assumed
to be 1 in. thick × 10 in. wide. The final end plate thickness may be different.

From AISC Manual Part 9 and Figure 5-4a:

b
bbdb
=
=
ʹ=−
=−
=
52 in. − 1.00 in.
2
225
2
225
2
181
d in.
in.
in.
in.
.
.
.
( Manual E q. 9 -21)
AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 63
a =10.0 in. −^52 in.
.
.
.
2
225
2
125
2
225
in.
in
=
ʹ=+⎛
⎝⎜
⎞
⎠⎟
≤+⎛
⎝⎜
⎞
⎠⎟
=
aadbbb d
.. in.
in. in.
⎛ +
⎝⎜
⎞
⎠⎟
≤⎡ ()+
⎣⎢
⎤
⎦⎥
=<
d in. d in.
2
125225
2
269325
..
.. o.k.
( Manual Eq. 9-27)
From AISC Specification Table J3.3 for a d-in.-diameter bolt, the standard hole dimension is , in.

ρ=ʹ
ʹ
=
=
=
b
a
p
181
269
0 673
.
.
.
in.
in.
pitchofbolts
=3 in.
( Manual Eq. 9-26)
δ=− ʹ
=−
d
p
1
1 , in.
300 in.
0 688
.
=.
( Manual Eq. 9-24)
From AISC Manual Part 9, the available tensile strength, including prying action effects, is:

LRFD ASD
From AISC Manual Equation 9-30a, with B = φ rnt =
24.2 kips previously determined:
t Bb
c pFu
= ʹ
= ()()
()()
=
4
4242 181
09065
0 999
φ
..
.
.
kips in.
3.00in.ksi
iin.
ʹ=
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
()+
α
δρ
1
1
1
1
0 688 10673
0 999
100
t^2
t
c
..
.
.
in.
iin.
0.00
Because 0 determine
from
⎛
⎝
⎜
⎞
⎠
⎟ −
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
≤ ʹ≤
2
1
α 1 , Q
AAISC Equation 9-33
in.
Manual
Q tt
c
=
⎛
⎝
⎜
⎞
⎠
⎟ ()+ ʹ

=
2
1
100
099
δα
.
. 99

10688000
100
2
in.
⎛
⎝⎜
⎞
⎠⎟
⎡⎣+ ()⎤⎦

=
..
.
From AISC Manual Equation 9-30b, with B = rnt /Ω =
16.1 kips previously determined:
t Bb
c pFu
= ʹ
= ()()()
()()
=
Ω 4
1674 16 11 81
65
09
...
.
kips in.
3.00in.ksi
999 in.
ʹ=
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
()+
α
δρ
1
1
1
1
0 688 10673
0 999
100
t^2
t
c
..
.
.
in.
iin.
.00
Because determine
from
⎛
⎝
⎜
⎞
⎠
⎟ −
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
≤ ʹ≤
2
1
0
01 α , Q
AAISC Equation 9-33
in.
Manual
Q tt
c
=
⎛
⎝
⎜
⎞
⎠
⎟()+ ʹ

=
2
1
100
099
δα
.
. 99

10688000
100
2
in.
⎛
⎝⎜
⎞
⎠⎟
⎡⎣+ ()⎤⎦

=
..
.
64 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

LRFD ASD
Because 0 ≤ α′ ≤ 1, determine Q from AISC Manual
Equation 9-33:
ʹ=
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
()+
α
δρ
1
1
1
1
0 688 10673
0 999
100
t^2
t
c
..
.
.
in.
iin.
0.00
Because 0 determine
from
⎛
⎝
⎜
⎞
⎠
⎟ −
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
≤ ʹ≤
2
1
α 1 , Q
AAISC Equation 9-33
in.
Manual
Q t
tc
=⎛
⎝
⎜
⎞
⎠
⎟ ()+ ʹ

=
2
1
100
099
δα
.
. 99

10688000
100
2
in.
⎛
⎝⎜
⎞
⎠⎟
⎡⎣+ ()⎤⎦

=
..
.
From AISC Manual Equation 9-31:
TBavail = Q
=()()
=>
242100
242126
..
..
kips
kips kips o.k.
Because 0 ≤ α′ ≤ 1, determine Q from AISC Manual
Equation 9-33:
ʹ=
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
()+
α
δρ
1
1
1
1
0 688 10673
0 999
100
t^2
t
c
..
.
.
in.
iin.
.00
Because determine
from
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
≤ ʹ≤
2
1
0
01 α , Q
AAISC Equation 9-33
in.
Manual
Q t
tc
=⎛
⎝
⎜
⎞
⎠
⎟()+ ʹ

=
2
1
100
099
δα
.
. 99

10688000
100
2
in.
⎛
⎝⎜
⎞
⎠⎟
⎡⎣ + ()⎤⎦

=
..
.
From AISC Manual Equation 9-31:
TBavail = Q
=()()
=>
161100
161836
..
..
kips
kips kips o.k.
Physically, note that tc is the plate thickness required to develop the bolt strength, B , with no prying action, i.e., q = 0. It is, there-
fore, the maximum effective plate thickness. A thicker plate would not increase the connection’s strength. From this we can see
that the 1-in.-thick end plate is unnecessarily thick. A thinner plate will allow some prying force to develop, resulting in double
curvature in the plate. Try a s-in.-thick end plate.

From AISC Manual Part 9, the available bolt tensile strength, including the effects of prying action, is:

LRFD ASD
ʹ=
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
()+
α δρ 11 1
1
0 688 10673
0 999
t^2
t
c
..
.in.
s in.
⎛⎛
⎝
⎜
⎞
⎠
⎟ −
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
2
1
13 5.
Because α′ > 1, determine Q from AISC Manual
Equation 9-34
in.
Q t
tc
=⎛
⎝
⎜
⎞
⎠
⎟ ()+

=⎛
⎝
2
1
0 999
δ
s in.
⎜⎜.
⎞
⎠⎟
()+
=
2
10688
0 661
.
.
TBavail = Q
=()()
=>
24 20 661
16 01 26
..
..
kips
kips kips o.k.
ʹ=
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
()+
α δρ 11 1
1
0 688 10673
0 999
t^2
t
c
..
.in.
s in.
⎛⎛
⎝
⎜
⎞
⎠
⎟ −
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
2
1
1.35
Because α′ > 1, determine Q from AISC Manual
Equation 9-34
in.
Q t
tc
=⎛
⎝
⎜
⎞
⎠
⎟ ()+

=⎛
⎝⎜
⎞
2
1
0 999
δ
s in.
. ⎠⎟ ()+
2
10688
0 661
.
.
TBavail = Q
=()()
=>
16 10 661
10 68 36
..
..
kips
kips kips o.k.
Use a s-in.-thick end plate. Now that an end-plate thickness is known, check the end plate for the remaining limit states. Note
that the beam-to-column portion of the end-plate connection may require a thicker end plate.

AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 65
Check bolt bearing at bolt holes on end plate

Check the bearing strength at the top bolts, assuming the optional cut on the gusset plate occurs and the end plate edge distance
correspondingly decreases to 1w in., as the available bearing strength will have the lowest value at that location. This edge dis-
tance is reflected in Figure 5-4b. The clear distance, based on this edge distance is:

lc = 1 w in. − 0.5(, in.)
= 1.28 in.
Assuming that deformation at the bolt hole is a design consideration, use AISC Specification Equation J3-6a for the nominal
bearing strength:

Rn = 1.2 lctFu ≤ 2.4 dtFu ( Spec. Eq. J3-6a)
The available strength is determined as follows:

LRFD ASD
φ1.2 lctFu = 0.75(1.2)(1.28 in.)(s in.)(65 ksi)
= 46.8 kips/bolt
φ2.4 dtFu = 0.75(2.4)(d in.)(s in.)(65 ksi)
= 64.0 kips/bolt
Therefore, φ rn = 46.8 kips/bolt
1.2 lctFu /Ω = 1.2(1.28 in.)(s in.)(65 ksi)/2.00
= 31.2 kips/bolt
2.4 dtFu /Ω = 2.4(d in.)(s in.)(65 ksi)/2.00
= 42.7 kips/bolt
Therefore, rn /Ω = 31.2 kips/bolt
Because 46.8 kips/bolt > 30.7 kips/bolt, LRFD (31.2 kips/bolt > 20.4 kips/bolt, ASD), bolt shear controls over bearing strength
at bolt holes, and this check will not govern.

Check block shear rupture of the end plate

The available strength for the limit state of block shear rupture is given in AISC Specification Section J4.3 as follows:

Rn = 0.60 Fu Anv + UbsFuAnt ≤ 0.60 Fy Agv + UbsFu Ant ( Spec. Eq. J4-5)
Shear yielding component:

Agv = (18.0 in. + 1 w in.)(s in.)
= 12.3 in.^2
0.60 Fy Agv = 0.60(50 ksi)(12.3 in.^2 )
= 369 kips
Shear rupture component:

Anv = 12.3 in.^2 − 6.5(, in. + z in.)(s in.)
= 8.24 in.^2
0.60 Fu Anv = 0.60(65 ksi)(8.24 in.^2 )
= 321 kips
Tension rupture component:

Ubs = 1 from AISC Specification Section J4.3 because the bolts are uniformly loaded
Ant = (^) [2.25 in. − 0.5(, in. + z in.)](s in.)
= 1.09 in.^2

UbsFuAnt = 1(65 ksi)(1.09 in.^2 )
= 70.9 kips
66 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

The available strength for the limit state of block shear rupture is determined as follows:

0.60 FuAnv + UbsFuAnt = 321 kips + 70.9 kips
= 392 kips
0.60 FyAgv + UbsFuAnt = 369 kips + 70.9 kips
= 440 kips
Therefore, Rn = 392 kips.

LRFD ASD
φ Rn = ()()
=>
07 5 392 2
588 302
.kips
kips kips o.k.
Rn
Ω
=()()
=>
392 2
200
392 201
kips
kips kips
.
o.k.
Check prying action on column flange

From AISC Manual Part 9:

b
bbd
a
b
=
=
ʹ=−
=−
=
=
52 in. − 0.440 in.
2
253
2
253
2
209
1
d in.
in.
in.
in.
.
.
.
445 550
2
450
..
.
in.in.
in.
−
=
( Manual E q. 9 -21)
Bolts:d"dia. A490-X
Holes: std. ," dia.
PLw"×10"×3'-11d"
3'-11
d""
6 @ 3"
3"
3"
5 @ 3"
Optional cut 10"
Fig. 5-4b. End-plate geometry.
AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 67
The fulcrum point for prying is controlled by the end plate with a = 2.25 in., so use this value for a.

ʹ=+⎛
⎝⎜
⎞
⎠⎟
≤+⎛
⎝⎜
⎞
⎠⎟
=≤(
aadbbb d
2
125
2
2.25 in. +
2
1.25 2.53 in.
.
d in. ⎡ ))+
⎣⎢
⎤
⎦⎥
=<
d in.
in.in.
2
26 .. (^9360)
( Manual Eq. 9-27)
ρ= b ʹʹ
a
p
in.
in.
pitchofbolts
=
=
=
= 3.00 in.
209
269
0 777
.
.
.
( Manual Eq. 9-26)
Using p = 3.00 in. assumes that the column flange is cut above and below the bolt group, which is conservative.
δ=− ʹ
=−
d
p
1
1 , in.
300 in.
0 688
.
=.
( Manual Eq. 9-24)
From AISC Manual Part 9, the available tensile strength including prying action effects is determined as follows:
LRFD ASD
From AISC Manual Equation 9-30a:
t Bb
c pFu
= ʹ
= ()()
()()
=
4
4242 209
09065
107
φ
..
.
.
kips in.
3.00in.ksi
inn.
ʹ=
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
()+
α
δρ
1
1
1
1
0 688 10777
107
0 710
t^2
t
c
..
.
.
in.
iin.
⎛
⎝
⎜
⎞
⎠
⎟ −
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
2
1

From AISC Manual Equation 9-30b:
t Bb
c pFu
= ʹ
= ()()()
()()
=
Ω 4
1674 16 12 09
65
10
...
.
kips in.
3.00in.ksi
7 7in.
ʹ=
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
()+
α
δρ
1
1
1
1
0 688 10777
107
0 710
t^2
t
c
..
.
.
in.
iin.
⎛
⎝
⎜
⎞
⎠
⎟ −
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
2
1

68 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

LRFD ASD
Because α′ > 1, determine Q from AISC Manual
Equation 9-34:
Q t
tc
=⎛
⎝
⎜
⎞
⎠
⎟()+

=⎛
⎝
⎜
⎞
⎠
⎟ ()+
=
2
2
1
0 710
107
10688
0 743
δ
.
.
.
.
in.
in.
From AISC Manual Equation 9-31:
TBavail = Q
=()()
=>
24.2 kips 0.743
18 .. 01 kips 26 kips o.k.
Because α′ > 1, determine Q from AISC Manual
Equation 9-34:
Q t
tc
=⎛
⎝
⎜
⎞
⎠
⎟ ()+

=⎛
⎝
⎜
⎞
⎠
⎟ ()+
=
2
2
1
0 710
107
10688
0 743
δ
.
.
.
.
in.
in.
From AISC Manual Equation 9-31:
TBavail = Q
=()()
=>
16 1 0.743
12 08 36
.
..
kips
kips kips o.k.
If this method were to fail, a more realistic model is given in Tamboli (2010). The effective tributary length of column flange for
a continuous column is:

p
np + π b + 2 a
n
n
p
eff =
()−

=
=
1
numberofrowsof bolts
= 7
boltpitch
=3.00 in.
in.
bb
a
b gage
p
f
eff
=
=
−
= −
=
= −
2
1455
2
4.50 in.
71
=2.53 in.
. 2 in.

(()()+ ()+ ()

=
300253 2450
7
4.99 in.
.. in. π in.i. n.
Using peff in place of p in the AISC Manual prying equations and following the procedure from AISC Manual Part 9:
ʹ=
=>=
ʹ=

b
aa
a
209
450225
269
.
..
.
in.
in.in.
in.
Use the smaller of and
, in.
in.
aa
d
p
h
.
.
.
.
ρ
δ
=
=−
=−
=
0 777
1
1
499
0 812
AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 69
LRFD ASD
t Bb
c pFu
= ′
= ()()
()()
=
4
4242 209
09065
0 832
φ
..
.
.
kips in.
4.99in.ksi
iin.
=
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
()+
α′
δρ
1
1
1
1
0 812 10777
0 832
071
t^2
t
c
..
.
.
in.
00
1
2
in.
0.259
⎛
⎝
⎜
⎞
⎠
⎟ −
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
Because 0 ≤ α′ ≤ 1, determine Q from AISC Manual
Equation 9-33
Q t
tc
=⎛
⎝
⎜
⎞
⎠
⎟ ()+

=
2
1
071
δα′
. 00
0 832

10 812 0 259
0 881
24 2
2
.
..
.
.
⎛
⎝⎜
⎞
⎠⎟
⎡⎣+()()⎤⎦

=
=
=
TBavail Q
(()kips
=> 21 ..kips 3126 o.k. kips
()0.881

t Bb
c pFu
= ′
= ()()()
()()
=
4
4167 16 1209
65
08
Ω
...
.
kips in.
4.99 in.ksi
332 in.
ʹ=
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
()+
α
δρ
1
1
1
1
0 812 10777
0 832
071
t^2
t
c
..
.
.
in.
00
1
0 259
2
in.
⎛
⎝
⎜
⎞
⎠
⎟ −
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=.
Because 0 ≤ α′ ≤ 1, determine Q from AISC Manual
Equation 9-33
Q t
tc
=⎛
⎝
⎜
⎞
⎠
⎟()+ ′

=⎛
⎝⎜
⎞
⎠⎟
+()(

2
2
1
0 710
0 832
10 812 0 259
δα
.
.
in. ..
in. ))
⎡⎣ ⎤⎦
=0 881.
TBavail = Q
=()()
=>
16 1 0.881
14 28 36
.
..
kips
kips kips o.k.
By this method the calculated available strength has increased by:

LRFD ASD
21 31 80
18 0
100 18 3
..
.
%.%
kips kips
kips
()−
×=
14 21 20
12 0
..100 18 3
.
kips kips %.%
kips
()− ×=

Thus, this method is considerably less conservative than the “cut column” model.

Check bearing on column flange

Because tf = 0.710 in. > tp = s in., bolt bearing on the column flange will not control the design, by inspection.

Beam-to-Column Connection

This section addresses the design of the portion of the end plate that connects the beam to the column. The required shear strength
is equal to Vub (LRFD) or Vab (ASD), based on the brace force, plus the beam reaction from the Given section of 50 kips (LRFD)
or 33.3 kips (ASD). The Vub and Vab force is reversible as the brace force goes from tension to compression, but the gravity beam
shear always remains in the same direction. Therefore, Vub (or Vab ) and the reaction should always be added even if shown in
opposite directions as in Figure 5-3.

70 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

The axial force in the beam shown in Figure 5-3 is affected by the transfer force, Aub, of 100 kips (LRFD) or Aab of 66.7 kips
(ASD). When the braces are in tension, the transfer force is compression as shown in Figure 5-1, and will increase the required
brace tensile strength of the next lower brace to:

LRFD ASD
716
47 2^976
kips kips
sin.°=
477
47 2^650
kips kips
sin.°=
Figure 5-3 shows that the axial force between the beam and column from equilibrium would be Aub + Huc for LRFD and Aab +
Hac for ASD, but it has been shown that frame action, as discussed in Section 4.2.6, will reduce the force Huc for LRFD or Hac
for ASD_._ Section 4.2.6 provides the following formula to estimate the moment in the beam due to the effect of the admissible
distortional forces from Tamboli (2010):

M P
Abc
II
I
b
I
c
bc
D bc
bc
bc
= ⎛
⎝⎜
⎞
⎠⎟ +
⎛
⎝
⎜
⎜⎜
⎞
⎠
⎟
⎟⎟
⎛ +
⎝
⎜⎜
⎞
⎠
(^62) ⎟⎟
22
(4 -12)
This formula is valid for bracing arrangements such as those shown in Figure 2-1, i.e., those involving one beam and two col-
umns. Other arrangements would involve a different formula. For cantilever situations, gravity forces rather than lateral forces
will probably dominate and Aub + Huc for LRFD or Aab + Hac for ASD should be used.
As given, the required strength of the brace is :
LRFD ASD
Pu = 840 kips Pa = 560 kips
The values of b and c to be used in the Tamboli equation are:
b l
c l
b
c
=
=()()
=
=
=
()
2
250100
2
150
2
25 0^118 in.
...
.
ft 12.0in ft
in.
ft
in.
in.
ft
in.
12 0
12 0
100
2
139
.
.
.
⎛
⎝⎜
⎞
⎠⎟
⎛
⎝⎜
⎞
⎠⎟
=
I
b
I
c
b
c
=
=
=

()
=
1 830
150
12 2
2 2 999
139
14 4
,
.
.
in.
in.
in.
in.
in.
in.
4
3
4
3
AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 71
The required flexural strength of the beam is:

LRFD ASD
MuD =
()()()
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
×
()
6 840
26 2 150 139
1 830
kips
in.in. in.
in.
2
4
.
, 9999
122144
150 139
150
in.^22
in.in.
(^4) in.in.
33

()
+
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
()+()
.. iin.in.
kip-in.
()()

⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
139
1 270,
Using previously determined variables, β and eb :
HuD MuDe
b
= +
=
+
=
β
1 270
12 01 07
55 9
,
..
.
kip-in.
in.in.
kips
MaD =
()()()
⎛
⎝
⎜
⎜
⎞
⎠
⎟
⎟
×
()
6 560
26 2 150 139
1 830
kips
in.in. in.
in.
2
4
.
, 9999
12 21 44
150 139
150
in.^22
in.in.
in.in.
i
4
33
()
+
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
()+()
.. nn. in.
kip-in.
()()

⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
139
848
Using previously determined variables, β and eb :
H M
aD e
aD
b
=
+
=
+
=
β
848
12 01 07
37 4
kip-in.
in.in.
kips
..
.
If this value of HD is used, the axial force between the beam and column will be:

LRFD ASD
Hu = 176 kips − 55.9 kips + 100 kips
= 220 kips
Ha = 117 kips − 37.4 kips + 66.7 kips
= 146 kips
A recent study (Fortney and Thornton, 2014) has shown that the average ratio of ( Hc − Hd + A )/( Hc + A ) is about 70%, but
the standard deviation of about 0.33 was too large to make a recommendation for design. This study also shows that using
max ( Hc , A ) as the axial force may not be justified. This Design Guide will use the justifiable axial force of Hc − Hd + A for the
following calculations:

LRFD ASD
Required Shear Strength
Vu = Vub + Reaction
= 269 kips + 50 kips
= 319 kips
Required Axial Strength
Tu = 176 kips − 55.9 kips + 100 kips
= 220 kips
Required Shear Strength
Va = Vab + Reaction
= 179 kips + 33.3 kips
= 212 kips
Required Axial Strength
Ta = 117 kips − 37.3 kips + 66.7 kips
= 146 kips
72 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

Design bolts at beam-to-column connection

For the connection geometry, see Figure 5-1. Try (12) d-in.-diameter ASTM A325-X bolts in the end-plate connection of the
beam to the column.

As determined previously, the available shear strength of a d-in.-diameter ASTM A325-X bolt is 30.7 kips for LRFD and
20.4 kips for ASD. The required shear and tensile bolt strengths are:

LRFD ASD
ruv =
=<
319
12
266307
kips
bolts
..kips/boltkips o.k.
rut =
=
220
12
18 3
kips
bolts
. kips/bolt

r
r
av
at
=
=<
=
212
12
17 72 04
146
kips
bolts
kips/boltkips
kips
..o.k.
112
12 2
bolts
=. kips/bolt
The available tensile strength considers the effects of combined tension and shear. From AISC Specification Section J3.7, the
available tensile strength of the bolts subject to combined tension and shear is:

LRFD ASD
Interaction of shear and tension on bolts is given by AISC
Specification Equation J3-3a:
FF ʹ =− F ≤
F
ntnt nt fF
nv
φ rv nt
From AISC Specification Table J3.2:
F
F
F
nt
nv
nt
=
=
ʹ = ()−
()
90
68
1390 90
68
26 6
ksi
ksi
ksi ksi
0.75 ksi
.. kipps
in.
ksiksi

0 601^2
38990
.
.
⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
=<o.k.
The reduced available tensile force per bolt due to com-
bined forces is:
φφ rFntnt = ʹ Ab
= ()()
=
075389 0 601
175183
...
..
kips in.
kips < kips
2
n.g.
Interaction of shear and tension on bolts is given by AISC
Specification Equation J3-3b:
FF ʹ =− F ≤
F
nt nt ntfF
nv
rv nt
Ω
From AISC Specification Table J3.2:
F
F
F
nt
nv
nt
=
=
′ = ()− ()

90
68
13 90
20090
68
17 7
ksi
ksi
ksi
ksi
ksi
kips
.
..
00 601
39 09 0

.
.
in.
ksiksi
2
⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
=<o.k.
The reduced available tensile force per bolt due to com-
bined forces is:
rFntntbA
ΩΩ
=
ʹ
=
()()
=
3890601
200
117122
..
.
..
kips in.
kips < kips
2
n.g.
AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 73
Try d-in.-diameter ASTM A490-X bolts.

LRFD ASD
From AISC Specification Table J3.2:
F
F
F
nt
nv
nt
=
=
ʹ = ()−
()
113
84
13113 113
84
26
ksi
ksi
ksi ksi
0.75 ksi
..^66
0 601
67 5 113

kips
in.
ksiksi
.^2
.

⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
=< o.k.
The reduced available tensile force per bolt due to com-
bined forces is:
φφ rFntntb = ʹ A
= ()()
=
075675 0 601
304183
...
..
kips in.
kips > kips
2
o.k.
From AISC Specification Table J3.2:
F
F
F
nt
nv
nt
=
=
ʹ = ()− ()

113
84
13113 20 0 113
84
17 7
ksi
ksi
ksi ksi
ksi
... kiips
in.
ksiksi

0 601^2
67 7 113
.
.
⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
=< o.k.
The reduced available tensile force per bolt due to com-
bined forces is:
rFntntbA
ΩΩ
= ʹ
=
()()
=>
6770601
200
20 3
..
.
.
kips in.
kips 12.2 kips
2
o.k.
Because A490-X bolts are required for the beam-to-column connection, they will be used everywhere in the connection. Using
A325 and A490 bolts of the same diameter in any one connection, or even within the same project, is not recommended.

Design beam web-to-end plate weld

Using V and T , which were previously determined, the resultant load, R , and its angle with the vertical, θ, are:

LRFD ASD
RVuu =+ Tu
= ()+()
=
= −
22
22
1
220 319
388
220
kips kips
kips
θ tan kips
3319
34 6
kips
⎛
⎝⎜
⎞
⎠⎟
=°.
RVaa =+ Ta
= ()+()
=
= −
22
22
1
146 212
257
146
2
kips kips
kips
θ tan kips
112
34 6
kips
⎛
⎝⎜
⎞
⎠⎟
=°.
The weld size is determined from AISC Manual Equation 8-2, including the increase in strength allowed by AISC Specification
Section J2.4 when the angle of loading is not along the weld longitudinal axis. In the following, only the weld length tributary to
the group of bolts is used; therefore, l = 6(3.00 in.) = 18.0 in.

LRFD ASD
Rearranging AISC Manual Equation 8-2a, and incorpo-
rating AISC Specification Equation J2-5, the weld size
required is:
Dreqd ’.
....sin.
=
()()+
388
21392 18010050 15 34 6
kips
kip/in.in.()°°
= 63 8.
Rearranging AISC Manual Equation 8-2b, and incorpo-
rating AISC Specification Equation J2-5, the weld size
required is:
Dreqd ’.
....sin.
=
()()+
257
20928 18010050 15 34 6
kips
kip/in.in.()°°
= 63 4.
Therefore, use a two-sided v-in. fillet weld to connect the beam web to the end plate. Note that this exceeds the minimum size
fillet weld of 4 in. required by AISC Specification Table J2.4.

74 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

Check the 5 2 -in. gage with v -in. fillet welds

From AISC Manual Table 7-15, the required clearance for d-in.-diameter bolts with circular washers is:

C 3 reqd
52 in.
22
,’ =
=− −
d in.
Clearance 0.515 in. v in.
= z in. > 2 d in. o.k.
Therefore, the 5 2 -in. gage is acceptable with v-in. fillet welds.

Check prying action on bolts and end plate

Using AISC Manual Part 9, determine the effect of prying action on the end-plate connection. The end plate is assumed to be
w in. thick × 10 in. wide:

bbdb
=
ʹ=−
2.49 in.
2
in.
=−
=
2.49 in.
20 5.
b =^52 in. − 0.515 in.
2
2
d in.
( Manual E q. 9 -21)
in.
in.
= −
=<
10052 in.
2
225125
.
..
a
bb
aadbbb d
o.k.
ʹ=+⎛
⎝⎜
⎞
⎠⎟
≤+⎛
⎝⎜
⎞
(^2) ⎠⎟
125
2
.
in.3
=+⎛
⎝⎜
⎞
⎠⎟
≤⎡ ()+
⎣⎢
=<
225 2 1.2 5249
269
..
...55 in.
d in. d in.
2
⎤
⎦⎥
( Manual Eq. 9-27)
From AISC Specification Table J3.3 for a d-in.-diameter bolt, the standard hole dimension is , in.
ρ
δ
= ʹʹ
=
=
=
=−ʹ
b
a
p
d
p
205
269
0 762
300
1
.
.
.
.
in.
in.
pitchofbolts
in.
==−
=
1
300
0 688
, in.
in..
.
=
( Manual Eq. 9-26)

AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 75
From the AISC Manual Part 9, the available tensile strength including prying action effects is:

LRFD ASD
From AISC Manual Equation 9-30a:
t Bb
c pFu
= ʹ
= ()()
()()
=
4
4304 205
09065
119
φ
..
.
.
kips in.
3.00in.ksi
inn.
From AISC Manual Equation 9-35:
in.
s in.
ʹ=
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
()+
α
δρ
1
1
1
1
0 688 10762
119
t^2
t
c
..
⎛⎛.
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
2
1
2.17
Because α′ > 1, α′ = 1.00
Determine Q from AISC Manual Equation 9-33:
Q t
tc
=⎛
⎝
⎜
⎞
⎠
⎟ ()+ ʹ

=⎛
⎝⎜
⎞
⎠⎟
⎡⎣+()()⎤

2
2
1
119
10688 100
δα
s in.
in..
..⎦⎦
=0 466.
From AISC Manual Equation 9-31:
Q tt
c
=
⎛
⎝
⎜
⎞
⎠
⎟ ()+ ʹ

=⎛
⎝⎜
⎞
⎠⎟
⎡⎣+()()⎤

2
2
1
119
10688 100
δα
s in.
in..
..⎦⎦
=
=
=(
0 466
30 4
.
.
From AISC Equation 9-31:
kips
Manual
TBavail Q
))( )
=<
0 466
142183
.
..kips n.g. kips
From AISC Manual Equation 9-30b:
t Bb
c pFu
= ′
= ()()()
()()
=
Ω 4
1674 20 32 05
65
11
...
.
kips in.
3.00in.ksi
9 9in.
From AISC Manual Equation 9-35:
in.
′=
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
()+
α
δρ
1
1
1
1
0 688 10762
119
t^2
t
c
..
.
s in.
⎛⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
2
1
21 7.
Because α′ > 1, α′ = 1.00
Determine Q from AISC Manual Equation 9-33:
Q t
tc
=⎛
⎝
⎜
⎞
⎠
⎟ ()+ ′

=
2
1 δα
s in.
119
10688 100
0 466
2
.
..
.
⎛
⎝⎜
⎞
⎠⎟
⎡⎣+()()⎤⎦

=
From AISC Manual Equation 9-31:
in.
′=
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
()+
α
δρ
1
1
1
1
0 688 10762
119
t^2
t
c
..
.
s in.
⎛⎛
⎝
⎜
⎞
⎠
⎟ −
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
′> ′=
2
1
217
100
.
Because 1, use.
Determine
αα
QM from AISC anual Equation 9-33:
Q tt
c
=
⎛
⎝
⎜
⎞
⎠
⎟ ()+ ′

=
2
1 δα
s in.
From AISC Eq
119
10688 100
0 466
2
.
..
.
⎛
⎝⎜
⎞
⎠⎟
⎡⎣+()()⎤⎦

=
Manual uuation 9-31:
kips
kips kips
TBavail = Q
=()()
=<
2030466
946122
..
..n.g.
The connection has failed. Since α′ > 1, it is known that the s-in.-thick end plate contributes to the failure.

76 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

Try an end plate of increased thickness, tp = w in.

LRFD ASD
′= in.
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
α^1
0 688 10762
(^1191)
125
2
..
.
.
w in.
Because α′ > 1, use α′ = 1.00
Determine Q from AISC Manual Equation 9-33:
Q
Tavail
=⎛
⎝⎜
⎞
⎠⎟
⎡⎣+()()⎤⎦
=
=
w in.
119 in.
10688 100
0 671
0 671
2
.
..
.
.330 4
204183
.
..
kips
kips kips
()
=>o.k.
′= in.
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
=
α^1
0 688 10762
(^1191)
125
2
..
.
.
w in.
Because α′ > 1, use α′ = 1.00
Determine Q from AISC Manual Equation 9-33:
Q
Tavail
=⎛
⎝⎜
⎞
⎠⎟
⎡⎣ +()()⎤⎦
=
=
w in.
119 in.
10688 100
0 671
067
2
.
..
.
.1 1203
136122
.
..
kips
kips kips
()
=>o.k.
Use the w-in.-thick end plate.
Check prying action on column flange
From the calculations for the gusset-to-column connection with d-in.-diameter bolts:
b ′ = 2.09 in.
a ′ = 2.69 in.
ρ = 0.777
p = 3.00 in.
δ = 0.688
LRFD ASD
tc = ()()
()()
=
=
4304 209
090300 65
120
1
06
.kips.in.
..in .ksi
.in.
′
.
α
88810777
120
0 710
1
152100
2
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
==
=
.
.
.
., use α′.
Q 00 710
120
10688100
0 591
0 591 30 4

.^2
.

..
.
..ki
⎛
⎝⎜
⎞
⎠⎟
⎡⎣+ ()⎤⎦

=
Tavail = pps
.kips.kips
()
=< 180183 n.g.
tc = ()()()
()()
=
=
41 67 20 3209
30065
1.21 in.
1
0
..kips .in.
.in. ksi
α′
...
.
.
., ′.
68810777
121
0 710
1
156100
2
()+
⎛
⎝⎜
⎞
⎠⎟
−
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥
== use α
QQ
Tavail
=⎛
⎝⎜
⎞
⎠⎟
⎡⎣+ ()⎤⎦

=
=
0 710
120
10688100
0 591
0 591 20 3
.^2
.

..
.
..kkips
.kips.kips
()
=< 120122 n.g.
The check indicates that the column flange is deficient. However, the effective length of the connection need not be limited to the
18 in. assumed. An increase of less than z in. per bolt, or slightly more than 4 in. total, in effective length is all that is required
to make the flange sufficient. This slight increase is okay by inspection. A yield-line analysis could be used to determine a better
estimate of the effective length.

AISC DESIGN GUIDE 29 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / 77
Check bolt bearing at end plate

By the calculations for the gusset-to-column connection, bearing strength at the bolt holes in the beam-to-column connection
will not control. The calculations for the bearing strength at bolt holes at this location would be similar to those presented for the
gusset-to-column connection, except that the edge distance will be greater than the 1 4 in. used there.

Check block shear rupture on end plate

The available strength for the limit state of block shear rupture is given in AISC Specification Section J4.3 as follows:

Rn = 0.60 Fu Anv + UbsFu Ant ≤ 0.60 Fy Agv + Ubs Fu Ant ( Spec. Eq. J4-5)
The edge distance to the bottom of the end plate will be 21.4 in.− 18.0 in.+ 1.00 in. = 4.40 in., with a 1.00 in. bottom projection.
The controlling block shear failure path cuts through each line of bolts and then to the outer edge of the end plate on each side.

Shear yielding component:

Agv = (15.0 in. + 4.40 in.)(w in.)
= 14.6 in.^2
0.6 Fy Agv = 0.6(50 ksi)(14.6 in.^2 )
= 438 kips
Shear rupture component:

Anv = 14.6 in.^2 − 5.5(, in. + z in.)(w in.)
= 10.5 in.^2
0.6 FuAnv = 0.6(65 ksi)(10.5 in.^2 )
= 410 kips
Tension rupture component:

Ubs = 1 from AISC Specification Section J4.3 because the bolts are uniformly loaded
Ant = (w in.)[2.25 in. − 0.5(, in. + z in.)]
= 1.31 in.^2
UbsFuAnt = 1(65 ksi)(1.31 in.^2 )
= 85.2 kips
The available strength for the limit state of block shear rupture is determined as follows:

0.60 Fu Anv + UbsFuAnt = 410 kips + 85.2 kips
= 495 kips
0.60 Fy Agv + UbsFuAnt = 438 kips + 85.2 kips
= 523 kips
Therefore, Rn = 495 kips.

LRFD ASD
φ Rn = ()()
=>
07 5 495 2
743 319
. kips
kips kips o.k.

Rn
Ω
=()()
=>
495 2
200
495 212
kips
kips kips
.
o.k.
78 / VERTICAL BRACING CONNECTIONS—ANALYSIS AND DESIGN / AISC DESIGN GUIDE 29

Check beam shear strength

The available beam shear strength is determined from AISC Specification Section J4.2, assuming shear yielding controls:

LRFD ASD
φφ RFny = Agv
= ()()()()
=
060
1000 60 50 2140515
331
.
.. ksii..n. in.
kipssk> 319 ips o.k.
Rn FAygv
ΩΩ
=
= ()()()
=>
060
06050214 0 515
150
220
.
...
.
ksiin. in.
kips 2212 kips o.k.
Check column shear strength

The available column shear strength is:

LRFD ASD
φφ RFny Agv
ksiin. in.
ki
=
= ()()()()
=
060
1000 60 50 1400440
185
.
.. ..
pps > kips 176 o.k.
Rn FAygv
ΩΩ
ksiin. in.
kips
=
= ()()()
=
060
06050140 0 440
150
123
.
...
.
>>117 kips o.k.
Discussion

A final comment on the end-plate thickness is in order. To calculate lh and α, tp = 1.00 in. was assumed. The final plate thickness
was tp = w in. This will cause α and α to be slightly different and will cause a very small couple to exist on the gusset-to-beam
interface. This couple can be ignored in the design of this connection.

The final completed design is shown in Figure 5-1. Note that no weld is specified for the flanges of the W21× 83 beam to the end
plate other than those out to approximately the k 1 dimension (the 1-in. returns). These welds are not required for the uniform
force transfer assumed in the calculations for the forces shown in Figure 5-3. If the flanges are fully welded to the end plate, the
bolts close to the flanges will see more load than those further away. This will affect the force distribution, which was assumed to
be supplied uniformly to the column flange as well, and column flange stiffeners may be required adjacent to these more highly
loaded bolts. It is important to recognize that a certain load path has been assumed by the use of the forces in Figure 5-3 and that
the connection parts have been developed from that assumed load path. Thus, it is important to arrange the connection to allow
the assumed load path to be realized.

If the flanges are welded to the end plate, this fact should be considered in the design from the outset. It sometimes happens
that a shop will weld the flanges to the end plate with AISC minimum fillet welds because it “looks better” and “more is better.”
But in this case, more may not be better. Fracture of the bolts and/or weld close to the flange may occur. However, if no column
stiffeners are provided adjacent to the beam flanges, the bolts near the flanges will probably not be overloaded because of column
flange flexibility.

The gusset “clip” of Figure 5-1 is used to separate the welds of the gusset to the beam and the gusset to the end plate. No weld
passes through this clip.