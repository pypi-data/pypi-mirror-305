#!/usr/bin/env python3
import os
import tempfile
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

# This imports from site-packages
# from bdrc_bag.src.bdrc_bag import bag_ops
import bdrc_bag.bag_ops as bag_ops
from archive_ops.InvertWork import invert_work as aoInvertWork

_bag: Path
test_bag_work: Path

media: [str] = ["images", "archive"]


@pytest.fixture(autouse=True)
def build_bag(tmp_path):
    """
    Create the config file used in the tests
    """
    global _bag
    global test_bag_work
    _bag = tmp_path
    test_bag_work = _bag / "Work1"
    for medium in media:
        for ig in range(1, 3):
            bag_src_home: Path = test_bag_work / medium / f"w1-ig{ig}"
            bag_src_home.mkdir(parents=True, exist_ok=True)
            # Create a couple of file
            for i in range(1, 4):
                with open(bag_src_home / f"ig{ig}{i:0>4}.{medium}.txt", "w") as f:
                    f.write(f"I'm file{i}.txt")

    # make other non ig related
    for non_ig_media in ["meta", "sources"]:
        for non_ig in range(1, 3):
            non_ig_dir: Path = test_bag_work / non_ig_media / f"{non_ig_media}_files{non_ig}"
            non_ig_dir.mkdir(parents=True, exist_ok=True)
            for i in range(1, 5):
                with open(non_ig_dir / f"{non_ig_media}{non_ig}{i:0>4}.txt", "w") as f:
                    f.write(f"I'm file{i}.txt")


@pytest.mark.parametrize("is_daemon", [True, False])
def test_bag(is_daemon: bool):
    assert Path.exists(test_bag_work)
    # Make a destination
    with TemporaryDirectory() as td:
        bag_dst = Path(td)
        bag_ops.bag(str(test_bag_work), str(bag_dst), True, in_daemon=is_daemon)
        assert Path.exists(bag_dst)
        assert bag_dst.is_dir()
        assert bag_dst / "data" / "w1-ig1" / "ig10001.txt"
        # unbag it
        with TemporaryDirectory() as td2:
            bag_ops.debag(str(bag_dst / "Work1.bag.zip"), td2, is_daemon)
            test_root: Path = Path(td2) / "Work1" / "images" / "w1-ig1"
            assert Path.exists(test_root / "ig10001.images.txt")
            assert Path.exists(test_root / "ig10002.images.txt")
            assert Path.exists(test_root / "ig10003.images.txt")
            assert not Path.exists(Path(td2) / "data")


@pytest.mark.parametrize("is_daemon", [True, False])
def test_debag(is_daemon: bool):
    bag_artifact = "Work1.bag.zip"
    assert Path.exists(test_bag_work)
    # Make a destination
    with TemporaryDirectory() as td:
        bag_dst = Path(td)
        bag_ops.bag(str(test_bag_work), str(bag_dst), True, in_daemon=False)
        assert Path.exists(bag_dst)
        assert bag_dst.is_dir()

        created_bag_path: Path = bag_dst / bag_artifact
        assert Path.exists(created_bag_path)
        # The above created 'Work1.bag.zip" in bag_dst
        # Unbag it
        with TemporaryDirectory() as td2:
            bag_ops.debag(str(created_bag_path), td2, is_daemon)
            extracted_bag_images = Path(td2, "Work1", "images")
            for i in range(1, 3):
                assert Path.exists(extracted_bag_images / "w1-ig1" / f"ig1{i:0>4}.images.txt")
            assert Path.exists(Path(td2) / "bags")


# search a path for subdirectories whose names contain any of the strings in a list of strings
def get_dirs_for_image_groups(search_work: Path, image_groups: [str]) -> [str]:
    """
    :param search_work:
    :param image_groups:
    :return:
    """
    #
    # Need uniqueness
    matching_dirs: set = set()
    # Iterdir only searches immediate descendants
    for media_dir in search_work.iterdir():
        for ig_dir in media_dir.iterdir():
            if ig_dir.is_dir() and any(s in ig_dir.name for s in image_groups):
                matching_dirs.add(media_dir.name)
    return list(matching_dirs)


