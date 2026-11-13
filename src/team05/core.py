"""Core image preprocessing functions for ClearVision."""

from PIL import Image


def adjust_gamma(path: str, gamma: float = 0.5) -> Image.Image:
    """Adjust image brightness using non-linear gamma correction for low-light images.

    Args:
        path (str): Path to the input image file.
        gamma (float): Gamma correction factor. Values < 1.0 brighten dark regions.

    Returns:
        PIL.Image.Image: Brightness-adjusted RGB image preserving original resolution.

    Raises:
        ValueError: If ``gamma`` is not positive.
        FileNotFoundError: If ``path`` does not exist.

    Examples:
        >>> img = adjust_gamma("samples/night.jpg", gamma=0.5)
        >>> img.mode
        'RGB'
    """
    raise NotImplementedError


def apply_clahe(
    path: str, clip_limit: float = 2.0, tile_grid_size: tuple[int, int] = (8, 8)
) -> Image.Image:
    """Enhance local contrast using Contrast Limited Adaptive Histogram Equalization.

    Args:
        path (str): Path to the input image file.
        clip_limit (float): Threshold for contrast limiting to prevent noise amplification.
        tile_grid_size (tuple[int, int]): Size of grid for histogram equalization.

    Returns:
        PIL.Image.Image: Contrast-enhanced RGB image.

    Raises:
        ValueError: If ``clip_limit`` is not positive.

    Examples:
        >>> img = apply_clahe("samples/night.jpg", clip_limit=2.0)
        >>> img.size[0] > 0
        True
    """
    raise NotImplementedError


def denoise_bilateral(
    path: str, d: int = 9, sigma_color: float = 75.0, sigma_space: float = 75.0
) -> Image.Image:
    """Reduce high-frequency sensor noise while preserving sharp edges.

    Args:
        path (str): Path to the input image file.
        d (int): Diameter of each pixel neighborhood used during filtering.
        sigma_color (float): Filter sigma in the color space.
        sigma_space (float): Filter sigma in the coordinate space.

    Returns:
        PIL.Image.Image: Denoised RGB image with preserved edges.

    Raises:
        ValueError: If ``d`` is not a positive integer.

    Examples:
        >>> img = denoise_bilateral("samples/noisy.jpg", d=9)
        >>> img.mode
        'RGB'
    """
    raise NotImplementedError


def dehaze_dark_channel(path: str, omega: float = 0.95) -> Image.Image:
    """Remove haze and atmospheric scattering using Dark Channel Prior.

    Args:
        path (str): Path to the input hazy image file.
        omega (float): Haze removal retention factor between 0.0 and 1.0.

    Returns:
        PIL.Image.Image: Dehazed RGB image with restored visibility.

    Raises:
        ValueError: If ``omega`` is not between 0.0 and 1.0.

    Examples:
        >>> img = dehaze_dark_channel("samples/foggy.jpg", omega=0.95)
        >>> img.mode
        'RGB'
    """
    raise NotImplementedError