# IceShard conan configurations
Conan configuration profiles and settings to be used with various other projects and conan packages.

# Remotes

Provides remotes for the following three repostories:
* Conan2 Center (https://center.conan.io)
* Conan2 IceShard (https://conan.iceshard.net)

# Profiles

Currently the following profiles are defined for IceShard:
* Linux (x64, C++20, clang20)
* Windows (x64, C++20, msvc194)

# Hooks (Conan v2)

Since Conan v2 does not allow us to provide custom generators anymore inside packages we need to implement a pre-generation hook globally.

This allows us to generate required `.bff` files for `ice-build-tools`.
The hook also removes the generator from the recipe generators list so it will not cause an error in conan.

This is not the cleanest way but one that works and does not disturb other packages.
