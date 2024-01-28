import numpy as np
from scipy.stats import multivariate_normal
from scipy.integrate import dblquad

# Set up the dart board parameters
# Dartboard diameter in mm converted to radius in mm
dartboard_radius_mm = 343 / 2

# Define the different scoring areas parameters in mm
radius_circle1 = 33 / 2
radius_circle2 = 13 / 2
radius_circle3 = (80 + 80 + 33) / 2
radius_circle4 = (10 + 10 + 80 + 80 + 33) / 2
radius_circle5 = (55 + 55 + 10 + 10 + 80 + 80 + 33) / 2
radius_circle6 = (10 + 10 + 55 + 55 + 10 + 10 + 80 + 80 + 33) / 2

# Define the scores for different areas
score_double_bullseye = 50
score_single_bullseye = 25

# Define the areas of each scoring circle
area_circle1 = np.pi * radius_circle1**2
area_circle2 = np.pi * radius_circle2**2
area_circle3 = np.pi * radius_circle3**2
area_circle4 = np.pi * radius_circle4**2
area_circle5 = np.pi * radius_circle5**2
area_circle6 = np.pi * radius_circle6**2

# Function to determine the score based on the location
def calculate_score(x, y):
    distance_from_center = np.sqrt(x**2 + y**2)
    angle = np.degrees(np.arctan2(y, x)) % 360

    # Determine the multiplier based on the area
    if distance_from_center <= radius_circle2:
        a = 2
        return score_double_bullseye * a
    elif distance_from_center <= radius_circle1:
        a = 1
        return score_single_bullseye * a
    elif distance_from_center <= radius_circle3:
        a = 1
    elif distance_from_center <= radius_circle4:
        a = 3
    elif distance_from_center <= radius_circle5:
        a = 1  # Outer single area
    elif distance_from_center <= radius_circle6:
        a = 2  # Double area
    else:
        return 0  # Outside the dartboard

    # Determine score based on the angle
    if 9 < angle <= 27:
        return 20 * a
    elif 27 < angle <= 45:
        return 1 * a
    elif 45 < angle <= 63:
        return 18 * a
    elif 63 < angle <= 81:
        return 4 * a
    elif 81 < angle <= 99:
        return 13 * a
    elif 99 < angle <= 117:
        return 6 * a
    elif 117 < angle <= 135:
        return 10 * a
    elif 135 < angle <= 153:
        return 15 * a
    elif 153 < angle <= 171:
        return 2 * a
    elif 171 < angle <= 189:
        return 17 * a
    elif 189 < angle <= 207:
        return 3 * a
    elif 207 < angle <= 225:
        return 19 * a
    elif 225 < angle <= 243:
        return 7 * a
    elif 243 < angle <= 261:
        return 16 * a
    elif 261 < angle <= 279:
        return 8 * a
    elif 279 < angle <= 297:
        return 11 * a
    elif 297 < angle <= 315:
        return 14 * a
    elif 315 < angle <= 333:
        return 9 * a
    elif 333 < angle <= 351:
        return 12 * a
    elif 351 < angle <= 359.999999 or 0 <= angle <= 9:
        return 20 * a
    else:
        return 0

# Function to integrate over the dartboard area for a given 2D normal distribution
def integrate_over_dartboard(sigma_x, sigma_y, rho, mu_x, mu_y):
    # Define the PDF of the 2D normal distribution
    rv = multivariate_normal(mean=[mu_x, mu_y], cov=[[sigma_x**2, rho * sigma_x * sigma_y], [rho * sigma_x * sigma_y, sigma_y**2]])

    # Integration function over dartboard
    def integrand(x, y):
        return rv.pdf([x, y]) * calculate_score(x, y)

    # Integrate over the dartboard area
    result, _ = dblquad(integrand