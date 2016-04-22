

class Solution:
    def __init__(self, n):
        """
        n: dimension of a lattice matrix
        """
        self.lattice_n = n   # will result in a (n+1) * (n+1) matrix
        self.lattice_path_count = 0   # only use for alpha implementation

    # This function print all possible paths
    # Not used for this problem
    def lattice_path_print(self, current_coord, current_path, total_paths):
        """
        current_coord: a tuple of current coordinate
        current_path: a list of coordinates
        total_path: a list of path (also list type)
        """
        coord_x = current_coord[0]
        coord_y = current_coord[1]

        p = current_path[:] # make a copy of current path
        p.append((coord_x, coord_y))
        if coord_x < self.lattice_n:
            self.lattice_path_print((coord_x+1, coord_y), p, total_paths)
        if coord_y < self.lattice_n:
            self.lattice_path_print((coord_x, coord_y+1), p, total_paths)
        if coord_x == self.lattice_n and coord_y == self.lattice_n:
            total_paths.append(p)


    # A naive recursive implementation, but is very slow as n gets large
    # Use another solution below instead
    def lattice_paths_alpha(self, current_coord):
        """
        current_coord: a tuple of current coordinate
        """
        coord_x = current_coord[0]
        coord_y = current_coord[1]

        if coord_x < self.lattice_n:
            self.lattice_paths_alpha((coord_x+1, coord_y))
        if coord_y < self.lattice_n:
            self.lattice_paths_alpha((coord_x, coord_y+1))
        if coord_x == self.lattice_n and coord_y == self.lattice_n:
            self.lattice_path_count += 1


    # Generate a matrix with each element indicating the number of paths from (0,0) to this point
    def lattice_paths_matrix(self):
        N = self.lattice_n + 1
        matrix = [ [0 for _ in range(N)] for __ in range(N) ]
        
        # Now initialize the first row and the first column
        for i in range(N):
            matrix[0][i] = 1
            matrix[i][0] = 1

        for i in range(1, N):
            for j in range(1, N):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

        return matrix


    def lattice_paths_beta(self):
        matrix = self.lattice_paths_matrix()
        # print matrix
        return matrix[-1][-1]


if __name__ == "__main__":
#    s = Solution(3)
#    path = []
#    total_paths = []
#    s.lattice_path_print((0, 0), path, total_paths)
#    # print total_paths
#    s = Solution(2)
#    s.lattice_paths_alpha((0, 0))
#    print s.lattice_path_count
    s = Solution(20)
    print s.lattice_paths_beta()


