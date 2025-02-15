import numpy as np
import random 

def CreateCircle(center, radius, colour, points = 10, offset = 0, semi = False):
    vertices = [center[0], center[1], center[2], colour[0], colour[1], colour[2]]
    indices = []

    if semi == True:
        for i in range(points+1):
            vertices += [
                center[0] + radius * np.cos(float(i * np.pi)/points),
                center[1] + radius * np.sin(float(i * np.pi)/points),
                center[2],
                colour[0],
                colour[1],
                colour[2],
                ]
            
            ind1 = i+1
            ind2 = i+2 if i != points else 1
            indices += [0 + offset, ind1 + offset, ind2 + offset]
    else:
        for i in range(points):
            vertices += [
                center[0] + radius * np.cos(float(i * 2* np.pi)/points),
                center[1] + radius * np.sin(float(i * 2* np.pi)/points),
                center[2],
                colour[0],
                colour[1],
                colour[2],
                ]
            
            ind1 = i+1
            ind2 = i+2 if i != points-1 else 1
            indices += [0 + offset, ind1 + offset, ind2 + offset]

    return (vertices, indices)    

def CreatePlayer():

    vertices, indices = CreateCircle([0.0, 0.0, 0.0001], 1.0, [220/255, 183/255, 139/255], 50, 0)

    eye_verts1, eye_inds1 = CreateCircle([0.4, -0.5, 0.05], 0.3, [1,1,1], 20, len(vertices)/6)
    vertices += eye_verts1
    indices += eye_inds1

    eye_verts2, eye_inds2 = CreateCircle([-0.4, -0.5, 0.05], 0.3, [1,1,1], 20, len(vertices)/6)
    vertices += eye_verts2
    indices += eye_inds2

    eye_verts3, eye_inds3 = CreateCircle([-0.4, -0.5, 0.10], 0.12, [0,0,0], 10, len(vertices)/6)
    vertices += eye_verts3
    indices += eye_inds3

    eye_verts4, eye_inds4 = CreateCircle([0.4, -0.5, 0.10], 0.12, [0,0,0], 10, len(vertices)/6)
    vertices += eye_verts4
    indices += eye_inds4

    eye_verts5, eye_inds5 = CreateCircle([0.0, 0.0, 0.2], 1.0, [1,0,0], 25, len(vertices)/6, True)
    vertices += eye_verts5
    indices += eye_inds5

    eye_verts6, eye_inds6 = CreateCircle([0.0, 0.95, 0.3], 0.3, [0.9,0.9,0.9], 20, len(vertices)/6)
    vertices += eye_verts6
    indices += eye_inds6

    return vertices, indices

def CreateMenuBackground():
    brown = [0.545, 0.271, 0.075]
    green = [0.133, 0.545, 0.133]
    blue = [0.529, 0.808, 0.922]
    lightblue = [0.878, 1.000, 1.000]
    red = [0.863, 0.078, 0.235]
    gray = [0.412, 0.412, 0.412]

    vertices = [
        -500, 350, -0.9, blue[0], blue[1], blue[2],
        -500, -200, -0.9, blue[0], blue[1], blue[2],
        500, 350, -0.9, blue[0], blue[1], blue[2],
        500, -200, -0.9, blue[0], blue[1], blue[2],

        -500, -200, -0.9, green[0], green[1], green[2],
        -500, -225, -0.9, green[0], green[1], green[2],
        500, -200, -0.9, green[0], green[1], green[2],
        500, -225, -0.9, green[0], green[1], green[2],

        -500, -225, -0.9, brown[0], brown[1], brown[2],
        -500, -350, -0.9, brown[0], brown[1], brown[2],
        500, -225, -0.9, brown[0], brown[1], brown[2],
        500, -350, -0.9, brown[0], brown[1], brown[2],

        -300, -100, -0.85, red[0], red[1], red[2],
        -300, -150, -0.85, red[0], red[1], red[2],
        -250, -125, -0.85, red[0], red[1], red[2],

        -305, -100, -0.89, gray[0], gray[1], gray[2],
        -300, -100, -0.89, gray[0], gray[1], gray[2],
        -305, -200, -0.89, gray[0], gray[1], gray[2],
        -300, -200, -0.89, gray[0], gray[1], gray[2],
    ]

    indices = [
        0,1,2, 1,3,2,
        4,6,5, 5,6,7,
        8,9,10, 9,10,11,
        12,13,14,
        15,16,17, 16,17,18,
    ]

    return vertices, indices

