# import arcade library
import arcade

# Set the window title and the dimensions
arcade.open_window(800, 600, 'Mountain landscape')

# Set the background color
arcade.set_background_color(arcade.color.HAN_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.BITTER_LIME)

# --- Draw the mountains ---

# Middle mountain
arcade.draw_triangle_filled(400, 500, 110, 100, 700, 110, arcade.color.CERULEAN_FROST)

# Snow of the middle mountain
arcade.draw_triangle_filled(400, 500, 380, 430, 420, 472, arcade.color.SNOW)
arcade.draw_triangle_filled(400, 500, 442, 445, 400, 460, arcade.color.SNOW)
arcade.draw_triangle_filled(400, 500, 370, 460, 380, 430, arcade.color.PLATINUM)

# Left mountain
arcade.draw_triangle_filled(200, 400, 80, 100, 590, 100, arcade.color.CAROLINA_BLUE)

# Snow of the left mountain
arcade.draw_triangle_filled(200, 400, 197, 340, 258, 355, arcade.color.SNOW)
arcade.draw_triangle_filled(197, 340, 258, 355, 230, 340, arcade.color.SNOW)
arcade.draw_triangle_filled(200, 400, 197, 340, 170, 324, arcade.color.PLATINUM)

# Right mountain
arcade.draw_triangle_filled(570, 350, 300, 90, 730, 90, arcade.color.LIGHT_STEEL_BLUE)

# Snow of the right mountain
arcade.draw_triangle_filled(570, 350, 555, 310, 588, 320, arcade.color.SNOW)
arcade.draw_triangle_filled(570, 350, 555, 320, 595, 310, arcade.color.SNOW)
arcade.draw_triangle_filled(570, 350, 535, 315, 555, 310, arcade.color.PLATINUM)

# --- Sky ---

# Moon
arcade.draw_circle_filled(710, 500, 40, arcade.color.BUBBLES)
arcade.draw_circle_filled(740, 500, 30, arcade.color.HAN_BLUE)

# Yellow Stars
arcade.draw_circle_filled(156, 398, 3, arcade.color.YELLOW)
arcade.draw_circle_filled(678, 423, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(35, 570, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(87, 470, 3, arcade.color.YELLOW)
arcade.draw_circle_filled(239, 512, 4, arcade.color.YELLOW)
arcade.draw_circle_filled(727, 398, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(49, 246, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(773, 217, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(546, 396, 3, arcade.color.YELLOW)
arcade.draw_circle_filled(452, 569, 2, arcade.color.YELLOW)

# --- Trees ---

# Left Tree
arcade.draw_rectangle_filled(67, 90, 8, 20, arcade.color.BROWN)
arcade.draw_triangle_filled(85, 95, 50, 95, 67, 120, arcade.color.CADMIUM_GREEN)
arcade.draw_triangle_filled(80, 110, 55, 110, 67, 140, arcade.color.CADMIUM_GREEN)

# Right Tree
arcade.draw_rectangle_filled(548, 80, 8, 20, arcade.color.BROWN)
arcade.draw_triangle_filled(560, 85, 536, 85, 548, 110, arcade.color.CADMIUM_GREEN)
arcade.draw_triangle_filled(555, 100, 541, 100, 548, 130, arcade.color.CADMIUM_GREEN)

# --- House ---

# Base
arcade.draw_rectangle_filled(700, 65, 35, 35, arcade.color.BONE)

# Door
arcade.draw_rectangle_filled(700, 55, 8, 15, arcade.color.BEAVER)

# Roof
arcade.draw_triangle_filled(675, 78, 725, 78, 700, 98, arcade.color.BRIGHT_MAROON)

# Left Window
arcade.draw_circle_filled(690, 70, 4, arcade.color.BLUEBERRY)

# Right Windor
arcade.draw_circle_filled(710, 70, 4, arcade.color.BLUEBERRY)

# Finish Drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()