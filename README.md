# IceShard conan configurations
Conan configuration profiles and settings to be used with various other projects and conan packages.

## Conan v2

Since conan upgraded to the second version, lots of changes where required and are no longer compatible with conan v1.

> Additionally configurations used by Unix / MacOS builds are not tested yet so issues are expeted.

# Remotes

Provides remotes for the following three repostories:
* Conan Center (https://center.conan.io)
* IceShard (https://conan.iceshard.net)
* Bincrafters (https://bincrafters.jfrog.io/artifactory/api/conan/public-conan)

# Profiles

Currently the following profiles are available:
* Linux x64 (clang 9.0)
* Linux x64 (clang 10.0)
* Linux x64 (clang 11.0)
* Linux x64 (clang 12.0)
* Linux x64 (clang 11.0)
* Linux x64 (clang 12.0)

A profile for MSVC is nor provided currently but will be added in the near future.

# Hooks (Conan v2)

Since Conan v2 does not allow us to provide custom generators anymore inside packages we need to implement a pre-generation hook globally.

This allows us to generate required `.bff` files for `ice-build-tools`.
The hook also removes the generator from the recipe generators list so it will not cause an error in conan.

This is not the cleanest way but one that works and does not disturb other packages.

> Please note the hook is still a wip idea, and might not work always!
