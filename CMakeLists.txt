cmake_minimum_required(VERSION 3.16)
project(ioh-objective-server LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Build type" FORCE)
endif()
if(POLICY CMP0135)
    cmake_policy(SET CMP0135 NEW)
endif()

include(FetchContent)
# IOHexperimenter, built with the server: the problems and the Analyzer logger. It needs only its fmt submodule, and
# it finds its data files in its source tree.
FetchContent_Declare(
    iohexperimenter
    GIT_REPOSITORY https://github.com/IOHprofiler/IOHexperimenter.git
    GIT_TAG 8d6746c12af427394b023fc6531fa150371b110d
    GIT_SUBMODULES external/fmt)
# the JSON messages and the command line
FetchContent_Declare(
    nlohmann_json
    URL https://github.com/nlohmann/json/releases/download/v3.11.3/json.tar.xz
    URL_HASH SHA256=d6c65aca6b1ed68e7a182f4757257b107ae403032760ed6ef121c9d55e81757d)
FetchContent_Declare(
    cxxopts
    URL https://github.com/jarro2783/cxxopts/archive/refs/tags/v3.2.1.tar.gz
    URL_HASH SHA256=841f49f2e045b9c6365997c2a8fbf76e6f215042dda4511a5bb04bc5ebc7f88a)
set(CXXOPTS_BUILD_EXAMPLES OFF CACHE BOOL "" FORCE)
set(CXXOPTS_BUILD_TESTS OFF CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(iohexperimenter nlohmann_json cxxopts)

add_executable(ioh-server ioh-server.cpp)
target_link_libraries(ioh-server PRIVATE ioh::ioh nlohmann_json::nlohmann_json cxxopts::cxxopts)
install(TARGETS ioh-server)
