#тесты для Алгоритма упорядочения дуг сети по начальной вершине

import unittest
from Algorithm1 import Graph  # Импортируем класс Graph из файла Topic1.py

class TestGraphAlgorithm(unittest.TestCase):
    def setUp(self):
        """
        Инициализация графа для тестирования.
        """
        self.graph = Graph(5)  # Создаем граф с 5 вершинами

    def test_add_edge(self):
        """
        Тест добавления дуг в граф.
        """
        self.graph.add_edge(1, 2, 10)
        self.graph.add_edge(3, 4, 5)
        self.assertEqual(len(self.graph.edges), 2)
        self.assertEqual(self.graph.edges[0].start, 1)
        self.assertEqual(self.graph.edges[1].weight, 5)

    def test_sort_edges_by_start(self):
        """
        Тест сортировки дуг по начальной вершине.
        """
        self.graph.add_edge(3, 4, 10)
        self.graph.add_edge(1, 2, 5)
        self.graph.add_edge(2, 3, 8)
        self.graph.sort_edges_by_start()
        starts = [edge.start for edge in self.graph.edges]
        self.assertEqual(starts, [1, 2, 3])

    def test_sort_edges_by_weight(self):
        """
        Тест сортировки дуг по весу, включая обработку отсутствующих весов.
        """
        self.graph.add_edge(1, 2, 10)
        self.graph.add_edge(3, 4)  # Без веса
        self.graph.add_edge(2, 3, 5)
        self.graph.sort_edges_by_weight()
        weights = [edge.weight if edge.weight is not None else float('inf') for edge in self.graph.edges]
        self.assertEqual(weights, [5, 10, float('inf')])

    def test_group_edges_by_start(self):
        """
        Тест группировки дуг по начальной вершине.
        """
        self.graph.add_edge(1, 2, 10)
        self.graph.add_edge(3, 4, 5)
        self.graph.add_edge(1, 3, 8)
        grouped_edges = {}
        for edge in self.graph.edges:
            grouped_edges.setdefault(edge.start, []).append(edge)

        self.assertEqual(len(grouped_edges[1]), 2)  # У вершины 1 должно быть 2 дуги
        self.assertEqual(grouped_edges[3][0].end, 4)  # У вершины 3 одна дуга к вершине 4

    def test_empty_graph(self):
        """
        Тест для графа без дуг.
        """
        self.assertEqual(len(self.graph.edges), 0)
        self.graph.sort_edges_by_start()  # Сортировка не должна вызывать ошибок
        self.graph.sort_edges_by_weight()  # Сортировка по весу также должна быть безопасной

    def test_duplicate_edges(self):
        """
        Тест добавления одинаковых дуг.
        """
        self.graph.add_edge(1, 2, 10)
        self.graph.add_edge(1, 2, 10)
        self.assertEqual(len(self.graph.edges), 2)  # Дублирующиеся дуги допускаются

    def test_large_graph(self):
        """
        Тест производительности на большом графе.
        """
        for i in range(1000):
            self.graph.add_edge(i, (i + 1) % 1000, i)
        self.graph.sort_edges_by_start()
        self.assertEqual(self.graph.edges[0].start, 0)
        self.assertEqual(len(self.graph.edges), 1000)

if __name__ == "__main__":
    unittest.main()