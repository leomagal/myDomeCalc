import sys
import math

from G3Object import *
from G3mathutil import *
from visual import *
# class G3Object:
#
#     def __init__(self):
#         self.location = location
#         self.northpole = vector(0, 0, 1)
#         self.equator = vector(0, 1, 0)
#         self.upperLimit = vector(1, 1, 1);
#         self.lowerLimit = vector(-1, -1, -1)
#         self.inscribedSphereRadius = 1

# class G3Edge:
#     def __init__(self, vec1, vec2):
#         self.vec1 = vec1
#         self.vec2 = vec2
#         self.color = color.green
#
#
# class G3Face:
#     def __init__(self, vertices):
#         self.vertices = vertices
#
#     def isEqual(self, vertices):
#         for v in self.vertices:
#             if v not in vertices:
#                 return False
#         return True
#
#     def toString(self):
#         return "(" + str(self.vertices[0]) + "," + str(self.vertices[1]) + "," + str(self.vertices[2]) + ")"
#
#
# class G3FaceList:
#     def __init__(self):
#         self.faces = []
#
#     def isIn(self, face):
#         for f in range(len(self.faces)):
#             if self.faces[f].isEqual(face.vertices):
#                 return f
#         return -1


# class G3Icosahedron(G3Object):
#     # vertice index
#     global A, B, C, D, E, F, G, H, I, J, K, L
#     (A, B, C, D, E, F, G, H, I, J, K, L) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)  # define some constants
#
#     def __init__(self, loc):
#         G3Object.__init__(self, loc)
#
#         self.edgelen = 2  # inital lengh for all edges (unless subdevided then its the longest edge length)
#
#         self.edgelencount = 0
#         self.verts = []
#         self.edges = []
#         self.faces = G3FaceList()
#
#         # initial 12 vertices based on interlocking golden rectangles.
#         self.verts.append(vector(0.0, 1.0, TAU_GOLDEN_RATIO))  # A  0
#         self.verts.append(vector(0.0, -1.0, TAU_GOLDEN_RATIO))  # B  1
#         self.verts.append(vector(0.0, -1.0, -TAU_GOLDEN_RATIO))  # C  2
#         self.verts.append(vector(0.0, 1.0, -TAU_GOLDEN_RATIO))  # D  3
#
#         self.verts.append(vector(TAU_GOLDEN_RATIO, 0.0, 1.0))  # E  4
#         self.verts.append(vector(-TAU_GOLDEN_RATIO, 0.0, 1.0))  # F  5
#         self.verts.append(vector(-TAU_GOLDEN_RATIO, 0.0, -1.0))  # G  6
#         self.verts.append(vector(TAU_GOLDEN_RATIO, 0.0, -1.0))  # H  7
#
#         self.verts.append(vector(1.0, TAU_GOLDEN_RATIO, 0.0))  # I  8
#         self.verts.append(vector(-1.0, TAU_GOLDEN_RATIO, 0.0))  # J  9
#         self.verts.append(vector(-1.0, -TAU_GOLDEN_RATIO, 0.0))  # K  10
#         self.verts.append(vector(1.0, -TAU_GOLDEN_RATIO, 0.0))  # L  11
#
#         self.inscribedSphereRadius = self.verts[0].mag
#
#         # 30 edges
#         self.calculateEdges()
#
#         # 20 faces
#         # calculate the faces
#         self.calculateFaces()
#
#     # calculate the edges. we walk though the vertices and check each one with all the rest
#     # add any where the distance between the vertices is equal to the edge length.
#     def calculateEdges(self):
#         # calculate the edges by finding the edge between two vertices that
#         # are the standard length.
#         for i in range(len(self.verts)):
#             for j in range(i + 1, len(self.verts)):
#                 distvec = self.verts[i] - self.verts[j]
#                 dist = mag(distvec)
#                 if almostEqual(dist, self.edgelen) or dist < self.edgelen:
#                     self.edges.append(G3Edge(i, j))
#
#     # find the faces by looking at each edge then find a vertic equal distance from
#     # end points of the edge.
#     def calculateFaces(self):
#         # 20 faces
#         # calculate the faces
#         for e in range(len(self.edges)):
#             for v in range(len(self.verts)):
#                 if v != self.edges[e].vec1 and v != self.edges[e].vec2:
#                     distvec = self.verts[v] - self.verts[self.edges[e].vec1]
#                     dist = mag(distvec)
#                     if almostEqual(dist, self.edgelen) or dist < self.edgelen:
#                         distvec = self.verts[v] - self.verts[self.edges[e].vec2]
#                         dist = mag(distvec)
#                         if almostEqual(dist, self.edgelen) or dist < self.edgelen:
#                             newface = G3Face([v, self.edges[e].vec1, self.edges[e].vec2])
#                             if self.faces.isIn(newface) < 0:
#                                 self.faces.faces.append(newface)
#
#     def drawEdge(self, e, acolor):
#         v1 = self.verts[e.vec1] + self.location
#         v2 = self.verts[e.vec2] + self.location
#         e.thecurve = curve(color=acolor)
#         e.thecurve.append(v1)
#         e.thecurve.append(v2)
#
#     def drawWire(self, acolor):
#         for e in self.edges:
#             self.drawEdge(e, acolor)


G3Icosahedron(vector(0,0,0,))