"""
Functions related to keyence
"""

# Imports
# Standard Library Imports
from __future__ import annotations
import csv
import importlib.resources
import xml.etree.ElementTree as element_tree

# External Imports

# Local Imports

COLUMNS = ["B", "C", "D", "E", "F", "G"]
ROWS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

LAYOUT_DEFAULT = [letter for letter in COLUMNS for _ in range(10)]


LENS_TABLE = "keyence_BZX800_lenses.csv"
LENSES = {}

with importlib.resources.open_text(
    "pepitatools.data", "keyence_BZX800_lenses.csv"
) as f:
    # with open(data_file, encoding="utf8", newline="", mode="r") as f:
    reader = csv.reader(f, delimiter="\t")
    next(reader, None)  # Skip the header

    for name, working_distance, pixel_size, numerical_aperture in reader:
        LENSES[name] = {
            "Numerical Aperture": float(numerical_aperture),
            "Pixel Size": float(pixel_size),
            "Working Distance": float(working_distance),
        }


def extract_metadata(filename):
    with open(filename, "br") as f:
        file_content = f.read()
        start = file_content.find(b"<?xml")
        xml = str(file_content[start:], "utf-8")

    try:
        main = element_tree.fromstring(xml).find("SingleFileProperty")
    except element_tree.ParseError:
        print("No xml data found.")
        exit(1)

    metadata = {}

    metadata["Aperture"] = int(_getxml(main, "Shooting", "Parameter", "Aperture")) / 100
    metadata["Digital Zoom"] = int(_getxml(main, "Image", "DigitalZoom")) / 100
    metadata["Exposure"] = {}
    metadata["Exposure"]["Label"] = (
        _getxml(main, "Shooting", "Parameter", "ExposureTime", "Numerator")
        + "/"
        + _getxml(main, "Shooting", "Parameter", "ExposureTime", "Denominator")
        + "s"
    )
    metadata["Exposure"]["Value"] = int(
        _getxml(main, "Shooting", "Parameter", "ExposureTime", "Numerator")
    ) / int(_getxml(main, "Shooting", "Parameter", "ExposureTime", "Denominator"))
    metadata["Field of View"] = {}
    metadata["Field of View"]["X Start"] = int(
        _getxml(main, "Shooting", "StageLocationX")
    )
    metadata["Field of View"]["X End"] = int(
        _getxml(main, "Shooting", "StageLocationX")
    ) + int(_getxml(main, "Shooting", "XyStageRegion", "Width"))
    metadata["Field of View"]["Y Start"] = int(
        _getxml(main, "Shooting", "StageLocationY")
    )
    metadata["Field of View"]["Y End"] = int(
        _getxml(main, "Shooting", "StageLocationY")
    ) + int(_getxml(main, "Shooting", "XyStageRegion", "Height"))
    metadata["Field of View"]["Z"] = int(_getxml(main, "Shooting", "StageLocationZ"))
    metadata["Gain"] = {}
    metadata["Gain"]["Camera Gain"] = (
        int(_getxml(main, "Shooting", "Parameter", "CameraGain")) - 54
    )  # match readout in Keyence analysis software
    metadata["Gain"]["Camera Gain Unit"] = _getxml(
        main, "Shooting", "Parameter", "CameraGainUnit"
    )
    metadata["Gain"]["Camera Hardware Gain"] = int(
        _getxml(main, "Shooting", "Parameter", "CameraHardwareGain")
    )
    metadata["IsoSpeed"] = _getxml(main, "Shooting", "Parameter", "IsoSpeed")
    metadata["Lens"] = _getxml(main, "Lens", "LensName")
    metadata["Magnification"] = int(_getxml(main, "Lens", "Magnification")) / 100

    metadata["Numerical Aperture"] = LENSES[metadata["Lens"]]["Numerical Aperture"]
    metadata["Pixel Size"] = LENSES[metadata["Lens"]]["Pixel Size"]
    metadata["Working Distance"] = LENSES[metadata["Lens"]]["Working Distance"]

    return metadata


def well_to_xy(well):
    col = well[0]
    row = int(well[1:])

    return COLUMNS.index(col) * 10 + ROWS.index(row) + 1


def xy_to_well(xy_num):
    xy_num -= 1

    return COLUMNS[xy_num // 10] + str(ROWS[xy_num % 10])


def _getxml(element, *fields):
    for field in fields:
        element = element.find(field)

    return element.text
