import networkx as nx
import matplotlib.pyplot as plt
import hierarchy_pos as hp

g = nx.Graph()
# g.add_edge('a1','a2')
# g.add_edge('a1','a3')
# g.add_edge('a2','a3')
# g.add_edge('a3','b1')
# g.add_edge('b1','b2')
# g.add_edge('b3','b2')
# g.add_edge('b3','b4')
# g.add_edge('b1','b4')

g.add_edges_from([('a1', 'a2'), ('a1', 'a3'), ('a2', 'a3'),
                  ('a3', 'b1'), ('b1', 'b2'), ('b1', 'b4'),
                  ('b2', 'b3'), ('b3', 'b4')])
print(g.edges)
print(g.nodes)
print(g.degree['a3'])
print(g.adj['a3'])

class EntropyGraph:
    def __init__(self, G):
        self.graph = G
        self.encoding_tree = self.init_encoding_tree()
        self.degree_dist = {}
        '''度数分布记录格式：'''
        self.community = {}


    # 加边
    def add_edge(self, e):
        self.graph.add_edge(*e) # 元组解包

    # 打印图
    def print_graph(self):
        fig, ax = plt.subplots()
        nx.draw(self.graph, ax=ax, with_labels=True)
        plt.show()

    # 打印当前编码树
    def print_encoding_tree(self):
        fig, ax = plt.subplots()
        pos = hp.hierarchy_pos(self.encoding_tree, 'root')
        nx.draw(self.encoding_tree, ax=ax, with_labels=True, pos=pos)
        plt.show()

    # 初始化编码树
    def init_encoding_tree(self):
        # self.encoding_tree = nx.tree_graph()
        T = nx.Graph()
        for node in self.graph.nodes:
            T.add_edge('root', node)
        return T

    def generate_kdim_encoding_tree(self, dim):
        if dim ==1 :

            pass

    # 统计节点度分布
    def statistic_degree(self):

        pass



    # 贪心结构熵极小化算法
    def calc_best_encoding_tree_greedy(self):
        pass

    # 融合算子
    def merging_operator(self):
        pass

    # 联合算子
    def combining_operator(self):
        pass

    # 计算T确定的结构熵主函数
    def calc_SE(self, T, dim):
        # 一维结构熵
        if dim == 1:


            pass

    # 计算T确定的节点结构熵
    def calc_single_node_SE(self):
        pass

    # 计算社区alpha的容量
    def calc_volume(self, alpha):
        pass

    # 获取alpha的父节点
    def get_parent(self, alpha):
        pass


eg = EntropyGraph(g)
eg.print_graph()
eg.print_encoding_tree()

