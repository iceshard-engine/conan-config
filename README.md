> [!IMPORTANT]
> With Conan getting more and more feature rich this repository is no longer needed.
>
> - **remotes** - Addign a single public remote via command-line is faster than running `conan config get` command.
> - **profiles** - The profiles defined here are not usefull unless you have the exact tools installed.
> - **hooks** - Conan now allows packages to generate files wich just requiring the generator in `[tool_requires]` section.

# IceShard conan configurations
Conan configuration profiles and settings to be used with various other projects and conan packages.

# Remotes

Provides remotes for the following three repostories:
* Conan2 Center (https://center.conan.io) - Conan2 Center Repository
* Conan2 IceShard ([https://code.iceshard.net](https://code.iceshard.net/libraries/-/packages)) - IceShard Public Repository (provides recipes only)

# Profiles

Currently the following profiles are defined for IceShard:
* Linux (x64, C++20, clang20)
* Windows (x64, C++20, msvc194)

# Hooks (Conan v2)

Since Conan v2 does not allow us to provide custom generators anymore inside packages we need to implement a pre-generation hook globally.

This allows us to generate required `.bff` files for `ice-build-tools`.
The hook also removes the generator from the recipe generators list so it will not cause an error in conan.

This is not the cleanest way but one that works and does not disturb other packages.
