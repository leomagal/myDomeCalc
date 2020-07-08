import decimal as D
import math

R = 1       # RADIUS
Pi = D.Decimal(str(math.pi))

# Icosahedron Coordinate Equations
# See fileS ICOSA_COORD*.GIF or for complete demonstration see
# http://www.vb-helper.com/tutorial_platonic_solids.html

# Z2 plane intersects icosahedron forming a pentagon shape in vertices b to f
# Pentagon Angles
t1 = D.Decimal(2 * Pi / 5)
t2 = D.Decimal(Pi / 10)
t3 = D.Decimal(-3 * Pi / 10)
t4 = D.Decimal(Pi / 5)

S_t = 2 * R * math.sin(t4)
S = D.Decimal(str(S_t))     # Side length of Z2 plane pentagon

H_t = math.cos(t4) * R  # Height of Z2 plane pentagon
H = D.Decimal(str(H_t))

Cx_t = R * math.cos(t2)
Cx = D.Decimal(str(Cx_t))

Cy_t = R * math.sin(t2)
Cy = D.Decimal(str(Cy_t))

H1 = D.Decimal(str(math.sqrt(S * S - R * R)))    # Distance from pentagon plane to apex
H2 = D.Decimal(str(math.sqrt((H + R) * (H + R) - (H * H))))  # Distance between pentagon planes

Z2 = D.Decimal((H2 - H1) / 2)  # Coordinate of points (b-f)
Z1 = D.Decimal(Z2 + H1)  # Coordinate of point (a)

# a = (   0,   0,  Z1)
# b = (   0,   R,  Z2)
# c = (  Cx,  Cy,  Z2)
# d = ( S/2,  -H,  Z2)
# e = (-S/2,  -H,  Z2)
# f = ( -Cx,  Cy,  Z2)
# g = (   0,  -R, -Z2)
# h = ( -Cx, -Cy, -Z2)
# i = (-S/2,   H, -Z2)
# j = ( S/2,   H, -Z2)
# k = (  Cx, -Cy, -Z2)
# l = (   0,   0, -Z1)

Icosa = [ ( 0, 0, Z1 ),( 0, R, Z2 ), ( Cx, Cy, Z2 ), ( S/2, -H, Z2 ), ( -S/2,  -H,  Z2 ), ( -Cx, Cy, Z2), ( 0, -R, -Z2),
    ( -Cx, -Cy, -Z2), (-S/2, H, -Z2), ( S/2, H, -Z2), ( Cx, -Cy, -Z2), ( 0, 0, -Z1 )]

print(Icosa[0])

# Outra forma

# self.verts.append(vector(0.0, 1.0, TAU_GOLDEN_RATIO))  # A  0
# self.verts.append(vector(0.0, -1.0, TAU_GOLDEN_RATIO))  # B  1
# self.verts.append(vector(0.0, -1.0, -TAU_GOLDEN_RATIO))  # C  2
# self.verts.append(vector(0.0, 1.0, -TAU_GOLDEN_RATIO))  # D  3
#
# self.verts.append(vector(TAU_GOLDEN_RATIO, 0.0, 1.0))  # E  4
# self.verts.append(vector(-TAU_GOLDEN_RATIO, 0.0, 1.0))  # F  5
# self.verts.append(vector(-TAU_GOLDEN_RATIO, 0.0, -1.0))  # G  6
# self.verts.append(vector(TAU_GOLDEN_RATIO, 0.0, -1.0))  # H  7
#
# self.verts.append(vector(1.0, TAU_GOLDEN_RATIO, 0.0))  # I  8
# self.verts.append(vector(-1.0, TAU_GOLDEN_RATIO, 0.0))  # J  9
# self.verts.append(vector(-1.0, -TAU_GOLDEN_RATIO, 0.0))  # K  10
# self.verts.append(vector(1.0, -TAU_GOLDEN_RATIO, 0.0))  # L  11