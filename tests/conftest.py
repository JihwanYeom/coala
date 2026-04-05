import asyncio
from logging import getLogger
from pathlib import Path
import pytest
import coala

log = getLogger(__name__)

# List to track created labs for proper teardown
_CREATED_LABS = []


async def _get_lab_async(lab_name: str, storage_path: str):
    """Asynchronously initializes a Lab."""
    lab = coala.Lab(lab_name, storage_path)
    await lab.start()
    _CREATED_LABS.append(lab)
    return lab


def get_lab(lab_name: str, storage_path: str):
    """Synchronous wrapper for _get_lab_async."""
    return asyncio.run(_get_lab_async(lab_name, storage_path))


@pytest.fixture(scope="session", autouse=True)
def cleanup_labs():
    """Session-scoped fixture to ensure all labs are closed after tests."""
    yield
    for lab in _CREATED_LABS:
        asyncio.run(lab.close())


def pytest_generate_tests(metafunc):
    """Dynamically parametrizes tests with Lab instances based on directory names."""
    # Discover all directories in the coala package that end with '_lab'
    coala_path = Path(coala.__file__).parent
    labs_dict = {
        path.name: path.name for path in coala_path.glob("*_lab") if path.is_dir()
    }

    for fixture_name in metafunc.fixturenames:
        if fixture_name in labs_dict:
            lab_name = labs_dict[fixture_name]

            # Use pytest's cache directory to store InfiniteCraft discoveries
            if metafunc.config.cache:
                cache_dir = metafunc.config.cache.mkdir("coala_discoveries")
                storage_path = str(cache_dir / f"{lab_name}.json")
            else:
                # Fallback to a temporary directory if cache is disabled
                import tempfile

                storage_path = str(
                    Path(tempfile.gettempdir()) / f"coala_{lab_name}.json"
                )

            lab = get_lab(lab_name, storage_path)
            metafunc.parametrize(fixture_name, (lab,), scope="session")
