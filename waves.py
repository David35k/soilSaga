import random, utilClasses

# make all the waves here (can't spawn enemies on last frame of wave)
wave1 = utilClasses.Wave(
    [
        ["robotBasicSlow", 25 * 60],
    ],
    25 * 60 + 1,
)
wave2 = utilClasses.Wave(
    [
        ["robotBasicSlow", 25 * 60],
        ["robotBasicSlow", 30 * 60],
        ["robotBasicSlow", 35 * 60],
        ["robotBasic", 45 * 60],
    ],
    45 * 60 + 1,
)
wave3 = utilClasses.Wave(
    [
        ["robotBasicSlow", 30 * 60],
        ["robotBasicSlow", 40 * 60],
        ["robotBasicSlow", 50 * 60],
        ["robotBasic", 50 * 60],
        ["robotBasicSlow", 60 * 60],
    ],
    60 * 60 + 1,
)
wave4 = utilClasses.Wave(
    [
        ["robotBasic", 15 * 60],
        ["robotBasic", 15 * 60],
        ["robotBasicSlow", 50 * 60],
        ["robotBasic", 50 * 60],
        ["robotBasicSlow", 60 * 60],
    ],
    60 * 60 + 1,
)
wave5 = utilClasses.Wave(
    [
        ["tractorBot", 15 * 60],
    ],
    60 * 100 + 1,
)
wave9 = utilClasses.Wave(
    [
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
        ["robotBasic", random.randint(60 * 10, 60 * 120)],
        ["assaultBot", random.randint(60 * 10, 60 * 120)],
        ["tractorBot", random.randint(60 * 10, 60 * 120)],
        ["teleportBot", random.randint(60 * 10, 60 * 120)],
        ["laneBot", random.randint(60 * 10, 60 * 120)],
    ],
    60 * 120 + 1,
)

wave10 = utilClasses.Wave(
    [
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
        ["robotBasic", random.randint(60 * 1, 60 * 10)],
        ["assaultBot", random.randint(60 * 1, 60 * 10)],
        ["tractorBot", random.randint(60 * 1, 60 * 10)],
        ["teleportBot", random.randint(60 * 1, 60 * 10)],
        ["laneBot", random.randint(60 * 1, 60 * 10)],
    ],
    60 * 10 + 1,
)