from pathlib import Path

import numpy as np
from easy_kit.timing import TimingTestCase

from easy_raster.raster_io import RasterIO
from easy_raster.utils.factory import RFactory


class TestIt(TimingTestCase):
    def test_noise(self):
        buffer = RFactory.heightmap(256)
        path = Path.cwd() / 'toto.png'
        RasterIO.write_normalize(path, buffer)
        xxx = RasterIO.read(path, 0)
        path.unlink()
        self.assertTrue(np.allclose(xxx / 255, buffer, atol=.005))
