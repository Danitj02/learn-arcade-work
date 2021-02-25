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

arcade.finish_render()
arcade.run()