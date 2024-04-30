#! python

import argparse


def parse_file(filepath: str) -> dict[int, str]:
    try:
        with open(filepath, "r") as f:
            game_list = [line.strip("\n") for line in f.readlines()]
    except IOError as ioe:
        print(ioe)

    return {game_id: parse_game(game) for game_id, game in enumerate(game_list,
                                                                     1)}


def parse_game(game: str) -> dict:
    cube_sets = game.split(":")[1]
    game = [
        cube.strip()
        for cube_set in cube_sets.split(";")
        for cube in cube_set.split(",")
    ]
    classified_game = parse_color(game)
    return get_max(classified_game)


def parse_color(game: list) -> dict[str, list[int]]:
    sets = {}
    for cubes_set in game:
        nb, cube = cubes_set.split(" ")
        key = "red" if "red" in cube else "blue" if "blue" in cube else "green"
        sets.setdefault(key, []).append(int(nb))
    return sets


def get_max(game: dict[str, list[int]]) -> dict[str, int]:
    return {color: max(cube_nbs) for color, cube_nbs in game.items()}


def color_max_filter(
    games: dict[int, dict[str, int]], color: str, max_cubes_nb: int
) -> int:
    filtered_games = {
        game_id: colors
        for game_id, colors in games.items()
        if colors[color] <= max_cubes_nb
    }

    return filtered_games.keys()


def main(*args) -> None:
    games = parse_file(args[0])

    green_ids = color_max_filter(games, "green", 13)
    blue_ids = color_max_filter(games, "blue", 14)
    red_ids = color_max_filter(games, "red", 12)

    solution = sum(
        [game_id for game_id in red_ids
            if game_id in green_ids
            and game_id in blue_ids]
    )

    print(f"Solution is {solution}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-filepath", "-f", type=str, required=True)

    args = parser.parse_args()
    main(args.filepath)
