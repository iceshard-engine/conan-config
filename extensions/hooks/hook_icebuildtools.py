import importlib.util
import sys, os

def pre_generate(conanfile):
    for require, dependency in conanfile.dependencies.build.items():
        conanfile.output.info("Dependency is direct={}: {}".format(require.direct, dependency.ref))

    try:
        # Remove the generator from the list as it's not a build-in type
        conanfile.generators.remove("FastBuildDeps")
        fbuild_generator_recipe = os.path.join(conanfile.dependencies.build['fastbuild-generator'].recipe_folder, "conanfile.py")

        # Load the conanfile.py recipe
        fbgen_spec = importlib.util.spec_from_file_location("fastbuild_generator", fbuild_generator_recipe)
        fbgen_module = importlib.util.module_from_spec(fbgen_spec)
        sys.modules["fastbuild_generator"] = fbgen_module
        fbgen_spec.loader.exec_module(fbgen_module)

        # Create the generator object and call .generate()
        generator = fbgen_module.FastBuildDeps(conanfile)
        conanfile.output.info("Executing FastBuildDeps generator")
        generator.generate(output_path=conanfile.generators_folder)

    except ValueError:
        pass  # do nothing!

    try:
        conanfile.generators.remove("JsonDeps")
        conanfile.output.warning("Json Generator!")
    except ValueError:
        pass  # do nothing!
