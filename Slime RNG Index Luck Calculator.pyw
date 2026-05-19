import importlib.util
from pathlib import Path


script_path = Path(__file__).with_suffix(".py")
spec = importlib.util.spec_from_file_location("slime_rng_index_luck_calculator", script_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.main()
