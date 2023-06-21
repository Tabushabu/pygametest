# Kyler Farnsworth
# KFarnsworth1@csu.fullerton.edu
# @Tabushabu

"""Scene objects for making games with PyGame."""

import pygame
import rgbcolors


# If you're interested in using abstract base classes, feel free to rewrite
# these classes.
# For more information about Python Abstract Base classes, see
# https://docs.python.org/3.8/library/abc.html


class Scene:
    """Base class for making PyGame Scenes."""

    def __init__(self, screen, background_color, soundtrack=None):
        """Scene initializer"""
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(background_color)
        self._frame_rate = 60
        self._is_valid = True
        self._soundtrack = soundtrack
        self._render_updates = None

    def draw(self):
        """Draw the scene."""
        self._screen.blit(self._background, (0, 0))

    def process_event(self, event):
        """Process a game event by the scene."""
        # This should be commented out or removed since it generates a lot of noise.
        # print(str(event))
        if event.type == pygame.QUIT:
            print("Good Bye!")
            self._is_valid = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("Bye bye!")
            self._is_valid = False

    def is_valid(self):
        """Is the scene valid? A valid scene can be used to play a scene."""
        return self._is_valid

    def render_updates(self):
        """Render all sprite updates."""

    def update_scene(self):
        """Update the scene state."""

    def start_scene(self):
        """Start the scene."""
        if self._soundtrack:
            try:
                pygame.mixer.music.load(self._soundtrack)
                pygame.mixer.music.set_volume(0.2)
            except pygame.error as pygame_error:
                print("Cannot open the mixer?")
                raise SystemExit("broken!!") from pygame_error
            pygame.mixer.music.play(-1)

    def end_scene(self):
        """End the scene."""
        if self._soundtrack and pygame.mixer.music.get_busy():
            # Fade music out so there isn't an audible pop
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()

    def frame_rate(self):
        """Return the frame rate the scene desires."""
        return self._frame_rate


class PressAnyKeyToExitScene(Scene):
    """Empty scene where it will invalidate when a key is pressed."""

    def process_event(self, event):
        """Process game events."""
        # TODO: Have the super/parent class process the event first before
        super().process_event(event)
        # processing the event yourself.
        # TOOD: If the event type is a keydown event, set self._is_valid to False.
        if event.type == pygame.KEYDOWN:
            self._is_valid = False


class PolygonTitleScene(PressAnyKeyToExitScene):
    """Scene with a title string and a polygon."""

    def __init__(
        self,
        screen,
        title,
        title_color=rgbcolors.ghostwhite,
        title_size=72,
        background_color=rgbcolors.purple4,
        soundtrack=None,
    ):
        """Initialize the scene."""
        # TODO: Have the super/parent class initialized
        super().__init__(screen, background_color, soundtrack)
        pygame.font.init()

        # TODO: Ask pygame for the default font at title_size size. Use the font to render the string title and assign this to an instance variable named self._title in the color title_color.
        title_font = pygame.font.Font(None, title_size)
        self._title = title_font.render(str(title), True, title_color)
        
       # TODO: Ask pygame for the default font at 18 point size. Use the font to render the string 'Press any key.' in the color black. Assign the rendered text to an instance variable named self._press_any_key.
        press_any_key_font = pygame.font.Font(None, 18)
        self._press_any_key = press_any_key_font.render('Press any key.', True, rgbcolors.black)
 
    def draw(self):
        """Draw the scene."""
        # TODO: Have the super/parent class draw first before drawing yourself.
        super().draw()

        # TODO: Draw a 100 pixel by 100 pixel rectangle that has it's center located 100 pixels below the center of the window.
        rect = pygame.Rect(
            self._screen.get_width() // 2 - 50,
            self._screen.get_height() // 2 + 100,
            100,
            100,
        )
        pygame.draw.rect(self._screen, rgbcolors.dodgerblue1, rect)
        
        # TODO: Blit the title text to the center of the window.
        title_rect = self._title.get_rect(center=self._screen.get_rect().center)
        self._screen.blit(self._title, title_rect)

        # TODO: Blit the press any key message to the bottom of the window. The text should be centered horizontally and be 50 pixels above the bottom edge of the window.
        press_any_key_rect = self._press_any_key.get_rect(
            center=(self._screen.get_width() // 2, self._screen.get_height() - 50)
        )
        self._screen.blit(self._press_any_key, press_any_key_rect)

        