import numpy as np

from abc import ABC, abstractmethod
from numpy.polynomial import polynomial as P

# Interfaces / Abstract classes

class IProfilometry(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def heightmap(self, **kwargs):
        pass

class IFringeProfilometry(IProfilometry):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def heightmap(self, **kwargs):
        pass

    @abstractmethod
    def phasemaps_needed(self) -> int:
        pass

class PhaseHeight(IFringeProfilometry):
    """ Classic phase-height model

        Note: Camera and Projector must both be perpendicular to reference plane

        Extend this class and overload the calibrate / heightmap methods for your own functionality

    Args:
        calib_data : Calibration data required for heightmap reconstruction
    """
     
    def __init__(self, calib_data=None):
        self.__post_cbs = []

        self._calib_data = calib_data

    def heightmap(self, phasemaps):
        ref_phase = phasemaps[0]
        meas_phase = phasemaps[1]

        phase_diff = meas_phase - ref_phase

        # h = 𝜙𝐷𝐸 ⋅ 𝑝 ⋅ 𝑑 / 𝜙𝐷𝐸 ⋅ 𝑝 + 2𝜋𝑙

        a = phase_diff * self.calib_data[0] * self.calib_data[2]
        b = phase_diff * self.calib_data[0] + 2.0 * np.pi * self.calib_data[1]
        
        return a / b

    def calibrate(self, phasemaps, heights):
        return None
    
    @property
    def calib_data(self):
        return self._calib_data

    @property
    def phasemaps_needed(self) -> int:
        return 2

    @property
    def post_cbs(self):
        return self.__post_cbs
        
    def add_post_ref_cb(self, cb):
        """ TODO: Add description """
        self.__post_cbs.append(cb)

    def call_post_cbs(self):
        for cb in self.__post_cbs: cb()

class LinearInversePH(PhaseHeight):
    def __init__(self, calib_data=None):
        super().__init__(calib_data)
        
    def calibrate(self, phasemaps, heights):
        """
            The linear inverse calibration model for fringe projection setups.

            Note:   
                - The moving plane must be parallel to the camera 
                - The first phasemap is taken to be the reference phasemap

                Δ𝜙(x, y) = h(x, y)Δ𝜙(x, y)a(x, y) + h(x, y)b(x, y)
        """

        if (heights is None): raise TypeError

        # Check passed number of heights equals numebr of img steps
        if (li := len(phasemaps)) != (lh := len(heights)): 
            raise ValueError(f"You must provide an equal number of heights to phasemaps ({li} and {lh} given)")

        # Calculate phase difference maps at each height
        # Phase difference between ref and h = 0 is zero
        z, h, w = phasemaps.shape
        ref_phase = phasemaps[0] # Assume reference phasemap is first entry

        ph_maps = np.empty(shape=(z, h, w))
        ph_maps[0] = 0.0
        ph_maps[1:] = phasemaps[1:] - ref_phase

        # Least squares fit on a pixel-by-pixel basis to its height value (a, b)
        self._calib_data = np.empty(shape=(2, h, w), dtype=np.float64)

        # Δ𝜙(x, y) = h(x, y)Δ𝜙(x, y)a(x, y) + h(x, y)b(x, y)

        for y in range(h):
            for x in range(w):
                t = heights * ph_maps[:, y, x]

                A = np.vstack([t, np.ones(len(t))]).T
                m, c = np.linalg.lstsq(A, heights)[0]

                self._calib_data[0, y, x] = m
                self._calib_data[1, y, x] = c

    def heightmap(self, phasemaps):
        """ Obtain a heightmap using a set of reference and measurement images using the already calibrated values """

        # Check if number of phasemaps passed was correct
        if len(phasemaps) != self.phasemaps_needed:
            raise Exception(f"Provided number of phase maps is incorrect ({len(phasemaps)} passed, {self.phasemaps_needed} needed)")

        # Obtain phase difference
        ref_phase = phasemaps[0]
        img_phase = phasemaps[1]
        phase_diff = img_phase - ref_phase

        # Apply calibrated polynomial values to each pixel of the phase difference
        h, w = phase_diff.shape
        heightmap = np.zeros_like(phase_diff)

        for y in range(h):
            for x in range(w):
                heightmap[y, x] = phase_diff[y, x] / (phase_diff[y, x] * self._calib_data[0, y, x] + self._calib_data[1, y, x])

        return heightmap

class PolynomialPH(PhaseHeight):
    def __init__(self, calib_data=None, degree=5):
        super().__init__(calib_data)

        if not (self.calib_data is None):
            cs, h, w = self.calib_data.shape
            self.__degree = cs
            
        elif degree is None:
            raise Exception("You must provide a degree or existing calibration data for the calibration")
        
        else:
            self.__degree = degree

    @property
    def degree(self):
        """ The degree of the polynomial used for the last calibration """
        return self.__degree
        
    def calibrate(self, phasemaps, heights):
        """
            The polynomial calibration model for fringe projection setups.

            Note:   
                - The moving plane must be parallel to the camera 
                - The first phasemap is taken to be the reference phasemap
        """

        if (heights is None): raise TypeError

        # Check polynomial degree is greater than zero
        if self.degree < 1: raise ValueError("Degree of the polynomial must be greater than zero")

        # Check passed number of heights equals numebr of img steps
        if (li := len(phasemaps)) != (lh := len(heights)): 
            raise ValueError(f"You must provide an equal number of heights to phasemaps ({li} and {lh} given)")

        # Calculate phase difference maps at each height
        # Phase difference between ref and h = 0 is zero
        z, h, w = phasemaps.shape
        ref_phase = phasemaps[0] # Assume reference phasemap is first entry

        ph_maps = np.empty(shape=(z, h, w))
        ph_maps[0] = 0.0
        ph_maps[1:] = phasemaps[1:] - ref_phase

        # Polynomial fit on a pixel-by-pixel basis to its height value
        self._calib_data = np.empty(shape=(self.degree + 1, h, w), dtype=np.float64)

        for y in range(h):
            for x in range(w):
                self._calib_data[:, y, x] = P.polyfit(ph_maps[:, y, x], heights, deg=self.degree)

    def heightmap(self, phasemaps):
        """ Obtain a heightmap using a set of reference and measurement images using the already calibrated values """

        # Check if number of phasemaps passed was correct
        if len(phasemaps) != self.phasemaps_needed:
            raise Exception(f"Provided number of phase maps is incorrect ({len(phasemaps)} passed, {self.phasemaps_needed} needed)")

        # Obtain phase difference
        ref_phase = phasemaps[0]
        img_phase = phasemaps[1]
        phase_diff = img_phase - ref_phase

        # Apply calibrated polynomial values to each pixel of the phase difference
        h, w = phase_diff.shape
        heightmap = np.zeros_like(phase_diff)

        for y in range(h):
            for x in range(w):
                heightmap[y, x] = P.polyval(phase_diff[y, x], self._calib_data[:, y, x])

        return heightmap

    # def save_data(self, path):
    #     if self.__calib is None:
    #         raise Exception("You need to run/load calibration data first")

    #     

# class TriangularStereoHeight(PhaseHeight):
#     def __init__(self, ref_dist, sensor_dist, freq):
#         super().__init__()
        
#         self.ref_dist = ref_dist
#         self.sensor_dist = sensor_dist
#         self.freq = freq
    
#     def heightmap(self, imgs):
#         phase = self.phasemap(imgs)

#         #heightmap = np.divide(self.ref_dist * phase_diff, 2.0 * np.pi * self.sensor_dist * self.freq)
        
#         #heightmap[heightmap <= 0] = 0 # Remove negative values

#         return None

#     def to_stl(self, heightmap):
#         # Create vertices from the heightmap
#         vertices = []
#         for y in range(heightmap.shape[0]):
#             for x in range(heightmap.shape[1]):
#                 vertices.append([x, y, heightmap[y, x]])

#         vertices = np.array(vertices)

#         # Create faces for the mesh
#         faces = []
#         for y in range(heightmap.shape[0] - 1):
#             for x in range(heightmap.shape[1] - 1):
#                 v1 = x + y * heightmap.shape[1]
#                 v2 = (x + 1) + y * heightmap.shape[1]
#                 v3 = x + (y + 1) * heightmap.shape[1]
#                 v4 = (x + 1) + (y + 1) * heightmap.shape[1]

#                 # First triangle
#                 faces.append([v1, v2, v3])
#                 # Second triangle
#                 faces.append([v2, v4, v3])

#         # Create the mesh object
#         # mesh_data = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))
#         # for i, f in enumerate(faces):
#         #     for j in range(3):
#         #         mesh_data.vectors[i][j] = vertices[f[j]]

#         # mesh_data.save('heightmap_mesh.stl')