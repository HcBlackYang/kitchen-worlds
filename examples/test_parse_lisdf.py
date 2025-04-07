from config import ASSET_PATH
from os.path import join, dirname
from lisdf.parsing.sdf_j import load_sdf

# test_cases = ['kitchen_counter', 'm0m_0_test', 'm0m_joint_test']
test_cases = ['kitchen_basics']
scene_paths = [join(ASSET_PATH, 'scenes', f'{l}.lisdf') for l in test_cases]
# scene_paths = ['/home/yang/Documents/kitchen-worlds/outputs/test_full_kitchen/1230-140406_original_3/scene.lisdf']

if __name__ == "__main__":
    for lisdf_path in scene_paths:
        lissdf_results = load_sdf(lisdf_path)
        models = lissdf_results.worlds[0].models
        print(f"{lisdf_path} has {len(models)} models\n", end='\r')
    print(f'finished parsing {len(test_cases)} scene files')

    for model in models:
        print(f"Available attributes in Model: {dir(model)}")

    for model in models:
        print(f"Converting {model.name} to URDF...")
        try:
            urdf_string = model.to_urdf()
            with open(f"{model.name}.urdf", "w") as f:
                f.write(urdf_string)
            print(f"Saved {model.name}.urdf")
        except FileNotFoundError as e:
            print(f"Skipping {model.name}, missing file: {e}")




