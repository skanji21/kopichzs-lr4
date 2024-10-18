
import numpy as np

def find_positive_columns(matrix):
    """Находит номера столбцов с только положительными элементами в матрице."""
    return [col for col in range(matrix.shape[1]) if np.all(matrix[:, col] > 0)]

def main():
    # Генерация двумерных массивов размером до 10x10
    matrices = [np.random.uniform(-10, 10, (np.random.randint(1, 11), np.random.randint(1, 11))) for _ in range(2)]
    
    for i, matrix in enumerate(matrices, start=1):
        print(f"\nМатрица {i}:\n{matrix}")
        positive_columns = find_positive_columns(matrix)
        print(f"Номера столбцов с положительными элементами: {positive_columns or 'нет'}.")

if __name__ == "__main__":
    main()