def CreateDefeatScreen():
    red = [0.545, 0.000, 0.000]
    black = [0, 0, 0]

    vertices = [
        -480, 0, -0.9, red[0], red[1], red[2],
        480, 0, -0.9, red[0], red[1], red[2],

        0, 50, -0.9, black[0], black[1], black[2],
        0, -50, -0.9, black[0], black[1], black[2],
    ]

    indices = [
        0,1,2,
        0,1,3,
    ]
    return vertices, indices

def CreateCloud():
    col = [0.878, 1.000, 1.000]
    vertices, indices = CreateCircle([0,1,0], 2, col, 20, 0)
    v, i = CreateCircle([0, -2, 0], 2, col, 20, int(len(vertices)/6))
    vertices += v
    indices += i

    v, i = CreateCircle([-3, 0, 0], 2, col, 20, int(len(vertices)/6))
    vertices += v
    indices += i

    v, i = CreateCircle([3, 0, 0], 2, col, 20, int(len(vertices)/6))
    vertices += v
    indices += i

    v, i = CreateCircle([2, -2, 0], 2, col, 20, int(len(vertices)/6))
    vertices += v
    indices += i

    return vertices, indices

def CreateForest():
    brown = [0.545, 0.271, 0.075]
    green_light = [0.180, 0.545, 0.341]
    green_dark = [0.000, 0.392, 0.000]
    blue = [0.000, 0.392, 0.000]

    vertices = [
        -500, 350, -0.9, blue[0], blue[1], blue[2],
        -500, 50, -0.9, blue[0], blue[1], blue[2],
        500, 350, -0.9, blue[0], blue[1], blue[2],
        500, 50, -0.9, blue[0], blue[1], blue[2],
        
        # Ground (Grass)
        -500, 50, -0.9, green_light[0], green_light[1], green_light[2],
        -500, -100, -0.9, green_light[0], green_light[1], green_light[2],
        500, 50, -0.9, green_light[0], green_light[1], green_light[2],
        500, -100, -0.9, green_light[0], green_light[1], green_light[2],
        
        # Barren land patches
        -200, -100, -0.9, brown[0], brown[1], brown[2],
        -200, -150, -0.9, brown[0], brown[1], brown[2],
        200, -100, -0.9, brown[0], brown[1], brown[2],
        200, -150, -0.9, brown[0], brown[1], brown[2],
        
        # Dense Forest Section
        -500, -100, -0.9, green_dark[0], green_dark[1], green_dark[2],
        -500, -350, -0.9, green_dark[0], green_dark[1], green_dark[2],
        500, -100, -0.9, green_dark[0], green_dark[1], green_dark[2],
        500, -350, -0.9, green_dark[0], green_dark[1], green_dark[2],
    ]

    indices = [
        0,1,2, 1,3,2,  # Sky
        4,6,5, 5,6,7,  # Grass
        8,9,10, 9,10,11,  # Barren Land
        12,13,14, 13,14,15  # Dense Forest
    ]
    return vertices, indices

def CreateRiver():
    blue = [0.529, 0.808, 0.922]
    green = [0.133, 0.545, 0.133]

    vertices = [
        -500, 350, -0.9, green[0], green[1], green[2],
        -400, 350, -0.9, green[0], green[1], green[2],
        -500, -350, -0.9, green[0], green[1], green[2],
        -400, -350, -0.9, green[0], green[1], green[2],

        500, 350, -0.9, green[0], green[1], green[2],
        400, 350, -0.9, green[0], green[1], green[2],
        500, -350, -0.9, green[0], green[1], green[2],
        400, -350, -0.9, green[0], green[1], green[2],

        -400, 350, -0.9, blue[0], blue[1], blue[2],
        400, 350, -0.9, blue[0], blue[1], blue[2],
        -400, -350, -0.9, blue[0], blue[1], blue[2],
        400, -350, -0.9, blue[0], blue[1], blue[2],

    ]

    indices = [
        0,1,2, 1,2,3,
        4,5,6, 5,6,7,
        8,9,10, 9,10,11,
    ]
    return vertices, indices

