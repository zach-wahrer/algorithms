from models.maze import Maze, OBSTACLE, TRIED, PART_OF_PATH, DEAD_END


def search_from(maze, start_row, start_column):
    maze.update_position(start_row, start_column)

    if maze[start_row][start_column] == OBSTACLE:
        return False
    if maze[start_row][start_column] == TRIED:
        return False
    if maze.is_exit(start_row, start_column):
        return True

    maze.update_position(start_row, start_column, TRIED)

    found = search_from(maze, start_row + 1, start_column) or \
        search_from(maze, start_row, start_column + 1) or \
        search_from(maze, start_row - 1, start_column) or \
        search_from(maze, start_row, start_column - 1)

    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return found


my_maze = Maze('maze.txt')
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_col)

search_from(my_maze, my_maze.start_row, my_maze.start_col)
