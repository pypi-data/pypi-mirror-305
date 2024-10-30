from yta_multimedia.video.generation.manim.constants import HALF_SCENE_HEIGHT, HALF_SCENE_WIDTH
from yta_multimedia.video.generation.manim.utils.dimensions import width_to_manim_width, height_to_manim_height
from yta_general_utils.programming.enum import YTAEnum as Enum
from yta_general_utils.random import randrangefloat
from random import random


class ManimScreenPosition(Enum):
    """
    Enum class that represents a position inside the screen
    scene. This can be used to position a video in one of
    these different regions.
    """
    TOP = 'top'
    BOTTOM = 'bottom'
    LEFT = 'left'
    RIGHT = 'right'
    # TODO: Add more positions

    def get_limits(self):
        """
        Return the left, right, top and bottom limits for this
        screen position. This edges represent the limits of the
        region in which the video should be placed to fit this
        screen position.

        We consider each screen region as a limited region of
        half of the scene width and height.

        Corner limits:
        [-7-1/9,  4, 0]   [0,  4, 0]   [7+1/9,  4, 0]
        [-7-1/9,  0, 0]   [0,  0, 0]   [7+1/9,  0, 0]
        [-7-1/9, -4, 0]   [0, -4, 0]   [7+1/9, -4, 0]
        """
        if self == ManimScreenPosition.TOP:
            return -HALF_SCENE_WIDTH / 2, HALF_SCENE_WIDTH / 2, HALF_SCENE_HEIGHT, 0
        elif self == ManimScreenPosition.BOTTOM:
            return -HALF_SCENE_WIDTH / 2, HALF_SCENE_WIDTH / 2, -HALF_SCENE_HEIGHT, 0
        elif self == ManimScreenPosition.LEFT:
            return -HALF_SCENE_WIDTH, 0, HALF_SCENE_HEIGHT / 2, -HALF_SCENE_HEIGHT / 2
        elif self == ManimScreenPosition.RIGHT:
            return 0, HALF_SCENE_WIDTH, HALF_SCENE_HEIGHT / 2, -HALF_SCENE_HEIGHT / 2
        # TODO: Add more limits according to the new positions
        
    def get_position(self, width: float, height: float):
        """
        Calculate the position in which the center of the element 
        with the provided 'width' and 'height' must be placed to
        obtain this position.

        The provided 'width' and 'height' must be in pixels.
        """
        # TODO: Check if the provided 'width' and 'height' are in
        # in pixels and valid or if not

        # TODO: By now I'm just using the limits as numeric limits
        # for random position that will be used as the center of the
        # video, but we will need to consider the video dimensions 
        # in a near future to actually position it well, because the
        # video can be out of the scene right now with this approach
        left, right, top, bottom = self.get_limits()

        x, y = randrangefloat(left, right, width_to_manim_width(1)), randrangefloat(top, bottom, height_to_manim_height(1))

        # If video is larger than HALF/2 it won't fit correctly.
        if width > HALF_SCENE_WIDTH or height > HALF_SCENE_HEIGHT:
            # TODO: Video is bigger than the region, we cannot make
            # it fit so... what can we do (?)
            return x, y

        if x - width / 2 < left:
            x += left - (x - width / 2)
        if x + width / 2 > right:
            x -= (x + width / 2) - right
        if y - height / 2 < bottom:
            y += bottom - (y - height / 2)
        if y + height / 2 > top:
            y -= (y + height / 2) - top

        return x, y
        

class ManimPosition:
    @staticmethod
    def min_and_max_x(width: float):
        """
        Calculates the minimum and maximum possible 'x' to make the 
        object with the provided 'width' fit the manim screen, that
        means to be inside of it and appear in the video.

        The provided 'width' must be a manim width, not a width in
        pixels.

        This method returns the 'min, max' pair of minimum and
        maximum possible x values.
        """
        return -HALF_SCENE_WIDTH + (width / 2), HALF_SCENE_WIDTH - (width / 2)
    
    @staticmethod
    def min_and_max_y(height: float):
        """
        Calculates the minimum and maximum possible 'y' to make the
        object with the provided 'height' fit the manim screen, that
        means to be inside of it and appear in the video.

        The provided 'height' must be a manim height, not a height
        in pixels.

        This method returns the 'min, max' pair of minimum and
        maximum possible y values.
        """
        return -HALF_SCENE_HEIGHT + (height / 2), HALF_SCENE_HEIGHT - (height / 2)

    @classmethod
    def random_position(width: float, height: float):
        """
        Calculate a random position inside the manim screen limits according
        to the provided 'width' and 'height' that must be 

        Provided 'width' and 'height' must be in manim width and height.

        Calculate a random position inside the manim screen limits according
        to the provided 'width' and 'height' that must be of the element to
        position.
        """
        x_min, x_max = ManimPosition.min_and_max_x(width)
        random_x = x_min + (random() * (x_max - x_min))

        y_min, y_max = ManimPosition.min_and_max_y(height)
        random_y = y_min + (random() * (y_max - y_min))
        
        # TODO: Maybe in this class is as easy as return just 'x, y'
        return random_x, random_y