def CreateSpace():
    mid_blue = [0.0286, 0.0669, 0.22]

    vertices = [
        -500, 350, -0.9, mid_blue[0], mid_blue[1], mid_blue[2],
        500, 350, -0.9, mid_blue[0], mid_blue[1], mid_blue[2],
        -500, -350, -0.9, mid_blue[0], mid_blue[1], mid_blue[2],
        500, -350, -0.9, mid_blue[0], mid_blue[1], mid_blue[2],
    ]

    indices = [
        0,1,2, 1,2,3,
    ]
    return vertices, indices

def CreateTree():
    ForestGreen = [0.3478,0.94,0.1504]
    Green = [0.2259,0.65,0.0845]
    Brown = [0.35,0.1927,0.0455]

    vertices, indices = CreateCircle([0, 0, 0.9], 0.3, ForestGreen, 20, 0)

    v, i = CreateCircle([0.3, -0.4, 1], 0.3, Green, 20, int(len(vertices)/6))
    vertices += v
    indices += i

    v, i = CreateCircle([-0.3, -0.4, 1], 0.3, Green, 20, int(len(vertices)/6))
    vertices += v
    indices += i

    v, i = CreateCircle([0,-0.3 ,0.8], 0.1, Brown, 10, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-0.4 ,0.8], 0.1, Brown, 10, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-0.5 ,0.8], 0.1, Brown, 10, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-0.6 ,0.8], 0.1, Brown, 10, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-0.7 ,0.8], 0.1, Brown, 10, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-0.8 ,0.8], 0.1, Brown, 2, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-0.9 ,0.8], 0.1, Brown, 2, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-1 ,0.8], 0.1, Brown, 2, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-1.1 ,0.8], 0.1, Brown, 2, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-1.2 ,0.8], 0.1, Brown, 2, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-1.3 ,0.8], 0.1, Brown, 2, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-1.4 ,0.8], 0.1, Brown, 2, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-1.5 ,0.8], 0.1, Brown, 2, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-1.6 ,0.8], 0.1, Brown, 2, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-1.7 ,0.8], 0.1, Brown, 2, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-1.8 ,0.8], 0.1, Brown, 2, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-1.9 ,0.8], 0.1, Brown, 2, int(len(vertices)/6))
    vertices += v
    indices += i
    v, i = CreateCircle([0,-2.2 ,0.8], 0.1, Brown, 2, int(len(vertices)/6))
    vertices += v
    indices += i
    return vertices, indices

def CreateCoin():
    gold = [1.000, 0.843, 0.000]
    orange = [1.000, 0.647, 0.000]

    vertices, indices = CreateCircle([0.0, 0.0, -0.89], 0.5, gold, 50, 0)
    v, i = CreateCircle([0.0, 0.0, -0.8], 0.3, orange, 50, int(len(vertices)/6))
    vertices += v
    indices += i

    return vertices, indices

def CreatePlanet1():
    pink = [1.000, 0.000, 1.000]
    purple = [0.580, 0.000, 0.827]

    vertices, indices = CreateCircle([0, 0, 0.9], 3, pink, 100, 0)

    num_craters = 8  # Number of craters

    for _ in range(num_craters):
        radius = random.uniform(0.1, 0.8)  # Random size for craters
        x_offset = random.uniform(-2.2, 2.2)  # Random X offset to simulate surface position
        y_offset = random.uniform(-2.2, 2.2)  # Random Y offset

        v, i = CreateCircle([x_offset, y_offset, 1], radius, purple, 30, int(len(vertices)/6))
        vertices += v
        indices += i

    return vertices, indices

