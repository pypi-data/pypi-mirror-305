"""Tests video_utils"""
import h5py
import imageio_ffmpeg as mpg
import numpy as np
import pytest

import aind_ophys_utils.video_utils as vu


@pytest.mark.parametrize(
    ("array, input_fps, output_fps, strategy, expected"),
    [
        (
            # average downsample video file with this dataset:
            np.array(
                [
                    [[1, 1], [1, 1]],
                    [[2, 2], [2, 2]],
                    [[3, 3], [3, 3]],
                    [[4, 4], [4, 4]],
                    [[5, 5], [5, 5]],
                    [[6, 6], [6, 6]],
                    [[7, 7], [7, 7]],
                ]
            ),
            7,
            2,
            "average",
            np.array([[[2.5, 2.5], [2.5, 2.5]], [[6.0, 6.0], [6.0, 6.0]]]),
        ),
    ],
)
def test_video_downsample(
    array, input_fps, output_fps, strategy, expected, tmp_path
):
    """Test downsample_h5_video"""
    video_file = tmp_path / "sample_video_file.h5"
    with h5py.File(video_file, "w") as h5f:
        h5f.create_dataset("data", data=array)

    downsampled_video = vu.downsample_h5_video(
        video_file, input_fps, output_fps, strategy
    )

    assert np.array_equal(downsampled_video, expected)


def compare_videos(encoded_video_path: str, expected_video: np.ndarray):
    """Compare an encoded video with its original source"""

    reader = mpg.read_frames(
        encoded_video_path, pix_fmt="gray8", bits_per_pixel=8
    )
    meta = reader.__next__()
    obt_nframes = int(np.round(meta["duration"] * meta["fps"]))

    assert obt_nframes == len(expected_video)

    obt_frames = []
    for frame in reader:
        parsed_frame = np.frombuffer(frame, dtype="uint8")
        parsed_frame = parsed_frame.reshape(meta["size"][::-1])
        obt_frames.append(parsed_frame)
    obt_video = np.array(obt_frames)

    assert obt_video.shape == expected_video.shape
    # the default settings for imageio-ffmpeg are not lossless
    # so can't test for exact match
    np.testing.assert_allclose(obt_video, expected_video, atol=20)


@pytest.fixture
def raw_video_fixture(request):
    """Create a test video"""
    video_shape = request.param.get("video_shape", (16, 32))
    nframes = request.param.get("nframes", 25)
    fps = request.param.get("fps", 30)
    rng_seed = request.param.get("rng_seed", 0)

    rng = np.random.default_rng(rng_seed)

    raw_video = [
        rng.integers(0, 256, size=video_shape, dtype="uint8")
        for _ in range(nframes)
    ]

    result = {}
    result["raw_video"] = np.array(raw_video)
    result["fps"] = fps
    result["nframes"] = nframes

    return result


@pytest.mark.parametrize(
    "raw_video_fixture",
    [
        # make the test video a size of at least 16x16
        # otherwise, need to mess with macro_block_size arg
        ({"video_shape": (16, 16)}),
        ({"video_shape": (32, 16)}),
    ],
    indirect=["raw_video_fixture"],
)
def test_encode_video(raw_video_fixture, tmp_path):
    """Test encode_video"""
    output_path = tmp_path / "test_video.webm"

    fps = raw_video_fixture["fps"]
    expected_video = raw_video_fixture["raw_video"]

    vu.encode_video(
        video=expected_video, output_path=output_path.as_posix(), fps=fps
    ),

    compare_videos(output_path, expected_video)
