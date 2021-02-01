"""compactness.py"""
import cv2
import numpy as np


class Compactness(object):
    """Processing image to calculate compactness and keep result of calculations"""

    def __init__(self, image_name):
        if image_name == '':
            self.p2a = 0
            self.iso_ration = 0
            self.min_circle_comp = 0
            self.equal_fields_comp = 0
            pass

        self.__process_image(image_name)

    def __process_image(self, image_name, complex=False, approx_contours=True):
        # Reading image
        img2 = cv2.imread(image_name, cv2.IMREAD_COLOR)

        # Reading same image in another variable and
        # converting to gray scale.
        img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)

        # Converting image to a binary image
        # (black and white only image).
        _, threshold = cv2.threshold(img, 110, 255,
                                     cv2.THRESH_BINARY)

        # Detecting shapes in image by selecting region
        # with same colors or intensity.
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)

        area = 0
        perimeter = 0
        min_enclosing_circle_area = 0
        # Searching through every region selected to
        # find the required polygon.
        for cnt in contours:
            if approx_contours:
                cnt = cv2.approxPolyDP(cnt, epsilon=1, closed=True)
            area = cv2.contourArea(cnt)
            if area > 0:
                perimeter = cv2.arcLength(cnt, closed=True)
                (_, _), min_enclosing_radius = cv2.minEnclosingCircle(cnt)
                min_enclosing_circle_area = np.pi * (min_enclosing_radius ** 2)
                print(f"AREA = {area}, PERIMETER = {perimeter}, CIRCLE_AREA = {min_enclosing_circle_area}")

                break

        self.p2a = CalculateCompactness.perimeter_to_area(perimeter=perimeter, area=area)
        self.iso_ration = CalculateCompactness.isoperimetric_ratio(perimeter=perimeter, area=area)
        self.min_circle_comp = CalculateCompactness.shape_to_min_circle_at_shape(shape_area=area,
                                                                                 minimal_circle_area=min_enclosing_circle_area)
        self.equal_fields_comp = CalculateCompactness.perimeter_circle_to_perimeter_shape_fields_equal(shape_area=area,
                                                                                         shape_perimeter=perimeter)


class CalculateCompactness(object):
    """
        Methods to calculate compactness from given parameters
        Based on paper https://www.researchgate.net/profile/Ernesto_Bribiesca/publication/228948093_State_of_the_art_of_compactness_and_circularity_measures/links/0deec5339984009465000000/State-of-the-art-of-compactness-and-circularity-measures.pdf
    """

    @staticmethod
    def perimeter_to_area(perimeter, area):
        return (perimeter ** 2) / area

    @staticmethod
    def isoperimetric_ratio(perimeter, area):
        return (4 * np.pi * area) / (perimeter ** 2)

    @staticmethod
    def shape_to_min_circle_at_shape(shape_area, minimal_circle_area):
        return shape_area / minimal_circle_area

    @staticmethod
    def perimeter_circle_to_perimeter_shape_fields_equal(shape_area, shape_perimeter):
        circle_r = np.sqrt(shape_area / np.pi)
        circle_perimeter = 2 * np.pi * circle_r
        return circle_perimeter / shape_perimeter
