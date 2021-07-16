from setuptools import setup

setup(name = "hairgel_worms_dataset",
      entry_points = {"worm_dataset_loaders": ["hairgel_worms=hairgel_worms_loader"]})
