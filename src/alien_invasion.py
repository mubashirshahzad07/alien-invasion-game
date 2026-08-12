import sys

import pygame

from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.game_running = False
        self.game_count = 0
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.play_button = Button(self, "Play")
        self.ship = Ship(self)
        self.score_board = ScoreBoard(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_aliens_fleet()

    def run_game(self):
        while True:
            self._check_events()

            if self.game_running:
                self.ship.update()
                self._update_aliens()
                self._update_bullets()

            self._update_screen()
            self.clock.tick(60)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_a:
            self._check_play_button()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        self.screen.fill(self.settings.screen_bg_color)

        for bullet in self.bullets:
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.score_board.display_scoreboard()

        if not self.game_running:
            if self.game_count == 1:
                self.play_button = Button(self, "Play Again")
            self.play_button.draw_button()

        pygame.display.flip()

    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _remove_bullets(self):
        """Removes the bullets that have traveled out of the screen."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_aliens_bullet_collision(self):
        alien_hit = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if alien_hit:
            for aliens in alien_hit.values():
                self.stats.score += self.settings.alien_points * len(aliens)

            self.score_board.render_score()
            self.score_board.update_highest_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_aliens_fleet()
            self.settings.increase_game_speed()
            self.stats.level += 1
            self.score_board.render_level()

    def _update_bullets(self):
        self.bullets.update()
        self._remove_bullets()
        self._check_aliens_bullet_collision()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_at_bottom()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.hit_edges():
                self._change_aliens_fleet_direction()
                break

    def _change_aliens_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_aliens_fleet(self):
        alien = Alien(self)

        alien_width = alien.rect.width
        alien_height = alien.rect.height

        current_x = alien_width
        current_y = alien_height + 50

        while current_y < (self.settings.screen_height - 3 * alien_height - 70):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x, y):
        new_alien = Alien(self)
        new_alien.x = x
        new_alien.rect.x = x
        new_alien.rect.y = y
        self.aliens.add(new_alien)

    def _check_aliens_at_bottom(self):
        for alien in self.aliens:
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _ship_hit(self):
        """Handles the Alien-Ship collision."""
        self.stats.ships_left -= 1
        self.score_board.render_ships()

        self._update_screen()
        sleep(1)

        if self.stats.ships_left <= 0:
            self.game_running = False
            pygame.mouse.set_visible(True)

        self.aliens.empty()
        self.bullets.empty()

        self._create_aliens_fleet()
        self.ship.center_ship()

    def _check_play_button(self, mouse_pos=None):
        if not mouse_pos:
            mouse_pos = self.play_button.rect.center

        play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if play_button_clicked and not self.game_running:
            self.game_running = True
            self.stats.reset_stats()
            self.score_board.render_score()
            self.score_board.render_level()
            self.score_board.render_ships()
            self.aliens.empty()
            self.bullets.empty()
            self.ship.center_ship()
            self.game_count += 1
            self.settings.reset_game_speeds()
            pygame.mouse.set_visible(False)


if __name__ == "__main__":
    alien_invasion_game = AlienInvasion()
    alien_invasion_game.run_game()
