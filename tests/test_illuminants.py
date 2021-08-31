import matplotlib.pyplot as plt
import numpy as np
import pytest

import colorio


@pytest.mark.parametrize(
    "illuminant,decimals,values",
    [
        (colorio.illuminants.a(5e-9), 5, [0.93048, 1.12821, 1.35769]),
        (colorio.illuminants.d50(), 3, [0.019, 2.051, 7.778]),
        (colorio.illuminants.d55(), 3, [0.024, 2.072, 11.224]),
        (colorio.illuminants.d65(), 4, [0.03410, 3.2945, 20.2360]),
        # 5.132 is different from the standard; 5.133 is listed there. This is a
        # false rounding.
        (colorio.illuminants.d75(), 3, [0.043, 5.132, 29.808]),
    ],
)
def test_values(illuminant, decimals, values):
    _, data = illuminant
    rdata = np.around(data, decimals=decimals)
    assert rdata[0] == values[0]
    assert rdata[1] == values[1]
    assert rdata[2] == values[2]


# TODO make sure we see the actual whitepoints here
@pytest.mark.parametrize(
    "illuminant,ref",
    [
        (colorio.illuminants.d65(), [95.04897383777654, 100.0, 108.89219744235048]),
        (colorio.illuminants.e(), [100.01501815954022, 100.0, 100.06659759493049]),
        (colorio.illuminants.f2(), [99.14684057651468, 100.0, 67.31849751003291]),
        (colorio.illuminants.f7(), [95.01911237699836, 100.0, 108.63853342005218]),
        (colorio.illuminants.f11(), [100.90356906939995, 100.0, 64.28441370480544]),
    ],
)
def test_white_point(illuminant, ref):
    print(illuminant)
    values = colorio.illuminants.white_point(illuminant)
    print(list(values))
    assert np.all(abs(values - ref) < 1.0e-13 * np.abs(ref))


def test_show():
    lmbda, data = colorio.illuminants.d65()
    plt.plot(lmbda, data)
    # for T in [1000, 2000, 3000, 4000, 5000, 1000]:
    #     lmbda, data = colorio.illuminants.planckian_radiator(T)
    #     plt.plot(lmbda, data)
    plt.ylim(ymin=0)
    plt.show()


def test_spectrum_to_xyz100():
    spectrum = colorio.illuminants.d65()
    observer = colorio.observers.cie_1931_2()
    out = colorio.illuminants.spectrum_to_xyz100(spectrum, observer)
    out = out / out[1] * 100
    print(list(out))
    ref = [95.04897383777654, 100.0, 108.89219744235048]
    assert np.all(np.abs(out - ref) < 1.0e-13 * np.abs(ref))


def test_equal_energy():
    spectrum = colorio.illuminants.e()
    observer = colorio.observers.cie_1931_2()
    # observer = colorio.observers.cie_1964_10()
    print(observer)
    out = colorio.illuminants.spectrum_to_xyz100(spectrum, observer)
    dat = observer[1]
    print(dat.shape)
    print()
    print(np.sum(dat[0]))
    print(np.sum(dat[1]))
    print(np.sum(dat[2]))
    print()
    print(np.sum(dat[0, ::5]) * 5)
    print(np.sum(dat[1, ::5]) * 5)
    print(np.sum(dat[2, ::5]) * 5)
    print()
    print(np.sum(dat[0]) - dat[0][0] / 2 - dat[0][-1] / 2)
    print(np.sum(dat[1]) - dat[1][0] / 2 - dat[1][-1] / 2)
    print(np.sum(dat[2]) - dat[2][0] / 2 - dat[2][-1] / 2)
    exit(1)
    print()
    print(np.sum(dat, axis=1))
    print()
    print(out)
    print(out / out[1] * 100)
    print()
    print(np.sum(dat, axis=1))
    exit(1)


if __name__ == "__main__":
    # test_white_point()
    test_show()
