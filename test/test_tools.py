import tempfile
from pathlib import Path

import numpy as np
import pytest

import colorio


def test_flat_gamut():
    colorio.show_flat_gamut()


def test_xy_gamut_mesh():
    # points, cells =
    colorio.xy_gamut_mesh(0.05)
    # import meshio
    # meshio.write_points_cells("test.vtu", points, {"triangle": cells})


@pytest.mark.parametrize(
    "cs,lightness",
    [
        [colorio.cs.XYY(1), 0.4],
        [colorio.cs.CIELAB(), 50],
        [colorio.cs.CAM16UCS(0.69, 20, 4.074), 50],
    ],
)
def test_visible_slice(cs, lightness):
    colorio.show_visible_slice(cs, lightness)
    # colorio.save_visible_slice("visible-slice.png", cs, lightness)


def test_rgb_slice():
    cs = colorio.cs.CIELAB()
    colorio.show_rgb_slice(cs, lightness=50, n=100)


@pytest.mark.parametrize(
    "colorspace",
    [
        colorio.cs.CIELAB(),
        # test against xyy to trigger ~self.is_origin_well_defined
        colorio.cs.XYY(1),
        colorio.cs.CAM02("UCS", 0.69, 20, 64 / np.pi / 5),
    ],
)
@pytest.mark.parametrize("variant", ["srgb", "hdr"])
def test_srgb_gamut(colorspace, variant, n=10):
    with tempfile.TemporaryDirectory() as tmpdir:
        colorio.save_rgb_gamut(colorspace, Path(tmpdir) / "srgb.vtu", variant, n=n)


@pytest.mark.parametrize(
    "colorspace",
    [
        colorio.cs.CIELAB(),
        colorio.cs.XYY(1),
        colorio.cs.CAM02("UCS", 0.69, 20, 64 / np.pi / 5),
    ],
)
def test_cone_gamut(colorspace):
    observer = colorio.observers.cie_1931_2()
    with tempfile.TemporaryDirectory() as tmpdir:
        colorio.save_cone_gamut(
            colorspace, Path(tmpdir) / "cone.vtu", observer, max_Y=1
        )


def test_visible_gamut():
    colorspace = colorio.cs.XYY(1)
    illuminant = colorio.illuminants.d65()
    observer = colorio.observers.cie_1931_2()
    with tempfile.TemporaryDirectory() as tmpdir:
        colorio.save_visible_gamut(
            colorspace, observer, illuminant, Path(tmpdir) / "visible.vtu"
        )


def test_srgb_gradient():
    # cs = colorio.cs.CIELAB()
    cs = colorio.cs.OKLAB()
    # cs = colorio.cs.DIN99()
    # cs = colorio.cs.CIELUV()
    colorio.show_srgb255_gradient(cs, [0, 0, 255], [255, 255, 0])


def test_primary_srgb_gradient():
    cs = colorio.cs.CIELAB()
    # cs = colorio.cs.OKLAB()
    colorio.show_primary_srgb_gradients(cs)