# TODO: Remove this below when refactored and unneeded
def get_random_position(width: float, height: float):
    """
    Returns a random position inside the screen according to the provided element width and
    height to fit in. If you are trying to position a text inside screen limits, you must
    provide text width and height to let this method calculate that random position.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH + (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT + (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_upper_left_position(width: float, height: float):
    """
    Returns a random position in the upper left corner according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH + (width / 2)
    X_MAXIMUM = -(width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_upper_right_position(width: float, height: float):
    """
    Returns a random position in the upper right corner according to the 
    provided element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_upper_center_position(width: float, height: float):
    """
    Returns a random position in the upper center according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH / 2 + (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH / 2 - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_upper_position(width: float, height: float):
    """
    Returns a random position in the upper section according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH + (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_center_position(width: float, height: float):
    """
    Returns a random position in the center according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH / 2 + (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH / 2 - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT / 2 + (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT / 2 - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_center_left_position(width: float, height: float):
    """
    Returns a random position in the center left according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH + (width / 2)
    X_MAXIMUM = -(width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT / 2 + (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT / 2 - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_center_right_position(width: float, height: float):
    """
    Returns a random position in the center right according to the 
    provided element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT / 2 + (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT / 2 - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_lower_left_position(width: float, height: float):
    """
    Returns a random position in the lower left corner according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH + (width / 2)
    X_MAXIMUM = -(width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT + (height / 2)
    Y_MAXIMUM = -(height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_lower_right_position(width: float, height: float):
    """
    Returns a random position in the lower right corner according to the 
    provided element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT + (height / 2)
    Y_MAXIMUM = -(height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_lower_center_position(width: float, height: float):
    """
    Returns a random position in the lower center according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH / 2 + (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH / 2 - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT + (height / 2)
    Y_MAXIMUM = -(height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_lower_position(width: float, height: float):
    """
    Returns a random position in the upper section according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH + (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT + (height / 2)
    Y_MAXIMUM = -(height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

# Exact places
HEIGHT_DISTANCE_FROM_EDGES = height_to_manim_height(10)
WIDTH_DISTANCE_FROM_EDGES = width_to_manim_width(10)
def get_upper_left_position(width: float, height: float):
    """
    Returns the exact position of the upper left corner according to
    the provided element 'width' and 'height' to fit in and be placed
    just in the corner.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = -HALF_SCENE_WIDTH + WIDTH_DISTANCE_FROM_EDGES + (width / 2)
    Y = HALF_SCENE_HEIGHT - HEIGHT_DISTANCE_FROM_EDGES - (height / 2)

    return {
        'x': X,
        'y': Y
    }

def get_upper_right_position(width: float, height: float):
    """
    Returns the exact position of the upper right corner according to
    the provided element 'width' and 'height' to fit in and be placed
    just in the corner.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = HALF_SCENE_WIDTH - WIDTH_DISTANCE_FROM_EDGES - (width / 2)
    Y = HALF_SCENE_HEIGHT - HEIGHT_DISTANCE_FROM_EDGES - (height / 2)

    return {
        'x': X,
        'y': Y
    }

def get_upper_center_position(height: float):
    """
    Returns the exact position of the upper center position according 
    to the provided element 'width' and 'height' to fit in and be 
    placed just there.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = 0
    Y = HALF_SCENE_HEIGHT - HEIGHT_DISTANCE_FROM_EDGES - (height / 2)

    return {
        'x': X,
        'y': Y
    }

def get_left_position(width: float):
    """
    Returns the exact position of the left side according to
    the provided element 'width' and 'height' to fit in and be placed
    just in that place

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = -HALF_SCENE_WIDTH + WIDTH_DISTANCE_FROM_EDGES + (width / 2)
    Y = 0

    return {
        'x': X,
        'y': Y
    }

def get_center_position():
    """
    Returns the exact position of the center according to the 
    provided element 'width' and 'height' to fit in and be placed
    just in that place

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = 0
    Y = 0

    return {
        'x': X,
        'y': Y
    }

def get_right_position(width: float):
    """
    Returns the exact position of the right side according to
    the provided element 'width' and 'height' to fit in and be placed
    just in that place

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = HALF_SCENE_WIDTH - WIDTH_DISTANCE_FROM_EDGES - (width / 2)
    Y = 0

    return {
        'x': X,
        'y': Y
    }

def get_lower_left_position(width: float, height: float):
    """
    Returns the exact position of the lower left corner according to
    the provided element 'width' and 'height' to fit in and be placed
    just in the corner.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = -HALF_SCENE_WIDTH + WIDTH_DISTANCE_FROM_EDGES + (width / 2)
    Y = -HALF_SCENE_HEIGHT + HEIGHT_DISTANCE_FROM_EDGES + (height / 2)

    return {
        'x': X,
        'y': Y
    }

def get_lower_right_position(width: float, height: float):
    """
    Returns the exact position of the lower right corner according to
    the provided element 'width' and 'height' to fit in and be placed
    just in the corner.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = HALF_SCENE_WIDTH - WIDTH_DISTANCE_FROM_EDGES - (width / 2)
    Y = -HALF_SCENE_HEIGHT + HEIGHT_DISTANCE_FROM_EDGES + (height / 2)

    return {
        'x': X,
        'y': Y
    }

def get_lower_center_position(height: float):
    """
    Returns the exact position of the lower center position according 
    to the provided element 'width' and 'height' to fit in and be 
    placed just there.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = 0
    Y = -HALF_SCENE_HEIGHT + HEIGHT_DISTANCE_FROM_EDGES + (height / 2)

    return {
        'x': X,
        'y': Y
    }