def CreatePlanet2():
    maroon = [0.502, 0.000, 0.000]
    orange = [1.000, 0.549, 0.000]

    vertices, indices = CreateCircle([0, 0, 0.8], 2, maroon, 100, 0)

    num_craters = 8  # Number of craters

    for _ in range(num_craters):
        radius = random.uniform(0.01, 0.5)  # Random size for craters
        x_offset = random.uniform(-1.2, 1.2)  # Random X offset to simulate surface position
        y_offset = random.uniform(-1.2, 1.2)  # Random Y offset

        v, i = CreateCircle([x_offset, y_offset, 0.9], radius, orange, 30, int(len(vertices)/6))
        vertices += v
        indices += i

    return vertices, indices

def CreatePlanet3():
    blue = [0.282, 0.820, 0.800]
    green = [0.196, 0.804, 0.196]

    vertices, indices = CreateCircle([0, 0, 0.8], 5, blue, 100, 0)

    num_craters = 12  # Number of craters

    for _ in range(num_craters):
        radius = random.uniform(0.1, 1)  # Random size for craters
        x_offset = random.uniform(-3.8, 3.8)  # Random X offset to simulate surface position
        y_offset = random.uniform(-3.8, 3.8)  # Random Y offset

        v, i = CreateCircle([x_offset, y_offset, 0.9], radius, green, 30, int(len(vertices)/6))
        vertices += v
        indices += i

    return vertices, indices

def CreateLog():
    brown = [0.28, 0.042, 0.0975]

    vertices, indices = CreateCircle([0,0,-0.9],1.2, brown, 20, 0)
    return vertices, indices

def random_position():
    return np.array([np.random.uniform(-400, 400), np.random.uniform(-300, 300), 0], dtype = np.float32)

############################################################

