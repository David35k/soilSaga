import random, utilClasses

# make all the waves here (can't spawn enemies on last frame of wave)
wave1 = utilClasses.Wave(
    [
        ["robotBasicSlow", 25 * 60],
    ],
    30 * 60 + 1,
)
wave2 = utilClasses.Wave(
    [
        ["robotBasicSlow", 35 * 60],
        ["robotBasicSlow", 40 * 60],
        ["robotBasic", 45 * 60],
    ],
    45 * 60 + 1,
)
wave3 = utilClasses.Wave(
    [
        ["robotBasicSlow", 5 * 60],
        ["robotBasicSlow", 10 * 60],
        ["robotBasicSlow", 15 * 60],
        ["robotBasic", 20 * 60],
        ["robotBasicSlow", 25 * 60],
        ["robotBasicSlow", 30 * 60],
    ],
    35 * 60 + 1,
)
wave4 = utilClasses.Wave(
    [
        ["robotBasic", 10 * 60],
        ["robotBasic", 15 * 60],
        ["robotBasic", 17 * 60],
        ["robotBasicSlow", 25 * 60],
        ["robotBasicSlow", 27 * 60],
        ["robotBasic", 28 * 60],
        ["robotBasicSlow", 29 * 60],
        ["robotBasic", 30 * 60],
        ["robotBasicSlow", 30 * 60],
    ],
    35 * 60 + 1,
)
wave5 = utilClasses.Wave(
    [
        ["tractorBot", 15 * 60],
        ["robotBasic", 16 * 60],
        ["robotBasic", 17 * 60],
        ["tractorBot", 20 * 60],
        ["robotBasic", 11 * 60],
        ["robotBasic", 14 * 60],
        ["assaultBot", 25 * 60],
        ["robotBasic", 30 * 60],
        ["tractorBot", 40 * 60],
        ["tractorBot", 45 * 60],
        ["assaultBot", 42 * 60],
        ["assaultBot", 47 * 60],
    ],
    55 * 60 + 1,
)
wave6 = utilClasses.Wave(
    [
        ["tractorBot", 15 * 60],
        ["robotBasic", 16 * 60],
        ["robotBasic", 17 * 60],
        ["tractorBot", 20 * 60],
        ["robotBasic", 11 * 60],
        ["robotBasic", 14 * 60],
        ["assaultBot", 25 * 60],
        ["robotBasic", 30 * 60],
        ["tractorBot", 40 * 60],
        ["tractorBot", 45 * 60],
        ["assaultBot", 42 * 60],
        ["assaultBot", 47 * 60],
    ],
    55 * 60 + 1,
)
wave7 = utilClasses.Wave(
    [
        ["laneBot", 5],
        ["laneBot", 10],
        ["laneBot", 11],
        ["laneBot", 12],
        ["laneBot", 13],
        ["laneBot", 14],
        ["laneBot", 15],
        ["assaultBot", 20],
        ["tractorBot", 21],
        ["assaultBot", 22],
        ["tractorBot", 23],
        ["assaultBot", 24],
        ["tractorBot", 25],
        ["assaultBot", 30],
        ["tractorBot", 31],
        ["assaultBot", 32],
        ["tractorBot", 33],
        ["assaultBot", 34],
    ],
    45 * 60 + 1,
)
wave8 = utilClasses.Wave(
    [
        ["laneBot", 5],
        ["laneBot", 10],
        ["laneBot", 11],
        ["laneBot", 12],
        ["laneBot", 13],
        ["laneBot", 14],
        ["laneBot", 15],
        ["assaultBot", 20],
        ["tractorBot", 21],
        ["assaultBot", 22],
        ["tractorBot", 23],
        ["assaultBot", 24],
        ["tractorBot", 25],
        ["assaultBot", 30],
        ["tractorBot", 31],
        ["assaultBot", 32],
        ["tractorBot", 33],
        ["assaultBot", 34],
        ["robotBasic", random.randint(37 * 60, 60 * 45)],
        ["assaultBot", random.randint(37 * 10, 60 * 45)],
        ["tractorBot", random.randint(37 * 10, 60 * 45)],
        ["teleportBot", random.randint(37 * 10, 60 * 45)],
        ["laneBot", random.randint(37 * 10, 60 * 45)],
        ["robotBasic", random.randint(47 * 60, 60 * 50)],
        ["assaultBot", random.randint(47 * 10, 60 * 50)],
        ["tractorBot", random.randint(47 * 10, 60 * 50)],
        ["teleportBot", random.randint(47 * 10, 60 * 50)],
        ["laneBot", random.randint(47 * 10, 60 * 50)],
        ["robotBasic", random.randint(52 * 60, 60 * 57)],
        ["assaultBot", random.randint(52 * 10, 60 * 57)],
        ["tractorBot", random.randint(52 * 10, 60 * 57)],
        ["teleportBot", random.randint(52 * 10, 60 * 57)],
        ["laneBot", random.randint(52 * 10, 60 * 57)],
    ],
    60 * 60 + 1,
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
    ],
    130 * 60 + 1,
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
        ["robotBasicSlow", 15 * 60],
    ],
    15 * 60 + 1,
)
