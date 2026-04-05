from coala import Lab
import pytest


def test_all_lab(tutorial_lab: Lab):
    # lab load 가 문제없는지 확인함
    assert isinstance(tutorial_lab, Lab)
    assert tutorial_lab.lab_name == "tutorial_lab"


@pytest.mark.asyncio
async def test_lab_integrity(tutorial_lab: Lab):
    """Verifies that all recipes in the lab are structurally sound and fusable."""
    await tutorial_lab.assert_is_fusable()


@pytest.mark.asyncio
async def test_fuse_fire_and_water(tutorial_lab: Lab):
    result = await tutorial_lab.fuse("fire", "water")
    assert result == "steam"
