from sys import exit
import pygame as pg

from objects import Sphere, Checkerboard
from camera import Camera
from skybox import Skybox
from vector import Vector
from light import Light
from ray import Ray

pg.init()
pg.display.init()

screen_size     = Vector(1280, 720)
shadow_bias     = 0.0001
max_reflections = 3

display = pg.display.set_mode((screen_size.x, screen_size.y))
pg.display.set_caption("Python Raytracer")

camera = Camera(Vector(0, 0, 0), screen_size)
skybox = Skybox("skybox.png")

objects = [
    Sphere(Vector(0, 0, -10), 2, Vector(1, 0, 0)),
    Sphere(Vector(5, 0, -15), 2, Vector(0, 1, 0)),
    Sphere(Vector(-5, 0, -15), 2, Vector(0, 0, 1)),
    Checkerboard(2, Vector(0, 0, 0), Vector(1, 1, 1))
]

light = Light(Vector(-1, 1, -1), 1)

def trace_ray(ray: Ray) -> Vector:
    color = Vector(0, 0, 0)
    intersect, object = ray.cast(objects)
    normal = False
    if intersect:
        normal = object.get_normal(intersect)
        color  = object.get_color(intersect)
        light_ray = Ray(intersect + normal * shadow_bias, -light.direction.normalize())
        light_intersect, obstacle = light_ray.cast(objects)
        if light_intersect:
            color *= 0.1 / light.strength
        color *= normal.dot(-light.direction * light.strength)
    else:
        color = skybox.get_image_coords(ray.direction)
    return color, intersect, normal

for y in range(pg.display.get_window_size()[1]):
    for x in range(pg.display.get_window_size()[0]):
        ray = camera.get_direction(Vector(x, y))

        color, intersect, normal = trace_ray(ray)
        if intersect:
            reflection_ray = Ray(intersect, ray.direction.reflect(normal))
            reflection_color = Vector(0, 0, 0)
            reflection_times = 0
            for reflection in range(max_reflections):
                new_color, intersect, normal = trace_ray(reflection_ray)
                reflection_color += new_color
                reflection_times += 1
                if intersect:
                    reflection_ray = Ray(intersect, reflection_ray.direction.reflect(normal))
                else:
                    break
            color += reflection_color / reflection_times
        else:
            color = skybox.get_image_coords(ray.direction)

        display.set_at((x, y), color.to_rgb())

    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