def test_inverted():
    """
    Test scanning a work archive for directories that contain directories whose name
     contains any of the image groups catalogued in the work.
    :return:
    """

    # Patch ao get_dirs_for_image_groups, for non-catalogued work
    # in production, use archive_ops.api.get_volumes_in_work()
    # import archive_ops.api
    image_groups: [str] = ["ig1", "ig2"]
    media_with_image_group = get_dirs_for_image_groups(test_bag_work, image_groups)
    with TemporaryDirectory() as td:
        inverted_work = Path(td) / "Inverted"
        os.makedirs(inverted_work, exist_ok=True)
        aoInvertWork(test_bag_work, inverted_work, media_with_image_group)
        for i in range(1, 3):
            for j in range(1, 4):
                assert Path.exists(inverted_work / f"w1-ig{i}" / "images" / f"ig{i}000{j}.images.txt")
                assert Path.exists(inverted_work / f"w1-ig{i}" / "archive" / f"ig{i}000{j}.archive.txt")
        assert Path.exists(inverted_work / "sources" / "sources_files1" / "sources10001.txt")
        assert Path.exists(inverted_work / "meta" / "meta_files1" / "meta10002.txt")


def test_segmented():
    """
    Test internal of appending bags to a zipped bag.
    :return:
    """
    assert Path.exists(test_bag_work)
    # Make a destination
    td = tempfile.mkdtemp()
    #     with TemporaryDirectory(dir=append_to_name) as td:
    bag_parent_path = Path(td)

    # exclude list, for later
    exclude_list: [] = []
    #
    # create bags for media subdirs of test_bag_work
    for medium in media:
        to_bag: Path = test_bag_work / medium
        if not os.path.exists(to_bag):
            continue
        bag_ops.bag(str(to_bag), str(bag_parent_path), True, in_daemon=False, do_append=False)
        assert Path.exists(bag_parent_path / f"{medium}.bag.zip")
        exclude_list.append(test_bag_work / medium)
    assert bag_parent_path.is_dir()

    # Build a bag out of the other things
    # Append the bag to a named zip in the directory

    append_dest: Path = bag_parent_path / f"{test_bag_work.name}.bag.zip"
    for non_wig_media in os.listdir(test_bag_work):
        non_wig_path: Path = Path(non_wig_media)
        if non_wig_media in media:
            continue
        bag_ops.bag(str(test_bag_work / non_wig_path), str(bag_parent_path), True, in_daemon=False, do_append=True,
                    append_dest=append_dest)
    assert Path.exists(bag_parent_path)
    assert bag_parent_path.is_dir()

    assert Path.exists(append_dest)
    # The above created 'Work1.bag.zip" in bag_dst
    # Unbag it
    with TemporaryDirectory() as td2:
        #
        # Debag all zips in the assembly directory
        for zip_file in os.listdir(bag_parent_path):
            bag_ops.debag(str(bag_parent_path / zip_file), td2, False)
        # bag_ops.debag(str(append_dest), td2, False)

        # Find the images
        extracted_bag_images = Path(td2, "images")
        for i in range(1, 3):
            assert Path.exists(extracted_bag_images / "w1-ig1" / f"ig1{i:0>4}.images.txt")

        # Find the non ig media
        for non_ig_media in ["meta", "sources"]:
            for non_ig in range(1, 3):
                non_ig_dir: Path = Path(td2) / non_ig_media / f"{non_ig_media}_files{non_ig}"
                for i in range(1, 5):
                    assert Path.exists(non_ig_dir / f"{non_ig_media}{non_ig}{i:0>4}.txt")
        # And make sure the debagged bags are there
        assert Path.exists(Path(td2) / "bags")
        assert (Path(td2) / "bags").is_dir()
