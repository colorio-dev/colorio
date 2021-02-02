import matplotlib.pyplot as plt
import dufte

import colorio

plt.style.use(dufte.style)

# cs = colorio.cs.CIELAB()
# colorio.save_rgb_slice("srgb-gamut-slice-cielab.png", cs, lightness=50, n=101)
#
# cs = colorio.cs.OKLAB()
# colorio.save_rgb_slice("srgb-gamut-slice-oklab.png", cs, lightness=0.5, n=101)
#
# cs = colorio.cs.CAM16UCS(0.69, 20, 4.07)
# colorio.save_rgb_slice("srgb-gamut-slice-cam16.png", cs, lightness=50, n=101)

# cs = colorio.cs.XYY(1)
# colorio.plot_rgb_slice(cs, lightness=0.5, n=101)
# colorio.plot_visible_slice(cs, lightness=0.5)
# plt.savefig("visible-gamut-slice-xyy.png", transparent=True, bbox_inches="tight")

# cs = colorio.cs.JzAzBz()
# # colorio.plot_rgb_slice(cs, lightness=0.15, n=101)
# colorio.plot_visible_slice(cs, lightness=0.5)
# plt.savefig("visible-gamut-slice-jzazbz.png", transparent=True, bbox_inches="tight")
# # plt.gca().set_aspect("equal")
# # plt.gca().grid(False)

# cs = colorio.cs.OKLAB()
# colorio.plot_rgb_slice(cs, lightness=0.5, n=101)
# colorio.plot_visible_slice(cs, lightness=0.5)
# plt.savefig("visible-gamut-slice-oklab.png", transparent=True, bbox_inches="tight")

# data = [
#     ("munsell-xyy.svg", colorio.cs.XYY(1)),
#     ("munsell-cielab.svg", colorio.cs.CIELAB()),
#     ("munsell-cam16.svg", colorio.cs.CAM16UCS(0.69, 20, 4.07)),
# ]
# for filename, cs in data:
#     colorio.data.Munsell().plot(cs, V=5)
#     plt.gca().set_aspect("equal")
#     plt.gca().grid(False)
#     plt.savefig(filename, transparent=True, bbox_inches="tight")
#     plt.close()


# data = [
#     ("macadam1942-xyy.svg", colorio.cs.XYY(1)),
#     ("macadam1942-cielab.svg", colorio.cs.CIELAB()),
#     ("macadam1942-cam16.svg", colorio.cs.CAM16UCS(0.69, 20, 4.07)),
# ]
# for filename, cs in data:
#     colorio.data.MacAdam1942(50.0).plot(cs)
#     plt.gca().set_aspect("equal")
#     plt.gca().grid(False)
#     # plt.show()
#     plt.savefig(filename, transparent=True, bbox_inches="tight")
#     plt.close()
#
#
# data = [
#     ("luo-rigg-xyy.svg", colorio.cs.XYY(1)),
#     ("luo-rigg-cielab.svg", colorio.cs.CIELAB()),
#     ("luo-rigg-cam16.svg", colorio.cs.CAM16UCS(0.69, 20, 4.07)),
# ]
# for filename, cs in data:
#     colorio.data.LuoRigg(8).plot(cs)
#     plt.gca().set_aspect("equal")
#     plt.gca().grid(False)
#     # plt.show()
#     plt.savefig(filename, transparent=True, bbox_inches="tight")
#     plt.close()

# data = [
#     ("ebner-fairchild-xyy.svg", colorio.cs.XYY(1)),
#     ("ebner-fairchild-cielab.svg", colorio.cs.CIELAB()),
#     ("ebner-fairchild-cam16.svg", colorio.cs.CAM16UCS(0.69, 20, 4.07)),
# ]
# for filename, cs in data:
#     colorio.data.EbnerFairchild().plot(cs)
#     plt.gca().set_aspect("equal")
#     plt.gca().grid(False)
#     # plt.show()
#     plt.savefig(filename, transparent=True, bbox_inches="tight")
#     plt.close()
#
#
# data = [
#     ("hung-berns-xyy.svg", colorio.cs.XYY(1)),
#     ("hung-berns-cielab.svg", colorio.cs.CIELAB()),
#     ("hung-berns-cam16.svg", colorio.cs.CAM16UCS(0.69, 20, 4.07)),
# ]
# for filename, cs in data:
#     colorio.data.HungBerns().plot(cs)
#     plt.gca().set_aspect("equal")
#     plt.gca().grid(False)
#     # plt.show()
#     plt.savefig(filename, transparent=True, bbox_inches="tight")
#     plt.close()
#
#
# data = [
#     ("xiao-xyy.svg", colorio.cs.XYY(1)),
#     ("xiao-cielab.svg", colorio.cs.CIELAB()),
#     ("xiao-cam16.svg", colorio.cs.CAM16UCS(0.69, 20, 4.07)),
# ]
# for filename, cs in data:
#     colorio.data.Xiao().plot(cs)
#     plt.gca().set_aspect("equal")
#     plt.gca().grid(False)
#     # plt.show()
#     plt.savefig(filename, transparent=True, bbox_inches="tight")
#     plt.close()


# data = [
#     ("macadam1974-xyy.svg", colorio.cs.XYY(1)),
#     ("macadam1974-cielab.svg", colorio.cs.CIELAB()),
#     ("macadam1974-cam16.svg", colorio.cs.CAM16UCS(0.69, 20, 4.07)),
# ]
# for filename, cs in data:
#     colorio.data.MacAdam1974().plot(cs)
#     plt.gca().set_aspect("equal")
#     plt.gca().grid(False)
#     # plt.show()
#     plt.savefig(filename, transparent=True, bbox_inches="tight")
#     plt.close()


data = [
    ("fairchild-chen-xyy.svg", colorio.cs.XYY(1)),
    ("fairchild-chen-cielab.svg", colorio.cs.CIELAB()),
    ("fairchild-chen-cam16.svg", colorio.cs.CAM16UCS(0.69, 20, 4.07)),
]
for filename, cs in data:
    colorio.data.FairchildChen("SL2").plot(cs)
    # plt.gca().set_aspect("equal")
    # plt.gca().grid(False)
    # plt.show()
    plt.savefig(filename, transparent=True, bbox_inches="tight")
    plt.close()
