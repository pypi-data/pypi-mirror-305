import pooch
import xarray as xr

server = "https://callumrollo.com/files"
data_source_og = pooch.create(
    path=pooch.os_cache("glidertest"),
    base_url=server,
    registry={
        "sea076_20230906T0852_R.nc": "sha256:19e55e7018dc578a58a184b9d03e403e18470f59d20038deff59ab962c737902",
        "sea076_20230906T0852_delayed.nc": "sha256:bd50b2c1019b49f8c14381de8f78aa67d66e9d9e89607bbcedff246be60e6c92",
        "sea055_20220104T1536_R.nc": "sha256:5687c9d7b383713ff730ad4a570689622fe6eb9807e340919d59a83a437773b9",
        "sea055_20220104T1536_delayed.nc": "sha256:7f72f8a0398c3d339687d7b7dcf0311036997f6855ed80cae5bbf877e09975a6",
    },
)


def load_sample_dataset(dataset_name="sea076_20230906T0852_delayed.nc"):
    if dataset_name in data_source_og.registry.keys():
        file_path = data_source_og.fetch(dataset_name)
        return xr.open_dataset(file_path)
    else:
        msg = f"Requested sample dataset {dataset_name} not known"
        raise ValueError(msg)
