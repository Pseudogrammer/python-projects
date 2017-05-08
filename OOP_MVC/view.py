import pygame

colors = {
    'black': (0, 0, 0), 'red': (255, 0, 0),
    'green': (0, 255, 0), 'blue': (0, 0, 255),
    'white': (255, 255, 255), "magenta": (255,0,255)
    }

class Point(object):
    x = -1
    y = -1
    color = None
    default_color = colors['black']

    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        self.color = colors.get(color, self.default_color)

    def draw(self, surface, origin, scale_x, scale_y):
        x=round(origin.x+self.x*scale_x)
        y=round(origin.y-self.y*scale_y)
        pygame.draw.circle(surface, self.color, (x, y), 5, 5)


class ScatterPlot(object):
    points = list()
    surface = None
    width, height = 0, 0
    origin = None
    bound_x, bound_y = None, None
    scale_x, scale_y = None, None
    font = None
    color = colors['black']
    bg_color = colors['white']

    def __init__(self, tuples, surface, font):
        self.surface = surface
        self.width, self.height = self.surface.get_width(), self.surface.get_height()
        self.font = font

        origin_y = int(float(self.height)*.9)
        origin_x = int(float(self.width)*.1)
        self.origin = Point(origin_x, origin_y)

        max_x, max_y = 0, 0
        for data in tuples:
            x, y, pcolor = int(data[0]), int(data[1]), data[2]
            point = Point(x, y, pcolor)

            self.points.append(point)

            if max_x is None or max_x < x:
                max_x = x
            if max_y is None or max_y < y:
                max_y = y

        self.bound_x = 5 * (max_x // 5 + 1)
        self.bound_y = 5 * (max_y // 5 + 1)

        self.scale_x = (self.width - 20 - self.origin.x)/(self.bound_x)
        self.scale_y = (self.origin.y - 20) / self.bound_y


    def draw_axes(self):
        origin_label = self.font.render(str(0), True, self.color)
        self.surface.blit(origin_label, (self.origin.x - 10 - origin_label.get_width(), self.origin.y + 10))

        pygame.draw.line(self.surface, self.color, (self.origin.x, self.origin.y), (self.width - 10, self.origin.y))

        for i in range(0, self.bound_x + 1, 5):
            x = self.origin.x + i * self.scale_x
            pygame.draw.line(self.surface, self.color, (x, self.origin.y - 5), (x, self.origin.y + 5))
            if i > 0:
                x_label = self.font.render(str(i), True, self.color)
                self.surface.blit(x_label, (x, self.origin.y + 10))

        pygame.draw.line(self.surface, self.color, (self.origin.x, self.origin.y), (self.origin.x, 10))
        for i in range(0, self.bound_y + 1, 5):
            y = self.origin.y - i * self.scale_y
            pygame.draw.line(self.surface, self.color, (self.origin.x-5, y), (self.origin.x+5, y))
            if i > 0:
                y_label = self.font.render(str(i), True, self.color)
                self.surface.blit(y_label, (self.origin.x-25, y))


    def draw(self):
        self.surface.fill(self.bg_color)
        self.draw_axes()

        for point in self.points:
            point.draw(self.surface, self.origin, self.scale_x, self.scale_y)



