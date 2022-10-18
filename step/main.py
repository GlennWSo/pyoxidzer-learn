from typing import Optional
from ngsolve import Mesh

from netgen.occ import OCCGeometry
from netgen.meshing import MeshingStep

import numpy as np
from pyvista import PolyData

def get_verts(mesh: Mesh):
    vert_list = [v.point for v in mesh.vertices ]
    return np.array(vert_list, dtype=float)

def get_faces(mesh: Mesh):
    face_list = [[v.nr for v in face.vertices] for face in mesh.faces]
    return np.array(face_list, dtype=int)

def get_poly_data(mesh: Mesh):
    faces = np.pad(get_faces(mesh), ((0,0), (1,0)), constant_values=3)
    return PolyData(get_verts(mesh), faces=faces)

def generate_surf_mesh(geo: OCCGeometry, maxh=1):
    return Mesh(geo.GenerateMesh(maxh=maxh, perfstepsend=MeshingStep.MESHSURFACE))

def step2poly(path: str, maxh: Optional[float]=None) -> PolyData:
    geo = OCCGeometry(path)
    mesh = Mesh(geo.GenerateMesh(maxh=maxh, perfstepsend=MeshingStep.MESHSURFACE))
    return get_poly_data(mesh)

if __name__=="__main__":

    # mesh = generate_surf_mesh(unit_cube)
    step_path = "models/cylinder.step"

    poly = step2poly(step_path, maxh=1.0)
    print(poly.n_open_edges)

    poly.plot()
