import numpy as np
import plotly.graph_objects as go

def proyectar_tesseracto_4d():
    vertices_4d = np.array([[x, y, z, w] for x in [1, -1] for y in [1, -1] for z in [1, -1] for w in [1, -1]])

    vertices_3d = vertices_4d[:, :3] + 0.5 * vertices_4d[:, 3:4]

    return vertices_3d

vertices_3d = proyectar_tesseracto_4d()

aristas = [
    (0, 1), (0, 2), (0, 4), (0, 8), 
    (1, 3), (1, 5), (1, 9), (2, 3), 
    (2, 6), (2, 10), (3, 7), (4, 5), 
    (4, 6), (4, 12), (5, 7), (6, 7), 
    (8, 9), (8, 10), (8, 12), (9, 11),
    (10, 11), (12, 13), (12, 14), (13, 15),
    (14, 15)
]

caras = [
    (0, 1, 3, 2), (4, 5, 7, 6), (8, 9, 11, 10),
    (12, 13, 15, 14), (0, 1, 5, 4), (2, 3, 7, 6),
    (8, 9, 13, 12), (10, 11, 15, 14)
]

fig = go.Figure()

for cara in caras:
    cara_coords = np.array([vertices_3d[i] for i in cara])
    fig.add_trace(go.Mesh3d(
        x=cara_coords[:, 0],
        y=cara_coords[:, 1],
        z=cara_coords[:, 2],
        color=np.random.choice(['lightblue', 'orange', 'green', 'pink', 'purple']),
        opacity=0.5,
        flatshading=True
    ))

for start, end in aristas:
    fig.add_trace(go.Scatter3d(
        x=[vertices_3d[start, 0], vertices_3d[end, 0]],
        y=[vertices_3d[start, 1], vertices_3d[end, 1]],
        z=[vertices_3d[start, 2], vertices_3d[end, 2]],
        mode='lines',
        line=dict(color='white', width=5),
    ))

fig.update_layout(
    title="Tesseract 4D",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z"
    ),
    showlegend=False,
    hovermode='closest',
    template='plotly_dark',
    dragmode="orbit",
    margin=dict(l=0, r=0, b=0, t=40)
)

fig.show()
