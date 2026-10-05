import pygame
from pathlib import Path
from .player import Player
from .obstacle import Obstacle

# Game Engine

WHITE = (255, 255, 255)
BROWN = (120, 80, 40)
DARK_GREEN = (30, 100, 30)


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ground_y = height - 40

        self.speed_increase_per_frame = 0.003
        self.max_speed = 12

        self.font = pygame.font.SysFont("Arial", 30)
        self.game_over_font = pygame.font.SysFont("Arial", 48)
        self.menu_font = pygame.font.SysFont("Arial", 28)

        self.exit_requested = False
        self.game_over = False

        # Audio is optional: if pygame's mixer or a sound file is unavailable,
        # the game continues to work without sound.
        self.jump_sound = None
        self.score_sound = None
        self.game_over_sound = None
        self._init_sounds()

        self._start_new_game(6, 70)

    def _init_sounds(self):
        try:
            if pygame.mixer.get_init() is None:
                pygame.mixer.init()

            sound_dir = Path(__file__).resolve().parent.parent / "sounds"

            self.jump_sound = pygame.mixer.Sound(
                str(sound_dir / "jump.wav")
            )
            self.score_sound = pygame.mixer.Sound(
                str(sound_dir / "score.wav")
            )
            self.game_over_sound = pygame.mixer.Sound(
                str(sound_dir / "game_over.wav")
            )

        except (pygame.error, OSError):
            self.jump_sound = None
            self.score_sound = None
            self.game_over_sound = None

    def _start_new_game(self, starting_speed, spawn_interval):
        """Reset all state needed for a fresh run."""
        self.player = Player(80, self.ground_y)
        self.speed = starting_speed
        self.spawn_interval = spawn_interval
        self._spawn_timer = 0
        self.obstacles = []
        self.distance = 0
        self.score = 0
        self.game_over = False

    def _select_difficulty(self, difficulty):
        """Start a fresh game using the selected difficulty settings."""
        difficulty_settings = {
            "easy": (5, 80),
            "medium": (6, 70),
            "hard": (8, 55),
        }

        starting_speed, spawn_interval = difficulty_settings[difficulty]
        self._start_new_game(starting_speed, spawn_interval)

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if self.game_over:
            if event.key == pygame.K_1:
                self._select_difficulty("easy")

            elif event.key == pygame.K_2:
                self._select_difficulty("medium")

            elif event.key == pygame.K_3:
                self._select_difficulty("hard")

            elif event.key in (pygame.K_4, pygame.K_e, pygame.K_ESCAPE):
                self.exit_requested = True

            return

        if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
            if self.player.on_ground:
                self.player.jump()

                if self.jump_sound is not None:
                    self.jump_sound.play()

    def should_exit(self):
        return self.exit_requested

    def handle_input(self):
        # Reserved for continuously-held-key input; this runner only
        # needs an edge-triggered jump, handled in handle_event.
        pass

    def update(self):
        if self.game_over:
            return

        # Task 1: capped speed ramp.
        self.speed = min(
            self.speed + self.speed_increase_per_frame,
            self.max_speed
        )

        self.player.update()

        self._spawn_timer += 1

        if self._spawn_timer >= self.spawn_interval:
            self._spawn_timer = 0
            self.obstacles.append(
                Obstacle(self.width, self.ground_y, self.speed)
            )

        # Task 1: swept collision detection.
        # Check the obstacle's entire movement path for this frame,
        # rather than only its final position.
        player_rect = self.player.rect()

        for obstacle in self.obstacles:
            previous_x = obstacle.x

            obstacle.move()
            obstacle.speed = self.speed

            left = min(previous_x, obstacle.x)
            right = max(
                previous_x + obstacle.width,
                obstacle.x + obstacle.width
            )

            swept_rect = pygame.Rect(
                left,
                obstacle.y,
                right - left,
                obstacle.height
            )

            if swept_rect.colliderect(player_rect):
                self.game_over = True

                # Task 4: play Game Over sound once when collision
                # transitions the game into the Game Over state.
                if self.game_over_sound is not None:
                    self.game_over_sound.play()

                return

        # Score obstacles that successfully pass the player.
        for obstacle in self.obstacles:
            if (
                not obstacle.scored
                and obstacle.x + obstacle.width < self.player.x
            ):
                obstacle.scored = True
                self.score += 1

                # Task 4: play score sound once per scored obstacle.
                if self.score_sound is not None:
                    self.score_sound.play()

        self.obstacles = [
            obstacle for obstacle in self.obstacles
            if not obstacle.off_screen()
        ]

        self.distance += self.speed

    def render(self, screen):
        pygame.draw.line(
            screen,
            BROWN,
            (0, self.ground_y),
            (self.width, self.ground_y),
            4
        )

        pygame.draw.rect(
            screen,
            WHITE,
            self.player.rect()
        )

        for obstacle in self.obstacles:
            pygame.draw.rect(
                screen,
                DARK_GREEN,
                obstacle.rect()
            )

        score_text = self.font.render(
            f"Score: {self.score}",
            True,
            (0, 0, 0)
        )

        screen.blit(score_text, (10, 10))

        if self.game_over:
            overlay = pygame.Surface(
                (self.width, self.height),
                pygame.SRCALPHA
            )
            overlay.fill((0, 0, 0, 140))
            screen.blit(overlay, (0, 0))

            game_over_text = self.game_over_font.render(
                "GAME OVER",
                True,
                WHITE
            )

            final_score_text = self.font.render(
                f"Final Score: {self.score}",
                True,
                WHITE
            )

            menu_title = self.menu_font.render(
                "Choose a difficulty",
                True,
                WHITE
            )

            easy_text = self.menu_font.render(
                "1 - Easy",
                True,
                WHITE
            )

            medium_text = self.menu_font.render(
                "2 - Medium",
                True,
                WHITE
            )

            hard_text = self.menu_font.render(
                "3 - Hard",
                True,
                WHITE
            )

            exit_text = self.menu_font.render(
                "4 - Exit",
                True,
                WHITE
            )

            screen.blit(
                game_over_text,
                game_over_text.get_rect(
                    center=(self.width // 2, 80)
                )
            )

            screen.blit(
                final_score_text,
                final_score_text.get_rect(
                    center=(self.width // 2, 135)
                )
            )

            screen.blit(
                menu_title,
                menu_title.get_rect(
                    center=(self.width // 2, 190)
                )
            )

            screen.blit(
                easy_text,
                easy_text.get_rect(
                    center=(self.width // 2, 230)
                )
            )

            screen.blit(
                medium_text,
                medium_text.get_rect(
                    center=(self.width // 2, 265)
                )
            )

            screen.blit(
                hard_text,
                hard_text.get_rect(
                    center=(self.width // 2, 300)
                )
            )

            screen.blit(
                exit_text,
                exit_text.get_rect(
                    center=(self.width // 2, 335)
                )
            )