#Алгоритм упорядочения дуг сети по начальной вершине

class Edge:
    """Класс, представляющий дугу графа."""
    def __init__(self, start, end, weight=None):
        """
        Инициализация дуги.
        :param start: Начальная вершина дуги.
        :param end: Конечная вершина дуги.
        :param weight: Вес дуги (по умолчанию None).
        """
        self.start = start  # Начальная вершина
        self.end = end      # Конечная вершина
        self.weight = weight  # Вес дуги, если имеется

    def __repr__(self):
        """Строковое представление дуги для вывода."""
        return f"({self.start} -> {self.end}, weight: {self.weight})"

class Graph:
    """Класс, представляющий граф."""
    def __init__(self, num_vertices):
        """
        Инициализация графа.
        :param num_vertices: Количество вершин в графе.
        """
        self.num_vertices = num_vertices  # Количество вершин в графе
        self.edges = []  # Список всех дуг в графе

    def add_edge(self, start, end, weight=None):
        """
        Метод для добавления дуги в граф.
        :param start: Начальная вершина дуги.
        :param end: Конечная вершина дуги.
        :param weight: Вес дуги (по умолчанию None).
        """
        new_edge = Edge(start, end, weight)  # Создаём новую дугу
        self.edges.append(new_edge)  # Добавляем дугу в список

    def sort_edges_by_start(self):
        """Сортировка дуг по начальной вершине."""
        # Сортируем дуги по начальной вершине с использованием стандартной сортировки
        self.edges.sort(key=lambda edge: edge.start)

    def sort_edges_by_weight(self):
        """Сортировка дуг по весу."""
        # Сортируем дуги по весу. Если вес не задан, присваиваем вес "бесконечность".
        self.edges.sort(key=lambda edge: edge.weight if edge.weight is not None else float('inf'))

    def display_edges(self):
        """Вывод всех дуг графа."""
        if not self.edges:
            print("Граф не содержит дуг.")
            return
        # Выводим все дуги в графе
        for edge in self.edges:
            print(edge)

    def display_edges_grouped(self):
        """Группировка дуг по начальной вершине и вывод по группам."""
        grouped_edges = {}  # Словарь для группировки дуг по начальной вершине
        # Проходим по всем дугам и группируем их по начальной вершине
        for edge in self.edges:
            if edge.start not in grouped_edges:
                grouped_edges[edge.start] = []  # Если ещё нет группы для данной вершины, создаём её
            grouped_edges[edge.start].append(edge)  # Добавляем дугу в соответствующую группу

        # Выводим группированные дуги по начальной вершине
        for start, edges in grouped_edges.items():
            print(f"Начальная вершина {start}:")
            for edge in edges:
                print(f"  {edge}")

# Пример использования
graph = Graph(5)  # Создаём граф с 5 вершинами

# Добавляем дуги с указанием начальной и конечной вершины, а также веса
graph.add_edge(2, 4, 10)
graph.add_edge(1, 3, 5)
graph.add_edge(2, 5, 2)
graph.add_edge(1, 2, 8)
graph.add_edge(3, 4, 7)
graph.add_edge(3, 5, 6)

# Вывод исходных дуг (без сортировки)
print("Исходные дуги:")
graph.display_edges()  # Отображаем все дуги до сортировки
print("\n")

# Сортировка дуг по начальной вершине
graph.sort_edges_by_start()  # Сортируем дуги по начальной вершине
print("Дуги, отсортированные по начальной вершине:")
graph.display_edges()  # Отображаем отсортированные дуги
print("\n")

# Сортировка дуг по весу
graph.sort_edges_by_weight()  # Сортируем дуги по весу
print("Дуги, отсортированные по весу:")
graph.display_edges()  # Отображаем дуги после сортировки по весу
print("\n")

# Группировка дуг по начальной вершине
graph.display_edges_grouped()  # Группируем дуги по начальной вершине и выводим