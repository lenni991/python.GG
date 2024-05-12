import moderngl
import numpy as np
from PIL import Image
from pyrr import Matrix44

ctx = moderngl.create_standalone_context()

prog = ctx.program(
    vertex_shader="""
    #version 330
    uniform mat4 model;
    in vec2 in_vert;
    in vec3 in_color;
    out vec3 color;
    void main() {
        gl_Position = model * vec4(in_vert, 0.0, 1.0);
        color = in_color;
    }
    """,
    fragment_shader="""
    #version 330
    in vec3 color;
    out vec4 fragColor;
    void main() {
        fragColor = vec4(color, 1.0);
    }
    """,
)

buffer = ctx.buffer(np.array([
    #  x,    y,   r,   g,   b
    -0.9, -0.9, 1.0, 0.0, 0.0,  # v1 red
     0.9, -0.9, 0.0, 1.0, 0.0,  # v2 green
     0.0,  0.9, 0.0, 0.0, 1.0,  # v3 blue
], dtype='f4').tobytes())

vao = ctx.simple_vertex_array(prog, buffer, 'in_vert', 'in_color')

fbo = ctx.framebuffer(color_attachments=[ctx.texture((512, 512), 4)])

fbo.use()

# Clear the framebuffer
ctx.clear()

# Rotate the triangle
angle = np.radians(30)
model = Matrix44.from_eulers((0, 0, angle), dtype='f4')
prog['model'].write(model)

# Draw the triangle
vao.render(moderngl.TRIANGLES)

# Read pixels back & saving
pixels = fbo.read(components=3)
image = Image.frombytes('RGB', fbo.size, pixels)
image = image.transpose(Image.FLIP_TOP_BOTTOM)
image.save('output.png')