playerVerts, playerInds = CreatePlayer()
playerProps = {
    'vertices' : np.array(playerVerts, dtype = np.float32),
    
    'indices' : np.array(playerInds, dtype = np.uint32),
    
    'position' : np.array([-480, 0, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([30, 30, 1], dtype = np.float32),

    'sens' : 150,

    'velocity' : np.array([0, 0, 0], dtype = np.float32)
}

planetVerts, planetInds = CreatePlanet1()
planet1Props = {
    'vertices' : np.array(planetVerts, dtype = np.float32),
    
    'indices' : np.array(planetInds, dtype = np.uint32),

    'radius' : 120,

    'initial_position': np.array([-100, -250, 0], dtype = np.float32),
    
    'position' : np.array([-100, -250, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([30, 30, 1], dtype = np.float32),

    'sens' : 125,

    'velocity' : np.array([0, 0.1, 0], dtype = np.float32)
}

planetVerts, planetInds = CreatePlanet2()
planet2Props = {
    'vertices' : np.array(planetVerts, dtype = np.float32),
    
    'indices' : np.array(planetInds, dtype = np.uint32),

    'radius' : 99.9999,

    'initial_position': np.array([-380, 250, 0], dtype = np.float32),
    
    'position' : np.array([-380, 250, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([30, 30, 1], dtype = np.float32),

    'sens' : 125,

    'velocity' : np.array([0, -0.5, 0], dtype = np.float32)
}

planetVerts, planetInds = CreatePlanet3()
planet3Props = {
    'vertices' : np.array(planetVerts, dtype = np.float32),

    'indices' : np.array(planetInds, dtype = np.uint32),

    'radius' : 175,

    'initial_position': np.array([300, 0, 0], dtype = np.float32),
    
    'position' : np.array([300, 0, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([30, 30, 1], dtype = np.float32),

    'sens' : 125,

    'velocity' : np.array([0, -0.1, 0], dtype = np.float32)
}

treeVerts, treeInds = CreateTree()
treeProps = {
    'vertices' : np.array(treeVerts, dtype = np.float32),
    
    'indices' : np.array(treeInds, dtype = np.uint32),

    'position' : random_position(),

    'rotation_z' : 0.0,

    'scale' : np.array([30, 30, 1], dtype = np.float32),

    'sens' : 125,

    'velocity' : np.array([0, 0, 0], dtype = np.float32)
}

coinVerts, coinInds = CreateCoin()
coinProps = {
    'vertices' : np.array(coinVerts, dtype = np.float32),
    
    'indices' : np.array(coinInds, dtype = np.uint32),

    'position' : random_position(),

    'rotation_z' : 0.0,

    'scale' : np.array([30, 30, 1], dtype = np.float32),

    'sens' : 125,

    'velocity' : np.array([0, 0, 0], dtype = np.float32)
}

cloudVerts, cloudInds = CreateCloud()
cloud1Props = {
    'vertices' : np.array(cloudVerts, dtype = np.float32),
    
    'indices' : np.array(cloudInds, dtype = np.uint32),

    'position' : np.array([-300, 230, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([30, 30, 1], dtype = np.float32),

    'sens' : 125,

    'velocity' : np.array([0, 0, 0], dtype = np.float32)
}

cloudVerts, cloudInds = CreateCloud()
cloud2Props = {
    'vertices' : np.array(cloudVerts, dtype = np.float32),
    
    'indices' : np.array(cloudInds, dtype = np.uint32),

    'position' : np.array([400, 250, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([30, 30, 1], dtype = np.float32),

    'sens' : 125,

    'velocity' : np.array([0, 0, 0], dtype = np.float32)
}

logVerts, logInds = CreateLog()
logProps = {
    'vertices' : np.array(logVerts, dtype = np.float32),
    
    'indices' : np.array(logInds, dtype = np.uint32),

    'position' : np.array([0,0,-0.95], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([30, 30, 1], dtype = np.float32),

    'sens' : 125,

    'velocity' : np.array([0, 1, 0], dtype = np.float32)
}


backgroundVerts, backgroundInds = CreateMenuBackground()
menuProps = {
    'vertices' : np.array(backgroundVerts, dtype = np.float32),
    
    'indices' : np.array(backgroundInds, dtype = np.uint32),

    'position' : np.array([0, 0, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([1, 1, 1], dtype = np.float32),

    'boundary' : [500.0, -500.0, 500.0, 500.0],

    'river_banks': [-400.0, 400.0]
}

backgroundVerts, backgroundInds = CreateDefeatScreen()
defeatProps = {
    'vertices' : np.array(backgroundVerts, dtype = np.float32),
    
    'indices' : np.array(backgroundInds, dtype = np.uint32),

    'position' : np.array([0, 0, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([1, 1, 1], dtype = np.float32),

    'boundary' : [500.0, -500.0, 500.0, 500.0],

    'river_banks': [-400.0, 400.0]
}


backgroundVerts, backgroundInds = CreateForest()
forestProps = {
    'vertices' : np.array(backgroundVerts, dtype = np.float32),
    
    'indices' : np.array(backgroundInds, dtype = np.uint32),

    'position' : np.array([0, 0, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([1, 1, 1], dtype = np.float32),

    'boundary' : [500.0, -500.0, 500.0, 500.0],

    'river_banks': [-400.0, 400.0]
}

backgroundVerts, backgroundInds = CreateRiver()
riverProps = {
    'vertices' : np.array(backgroundVerts, dtype = np.float32),
    
    'indices' : np.array(backgroundInds, dtype = np.uint32),

    'position' : np.array([0, 0, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([1, 1, 1], dtype = np.float32),

    'boundary' : [500.0, -500.0, 500.0, 500.0],

    'river_banks': [-400.0, 400.0]
}

backgroundVerts, backgroundInds = CreateSpace()
spaceProps = {
    'vertices' : np.array(backgroundVerts, dtype = np.float32),
    
    'indices' : np.array(backgroundInds, dtype = np.uint32),

    'position' : np.array([0, 0, 0], dtype = np.float32),

    'rotation_z' : 0.0,

    'scale' : np.array([1, 1, 1], dtype = np.float32),

    'boundary' : [500.0, -500.0, 500.0, 500.0],

    'river_banks': [-400.0, 400.0]
}