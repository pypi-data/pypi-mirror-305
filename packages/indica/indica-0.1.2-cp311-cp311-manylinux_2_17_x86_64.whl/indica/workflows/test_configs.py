import hydra
from omegaconf import DictConfig


@hydra.main(version_base=None, config_path="../configs/workflows/bda_run", config_name="test_config", )
def test_configs(cfgs: DictConfig):
    print(cfgs)
    return


test_configs()
