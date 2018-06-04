import functools as ft
class Perceptron(object):
    def __init__(self, input_num, activator):
        """
        初始化感知器
        """
        self.activator = activator
        # 权重向量初始化为0
        self.weights = [0.0 for _ in range(input_num)]
        # 偏置项初始化为0
        self.bias = 0.0

    def __str__(self):
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)

    def predict(self, input_vec):
        """
        输入向量，输入感知器的计算结果
        """
        return self.activator(ft.reduce(lambda a, b : a + b , map(lambda x_w:x_w[0]*x_w[1], zip(input_vec, self.weights)),
                                     0.0) + self.bias )


    def train(self, input_vecs, labels, iteration, rate):
        """
        输入训练数据：一组向量，与每个向量对应的label;以及训练轮数，学习率
        """
        for i in  range(iteration):
            self._one_iteration(input_vecs, labels, rate)

    def _one_iteration(self, input_vecs, labels, rate):
        """
        一次迭代，把所有训练数据过一遍
        """
        samples = zip(input_vecs, labels)
        # 对每个样本，按照感知器规则更新权重
        for (input_vecs, label) in samples:
            # 计算感知器在当前权重下的输出
            output = self.predict(input_vecs)
            self._update_weights(input_vecs, output, label, rate)

    def _update_weights(self, input_vec, output, label, rate):
        """
        按照感知器规则更新权重
        """
        delta = label - output
        self.weights = map(lambda x_w :x_w[1] + rate* delta * x_w[0],  zip(input_vec, self.weights))
        self.bias += rate * delta