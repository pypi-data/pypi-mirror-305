import numpy as np

def Gaussian(x, x0, amp, fwhm):
    return amp * np.exp(-(x-x0)**2/ 2 / (fwhm/2.3548)**2)


if __name__ == '__main__':
    assert( Gaussian(1, 1, 1, 1) == 1.)
