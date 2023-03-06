import pygame
from Models.ibutton import IButton

from Views.iview import IView
from Windows.main_window import MainWindow
from Factories.button_factory import ButtonFactory


class GameFinishView(IView):

    def __init__(self, pyg: pygame) -> None:
        self.pyg = pyg

        self.continue_button: IButton = ButtonFactory \
            .create_button(self.__get_continue_button_pos(),
                           "Continue",
                           MainWindow.SURFACE)
            
    def draw(self) -> None:
        self.__draw_buttons()
        
        self.pyg.display.update()        

    def __get_continue_button_pos(self):
        return (MainWindow.WIDTH / 2,
                MainWindow.HEIGHT / 2)
        
    def __draw_buttons(self):
        self.continue_button.draw()
        
    # def __draw_winner_text(self, winner_text: str) -> None:
    #     draw_text = self.font.render(winner_text, 1, Colors.WHITE)
    #     MainWindow.SURFACE.blit(draw_text,
    #                             (MainWindow.WIDTH/2 - draw_text.get_width() / 2,
    #                              MainWindow.HEIGHT/2 - draw_text.get_height() / 2)
    #                             )
    #     self.pyg.display.update()
