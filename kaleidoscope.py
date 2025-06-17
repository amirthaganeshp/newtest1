import math # New import

# Screen dimensions (now constants, not Pygame dependent for definition)
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100) # New color for the base shape

# Kaleidoscope settings
NUM_SEGMENTS = 6

def rotate_point(point_coords, center_coords, angle_rad):
    px, py = point_coords
    center_x, center_y = center_coords

    translated_x = px - center_x
    translated_y = py - center_y

    rotated_x = translated_x * math.cos(angle_rad) - translated_y * math.sin(angle_rad)
    rotated_y = translated_x * math.sin(angle_rad) + translated_y * math.cos(angle_rad)

    final_x = int(rotated_x + center_x)
    final_y = int(rotated_y + center_y)
    return (final_x, final_y)

# --- Main game loop ---
def main():
    import pygame # Moved import
    import sys # Moved import

    # Initialize Pygame & Screen inside main
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Interactive Kaleidoscope")

    running = True
    clicked_points = [] # New list to store points

    center_x = WIDTH // 2  # Define center_x
    center_y = HEIGHT // 2 # Define center_y

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            # New event: Mouse button down
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_points.append(event.pos)
                # print(f"Clicked points: {clicked_points}") # Optional: keep for debugging

        # Drawing
        SCREEN.fill(BLACK)

        # Optional: Draw the original shape being drawn by the user in a different color
        if len(clicked_points) > 1:
            pygame.draw.lines(SCREEN, GREY, False, clicked_points, 1)

        # Draw the kaleidoscope pattern (lines)
        if len(clicked_points) > 1:
            for j in range(len(clicked_points) - 1):
                p1_orig = clicked_points[j]
                p2_orig = clicked_points[j+1]

                for i in range(NUM_SEGMENTS):
                    angle_rad = i * (2 * math.pi / NUM_SEGMENTS)

                    final_p1 = rotate_point(p1_orig, (center_x, center_y), angle_rad)
                    final_p2 = rotate_point(p2_orig, (center_x, center_y), angle_rad)

                    pygame.draw.line(SCREEN, WHITE, final_p1, final_p2, 1)
        # If there's only one point, draw it (and its reflections) like before
        elif len(clicked_points) == 1:
            px, py = clicked_points[0]
            for i in range(NUM_SEGMENTS):
                angle_rad = i * (2 * math.pi / NUM_SEGMENTS)

                final_point = rotate_point((px, py), (center_x, center_y), angle_rad)
                pygame.draw.circle(SCREEN, WHITE, final_point, 3)


        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
