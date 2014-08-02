import pygame, math
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((700, 500))
numPoints = int(input("numPoints: "))
size = int(input("size: "))
pos = [None] * 2
pos[0] = int(input("xposition: "))
pos[1] = int(input("yposition: "))
width = int(input("width: "))
#numPoints = 5
#size = 100
#pos = [350, 250]
#width = 5

def drawStar(numPoints, size, pos, width):
    points = []
    for i in range(numPoints):
        points.append([None, None])
    totalDegrees = (numPoints - 2) * 180
    degreeIncrement = 360/numPoints
    currentDegree = 0
    #pygame.draw.circle(screen, WHITE, pos, 5)
    for point in points:
        point[0] = size * math.cos(math.radians(currentDegree)) + pos[0]
        point[1] = size * math.sin(math.radians(currentDegree)) + pos[1]
        currentDegree += degreeIncrement
        pygame.draw.circle(screen, WHITE, (int(point[0]), int(point[1])), 5)
    if numPoints % 2 == 0:
        print("even")
    if numPoints % 2 == 1:
        currentPoint = 0
        for point in points:
            nextPoint = (numPoints - 1)/2 + currentPoint
            if not nextPoint < numPoints:
                nextPoint -= numPoints
            currentPointValue = points[int(currentPoint)]
            nextPointValue = points[int(nextPoint)]
            pygame.draw.line(screen, WHITE, currentPointValue, nextPointValue, width)
            currentPoint = nextPoint

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(BLACK)
    drawStar(numPoints, size, pos, width)
    pygame.display.flip()
