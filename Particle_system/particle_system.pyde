import particle

def setup():
    global particles
    particles = []
    for i in range(10):
        particle_system = particle.Particle()
        particle_system.randomize()
        particles.append(particle_system)
    size(400, 400)

def draw():
    global particles
    background(0)
    for i in range(len(particles)):
        for j in range(1, len(particles)):
            line(particles[i].x_position, particles[i].y_position, particles[j].x_position, particles[j].y_position)
            stroke(225, 225, 225)
        particle_system = particles[i]
        particle_system.move()
        particle_system.draw_it()
